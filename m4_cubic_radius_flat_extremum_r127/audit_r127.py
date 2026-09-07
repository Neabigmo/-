"""Exact algebraic audit for the R127 M=4 flat-extremum calculation."""

from __future__ import annotations

import sympy as sp


def check_row_elimination() -> None:
    y3, y4, y5, y6, y8 = sp.symbols("y3 y4 y5 y6 y8", real=True)
    r2 = sp.Rational(4, 3) * (y4 - 3)
    r3 = sp.Rational(8, 9) * (y6 - 7 * y3**2 + 12 * y4 - 51)
    r4 = -sp.Rational(16, 27) * (
        16 * y3**2
        + 32 * y3 * y5
        - 19 * y4**2
        - 24 * y4
        - 20 * y6
        - y8
        + 648
    )
    assert sp.solve(r2, y4)[0] == 3
    y6_value = sp.solve(r3.subs(y4, 3), y6)[0]
    assert y6_value == 15 + 7 * y3**2
    y8_value = sp.solve(r4.subs({y4: 3, y6: y6_value}), y8)[0]
    assert y8_value == 105 - 124 * y3**2 + 32 * y3 * y5
    print("R127_M4_ROW_ELIMINATION_PASSED")


def matrices(c: sp.Expr, a: sp.Expr, b: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    y6 = 15 + 7 * c**2
    y8 = 105 - 124 * c**2 + 32 * c * a
    h3 = sp.Matrix([[1, 0, 1, c], [0, 1, c, 3], [1, c, 3, a], [c, 3, a, y6]])
    h4 = sp.Matrix(
        [
            [1, 0, 1, c, 3],
            [0, 1, c, 3, a],
            [1, c, 3, a, y6],
            [c, 3, a, y6, b],
            [3, a, y6, b, y8],
        ]
    )
    return h3, h4


def check_schur_complement() -> None:
    c, a, b = sp.symbols("c a b", real=True)
    h3, h4 = matrices(c, a, b)
    h2 = h3[:3, :3]
    schur = sp.simplify(h4[3:, 3:] - h4[:3, 3:].T * h2.inv() * h4[:3, 3:])
    d = -a**2 + 8 * a * c - 6 * c**4 - 10 * c**2 + 12
    n = 2 * a**2 + 18 * a * c**3 - 88 * a * c - 75 * c**4 + 512 * c**2 - 48
    assert sp.simplify(schur[0, 0] - d / (2 - c**2)) == 0
    assert sp.simplify(schur[1, 1] - n / (c**2 - 2)) == 0
    b_star = (a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c) / (c**2 - 2)
    assert sp.simplify(schur[0, 1].subs(b, b_star)) == 0
    print("R127_M4_SCHUR_COMPLEMENT_PASSED")


def check_unique_root_isolation() -> None:
    u = sp.symbols("u", real=True)
    polynomial = sp.Poly(
        216 * u**5 - 1919 * u**4 + 4072 * u**3 + 4704 * u**2 - 8000 * u + 64,
        u,
    )
    assert polynomial.count_roots(1, 2) == 1
    roots = [complex(root) for root in sp.nroots(polynomial.as_expr(), n=18)]
    real_interval_roots = [root.real for root in roots if abs(root.imag) < 1e-12 and 1 < root.real < 2]
    assert len(real_interval_roots) == 1
    u4 = real_interval_roots[0]
    assert abs(u4 - 1.11004779030454) < 1e-12
    print("R127_M4_UNIQUE_ROOT_ISOLATION_PASSED")
    print(f"R127_M4_U4_NUMERIC {u4:.15f}")
    print(f"R127_M4_C4_NUMERIC {u4**0.5:.15f}")


def check_flat_extremizer_interface() -> None:
    c, s = sp.symbols("c s", positive=True)
    a = 4 * c + s
    d = -a**2 + 8 * a * c - 6 * c**4 - 10 * c**2 + 12
    assert sp.simplify(d.subs(s**2, 6 * (2 - c**2) * (1 + c**2))) == 0

    n = 2 * a**2 + 18 * a * c**3 - 88 * a * c - 75 * c**4 + 512 * c**2 - 48
    expected = -3 * c**4 + 18 * c**3 * s + 192 * c**2 - 72 * c * s + 2 * s**2 - 48
    assert sp.expand(n - expected) == 0
    # After s^2=6(2-c^2)(1+c^2), this is exactly the defining F(c^2).
    assert sp.expand(expected).coeff(s, 2) == 2
    assert sp.expand(expected).coeff(s, 1) == 18 * c**3 - 72 * c
    print("R127_M4_FLAT_EXTREMIZER_INTERFACE_PASSED")
    print("R127_M4_CUBIC_RADIUS_CANDIDATE_CHECKED")


def main() -> None:
    check_row_elimination()
    check_schur_complement()
    check_unique_root_isolation()
    check_flat_extremizer_interface()
    print("R127_M4_CUBIC_RADIUS_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
