#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PATCH = Path(__file__).resolve().parent
REPO = PATCH.parent
PKG_ROOT = REPO / "chi2_n3_ou_coherent_stage27u_retry2_2026-09-03"
PKG_PY = PKG_ROOT / "python"
sys.path.insert(0, str(PKG_PY))


def _truthy(series):
    return series.astype(str).str.lower().isin(["true", "1"])


def retry3_gradient_audit(result_dir: Path):
    p = result_dir / "stage27u_gradient_audit.csv"
    if not p.exists():
        raise AssertionError("missing stage27u_gradient_audit.csv")
    g = pd.read_csv(p)

    required = {
        "N", "status", "grad_fd_error", "checked_directions",
        "scientific_valid", "qp_success", "tail_regime_signal",
        "active_count", "tail_lb",
    }
    missing = required - set(g.columns)
    if missing:
        raise AssertionError(f"gradient audit missing columns: {sorted(missing)}")

    stable = g[g.status.astype(str) == "CHECKED_STABLE_ACTIVE_SET"]
    for N in (32, 48, 64, 80):
        gn = stable[stable.N.astype(int) == N]
        if len(gn) < 2:
            raise AssertionError((N, "too few retry3 stable gradient points", len(gn)))
        if not _truthy(gn.scientific_valid).all():
            raise AssertionError((N, "stable row not scientific_valid"))
        if not _truthy(gn.qp_success).all():
            raise AssertionError((N, "stable row without strict qp_success"))

        dirs = pd.to_numeric(gn.checked_directions, errors="coerce")
        if dirs.isna().any() or not (dirs >= 2).all():
            raise AssertionError((N, "stable row has fewer than two strict FD directions"))

        err = pd.to_numeric(gn.grad_fd_error, errors="coerce")
        if err.isna().any() or not np.isfinite(err.to_numpy(float)).all():
            raise AssertionError((N, "nonfinite stable gradient error"))
        if float(err.max()) >= 2e-3:
            raise AssertionError((N, "gradient error threshold violated", float(err.max())))

        tail_signal = _truthy(gn.tail_regime_signal)
        active = pd.to_numeric(gn.active_count, errors="coerce").fillna(0) > 0
        tail_lb = pd.to_numeric(gn.tail_lb, errors="coerce").fillna(0).abs() > 1e-8
        if not bool((tail_signal & (active | tail_lb)).any()):
            raise AssertionError((N, "no stable nontrivial-tail gradient check"))

    # Diagnostic exception/rejection rows are allowed in preflight, but they
    # can never count toward stable coverage. No +/-Inf is allowed anywhere.
    for c in g.columns:
        z = pd.to_numeric(g[c], errors="coerce").dropna().to_numpy(float)
        if len(z) and np.isinf(z).any():
            raise AssertionError(f"gradient audit contains +/-Inf in {c}")


def run_retry2_audit(result_dir: Path):
    # Reuse the original independent artifact replay/failure audit unchanged.
    import audit_stage27u_results as old_audit
    saved = sys.argv[:]
    try:
        sys.argv = ["audit_stage27u_results.py", "--result-dir", str(result_dir)]
        old_audit.main()
    finally:
        sys.argv = saved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--result-dir", required=True)
    a = ap.parse_args()
    result_dir = Path(a.result_dir)
    retry3_gradient_audit(result_dir)
    run_retry2_audit(result_dir)
    print("STAGE27U_RETRY3_NUMERIC_AUDIT_OK")


if __name__ == "__main__":
    main()
