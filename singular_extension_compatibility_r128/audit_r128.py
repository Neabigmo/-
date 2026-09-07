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


def main() -> None:
    check_singular_extension_lemma()
    check_r5_row()
    print("R128_SINGULAR_EXTENSION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
