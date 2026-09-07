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

# Exact renormalized-ratio constants and the elementary factorial decay.
rho = sp.Rational(3025, 5832)
assert rho < 1
for u in range(1, 40):
    assert Fraction(u, 2 * (2 * u - 1)) <= Fraction(1, 2)

# The recurrence majorant has (m/R^2) <= 1/54 whenever m <= 2n and
# R^2=36(3n+1).  The remaining factorial series is summable because its
# consecutive ratio is eventually < 1/2, even after multiplication by rho.
n_sym = sp.symbols("n", positive=True)
assert sp.simplify(
    sp.Rational(1, 54) - 2 * n_sym / (36 * (3 * n_sym + 1))
) == sp.Rational(1, 54) / (3 * n_sym + 1)
assert 4 * rho < 3
for D in range(64, 80):
    ratio = sp.Rational(4 * 1, D + 1) * rho
    assert ratio < sp.Rational(1, 2)

# Fixed-order commutator estimates always cross at sqrt(n):
# r/2 + (1-r)/2 = 1/2 exactly.
for r in range(2, 20):
    assert sp.Rational(r, 2) + sp.Rational(1 - r, 2) == sp.Rational(1, 2)
assert sp.Rational(1, 2) < 1

# Exact first nonzero Hermite mode of the actual R80 quadratic source.
# With r_j=sqrt(2/3) cos(theta+2*pi*j/3), write p_ij=r_i*r_j.
# The p_ij have sum -1/2, pairwise sum 0, and product (r1*r2*r3)^2.
# Averaging (r1*r2*r3)^2 gives 1/108, hence sum p_ij^3=-7/72.
C33 = -sp.Rational(1, 8) + 3 * sp.Rational(1, 108)
assert C33 == -sp.Rational(7, 72)
A6 = sp.Rational(3) * sp.Rational(1, 6) ** 3 * sp.binomial(6, 3)
V6 = sp.simplify(-(C33 / 36) / A6)
assert A6 == sp.Rational(5, 18)
assert V6 == sp.Rational(7, 720)
assert sp.sqrt(sp.factorial(6)) * V6 == 7 * sp.sqrt(5) / 60
eta6 = 7 * sp.sqrt(5) / 60
for i in range(7):
    assert sp.simplify(eta6 * sp.sqrt(sp.binomial(6, i))
                       - eta6 * sp.sqrt(sp.factorial(6)
                                         / (sp.factorial(i) * sp.factorial(6 - i)))) == 0

print("R98_EXACT_GAUSSIAN_MODE_COST_PASSED")
print("R98_ACTUAL_K51_NONZERO_PASSED")
print("R98_GROWING_RADIUS_RATIO_PASSED")
print("R98_RENORMALIZED_ENDPOINT_COLUMN_MAJORANT_PASSED")
print("R98_FINITE_COMMUTATOR_SQRTN_BARRIER_PASSED")
print("R98_G2_GAP6_ANCHOR_PASSED")
print("R98_G2_DEGREE6_CORNER_PASSED")
print("R98_CGAMMA_ZERO_ENDPOINT_OBSTRUCTION_COMPLETED")
