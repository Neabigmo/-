"""R69 exact audit for the projection first-difference reduction.

The checks use exact factorial/rational arithmetic and symbolic limits for the
local scaling. The global Gaussian majorant is inherited from R67 and is not
replaced by finite numerical sampling.
"""

from fractions import Fraction
from math import factorial

import sympy as sp


def term(m: int, j: int) -> Fraction:
    a = j * j + 5 * j - 2 * m
    numerator = (j + 1) ** 2 * (j + 2) ** 2 * a**2
    return Fraction(numerator, 4 * factorial(m + 3)) * Fraction(
        factorial(m - j - 1) ** 2, factorial(m - 2 * j)
    )


def check_adjacent_term_identity() -> None:
    for m in range(4, 31):
        for j in range((m - 1) // 2 + 1):
            a = j * j + 5 * j - 2 * m
            L = Fraction((m + 3) * (m - 2 * j), (m - j - 1) ** 2)
            base = Fraction((j + 1) ** 2 * (j + 2) ** 2, 4 * factorial(m + 3))
            base *= Fraction(factorial(m - j - 1) ** 2, factorial(m - 2 * j))
            lhs = term(m - 1, j)
            rhs = base * L * (a + 2) ** 2
            assert lhs == rhs
            assert term(m - 1, j) - term(m, j) == base * (
                L * (a + 2) ** 2 - a**2
            )
    print("R69_ADJACENT_TERM_IDENTITY PASSED")


def check_scaled_difference_identity() -> None:
    for m in range(4, 31):
        for j in range((m - 1) // 2 + 1):
            a = j * j - 2 * m + 5 * j
            L = Fraction((m + 3) * (m - 2 * j), (m - j - 1) ** 2)
            assert L - 1 == Fraction(5 * m - j * j - 8 * j - 1,
                                     (m - j - 1) ** 2)
            B_direct = Fraction(L * (a + 2) ** 2 - a**2, m)
            B_split = (
                m * (L - 1) * Fraction(a, m) ** 2
                + 4 * L * Fraction(a, m)
                + Fraction(4 * L, m)
            )
            assert B_direct == B_split
            rho = Fraction(
                m**5 * factorial(m - j - 1) ** 2,
                factorial(m - 2 * j) * factorial(m + 3),
            )
            G_direct = m**2 * (term(m - 1, j) - term(m, j))
            G_scaled = Fraction(1, 4) * Fraction(
                (j + 1) ** 2 * (j + 2) ** 2, m**2
            ) * rho * B_direct
            assert G_direct == G_scaled
    print("R69_SCALED_DIFFERENCE_IDENTITIES PASSED")


def check_local_limit_polynomial() -> None:
    x, y = sp.symbols("x y", positive=True)
    j = y * sp.sqrt(x)
    L = (x + 3) * (x - 2 * j) / (x - j - 1) ** 2
    A = j**2 + 5 * j - 2 * x
    B = (L * (A + 2) ** 2 - A**2) / x
    assert sp.simplify(sp.limit(x * (L - 1), x, sp.oo) - (5 - y**2)) == 0
    assert sp.simplify(sp.limit(A / x, x, sp.oo) - (y**2 - 2)) == 0
    assert sp.simplify(sp.limit(B, x, sp.oo) - (
        (5 - y**2) * (y**2 - 2) ** 2 + 4 * (y**2 - 2)
    )) == 0
    limiting_polynomial = sp.expand(
        sp.Rational(1, 4) * y**4 * (
            (5 - y**2) * (y**2 - 2) ** 2 + 4 * (y**2 - 2)
        )
    )
    expected = sp.Rational(1, 4) * (
        -y**10 + 9 * y**8 - 20 * y**6 + 12 * y**4
    )
    assert sp.expand(limiting_polynomial - expected) == 0
    print("R69_LOCAL_LIMIT_POLYNOMIAL PASSED")


def check_floor_endpoint_bound() -> None:
    # For m=2k, the additional endpoint is exactly reducible to a central
    # binomial denominator, hence the elementary central-binomial lower bound
    # gives O(m^4 2^(-m)).
    k = sp.symbols("k", integer=True, positive=True)
    m = 2 * k
    endpoint = (
        sp.Rational(1, 4)
        * (k + 1) ** 2 * (k + 2) ** 2 * (k**2 + k) ** 2
        * sp.factorial(k - 1) ** 2 / sp.factorial(2 * k + 3)
    )
    central_form = (
        (k + 1) ** 4 * (k + 2) ** 2
        / (4 * (2 * k + 1) * (2 * k + 2) * (2 * k + 3)
           * sp.binomial(2 * k, k))
    )
    assert sp.simplify(endpoint - central_form) == 0
    print("R69_FLOOR_ENDPOINT_REDUCTION PASSED")


def check_difference_integral_constant() -> None:
    y = sp.symbols("y", nonnegative=True)
    integral = sp.Rational(1, 4) * sp.sqrt(sp.pi) * (
        -sp.Rational(945, 64)
        + sp.Rational(945, 32)
        - sp.Rational(300, 16)
        + sp.Rational(36, 8)
    )
    assert sp.simplify(integral - sp.Rational(33, 256) * sp.sqrt(sp.pi)) == 0
    print("R69_DIFFERENCE_INTEGRAL_CONSTANT PASSED")


def check_index_conversion() -> None:
    n, m = sp.symbols("n m", integer=True, positive=True)
    assert sp.simplify((n - 3) - m).subs(n, m + 3) == 0
    assert sp.simplify((m + 3) ** sp.Rational(3, 2) /
                       (m ** sp.Rational(3, 2))).limit(m, sp.oo) == 1
    print("R69_INDEX_CONVERSION PASSED")


if __name__ == "__main__":
    check_adjacent_term_identity()
    check_scaled_difference_identity()
    check_local_limit_polynomial()
    check_floor_endpoint_bound()
    check_difference_integral_constant()
    check_index_conversion()
    print("R69_PROJECTION_DIFFERENCE_AUDIT_COMPLETED")
