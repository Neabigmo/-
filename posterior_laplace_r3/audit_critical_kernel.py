from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import result_dir


def main():
    # One exact symmetric two-point prior: mu=(delta_-1+delta_+1)/2, v=r=1,
    # evaluated at y=0.  Here f=P_v mu is genuinely heat-smoothed.
    k = sp.Rational(1, 2)*sp.exp(-sp.Rational(3, 4)) + sp.Rational(3, 2)*sp.exp(-sp.Rational(17, 12))
    gaussian_lower_bound = sp.Rational(3, 2)  # 1+r/(1+v), the Gaussian value.
    # e^(-3/4)<1 and e^(-17/12)<1/2 (because 17/12>log 2), hence k<5/4<3/2.
    assert k < sp.Rational(5, 4)
    assert k < gaussian_lower_bound
    out = {
        "status": "EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE",
        "prior": "(delta_-1+delta_+1)/2",
        "v": 1,
        "r": 1,
        "y": 0,
        "exact_K": "(1/2)*exp(-3/4)+(3/2)*exp(-17/12)",
        "gaussian_equality_value": "3/2",
        "strict_exact_comparison": "K < 5/4 < 3/2",
        "tested_mechanism": "universal Gaussian-equality lower bound K_{v,r}f >= K_Gaussian",
        "warning": "This refutes only the tested one-sided kernel inequality; it is not a counterexample to the original characterization.",
    }
    path = result_dir() / "critical_kernel_audit.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE_VERIFIED", path)


if __name__ == "__main__":
    main()
