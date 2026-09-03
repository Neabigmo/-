from __future__ import annotations

import hashlib
import json
import math

import mpmath as mp
import numpy as np

PRUNE_RECORDS = []
_SEEN = set()
CERT_MARGIN = 25.0
FAST_TRIGGER = 10.0
MAX_MP_WITNESSES = 4
MP_DPS_LOW = 220
MP_DPS_HIGH = 300
MP_REL_TOL = 1e-10
CONSERVATIVE_SHRINK = 1e-12


class CertifiedSingleWitnessPrune(FloatingPointError):
    def __init__(self, cert, eval_result):
        super().__init__(
            f"POINTWISE_SINGLE_WITNESS_PRUNE N={cert['N']} "
            f"margin_lb_conservative={cert['margin_lb_conservative']:.17g}"
        )
        self.cert = cert
        self.eval_result = eval_result


def coordinate_dual_lb(c, diag, eps):
    c = np.asarray(c, float)
    diag = np.asarray(diag, float)
    if c.ndim != 1 or diag.shape != c.shape:
        raise ValueError("coordinate_dual_lb shape mismatch")
    if not np.isfinite(c).all() or not np.isfinite(diag).all() or not np.isfinite(eps):
        raise FloatingPointError("nonfinite coordinate dual data")
    good = diag > 0
    lbs = np.zeros_like(c)
    neg = np.minimum(c, 0.0)
    lbs[good] = (neg[good] * neg[good]) / (diag[good] * float(eps) * float(eps))
    j = int(np.argmax(lbs)) if len(lbs) else -1
    return (float(lbs[j]) if j >= 0 else 0.0), j, lbs


def single_witness_mp_lb(q, N, u, witness, ridge=1e-11, dps=260):
    from joint_tail_core import scaled_hermites_mp, full_cross_kernel_mp
    from reduced_core import ReducedProblem
    old = mp.mp.dps
    mp.mp.dps = int(dps)
    try:
        qmp = mp.mpf(str(float(q)))
        lam = mp.mpf(str(float(witness[0])))
        s = mp.mpf(str(float(witness[1])))
        prob = ReducedProblem(int(N), 3, int(N) * float(q), scale=.30)
        eps = mp.mpf(str(float(prob.eps)))
        g = scaled_hermites_mp(qmp, lam, s, int(N))
        tail2 = full_cross_kernel_mp(qmp, lam, s, lam, s) - mp.fsum(
            g[n] * g[n] for n in range(int(N) + 1)
        )
        if not mp.isfinite(tail2) or tail2 <= mp.mpf('1e-100'):
            raise FloatingPointError(f"single witness tail2 invalid: {tail2}")
        d = mp.sqrt(tail2)
        um = np.asarray(u, float)
        prefix = mp.mpf(1) + eps * mp.fsum(
            mp.mpf(str(float(um[n]))) * g[n] for n in range(3, int(N) + 1)
        )
        c = prefix / d
        cjj = mp.mpf(1) + mp.mpf(str(float(ridge)))
        neg = min(c, mp.mpf(0))
        lb = (neg * neg) / (cjj * eps * eps)
        return dict(
            lb=float(lb), c=float(c), cjj=float(cjj), tail2=float(tail2),
            eps=float(eps), dps=int(dps), witness=(float(witness[0]), float(witness[1]))
        )
    finally:
        mp.mp.dps = old


def _consistent_pair(rep1, rep2):
    a = float(rep1['lb']); b = float(rep2['lb'])
    if not (np.isfinite(a) and np.isfinite(b) and a >= 0 and b >= 0):
        return None
    rel = abs(a-b) / (1.0 + abs(a) + abs(b))
    if rel > MP_REL_TOL:
        return None
    conservative = min(a, b) * (1.0 - CONSERVATIVE_SHRINK)
    return float(conservative), float(rel)


def _y_key(N, y):
    a = np.asarray(y, dtype=np.float64)
    return f"{int(N)}:" + hashlib.sha256(a.tobytes()).hexdigest()[:24]


def _record(cert):
    key = cert['key']
    if key not in _SEEN:
        _SEEN.add(key)
        PRUNE_RECORDS.append(dict(cert))


def _try_single_witness_cert(om, self, y, original_exc):
    if not str(original_exc).startswith('NNQP invalid'):
        raise original_exc
    y = np.asarray(y, float)
    cc, _J = om.complete_low_lift_high_with_jac(y, self.N, self.q_low, self.q_high)
    E = float(cc.prefix_energy_high)
    qp, joint, c = om.tail_lower_bound_prepared(self.prepared, cc.u_high)
    if qp.success or not np.isfinite(E):
        raise original_exc
    eps = float(self.prepared['prob'].eps)
    fast_lb, _j, lbs = coordinate_dual_lb(c, np.diag(joint['C']), eps)
    if E + fast_lb - self.A < FAST_TRIGGER:
        raise original_exc
    order = np.argsort(-lbs)
    best = None
    for j in order[:min(MAX_MP_WITNESSES, len(order))]:
        if lbs[j] <= 0:
            continue
        w = joint['witnesses'][int(j)]
        try:
            rep_low = single_witness_mp_lb(self.q_high, self.N, cc.u_high, w, ridge=self.ridge, dps=MP_DPS_LOW)
            rep_high = single_witness_mp_lb(self.q_high, self.N, cc.u_high, w, ridge=self.ridge, dps=max(MP_DPS_HIGH, self.dps + 80))
            pair = _consistent_pair(rep_low, rep_high)
        except Exception:
            continue
        if pair is None:
            continue
        lb_cons, rel_gap = pair
        margin = E + lb_cons - self.A
        if best is None or margin > best['margin_lb_conservative']:
            best = dict(j=int(j), witness=rep_high['witness'], c_mp_high=float(rep_high['c']),
                        cjj_mp=float(rep_high['cjj']), tail2_mp_high=float(rep_high['tail2']),
                        dual_lb_mp_low=float(rep_low['lb']), dual_lb_mp_high=float(rep_high['lb']),
                        dual_lb_conservative=float(lb_cons), mp_rel_gap=float(rel_gap),
                        dps_low=int(rep_low['dps']), dps_high=int(rep_high['dps']),
                        margin_lb_conservative=float(margin), fast_lb=float(lbs[j]))
    if best is None or best['margin_lb_conservative'] < CERT_MARGIN:
        raise original_exc
    key = _y_key(self.N, y)
    cert = dict(key=key, N=int(self.N), q_high=float(self.q_high), q_low=float(self.q_low),
                A=float(self.A), ridge=float(self.ridge), prefix_energy=E,
                fast_best_lb=float(fast_lb), witness_index=int(best['j']),
                witness_lambda=float(best['witness'][0]), witness_s=float(best['witness'][1]),
                c_mp_high=float(best['c_mp_high']), cjj_mp=float(best['cjj_mp']),
                tail2_mp_high=float(best['tail2_mp_high']),
                dual_lb_mp_low=float(best['dual_lb_mp_low']), dual_lb_mp_high=float(best['dual_lb_mp_high']),
                dual_lb_conservative=float(best['dual_lb_conservative']), mp_rel_gap=float(best['mp_rel_gap']),
                margin_lb_conservative=float(best['margin_lb_conservative']),
                dps_low=int(best['dps_low']), dps_high=int(best['dps_high']), qp_success=bool(qp.success),
                qp_reported_m2=(float(qp.m2_dual) if np.isfinite(qp.m2_dual) else math.nan),
                qp_kkt=float(qp.projected_kkt_inf), qp_comp=float(qp.complementarity_inf),
                y_json=json.dumps([float(x) for x in y]), status='POINTWISE_SINGLE_WITNESS_PRUNE')
    _record(cert)
    self.barrier_evaluations += 1
    ev = om.EvalResult(math.nan, math.nan, E, float(best['dual_lb_conservative']), cc.u_high,
                       cc.fock_residual_low, None, None, False, 'POINTWISE_SINGLE_WITNESS_PRUNE')
    raise CertifiedSingleWitnessPrune(cert, ev)


def install_retry4(om):
    if getattr(om, '_stage27u_retry4_installed', False):
        return
    original_evaluate = om.CoherentObjective.evaluate
    original_local_search = om.local_search
    def evaluate_retry4(self, y):
        try:
            return original_evaluate(self, y)
        except FloatingPointError as exc:
            return _try_single_witness_cert(om, self, y, exc)
    def local_search_retry4(obj, start, maxiter=220):
        try:
            return original_local_search(obj, start, maxiter=maxiter)
        except CertifiedSingleWitnessPrune:
            start = np.asarray(start, float)
            try:
                ev = obj.evaluate(start)
                return dict(y=start.copy(), eval=ev, success=False,
                            message='RETRY4_PRUNE_DURING_SEARCH_FALLBACK_TO_VALID_START', nit=0,
                            grad_fd_error=math.nan, grad_check_status='NOT_RUN_AFTER_PRUNE', grad_check_count=0)
            except CertifiedSingleWitnessPrune as start_pruned:
                return dict(y=start.copy(), eval=start_pruned.eval_result, success=False,
                            message='RETRY4_START_POINTWISE_SINGLE_WITNESS_PRUNED', nit=0,
                            grad_fd_error=math.nan, grad_check_status='POINTWISE_PRUNED', grad_check_count=0)
    om.CoherentObjective.evaluate = evaluate_retry4
    om.local_search = local_search_retry4
    om._stage27u_retry4_installed = True


def write_prune_csv(path):
    import pandas as pd
    cols = ['key','N','q_high','q_low','A','ridge','prefix_energy','fast_best_lb','witness_index',
            'witness_lambda','witness_s','c_mp_high','cjj_mp','tail2_mp_high','dual_lb_mp_low',
            'dual_lb_mp_high','dual_lb_conservative','mp_rel_gap','margin_lb_conservative','dps_low',
            'dps_high','qp_success','qp_reported_m2','qp_kkt','qp_comp','y_json','status']
    pd.DataFrame(PRUNE_RECORDS, columns=cols).to_csv(path, index=False)
