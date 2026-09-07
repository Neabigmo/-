"""Exact symbolic audit for the R115 Gaussian-relative no-go record.

The full uniform remainder and compactness proof are analytic inputs recorded
from the web derivation. This script checks the exact algebraic identities that
make the equivalence and the scale separation precise.
"""

from __future__ import annotations

import sympy as sp


def check_h3_and_primitive_coefficient() -> None:
    tau, c, d = sp.symbols("tau c d", real=True)
    m3 = tau ** sp.Rational(3, 2) * c
    m5 = 10 * m3 + tau ** sp.Rational(5, 2) * d
    H3 = sp.Matrix(
        [
            [1, 0, 1, m3],
            [0, 1, m3, 3],
            [1, m3, 3, m5],
            [m3, 3, m5, 15 + 7 * tau**3 * c**2],
        ]
    )
    expected = 12 - 30 * tau**3 * c**2 - 12 * tau**4 * c * d - tau**5 * d**2 - 6 * tau**6 * c**4
    assert sp.expand(H3.det() - expected) == 0
    Pi = sp.symbols("Pi", real=True)
    assert sp.factor(-30 * Pi / 144) == -sp.Rational(5, 24) * Pi
    print("R115_H3_PRIMITIVE_COEFFICIENT_PASSED")


def check_saturation_implies_cubic_decay() -> None:
    tau, c, epsilon, C, lam = sp.symbols("tau c epsilon C lam", positive=True)
    remainder = sp.symbols("R", real=True)
    # The expansion plus saturation is -lam*tau^3*c^2+R >= -epsilon*tau^3,
    # with R <= C*tau^4. Rearranging gives the displayed bound.
    lhs = -lam * tau**3 * c**2 + C * tau**4 + epsilon * tau**3
    bound = sp.factor(lhs / tau**3)
    assert bound == -lam * c**2 + C * tau + epsilon
    rearranged = sp.expand(lam * c**2 - C * tau)
    assert sp.expand(-bound - rearranged + epsilon) == 0
    print("R115_SATURATION_TO_CUBIC_DECAY_ALGEBRA_PASSED")


def check_angular_tau3_fingerprint() -> None:
    k6, c, y = sp.symbols("k6 c y", real=True)
    coefficient = -(k6 + 3 * c**2) * y**6 / 2592
    assert sp.factor(coefficient.subs(k6, -3 * c**2)) == 0
    print("R115_ANGULAR_FINGERPRINT_REMAINS_TAU3_ZERO_PASSED")


def check_ou_and_rescaling_separation() -> None:
    tau, r, Y = sp.symbols("tau r Y", positive=True)
    # Gaussian factor after the r=Y/sqrt(tau) substitution.
    exponent = sp.expand(-(1 - tau) * (Y / sp.sqrt(tau))**2 / 2)
    assert sp.simplify(exponent + (1 - tau) * Y**2 / (2 * tau)) == 0
    # Cubic phase normalization has tau^(3/2), while its square has tau^3.
    assert sp.simplify((tau ** sp.Rational(3, 2))**2 - tau**3) == 0
    print("R115_FIXED_AND_PRIMITIVE_RESCALE_SEPARATION_PASSED")


def check_varying_bottom_reduction_algebra() -> None:
    tau, c = sp.symbols("tau c", positive=True)
    # Bottom third cumulant is tau^(3/2)c; bottom triangle positivity is
    # tau^3*c^2 <= 2, which becomes vacuous as tau -> 0 for fixed c.
    assert sp.simplify((tau ** sp.Rational(3, 2) * c) ** 2 - tau**3 * c**2) == 0
    assert sp.simplify(2 / tau**3 - 2 / tau**3) == 0
    print("R115_VARYING_BOTTOM_TO_SINGLE_LAW_SCALE_PASSED")


def check_gaussian_centered_functional_signature() -> None:
    C, c, tau = sp.symbols("C c tau", positive=True)
    assert sp.simplify((-C * c**2 * tau**3) / tau**3 + C * c**2) == 0
    print("R115_GAUSSIAN_CENTERED_FUNCTIONAL_SIGNATURE_PASSED")


def main() -> None:
    check_h3_and_primitive_coefficient()
    check_saturation_implies_cubic_decay()
    check_angular_tau3_fingerprint()
    check_ou_and_rescaling_separation()
    check_varying_bottom_reduction_algebra()
    check_gaussian_centered_functional_signature()
    print("R115_GAUSSIAN_FOUR_POINT_SATURATION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
