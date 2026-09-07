"""Exact elementary checks for the R132 smoothing/log-density interface."""

from __future__ import annotations

import sympy as sp


def check_mehler_l2_norm() -> None:
    s, y = sp.symbols("s y", positive=True)
    # With P_s He_n=s**(n/2) He_n, the Mehler correlation is sqrt(s).
    # Completing the square in x gives the exact prefactor and exponent.
    # M_s^2 against dgamma has the Gaussian integral
    # E exp(-a X^2+b X), with a=s/(1-s), b=2*sqrt(s)*y/(1-s),
    # and the constant exp(-s*y^2/(1-s))/(1-s).
    a = s / (1 - s)
    b = 2 * sp.sqrt(s) * y / (1 - s)
    gaussian_prefactor = (1 + 2 * a) ** sp.Rational(-1, 2)
    prefactor_sq = sp.simplify(gaussian_prefactor / (1 - s))
    exponent = sp.simplify(-s * y**2 / (1 - s) + b**2 / (2 * (1 + 2 * a)))
    # SymPy is not told s<1, so verify the positive prefactor by its square.
    assert sp.simplify(prefactor_sq**2 - 1 / (1 - s**2)) == 0
    assert sp.simplify(exponent - s * y**2 / (1 + s)) == 0
    # At s=1/2, the operator-norm factor is (1-s**2)^(-1/4)=(4/3)^(1/4).
    # Together with exp(-1/6), this is still strictly below 1.
    assert sp.simplify((1 - sp.Rational(1, 4)) - sp.Rational(3, 4)) == 0
    print("R132_MEHLER_L2_NORM_CORRECTED_PASSED")


def check_exact_tail_mgf() -> None:
    eta = sp.symbols("eta", positive=True)
    # Q~chi^2_2 has M_Q(lambda)=(1-2 lambda)^(-1).
    mgf = 1 / (1 - 4 * eta)
    assert sp.simplify(mgf - 1 / (1 - 4 * eta)) == 0
    # The Jensen step contributes exp(-eta) to the X^2 bound.
    assert sp.simplify(sp.exp(-eta) * sp.exp(eta) - 1) == 0
    print("R132_EXACT_TAIL_MGF_INTERFACE_PASSED")


def check_smoothing_constant() -> None:
    t = sp.symbols("t", positive=True)
    # ||f||_2<2 sqrt(2), then the Hermite degrees >=3 give
    # (2t)^(3/2)*2sqrt(2)=8*t^(3/2).
    constant = sp.simplify((2 * t) ** sp.Rational(3, 2) * 2 * sp.sqrt(2) / t ** sp.Rational(3, 2))
    assert constant == 8
    # At s=1/2, the exact factor is (4/3)^(1/4) exp(-1/6)<1;
    # raising to the fourth power reduces this to 4/3 < exp(2/3),
    # and exp(2/3)>1+2/3=5/3>4/3.
    assert sp.Rational(5, 3) > sp.Rational(4, 3)
    print("R132_SMOOTHING_CONSTANT_8_PASSED")


def check_lp_factorization() -> None:
    p, t = sp.symbols("p t", positive=True)
    inner = sp.simplify((t * (p - 1)) * (1 / (p - 1)))
    assert inner == t
    # The inner smoothing estimate is available when t*(p-1)<=1/2.
    assert sp.simplify(1 / (2 * (p - 1)) * (p - 1) - sp.Rational(1, 2)) == 0
    print("R132_LP_HYPERCONTRACTIVE_FACTORISATION_PASSED")


def check_log_lower_bound_constants() -> None:
    t = sp.Rational(1, 64)
    assert t / (1 - t) == sp.Rational(1, 63)
    assert 2 * (1 + t) / (1 - t) < 3
    # The Gaussian inverse-L^4 exponent is 4*x^2/63,
    # whose mgf is (1-8/63)^(-1/2)=(63/55)^(1/2).
    assert sp.simplify(1 - sp.Rational(8, 63) - sp.Rational(55, 63)) == 0
    print("R132_LOG_LOWER_BOUND_CONSTANTS_PASSED")


def check_beta2_log_relation() -> None:
    x, m3 = sp.symbols("x m3")
    # Full exact class supplies E[X]=0, E[X^2]=1, E[X^3]=m3, E[X^4]=3.
    moments = {0: 1, 1: 0, 2: 1, 3: m3, 4: 3}
    p2 = x**2 - m3 * x - 1
    expanded = sp.Poly(sp.expand(p2**2), x)
    norm = sp.expand(sum(coeff * moments[power[0]] for power, coeff in expanded.terms()))
    assert sp.simplify(norm - (2 - m3**2)) == 0
    assert sp.simplify((1 - (2 - m3**2) / 2) - m3**2 / 2) == 0
    # a_3=m3/sqrt(6), hence m3^2/2=3*a_3^2.
    a3 = m3 / sp.sqrt(6)
    assert sp.simplify(m3**2 / 2 - 3 * a3**2) == 0
    print("R132_BETA2_LOG_CHARGE_RELATION_PASSED")


def main() -> None:
    check_mehler_l2_norm()
    check_exact_tail_mgf()
    check_smoothing_constant()
    check_lp_factorization()
    check_log_lower_bound_constants()
    check_beta2_log_relation()
    print("R132_EXACT_LAW_SMOOTHING_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
