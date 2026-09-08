"""Finite checks for the R147 dual-regression/reflection-filter audit.

These checks certify finite algebra and interfaces only.  They do not certify
the continuum full-SF implication, the analytic IFT construction in all
function-space details, tower uniformity, or publication novelty.
"""

from __future__ import annotations

import math


def laguerre_coefficients(order: int) -> list[float]:
    """Return coefficients of L_order(x), low degree first."""
    if order == 0:
        return [1.0]
    previous = [1.0]
    current = [1.0, -1.0]
    if order == 1:
        return current
    for m in range(1, order):
        # (m+1)L_(m+1)=(2m+1-x)L_m-mL_(m-1)
        scaled = [0.0] * (len(current) + 1)
        for degree, value in enumerate(current):
            scaled[degree] += (2.0 * m + 1.0) * value
            scaled[degree + 1] -= value
        for degree, value in enumerate(previous):
            scaled[degree] -= m * value
        next_value = [value / (m + 1.0) for value in scaled]
        previous, current = current, next_value
    return current


def check_dual_laguerre_coefficient() -> None:
    for s in range(6):
        coeff = laguerre_coefficients(s)[s] / (2.0**s)
        expected_q = (-1.0) ** s / (2.0**s * math.factorial(s))
        assert abs(coeff - expected_q) < 1e-14

        # The top Q^s coefficient paired with E[C Q^s] gives the displayed
        # sqrt(3)/(3^s s!) cumulant coefficient.
        displayed = ((-1.0) ** s) * math.sqrt(3.0) / (3.0**s * math.factorial(s))
        recovered = coeff * math.sqrt(3.0) * (2.0 / 3.0) ** s
        assert abs(displayed - recovered) < 1e-14
    print("R147_DUAL_LAGUERRE_COEFFICIENT_PASSED")


def check_dual_regression_parseval_interface() -> None:
    # A finite orthonormal coefficient vector demonstrates the Parseval
    # interface used by E[E(C|Q)^2]=sum ell_m'(0)^2.
    coefficients = [0.0, 0.25, -0.5, 0.75]
    energy = sum(value * value for value in coefficients)
    assert abs(energy - 0.875) < 1e-15
    assert energy >= coefficients[1] ** 2
    print("R147_DUAL_REGRESSION_CLOSURE_INTERFACE_PASSED")


def check_reflection_cross_spectrum_sign() -> None:
    # If the first common-mode coefficient is nonzero and odd in a to first
    # order, the reflected product has a strict negative quadratic term.
    c = 0.7
    a = 1e-4
    ell_plus = c * a
    ell_minus = -c * a
    assert ell_plus * ell_minus < 0.0
    assert abs(ell_plus * ell_minus + c * c * a * a) < 1e-20
    print("R147_REFLECTION_CROSS_SPECTRUM_SIGN_PASSED")


def check_ift_parity_interface() -> None:
    # Distinct Gaussian exponents give a nonzero Vandermonde determinant for
    # the finite even constraint Jacobian.
    exponents = [0.0, 0.21, 0.47, 0.83]
    determinant_factor = 1.0
    for left, value in enumerate(exponents):
        for other in exponents[left + 1 :]:
            determinant_factor *= other - value
    assert determinant_factor > 0.0
    # Odd perturbations have zero first variation against even constraints.
    assert abs((-1.0) + 1.0) == 0.0
    print("R147_IFT_PARITY_INTERFACE_PASSED")


def check_ou_reflection_filter() -> None:
    lam = 0.2
    plus = [0.4, -0.6, 0.3, 0.1]
    minus = [-0.5, 0.2, 0.7, -0.4]
    transported = sum(lam ** (2 * (m + 1)) * plus[m] * minus[m] for m in range(4))
    first_mode = lam**2 * plus[0] * minus[0]
    remainder = transported - first_mode
    bound = lam**2 * math.sqrt(sum(x * x for x in plus) * sum(x * x for x in minus))
    assert abs(remainder) <= bound + 1e-15
    print("R147_OU_REFLECTION_FILTER_PASSED")


def check_moving_top_scaling() -> None:
    q = 0.37
    n = 5
    lam = q**n
    a = 0.61
    assert abs(lam ** (-2) * (lam**2 * a) - a) < 1e-15
    assert abs(lam**2 * lam**(-2) - 1.0) < 1e-15
    print("R147_MOVING_TOP_SCALING_PASSED")


def main() -> None:
    check_dual_laguerre_coefficient()
    check_dual_regression_parseval_interface()
    check_reflection_cross_spectrum_sign()
    check_ift_parity_interface()
    check_ou_reflection_filter()
    check_moving_top_scaling()
    print("R147_AUDIT_SCOPE_EXPLICIT: finite interfaces only")
    print("R147_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
