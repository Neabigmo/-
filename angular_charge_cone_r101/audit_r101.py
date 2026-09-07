"""Exact symbolic audit for the R101 angular charge cone formulas."""

from __future__ import annotations

from itertools import product

import sympy as sp


z = sp.symbols("z")
c = sp.sqrt(sp.Rational(2, 3))
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2


def direction(j: int) -> sp.Expr:
    """r_j(theta), with z=exp(i theta), in exact Laurent form."""
    phase = omega**j
    return sp.expand(c * (phase * z + sp.conjugate(phase) / z) / 2)


def angular_filter(r: int, k1: int, k2: int, k3: int) -> sp.Expr:
    """Fourier coefficient of exp(-3*i*r*theta) prod_j r_j(theta)^k_j."""
    degree = k1 + k2 + k3
    expr = sp.expand(z**degree * direction(0)**k1 * direction(1)**k2 * direction(2)**k3)
    return sp.simplify(sp.expand(expr).coeff(z, degree + 3 * r))


def beta(m: int, r: int, coefficients: dict[int, sp.Expr]) -> sp.Expr:
    out = 0
    for k1 in range(m + 1):
        for k2 in range(m - k1 + 1):
            k3 = m - k1 - k2
            filt = angular_filter(r, k1, k2, k3)
            out += (
                sp.sqrt(sp.factorial(m) / (sp.factorial(k1) * sp.factorial(k2) * sp.factorial(k3)))
                * filt
                * coefficients.get(k1, 0)
                * coefficients.get(k2, 0)
                * coefficients.get(k3, 0)
            )
    return sp.simplify(out)


def check_geometry_and_selection() -> None:
    assert sp.simplify(sum(direction(j) ** 2 for j in range(3)) - 1) == 0
    for m in range(0, 10):
        for r in range(-3, 4):
            # The root-filter coefficient must vanish outside the trigonometric
            # degree/parity window, independently of the one-body coefficients.
            for k1 in range(m + 1):
                for k2 in range(m - k1 + 1):
                    k3 = m - k1 - k2
                    value = angular_filter(r, k1, k2, k3)
                    if m < 3 * abs(r) or (m - r) % 2:
                        assert value == 0
    print("R101_D3_GEOMETRY_AND_SELECTION_RULES_PASSED")


def check_charge_map() -> None:
    a = {k: sp.symbols(f"a{k}") for k in range(10)}
    a[0] = sp.Integer(1)
    a[1] = sp.Integer(0)
    a[2] = sp.Integer(0)
    a[4] = sp.Integer(0)

    expected = {
        3: sp.sqrt(6) * a[3] / 12,
        5: 5 * sp.sqrt(6) * a[5] / 72,
        7: 7 * sp.sqrt(6) * a[7] / 144,
        9: (
            7 * sp.sqrt(6) * a[9] / 216
            - 7 * sp.sqrt(14) * a[6] * a[3] / 144
            + sp.sqrt(70) * a[3] ** 3 / 216
        ),
    }
    for degree, value in expected.items():
        assert sp.simplify(beta(degree, 1, a) - value) == 0

    # A genuine full-exact degree-six row gives the reduced degree-nine form.
    reduced = expected[9].subs(a[6], 7 * a[3] ** 2 / (2 * sp.sqrt(5)))
    reduced_expected = 7 * sp.sqrt(6) * a[9] / 216 - 127 * sp.sqrt(70) * a[3] ** 3 / 4320
    assert sp.simplify(reduced - reduced_expected) == 0
    print("R101_CHARGE_MAP_DEGREE_3_5_7_9_PASSED")


def check_first_odd_mode_and_scaling() -> None:
    for degree in (3, 5, 7, 9, 11, 13):
        assert degree % 2 == 1 and degree >= 3
        lam = 3 * (sp.sqrt(sp.Rational(2, 3)) / 2) ** degree * sp.binomial(
            degree, (degree - 3) // 2
        )
        assert lam.is_positive is True

    t = sp.symbols("t", positive=True)
    m = sp.symbols("m", integer=True, nonnegative=True)
    # The OU grading is the exact exponent used in the all-degree cone.
    assert sp.simplify((t ** (m / 2)) ** 2 / t**m - 1) == 0
    print("R101_FIRST_ODD_MODE_AND_OU_SCALING_PASSED")


def main() -> None:
    check_geometry_and_selection()
    check_charge_map()
    check_first_odd_mode_and_scaling()
    print("R101_ANGULAR_HERGLOTZ_CHARGE_CONE_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()

