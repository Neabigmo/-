#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np

PATCH = Path(__file__).resolve().parent
REPO = PATCH.parent
PKG_PY = REPO / "chi2_n3_ou_coherent_stage27u_retry2_2026-09-03" / "python"
sys.path.insert(0, str(PKG_PY))
sys.path.insert(0, str(PATCH))

from gradient_audit_retry3 import gradient_spot_check_retry3


class PartialBadObjective:
    """Quadratic objective with one deliberately invalid FD coordinate."""

    def evaluate(self, y):
        y = np.asarray(y, float)
        # Coordinate 0 perturbations emulate a failed NNQP solve.
        if abs(float(y[0])) > 1e-12:
            raise FloatingPointError("synthetic invalid NNQP perturbation")
        return SimpleNamespace(
            scientific_valid=True,
            grad=2.0 * y,
            status="FINITE_TAIL",
            qp=SimpleNamespace(alpha=np.asarray([1.0])),
            value=float(y @ y),
        )


def main():
    obj = PartialBadObjective()
    y = np.zeros(3, float)
    g = gradient_spot_check_retry3(obj, y, max_dirs=3, h=1e-6, min_dirs=2)
    assert g["status"] == "CHECKED_STABLE_ACTIVE_SET", g
    assert g["count"] == 2, g
    assert g["attempted"] == 3, g
    assert g["rejected_numeric"] == 1, g
    assert np.isfinite(g["error"]) and g["error"] < 1e-10, g
    print("STAGE27U_RETRY3_PATCH_SELFTEST_OK")


if __name__ == "__main__":
    main()
