"""Finite, reproducible audit for the R149 nonlinear package.

The script deliberately does not claim to certify an infinite-dimensional
positive branch, a novelty claim, or any of the project's open bridges.
"""

from __future__ import annotations

import math
from typing import Iterable

import numpy as np
from numpy.polynomial.hermite import hermgauss


def central_trinomial(n: int) -> int:
    total = 0
    for j in range(n // 2 + 1):
        total += math.factorial(n) // (
            math.factorial(j) ** 2 * math.factorial(n - 2 * j)
        )
    return total


def hermite_probabilist(n: int, x: np.ndarray) -> np.ndarray:
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return x.copy()
    h0 = np.ones_like(x)
    h1 = x.copy()
    for k in range(1, n):
        h0, h1 = h1, x * h1 - k * h0
    return h1


def psi(n: int, x: np.ndarray) -> np.ndarray:
    return hermite_probabilist(n, x) / math.sqrt(math.factorial(n))


def gaussian_expectation(values: np.ndarray, nodes: np.ndarray, weights: np.ndarray) -> float:
    return float(np.sum(weights * values) / math.sqrt(math.pi))


def source_formula(z: float, d: int) -> float:
    r = 2.0 * z / (1.0 + 2.0 * z)
    return (1.0 / (1.0 + 2.0 * z)) * central_trinomial(d) / (3.0**d) * r**d


def source_quadrature(z: float, d: int, order: int = 70) -> float:
    nodes, weights = hermgauss(order)
    x = math.sqrt(2.0) * nodes
    w = weights / math.sqrt(math.pi)
    x1 = x[:, None, None]
    x2 = x[None, :, None]
    x3 = x[None, None, :]
    q = ((x1 - x2) ** 2 + (x2 - x3) ** 2 + (x3 - x1) ** 2) / 3.0
    integrand = np.exp(-z * q) * psi(d, x2) * psi(d, x3)
    return float(np.einsum("i,j,k,ijk->", w, w, w, integrand))


def kernel_q(z: float, a: float, x: float, y: float) -> float:
    q = ((a - x) ** 2 + (x - y) ** 2 + (y - a) ** 2) / 3.0
    return math.exp(-z * q)


def finite_measure_quadratic(z: float, nu: Iterable[tuple[float, float]], sigma: Iterable[tuple[float, float]]) -> float:
    return sum(
        wa * wx * wy * kernel_q(z, a, x, y)
        for a, wa in nu
        for x, wx in sigma
        for y, wy in sigma
    )


def ou_mobius(z: float, lam: float) -> float:
    return lam * z / (1.0 + 2.0 * (1.0 - lam) * z)


def main() -> None:
    assert [central_trinomial(n) for n in range(6)] == [1, 1, 3, 7, 19, 51]
    for n in range(2, 14):
        assert n * central_trinomial(n) == (
            (2 * n - 1) * central_trinomial(n - 1)
            + 3 * (n - 1) * central_trinomial(n - 2)
        )
    print("R149_CENTRAL_TRINOMIAL_RECURRENCE_PASSED")

    for d in (3, 5, 7, 9):
        for z in (0.05, 0.4, 2.0):
            exact = source_formula(z, d)
            numeric = source_quadrature(z, d)
            assert abs(exact - numeric) < 2e-9, (d, z, exact, numeric)
    print("R149_ODD_HERMITE_SOURCE_PROFILE_PASSED")

    for d in (3, 5, 7, 9, 15, 25):
        td = central_trinomial(d)
        ad = math.factorial(d) * td / math.sqrt(math.factorial(2 * d))
        bd = td / math.comb(2 * d, d)
        assert abs(ad * math.factorial(d) / math.sqrt(math.factorial(2 * d)) - bd) < 1e-12
        if d >= 5:
            assert 4 * td < math.comb(2 * d, d)
    print("R149_EVEN_INVERSE_AND_TAIL_DISCRIMINANT_PASSED")

    # A finite odd signed measure inside its symmetric positive envelope.
    nu = [(-1.0, 0.5), (1.0, 0.5)]
    sigma = [(-1.0, -0.5), (1.0, 0.5)]
    for z in (0.1, 1.0, 4.0):
        qval = finite_measure_quadratic(z, nu, sigma)
        fval = finite_measure_quadratic(z, nu, nu)
        assert qval > 0.0
        assert qval < fval
        zprime = ou_mobius(z, 0.37)
        assert 0.0 < zprime < z
    print("R149_FINITE_SIGNED_MEASURE_SANDWICH_PASSED")
    print("R149_OU_MOBIUS_INTERFACE_PASSED")

    # The first two asymptotic diagnostics are intentionally ratios, not a
    # proof of the inherited R137 moving-degree statement.
    d = 41
    ad = math.factorial(d) * central_trinomial(d) / math.sqrt(math.factorial(2 * d))
    central_binom = math.comb(d, (d - 1) // 2)
    ratio = ad / central_binom
    scale = d ** 0.25 * (3.0 / 4.0) ** d
    assert 0.0 < ratio / scale < 10.0
    print("R149_MOVING_DEGREE_RATIO_DIAGNOSTIC_PASSED")
    print("R149_AUDIT_SCOPE_EXPLICIT: finite identities, quadrature, and interfaces only")
    print("R149_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
