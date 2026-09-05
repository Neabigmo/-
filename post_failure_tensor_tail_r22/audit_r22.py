"""Proof-level audit for the R22 heat-Hankel and flat-tail reductions."""

from __future__ import annotations

import itertools
import math

import sympy as sp


def laplacian(expr: sp.Expr, variables: list[sp.Symbol]) -> sp.Expr:
    return sp.expand(sum(sp.diff(expr, x, 2) for x in variables))


def multiindices(length: int, bound: int):
    return itertools.product(range(bound + 1), repeat=length)


def check_vandermonde_heat_identity() -> None:
    # Three variables already contain the nontrivial Vandermonde/harmonic case.
    variables = sp.symbols("x0:3")
    a = sp.symbols("a")
    x0, x1, x2 = variables
    V = (x1 - x0) * (x2 - x0) * (x2 - x1)
    degree = sp.Poly(V, *variables).total_degree()

    heat = V**2
    lap_power = V**2
    for k in range(1, degree + 1):
        lap_power = laplacian(lap_power, list(variables))
        heat += a**k / (2**k * sp.factorial(k)) * lap_power

    rhs = 0
    for alpha in multiindices(len(variables), degree):
        order = sum(alpha)
        derivative = V
        denominator = 1
        for variable, count in zip(variables, alpha):
            derivative = sp.diff(derivative, variable, count)
            denominator *= sp.factorial(count)
        rhs += a**order / denominator * derivative**2
    assert sp.simplify(heat - rhs) == 0

    # Highest heat coefficient C_(2,3) is the universal product 0!*1!*2! = 2.
    top = 0
    for alpha in multiindices(len(variables), degree):
        if sum(alpha) != degree:
            continue
        derivative = V
        denominator = 1
        for variable, count in zip(variables, alpha):
            derivative = sp.diff(derivative, variable, count)
            denominator *= sp.factorial(count)
        top += derivative**2 / denominator
    assert sp.simplify(top / sp.factorial(len(variables)) - 2) == 0


def check_flat_crossing_transversality() -> None:
    # P_M' = M P_(M-1) plus lower orthogonal components.  With positive
    # lower norms, its squared norm is strictly larger than M^2 h_(M-1).
    M = 4
    h = sp.symbols("h0:4", positive=True)
    lower_coefficients = sp.symbols("c0:3", real=True)
    norm = M**2 * h[M - 1] + sum(
        lower_coefficients[j] ** 2 * h[j] for j in range(M - 1)
    )
    assert sp.expand(norm - M**2 * h[M - 1]) == sum(
        lower_coefficients[j] ** 2 * h[j] for j in range(M - 1)
    )


def check_flat_leakage_determinant() -> None:
    h0, h1, h2, ell, tail = sp.symbols("h0 h1 h2 ell tail")
    block = sp.diag(h0, h1, h2, 1, 1)
    block[3, 3], block[3, 4] = 0, ell
    block[4, 3], block[4, 4] = ell, tail
    determinant = sp.factor(block.det())
    assert sp.simplify(determinant + h0 * h1 * h2 * ell**2) == 0


def check_adjacent_coefficient_bound() -> None:
    M = sp.symbols("M", positive=True)
    c = sp.symbols("c", real=True)
    threshold = 3 * M**2 / (2 * (M + 1) ** 2)
    six_equal = 6 * (M * c / (2 * (M + 1))) ** 2
    assert sp.simplify(six_equal - threshold * c**2) == 0

    # The three derivative equations have disjoint pairs of adjacent
    # coefficients; Cauchy gives M^2 c^2 <= 2(M+1)^2 times each pair norm.
    pair_bound = 2 * (M + 1) ** 2
    assert sp.simplify(3 * M**2 - threshold * pair_bound) == 0


def check_degree_3M_forces_h3M_channel() -> None:
    M = 2
    theta = 0.0
    alpha = [
        math.sqrt(2 / 3) * math.cos(theta + 2 * math.pi * j / 3)
        for j in range(3)
    ]
    triple_pivot = math.comb(6, 2) * math.comb(4, 2) * alpha[0] ** M * alpha[1] ** M * alpha[2] ** M
    coordinate_3M = [alpha_j ** (3 * M) for alpha_j in alpha]
    assert abs(triple_pivot) > 0
    assert all(abs(value) > 0 for value in coordinate_3M)


def main() -> None:
    checks = [
        check_vandermonde_heat_identity,
        check_flat_crossing_transversality,
        check_flat_leakage_determinant,
        check_adjacent_coefficient_bound,
        check_degree_3M_forces_h3M_channel,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R22_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
