"""Finite audit for the exact R151 Hermite-Gram identities.

The checks are algebraic coefficient checks only.  They do not certify an
infinite positive-definite law, a backward tower, or the R152 limit.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, prod

import sympy as sp


def kernel_coefficient(m: int, n: int, k: int) -> sp.Expr:
    """Coefficient of u^m v^n in exp(uv)(u+v)^k."""
    if (m + n - k) % 2:
        return sp.Integer(0)
    r = (m + n - k) // 2
    if r < 0 or r > min(m, n):
        return sp.Integer(0)
    return sp.Rational(comb(k, m - r), factorial(r))


def derivative_formula(m: int, n: int, k: int) -> sp.Expr:
    return sp.sqrt(factorial(m) * factorial(n)) * kernel_coefficient(m, n, k)


def check_generating_identity() -> None:
    u, v = sp.symbols("u v")
    # Differentiate at the Gaussian point.  The exponential e^(uv) needs
    # only finitely many terms for any fixed coefficient, so compare its
    # finite coefficient extraction with the closed formula directly.
    for m in range(7):
        for n in range(7):
            for k in (3, 5):
                polynomial = sp.expand((u + v) ** k)
                coefficient = sp.Integer(0)
                for r in range(min(m, n) + 1):
                    coefficient += sp.Rational(1, factorial(r)) * polynomial.coeff(u, m - r).coeff(v, n - r)
                expected = kernel_coefficient(m, n, k)
                assert sp.simplify(coefficient - expected) == 0
    print("R151_HERMITE_GRAM_GENERATOR_PASSED")


def check_adjacent_sensitivities() -> None:
    for d in (5, 7, 9, 13):
        s = (d - 1) // 2
        for M in range(s + 1, s + 8):
            direct = derivative_formula(M, M + 1, d)
            advertised = comb(d, s) * sp.sqrt(M + 1) * prod(range(M - s + 1, M + 1))
            assert sp.simplify(direct - advertised) == 0

            next_direct = derivative_formula(M, M + 1, d + 2)
            ratio = sp.simplify(next_direct / direct)
            expected_ratio = sp.Rational(4 * (d + 2), d + 3) * (M - s)
            assert sp.simplify(ratio - expected_ratio) == 0
    print("R151_ADJACENT_RATIO_PASSED")


def check_all_higher_ratios() -> None:
    for d in (5, 7, 11):
        s = (d - 1) // 2
        for M in range(s + 3, s + 8):
            base = derivative_formula(M, M + 1, d)
            for j in range(0, 4):
                direct = derivative_formula(M, M + 1, d + 2 * j)
                falling = prod(range(M - s - j + 1, M - s + 1)) if j else 1
                expected = sp.Rational(comb(d + 2 * j, s + j), comb(d, s)) * falling
                assert sp.simplify(direct / base - expected) == 0
    print("R151_ALL_HIGHER_ODD_RATIOS_PASSED")


def check_critical_exponents() -> None:
    # With M=tau*|a|^(-2/d), a*L_(d+2j,M) has exponent zero after the
    # proposed coefficient scaling |a|^(1+2j/d).
    for d in (5, 7, 13, 31):
        for j in range(4):
            exponent = Fraction(1, 1) + Fraction(2 * j, d) - Fraction(d + 2 * j, d)
            assert exponent == 0
    print("R151_CRITICAL_EXPONENTS_PASSED")


def check_ou_shape_invariance() -> None:
    # c_(d+2j)/|c_d|^(1+2j/d) is unchanged by c_n -> lambda^(n/2)c_n.
    for d in (5, 9, 21):
        for j in range(5):
            numerator_power = Fraction(d + 2 * j, 2)
            denominator_power = Fraction(d, 2) * Fraction(d + 2 * j, d)
            assert numerator_power == denominator_power
    print("R151_OU_SHAPE_INVARIANCE_PASSED")


def main() -> None:
    check_generating_identity()
    check_adjacent_sensitivities()
    check_all_higher_ratios()
    check_critical_exponents()
    check_ou_shape_invariance()
    print("R151_SCOPE_EXPLICIT: exact finite coefficient identities only")
    print("R151_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
