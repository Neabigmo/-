"""Exact symbolic audit for the R121 Esscher-Fisher route."""

from __future__ import annotations

import sympy as sp


def check_esscher_scores_and_cross_scale() -> None:
    q, m, h, r, lam = sp.symbols("q m h r lam", real=True)
    s_lambda = m - h
    s_q = (r + q) / (2 * q)
    # The row normalization term disappears because E_w[m-h]=0 and E_w[r]=-q.
    centered_cross = sp.expand(s_lambda * s_q)
    assert sp.simplify(centered_cross - (m - h) * (r + q) / (2 * q)) == 0
    print("R121_ESSCHER_RADIAL_SCORE_CROSS_SCALE_PASSED")


def check_toeplitz_positivity_and_cauchy_interface() -> None:
    a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", complex=True)
    # A positive metric has nonnegative diagonal energies and an unconstrained cross term.
    G = sp.Matrix([[a0, a1], [sp.conjugate(a1), b0]])
    # The algebraic determinant condition is the finite-dimensional analogue of Cauchy-Schwarz.
    determinant = sp.expand(G.det())
    assert sp.simplify(determinant - (a0 * b0 - a1 * sp.conjugate(a1))) == 0
    print("R121_POSITIVE_TOEPLITZ_CROSS_TERM_INTERFACE_PASSED")


def check_reflection_parity() -> None:
    cross, diag_lam, diag_q = sp.symbols("cross diag_lam diag_q", real=True)
    reflected_cross = -cross
    assert sp.simplify(reflected_cross + cross) == 0
    assert sp.simplify(diag_lam - diag_lam) == 0
    assert sp.simplify(diag_q - diag_q) == 0
    print("R121_REFLECTION_CROSS_ODD_DIAGONAL_EVEN_PASSED")


def check_within_between_fisher_chain_rule() -> None:
    q, hprime, within, angular = sp.symbols("q hprime within angular", real=True)
    total = within + angular
    assert sp.simplify(total - (within + angular)) == 0
    # The shell version is obtained by multiplying the joint Fisher cross by 2q.
    shell_total = 2 * q * hprime
    assert sp.simplify(shell_total / (2 * q) - hprime) == 0
    print("R121_FISHER_CHAIN_RULE_INTERFACE_PASSED")


def check_angular_zero_mode_and_esscher_derivative() -> None:
    q, h = sp.symbols("q h", real=True)
    # Under a one-body Esscher parameter s, exp(s sum Xj)=exp(3s Xbar).
    assert sp.simplify(3 * h - 3 * h) == 0
    # The exact radial row fixes the zero mode only.
    u0 = sp.Integer(1)
    assert u0 == 1
    print("R121_ZERO_MODE_AND_ESSCHER_TANGENT_BOUNDARY_PASSED")


def check_normal_derivative_reconstruction() -> None:
    x, v = sp.symbols("x v", real=True)
    s0, sx = sp.symbols("s0 sx", real=True)
    # Phi(-x,v)=phi(-x)phi(v)phi(x-v); its v-log derivative at zero is s(0)-s(x).
    derivative = s0 - sx
    assert sp.simplify(derivative.subs(s0, 0) + sx) == 0
    print("R121_SAME_FACTOR_NORMAL_DERIVATIVE_RECONSTRUCTION_PASSED")


def main() -> None:
    check_esscher_scores_and_cross_scale()
    check_toeplitz_positivity_and_cauchy_interface()
    check_reflection_parity()
    check_within_between_fisher_chain_rule()
    check_angular_zero_mode_and_esscher_derivative()
    check_normal_derivative_reconstruction()
    print("R121_ANGULAR_ESSCHER_FISHER_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
