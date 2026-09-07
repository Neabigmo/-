"""Exact algebraic audit for the R126 M=3 singular-ghost theorem."""

from __future__ import annotations

import sympy as sp


def hankel_family(c: sp.Expr) -> sp.Matrix:
    return sp.Matrix(
        [
            [1, 0, 1, c],
            [0, 1, c, 3],
            [1, c, 3, 4 * c],
            [c, 3, 4 * c, 15 + 7 * c**2],
        ]
    )


def check_row_elimination() -> None:
    y3, y4, y6 = sp.symbols("y3 y4 y6", real=True)
    r2 = sp.Rational(4, 3) * (y4 - 3)
    r3 = sp.Rational(8, 9) * (y6 - 7 * y3**2 + 12 * y4 - 51)
    assert sp.solve(r2, y4)[0] == 3
    assert sp.solve(r3.subs(y4, 3), y6)[0] == 15 + 7 * y3**2
    print("R126_M3_ROW_ELIMINATION_PASSED")


def check_relaxed_radius() -> None:
    c = sp.symbols("c", real=True)
    h2 = hankel_family(c)[:3, :3]
    assert sp.factor(h2.det()) == 2 - c**2

    endpoint = hankel_family(sp.sqrt(2))
    principal = []
    for size in range(1, 5):
        for indices in sp.utilities.iterables.combinations(range(4), size):
            principal.append(sp.factor(endpoint.extract(indices, indices).det()))
    assert all(value >= 0 for value in principal)
    assert sp.factor(endpoint.det()) == 0
    print("R126_M3_RELAXED_RADIUS_SQRT2_PASSED")


def check_pd_approaching_family() -> None:
    c, u = sp.symbols("c u", real=True)
    family = hankel_family(c)
    assert sp.simplify(family.det() - 6 * (2 - c**2) * (1 + c**2)) == 0
    three_minors = [
        sp.factor(family.extract(indices, indices).det())
        for indices in sp.utilities.iterables.combinations(range(4), 3)
    ]
    assert any(sp.simplify(value - (2 - c**2)) == 0 for value in three_minors)
    assert any(sp.simplify(value - 6 * (1 + c**2)) == 0 for value in three_minors)
    assert any(sp.simplify(value - (30 + 3 * c**2)) == 0 for value in three_minors)
    assert any(
        sp.simplify(value - (18 + 14 * c**2 - 7 * c**4)) == 0
        for value in three_minors
    )
    assert sp.simplify(family.det() - 6 * (2 - c**2) * (1 + c**2)) == 0
    assert sp.factor((18 + 14 * u - 7 * u**2).subs(u, 0)) > 0
    assert sp.factor((18 + 14 * u - 7 * u**2).subs(u, 2)) > 0
    print("R126_M3_PD_APPROACHING_FAMILY_PASSED")


def check_ghost_nonflat_and_nonrepresentability() -> None:
    c = sp.sqrt(2)
    h2 = hankel_family(c)[:3, :3]
    h3 = hankel_family(c)
    kernel = sp.Matrix([-1, -c, 1])
    assert h2 * kernel == sp.zeros(3, 1)
    assert h2.rank() == 2 and h3.rank() == 3

    # The kernel relation x^2=c*x+1 would force y6=4*c^2+3=11,
    # while R3=0 at the endpoint forces y6=29.
    forced_y6 = sp.simplify(4 * c**2 + 3)
    exact_y6 = sp.simplify(15 + 7 * c**2)
    assert forced_y6 == 11
    assert exact_y6 == 29
    assert forced_y6 != exact_y6
    print("R126_M3_GHOST_NONFLAT_PASSED")
    print("R126_M3_ENDPOINT_NONREPRESENTABLE_PASSED")
    print("R126_M3_GENUINE_SUPREMUM_NOT_ATTAINED")


def main() -> None:
    check_row_elimination()
    check_relaxed_radius()
    check_pd_approaching_family()
    check_ghost_nonflat_and_nonrepresentability()
    print("R126_SINGULAR_GHOST_EXTREMUM_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
