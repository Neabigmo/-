"""Finite audit for the R148 continuum dual/reflection package.

The checks below certify only finite algebra, quadrature interfaces, and a
finite signed-measure decomposition.  They do not certify infinite
dimensional uniqueness, the exact full-SF characterization, positivity of a
nonlinear branch, tower uniformity, or publication novelty.
"""

from __future__ import annotations

import math
from itertools import product

import mpmath as mp
import numpy as np


def laguerre(m: int, x: mp.mpf) -> mp.mpf:
    if m == 0:
        return mp.mpf(1)
    if m == 1:
        return 1 - x
    previous, current = mp.mpf(1), 1 - x
    for n in range(1, m):
        current, previous = (
            ((2 * n + 1 - x) * current - n * previous) / (n + 1),
            current,
        )
    return current


def check_bessel_laguerre_identity() -> None:
    for m in range(6):
        for y in (mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2.3")):
            lhs = mp.quad(
                lambda x: mp.e ** (-x) * laguerre(m, x)
                * mp.besselj(0, 2 * mp.sqrt(x * y)),
                [0, mp.inf],
            )
            rhs = mp.e ** (-y) * y**m / math.factorial(m)
            assert abs(lhs - rhs) < mp.mpf("2e-10")
    print("R148_BESSEL_LAGUERRE_IDENTITY_PASSED")


def check_dual_transform_generating_function() -> None:
    coefficients = [mp.mpf("0.0"), mp.mpf("0.31"), mp.mpf("-0.22"), mp.mpf("0.17")]
    y = mp.mpf("0.83")
    direct = mp.mpf(0)
    for m, coefficient in enumerate(coefficients):
        direct += coefficient * mp.quad(
            lambda x, m=m: mp.e ** (-x)
            * laguerre(m, x)
            * mp.besselj(0, 2 * mp.sqrt(x * y)),
            [0, mp.inf],
        )
    generated = mp.e ** (-y) * sum(
        coefficient * y**m / math.factorial(m)
        for m, coefficient in enumerate(coefficients)
    )
    assert abs(direct - generated) < mp.mpf("2e-10")
    print("R148_DUAL_BESSEL_GENERATING_INTERFACE_PASSED")


def probabilists_hermite(n: int, x: np.ndarray) -> np.ndarray:
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return x
    previous, current = np.ones_like(x), x
    for k in range(1, n):
        current, previous = x * current - k * previous, current
    return current


def gaussian_expectation(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.sum(weights * values) / math.sqrt(math.pi))


def check_continuum_linearization_multipliers() -> None:
    nodes, weights = np.polynomial.hermite.hermgauss(100)
    x = math.sqrt(2.0) * nodes
    normalized_weights = weights
    for z in (0.13, 0.8, 2.4):
        r = 2.0 * z / (1.0 + 2.0 * z)
        b = 2.0 * z / (3.0 + 2.0 * z)
        profile = np.exp(-b * x * x) / math.sqrt(
            (1.0 + 2.0 * z) * (1.0 + 2.0 * z / 3.0)
        )
        for m in range(6):
            psi_even = probabilists_hermite(2 * m, x) / math.sqrt(
                math.factorial(2 * m)
            )
            numerical = 3.0 * gaussian_expectation(
                psi_even * profile, normalized_weights
            )
            expected = (
                3.0
                / (1.0 + 2.0 * z)
                * math.sqrt(math.factorial(2 * m))
                / math.factorial(m)
                * (-r / 3.0) ** m
            )
            assert abs(numerical - expected) < 2e-9
            psi_odd = probabilists_hermite(2 * m + 1, x) / math.sqrt(
                math.factorial(2 * m + 1)
            )
            odd_response = gaussian_expectation(psi_odd * profile, normalized_weights)
            assert abs(odd_response) < 2e-12
    print("R148_CONTINUUM_LINEARIZATION_MULTIPLIERS_PASSED")


def sample_f_measure(values: list[float], probabilities: list[float], z: float) -> float:
    total = 0.0
    for i, j, k in product(range(len(values)), repeat=3):
        x, y, w = values[i], values[j], values[k]
        q = ((x - y) ** 2 + (y - w) ** 2 + (w - x) ** 2) / 3.0
        total += probabilities[i] * probabilities[j] * probabilities[k] * math.exp(-z * q)
    return total


def mixed_f_measure(
    first: list[float], first_p: list[float],
    second: list[float], second_p: list[float],
    third: list[float], third_p: list[float], z: float,
) -> float:
    total = 0.0
    for i, j, k in product(range(len(first)), range(len(second)), range(len(third))):
        x, y, w = first[i], second[j], third[k]
        q = ((x - y) ** 2 + (y - w) ** 2 + (w - x) ** 2) / 3.0
        total += first_p[i] * second_p[j] * third_p[k] * math.exp(-z * q)
    return total


def check_reflection_deficit_decomposition() -> None:
    # A finite nonsymmetric law and its reflected symmetrization.
    support = [-1.0, 0.4, 1.3]
    probabilities = [0.2, 0.5, 0.3]
    union = sorted(set(support + [-x for x in support]))
    mu_p = [sum(p for x, p in zip(support, probabilities) if x == u) for u in union]
    reflected_p = [sum(p for x, p in zip(support, probabilities) if -x == u) for u in union]
    nu_p = [(a + b) / 2.0 for a, b in zip(mu_p, reflected_p)]
    sigma_p = [(a - b) / 2.0 for a, b in zip(mu_p, reflected_p)]
    z = 0.61
    f_mu = sample_f_measure(union, mu_p, z)
    f_nu = sample_f_measure(union, nu_p, z)
    cross = mixed_f_measure(union, nu_p, union, sigma_p, union, sigma_p, z)
    assert abs(f_mu - (f_nu + 3.0 * cross)) < 2e-13
    # The signed quadratic form is nonnegative for every fixed first point.
    a = union[2]
    quadratic = 0.0
    for i, j in product(range(len(union)), repeat=2):
        x, y = union[i], union[j]
        q = ((a - x) ** 2 + (x - y) ** 2 + (y - a) ** 2) / 3.0
        quadratic += sigma_p[i] * sigma_p[j] * math.exp(-z * q)
    assert quadratic >= -2e-13
    print("R148_REFLECTION_DEFICIT_DECOMPOSITION_PASSED")


def check_ou_normalized_shape() -> None:
    lam = 0.19
    t = 0.73
    # Test the exact identity on an arbitrary finite Laguerre/Bessel shape.
    coefficients = [0.0, 0.4, -0.2, 0.11]

    def hat_d(x: float) -> float:
        return sum(c * (x * x / 2.0) ** m / math.factorial(m) for m, c in enumerate(coefficients))

    lhs = math.exp(t * t / 2.0) * math.sqrt(lam) * math.exp(
        -(1.0 - lam) * t * t / 2.0
    ) * math.exp(-lam * t * t / 2.0) * hat_d(math.sqrt(lam) * t)
    rhs = math.sqrt(lam) * hat_d(math.sqrt(lam) * t)
    assert abs(lhs - rhs) < 1e-14
    print("R148_OU_NORMALIZED_SHAPE_PASSED")


def main() -> None:
    mp.mp.dps = 40
    check_bessel_laguerre_identity()
    check_dual_transform_generating_function()
    check_continuum_linearization_multipliers()
    check_reflection_deficit_decomposition()
    check_ou_normalized_shape()
    print("R148_AUDIT_SCOPE_EXPLICIT: finite identities and numerical interfaces only")
    print("R148_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
