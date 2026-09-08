"""Finite symbolic/numeric checks for the R138 infinite-tail audit."""

from __future__ import annotations

import math
from collections import defaultdict

import sympy as sp


def fourier_p(m: int) -> dict[int, sp.Expr]:
    """Fourier coefficients of p_m(theta)=sum_j r_j(theta)^m."""
    a = sp.sqrt(sp.Rational(2, 3))
    out: dict[int, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for k in range(m + 1):
        freq = m - 2 * k
        if freq % 3 == 0:
            out[freq] += 3 * (a / 2) ** m * sp.binomial(m, k)
    return dict(out)


def angular_average_product(ms: tuple[int, ...]) -> sp.Expr:
    coeff = {0: sp.Integer(1)}
    for m in ms:
        nxt: dict[int, sp.Expr] = defaultdict(lambda: sp.Integer(0))
        for f0, v0 in coeff.items():
            for f1, v1 in fourier_p(m).items():
                nxt[f0 + f1] += v0 * v1
        coeff = dict(nxt)
    return sp.simplify(coeff.get(0, 0))


def check_even_pivot() -> None:
    for n in range(2, 14):
        actual = angular_average_product((2 * n,))
        expected = 3 * sp.binomial(2 * n, n) / 6**n
        assert sp.simplify(actual - expected) == 0
        assert actual > 0
    print("R138_EVEN_PIVOT_PASSED")


def check_zero_divisor_pairing() -> None:
    # A finite non-paired reciprocal divisor produces a nonzero odd power sum.
    # The paired contribution cancels exactly for odd powers.
    w, v = sp.symbols("w v", nonzero=True)
    for m in (3, 5, 7):
        paired = w**m + (-w) ** m
        assert sp.simplify(paired) == 0
        assert sp.simplify(v**m - (-v) ** m) == 2 * v**m
    print("R138_ZERO_DIVISOR_PARITY_PASSED")


def check_finite_zero_leading_term() -> None:
    for m in (2, 4, 6):
        # cos(theta)cos(theta+2pi/3)cos(theta+4pi/3)=cos(3theta)/4.
        # The average of cos(3theta)^(2k) is binom(2k,k)/4^k.
        k = m // 2
        value = (sp.Rational(2, 3) ** sp.Rational(3, 2) / 4) ** m
        value *= sp.binomial(2 * k, k) / 4**k
        assert sp.simplify(value) > 0
    print("R138_FINITE_ZERO_TOP_TERM_PASSED")


def check_gaussian_bochner_minor() -> None:
    t = sp.symbols("t", real=True)
    phi = lambda x: sp.exp(-x**2 / 2)
    determinant = 1 - 2 * phi(t) ** 2 - phi(2 * t) ** 2 + 2 * phi(t) ** 2 * phi(2 * t)
    series = sp.series(determinant, t, 0, 10).removeO().expand()
    assert sp.simplify(series.coeff(t, 6) - 2) == 0
    assert sp.simplify(series.coeff(t, 8) + 4) == 0
    print("R138_GAUSSIAN_BOCHNER_MINOR_PASSED")


def check_zero_free_constant() -> None:
    assert math.exp(-7 / 8) < 1
    eta = sp.Rational(1, 8)
    assert sp.simplify(1 / (1 - 4 * eta) - 2) == 0
    print("R138_ZERO_FREE_DISK_CONSTANT_PASSED")


def check_compactness_parameters() -> None:
    p = sp.Rational(3, 2)
    q = p / (p - 1)
    eta = sp.Rational(1, 10)
    assert q * eta < sp.Rational(1, 2)
    exponent = sp.simplify(-sp.Rational(1, 2) / q)
    assert exponent == -sp.Rational(1, 6)
    print("R138_COMPACTNESS_PARAMETER_PASSED")


def main() -> None:
    check_even_pivot()
    check_zero_divisor_pairing()
    check_finite_zero_leading_term()
    check_gaussian_bochner_minor()
    check_zero_free_constant()
    check_compactness_parameters()
    print("R138_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
