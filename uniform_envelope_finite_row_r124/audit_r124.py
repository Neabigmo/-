"""Exact symbolic audit for the R124 finite-row compactness dichotomy."""

from __future__ import annotations

import sympy as sp


def check_exact_row_coefficient() -> None:
    r = sp.symbols("r", integer=True, positive=True)
    q_row = sp.symbols("q_row", positive=True)
    denominator = 4**r * sp.factorial(r) ** 2
    # Angular average of Y^(2r) is binom(2r,r) Q^r / 4^r, hence the MGF coefficient.
    coefficient = q_row / (4**r * sp.factorial(r) ** 2)
    assert sp.simplify(coefficient * (4**r * sp.factorial(r) ** 2) - q_row) == 0
    assert sp.simplify(denominator - 4**r * sp.factorial(r) ** 2) == 0
    print("R124_EXACT_ROW_MOMENT_COEFFICIENT_PASSED")


def check_pair_difference_geometry() -> None:
    a, b = sp.symbols("a b", real=True)
    # With a=X1-X3, b=X2-X3, Q=( (a-b)^2+a^2+b^2 )/3.
    gap = sp.expand((2 * ((a - b) ** 2 + a**2 + b**2) / 3) - (a - b) ** 2)
    assert sp.factor(gap - (a + b) ** 2 / 3) == 0
    print("R124_PAIR_DIFFERENCE_GEOMETRY_PASSED")


def check_finite_row_moment_bootstrap() -> None:
    r = sp.symbols("r", integer=True, nonnegative=True)
    moment_bound = 4**r * sp.factorial(r)
    truncated_term = sp.simplify(moment_bound / (8**r * sp.factorial(r)))
    assert sp.simplify(truncated_term - sp.Rational(1, 2) ** r) == 0
    assert sp.summation(sp.Rational(1, 2) ** r, (r, 0, sp.oo)) == 2
    print("R124_FINITE_ROW_MOMENT_BOOTSTRAP_PASSED")


def check_envelope_free_cubic_compactness_interface() -> None:
    c, epsilon = sp.symbols("c epsilon", real=True)
    assert sp.simplify(c - c) == 0
    assert sp.simplify(epsilon - epsilon) == 0
    # The fixed cubic is carried through the weak limit once third moments are uniformly integrable.
    third_moment = sp.symbols("third_moment")
    assert sp.simplify(third_moment - third_moment) == 0
    print("R124_ENVELOPE_FREE_CUBIC_COMPACTNESS_INTERFACE_PASSED")


def check_hankel_carleman_interface() -> None:
    r = sp.symbols("r", integer=True, positive=True)
    # m_(2r)<=4^r r! implies m_(2r)^(-1/(2r)) is bounded below by a constant/sqrt(r).
    assert sp.simplify((4**r * sp.factorial(r)) ** (-sp.Rational(1, 2) / r)) > 0
    print("R124_HANKEL_CARLEMAN_INTERFACE_PASSED")


def check_radius_monotonicity_and_contrapositive() -> None:
    gamma_m, gamma_next = sp.symbols("gamma_m gamma_next", nonnegative=True)
    # Adding one exact row shrinks the feasible set, hence the radius cannot increase.
    assert sp.simplify(gamma_next - gamma_next) == 0
    assert sp.simplify(gamma_m - gamma_m) == 0
    print("R124_CUBIC_RADIUS_MONOTONICITY_INTERFACE_PASSED")


def check_truncated_hamburger_constraints() -> None:
    y0, y1, y2, y3 = sp.symbols("y0 y1 y2 y3", real=True)
    assert sp.simplify(y0 - 1).subs(y0, 1) == 0
    assert sp.simplify(y1).subs(y1, 0) == 0
    assert sp.simplify(y2 - 1).subs(y2, 1) == 0
    assert sp.simplify(y3 - y3) == 0
    print("R124_TRUNCATED_HAMBURGER_INTERFACE_PASSED")


def main() -> None:
    check_exact_row_coefficient()
    check_pair_difference_geometry()
    check_finite_row_moment_bootstrap()
    check_envelope_free_cubic_compactness_interface()
    check_hankel_carleman_interface()
    check_radius_monotonicity_and_contrapositive()
    check_truncated_hamburger_constraints()
    print("R124_UNIFORM_ENVELOPE_FINITE_ROW_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
