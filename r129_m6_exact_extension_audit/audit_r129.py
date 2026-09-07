"""R129 exact-row and M=5 -> M=6 singular-extension audit.

This file deliberately keeps the relaxed Hankel calculation separate from
representing-measure claims.  The only numerical value printed is an
evaluation of exact symbolic expressions at the isolated R127 algebraic root.
"""

from __future__ import annotations

import sympy as sp


def moment_expectation(poly: sp.Expr, xs: tuple[sp.Symbol, ...], moments: tuple[sp.Symbol, ...]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), *xs)
    out = 0
    for powers, coefficient in expanded.terms():
        term = coefficient
        for power, moment in zip(powers, moments):
            term *= moments[power]
        out += term
    return sp.expand(out)


def exact_rows() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Return the exact R2--R6 equations in triangular solved form."""
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    y = sp.symbols("y0:13")
    substitutions = {y[0]: 1, y[1]: 0, y[2]: 1}
    q = sp.expand(((x1 - x2) ** 2 + (x1 - x3) ** 2 + (x2 - x3) ** 2) / 3)
    rows = []
    for r in range(2, 7):
        value = moment_expectation(q**r, (x1, x2, x3), y)
        value = sp.expand(value.subs(substitutions))
        solved = sp.solve(sp.Eq(value, 2**r * sp.factorial(r)), y[2 * r])[0]
        rows.append(sp.factor(solved))
        substitutions[y[2 * r]] = solved
    return tuple(rows)  # type: ignore[return-value]


def check_r6_exact_row() -> None:
    r2, r3, r4, r5, r6 = exact_rows()
    y = sp.symbols("y0:13")
    assert r2 == 3
    assert r3 == 15 + 7 * y[3] ** 2
    assert r4 == 105 - 124 * y[3] ** 2 + 32 * y[3] * y[5]
    assert sp.expand(r5 - 3 * (
        17 * y[5] ** 2 - 280 * y[3] * y[5]
        + 20 * y[3] * y[7] + 470 * y[3] ** 2 + 315
    )) == 0
    assert y[11] not in r6.free_symbols
    print(f"R129_R6_SOLVED_AFTER_R2_R5 = {r6}")
    c, a, b, d = sp.symbols("c a b d")
    reduced = sp.factor(r6.subs({
        y[3]: c,
        y[4]: 3,
        y[5]: a,
        y[6]: 15 + 7 * c**2,
        y[7]: b,
        y[8]: 105 - 124 * c**2 + 32 * c * a,
        y[9]: d,
        y[10]: 3 * (17 * a**2 - 280 * a * c + 20 * b * c + 470 * c**2 + 315),
    }))
    print("R129_R6_EXACT_ROW_PASSED")
    print(f"R129_R6_Y12_REDUCED = {reduced}")


def reduce_relation(expr: sp.Expr, relation: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    numerator, denominator = sp.fraction(sp.factor(expr))
    remainder = sp.rem(sp.Poly(sp.expand(numerator), variable), sp.Poly(relation, variable)).as_expr()
    return sp.factor(remainder / denominator)


def m5_to_m6_compatibility() -> None:
    c, s = sp.symbols("c s", positive=True)
    a = 4 * c + s
    b = (a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c) / (c**2 - 2)
    d = -(
        a**2 * c - a * b * c + 4 * a * c**2 + 24 * a
        + 7 * b * c**2 + 12 * b - 49 * c**5 - 189 * c**3 - 180 * c
    ) / (c**2 - 2)
    y6 = 15 + 7 * c**2
    y8 = 105 - 124 * c**2 + 32 * c * a
    y10 = 3 * (17 * a**2 - 280 * a * c + 20 * b * c + 470 * c**2 + 315)
    h2 = sp.Matrix([[1, 0, 1], [0, 1, c], [1, c, 3]])
    u = sp.Matrix([y6, b, y8])
    B = sp.Matrix([[c, 3, a], [3, a, y6], [a, y6, b]])
    v = sp.Matrix([d, y10, sp.Symbol("y11")])
    residual = sp.simplify(v - B.T * h2.inv() * u)
    relation = s**2 - 6 * (2 - c**2) * (1 + c**2)
    r0 = reduce_relation(residual[0], relation, s)
    r1 = reduce_relation(residual[1], relation, s)
    r2 = reduce_relation(residual[2], relation, s)
    B = -5 * c**4 + 6 * c**3 * s + 68 * c**2 - 24 * c * s - 8
    C = (
        30 * c**8 - 124 * c**6 + 23 * c**5 * s + 3 * c**4
        - 62 * c**3 * s + 516 * c**2 - 40 * c * s - 208
    )
    delta5 = -18 * C / (c**2 - 2) ** 2
    s_from_B = sp.factor((5 * c**4 - 68 * c**2 + 8) / (6 * c**3 - 24 * c))
    endpoint_polynomial = (
        216 * c**10 - 1919 * c**8 + 4072 * c**6
        + 4704 * c**4 - 8000 * c**2 + 64
    )
    r0_on_B = sp.factor(sp.together(r0.subs(s, s_from_B)))
    r1_minus_delta5_on_B = sp.factor(sp.together((r1 - delta5).subs(s, s_from_B)))
    assert sp.factor(r0_on_B + endpoint_polynomial / (
        2 * c * (c - 2) * (c + 2) * (c**2 - 2) ** 2
    )) == 0
    assert sp.factor(r1_minus_delta5_on_B - endpoint_polynomial / (
        2 * (c - 2) * (c + 2) * (c**2 - 2) ** 2
    )) == 0
    assert r2.has(sp.Symbol("y11"))
    print("R129_M5_TO_M6_KERNEL_COMPATIBILITY_DERIVED")
    print(f"R129_COMPATIBILITY_RESIDUAL_0 = {r0}")
    print(f"R129_COMPATIBILITY_RESIDUAL_1 = {r1}")
    print(f"R129_COMPATIBILITY_RESIDUAL_2 = {r2}")

    # The R127 endpoint is the unique root u in (1,2) of this polynomial.
    uvar = sp.symbols("uvar", real=True)
    polynomial = sp.Poly(
        216 * uvar**5 - 1919 * uvar**4 + 4072 * uvar**3
        + 4704 * uvar**2 - 8000 * uvar + 64,
        uvar,
    )
    assert polynomial.count_roots(1, 2) == 1
    root = [z for z in sp.nroots(polynomial.as_expr(), n=30, maxsteps=200)
            if abs(sp.im(z)) < sp.Rational(1, 10) ** 20 and 1 < float(sp.re(z)) < 2][0]
    cnum = sp.sqrt(sp.re(root))
    snum = sp.sqrt(6 * (2 - sp.re(root)) * (1 + sp.re(root)))
    r0num = sp.N(r0.subs({c: cnum, s: snum}), 18)
    r1num = sp.N(r1.subs({c: cnum, s: snum}), 18)
    delta5num = sp.N(delta5.subs({c: cnum, s: snum}), 18)
    assert abs(float(r0num)) < 1e-12
    assert abs(float(r1num - delta5num)) < 1e-10
    assert float(delta5num) > 0
    print("R129_M5_TO_M6_KERNEL_COMPATIBILITY_DERIVED")
    print(f"R129_FIRST_UNTESTED_DEFECT_NUMERIC = {r1num}")
    print(f"R129_PREVIOUS_M5_SCHUR_DEFECT_NUMERIC = {delta5num}")
    print("R129_M6_R128_GHOST_EXCLUDED_ANALYTICALLY")


def main() -> None:
    check_r6_exact_row()
    m5_to_m6_compatibility()
    print("R129_M6_EXACT_EXTENSION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
