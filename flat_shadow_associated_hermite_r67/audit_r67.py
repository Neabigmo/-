"""R67 exact audit of the associated-Hermite projection asymptotics.

The script verifies the all-degree formulas at finite symbolic stages and
checks the normalization of the Riemann-sum limit.  It does not use beta_11,
degree-22 norm ratios, or numerical sweeps.
"""

from fractions import Fraction
from math import factorial, sqrt, pi
from pathlib import Path
import sys

import sympy as sp


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "flat_shadow_quadratic_response_r65"))
from audit_r65 import u, M as M_r65  # noqa: E402


x = sp.symbols("x")


def H(n):
    return sp.hermite_prob(n, x)


def gaussian_norm(poly):
    value = sp.Integer(0)
    for (degree,), coefficient in sp.Poly(sp.expand(poly**2), x).terms():
        value += coefficient * (sp.Integer(1) if degree == 0 else sp.factorial2(degree - 1))
    return sp.expand(value)


def q_sequence(limit):
    q = [sp.Integer(0), sp.Integer(0), -H(1), -H(0)]
    for n in range(3, limit):
        q.append(sp.expand(x * q[-1] - n * q[-2]))
    return q[: limit + 1]


def associated(m, c):
    values = [sp.Integer(0), sp.Integer(1)]
    for r in range(0, m):
        values.append(sp.expand(x * values[-1] - (r + c) * values[-2]))
    return values[m + 1]


def associated_hermite_expansion(m, c):
    return sp.expand(sum(
        (-1)**j * sp.binomial(m - j, j) * sp.rf(c, j) * H(m - 2*j)
        for j in range(m // 2 + 1)
    ))


def c_formula(m, j):
    return (
        (-1)**(j + 1)
        * sp.Rational((j + 1) * (j + 2) * (j*j + 5*j - 2*m), 2)
        * sp.factorial(m - j - 1)
        / sp.factorial(m - 2*j)
    )


def q_closed(n):
    m = n - 3
    return sp.expand(sum(
        c_formula(m, j) * H(m - 2*j)
        for j in range(m // 2 + 1)
    ))


def check_associated_expansion_and_q_formula():
    for c in (3, 4):
        for m in range(0, 15):
            assert associated(m, c) == associated_hermite_expansion(m, c)
    q = q_sequence(19)
    for n in range(4, 19):
        assert q[n] == q_closed(n)
    print("R67_ASSOCIATED_HERMITE_AND_Q_CLOSED_FORM PASSED")


def check_positive_norm_sum():
    q = q_sequence(19)
    for n in range(4, 19):
        m = n - 3
        norm_from_q = gaussian_norm(q[n])
        norm_from_sum = sum(
            c_formula(m, j)**2 * factorial(m - 2*j)
            for j in range(m // 2 + 1)
        )
        assert norm_from_q == sp.expand(norm_from_sum)
        assert all(c_formula(m, j)**2 * factorial(m - 2*j) >= 0
                   for j in range(m // 2 + 1))
    print("R67_POSITIVE_P_AND_P_N_FINITE_SUM PASSED")


def rho(m, j):
    return sp.Rational(m**5 * factorial(m - j - 1)**2,
                       factorial(m - 2*j) * factorial(m + 3))


def rho_product(m, j):
    numerator = sp.prod(
        sp.Rational(m - ell, m) for ell in range(j + 1, 2*j)
    )
    denominator = sp.prod(
        sp.Rational(m - ell, m) for ell in range(-3, j + 1)
    )
    return sp.factor(numerator / denominator)


def term(m, j):
    polynomial = (j + 1) * (j + 2) * (j*j + 5*j - 2*m)
    return sp.Rational(1, 4) * polynomial**2 * sp.factorial(m - j - 1)**2 / (
        sp.factorial(m - 2*j) * sp.factorial(m + 3)
    )


def check_rho_and_riemann_normalization():
    for m in range(1, 30):
        for j in range(m // 2 + 1):
            assert rho(m, j) == rho_product(m, j)
            F = sp.Rational(1, 4) * (
                sp.Rational((j + 1)**2 * (j + 2)**2, m**2)
                * sp.Rational((j*j + 5*j - 2*m)**2, m**2)
                * rho(m, j)
            )
            assert sp.expand(m * term(m, j) - F) == 0
    print("R67_RHO_PRODUCT_AND_RIEMANN_TERM_NORMALIZATION PASSED")


def check_limit_constant():
    integral = sp.Rational(1, 4) * (
        sp.Rational(105, 32) - 4 * sp.Rational(15, 16)
        + 4 * sp.Rational(3, 8)
    ) * sp.sqrt(sp.pi)
    assert sp.simplify(integral - sp.Rational(33, 128) * sp.sqrt(sp.pi)) == 0
    print("R67_SQRT_PI_CONSTANT_33_OVER_128_PASSED")


def check_targeted_exact_normalization():
    q = q_sequence(501)
    targets = (100, 200, 500)
    constant = 33 * sqrt(pi) / 128
    values = []
    for n in targets:
        p = float(gaussian_norm(q[n]) / factorial(n))
        values.append((n, sqrt(n) * p, abs(sqrt(n) * p - constant)))
    assert all(error < 0.002 for _, _, error in values)
    print("R67_TARGETED_EXACT_P_ASYMPTOTIC_ORIENTATION", values)


if __name__ == "__main__":
    check_associated_expansion_and_q_formula()
    check_positive_norm_sum()
    check_rho_and_riemann_normalization()
    check_limit_constant()
    check_targeted_exact_normalization()
    print("R67_ASSOCIATED_HERMITE_AUDIT_COMPLETED")
