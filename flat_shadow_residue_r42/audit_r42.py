"""R42 exact audit for the bivariate residue generators and m=4 assembly.

The web review supplied exact generating functions for the R41 blocks and for
the odd conditional derivative, plus a complete m=4 asymptotic assembly.  The
finite checks below distinguish those exact identities from the supplied
singular expansions: the latter are only checked algebraically after the
coefficients are supplied.
"""

import sys
from pathlib import Path

from sympy import (
    Matrix,
    Poly,
    Rational,
    binomial,
    expand,
    factorial,
    pi,
    rf,
    simplify,
    sqrt,
    symbols,
)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    c,
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    phi,
    two_body_projection_formula,
)
from flat_shadow_hoeffding_transgression_r38.audit_r38 import (  # noqa: E402
    finite_sum_head,
)
from flat_shadow_mixed_hessian_r40.audit_r40 import (  # noqa: E402
    mixed_hessian,
)
from flat_shadow_residue_r41.audit_r41 import (  # noqa: E402
    tau_general,
)


def block_sum_bivariate(k, ell, r, j):
    """Exact coefficient sum for E[h_(2j)(S)h_(2r-2j)(D)p_k p_ell]."""
    total = 0
    for b in range(k + 1):
        for bp in range(ell + 1):
            total += (
                (-1) ** (k + ell)
                * Rational(1, 3) ** (b + bp)
                * c(b)
                * c(bp)
                * c(k - b)
                * c(ell - bp)
                * tau_general(2 * j, 2 * b, 2 * bp)
                * tau_general(
                    2 * (r - j), 2 * (k - b), 2 * (ell - bp)
                )
            )
    return simplify(total)


def denominator_coefficient(t, alpha, beta):
    """[u^t](1-u/9)^(-alpha)(1-u)^(-beta), exactly."""
    if t < 0:
        return 0
    return simplify(
        sum(
            rf(alpha, p) / factorial(p) * Rational(1, 9) ** p
            * rf(beta, t - p) / factorial(t - p)
            for p in range(t + 1)
        )
    )


def block_generator_coefficient(k, ell, r, j):
    """Coefficient of z^k w^ell in the exact R42.3 generator."""
    z, w = symbols("z w")
    numerator = expand(
        (z + w - Rational(2, 3) * z * w) ** j
        * (z + w - 2 * z * w) ** (r - j)
    )
    polynomial = Poly(numerator, z, w)
    alpha = Rational(1, 2) + j
    beta = Rational(1, 2) + r - j
    coefficient = 0
    for (power_z, power_w), value in polynomial.terms():
        if k - power_z != ell - power_w:
            continue
        coefficient += value * denominator_coefficient(
            k - power_z, alpha, beta
        )
    prefactor = (-1) ** r * Rational(1, 3) ** j * c(j) * c(r - j)
    return simplify(prefactor * coefficient)


def check_bivariate_block_generator():
    """Check R42.3 against the exact double finite Hermite sum."""
    for k in range(4):
        for ell in range(4):
            for r in range(1, 5):
                for j in range(r + 1):
                    lhs = block_sum_bivariate(k, ell, r, j)
                    rhs = block_generator_coefficient(k, ell, r, j)
                    assert simplify(lhs - rhs) == 0


def rational_series_coefficients(expression, variable, order):
    return [
        simplify(expand(expression.series(variable, 0, order).removeO()).coeff(variable, i))
        for i in range(order)
    ]


def dot_p3_generator_coefficient(n, s, d):
    """Coefficient of z^n in the exact R42.5 generating function."""
    z = symbols("z")
    f1 = 2 * sqrt(3) * z**2 * (2 * z - 3) / (3 - z) ** 3
    f3 = 2 * sqrt(2) * z**3 / (3 - z) ** 3
    f1_coeffs = rational_series_coefficients(f1, z, n + 1)
    f3_coeffs = rational_series_coefficients(f3, z, n + 1)
    h1s, h3s = h_norm(1, s), h_norm(3, s)
    result = 0
    for q in range(n + 1):
        p = two_body_projection_formula(
            n - q, (s + d) / sqrt(2), (s - d) / sqrt(2)
        )
        result += p * (f1_coeffs[q] * h1s + f3_coeffs[q] * h3s)
    return simplify(result)


def dot_p3_direct(n, s, d):
    x1, x2, x3 = symbols("x1 x2 x3")
    direct = marginal_gaussian(
        phi(n, x1, x2, x3) * h_norm(3, x3),
        [x3],
        [x1, x2, x3],
    )
    return simplify(
        direct.subs(
            {
                x1: (s + d) / sqrt(2),
                x2: (s - d) / sqrt(2),
            }
        )
    )


def check_dot_p3_generator():
    """Check R42.5 by direct Gaussian marginalization for n<=3."""
    s, d = symbols("s d")
    for n in range(4):
        assert simplify(dot_p3_generator_coefficient(n, s, d) - dot_p3_direct(n, s, d)) == 0


def sd_coefficient(polynomial, s, d, j, total):
    return simplify(
        gaussian_expectation(
            polynomial * h_norm(j, s) * h_norm(total - j, d),
            (s, d),
        )
    )


def check_m4_q_coefficients():
    s, d = symbols("s d")
    m = 4
    a = 2 * m + 1
    total = 2 * m + 4
    x1 = (s + d) / sqrt(2)
    x2 = (s - d) / sqrt(2)
    G = h_norm(a, x1) * h_norm(3, x2) + h_norm(3, x1) * h_norm(a, x2)
    chi = sqrt(binomial(total, 3))
    cancelled = G + chi * (h_norm(total, x1) + h_norm(total, x2))
    expected = {
        2: Rational(9, 16) * sqrt(30),
        4: Rational(87, 8),
        6: Rational(11, 8) * sqrt(105),
    }
    for j, value in expected.items():
        assert sd_coefficient(cancelled, s, d, j, total) == value


def check_m4_residue_quotient_algebra():
    """Verify the supplied m=4 numerator/denominator assembly exactly."""
    rho = Rational(63, 8) * sqrt(15)
    w7 = -Rational(31461, 10240) * sqrt(210) / sqrt(pi)
    w5 = Rational(366125, 131072) * sqrt(210) / sqrt(pi)
    d7 = -Rational(9, 1280) * sqrt(14) / sqrt(pi)
    d5 = -Rational(68973, 81920) * sqrt(14) / sqrt(pi)
    c7 = -Rational(9, 256) * sqrt(210) / sqrt(pi)
    c5 = Rational(911, 8192) * sqrt(210) / sqrt(pi)
    numerator7 = simplify(w7 - rho * d7 + 2 * c7)
    numerator5 = simplify(w5 - rho * d5 + 2 * c5)
    assert numerator7 == -Rational(15807, 5120) * sqrt(210) / sqrt(pi)
    assert numerator5 == Rational(1580421, 163840) * sqrt(210) / sqrt(pi)

    denominator0 = sqrt(35) / (8 * sqrt(pi))
    denominator1 = -Rational(3, 256) * sqrt(35) / sqrt(pi)
    sigma4 = simplify(numerator7 / denominator0)
    kappa4 = simplify(numerator5 / denominator0 - numerator7 * denominator1 / denominator0**2)
    assert sigma4 == -Rational(15807, 640) * sqrt(6)
    assert kappa4 == Rational(38325, 512) * sqrt(6)


def check_m4_exact_residue_regression():
    m = 4
    n = 4
    chi = sqrt(binomial(2 * m + 4, 3))
    rho = sqrt(3 * (m + 1)) * (2 * m + 1) * (4 * m + 5) / (4 * (m + 2))
    K = mixed_hessian(n, 2 * m + 1, 3)
    residue = simplify(
        (K + chi * finite_sum_head(n, m + 2) - rho * finite_sum_head(n, m + 1))
        / finite_sum_head(n, m)
    )
    assert K == -Rational(25808, 2187) * sqrt(105)
    assert finite_sum_head(n, 4) == Rational(262, 81) * sqrt(70)
    assert finite_sum_head(n, 5) == Rational(19040, 2187) * sqrt(7)
    assert finite_sum_head(n, 6) == Rational(1640, 2187) * sqrt(231)
    assert residue == -Rational(11639, 1179) * sqrt(6)


def check_m4_weighted_conditioning():
    """Check the exact exponent arithmetic used for the conditional step."""
    # kappa_4 != 0 gives an n^(-1) residue row; the carrier scale is n^(-7/2).
    assert simplify(Rational(1) - 4 + Rational(1, 2)) == -Rational(5, 2)
    ranks = (1, 2, 3, 5)
    matrix = Matrix(
        [[1] * 4, list(ranks), [n**2 for n in ranks], [Rational(1, n) for n in ranks]]
    )
    assert matrix.det() != 0


def main():
    check_bivariate_block_generator()
    print("R42_BLOCK_BIVARIATE_GENERATOR PASSED")
    check_dot_p3_generator()
    print("R42_DOTP3_GENERATOR PASSED")
    check_m4_q_coefficients()
    print("R42_M4_Q_COEFFICIENTS PASSED")
    check_m4_residue_quotient_algebra()
    print("R42_M4_RESIDUE_QUOTIENT_ALGEBRA PASSED")
    check_m4_exact_residue_regression()
    print("R42_M4_EXACT_RESIDUE_REGRESSION PASSED")
    check_m4_weighted_conditioning()
    print("R42_M4_WEIGHTED_CONDITIONING PASSED")
    print("R42_M4_SINGULAR_EXPANSIONS REMAIN_WEB_DERIVED_UNAUDITED")
    print("R42_GENERAL_M_KAPPA REMAINS OPEN")
    print("R42_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
