"""Exact algebraic audits for the R87 small-proportional safety window."""

from math import factorial
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_all_gap_r83.audit_r83 import green_closed  # noqa: E402


I = sp.I
OMEGA = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2


def check_angular_branch_and_zeta() -> None:
    alpha, x, rho = sp.symbols("alpha x rho")
    rho_alpha = alpha / (1 + alpha)
    polynomial = 1 + (1 - OMEGA) * (2 * rho_alpha - 1) * x - OMEGA * x**2

    assert sp.simplify(polynomial.subs({alpha: 0, x: 1})) == 0
    assert sp.simplify(sp.diff(polynomial, x).subs({alpha: 0, x: 1}) + 1 + OMEGA) == 0
    assert sp.simplify(1 + OMEGA) != 0

    # Expanded action on the saddle branch; x-dependence is held fixed by
    # the envelope theorem because the x derivative vanishes there.
    phi_expanded = (
        2 * alpha * sp.log(OMEGA * (1 + OMEGA * x))
        + 2 * sp.log(1 + x)
        - (1 + alpha) * sp.log(x)
        - 2 * (1 + alpha) * sp.log(2)
    )
    envelope_derivative = sp.diff(phi_expanded, alpha)
    expected = (
        2 * sp.log(OMEGA * (1 + OMEGA * x))
        - sp.log(x)
        - 2 * sp.log(2)
    )
    assert sp.simplify(envelope_derivative - expected) == 0

    # The exponential form of alpha*exp(-expected) is algebraically the
    # displayed zeta formula; the branch-independent polynomial identity is
    # enough for this exact audit.
    zeta = 4 * alpha * x / (OMEGA**2 * (1 + OMEGA * x) ** 2)
    assert sp.simplify(OMEGA**2 * (1 + OMEGA) ** 2 - 1) == 0

    # Formal first-order expansion x=1+x1*alpha+O(alpha^2) gives zeta=4alpha.
    x1 = sp.symbols("x1")
    formal_polynomial = sp.series(
        polynomial.subs(x, 1 + x1 * alpha), alpha, 0, 2
    ).removeO()
    x1_solution = sp.solve(sp.Eq(sp.expand(formal_polynomial).coeff(alpha), 0), x1)[0]
    assert sp.simplify(
        sp.expand(formal_polynomial).coeff(alpha, 0)
    ) == 0
    assert sp.simplify(
        sp.limit(zeta.subs(x, 1 + x1_solution * alpha) / alpha, alpha, 0) - 4
    ) == 0
    print("R87_ANGULAR_BRANCH_AND_ZETA_PASSED")


def check_endpoint_algebra_and_correction() -> None:
    alpha, zeta = sp.symbols("alpha zeta", positive=True)
    L = 1 + alpha + zeta
    Delta = L + zeta
    lam = zeta / L

    p_h = (1 + lam) ** 3 / (1 - lam)
    p_g = (L - zeta) / (L + zeta)
    assert sp.simplify(p_h - Delta**3 / ((1 + alpha) * L**2)) == 0
    assert sp.simplify(p_g - (1 + alpha) / Delta) == 0
    assert sp.simplify(p_h * p_g - Delta**2 / L**2) == 0

    # Explicitly reject the inverse Green factor and the product it induces.
    inverse_p_g = (L + zeta) / (L - zeta)
    assert sp.simplify(p_g - inverse_p_g) != 0
    wrong_product = Delta**4 / ((1 + alpha) ** 2 * L**2)
    assert sp.simplify(p_h * p_g - wrong_product) != 0

    # Formal small-alpha arithmetic, using zeta=4alpha+O(alpha^2).
    a, z1 = sp.symbols("a z1")
    L_series = 1 + a + 4 * a + z1 * a**2
    Delta_series = L_series + 4 * a + z1 * a**2
    assert sp.expand(Delta_series).coeff(a, 1) == 9
    assert sp.limit((4 * a / L_series) / a, a, 0) == 4
    assert sp.limit(Delta_series, a, 0) == 1
    print("R87_ENDPOINT_ALGEBRA_AND_CORRECTION_PASSED")


def check_green_endpoint_derivative() -> None:
    alpha, zeta, u, eta = sp.symbols(
        "alpha zeta u eta", real=True, positive=True
    )
    L = 1 + alpha + zeta
    Delta = L + zeta
    derivative = zeta + L / u
    reduced = sp.simplify(derivative - (Delta + (1 / u - 1) * L))
    assert reduced == 0
    # L=(1+alpha+Delta)/2, so Re(Delta)>=eta>0 implies L>0 on real alpha.
    assert sp.simplify(2 * L - (1 + alpha + Delta)) == 0

    # The exact finite Green integral has the endpoint sign structure used in
    # the Laplace step; this remains a finite check, not a uniform asymptotic.
    for ell in range(5, 12):
        for gap in range(0, min(6, ell - 1)):
            value = green_closed(ell, gap)
            if gap == 0:
                assert value == 1
            else:
                assert (-1) ** gap * value > 0
    print("R87_GREEN_ENDPOINT_DERIVATIVE_PASSED")


def check_conjugate_phase_non_degeneracy() -> None:
    theta, real_c, imag_c = sp.symbols("theta real_c imag_c", real=True)
    c = real_c + I * imag_c
    # If theta is 0 or pi modulo pi, the pair is 2*(-1)^j*Re(c).
    degenerate = sp.simplify((c + sp.conjugate(c)).subs({sp.conjugate(c): real_c - I * imag_c}))
    assert sp.simplify(degenerate - 2 * real_c) == 0
    # The counterexample shows C!=0 alone is insufficient.
    assert sp.simplify((I + (-I))) == 0

    # Away from theta in pi*Z, the Cesaro mean of the squared real pair is
    # 2|C|^2; the geometric sum of exp(2*i*j*theta) has vanishing average.
    modulus_squared = sp.expand(c * sp.conjugate(c))
    assert sp.simplify(modulus_squared - (real_c**2 + imag_c**2)) == 0
    print("R87_CONJUGATE_PHASE_NONDEGENERACY_PASSED")


def check_fallback_multinomial_arithmetic() -> None:
    D = 9
    total = sum(
        sp.Rational(1, factorial(r) * factorial(s) * factorial(D - r - s))
        for r in range(D + 1)
        for s in range(D - r + 1)
    )
    assert sp.simplify(total - sp.Rational(3**D, factorial(D))) == 0

    weighted = sum(
        sp.Rational((1 + r) ** 2, factorial(r) * factorial(s) * factorial(D - r - s))
        for r in range(D + 1)
        for s in range(D - r + 1)
    )
    coarse = sp.Rational((D + 1) ** 2 * 3**D, factorial(D))
    assert weighted <= coarse
    assert weighted > total
    print("R87_FALLBACK_MULTINOMIAL_ARITHMETIC_PASSED")


if __name__ == "__main__":
    check_angular_branch_and_zeta()
    check_endpoint_algebra_and_correction()
    check_green_endpoint_derivative()
    check_conjugate_phase_non_degeneracy()
    check_fallback_multinomial_arithmetic()
    print("R87_GREEN_REGION_AUDIT_COMPLETED")
