"""R41 exact audit for the renormalized mixed-Hessian residue.

The web review supplied a new finite block sum for
T_(r,j)(n)=E[h_(2j)(S) h_(2(r-j))(D) p_n**2], a closed candidate for the
residue limit sigma_m, and an m=3 first-variation coefficient.  This audit
checks the finite block sum, the new S,D coefficients, small exact residue
regressions, and the algebraic specializations of the proposed asymptotic
coefficients.  It does not promote a formal asymptotic expansion to a proof.
"""

import sys
from pathlib import Path

from sympy import Matrix, Rational, binomial, factorial, pi, prod, simplify, sqrt, symbols

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    c,
    gaussian_expectation,
    h_norm,
    two_body_projection_formula,
)
from flat_shadow_hoeffding_transgression_r38.audit_r38 import (  # noqa: E402
    finite_sum_head,
)
from flat_shadow_mixed_hessian_r40.audit_r40 import (  # noqa: E402
    mixed_hessian,
)


def tau_general(p, q, r):
    """Return E[h_p(G) h_q(G) h_r(G)] exactly."""
    numerators = (p + q - r, p + r - q, q + r - p)
    if any(value < 0 or value % 2 for value in numerators):
        return 0
    alpha, beta, gamma = (value // 2 for value in numerators)
    return sqrt(factorial(p) * factorial(q) * factorial(r)) / (
        factorial(alpha) * factorial(beta) * factorial(gamma)
    )


def pair_projection_in_sd(n, s, d):
    return two_body_projection_formula(
        n, (s + d) / sqrt(2), (s - d) / sqrt(2)
    )


def block_direct(n, r, j):
    """Direct Gaussian projection of the web-defined T_(r,j) block."""
    s, d = symbols("s d")
    p = pair_projection_in_sd(n, s, d)
    return simplify(
        gaussian_expectation(
            h_norm(2 * j, s) * h_norm(2 * (r - j), d) * p**2,
            (s, d),
        )
    )


def block_sum(n, r, j):
    """The exact finite (s,b) sum stated in (R41.1)."""
    total = 0
    for shift in range(-j, j + 1):
        for b in range(n + 1):
            bp = b + shift
            if not 0 <= bp <= n:
                continue
            total += (
                Rational(1, 3) ** (2 * b + shift)
                * c(b)
                * c(bp)
                * c(n - b)
                * c(n - bp)
                * tau_general(2 * j, 2 * b, 2 * bp)
                * tau_general(
                    2 * (r - j), 2 * (n - b), 2 * (n - bp)
                )
            )
    return simplify(total)


def sd_coefficient(polynomial, s, d, j, total):
    return simplify(
        gaussian_expectation(
            polynomial * h_norm(j, s) * h_norm(total - j, d),
            (s, d),
        )
    )


def check_block_formula():
    """Check (R41.1) against direct Gaussian integration at small degrees."""
    for n in range(1, 4):
        for r in range(2, 6):
            for j in range(r + 1):
                assert simplify(block_direct(n, r, j) - block_sum(n, r, j)) == 0


def check_q_coefficients():
    """Check the new j=2 and j=4 coefficients of the cancelled block."""
    s, d = symbols("s d")
    for m in (3, 4):
        a = 2 * m + 1
        total = 2 * m + 4
        x1 = (s + d) / sqrt(2)
        x2 = (s - d) / sqrt(2)
        G = h_norm(a, x1) * h_norm(3, x2) + h_norm(3, x1) * h_norm(a, x2)
        chi = sqrt(binomial(total, 3))
        cancelled = G + chi * (h_norm(total, x1) + h_norm(total, x2))
        q2 = Rational(1, 2) ** m * sqrt(3) * (2 * m + 1) * sqrt(2 * m + 2)
        q4 = (
            Rational(1, 2) ** (m - 1)
            * sqrt(2 * m + 1)
            * (2 * m**2 - m + 1)
        )
        assert sd_coefficient(cancelled, s, d, 2, total) == simplify(q2)
        assert sd_coefficient(cancelled, s, d, 4, total) == simplify(q4)


def sigma_candidate(m):
    return simplify(
        -sqrt(6 * (2 * m + 1))
        * (160 * m**3 + 312 * m**2 + 140 * m + 15)
        / (64 * (m + 1) * (m + 2))
    )


def check_sigma_specializations():
    """Check the closed candidate's exact specializations and strict sign."""
    expected_m3 = -7563 * sqrt(42) / 1280
    assert sigma_candidate(3) == expected_m3
    for m in range(3, 9):
        assert sigma_candidate(m) < 0


def check_m3_first_variation_algebra():
    """Divide the supplied m=3 numerator/denominator expansions exactly."""
    numerator0 = -7563 * sqrt(105) / (1280 * sqrt(pi))
    numerator1 = 528849 * sqrt(105) / (40960 * sqrt(pi))
    denominator0 = sqrt(10) / (2 * sqrt(pi))
    denominator1 = -3 * sqrt(10) / (64 * sqrt(pi))
    sigma3 = simplify(numerator0 / denominator0)
    kappa3 = simplify(
        numerator1 / denominator0 - numerator0 * denominator1 / denominator0**2
    )
    assert sigma3 == sigma_candidate(3)
    assert kappa3 == 6327 * sqrt(42) / 512


def check_exact_residue_regressions():
    """Check the new exact S_(n,3) values against independent R40/R38 code."""
    m = 3
    chi = sqrt(binomial(2 * m + 4, 3))
    rho = sqrt(3 * (m + 1)) * (2 * m + 1) * (4 * m + 5) / (4 * (m + 2))
    expected = {
        3: -12231 * sqrt(42) / 5410,
        4: -1070469 * sqrt(42) / 297280,
        5: -104889 * sqrt(42) / 24520,
    }
    for n, target in expected.items():
        K = mixed_hessian(n, 2 * m + 1, 3)
        residue = simplify(
            (K + chi * finite_sum_head(n, m + 2) - rho * finite_sum_head(n, m + 1))
            / finite_sum_head(n, m)
        )
        assert residue == target


def check_four_by_four_determinant():
    """Check the leading 1,n,n^2,n^(-1) determinant identity up to sign."""
    ranks = (1, 2, 3, 5)
    matrix = Matrix([[1] * 4, list(ranks), [n**2 for n in ranks], [Rational(1, n) for n in ranks]])
    determinant = simplify(matrix.det())
    numerator = prod(
        ranks[j] - ranks[i] for i in range(4) for j in range(i + 1, 4)
    )
    rhs = Rational(numerator, prod(ranks))
    assert simplify(determinant**2 - rhs**2) == 0


def main():
    check_block_formula()
    print("R41_BLOCK_FORMULA_FINITE_CHECK PASSED")
    check_q_coefficients()
    print("R41_Q_COEFFICIENTS_FINITE_CHECK PASSED")
    check_sigma_specializations()
    print("R41_SIGMA_SPECIALIZATION_AND_SIGN PASSED")
    check_m3_first_variation_algebra()
    print("R41_M3_FIRST_VARIATION_ALGEBRA PASSED")
    check_exact_residue_regressions()
    print("R41_EXACT_RESIDUE_REGRESSION PASSED")
    check_four_by_four_determinant()
    print("R41_4X4_DETERMINANT_IDENTITY PASSED")
    print("R41_GENERAL_M_FIRST_VARIATION REMAINS OPEN")
    print("R41_ASYMPTOTIC_CLAIMS REMAIN_WEB_DERIVED_UNAUDITED")
    print("R41_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
