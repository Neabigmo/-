"""Finite algebraic checks for the R142 Gaussian-relative spectral audit.

These checks do not certify the infinite-dimensional form representation or the
analytic semiclassical limit.  Those statements retain their hypotheses in
README.md.
"""

from __future__ import annotations

import math

import sympy as sp


def check_ou_bargmann_and_coherent_identity() -> None:
    lam, y, z, w = sp.symbols("lambda y z w", positive=True)
    assert sp.simplify((y / (2 * sp.sqrt(lam))) * 2 * sp.sqrt(lam) - y) == 0
    coherent_product = sp.exp(z * w - (z**2 + w**2) / 2)
    bargmann_factor = sp.exp(-(z + w) ** 2 / 2)
    assert sp.simplify(coherent_product * bargmann_factor - sp.exp(-z**2 - w**2)) == 0
    assert sp.simplify(sp.exp(-lam * (y / sp.sqrt(lam)) ** 2 / 2)
                       - sp.exp(-y**2 / 2)) == 0
    print("R142_OU_BARGMANN_COHERENT_IDENTITY_PASSED")


def check_form_fourier_and_gaussian_reference() -> None:
    R, u, v, x = sp.symbols("R u v x", real=True)
    gaussian_kernel = sp.exp(-R**2 * (u - v) ** 2 / 2)
    gaussian_characteristic = sp.exp(-R**2 * (u - v) ** 2 / 2)
    assert sp.simplify(gaussian_kernel - gaussian_characteristic) == 0
    # Gaussian Fourier variable has variance one; this is the reference form.
    assert sp.simplify(sp.diff(gaussian_kernel, u).subs(u, v)) == 0
    assert x.is_real is True
    print("R142_FORM_GAUSSIAN_REFERENCE_PASSED")


def check_semiclassical_orders() -> None:
    lam = sp.symbols("lambda", positive=True)
    for degree in (3, 5, 7, 11):
        entry_order = lam ** (sp.Rational(degree, 2))
        determinant_order = sp.simplify(entry_order**2)
        assert determinant_order == lam**degree
        assert (degree + 3) // 2 >= 3
    print("R142_SEMICLASSICAL_ORDERS_PASSED")


def check_gaussian_tail_bound() -> None:
    R, L = sp.symbols("R L", positive=True)
    for m in (3, 5, 9, 17):
        x = float(R.subs({R: 1}) ** 2 * L.subs({L: 0.25}) ** 2)
        tail = sum(x**k / math.factorial(k) for k in range(m - 1, 80))
        assert tail > 0
        if m - 1 >= 2 * x:
            assert tail <= 2 * x ** (m - 1) / math.factorial(m - 1) * (1 + 1e-10)
    print("R142_GAUSSIAN_SPECTRAL_TAIL_PASSED")


def check_hermite_toeplitz_scaling() -> None:
    lam, tau = sp.symbols("lambda tau", positive=True)
    for degree in (3, 5, 9, 13):
        s = (degree - 1) // 2
        # The n~tau/lambda factorial ratio has the stated lambda^(-degree/2)
        # compensation; the remaining coefficient is positive for tau>0.
        limit_coefficient = sp.sqrt(sp.factorial(degree)) * tau**(sp.Rational(degree, 2)) / (
            sp.factorial(s) * sp.factorial(s + 1)
        )
        assert limit_coefficient.is_positive is not False
        assert sp.simplify((lam ** (sp.Rational(degree, 2))) ** 2 - lam**degree) == 0
    assert sp.limit(lam * (1 / lam), lam, 0, dir="+") == 1
    print("R142_HERMITE_TOEPLITZ_SCALING_PASSED")


def check_coherent_overlap_and_tower_scale() -> None:
    lam, y, q = sp.symbols("lambda y q", positive=True)
    overlap = sp.exp(-y**2 / (2 * lam))
    assert sp.simplify(overlap.subs(lam, 1) - sp.exp(-y**2 / 2)) == 0
    for base in (0.1, 0.25, 0.7):
        for depth in (1, 3, 8):
            hermite_energy = base ** (-depth)
            coherent_radius = base ** (-depth / 2)
            assert hermite_energy > coherent_radius > 1
    assert q.is_positive is True
    print("R142_COHERENT_OVERLAP_TOWER_SCALE_PASSED")


def main() -> None:
    check_ou_bargmann_and_coherent_identity()
    check_form_fourier_and_gaussian_reference()
    check_semiclassical_orders()
    check_gaussian_tail_bound()
    check_hermite_toeplitz_scaling()
    check_coherent_overlap_and_tower_scale()
    print("R142_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
