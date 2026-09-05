"""R38 exact follow-up audit for the R37 two-body head calculation.

R37's web review supplied a complete Gateaux derivative decomposition and a
finite Hermite-sum formula for the two-body Hoeffding energy.  This audit only
checks those identities at small exact degrees.  It does not use the formal
first variation as a probability counterexample and does not infer an
asymptotic theorem from a finite table.
"""

import sys
from pathlib import Path

from sympy import Rational, binomial, factorial, simplify, sqrt, symbols

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (
    c,
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    one_body_kappa,
    phi,
    two_body_projection_formula,
)


def eta(n, b):
    """Coefficient in the normalized S,D expansion of h_(2,n)."""
    return (-1) ** n * (
        Rational(1, 3) ** b * c(n - b) * c(b)
        - 2 * c(n) * Rational(1, 3) ** n * sqrt(binomial(2 * n, 2 * b))
    )


def tau(r, s, t):
    """E[h_(2r)(G) h_(2s)(G) h_(2t)(G)] exactly."""
    a = r + s - t
    b = r + t - s
    d = s + t - r
    if min(a, b, d) < 0:
        return 0
    return sqrt(factorial(2 * r) * factorial(2 * s) * factorial(2 * t)) / (
        factorial(a) * factorial(b) * factorial(d)
    )


def pair_kernel_in_sd(n, s, d):
    return two_body_projection_formula(n, (s + d) / sqrt(2), (s - d) / sqrt(2))


def one_body_sum_in_sd(n, s, d):
    x1 = (s + d) / sqrt(2)
    x2 = (s - d) / sqrt(2)
    return one_body_kappa(n) * (h_norm(2 * n, x1) + h_norm(2 * n, x2))


def pair_kernel_eta(n, s, d):
    return sum(
        eta(n, b) * h_norm(2 * (n - b), d) * h_norm(2 * b, s)
        for b in range(n + 1)
    )


def check_normalized_pair_expansion():
    s, d = symbols("s d")
    for n in range(1, 5):
        p = pair_kernel_in_sd(n, s, d)
        h2 = simplify(p - one_body_sum_in_sd(n, s, d))
        assert simplify(h2 - pair_kernel_eta(n, s, d)) == 0


def check_full_derivative_and_cancellations():
    x1, x2, x3 = symbols("x1 x2 x3")
    for n in range(1, 4):
        for N in (2, 4):
            p = two_body_projection_formula(n, x1, x2)
            k1 = one_body_kappa(n) * h_norm(2 * n, x1)
            k2 = one_body_kappa(n) * h_norm(2 * n, x2)
            h2 = simplify(p - k1 - k2)
            g1 = h_norm(N, x1)
            g2 = h_norm(N, x2)
            g3 = h_norm(N, x3)

            # Complete derivatives of p, k and the mean under
            # dmu=(1+epsilon*g)dgamma, kept separate on purpose.
            dot_p = marginal_gaussian(phi(n, x1, x2, x3) * g3, [x3], [x1, x2, x3])
            dot_k1 = marginal_gaussian(
                phi(n, x1, x2, x3) * (g2 + g3),
                [x2, x3],
                [x1, x2, x3],
            )
            dot_k2 = marginal_gaussian(
                phi(n, x1, x2, x3) * (g1 + g3),
                [x1, x3],
                [x1, x2, x3],
            )
            dot_theta = marginal_gaussian(
                phi(n, x1, x2, x3) * (g1 + g2 + g3),
                [x1, x2, x3],
                [x1, x2, x3],
            )
            dot_h2 = simplify(dot_p - dot_k1 - dot_k2 + dot_theta)

            # Degeneracy removes the subtraction and mean derivatives from
            # <h2, dot h2>; chaos order removes the conditional-kernel term.
            inner_p = gaussian_expectation(h2 * dot_p, (x1, x2))
            inner_k1 = gaussian_expectation(h2 * dot_k1, (x1, x2))
            inner_k2 = gaussian_expectation(h2 * dot_k2, (x1, x2))
            inner_theta = gaussian_expectation(h2 * dot_theta, (x1, x2))
            assert inner_p == 0
            assert inner_k1 == 0
            assert inner_k2 == 0
            assert inner_theta == 0
            assert gaussian_expectation(h2 * dot_h2, (x1, x2)) == 0

            # The remaining measure-weight derivative agrees with the
            # derivative of ||p||^2-2||k||^2, including both shared/leaf terms.
            weight_only = 2 * gaussian_expectation(g1 * h2**2, (x1, x2))
            s2 = gaussian_expectation(g1 * p**2, (x1, x2))
            x4 = symbols("x4")
            l2 = gaussian_expectation(
                h_norm(N, x3) * phi(n, x1, x2, x3) * phi(n, x1, x2, x4),
                (x1, x2, x3, x4),
            )
            s1 = gaussian_expectation(g1 * k1**2, (x1,))
            l1 = gaussian_expectation(g2 * p * k1, (x1, x2))
            full_from_norms = simplify(2 * (s2 + l2) - 2 * (s1 + 4 * l1))
            assert simplify(weight_only - full_from_norms) == 0


def finite_sum_head(n, m):
    return simplify(
        2
        * sum(
            Rational(1, 2) ** m
            * sqrt(binomial(2 * m, 2 * j))
            * sum(
                eta(n, b)
                * eta(n, bp)
                * tau(n - b, n - bp, m - j)
                * tau(b, bp, j)
                for b in range(n + 1)
                for bp in range(n + 1)
            )
            for j in range(m + 1)
        )
    )


def check_finite_head_formula_and_values():
    x1, x2 = symbols("x1 x2")
    for n in range(1, 5):
        p = two_body_projection_formula(n, x1, x2)
        k1 = one_body_kappa(n) * h_norm(2 * n, x1)
        k2 = one_body_kappa(n) * h_norm(2 * n, x2)
        h2 = simplify(p - k1 - k2)
        for m in (1, 2):
            direct = simplify(2 * gaussian_expectation(h_norm(2 * m, x1) * h2**2, (x1, x2)))
            assert simplify(direct - finite_sum_head(n, m)) == 0

    expected_n2 = [2 * sqrt(2) / 9, 28 * sqrt(2) / 27, 410 * sqrt(2) / 243, 14248 * sqrt(2) / 6561]
    expected_n4 = [0, 2 * sqrt(6) / 3, 58 * sqrt(6) / 27, 2948 * sqrt(6) / 729]
    observed_n2 = [finite_sum_head(n, 1) for n in range(1, 5)]
    observed_n4 = [finite_sum_head(n, 2) for n in range(1, 5)]
    assert observed_n2 == expected_n2
    assert observed_n4 == expected_n4


def main():
    check_normalized_pair_expansion()
    print("R38_TWO_BODY_NORMALIZED_EXPANSION PASSED")
    check_full_derivative_and_cancellations()
    print("R38_TWO_BODY_FULL_DERIVATIVE PASSED")
    print("R38_INTERNAL_HOEFFDING_DERIVATIVES_CANCEL PASSED")
    check_finite_head_formula_and_values()
    print("R38_FIXED_HEAD_FINITE_SUM PASSED")
    print("R38_TWO_BODY_CARRIER_WINDOW WEB_REVIEWED_LOCAL_FINITE_CHECK PASSED")
    print("R38_MULTI_GRADE_CONDITIONING REMAINS OPEN")
    print("R38_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
