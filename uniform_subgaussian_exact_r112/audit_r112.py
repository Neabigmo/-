"""Exact symbolic audit for the R112 uniform envelope theorem.

The probability-law identification Q ~ chi^2_2 is an analytic input from the
genuine exact angular realization.  This audit checks the deterministic
inequality, Jensen curvature, explicit constants, and the OU/ellipse algebra.
"""

from __future__ import annotations

import sympy as sp


def check_pair_difference_identity() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    mean = (x1 + x2 + x3) / 3
    Q = sp.expand((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2)
    D = x1 - x2
    assert sp.factor(2 * Q - D**2) == (x1 + x2 - 2 * x3)**2 / 3
    print("R112_PAIR_DIFFERENCE_SQUARE_IDENTITY_PASSED")


def check_jensen_curvature() -> None:
    a, x = sp.symbols("a x", positive=True)
    curvature = sp.factor(sp.diff(sp.exp(a * x**2), x, 2))
    assert curvature == 2 * a * (1 + 2 * a * x**2) * sp.exp(a * x**2)
    print("R112_JENSEN_STRICT_CONVEXITY_PASSED")


def check_envelope_constants() -> None:
    a = sp.Rational(1, 8)
    assert sp.simplify(1 / (1 - 4 * a)) == 2
    rho_sq = sp.E / 128
    r_sq = sp.E / 512
    assert sp.simplify(r_sq - rho_sq / 4) == 0
    C = 2 * 2**21 * sp.log(2) / sp.E**3
    assert sp.simplify(C - 2**22 * sp.log(2) / sp.E**3) == 0
    print("R112_EXPLICIT_ENVELOPE_CONSTANTS_PASSED")


def check_ellipse_and_q3n_scaling() -> None:
    q, N, s, t = sp.symbols("q N s t", positive=True)
    radii = (s, s + t, 2 * s + t)
    y2 = sp.expand(sum(r**2 for r in radii))
    assert y2 == 6 * s**2 + 6 * s * t + 2 * t**2
    x1, x2, x3 = sp.symbols("x1 x2 x3", nonnegative=True)
    power_gap = sp.Poly(
        sp.expand((x1 + x2 + x3)**3 - (x1**3 + x2**3 + x3**3)),
        x1, x2, x3,
    )
    assert all(coefficient >= 0 for coefficient in power_gap.coeffs())
    assert sp.simplify((q**(N / 2))**6 - q**(3 * N)) == 0
    print("R112_ELLIPSE_AND_Q3N_SCALING_PASSED")


def main() -> None:
    check_pair_difference_identity()
    check_jensen_curvature()
    check_envelope_constants()
    check_ellipse_and_q3n_scaling()
    print("R112_UNIFORM_SUBGAUSSIAN_EXACT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
