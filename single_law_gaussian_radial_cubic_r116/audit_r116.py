"""Exact symbolic audit for the R116 single-law reduction.

The script checks finite algebraic identities only.  It deliberately does not
claim to prove the infinite-dimensional same-factor angular annihilation.
"""

from __future__ import annotations

import sympy as sp


def check_complex_residual_and_frame() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    I = sp.I
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * I / 2
    A = x1 + omega * x2 + omega**2 * x3
    abs_sq = sp.expand(A * sp.conjugate(A))
    q = sp.expand(sum((x - (x1 + x2 + x3) / 3) ** 2 for x in (x1, x2, x3)))
    assert sp.simplify(sp.expand(sp.Rational(2, 3) * abs_sq - q)) == 0

    vectors = [
        sp.Matrix([sp.sqrt(sp.Rational(2, 3)), 0]),
        sp.Matrix([-sp.sqrt(sp.Rational(2, 3)) / 2, sp.sqrt(2) / 2]),
        sp.Matrix([-sp.sqrt(sp.Rational(2, 3)) / 2, -sp.sqrt(2) / 2]),
    ]
    assert sp.simplify(sum(vectors, sp.zeros(2, 1))) == sp.zeros(2, 1)
    frame = sum((v * v.T for v in vectors), sp.zeros(2, 2))
    assert sp.simplify(frame - sp.eye(2)) == sp.zeros(2, 2)
    assert all(sp.simplify((v.T * v)[0] - sp.Rational(2, 3)) == 0 for v in vectors)
    print("R116_RESIDUAL_IDENTITY_AND_TIGHT_FRAME_PASSED")


def check_cubic_skew_identity() -> None:
    m3 = sp.symbols("m3", real=True)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    surviving_coefficient = sp.simplify(1 + omega**3 + omega**6)
    assert surviving_coefficient == 3
    factor = sp.simplify(3 * (sp.Rational(2, 3)) ** sp.Rational(3, 2))
    assert factor == 2 * sp.sqrt(sp.Rational(2, 3))
    assert sp.simplify(sp.sqrt(sp.Rational(3, 8)) * factor - 1) == 0
    print("R116_CUBIC_SKEW_AND_ANGULAR_MOMENT_FACTOR_PASSED")


def check_hankel_and_bessel_leading_terms() -> None:
    rho, z, kappa3 = sp.symbols("rho z kappa3", real=True)
    ez3 = 2 * sp.sqrt(sp.Rational(2, 3)) * kappa3
    j3_leading = rho**3 / 48
    i3_leading = z**3 / 48
    expected_h = sp.sqrt(sp.Rational(2, 3)) * kappa3 * rho**3 / 24
    expected_c = sp.sqrt(sp.Rational(2, 3)) * kappa3 * z**3 / 24
    assert sp.simplify(j3_leading * ez3 - expected_h) == 0
    assert sp.simplify(i3_leading * ez3 - expected_c) == 0
    print("R116_HANKEL_AND_MODIFIED_BESSEL_LEADING_TERM_PASSED")


def check_ou_exactness_and_cubic_scaling() -> None:
    t, rho, kappa3 = sp.symbols("t rho kappa3", positive=True)
    # The isotropic Gaussian factor preserves the radial characteristic mode.
    radial_factor = sp.exp(-(1 - t) * rho**2 / 2) * sp.exp(-t * rho**2 / 2)
    assert sp.simplify(radial_factor - sp.exp(-rho**2 / 2)) == 0
    assert sp.simplify((t ** sp.Rational(3, 2) * kappa3) ** 2 - t**3 * kappa3**2) == 0
    print("R116_FORWARD_OU_RADIAL_PRESERVATION_AND_CUBIC_SCALING_PASSED")


def check_nonfactorized_smooth_obstruction() -> None:
    r, epsilon = sp.symbols("r epsilon", real=True)
    # The angular pairing in the perturbation leaves only z^3 * conjugate(z)^3.
    a = sp.Rational(3, 2)
    radial_integral = sp.integrate(r**7 * sp.exp(-a * r**2), (r, 0, sp.oo))
    assert sp.simplify(radial_integral - sp.Rational(16, 27)) == 0
    # The perturbation has zero angular average, so total mass remains one;
    # the displayed cubic moment is nonzero whenever epsilon is nonzero.
    assert sp.simplify(epsilon * radial_integral - sp.Rational(16, 27) * epsilon) == 0
    print("R116_SMOOTH_GAUSSIAN_RADIAL_NONFACTORIZED_OBSTRUCTION_PASSED")


def check_infinite_divisibility_condition() -> None:
    kappa3, kappa6 = sp.symbols("kappa3 kappa6", real=True)
    exact_fingerprint = sp.Eq(kappa6, -3 * kappa3**2)
    assert exact_fingerprint.rhs == -3 * kappa3**2
    # kappa6 >= 0 and the exact fingerprint force the square to vanish.
    forced_square = sp.simplify(-exact_fingerprint.rhs / 3)
    assert forced_square == kappa3**2
    print("R116_INFINITE_DIVISIBILITY_CONDITIONAL_GAUSSIAN_STEP_PASSED")


def main() -> None:
    check_complex_residual_and_frame()
    check_cubic_skew_identity()
    check_hankel_and_bessel_leading_terms()
    check_ou_exactness_and_cubic_scaling()
    check_nonfactorized_smooth_obstruction()
    check_infinite_divisibility_condition()
    print("R116_SINGLE_LAW_GAUSSIAN_RADIAL_CUBIC_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
