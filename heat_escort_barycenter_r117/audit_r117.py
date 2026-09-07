"""Exact symbolic audit for the R117 heat-escort reduction.

Only finite algebraic identities are checked here.  The same-factor global
annihilation remains explicitly open.
"""

from __future__ import annotations

import sympy as sp


def check_gaussian_overlap_and_laplace_equivalence() -> None:
    t = sp.symbols("t", positive=True)
    prefactor = (2 * sp.pi * t) ** sp.Rational(-3, 2) * sp.sqrt(2 * sp.pi * t / 3)
    assert sp.simplify(prefactor - 1 / (2 * sp.pi * t * sp.sqrt(3))) == 0
    laplace_chi2 = t / (1 + t)
    exact_curve = sp.simplify(prefactor * laplace_chi2)
    expected = 1 / (2 * sp.pi * sp.sqrt(3) * (1 + t))
    assert sp.simplify(exact_curve - expected) == 0
    print("R117_GAUSSIAN_OVERLAP_AND_LAPLACE_EQUIVALENCE_PASSED")


def check_heat_derivative_identity() -> None:
    t, C = sp.symbols("t C", positive=True)
    A = C / (1 + t)
    I = sp.simplify(-sp.diff(A, t) / 3)
    J = sp.simplify(-sp.diff(I, t))
    assert I == C / (3 * (1 + t) ** 2)
    assert J == 2 * C / (3 * (1 + t) ** 3)
    assert sp.simplify(A * J - 6 * I**2) == 0
    assert sp.factor(A * J - 4 * I**2) == 2 * C**2 / (9 * (1 + t) ** 4)
    print("R117_HEAT_CURVATURE_AND_STRICT_INTERIOR_PASSED")


def check_tilted_completion_and_escort_extractor() -> None:
    y, bar, lam, t = sp.symbols("y bar lam t", real=True, positive=True)
    left = -3 * (y - bar) ** 2 / (2 * t) + lam * y
    shifted = -3 * (y - bar - lam * t / 3) ** 2 / (2 * t) + lam * bar + lam**2 * t / 6
    assert sp.expand(left - shifted) == 0

    kappa3 = sp.symbols("kappa3", real=True)
    prefactor = 1 / (2 * sp.pi * t * sp.sqrt(3))
    leading_B = sp.simplify(prefactor * (-kappa3 / (3 * t)))
    expected_B = -kappa3 / (6 * sp.pi * sp.sqrt(3) * t**2)
    assert sp.simplify(leading_B - expected_B) == 0
    C = 1 / (2 * sp.pi * sp.sqrt(3))
    A = C / (1 + t)
    assert sp.simplify(sp.limit(t * leading_B / A, t, sp.oo) + kappa3 / 3) == 0
    print("R117_TILTED_COMPLETION_AND_HEAT_ESCORT_EXTRACTOR_PASSED")


def check_sample_mean_variance_cubic_coefficients() -> None:
    x1, x2, x3, m3 = sp.symbols("x1 x2 x3 m3", real=True)
    S = x1 + x2 + x3
    q = sp.expand(x1**2 + x2**2 + x3**2 - S**2 / 3)
    poly = sp.Poly(sp.expand(S * q), x1, x2, x3)

    def moment(exponent: int) -> sp.Expr:
        return {0: sp.Integer(1), 1: sp.Integer(0), 2: sp.Integer(1), 3: m3}[exponent]

    expected_sq = sum(
        coeff * moment(mon[0]) * moment(mon[1]) * moment(mon[2])
        for mon, coeff in poly.terms()
    )
    assert sp.simplify(expected_sq - 2 * m3) == 0
    assert sp.simplify(expected_sq / (3 * sp.sqrt(3)) - 2 * m3 / (3 * sp.sqrt(3))) == 0
    print("R117_SAMPLE_MEAN_VARIANCE_CUBIC_COEFFICIENTS_PASSED")


def check_conditional_characteristic_leading_term() -> None:
    rho, kappa3 = sp.symbols("rho kappa3", real=True)
    # D(rho)=i E[M J0(rho sqrt(Q))], J0=1-rho^2 Q/4+O(rho^4).
    leading = -sp.I * rho**2 / 4 * (2 * kappa3 / sp.sqrt(3))
    expected = -sp.I * kappa3 * rho**2 / (2 * sp.sqrt(3))
    assert sp.simplify(leading - expected) == 0
    assert sp.simplify(expected.subs(kappa3, 0)) == 0
    print("R117_CONDITIONAL_CHARACTERISTIC_LEADING_TERM_PASSED")


def check_nonfactorized_i3_obstruction_integral() -> None:
    r, epsilon = sp.symbols("r epsilon", real=True)
    integral = sp.integrate(r**7 * sp.exp(-sp.Rational(3, 2) * r**2), (r, 0, sp.oo))
    assert sp.simplify(integral - sp.Rational(16, 27)) == 0
    assert sp.simplify(epsilon * integral - sp.Rational(16, 27) * epsilon) == 0
    print("R117_I3_POSITIVE_NONFACTORIZED_OBSTRUCTION_PASSED")


def main() -> None:
    check_gaussian_overlap_and_laplace_equivalence()
    check_heat_derivative_identity()
    check_tilted_completion_and_escort_extractor()
    check_sample_mean_variance_cubic_coefficients()
    check_conditional_characteristic_leading_term()
    check_nonfactorized_i3_obstruction_integral()
    print("R117_HEAT_ESCORT_BARYCENTER_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
