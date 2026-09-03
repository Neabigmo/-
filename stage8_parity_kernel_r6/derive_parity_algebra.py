"""Exact symbolic replay of the parity Hadamard factorisation."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    e1, e2, e3, o1, o2, o3 = sp.symbols("E1 E2 E3 O1 O2 O3")
    s1, s2, s3 = sp.symbols("s1 s2 s3")
    lhs = e1 * e2 * e3 + s2 * s3 * e1 * o2 * o3
    lhs += s1 * s3 * o1 * e2 * o3 + s1 * s2 * o1 * o2 * e3
    rhs = sp.Rational(1, 2) * (
        (e1 + s1 * o1) * (e2 + s2 * o2) * (e3 + s3 * o3)
        + (e1 - s1 * o1) * (e2 - s2 * o2) * (e3 - s3 * o3)
    )
    residual = sp.expand(lhs - rhs)
    gaussian_residual = sp.expand((lhs - rhs).subs({o1: 0, o2: 0, o3: 0}))
    payload = {
        "identity_residual": str(residual),
        "gaussian_replay_residual": str(gaussian_residual),
        "factorization_exact": residual == 0,
        "strict_positive_condition": "all E_j > abs(O_j)",
        "marker": "PARITY_HADAMARD_FACTORIZATION_CERTIFIED" if residual == 0 else "FAILED",
    }
    (RESULTS / "parity_algebra.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("PARITY_IDENTITY_RESIDUAL", residual)


if __name__ == "__main__":
    main()
