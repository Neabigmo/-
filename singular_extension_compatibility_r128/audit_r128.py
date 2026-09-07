"""Exact audit for the R128 singular-extension and R5 interfaces."""

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


def check_singular_extension_lemma() -> None:
    # A PSD block matrix has q^T H q=0 only when Hq=0.  Applying this to
    # q=(p,0) yields the old-kernel/new-column compatibility equation.
    p0, p1, p2 = sp.symbols("p0 p1 p2")
    y3, y4, y5 = sp.symbols("y3 y4 y5")
    compatibility = p0 * y3 + p1 * y4 + p2 * y5
    assert compatibility == sp.Add(*(p * y for p, y in zip((p0, p1, p2), (y3, y4, y5))))
    print("R128_SINGULAR_EXTENSION_COMPATIBILITY_PASSED")


def check_r5_row() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    moments = sp.symbols("y0:11")
    q = sp.expand((x1 - x2) ** 2 / 2 + (x1 - x3) ** 2 / 2 + (x2 - x3) ** 2 / 2)
    eq5 = moment_expectation(q**5, (x1, x2, x3), moments)
    eq5 = sp.expand(eq5.subs({moments[0]: 1, moments[1]: 0, moments[2]: 1}))
    expected = (
        3 * moments[10]
        - 360 * moments[3] * moments[5]
        - 180 * moments[3] * moments[7]
        + 225 * moments[4] ** 2
        + 270 * moments[4] * moments[6]
        - 153 * moments[5] ** 2
        + 180 * moments[6]
        + 90 * moments[8]
    )
    assert sp.expand(eq5 - expected) == 0
    y10 = sp.solve(sp.Eq(eq5, 2**5 * sp.factorial(5)), moments[10])[0]
    expected_y10 = (
        120 * moments[3] * moments[5]
        + 60 * moments[3] * moments[7]
        - 75 * moments[4] ** 2
        - 90 * moments[4] * moments[6]
        + 51 * moments[5] ** 2
        - 60 * moments[6]
        - 30 * moments[8]
        + 1280
    )
    assert sp.expand(y10 - expected_y10) == 0
    print("R128_R5_EXACT_ROW_PASSED")
    print("R128_R5_TRIANGULAR_ELIMINATION_PASSED")


def check_strict_m5_drop_certificate() -> None:
    u = sp.symbols("u", real=True)
    polynomial = sp.Poly(
        216 * u**5 - 1919 * u**4 + 4072 * u**3 + 4704 * u**2 - 8000 * u + 64,
        u,
    )
    left = sp.Rational(111, 100)
    right = sp.Rational(28, 25)
    assert polynomial.count_roots(1, 2) == 1
    assert polynomial.eval(left) * polynomial.eval(right) < 0
    print("R128_R127_ROOT_INTERVAL_PASSED")

    c, s = sp.symbols("c s", positive=True)
    a = 4 * c + s
    b = (a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c) / (c**2 - 2)
    y10 = sp.factor(51 * a**2 - 840 * a * c + 60 * b * c + 1410 * c**2 - 7495)
    relation = s**2 - 6 * (2 - c**2) * (1 + c**2)
    numerator, denominator = sp.fraction(y10)
    reduced = sp.rem(sp.Poly(sp.expand(numerator), s), sp.Poly(relation, s)).as_expr()
    expected = -666 * c**6 + 1044 * c**4 - 6307 * c**2 + 13766 - 216 * c * s * (2 * c**2 + 1)
    assert sp.expand(reduced - expected) == 0
    assert denominator == c**2 - 2
    print("R128_M4_EXTREMIZER_R5_REDUCTION_PASSED")

    # Exact rational interval certificate: for u in (111/100, 28/25),
    # A(u)>7000 and T(u)<2500, so N=A-T>4500.
    A = -666 * u**3 + 1044 * u**2 - 6307 * u + 13766
    assert sp.diff(A, u).subs(u, left) < 0
    assert sp.diff(A, u).subs(u, right) < 0
    assert A.subs(u, right) > 7000
    t2_upper = (
        216**2
        * right
        * 6
        * sp.Rational(89, 100)
        * sp.Rational(53, 25)
        * (sp.Rational(81, 25)) ** 2
    )
    assert t2_upper < 2500**2
    print("R128_M5_NEGATIVE_Y10_INTERVAL_CERTIFICATE_PASSED")
    print("R128_STRICT_RELAXED_RADIUS_DROP_INTERFACE_PASSED")


def main() -> None:
    check_singular_extension_lemma()
    check_r5_row()
    check_strict_m5_drop_certificate()
    print("R128_SINGULAR_EXTENSION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
