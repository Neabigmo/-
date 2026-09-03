from __future__ import annotations

import math
import numpy as np

from coherence_lift import odd_indices
from outer_minimax import CoherentObjective, _active_signature

QLOW = 0.05
QHIGH = 0.10
RIDGE = 1e-11


def gradient_spot_check_retry3(obj, y, max_dirs=8, h=8e-7, min_dirs=2):
    """Strict interior FD audit with per-direction numerical rejection.

    Every USED direction requires valid +/- evaluations, unchanged objective
    branch, and unchanged NNQP active set. A failed NNQP perturbation rejects
    only that direction. The point is stable only if at least min_dirs strict
    directions remain. No failed qp.success result can be counted as stable.
    """
    y = np.asarray(y, float)
    try:
        base = obj.evaluate(y)
    except Exception as exc:
        return dict(status="BASE_EXCEPTION", error=math.nan, count=0, attempted=0,
                    rejected_numeric=0, rejected_branch=0, rejected_active=0,
                    active_stable=False, exception=repr(exc))

    if not base.scientific_valid or base.grad is None or not np.all(np.isfinite(base.grad)):
        return dict(status="INVALID_BASE", error=math.nan, count=0, attempted=0,
                    rejected_numeric=0, rejected_branch=0, rejected_active=0,
                    active_stable=False)

    slack = 5.0 - float(y @ y)
    if slack <= max(1e-5, 20 * h * (1 + np.linalg.norm(y))):
        return dict(status="BOUNDARY_SKIPPED", error=math.nan, count=0, attempted=0,
                    rejected_numeric=0, rejected_branch=0, rejected_active=0,
                    active_stable=False)

    sig0 = _active_signature(base.qp)
    errs = []
    attempted = rejected_numeric = rejected_branch = rejected_active = 0

    for j in range(min(len(y), max_dirs)):
        attempted += 1
        step = h * (1 + abs(float(y[j])))
        yp = y.copy(); ym = y.copy()
        yp[j] += step; ym[j] -= step
        try:
            ep = obj.evaluate(yp); em = obj.evaluate(ym)
        except (FloatingPointError, np.linalg.LinAlgError, RuntimeError):
            rejected_numeric += 1
            continue
        if not (ep.scientific_valid and em.scientific_valid):
            rejected_numeric += 1
            continue
        if ep.status != base.status or em.status != base.status:
            rejected_branch += 1
            continue
        if base.qp is not None:
            if _active_signature(ep.qp) != sig0 or _active_signature(em.qp) != sig0:
                rejected_active += 1
                continue
        fd = (ep.value - em.value) / (2 * step)
        an = float(base.grad[j])
        if not (np.isfinite(fd) and np.isfinite(an)):
            rejected_numeric += 1
            continue
        errs.append(abs(fd - an) / (1 + abs(fd) + abs(an)))

    try:
        obj.evaluate(y)
    except Exception:
        pass

    used = len(errs)
    meta = dict(count=used, attempted=attempted, rejected_numeric=rejected_numeric,
                rejected_branch=rejected_branch, rejected_active=rejected_active)
    if used < int(min_dirs):
        return dict(status="INSUFFICIENT_STABLE_DIRECTIONS", error=math.nan,
                    active_stable=False, **meta)
    return dict(status="CHECKED_STABLE_ACTIVE_SET", error=float(max(errs)),
                active_stable=True, **meta)


def _candidate_stream(N, rng, max_trials=64):
    dim = len(odd_indices(N))
    yield "zero", np.zeros(dim, float)
    if dim == 0:
        return
    amps = (1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4,
            1e-3, 2e-3, 3e-3, 1e-2, 2e-2, 3e-2, 4e-2, 7e-2)
    coords = []
    for j in (0, dim // 4, dim // 2, (3 * dim) // 4, dim - 1):
        if j not in coords:
            coords.append(j)
    emitted = 1
    for k, amp in enumerate(amps):
        if emitted >= max_trials:
            return
        j = coords[k % len(coords)]
        y = np.zeros(dim, float)
        y[j] = amp * (-1.0 if k % 2 else 1.0)
        yield f"coord_{j}_a{amp:.0e}", y
        emitted += 1
        if emitted >= max_trials:
            return
        z = rng.normal(size=dim)
        z /= max(np.linalg.norm(z), 1e-300)
        yield f"random_a{amp:.0e}_{k}", z * amp
        emitted += 1


def gradient_audit_rows_retry3(W, Ns, target_stable=5, max_trials=64):
    """Adaptive strict preflight with explicit active-tail coverage."""
    rows = []
    rng = np.random.default_rng(27112026)

    for N in Ns:
        obj = CoherentObjective(N, W, q_low=QLOW, q_high=QHIGH, A=5, ridge=RIDGE, dps=180)
        stable_count = 0
        active_tail_stable = 0

        for trial, (name, y) in enumerate(_candidate_stream(N, rng, max_trials=max_trials)):
            try:
                ev = obj.evaluate(y)
            except Exception as exc:
                rows.append(dict(N=N, test=name, trial=trial, status="GRADIENT_TEST_EXCEPTION",
                                 grad_fd_error=math.nan, checked_directions=0, attempted_directions=0,
                                 rejected_numeric=0, rejected_branch=0, rejected_active=0,
                                 scientific_valid=False, eval_status="EXCEPTION", prefix_energy=math.nan,
                                 tail_lb=math.nan, active_count=math.nan, tail_regime_signal=False,
                                 ball_slack=5.0-float(y@y), qp_success=False, error=repr(exc)))
                continue

            qp_success = bool(ev.qp is None or getattr(ev.qp, "success", False))
            active_count = int(getattr(ev.qp, "active_count", 0)) if ev.qp is not None else 0
            tail_lb = float(ev.tail_lb) if np.isfinite(ev.tail_lb) else math.nan
            tail_signal = bool(active_count > 0 or (np.isfinite(tail_lb) and abs(tail_lb) > 1e-8))

            if not ev.scientific_valid or not qp_success:
                rows.append(dict(N=N, test=name, trial=trial, status="NNQP_REJECTED",
                                 grad_fd_error=math.nan, checked_directions=0, attempted_directions=0,
                                 rejected_numeric=0, rejected_branch=0, rejected_active=0,
                                 scientific_valid=False, eval_status=ev.status,
                                 prefix_energy=(float(ev.prefix_energy) if np.isfinite(ev.prefix_energy) else math.nan),
                                 tail_lb=tail_lb, active_count=active_count, tail_regime_signal=tail_signal,
                                 ball_slack=5.0-float(y@y), qp_success=False,
                                 error="base QP not strictly successful"))
                continue

            # Once five general stable points exist, continue scanning only until
            # a genuinely active-tail stable point is also validated.
            if stable_count >= target_stable and active_tail_stable >= 1:
                break

            gc = gradient_spot_check_retry3(obj, y, max_dirs=min(8, len(y)), h=8e-7, min_dirs=2)
            rows.append(dict(N=N, test=name, trial=trial, status=gc["status"],
                             grad_fd_error=gc["error"], checked_directions=gc["count"],
                             attempted_directions=gc.get("attempted", 0),
                             rejected_numeric=gc.get("rejected_numeric", 0),
                             rejected_branch=gc.get("rejected_branch", 0),
                             rejected_active=gc.get("rejected_active", 0),
                             scientific_valid=bool(ev.scientific_valid), eval_status=ev.status,
                             prefix_energy=float(ev.prefix_energy), tail_lb=tail_lb,
                             active_count=active_count, tail_regime_signal=tail_signal,
                             ball_slack=5.0-float(y@y), qp_success=qp_success,
                             error=gc.get("exception", "")))
            if gc["status"] == "CHECKED_STABLE_ACTIVE_SET":
                stable_count += 1
                if tail_signal:
                    active_tail_stable += 1

    return rows
