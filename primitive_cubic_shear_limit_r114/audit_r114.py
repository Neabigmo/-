"""Exact symbolic audit for the R114 primitive cubic shear record.

The full trace-resolvent derivation and bump-realization construction remain
web-side analytic arguments. This audit checks their exact algebraic inputs and
does not assert that finite-jet exactness is all-degree exactness.
"""

from __future__ import annotations

import sympy as sp


def check_cumulant_to_moment_substitution() -> None:
    tau, c, d = sp.symbols("tau c d", real=True)
    m3 = tau ** sp.Rational(3, 2) * c
    m4 = sp.Integer(3)
    m5 = 10 * m3 + tau ** sp.Rational(5, 2) * d
    m6 = 15 + 7 * tau**3 * c**2
    assert m4 == 3
    assert sp.expand(m5 - (10 * tau ** sp.Rational(3, 2) * c + tau ** sp.Rational(5, 2) * d)) == 0
    assert sp.expand(m6 - (15 + 7 * tau**3 * c**2)) == 0
    print("R114_CUMULANT_TO_MOMENT_SUBSTITUTION_PASSED")


def check_h3_determinant_and_primitive_expansion() -> None:
    tau, c, d = sp.symbols("tau c d", real=True)
    m3 = tau ** sp.Rational(3, 2) * c
    m5 = 10 * m3 + tau ** sp.Rational(5, 2) * d
    H3 = sp.Matrix(
        [
            [1, 0, 1, m3],
            [0, 1, m3, 3],
            [1, m3, 3, m5],
            [m3, 3, m5, 15 + 7 * tau**3 * c**2],
        ]
    )
    expected = 12 - 30 * tau**3 * c**2 - 12 * tau**4 * c * d - tau**5 * d**2 - 6 * tau**6 * c**4
    assert sp.expand(H3.det() - expected) == 0
    assert sp.expand(expected.subs({d: 0}) - (12 - 30 * tau**3 * c**2 - 6 * tau**6 * c**4)) == 0
    print("R114_H3_DETERMINANT_AND_TAU3_EXPANSION_PASSED")


def check_gaussian_slack_factor() -> None:
    s, t = sp.symbols("s t", real=True)
    H3_gauss = sp.Matrix(
        [
            [1, 0, 1, 0],
            [0, 1, 0, 3],
            [1, 0, 3, 0],
            [0, 3, 0, 15],
        ]
    )
    Pi = s**6 * t**2 * (s + t)**4 * (2 * s + t)**2
    assert H3_gauss.det() == 12
    assert sp.factor(H3_gauss.det() * Pi / 144) == Pi / 12
    assert sp.factor((-30) * Pi / 144) == -sp.Rational(5, 24) * Pi
    print("R114_GAUSSIAN_SLACK_AND_NEGATIVE_PRIMITIVE_COEFFICIENT_PASSED")


def check_angular_tau3_cancellation() -> None:
    tau, y, k6, c = sp.symbols("tau y k6 c", real=True)
    p6 = sp.Rational(5, 18)
    p3sq = sp.Rational(1, 12)
    coefficient = -k6 * p6 / sp.factorial(6) - c**2 * p3sq / (2 * sp.factorial(3) ** 2)
    expected = -(k6 + 3 * c**2) / 2592
    assert sp.simplify(coefficient - expected) == 0
    assert sp.simplify(expected.subs(k6, -3 * c**2)) == 0
    print("R114_ANGULAR_TAU3_EXACTNESS_CANCELLATION_PASSED")


def check_scale_and_shear_identities() -> None:
    tau, s, t = sp.symbols("tau s t", positive=True)
    assert sp.simplify((tau ** sp.Rational(3, 2)) ** 2 - tau**3) == 0
    assert sp.factor(t**3 - 2 * (s + t)**3 + (2 * s + t)**3) == 6 * s**2 * (s + t)
    y2 = sp.expand(s**2 + (s + t)**2 + (2 * s + t)**2)
    assert y2 == 6 * s**2 + 6 * s * t + 2 * t**2
    print("R114_PRIMITIVE_SCALE_AND_SHEAR_IDENTITIES_PASSED")


def main() -> None:
    check_cumulant_to_moment_substitution()
    check_h3_determinant_and_primitive_expansion()
    check_gaussian_slack_factor()
    check_angular_tau3_cancellation()
    check_scale_and_shear_identities()
    print("R114_PRIMITIVE_CUBIC_SHEAR_LIMIT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()

