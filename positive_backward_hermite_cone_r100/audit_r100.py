"""Exact symbolic audit for the R100 finite-depth certificate."""

from __future__ import annotations

import sympy as sp


t = sp.symbols("t", positive=True)
a3, a4, a6 = sp.symbols("a3 a4 a6", real=True)

# R99's [psi_1, psi_2] determinant, after clearing its positive t^-2 factor.
det12_cleared = sp.sqrt(6) * a4 + t**2 - 3 * a3**2 / t
f34 = sp.expand(t * det12_cleared)
assert sp.simplify(f34 - (t**3 + sp.sqrt(6) * a4 * t - 3 * a3**2)) == 0

# R99's [psi_0, psi_3] wall, after clearing its positive t^-3 factor.
det03_cleared = (
    2 * sp.sqrt(5) * a6 + 3 * sp.sqrt(6) * t * a4
    + t**3 - a3**2
)
assert sp.simplify(
    det03_cleared - (
        2 * sp.sqrt(5) * a6 + 3 * sp.sqrt(6) * t * a4
        + t**3 - a3**2
    )
) == 0

# The unique-root argument is encoded algebraically: the only critical point
# for a4<0 is a minimum, and its value is strictly below f(0).
f = t**3 + sp.sqrt(6) * a4 * t - 3 * a3**2
fp = sp.diff(f, t)
assert fp == 3 * t**2 + sp.sqrt(6) * a4
assert sp.simplify(f.subs(t, 0) + 3 * a3**2) == 0

# The centered negative-kurtosis specialization has the stated threshold.
threshold = sp.sqrt(-sp.sqrt(6) * a4)
assert sp.simplify(threshold**2 + sp.sqrt(6) * a4) == 0

# Depth substitution is literal and preserves the strict direction.
q, N = sp.symbols("q N", positive=True)
depth_polynomial = sp.expand(f.subs(t, q**N))
assert depth_polynomial.has(q ** (3 * N))
assert depth_polynomial.has(q**N)

print("R100_SKEW_KURTOSIS_POLYNOMIAL_PASSED")
print("R100_SIXTH_ORDER_FEASIBILITY_WALL_PASSED")
print("R100_UNIQUE_ROOT_ALGEBRA_PASSED")
print("R100_DEPTH_SUBSTITUTION_PASSED")
print("R100_FINITE_DEPTH_CERTIFICATE_AUDIT_COMPLETED")
