"""Proof-level audit for the R25 flat-null-square reductions.

This file checks exact algebraic identities and the radius-gap integration
bound.  The compactness-modulus statement is recorded as a conditional proof
schema in the README; it is not silently promoted to an orientation theorem.
"""

from __future__ import annotations

import sympy as sp


def one_body_expectation(poly: sp.Expr, x: sp.Symbol, moments: list[sp.Expr]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), x)
    return sp.simplify(
        sum(coefficient * moments[monomial[0]] for monomial, coefficient in expanded.terms())
    )


def iid_expectation(
    poly: sp.Expr, variables: tuple[sp.Symbol, ...], moments: list[sp.Expr]
) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), *variables)
    total = sp.Integer(0)
    for monomial, coefficient in expanded.terms():
        product = coefficient
        for degree in monomial:
            product *= moments[degree]
        total += product
    return sp.simplify(total)


def jacobi_seed() -> list[sp.Expr]:
    J = sp.Matrix(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, -1 - 2 * sp.sqrt(3)],
        ]
    )
    moments = [sp.simplify((J**degree)[0, 0]) for degree in range(9)]
    expected = [
        sp.Integer(1),
        sp.Integer(0),
        sp.Integer(1),
        sp.Integer(1),
        sp.Integer(3),
        4 - 2 * sp.sqrt(3),
        sp.Integer(22),
        3 - 36 * sp.sqrt(3),
        274 + 44 * sp.sqrt(3),
    ]
    assert moments == expected
    return moments


def check_common_root_derivative_identity() -> None:
    s, d, q, r = sp.symbols("s d q r")
    D_M = d * s + r * s**2
    h_next = q + r * s
    D_next = sp.expand(D_M * h_next)
    assert sp.diff(D_next, s).subs(s, 0) == d * q

    # At a first boundary d=D_M'(a_*)<0, the sign equivalence is immediate.
    d_value = sp.Integer(-5)
    for q_value in (-sp.Integer(2), sp.Integer(0), sp.Integer(3)):
        derivative = d_value * q_value
        assert (q_value >= 0) == (derivative <= 0)


def check_residual_null_square_identity() -> None:
    x, x1, x2, x3 = sp.symbols("x x1 x2 x3")
    moments = jacobi_seed()
    formal = moments.copy()
    formal[8] = 109 - 64 * sp.sqrt(3)

    J = sp.Matrix(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, -1 - 2 * sp.sqrt(3)],
        ]
    )
    P3 = sp.expand(J.charpoly(x).as_expr())
    q3 = one_body_expectation(x**2 * P3**2, x, formal)
    assert q3 == -(165 + 108 * sp.sqrt(3))

    # The null-square relations L(P^2)=L(x P^2)=0 make every constant shift
    # (x-c)^2 P(x)^2 have the same expectation q.
    c = sp.symbols("c")
    shifted = one_body_expectation((x - c) ** 2 * P3**2, x, formal)
    assert sp.expand(shifted - q3) == 0

    bar = (x1 + x2 + x3) / 3
    psi = sum((xi - bar) ** 2 * P3.subs(x, xi) ** 2 for xi in (x1, x2, x3))
    psi_expectation = iid_expectation(psi, (x1, x2, x3), formal)
    assert psi_expectation == sp.Rational(4, 3) * q3
    assert sp.simplify(sp.Rational(3, 4) * psi_expectation - q3) == 0


def check_radius_gap_bound() -> None:
    M = sp.symbols("M", positive=True, integer=True)
    h_lower = sp.symbols("h_lower", positive=True)
    gap = sp.symbols("gap", nonnegative=True)
    t = sp.symbols("t", nonnegative=True)

    # t=a_*-a.  The two derivative inequalities give
    # h_M(a) >= M^2 h_(M-1)(a_*) t and then integrate once more for h_(M+1).
    lower_integral = sp.integrate(
        (M + 1) ** 2 * M**2 * h_lower * t, (t, 0, gap)
    )
    claimed = sp.Rational(1, 2) * M**2 * (M + 1) ** 2 * h_lower * gap**2
    assert sp.simplify(lower_integral - claimed) == 0


def check_omega_monotonicity_schema() -> None:
    # Omega_(K+1) <= Omega_K is just nested admissible classes.  This small
    # finite proxy checks the order-theoretic step without claiming compactness.
    overshoots = [sp.Rational(7, 3), sp.Rational(5, 4), sp.Rational(1, 2), sp.Rational(1, 5)]
    omega = [max(overshoots[k:]) for k in range(len(overshoots))]
    assert all(omega[k + 1] <= omega[k] for k in range(len(omega) - 1))


def main() -> None:
    checks = [
        check_common_root_derivative_identity,
        check_residual_null_square_identity,
        check_radius_gap_bound,
        check_omega_monotonicity_schema,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R25_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
