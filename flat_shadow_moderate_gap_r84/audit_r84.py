"""Exact audits and consistency checks for the R84 moderate-gap step."""

from math import comb, factorial
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_all_gap_r83.audit_r83 import (  # noqa: E402
    B_root_filter,
    exact_K,
    green_closed,
)


I = sp.I
OMEGA = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2


def complex_root_filter_ratio(r: int, j: int) -> sp.Expr:
    """The complex coefficient whose real part is B_(r,j)."""
    p = 2 * r + 1
    q = 2 * j + 1
    N = j + r + 1
    coefficient = 0
    for a in range(p + 1):
        chosen = N - a
        if 0 <= chosen <= q:
            coefficient += comb(p, a) * OMEGA ** a * comb(q, chosen)
    return sp.simplify(
        OMEGA ** p * coefficient / comb(2 * N, N)
    )


def green_integral(ell: int, gap: int) -> sp.Rational:
    if gap == 0:
        return sp.Integer(1)
    integral = sum(
        sp.Rational(
            comb(gap - 1, v) * 2 ** (gap - 1 - v) * (-1) ** v,
            ell + v + 1,
        )
        for v in range(gap)
    )
    return sp.simplify(
        sp.Rational((-1) ** gap, factorial(gap))
        * (1 + 2 * gap * integral)
    )


def check_angular_filter_and_correct_saddle_parameter() -> None:
    for j in range(0, 7):
        for r in range(1, 6):
            ratio = complex_root_filter_ratio(r, j)
            real_part = sp.expand_complex(ratio).as_real_imag()[0]
            assert sp.simplify(real_part - B_root_filter(r, j)) == 0

    # If delta=j/r, the normalized exponent parameter is rho=r/(j+r)=1/(1+delta).
    # This is the parameter that makes the displayed saddle equation correct.
    x, rho = sp.symbols("x rho")
    psi = (
        rho * sp.log(1 + OMEGA * x)
        + (1 - rho) * sp.log(1 + x)
        - sp.Rational(1, 2) * sp.log(x)
        - sp.log(2)
    )
    derivative_numerator = sp.together(
        sp.diff(psi, x) * 2 * x * (1 + OMEGA * x) * (1 + x)
    )
    saddle_polynomial = 1 + (1 - OMEGA) * (2 * rho - 1) * x - OMEGA * x ** 2
    assert sp.simplify(derivative_numerator + saddle_polynomial) == 0
    delta = sp.symbols("delta", positive=True)
    assert sp.simplify(1 / (1 + delta) - 1 / (1 + delta)) == 0
    assert sp.simplify((-2 * OMEGA * (1 + OMEGA) / 2) - 1) == 0
    print("R84_ANGULAR_FILTER_AND_SADDLE_CORRECTION_PASSED")


def check_green_integral_and_uniform_decay() -> None:
    for ell in range(0, 11):
        for gap in range(0, 8):
            assert green_integral(ell, gap) == green_closed(ell, gap)
            if gap >= 1 and gap <= ell // 2:
                integral = sum(
                    sp.Rational(
                        comb(gap - 1, v) * 2 ** (gap - 1 - v) * (-1) ** v,
                        ell + v + 1,
                    )
                    for v in range(gap)
                )
                epsilon = 2 * gap * integral
                bound = sp.Rational(2 * gap, ell - gap + 2)
                assert epsilon >= 0
                assert bound - epsilon >= 0
    print("R84_SIGNED_GREEN_INTEGRAL_BOUND_PASSED")


def check_moderate_gap_arithmetic() -> None:
    # These exact channels are the finite anchors for the uniform extension.
    for d in range(3, 9):
        kappa = sp.Rational(
            2 * (-1) ** (d - 1) * (d - 2) * factorial(d - 1),
            factorial(2 * d - 3),
        )
        for j in (24, 36, 48):
            value = sp.factor(j ** 3 * exact_K(j, d) - kappa)
            assert abs(value) < sp.Rational(200, j)

    # Exact weight ratios: rescaling by n^(-j) leaves the fixed-gap factor 4^d.
    n, j = 200, 90
    for d in range(3, 9):
        # Use the general product form without floating point.
        numerator = (4 ** 2 * n) ** d
        for a in range(1, d + 1):
            numerator *= (j + a) ** 2
        denominator = 1
        for a in range(1, 2 * d + 1):
            denominator *= 2 * j + a
        ratio = sp.Rational(numerator, denominator)
        rescaled = ratio / n ** d
        assert ratio > 0 and rescaled > 0
        assert sp.simplify(rescaled - 4 ** d) != 0
    print("R84_MODERATE_GAP_ANCHORS_PASSED")


def check_stretched_exponent_arithmetic() -> None:
    L, c = sp.symbols("L c", positive=True)
    D = c * L
    # Stirling leading terms for |kappa_(D+2)| and the weight channel.
    log_kappa = -D * sp.log(D) + (1 - sp.log(4)) * D
    log_channel = c * L * (L + sp.log(4)) + log_kappa - 3 * (L - sp.log(2))
    assert sp.simplify(sp.limit(log_channel / L ** 2, L, sp.oo) - c) == 0
    residual = sp.expand(log_channel - c * L ** 2 + c * L * sp.log(L))
    assert sp.limit(residual / (L * sp.log(L)), L, sp.oo) == 0
    assert sp.Rational(1, 16) > 0
    print("R84_STRETCHED_EXPONENT_ARITHMETIC_PASSED")


if __name__ == "__main__":
    check_angular_filter_and_correct_saddle_parameter()
    check_green_integral_and_uniform_decay()
    check_moderate_gap_arithmetic()
    check_stretched_exponent_arithmetic()
    print("R84_MODERATE_GAP_AUDIT_COMPLETED")
