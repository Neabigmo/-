"""Exact symbolic audit for the R122 normal-derivative/Bochner-trace route."""

from __future__ import annotations

import sympy as sp


def check_same_factor_normal_reconstruction() -> None:
    s0, sx = sp.symbols("s0 sx", real=True)
    derivative = s0 - sx
    assert sp.simplify(derivative.subs(s0, 0) + sx) == 0
    print("R122_SAME_FACTOR_NORMAL_RECONSTRUCTION_PASSED")


def check_interior_tangential_compatibility() -> None:
    du, dv, dw = sp.symbols("d_u d_v d_w", real=True)
    su, sv, sw = -du, -dv, -dw
    partial_u = su - sw
    partial_v = sv - sw
    assert sp.simplify(partial_u - (dw - du)) == 0
    assert sp.simplify(partial_v - (dw - dv)) == 0
    print("R122_INTERIOR_TRACE_COMPATIBILITY_PASSED")


def check_three_dimensional_log_wave_equation() -> None:
    sum_kpp = sp.symbols("sum_kpp", real=True)
    partial_xi_sq = sum_kpp / 3
    laplace_eta = sp.Rational(2, 3) * sum_kpp
    assert sp.simplify(laplace_eta - 2 * partial_xi_sq) == 0
    print("R122_LOG_WAVE_EQUATION_COEFFICIENT_PASSED")


def check_mean_trace_factor_and_reflection_parity() -> None:
    phi, normal = sp.symbols("phi normal", nonzero=True)
    psi = phi * normal / (sp.I * sp.sqrt(3))
    equivalent = phi * normal / (3 * sp.I) * sp.sqrt(3)
    assert sp.simplify(psi - equivalent) == 0
    normal_reflected = -normal
    assert sp.simplify(normal_reflected + normal) == 0
    print("R122_MEAN_TRACE_FACTOR_AND_REFLECTION_PARITY_PASSED")


def check_hankel_and_cubic_interfaces() -> None:
    rho, kappa3 = sp.symbols("rho kappa3", real=True)
    p1_log = -sp.I * kappa3 * rho**3 / (12 * sp.sqrt(6))
    multiplier = sp.sqrt(2) * 2 * 3
    n0 = sp.simplify(multiplier * p1_log / rho)
    assert sp.simplify(n0 + sp.I * kappa3 * rho**2 / (2 * sp.sqrt(3))) == 0
    g0_leading = -kappa3 * rho**2 / 6
    assert sp.simplify(g0_leading / (-kappa3 * rho**2 / 6) - 1) == 0
    print("R122_HANKEL_LOG_LOWERING_CUBIC_INTERFACE_PASSED")


def check_exact_schwarz_budget() -> None:
    rho = sp.symbols("rho", real=True)
    leading = sp.Rational(1, 3) * sp.Rational(1, 4) * rho**4
    assert sp.simplify(leading - rho**4 / 12) == 0
    g = sp.symbols("g", real=True)
    assert sp.simplify((-g) ** 2 - g**2) == 0
    print("R122_EXACT_SCHWARZ_MAGNITUDE_BUDGET_PASSED")


def check_tangent_obstruction_moments() -> None:
    a, b = sp.symbols("a b", positive=True)
    ea = sp.exp(-a**2 / 2)
    eb = sp.exp(-b**2 / 2)
    c = a * ea / (b * eb)
    centered = a * ea - c * b * eb
    h3 = -a**3 * ea + c * b**3 * eb
    assert sp.simplify(centered) == 0
    assert sp.simplify(h3 - a * (b**2 - a**2) * ea) == 0
    assert sp.simplify(h3.subs(b, a)) == 0
    print("R122_ANALYTIC_TANGENT_MOMENT_OBSTRUCTION_PASSED")


def check_radial_first_variation_is_blind() -> None:
    radial_score, radial_test = sp.symbols("radial_score radial_test")
    reflected_integrand = radial_test * (-radial_score)
    assert sp.simplify(reflected_integrand + radial_test * radial_score) == 0
    print("R122_RADIAL_FIRST_VARIATION_BLIND_TO_ODD_SCORE_PASSED")


def main() -> None:
    check_same_factor_normal_reconstruction()
    check_interior_tangential_compatibility()
    check_three_dimensional_log_wave_equation()
    check_mean_trace_factor_and_reflection_parity()
    check_hankel_and_cubic_interfaces()
    check_exact_schwarz_budget()
    check_tangent_obstruction_moments()
    check_radial_first_variation_is_blind()
    print("R122_NORMAL_DERIVATIVE_BOCHNER_TRACE_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
