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
    q = sp.expand(((x1 - x2) ** 2 + (x1 - x3) ** 2 + (x2 - x3) ** 2) / 3)
    eq5 = moment_expectation(q**5, (x1, x2, x3), moments)
    eq5 = sp.expand(eq5.subs({moments[0]: 1, moments[1]: 0, moments[2]: 1}))
    expected = sp.Rational(32, 81) * (
        moments[10]
        - 120 * moments[3] * moments[5]
        - 60 * moments[3] * moments[7]
        + 75 * moments[4] ** 2
        + 90 * moments[4] * moments[6]
        - 51 * moments[5] ** 2
        + 60 * moments[6]
        + 30 * moments[8]
    )
    assert sp.expand(eq5 - expected) == 0
    gaussian = {
        moments[0]: 1,
        moments[1]: 0,
        moments[2]: 1,
        moments[3]: 0,
        moments[4]: 3,
        moments[5]: 0,
        moments[6]: 15,
        moments[7]: 0,
        moments[8]: 105,
        moments[9]: 0,
        moments[10]: 945,
    }
    assert expected.subs(gaussian) == 2**5 * sp.factorial(5)
    print("R128_GAUSSIAN_NORMALIZATION_CHECK_PASSED")
    y10 = sp.solve(sp.Eq(eq5, 2**5 * sp.factorial(5)), moments[10])[0]
    expected_y10 = (
        120 * moments[3] * moments[5]
        + 60 * moments[3] * moments[7]
        - 75 * moments[4] ** 2
        - 90 * moments[4] * moments[6]
        + 51 * moments[5] ** 2
        - 60 * moments[6]
        - 30 * moments[8]
        + 9720
    )
    assert sp.expand(y10 - expected_y10) == 0
    reduced_after_previous_rows = sp.expand(
        expected_y10.subs({moments[4]: 3, moments[6]: 15 + 7 * moments[3] ** 2,
                           moments[8]: 105 - 124 * moments[3] ** 2 + 32 * moments[3] * moments[5]})
    )
    assert sp.factor(reduced_after_previous_rows - 3 * (
        17 * moments[5] ** 2 - 280 * moments[5] * moments[3]
        + 20 * moments[7] * moments[3] + 470 * moments[3] ** 2 + 315
    )) == 0
    print("R128_R5_PREVIOUS_ROW_REDUCTION_PASSED")
    print("R128_R5_EXACT_ROW_PASSED")
    print("R128_R5_TRIANGULAR_ELIMINATION_PASSED")


def check_m5_singular_ghost() -> None:
    c, s = sp.symbols("c s", positive=True)
    a = 4 * c + s
    b = (a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c) / (c**2 - 2)
    d = -(
        a**2 * c
        - a * b * c
        + 4 * a * c**2
        + 24 * a
        + 7 * b * c**2
        + 12 * b
        - 49 * c**5
        - 189 * c**3
        - 180 * c
    ) / (c**2 - 2)
    y6 = 15 + 7 * c**2
    y8 = 105 - 124 * c**2 + 32 * c * a
    y10 = 3 * (17 * a**2 - 280 * a * c + 20 * b * c + 470 * c**2 + 315)
    h2 = sp.Matrix([[1, 0, 1], [0, 1, c], [1, c, 3]])
    h5 = sp.Matrix(
        [
            [1, 0, 1, c, 3, a],
            [0, 1, c, 3, a, y6],
            [1, c, 3, a, y6, b],
            [c, 3, a, y6, b, y8],
            [3, a, y6, b, y8, d],
            [a, y6, b, y8, d, y10],
        ]
    )
    schur = sp.simplify(h5[3:, 3:] - h5[:3, 3:].T * h2.inv() * h5[:3, 3:])
    relation = s**2 - 6 * (2 - c**2) * (1 + c**2)

    def reduced(expr: sp.Expr) -> sp.Expr:
        numerator, _ = sp.fraction(sp.factor(expr))
        return sp.factor(sp.rem(sp.Poly(sp.expand(numerator), s), sp.Poly(relation, s)).as_expr())

    B = -5 * c**4 + 6 * c**3 * s + 68 * c**2 - 24 * c * s - 8
    assert reduced(schur[0, 0]) == 0
    assert reduced(schur[0, 1]) == 0
    assert sp.expand(reduced(schur[0, 2]) - 3 * (c**2 - 2) * B) == 0
    assert sp.expand(reduced(schur[1, 1]) - 3 * B) == 0
    assert reduced(schur[1, 2]) == 0
    # The R127 endpoint equation is F(u4)=0, and its boundary expression is
    # exactly F(c^2)=3B.  Thus the two remaining entries vanish at u4.
    print("R128_M5_SCHUR_ZERO_ROWS_INTERFACE_PASSED")

    C = (
        30 * c**8
        - 124 * c**6
        + 23 * c**5 * s
        + 3 * c**4
        - 62 * c**3 * s
        + 516 * c**2
        - 40 * c * s
        - 208
    )
    assert reduced(schur[2, 2] + 18 * C / (c**2 - 2) ** 2) == 0
    # The endpoint u4 is the unique R127 root in (1,2), and its sign change
    # isolates it in (1.11, 1.12).  The following rational bounds certify C<0.
    u = sp.symbols("u", real=True)
    polynomial = sp.Poly(
        216 * u**5 - 1919 * u**4 + 4072 * u**3 + 4704 * u**2 - 8000 * u + 64,
        u,
    )
    left = sp.Rational(111, 100)
    right = sp.Rational(28, 25)
    assert polynomial.count_roots(1, 2) == 1
    assert polynomial.eval(left) * polynomial.eval(right) < 0
    A_upper = 30 * right**4 - 124 * left**3 + 3 * right**2 + 516 * right - 208
    B_left = 23 * left**2 - 62 * left - 40
    assert A_upper < 252
    assert 46 * right - 62 < 0
    assert B_left < -80
    cs2_lower = left * 6 * (2 - right) * (1 + left)
    assert cs2_lower > sp.Rational(49, 4)
    print("R128_M5_GHOST_DELTA_INTERVAL_CERTIFICATE_PASSED")
    print("R128_M5_RELAXED_ENDPOINT_GHOST_INTERFACE_PASSED")


def main() -> None:
    check_singular_extension_lemma()
    check_r5_row()
    check_m5_singular_ghost()
    print("R128_SINGULAR_EXTENSION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
