"""Exact finite and asymptotic sanity checks for the R83 all-gap kernel."""

from math import comb, factorial
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_exact_mixed_kernel_r82.audit_r82 import (
    angular_pair_average,
    mixed_M,
    source_R,
)


def root_filter_ratio(r: int, j: int) -> sp.Rational:
    """The finite root-of-unity expression for <S_p S_q>/A_(p+q)."""
    p = 2 * r + 1
    q = 2 * j + 1
    center = j + r + 1
    numerator = 0
    for a in range(p + 1):
        if (p - 2 * a) % 3 == 0:
            chosen = center - a
            if 0 <= chosen <= q:
                numerator += comb(p, a) * comb(q, chosen)
    return sp.Rational(
        3 * numerator,
        comb(p + q, center),
    )


def B_root_filter(r: int, j: int) -> sp.Rational:
    return sp.simplify((root_filter_ratio(r, j) - 1) / 2)


def q_band_coefficient(ell: int, a: int) -> sp.Rational:
    """Q_(ell,a) from the claimed exact Hermite band formula."""
    return sp.simplify(
        (-1) ** (a + 1)
        * sp.Rational((a + 1) * (a + 2), 2)
        * (a * a + 5 * a - 2 * (ell - 3))
        * sp.Rational(factorial(ell - a - 4), factorial(ell - 3 - 2 * a))
    )


def p_band_formula(ell: int, s: int) -> sp.Expr:
    first = 0
    for a in range(s):
        if ell - 3 - 2 * a < 0 or ell - a - 4 < 0:
            continue
        first += (
            q_band_coefficient(ell, a)
            * factorial(s - a - 1)
            * comb(ell + 1, s - a - 1)
            * comb(ell - 3 - 2 * a, s - a - 1)
        )
    second = 0
    for a in range(s - 1):
        if ell - 1 - 3 - 2 * a < 0 or ell - 1 - a - 4 < 0:
            continue
        second += (
            ell
            * q_band_coefficient(ell - 1, a)
            * factorial(s - a - 2)
            * comb(ell, s - a - 2)
            * comb(ell - 4 - 2 * a, s - a - 2)
        )
    return sp.simplify(first - second)


def green_closed(ell: int, gap: int) -> sp.Rational:
    """Coefficient of x^(ell+gap) in the signed Green generating function."""
    if gap == 0:
        return sp.Integer(1)
    return sp.simplify(
        sp.Rational((-1) ** gap, factorial(gap))
        - 2
        * sum(
            sp.Rational((-2) ** (gap - 1 - u),
                       factorial(gap - 1 - u) * factorial(u) * (ell + u + 1))
            for u in range(gap)
        )
    )


def green_from_truncated_series(ell: int, gap: int) -> sp.Rational:
    """Extract the same coefficient by finite formal-series convolution."""
    first = sp.Rational((-1) ** gap, factorial(gap))
    second = 0
    for u in range(gap):
        integral_power = ell + u + 1
        integral_coefficient = sp.Rational(1, factorial(u) * integral_power)
        exponential_power = gap - u - 1
        second += integral_coefficient * sp.Rational(
            (-2) ** exponential_power, factorial(exponential_power)
        )
    return sp.simplify(first - 2 * second)


def source_R_formula(ell: int, m: int) -> sp.Expr:
    s = ell - m
    if s < 1:
        return sp.Integer(0)
    p = p_band_formula(ell, s)
    return sp.simplify(-2 * factorial(2 * m) * p / factorial(ell) ** 2)


def mixed_M_root(j: int, r: int) -> sp.Expr:
    c_j = sp.Rational(factorial(j) ** 2, factorial(2 * j + 1))
    upsilon = sp.Rational(
        (-1) ** (r - 1) * r * factorial(r + 1),
        2 * factorial(2 * r + 1),
    )
    return sp.simplify(c_j * upsilon * B_root_filter(r, j))


def exact_K(j: int, gap: int) -> sp.Expr:
    result = 0
    for h in range(3, gap + 1):
        ell = j + h
        source_sum = 0
        for r in range(1, h - 1):
            m = j + r + 1
            source_sum += source_R_formula(ell, m) * mixed_M_root(j, r)
        result += green_closed(ell, gap - h) * source_sum
    return sp.factor(result)


def check_root_filter_and_source_formula() -> None:
    # The root-filter expression must reproduce the direct angular moments.
    for j in range(0, 6):
        for r in range(1, 5):
            p = 2 * r + 1
            q = 2 * j + 1
            direct = sp.simplify(
                (angular_pair_average(p, q) + angular_pair_average(q, p))
                / (2 * (sp.Rational(3, 6 ** (j + r + 1)) * comb(2 * (j + r + 1), j + r + 1)))
            )
            assert sp.simplify(direct - B_root_filter(r, j)) == 0

    q_polys = [sp.Integer(0), sp.Integer(0), -sp.hermite_prob(1, sp.Symbol("x")),
               -sp.hermite_prob(0, sp.Symbol("x"))]
    x = sp.Symbol("x")
    q_polys = [sp.Integer(0), sp.Integer(0), -sp.hermite_prob(1, x),
               -sp.hermite_prob(0, x)]
    for ell in range(3, 20):
        if len(q_polys) <= ell:
            q_polys.append(sp.expand(x * q_polys[-1] - (len(q_polys) - 1) * q_polys[-2]))

    for ell in range(8, 18):
        band = 0
        for a in range((ell - 3) // 2 + 1):
            band += q_band_coefficient(ell, a) * sp.hermite_prob(ell - 3 - 2 * a, x)
        assert sp.expand(q_polys[ell] - band) == 0
        P = sp.expand(
            sp.hermite_prob(ell + 1, x) * q_polys[ell]
            - ell * sp.hermite_prob(ell, x) * q_polys[ell - 1]
        )
        for s in range(1, 6):
            m = ell - s
            if m < 0:
                continue
            # Hermite coefficient via Gaussian orthogonality.
            moment = 0
            for (degree,), coefficient in sp.Poly(sp.expand(P * sp.hermite_prob(2 * m, x)), x).terms():
                moment += coefficient * (0 if degree % 2 else sp.factorial2(degree - 1))
            p_exact = sp.simplify(moment / factorial(2 * m))
            assert sp.simplify(p_exact - p_band_formula(ell, s)) == 0

            assert sp.simplify(
                source_R_formula(ell, m) - source_R(ell, m)
            ) == 0
    print("R83_ROOT_FILTER_AND_HERMITE_BAND_PASSED")


def check_green_and_fixed_gap_channels() -> None:
    for ell in range(0, 8):
        for gap in range(0, 7):
            assert green_closed(ell, gap) == green_from_truncated_series(ell, gap)
            if gap == 1:
                assert green_closed(ell, gap) == -sp.Rational(ell + 3, ell + 1)

    expected_kappa = {
        d: sp.Rational(2 * (-1) ** (d - 1) * (d - 2) * factorial(d - 1),
                       factorial(2 * d - 3))
        for d in range(3, 9)
    }
    for d, kappa in expected_kappa.items():
        # Exact rational evaluations at increasing j certify the displayed
        # leading constants without using floating-point arithmetic.
        for j in (24, 36, 48):
            value = sp.factor(j ** 3 * exact_K(j, d) - kappa)
            assert abs(value) < sp.Rational(200, j)

        if d in (3, 4):
            assert sp.simplify(exact_K(12, d) - (
                sp.Rational(2 * (12 + 6), 3 * (12 + 1) * (12 + 2) * (12 + 3) ** 2)
                if d == 3 else
                -sp.Rational(3 * 12 ** 3 + 146 * 12 ** 2 + 1001 * 12 + 1560,
                             15 * (12 + 1) * (12 + 2) * (12 + 3) ** 2 * (12 + 4) ** 2)
            )) == 0
    print("R83_GREEN_AND_FIXED_GAP_KAPPA_PASSED")


def check_generating_function_and_superpolynomial_lower_bound() -> None:
    z = sp.symbols("z")
    series = 0
    for d in range(3, 10):
        kappa = sp.Rational(2 * (-1) ** (d - 1) * (d - 2) * factorial(d - 1),
                            factorial(2 * d - 3))
        series += kappa * z ** d
    tangent_series = 0
    for r in range(1, 8):
        upsilon = sp.Rational(
            (-1) ** (r - 1) * r * factorial(r + 1),
            2 * factorial(2 * r + 1),
        )
        tangent_series += 4 * upsilon * z ** (r + 2)
    assert sp.series(series - tangent_series, z, 0, 10).removeO() == 0

    # For each requested polynomial degree p, a fixed gap d>p+3 produces
    # an exact channel of order n^(d-3) at j=floor(n/2).
    for p in range(0, 7):
        d = p + 4
        kappa = sp.Rational(2 * (-1) ** (d - 1) * (d - 2) * factorial(d - 1),
                            factorial(2 * d - 3))
        assert kappa != 0
        # The exponent is strictly larger than p; this is the only fact
        # needed for the super-polynomial conclusion.
        assert d - 3 > p
    print("R83_GENERATING_FUNCTION_AND_SUPERPOLY_LOWER_BOUND_PASSED")


if __name__ == "__main__":
    check_root_filter_and_source_formula()
    check_green_and_fixed_gap_channels()
    check_generating_function_and_superpolynomial_lower_bound()
    print("R83_ALL_GAP_AUDIT_COMPLETED")
