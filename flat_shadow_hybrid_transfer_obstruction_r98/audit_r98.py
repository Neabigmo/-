"""Exact audit for the R98 growing-radius hybrid obstruction."""

from __future__ import annotations

from fractions import Fraction
from math import factorial

import sympy as sp


R = sp.symbols("R", positive=True)


def c(j: int) -> sp.Rational:
    return sp.Rational(factorial(j) ** 2, factorial(2 * j + 1))


def A(m: int) -> sp.Expr:
    return sp.expand(
        sum(
            sp.Rational(factorial(m), 2**ell * factorial(ell) * factorial(m - 2 * ell))
            * R ** (m - 2 * ell)
            / sp.sqrt(factorial(m))
            for ell in range(m // 2 + 1)
        )
    )


def K_gap_four(j: int) -> Fraction:
    numerator = 3 * j**3 + 146 * j**2 + 1001 * j + 1560
    denominator = 15 * (j + 1) * (j + 2) * (j + 3) ** 2 * (j + 4) ** 2
    return -Fraction(numerator, denominator)


assert sp.simplify(A(3) - (R**3 + 3 * R) / sp.sqrt(6)) == 0
assert sp.simplify(sp.Poly(A(11), R).LC() - 1 / sp.sqrt(sp.factorial(11))) == 0
assert c(1) == sp.Rational(1, 6)
assert c(5) == sp.Rational(1, 2772)
assert K_gap_four(1) == -Fraction(271, 3600)

ratio = sp.simplify(c(5) * A(11) / (c(1) * A(3)))
leading = sp.simplify(sp.limit(ratio / R**8, R, sp.oo))
assert leading == sp.sqrt(sp.Rational(6, factorial(11))) / 462
assert leading > 0

print("R98_EXACT_GAUSSIAN_MODE_COST_PASSED")
print("R98_ACTUAL_K51_NONZERO_PASSED")
print("R98_GROWING_RADIUS_RATIO_PASSED")
print("R98_CGAMMA_ZERO_ENDPOINT_OBSTRUCTION_COMPLETED")
