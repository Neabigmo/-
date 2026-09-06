"""R65 exact audit of the finite quadratic-response sums.

This audit uses rational arithmetic only.  It checks the root-of-unity closed
form for C_(r,s), the induced even response v_(2n), and the K/Lambda formulas
at targeted exact stages.  The cutoff lemma itself is recorded in corrected
form in the README; its scale is n/|Lambda_n|.
"""

from fractions import Fraction
from math import comb, factorial
from functools import lru_cache


@lru_cache(None)
def u(degree):
    if degree < 3 or degree % 2 == 0:
        return Fraction(0)
    m = (degree - 1) // 2
    return Fraction((-1)**(m - 1) * m * factorial(m + 1), 2)


@lru_cache(None)
def C_closed(r, s):
    n = (r + s) // 2
    central = comb(2*n, n)
    selected = sum(
        comb(r, p) * comb(s, n - p)
        for p in range(r + 1)
        if 0 <= n - p <= s and (2*p - r) % 3 == 0
    )
    return Fraction(3, 2 * 6**n) * (3*selected - central)


def A(n):
    return Fraction(3 * comb(2*n, n), 6**n)


@lru_cache(None)
def v(degree):
    if degree < 6 or degree % 2:
        return Fraction(0)
    n = degree // 2
    convolution = sum(
        u(r) * u(degree - r) / (factorial(r) * factorial(degree - r))
        * C_closed(r, degree - r)
        for r in range(3, degree, 2)
    )
    return -convolution / A(n) * factorial(degree)


@lru_cache(None)
def M(n, k):
    return sum(
        factorial(j) * comb(n, j) * comb(k, j) * u(n + k - 2*j)
        for j in range(min(n, k) + 1)
    )


@lru_cache(None)
def D(n):
    return sum(
        factorial(j) * comb(n, j)**2 * v(2*n - 2*j)
        for j in range(n + 1)
    )


@lru_cache(None)
def K(n):
    return D(n) - sum(M(n, k)**2 / factorial(k) for k in range(n))


def Lambda(n):
    return (K(n) - n*K(n - 1)) / factorial(n - 1)


def check_response_sums():
    expected = {
        6: Fraction(7),
        8: Fraction(-192),
        10: Fraction(3996),
        12: Fraction(-817 * factorial(12), 4989600),
    }
    for degree, value in expected.items():
        assert v(degree) == value
    print("R65_CLOSED_C_AND_EVEN_RESPONSE_TARGETS PASSED")


def check_lambda_targets():
    targets = {
        10: Fraction(-1481, 21),
        15: Fraction(15335, 858),
        20: Fraction(-42799, 19019),
        30: Fraction(1063856351, 38818159380),
    }
    for n, value in targets.items():
        assert Lambda(n) == value
    assert Lambda(100) > 0
    assert Lambda(200) > 0
    print("R65_LAMBDA_EXACT_TARGETS_10_15_20_30_100_200 PASSED")


if __name__ == "__main__":
    check_response_sums()
    check_lambda_targets()
    print("R65_QUADRATIC_RESPONSE_AUDIT_COMPLETED")
