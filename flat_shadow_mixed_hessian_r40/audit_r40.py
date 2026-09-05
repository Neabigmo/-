"""R40 local exact probe for the mixed-Hessian two-body response.

This is a deliberately small exact calculation prepared while the web review
is working.  It computes the complete mixed second derivative of the
law-dependent degenerate Hoeffding energy, including all five classes of terms
from R39, and prints exact low-degree values.  It is not an asymptotic claim.
"""

import sys
from pathlib import Path

from sympy import Rational, binomial, expand, simplify, sqrt, symbols

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    one_body_kappa,
    phi,
    two_body_projection_formula,
)


def mixed_hessian(n, a, b, *, return_terms=False):
    """Return D^2 B_n(gamma)[h_a,h_b] by two independent exact expansions."""
    x1, x2, x3 = symbols("x1 x2 x3")
    g1, g2, g3 = h_norm(a, x1), h_norm(a, x2), h_norm(a, x3)
    r1, r2, r3 = h_norm(b, x1), h_norm(b, x2), h_norm(b, x3)
    p = two_body_projection_formula(n, x1, x2)
    k1 = one_body_kappa(n) * h_norm(2 * n, x1)
    k2 = one_body_kappa(n) * h_norm(2 * n, x2)
    h2 = simplify(p - k1 - k2)

    def first(g_left, g_right, g_third):
        dp = marginal_gaussian(phi(n, x1, x2, x3) * g_third, [x3], [x1, x2, x3])
        dk1 = marginal_gaussian(
            phi(n, x1, x2, x3) * (g_right + g_third),
            [x2, x3],
            [x1, x2, x3],
        )
        dk2 = marginal_gaussian(
            phi(n, x1, x2, x3) * (g_left + g_third),
            [x1, x3],
            [x1, x2, x3],
        )
        dtheta = marginal_gaussian(
            phi(n, x1, x2, x3) * (g_left + g_right + g_third),
            [x1, x2, x3],
            [x1, x2, x3],
        )
        return simplify(dp - dk1 - dk2 + dtheta)

    dot_g = first(g1, g2, g3)
    dot_r = first(r1, r2, r3)
    ddot_k1 = marginal_gaussian(
        phi(n, x1, x2, x3) * (g2 * r3 + r2 * g3),
        [x2, x3],
        [x1, x2, x3],
    )
    ddot_k2 = marginal_gaussian(
        phi(n, x1, x2, x3) * (g1 * r3 + r1 * g3),
        [x1, x3],
        [x1, x2, x3],
    )
    ddot_theta = marginal_gaussian(
        phi(n, x1, x2, x3)
        * (
            g1 * r2
            + r1 * g2
            + g1 * r3
            + r1 * g3
            + g2 * r3
            + r2 * g3
        ),
        [x1, x2, x3],
        [x1, x2, x3],
    )
    ddot_h = simplify(-ddot_k1 - ddot_k2 + ddot_theta)

    terms = {
        "W": gaussian_expectation((g1 * r2 + r1 * g2) * h2**2, (x1, x2)),
        "g_cross": 2 * gaussian_expectation(
            (g1 + g2) * h2 * dot_r, (x1, x2)
        ),
        "r_cross": 2 * gaussian_expectation(
            (r1 + r2) * h2 * dot_g, (x1, x2)
        ),
        "dot_dot": 2 * gaussian_expectation(dot_g * dot_r, (x1, x2)),
        "ddot": 2 * gaussian_expectation(h2 * ddot_h, (x1, x2)),
    }
    displayed = sum(terms.values())

    epsilon, delta = symbols("epsilon delta")
    h_affine = h2 + epsilon * dot_g + delta * dot_r + epsilon * delta * ddot_h
    density = (1 + epsilon * g1 + delta * r1) * (1 + epsilon * g2 + delta * r2)
    direct_coeff = expand(density * h_affine**2).coeff(epsilon, 1).coeff(delta, 1)
    direct = gaussian_expectation(direct_coeff, (x1, x2))
    assert simplify(displayed - direct) == 0
    direct = simplify(direct)
    if return_terms:
        return {**terms, "direct": direct}
    return direct


def sd_coefficient(polynomial, s, d, j, total):
    """Project a total-chaos polynomial onto h_j(S) h_(total-j)(D)."""
    return simplify(
        gaussian_expectation(
            polynomial * h_norm(j, s) * h_norm(total - j, d), (s, d)
        )
    )


def check_web_finite_coefficients():
    """Check the new exact S,D leading-cancellation coefficients."""
    s, d = symbols("s d")
    for m in (3, 4):
        a = 2 * m + 1
        total = 2 * m + 4
        x1 = (s + d) / sqrt(2)
        x2 = (s - d) / sqrt(2)
        G = h_norm(a, x1) * h_norm(3, x2) + h_norm(3, x1) * h_norm(a, x2)
        sum_total = h_norm(total, x1) + h_norm(total, x2)
        chi = sqrt(binomial(total, 3))
        assert sd_coefficient(G, s, d, 0, total) == simplify(
            -2 ** (1 - Rational(total, 2)) * chi
        )
        q2 = simplify(
            Rational(1, 2) ** m * sqrt(3) * (2 * m + 1) * sqrt(2 * m + 2)
        )
        assert sd_coefficient(G + chi * sum_total, s, d, 2, total) == q2


def check_cancellation_terms_and_regressions():
    """Audit exact chaos cancellations and the web's extra low-order point."""
    values = []
    for n in range(1, 6):
        terms = mixed_hessian(n, 7, 3, return_terms=True)
        values.append(terms["direct"])
        assert terms["dot_dot"] == 0
        assert terms["ddot"] == 0
        assert terms["r_cross"] == 0
        assert simplify(terms["direct"] - terms["W"] - terms["g_cross"]) == 0
    assert values[2] == -100 * sqrt(210) / 81
    assert values[3] == -25264 * sqrt(210) / 2187
    assert values[4] == -320648 * sqrt(210) / 6561
    assert mixed_hessian(4, 9, 3) == -25808 * sqrt(105) / 2187
    return values


def main():
    # The target R39 channel is a=2m+1, b=3.  Keep this deliberately small;
    # the output is a finite exact regression, not a numerical sweep.
    values = check_cancellation_terms_and_regressions()
    print(f"R40_K_N6_VALUES: {values}")
    print("R40_MIXED_HESSIAN_COMPLETE_DECOMPOSITION PASSED")
    print("R40_CHAOS_CROSS_TERMS_CANCEL PASSED")
    check_web_finite_coefficients()
    print("R40_LEADING_COMPONENT_COEFFICIENTS PASSED")
    print("R40_MIXED_HESSIAN_FINITE_REGRESSION PASSED")
    print("R40_ASYMPTOTIC_RESPONSE WEB_CANDIDATE_RECORDED_UNAUDITED")
    print("R40_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
