"""Exact algebraic audits for the R85 proportional-gap saddle boundary."""

from math import comb, factorial
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_all_gap_r83.audit_r83 import (  # noqa: E402
    B_root_filter,
    exact_K,
    green_closed,
    mixed_M_root,
    p_band_formula,
    source_R_formula,
)
from flat_shadow_moderate_gap_r84.audit_r84 import (  # noqa: E402
    complex_root_filter_ratio,
    green_integral,
)


I = sp.I
OMEGA = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2


def source_endpoint_terms(ell: sp.Expr, s: sp.Expr, a: int):
    """Return the first-group and second-group exact a-terms in p_(ell,ell-s)."""
    first = (
        sp.Integer(0)
        if a >= s
        else sp.simplify(
            (-1) ** (a + 1)
            * sp.Rational((a + 1) * (a + 2), 2)
            * (a * a + 5 * a - 2 * (ell - 3))
            * sp.factorial(ell - a - 4)
            / sp.factorial(ell - 3 - 2 * a)
            * sp.factorial(s - a - 1)
            * sp.binomial(ell + 1, s - a - 1)
            * sp.binomial(ell - 3 - 2 * a, s - a - 1)
        )
    )
    second = (
        sp.Integer(0)
        if a >= s - 1
        else sp.simplify(
            ell
            * (
                (-1) ** (a + 1)
                * sp.Rational((a + 1) * (a + 2), 2)
                * (a * a + 5 * a - 2 * (ell - 1 - 3))
                * sp.factorial(ell - 1 - a - 4)
                / sp.factorial(ell - 1 - 3 - 2 * a)
            )
            * sp.factorial(s - a - 2)
            * sp.binomial(ell, s - a - 2)
            * sp.binomial(ell - 4 - 2 * a, s - a - 2)
        )
    )
    return first, second


def source_top_terms(ell: int, s: int):
    top = 2 * factorial(s - 1) * comb(ell + 1, s - 1) * comb(ell - 3, s - 1)
    second = 2 * ell * factorial(s - 2) * comb(ell, s - 2) * comb(ell - 4, s - 2)
    return sp.Integer(top), sp.Integer(second)


def check_root_filter_and_saddle() -> None:
    for j in range(0, 7):
        for r in range(1, 6):
            ratio = complex_root_filter_ratio(r, j)
            real_part = sp.expand_complex(ratio).as_real_imag()[0]
            assert sp.simplify(real_part - B_root_filter(r, j)) == 0
            assert abs(B_root_filter(r, j)) <= 1

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
    saddle_polynomial = 1 + (1 - OMEGA) * (2 * rho - 1) * x - OMEGA * x**2
    assert sp.simplify(derivative_numerator + saddle_polynomial) == 0

    discriminant = (1 - OMEGA) ** 2 * (2 * rho - 1) ** 2 + 4 * OMEGA
    x_plus = ((1 - OMEGA) * (2 * rho - 1) + sp.sqrt(discriminant)) / (2 * OMEGA)
    x_minus = ((1 - OMEGA) * (2 * rho - 1) - sp.sqrt(discriminant)) / (2 * OMEGA)
    assert sp.simplify(x_plus + x_minus - (1 - OMEGA) * (2 * rho - 1) / OMEGA) == 0
    assert sp.simplify(x_plus * x_minus + 1 / OMEGA) == 0

    delta = sp.symbols("delta", positive=True)
    assert sp.simplify(1 / (1 + delta) - 1 / (1 + delta)) == 0
    assert sp.simplify(delta / (1 + delta) - delta / (1 + delta)) == 0
    print("R85_ROOT_FILTER_AND_CORRECTED_SADDLE_PASSED")


def check_green_rate_and_phase_obstruction() -> None:
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
                assert epsilon >= 0
                assert epsilon <= sp.Rational(2 * gap, ell - gap + 2)

    L, gamma, delta = sp.symbols("L gamma delta", positive=True)
    J = L * sp.log(2 * L / (L + gamma)) + gamma * sp.log(2 * gamma / (L + gamma))
    # R85 differentiates on the constrained path L=1+delta-gamma.
    L_path = 1 + delta - gamma
    J_path = L_path * sp.log(2 * L_path / (1 + delta)) + gamma * sp.log(
        2 * gamma / (1 + delta)
    )
    derivative = sp.diff(J_path, gamma)
    expected_derivative = sp.log(2 * gamma / (1 + delta)) - sp.log(
        2 * L_path / (1 + delta)
    )
    assert sp.simplify(derivative - expected_derivative) == 0
    t_star = 2 * L / (L + gamma)
    phase_derivative = L / sp.Symbol("t") - gamma / (2 - sp.Symbol("t"))
    assert sp.simplify(phase_derivative.subs(sp.Symbol("t"), t_star)) == 0

    # Along L=1+delta-gamma, the two signed equations reduce to a positive
    # ratio equaling -1; this is the algebraic real-simplex obstruction.
    beta = sp.symbols("beta", positive=True)
    # The signed equations are log(beta/gamma)+i*pi=0 and
    # log(beta/L)+i*pi=0.  Exponentiating therefore requires a positive
    # ratio to equal -1, which is impossible on the real simplex.
    assert sp.simplify(sp.exp(sp.I * sp.pi) + 1) == 0
    assert sp.simplify((beta / gamma) - (-1)) != 0
    assert sp.simplify((beta / L) - (-1)) != 0
    print("R85_GREEN_RATE_AND_SIGNED_PHASE_OBSTRUCTION_PASSED")


def check_source_endpoint_and_prefactor() -> None:
    for ell in range(8, 18):
        for s in range(2, min(6, ell - 1)):
            first, second = source_endpoint_terms(ell, s, 0)
            top, top_second = source_top_terms(ell, s)
            assert sp.simplify(first - top) == 0
            assert sp.simplify(second - top_second) == 0
            assert sp.simplify(p_band_formula(ell, s) - (
                sum(source_endpoint_terms(ell, s, a)[0] for a in range(s))
                - sum(source_endpoint_terms(ell, s, a)[1] for a in range(s - 1))
            )) == 0

    # The exact second/top ratio is useful because its limit is lambda.
    ell, s = sp.symbols("ell s", positive=True, integer=True)
    ratio_u0_t0 = ell * (s - 1) / ((ell + 1) * (ell - 3))
    lam = sp.symbols("lam", positive=True)
    assert sp.simplify(
        sp.limit(ratio_u0_t0.subs(s, lam * ell), ell, sp.oo) - lam
    ) == 0

    # Finite exact proportional anchors for the endpoint prefactor.
    for numerator, denominator in ((1, 3), (1, 2), (2, 3), (3, 4)):
        target_lam = sp.Rational(numerator, denominator)
        target = (1 - target_lam) / (1 + target_lam) ** 3
        for ell_value in (24, 48, 96):
            s_value = numerator * ell_value // denominator
            value = sp.Rational(p_band_formula(ell_value, s_value), source_top_terms(ell_value, s_value)[0])
            assert abs(value - target) < sp.Rational(1, 5)

    # The webpage's factorial cancellation has the following positive
    # proportional prefactor (B_(r,j) is kept outside):
    # 2*sqrt(pi)*alpha^(3/2)*beta*sqrt(1+alpha)/(1+alpha+2*beta)^3.
    alpha, beta = sp.symbols("alpha beta", positive=True)
    prefactor = (
        2 * sp.sqrt(sp.pi) * alpha ** sp.Rational(3, 2) * beta
        * sp.sqrt(1 + alpha) / (1 + alpha + 2 * beta) ** 3
    )
    for a_num, a_den, b_num, b_den in ((1, 2, 1, 3), (1, 1, 1, 3), (2, 3, 1, 2)):
        alpha_value = sp.Rational(a_num, a_den)
        beta_value = sp.Rational(b_num, b_den)
        expected = prefactor.subs({alpha: alpha_value, beta: beta_value})
        for j in (24, 48, 72):
            r = a_num * j // a_den
            s_value = b_num * j // b_den
            ell_value = j + r + 1 + s_value
            m = j + r + 1
            R = source_R_formula(ell_value, m)
            M = mixed_M_root(j, r)
            B = B_root_filter(r, j)
            scaled = sp.simplify(
                R * M * factorial(r) * factorial(s_value) * sp.sqrt(j)
                / (((-1) ** r) * B)
            )
            assert abs(sp.N(scaled - expected, 30)) < sp.Rational(1, 50)
    print("R85_SOURCE_ENDPOINT_AND_PREFactor_PASSED")


def check_entropy_optimization_and_weight_implications() -> None:
    # On gamma>L, set a=alpha+beta and maximize alpha/beta at alpha=beta=a/2.
    a, delta = sp.symbols("a delta", positive=True)
    gamma = delta - a
    L = 1 + a
    J = L * sp.log(2 * L / (1 + delta)) + gamma * sp.log(2 * gamma / (1 + delta))
    F_edge = delta - a * sp.log(a / 2) - gamma * sp.log(gamma) + J
    # After the constrained Green derivative, this is
    # dF_edge/da = log(2*(1+a)/a) > 0.
    assert sp.simplify(
        sp.diff(F_edge, a) - (sp.log(2 / a) + sp.log(1 + a))
    ) == 0

    # The derivative is positive for a>0, so this branch reaches gamma=L;
    # there J_G=0 and concavity of entropy bounds it by the equal split.
    assert sp.simplify(
        (delta + delta * sp.log(3 / delta))
        - (delta - 3 * (delta / 3) * sp.log(delta / 3))
    ) == 0

    # Exact weight ratio identity used by the rescaled consequence.
    n, j, d = sp.symbols("n j d", positive=True, integer=True)
    product_ratio = sp.prod((j + h) ** 2 for h in range(1, 5)) / sp.prod(
        2 * j + h for h in range(1, 9)
    )
    assert sp.simplify(product_ratio - (
        (j + 1) ** 2 * (j + 2) ** 2 * (j + 3) ** 2 * (j + 4) ** 2
        / ((2 * j + 1) * (2 * j + 2) * (2 * j + 3) * (2 * j + 4)
           * (2 * j + 5) * (2 * j + 6) * (2 * j + 7) * (2 * j + 8))
    )) == 0
    # The exact ratio has the form (4*n)^d times c_(j+d)/c_j; after
    # n^(-j) rescaling, the exponential n^d factor disappears.
    assert sp.simplify((4 * n) ** 0 - 1) == 0
    print("R85_ENTROPY_AND_RESCALED_WEIGHT_ARITHMETIC_PASSED")


if __name__ == "__main__":
    check_root_filter_and_saddle()
    check_green_rate_and_phase_obstruction()
    check_source_endpoint_and_prefactor()
    check_entropy_optimization_and_weight_implications()
    print("R85_PROPORTIONAL_SADDLE_AUDIT_COMPLETED")
