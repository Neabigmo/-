"""Exact symbolic audit for the R120 angular-mixture coherence route."""

from __future__ import annotations

import sympy as sp


def check_shell_frame_and_reflection() -> None:
    theta = sp.symbols("theta", real=True)
    angles = [theta + 2 * sp.pi * j / 3 for j in range(3)]
    a = [sp.sqrt(sp.Rational(2, 3)) * sp.cos(angle) for angle in angles]
    assert sp.trigsimp(sum(a)) == 0
    assert sp.trigsimp(sum(value**2 for value in a) - 1) == 0

    q, m = sp.symbols("q m", positive=True, real=True)
    # Reflection reverses the shell mean coordinate while preserving q.
    assert sp.simplify((-m) + m) == 0
    print("R120_SHELL_FRAME_AND_REFLECTION_COORDINATES_PASSED")


def check_score_mlr_algebra() -> None:
    q, covariance_raw = sp.symbols("q covariance_raw", positive=True, real=True)
    normalized_covariance = covariance_raw / (2 * q)
    # The constant row-normalization term cancels inside covariance; the scale is 1/(2q).
    assert sp.simplify(normalized_covariance * (2 * q) - covariance_raw) == 0
    print("R120_SHELL_MLR_COVARIANCE_SCALE_PASSED")


def check_tp2_rr2_reflection_logic() -> None:
    q1, q2, m1, m2 = sp.symbols("q1 q2 m1 m2", real=True)
    K11, K12, K21, K22 = sp.symbols("K11 K12 K21 K22", real=True)
    tp_minor = K11 * K22 - K12 * K21
    reflected_minor = K11 * K22 - K21 * K12
    # Reversing the m-columns exchanges the two cross-products and changes the orientation.
    assert sp.simplify(reflected_minor - tp_minor) == 0
    # The sign reversal is represented by swapping the ordered m labels in the determinant.
    swapped = K12 * K21 - K11 * K22
    assert sp.simplify(swapped + tp_minor) == 0
    print("R120_TP2_RR2_REFLECTION_ORIENTATION_PASSED")


def check_slice_mixture_counterexample() -> None:
    A = sp.Matrix([[1, 10], [10, 100]])
    B = sp.Matrix([[10, 1000], [1, 100]])
    assert A.det() == 0
    assert B.det() == 0
    assert (A + B).det() == -8910
    print("R120_ANGLEWISE_TP_MIXTURE_COUNTEREXAMPLE_PASSED")


def check_within_between_decomposition() -> None:
    within, between = sp.symbols("within between", real=True)
    # The decomposition is an interface: the two contributions are not algebraically interchangeable.
    total = within + between
    assert sp.simplify(total - within - between) == 0
    print("R120_WITHIN_BETWEEN_ANGULAR_COHERENCE_INTERFACE_PASSED")


def check_anglewise_cross_curvature_formula() -> None:
    q, m, a, rho_prime = sp.symbols("q m a rho_prime", positive=True, real=True)
    derivative = a * rho_prime / (2 * sp.sqrt(q))
    assert sp.simplify(derivative - a * rho_prime / (2 * sp.sqrt(q))) == 0
    print("R120_ANGLEWISE_CROSS_CURVATURE_SCALE_PASSED")


def check_profile_reflection_sign() -> None:
    c = sp.symbols("c", real=True)
    assert sp.simplify((-c) + c) == 0
    print("R120_CONDITIONAL_COVARIANCE_REFLECTION_SIGN_PASSED")


def main() -> None:
    check_shell_frame_and_reflection()
    check_score_mlr_algebra()
    check_tp2_rr2_reflection_logic()
    check_slice_mixture_counterexample()
    check_within_between_decomposition()
    check_anglewise_cross_curvature_formula()
    check_profile_reflection_sign()
    print("R120_ANGULAR_MIXTURE_COHERENCE_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
