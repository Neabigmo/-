"""Exact audit for the explicit conditional bridge in R111.

No numerical search or optimization is used.  The analytic inequalities are
recorded in the README; this file checks their algebraic constants, geometric
scaling, and the cumulant tail formula.
"""

from __future__ import annotations

import sympy as sp


def check_zero_free_radius_constants() -> None:
    a, B, r = sp.symbols("a B r", positive=True)
    rho_sq = sp.Min(a / 4, a * sp.E / (8 * B))
    prefactor_at_second_radius = sp.simplify(
        (B * r**2 / (a * sp.E)).subs(r**2, a * sp.E / (8 * B))
    )
    exponent_at_first_radius = sp.simplify(
        (r**2 / (2 * a)).subs(r**2, a / 4)
    )
    assert prefactor_at_second_radius == sp.Rational(1, 8)
    assert exponent_at_first_radius == sp.Rational(1, 8)
    assert rho_sq.has(a / 4) and rho_sq.has(a * sp.E / (8 * B))
    print("R111_ZERO_FREE_RADIUS_CONSTANTS_PASSED")


def check_cumulant_tail() -> None:
    x = sp.symbols("x", positive=True)
    m = sp.symbols("m", integer=True, nonnegative=True)
    finite = sp.summation(x ** (2 * m), (m, 3, 8))
    expected = x**6 / (1 - x**2)
    assert sp.simplify(expected - finite - x**18 / (1 - x**2)) == 0
    assert sp.simplify(
        (x**6 / (1 - x**2)).subs(x, sp.Rational(1, 2))
        - sp.Rational(1, 48)
    ) == 0
    print("R111_CUMULANT_TAIL_GEOMETRY_PASSED")


def check_ou_and_ellipse_scaling() -> None:
    q, N, s, t = sp.symbols("q N s t", positive=True)
    radii = (s, s + t, 2 * s + t)
    y2 = sp.expand(sum(r**2 for r in radii))
    assert y2 == 6 * s**2 + 6 * s * t + 2 * t**2
    assert sp.simplify((q ** (N / 2)) ** 6 - q ** (3 * N)) == 0
    print("R111_OU_AND_ELLIPSE_SCALING_PASSED")


def check_d3_exactness_sign_interface() -> None:
    kappa3, kappa6 = sp.symbols("kappa3 kappa6", real=True)
    assert sp.simplify(
        (kappa6 + 3 * kappa3**2).subs(kappa6, -3 * kappa3**2)
    ) == 0
    assert sp.simplify(
        (-kappa6 / sp.factorial(6)).subs(kappa6, -3 * kappa3**2)
        - kappa3**2 / 240
    ) == 0
    print("R111_D3_SIGN_INTERFACE_PASSED")


def main() -> None:
    check_zero_free_radius_constants()
    check_cumulant_tail()
    check_ou_and_ellipse_scaling()
    check_d3_exactness_sign_interface()
    print("R111_UNIFORM_MODULUS_SOURCE_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
