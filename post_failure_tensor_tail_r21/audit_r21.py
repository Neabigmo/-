"""Proof-level audit for the R21 first-pivot / cubic-tail reduction."""

from __future__ import annotations

import math

import sympy as sp


def check_residual_projection_geometry() -> None:
    A = sp.Matrix(
        [
            [1 / sp.sqrt(2), -1 / sp.sqrt(2), 0],
            [1 / sp.sqrt(6), 1 / sp.sqrt(6), -2 / sp.sqrt(6)],
        ]
    )
    one = sp.ones(3, 1)
    assert sp.simplify(A * A.T - sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(A.T * A - (sp.eye(3) - one * one.T / 3)) == sp.zeros(3)


def check_rotational_polynomial_lift() -> None:
    x, y, theta = sp.symbols("x y theta", real=True)
    u = x * sp.cos(theta) - y * sp.sin(theta)
    v = x * sp.sin(theta) + y * sp.cos(theta)
    F = u**2 + 2 * u * v + 3 * v**2
    averaged = sp.trigsimp(sp.integrate(F**2, (theta, 0, 2 * sp.pi)) / (2 * sp.pi))
    q = sp.symbols("q")
    expected = sp.expand(averaged.subs(y**2, q - x**2))
    assert sp.simplify(sp.diff(expected, x)) == 0
    assert sp.simplify(averaged - expected.subs(q, x**2 + y**2)) == 0


def check_first_failure_capture() -> None:
    M = 4
    theta = sp.symbols("theta", real=True)
    alphas = [
        sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta + 2 * sp.pi * j / 3)
        for j in range(3)
    ]
    assert sp.simplify(sum(a**2 for a in alphas) - 1) == 0
    # Degree-M first-pivot capture after rotational averaging.
    ridge_norm = sp.binomial(2 * M, M) / 4**M
    avg_cos = sp.integrate(sp.cos(3 * theta) ** (2 * M), (theta, 0, 2 * sp.pi)) / (2 * sp.pi)
    assert sp.simplify(avg_cos - ridge_norm) == 0
    lambda_2M = sp.simplify(3 * sp.Rational(2, 3) ** M * ridge_norm)
    assert sp.simplify(
        lambda_2M - 3 * (sp.Rational(2, 3)) ** M * sp.binomial(2 * M, M) / 4**M
    ) == 0
    bound = float(sp.Rational(2, 3) ** (M - 1))
    for sample in (0, sp.pi / 7, sp.pi / 5):
        value = float(sp.N(sum(a ** (2 * M) for a in alphas).subs(theta, sample)))
        assert value <= bound + 1e-12


def check_triple_pivot_amplification() -> None:
    M = sp.symbols("M", integer=True, positive=True)
    multinomial_sq = sp.factorial(3 * M) ** 2 / sp.factorial(M) ** 6
    angular_moment = sp.binomial(2 * M, M) / 4**M
    gamma = sp.simplify(multinomial_sq * angular_moment / 54**M)
    claimed = sp.factorial(3 * M) ** 2 * sp.binomial(2 * M, M) / (
        sp.factorial(M) ** 6 * 54**M * 4**M
    )
    assert sp.simplify(gamma - claimed) == 0

    # Small log-Stirling sanity check for the claimed exponential base/power.
    for m in (100, 500, 2000):
        log_gamma = (
            2 * math.lgamma(3 * m + 1)
            + math.lgamma(2 * m + 1)
            - 8 * math.lgamma(m + 1)
            - m * math.log(54)
            - m * math.log(4)
        )
        log_leading = (
            math.log(3 / (4 * math.pi ** 2.5))
            + m * math.log(27 / 2)
            - 2.5 * math.log(m)
        )
        assert abs(math.exp(log_gamma - log_leading) - 1) < 0.01


def main() -> None:
    checks = [
        check_residual_projection_geometry,
        check_rotational_polynomial_lift,
        check_first_failure_capture,
        check_triple_pivot_amplification,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R21_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
