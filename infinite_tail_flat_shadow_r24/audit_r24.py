"""Proof-level audit for the R24 flat-shadow orientation reduction.

The explicit seed is deliberately finite-prefix.  It tests the algebraic
obstruction without claiming a full-exact non-Gaussian law.
"""

from __future__ import annotations

import sympy as sp


def one_body_expectation(poly: sp.Expr, x: sp.Symbol, moments: list[sp.Expr]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), x)
    return sp.simplify(
        sum(coefficient * moments[monomial[0]] for monomial, coefficient in expanded.terms())
    )


def iid_expectation(poly: sp.Expr, variables: tuple[sp.Symbol, ...], moments: list[sp.Expr]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), *variables)
    total = sp.Integer(0)
    for monomial, coefficient in expanded.terms():
        product = coefficient
        for degree in monomial:
            product *= moments[degree]
        total += product
    return sp.simplify(total)


def jacobi_seed() -> tuple[sp.Matrix, list[sp.Expr]]:
    x = sp.symbols("x")
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
    return J, moments


def check_null_square_and_explicit_overshoot() -> None:
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    J, seed_moments = jacobi_seed()
    P3 = sp.expand(J.charpoly(x).as_expr())

    # P3 is the monic annihilating polynomial of the 3-atomic seed.  The
    # degree-7 leakage vanishes, while replacing only m8 by the formal Q^4
    # value makes the next square strictly negative.
    ell = one_body_expectation(P3 * x**4, x, seed_moments)
    assert ell == 0
    formal_moments = seed_moments.copy()
    formal_moments[8] = 109 - 64 * sp.sqrt(3)
    q3 = one_body_expectation(x**2 * P3**2, x, formal_moments)
    assert q3 == -(165 + 108 * sp.sqrt(3))
    assert q3 < 0

    Q = sp.Rational(2, 3) * (
        x1**2 + x2**2 + x3**2 - x1 * x2 - x1 * x3 - x2 * x3
    )
    assert iid_expectation(Q, (x1, x2, x3), seed_moments) == 2
    assert iid_expectation(Q**2, (x1, x2, x3), seed_moments) == 8
    assert iid_expectation(Q**3, (x1, x2, x3), seed_moments) == 48
    assert iid_expectation(Q**4, (x1, x2, x3), seed_moments) == (
        sp.Rational(4336, 9) + 64 * sp.sqrt(3)
    )
    assert iid_expectation(Q**4, (x1, x2, x3), formal_moments) == 384

    # q3 is exactly the difference between the formal next even moment and
    # the atomic shadow moment, so the Schur-direction identification is
    # witnessed on the same explicit seed.
    assert q3 == (109 - 64 * sp.sqrt(3)) - (274 + 44 * sp.sqrt(3))


def check_laguerre_sign_identity() -> None:
    T, unfixed = sp.symbols("T unfixed")
    for M in range(0, 9):
        n = M + 1
        laguerre = sp.Poly(sp.laguerre(n, T), T)
        expected_laguerre = sp.Integer(0)
        for (degree,), coefficient in laguerre.terms():
            expected_laguerre += coefficient * (
                sp.factorial(degree) if degree <= M else unfixed
            )
        expected_laguerre = sp.expand(expected_laguerre)
        assert sp.simplify(
            (-1) ** M * sp.factorial(n) * expected_laguerre
            - (sp.factorial(n) - unfixed)
        ) == 0


def gaussian_heat_add(moments: list[sp.Expr], variance: sp.Expr) -> list[sp.Expr]:
    result: list[sp.Expr] = []
    for degree in range(len(moments)):
        smoothed = sp.Integer(0)
        for j in range(degree // 2 + 1):
            double_factorial = sp.factorial2(2 * j - 1)
            smoothed += (
                sp.binomial(degree, 2 * j)
                * double_factorial
                * variance**j
                * moments[degree - 2 * j]
            )
        result.append(sp.simplify(smoothed))
    return result


def check_positive_smoothed_finite_prefix() -> None:
    _, seed_moments = jacobi_seed()
    formal_moments = seed_moments.copy()
    formal_moments[8] = 109 - 64 * sp.sqrt(3)
    smoothed = gaussian_heat_add(formal_moments, sp.Integer(1))
    expected = [
        1,
        0,
        2,
        1,
        12,
        14 - 2 * sp.sqrt(3),
        127,
        192 - 78 * sp.sqrt(3),
        1880 - 64 * sp.sqrt(3),
    ]
    assert smoothed == expected

    hankel_determinants = []
    for rank in range(5):
        matrix = sp.Matrix(
            [
                [smoothed[row + column] for column in range(rank + 1)]
                for row in range(rank + 1)
            ]
        )
        hankel_determinants.append(sp.factor(matrix.det()))
    expected_determinants = [
        1,
        2,
        15,
        6 * (119 + 8 * sp.sqrt(3)),
        72 * (2727 + sp.sqrt(3)),
    ]
    assert all(
        sp.simplify(actual - expected) == 0
        for actual, expected in zip(hankel_determinants, expected_determinants)
    )
    assert all(value.is_positive for value in hankel_determinants)

    x1, x2, x3 = sp.symbols("x1 x2 x3")
    Q = sp.Rational(2, 3) * (
        x1**2 + x2**2 + x3**2 - x1 * x2 - x1 * x3 - x2 * x3
    )
    q_moments = [iid_expectation(Q**degree, (x1, x2, x3), smoothed) for degree in range(1, 5)]
    assert q_moments == [4, 32, 384, 6144]
    # Rescaling each one-body variable by sqrt(2) makes the variance one and
    # divides Q by two, giving the target chi-square moments through order 4.
    assert [sp.simplify(moment / 2**degree) for degree, moment in enumerate(q_moments, 1)] == [
        2**degree * sp.factorial(degree) for degree in range(1, 5)
    ]


def main() -> None:
    checks = [
        check_null_square_and_explicit_overshoot,
        check_laguerre_sign_identity,
        check_positive_smoothed_finite_prefix,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R24_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
