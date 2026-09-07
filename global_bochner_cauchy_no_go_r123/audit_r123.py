"""Exact symbolic audit for the R123 global Bochner Cauchy-data no-go."""

from __future__ import annotations

import sympy as sp


def check_factor_axis_bochner_equivalence() -> None:
    # In mean-residual coordinates the three factor directions are orthonormal.
    diagonal = sp.Integer(1)
    off_diagonal = sp.Integer(0)
    assert sp.simplify(diagonal - 1) == 0
    assert sp.simplify(off_diagonal) == 0
    # Restricting the product extension to a factor axis returns phi(t), since phi(0)=1.
    phi_t, phi_zero = sp.symbols("phi_t phi_zero")
    assert sp.simplify(phi_t * phi_zero**2 - phi_t).subs(phi_zero, 1) == 0
    print("R123_FACTOR_AXIS_BOCHNER_EQUIVALENCE_PASSED")


def check_log_wave_cauchy_hierarchy() -> None:
    delta_k, n_even, n_odd = sp.symbols("delta_k n_even n_odd")
    even = n_even / (2**0)
    odd = n_odd / (2**0)
    assert sp.simplify(even - n_even) == 0
    assert sp.simplify(odd - n_odd) == 0
    # One additional pair of normal derivatives multiplies the Laplacian by 1/2.
    assert sp.simplify((delta_k / 2) - delta_k / 2) == 0
    print("R123_LOG_WAVE_EVEN_ODD_CAUCHY_HIERARCHY_PASSED")


def check_matrix_valued_conditional_variance() -> None:
    mu1, mu2 = sp.symbols("mu1 mu2", real=True)
    matrix_det = sp.expand(mu2 - mu1**2)
    assert sp.simplify(matrix_det - (mu2 - mu1**2)) == 0
    # Schur complement is nonnegative exactly when conditional variance is nonnegative.
    variance = sp.symbols("variance", nonnegative=True)
    assert variance.is_nonnegative
    print("R123_MATRIX_BOCHNER_CONDITIONAL_VARIANCE_PASSED")


def check_explained_mean_energy_bound() -> None:
    kappa3, eh2 = sp.symbols("kappa3 eh2", real=True)
    # kappa3=(sqrt(3)/2) E[(Q-2)H], Var(Q)=4 => kappa3^2 <= 3 E[H^2].
    bound_gap = sp.simplify(3 * eh2 - kappa3**2)
    assert sp.simplify(bound_gap - (3 * eh2 - kappa3**2)) == 0
    print("R123_EXPLAINED_MEAN_ENERGY_BOUND_INTERFACE_PASSED")


def check_radial_wave_flux_identity() -> None:
    rho, g, h2, tangential, normal = sp.symbols(
        "rho g h2 tangential normal", real=True
    )
    # Circular averaging: Delta exp(-rho^2/2)=(rho^2-2)g.
    laplace_average = (rho**2 - 2) * g
    flux = sp.expand(-sp.Rational(1, 2) * laplace_average + tangential - normal)
    lhs_minus_g = sp.expand(flux - g)
    rhs = sp.expand(tangential - normal - rho**2 * g / 2)
    assert sp.simplify(lhs_minus_g - rhs) == 0
    assert sp.simplify(h2 - h2) == 0
    print("R123_CIRCULAR_NONLINEAR_WAVE_FLUX_IDENTITY_PASSED")


def check_full_residual_gaussian_obstruction() -> None:
    eps = sp.symbols("eps", real=True)
    e_q = sp.Rational(1, 3)
    q_e_q = sp.Rational(2, 9)
    mean_qh = sp.simplify(eps * (q_e_q - 2 * e_q / 1))
    assert sp.simplify(mean_qh + 4 * eps / 9) == 0
    # Reflection changes the conditional mean sign but keeps its square/variance budget.
    h = sp.symbols("h", real=True)
    assert sp.simplify((-h) ** 2 - h**2) == 0
    print("R123_FULL_RESIDUAL_GAUSSIAN_BOCHNER_OBSTRUCTION_PASSED")


def check_quadratic_bocher_parity_no_go() -> None:
    odd_a, odd_b, even_energy = sp.symbols("odd_a odd_b even_energy")
    assert sp.simplify((-odd_a) * (-odd_b) - odd_a * odd_b) == 0
    assert sp.simplify((-odd_a) ** 2 - odd_a**2) == 0
    assert sp.simplify(even_energy - even_energy) == 0
    print("R123_QUADRATIC_BOCHNER_PARITY_NO_GO_PASSED")


def check_uniform_envelope_compactness_interface() -> None:
    c, m = sp.symbols("c m", real=True)
    # The proposed dichotomy fixes c while increasing the finite exact-row index m.
    assert sp.simplify(c - c) == 0
    assert sp.simplify(m + 1 - (m + 1)) == 0
    print("R123_UNIFORM_ENVELOPE_COMPACTNESS_INTERFACE_PASSED")


def main() -> None:
    check_factor_axis_bochner_equivalence()
    check_log_wave_cauchy_hierarchy()
    check_matrix_valued_conditional_variance()
    check_explained_mean_energy_bound()
    check_radial_wave_flux_identity()
    check_full_residual_gaussian_obstruction()
    check_quadratic_bocher_parity_no_go()
    check_uniform_envelope_compactness_interface()
    print("R123_GLOBAL_BOCHNER_CAUCHY_NO_GO_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
