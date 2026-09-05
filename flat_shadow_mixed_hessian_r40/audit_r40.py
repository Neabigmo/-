"""R40 local exact probe for the mixed-Hessian two-body response.

This is a deliberately small exact calculation prepared while the web review
is working.  It computes the complete mixed second derivative of the
law-dependent degenerate Hoeffding energy, including all five classes of terms
from R39, and prints exact low-degree values.  It is not an asymptotic claim.
"""

import sys
from pathlib import Path

from sympy import expand, simplify, symbols

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    one_body_kappa,
    phi,
    two_body_projection_formula,
)


def mixed_hessian(n, a, b):
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

    displayed = gaussian_expectation((g1 * r2 + r1 * g2) * h2**2, (x1, x2))
    displayed += 2 * gaussian_expectation((g1 + g2) * h2 * dot_r, (x1, x2))
    displayed += 2 * gaussian_expectation((r1 + r2) * h2 * dot_g, (x1, x2))
    displayed += 2 * gaussian_expectation(dot_g * dot_r, (x1, x2))
    displayed += 2 * gaussian_expectation(h2 * ddot_h, (x1, x2))

    epsilon, delta = symbols("epsilon delta")
    h_affine = h2 + epsilon * dot_g + delta * dot_r + epsilon * delta * ddot_h
    density = (1 + epsilon * g1 + delta * r1) * (1 + epsilon * g2 + delta * r2)
    direct_coeff = expand(density * h_affine**2).coeff(epsilon, 1).coeff(delta, 1)
    direct = gaussian_expectation(direct_coeff, (x1, x2))
    assert simplify(displayed - direct) == 0
    return simplify(direct)


def main():
    # The target R39 channel is a=2m+1, b=3.  Keep this deliberately small;
    # the output is a finite exact regression, not a numerical sweep.
    values = [mixed_hessian(n, 7, 3) for n in range(1, 6)]
    print(f"R40_K_N6_VALUES: {values}")
    print("R40_MIXED_HESSIAN_COMPLETE_DECOMPOSITION PASSED")
    print("R40_MIXED_HESSIAN_FINITE_REGRESSION PASSED")
    print("R40_ASYMPTOTIC_RESPONSE REQUIRES_WEB_REVIEW")
    print("R40_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
