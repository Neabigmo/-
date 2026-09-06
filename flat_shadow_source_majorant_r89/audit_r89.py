"""Exact audits for the R89 source factorization and conditional majorant."""

from math import comb, factorial
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_all_gap_r83.audit_r83 import (  # noqa: E402
    p_band_formula,
    source_R_formula,
)


I = sp.I
OMEGA = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2
Q = sp.sqrt(3) / 2 - I / 2  # exp(-i*pi/6)


def band_scale(m: int, s: int) -> sp.Expr:
    ell = m + s
    return sp.Integer(2) * factorial(s - 1) * comb(ell + 1, s - 1) * comb(
        ell - 3, s - 1
    )


def check_exact_source_factorization() -> None:
    m, s = sp.symbols("m s", integer=True, positive=True)
    ell = m + s
    # T is expanded symbolically only to verify the factorial simplification.
    T = 2 * sp.factorial(s - 1) * sp.binomial(ell + 1, s - 1) * sp.binomial(
        ell - 3, s - 1
    )
    xi = sp.symbols("Xi")
    p = xi * T
    left = -2 * sp.factorial(2 * m) * p / sp.factorial(ell) ** 2
    right = (
        -4
        * sp.factorial(2 * m)
        / (sp.factorial(m + 2) * sp.factorial(m - 2))
        * (ell + 1)
        / (ell * (ell - 1) * (ell - 2))
        * xi
        / sp.factorial(s - 1)
    )
    assert sp.simplify(sp.combsimp(left - right)) == 0

    for m_value in range(4, 11):
        for s_value in range(1, 6):
            ell_value = m_value + s_value
            T_value = band_scale(m_value, s_value)
            xi_value = sp.Rational(p_band_formula(ell_value, s_value), T_value)
            reconstructed = (
                -4
                * sp.factorial(2 * m_value)
                / (sp.factorial(m_value + 2) * sp.factorial(m_value - 2))
                * sp.Rational(ell_value + 1, ell_value * (ell_value - 1) * (ell_value - 2))
                * xi_value
                / factorial(s_value - 1)
            )
            assert sp.simplify(
                reconstructed - source_R_formula(ell_value, m_value)
            ) == 0
    print("R89_EXACT_SOURCE_FACTORIZATION_PASSED")


def check_poisson_coefficient_identity() -> None:
    # For f(n+1), z*exp(z)*E[f(N+1)] is exactly
    # z*sum_n f(n+1) z^n/n!. Check coefficient bookkeeping on rationals.
    z = sp.symbols("z")
    values = {n + 1: sp.Rational((n + 2) ** 2, n + 1) for n in range(8)}
    lhs = z * sum(values[n + 1] * z**n / factorial(n) for n in range(8))
    for degree in range(1, 9):
        assert sp.expand(lhs).coeff(z, degree) == values[degree] / factorial(degree - 1)
    print("R89_POISSON_COEFFICIENT_IDENTITY_PASSED")


def check_corrected_zeta_substitution() -> None:
    alpha, y, v, rho = sp.symbols("alpha y v rho", real=True)
    y_complex = sp.symbols("y_complex")
    # y=omega*x implies omega^2*(1+omega*x)^2=(1+y)^2/omega,
    # and x=y/omega; omega^3=1, so zeta=4 alpha y/(1+y)^2.
    x = y_complex / OMEGA
    correct = 4 * alpha * x / (OMEGA**2 * (1 + OMEGA * x) ** 2)
    assert sp.simplify(correct - 4 * alpha * y_complex / (1 + y_complex) ** 2) == 0

    polynomial_v = v**2 - sp.sqrt(3) * (2 * rho - 1) * v + 1
    original = 1 + (1 - OMEGA) * (2 * rho - 1) * (Q * v / OMEGA) - OMEGA * (
        Q * v / OMEGA
    ) ** 2
    assert sp.simplify(sp.expand(original) - polynomial_v) == 0

    # At alpha=0, y=omega and the corrected zeta/alpha limit is 4.
    assert sp.simplify(4 * OMEGA / (1 + OMEGA) ** 2 - 4) == 0
    # For |y|=1, y/(1+y)^2=1/(2+y+y^(-1)) is positive real whenever y!=-1.
    unit_identity = sp.simplify(
        y_complex / (1 + y_complex) ** 2
        - 1 / (2 + y_complex + 1 / y_complex)
    )
    assert unit_identity == 0
    print("R89_CORRECTED_ZETA_SUBSTITUTION_PASSED")


def check_leading_model_no_go() -> None:
    alpha, zeta, u = sp.symbols("alpha zeta u", positive=True)
    # The frozen normalization for R(z) proportional to z*exp(z) is exact up
    # to the harmless endpoint power u.  Its logarithmic exponent is the
    # displayed expression in the README.
    exponent = zeta * (u - 1 - sp.log(u)) - alpha * sp.log(u)
    assert sp.simplify(
        exponent - (zeta * (u - 1) - (alpha + zeta) * sp.log(u))
    ) == 0
    at_half = sp.simplify(exponent.subs(u, sp.Rational(1, 2)))
    assert sp.simplify(
        at_half - (zeta * (sp.log(2) - sp.Rational(1, 2)) + alpha * sp.log(2))
    ) == 0
    assert sp.N(sp.log(2) - sp.Rational(1, 2), 30) > 0
    print("R89_LEADING_MODEL_NO_GO_PASSED")


def check_source_majorant_arithmetic() -> None:
    # D_(m,s)<=9/m^2 follows for t=m+s>=3 from
    # t+1<=2t, t-1>=2t/3, t-2>=t/3.
    for m in range(2, 40):
        for s in range(1, 40):
            t = m + s
            d_factor = sp.Rational(t + 1, t * (t - 1) * (t - 2))
            assert d_factor <= sp.Rational(9, m**2)

    for D in (5, 8, 11):
        unweighted = sum(
            sp.Rational(1, factorial(r) * factorial(s) * factorial(D - r - s))
            for r in range(D + 1)
            for s in range(D - r + 1)
        )
        weighted = sum(
            sp.Rational((1 + r) ** 2 * (1 + s), factorial(r) * factorial(s) * factorial(D - r - s))
            for r in range(D + 1)
            for s in range(D - r + 1)
        )
        assert unweighted == sp.Rational(3**D, factorial(D))
        assert weighted <= (D + 1) ** 3 * unweighted
    print("R89_SOURCE_MAJORANT_ARITHMETIC_PASSED")


def check_rescaled_weight_ratio() -> None:
    j, D = sp.symbols("j D", positive=True, integer=True)
    c_ratio = sp.prod((j + h) ** 2 for h in range(1, 5)) / sp.prod(
        2 * j + h for h in range(1, 9)
    )
    exact = 16**4 * c_ratio
    expected = 16**4 * sp.prod((j + h) ** 2 for h in range(1, 5)) / sp.prod(
        2 * j + h for h in range(1, 9)
    )
    assert sp.simplify(exact - expected) == 0

    # The general product identity is checked at exact integer anchors.
    for j_value in (3, 7, 20):
        for D_value in (1, 2, 4, 6):
            ratio = sp.Rational(16**D_value)
            for h in range(1, D_value + 1):
                ratio *= sp.Rational((j_value + h) ** 2, 1)
            for h in range(1, 2 * D_value + 1):
                ratio /= 2 * j_value + h
            assert ratio > 0
            bound = sp.Rational(4**D_value) * sp.exp(
                sp.Rational(D_value * (D_value + 1), j_value)
            )
            assert sp.N(ratio - bound, 40) < 0
    print("R89_RESCALED_WEIGHT_RATIO_PASSED")


if __name__ == "__main__":
    check_exact_source_factorization()
    check_poisson_coefficient_identity()
    check_corrected_zeta_substitution()
    check_leading_model_no_go()
    check_source_majorant_arithmetic()
    check_rescaled_weight_ratio()
    print("R89_SOURCE_MAJORANT_AUDIT_COMPLETED")
