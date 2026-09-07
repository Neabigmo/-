"""Exact symbolic audit for the R99 positive backward-OU Hermite cone."""

from __future__ import annotations

import sympy as sp


def psi(n: int, x: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.hermite_prob(n, x) / sp.sqrt(sp.factorial(n)))


def product_coeff(i: int, j: int, ell: int) -> sp.Expr:
    return sp.factorial(ell) * sp.binomial(i, ell) * sp.binomial(j, ell) * sp.sqrt(
        sp.factorial(i + j - 2 * ell) / (sp.factorial(i) * sp.factorial(j))
    )


def cone_entry(i: int, j: int, t: sp.Symbol, a: dict[int, sp.Expr]) -> sp.Expr:
    return sp.expand(
        sum(
            product_coeff(i, j, ell)
            * t ** (-(i + j - 2 * ell) / 2)
            * a[i + j - 2 * ell]
            for ell in range(min(i, j) + 1)
        )
    )


x = sp.symbols("x")
t = sp.symbols("t", positive=True)
a = {k: sp.symbols(f"a{k}") for k in range(13)}
a[0] = sp.Integer(1)

# Verify the normalized Hermite product formula at low degrees.
for i in range(8):
    for j in range(8):
        rhs = sp.expand(
            sum(
                product_coeff(i, j, ell) * psi(i + j - 2 * ell, x)
                for ell in range(min(i, j) + 1)
            )
        )
        assert sp.simplify(psi(i, x) * psi(j, x) - rhs) == 0

# The degree-m diagonal coefficient formula is exact.
for m in range(1, 7):
    diagonal = sp.expand(
        sum(
            product_coeff(m, m, ell) * a[2 * m - 2 * ell]
            for ell in range(m + 1)
        )
    )
    closed = sp.expand(
        sum(
            sp.factorial(m) * sp.sqrt(sp.factorial(2 * m - 2 * ell))
            / (sp.factorial(ell) * sp.factorial(m - ell) ** 2)
            * a[2 * m - 2 * ell]
            for ell in range(m + 1)
        )
    )
    assert sp.simplify(diagonal - closed) == 0

# Centered variance-one specialization: a1=a2=0.
a[1] = sp.Integer(0)
a[2] = sp.Integer(0)

M22 = sp.simplify(cone_entry(2, 2, t, a))
M12 = sp.simplify(cone_entry(1, 2, t, a))
M33 = sp.simplify(cone_entry(3, 3, t, a))
assert sp.simplify(M22 - (t**-2 * a[4] * sp.sqrt(6) + 1)) == 0
assert sp.simplify(M12 - sp.sqrt(3) * t ** (-sp.Rational(3, 2)) * a[3]) == 0
assert sp.simplify(
    M33 - (2 * sp.sqrt(5) * t**-3 * a[6]
           + 3 * sp.sqrt(6) * t**-2 * a[4] + 1)
) == 0

# [psi_1, psi_2] positivity gives the exact kurtosis/skewness wall.
det12 = sp.expand(M22 - M12**2)
expected12 = t**-2 * (
    sp.sqrt(6) * a[4] + t**2 - 3 * t**-1 * a[3]**2
)
assert sp.simplify(det12 - expected12) == 0

# [psi_0, psi_3] gives the independent sixth-order wall.
det03 = sp.expand(M33 - (t ** (-sp.Rational(3, 2)) * a[3]) ** 2)
expected03 = t**-3 * (
    2 * sp.sqrt(5) * a[6] + 3 * sp.sqrt(6) * t * a[4]
    + t**3 - a[3]**2
)
assert sp.simplify(det03 - expected03) == 0

# Convert the [psi_1,psi_2] wall to raw centered moments.
m3, m4 = sp.symbols("m3 m4")
raw = sp.simplify(
    expected12.subs({a[3]: m3 / sp.sqrt(6),
                     a[4]: (m4 - 3) / sp.sqrt(24)})
)
assert sp.simplify(
    raw - sp.Rational(1, 2) * t**-2
    * (m4 - 3 + 2 * t**2 - m3**2 / t)
) == 0

# A depth-N specialization is obtained by the literal substitution t=q**N.
q, N = sp.symbols("q N", positive=True)
depth_bound = sp.simplify(
    (sp.sqrt(6) * a[4] + t**2 - 3 * t**-1 * a[3]**2).subs(t, q**N)
)
assert depth_bound.has(q ** (2 * N))
assert depth_bound.has(q ** (-N))

print("R99_HERMITE_PRODUCT_FORMULA_PASSED")
print("R99_POSITIVE_BACKWARD_GRAM_CONE_PASSED")
print("R99_DEGREE34_SKEW_KURTOSIS_WALL_PASSED")
print("R99_DEGREE36_SIXTH_ORDER_WALL_PASSED")
print("R99_DEPTH_N_SPECIALIZATION_PASSED")
print("R99_POSITIVE_BACKWARD_HERMITE_CONE_AUDIT_COMPLETED")
