"""Exact Gaussian normalization for the interior square-root multinomial LCLT."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    n = sp.symbols("n", positive=True)
    p1, p2, p3 = sp.symbols("p1 p2 p3", positive=True)
    matrix = sp.Matrix(
        [[1 / p1 + 1 / p3, 1 / p3], [1 / p3, 1 / p2 + 1 / p3]]
    )
    det_matrix = sp.factor(matrix.det())
    raw_matrix = matrix / n
    # The square of the leading amplitude times the 2D Gaussian integral.
    prefactor = 1 / (2 * sp.pi * n * sp.sqrt(p1 * p2 * p3))
    gaussian_integral = 2 * sp.pi / sp.sqrt(raw_matrix.det())
    normalization = sp.simplify(prefactor * gaussian_integral)
    sample = {p1: sp.Rational(1, 2), p2: sp.Rational(1, 3), p3: sp.Rational(1, 6)}
    normalization_on_simplex = sp.simplify(normalization.subs(p3, 1 - p1 - p2))
    sample_normalization = sp.simplify(normalization.subs(sample))
    epsilon = sp.Rational(1, 12)
    raw_deviation_exponent = sp.Rational(1, 2) + epsilon
    remainder_exponent = sp.simplify(3 * epsilon - sp.Rational(1, 2))
    payload = {
        "det_constraint_plane_matrix": str(det_matrix),
        "normalization_symbolic": str(normalization),
        "normalization_on_p_simplex": str(normalization_on_simplex),
        "normalization_sample": str(sample_normalization),
        "parity_sublattice_density": "1/4",
        "epsilon": str(epsilon),
        "raw_deviation_exponent": str(raw_deviation_exponent),
        "standardized_deviation_exponent": str(epsilon),
        "log_stirling_remainder_exponent": str(remainder_exponent),
        "normalization_exact": normalization_on_simplex == 1 and sample_normalization == 1,
        "marker": "INTERIOR_HELLINGER_LCLT_NORMALIZATION_CERTIFIED" if normalization_on_simplex == 1 else "FAILED",
    }
    (RESULTS / "interior_lclt.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("LCLT_DET", det_matrix)
    print("LCLT_NORMALIZATION", normalization)
    print("LCLT_PARITY_DENSITY", "1/4")


if __name__ == "__main__":
    main()
