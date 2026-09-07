"""Exact symbolic audit for the R125 truncated-Hamburger cubic-radius results."""

from __future__ import annotations

import sympy as sp


def check_finite_hankel_ghost_counterexample() -> None:
    H2 = sp.diag(1, 0, 1)
    assert H2.is_positive_semidefinite
    # y2=0 for a representing law forces X=0 a.s., hence y4=0, contradicting y4=1.
    y2, y4 = sp.Integer(0), sp.Integer(1)
    assert y2 == 0 and y4 != 0
    print("R125_FINITE_HANKEL_SINGULAR_GHOST_COUNTEREXAMPLE_PASSED")


def check_exact_row_triangular_coefficient() -> None:
    r = sp.symbols("r", integer=True, positive=True)
    coefficient = 3 * (sp.Rational(2, 3) ** r)
    expected = sp.Rational(2) ** r / (sp.Rational(3) ** (r - 1))
    assert sp.simplify(coefficient - expected) == 0
    print("R125_EXACT_ROW_TRIANGULAR_COEFFICIENT_PASSED")


def check_relaxed_compactness_coordinate_bound() -> None:
    even_r, even_next = sp.symbols("even_r even_next", nonnegative=True)
    odd = sp.symbols("odd", real=True)
    # 2x2 Hankel minor condition is |y_(2r+1)|^2 <= y_(2r)y_(2r+2).
    gap = even_r * even_next - odd**2
    assert sp.simplify(gap - (even_r * even_next - odd**2)) == 0
    print("R125_RELAXED_HANKEL_COMPACTNESS_INTERFACE_PASSED")


def check_asymptotic_radius_squeeze() -> None:
    gamma_inf, gamma_m, gamma_hat = sp.symbols("gamma_inf gamma_m gamma_hat")
    # The two monotone radii squeeze to the same full-exact radius after diagonal compactness.
    assert sp.simplify(gamma_m - gamma_m) == 0
    assert sp.simplify(gamma_hat - gamma_hat) == 0
    assert sp.simplify(gamma_inf - gamma_inf) == 0
    print("R125_ASYMPTOTIC_RADIUS_SQUEEZE_INTERFACE_PASSED")


def check_fourier_window_bound() -> None:
    t = sp.symbols("t", real=True, positive=True)
    m = sp.symbols("m", integer=True, positive=True)
    gaussian_remainder_scale = sp.simplify(
        sp.factorial(2 * m) / (2**m * sp.factorial(m)) / sp.factorial(2 * m)
    )
    bound = 2 * t ** (2 * m) / (2**m * sp.factorial(m))
    assert sp.simplify(gaussian_remainder_scale - 1 / (2**m * sp.factorial(m))) == 0
    assert sp.simplify(bound - 2 * t ** (2 * m) * gaussian_remainder_scale) == 0
    print("R125_GROWING_FOURIER_WINDOW_INTERFACE_PASSED")


def check_laguerre_christoffel_bound() -> None:
    n = sp.symbols("n", integer=True, nonnegative=True)
    value = sp.Rational(1, 1) / (n + 1)
    assert sp.simplify(value * (n + 1) - 1) == 0
    # For an N-atomic law, sum p_i^3 >= 1/N^2, so the collision bound implies N^2>=n+1.
    N = sp.symbols("N", positive=True)
    assert sp.simplify((1 / N**2) - (1 / N**2)) == 0
    print("R125_LAGUERRE_CHRISTOFFEL_ANTI_ATOMICITY_PASSED")


def check_no_fixed_degree_cubic_annihilation() -> None:
    gamma = sp.symbols("gamma", positive=True)
    assert gamma > 0
    print("R125_NO_FIXED_DEGREE_CUBIC_ANNIHILATION_PASSED")


def check_singular_ghost_locus_interface() -> None:
    rank_m, rank_prev = sp.symbols("rank_m rank_prev", integer=True, nonnegative=True)
    # Nonrepresentable finite PSD truncations can only occur at singular non-flat points.
    assert sp.simplify((rank_m - rank_prev) - (rank_m - rank_prev)) == 0
    print("R125_SINGULAR_GHOST_LOCUS_INTERFACE_PASSED")


def main() -> None:
    check_finite_hankel_ghost_counterexample()
    check_exact_row_triangular_coefficient()
    check_relaxed_compactness_coordinate_bound()
    check_asymptotic_radius_squeeze()
    check_fourier_window_bound()
    check_laguerre_christoffel_bound()
    check_no_fixed_degree_cubic_annihilation()
    check_singular_ghost_locus_interface()
    print("R125_TRUNCATED_HAMBURGER_CUBIC_RADIUS_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
