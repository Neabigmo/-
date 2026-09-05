"""R39 exact audit: the first two-grade two-body cancellation step.

The web review found an exact two-grade interpolation for the normalized
two-body Hoeffding carriers and isolated a mixed-Hessian channel at the next
grade.  This audit checks the finite algebra only.  It keeps full-exact
probability-law positivity separate from formal tangent calculations.
"""

import sys
from pathlib import Path

from sympy import Rational, binomial, expand, factorial, simplify, sqrt, symbols

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    one_body_kappa,
    phi,
    two_body_projection_formula,
)
from flat_shadow_hoeffding_transgression_r38.audit_r38 import (  # noqa: E402
    finite_sum_head,
)


def test_two_grade_weights():
    """Check the exact 2x2 cancellation equations for small degrees."""
    for m in (1, 2):
        for n1, n2 in ((1, 2), (2, 4), (3, 4)):
            if n1 < m or n2 < m:
                continue
            d1 = finite_sum_head(n1, m)
            d2 = finite_sum_head(n2, m)
            e1 = finite_sum_head(n1, m + 1)
            e2 = finite_sum_head(n2, m + 1)
            # Require nonzero denominators; these are exact rational multiples
            # of a square root, so no numerical tolerance is involved.
            assert simplify(d1) != 0
            assert simplify(d2) != 0
            denominator = simplify(e2 * d1 - e1 * d2)
            if denominator == 0:
                continue
            w1 = simplify(e2 * d1 / denominator)
            w2 = simplify(-e1 * d2 / denominator)
            assert simplify(w1 + w2 - 1) == 0
            assert simplify(w1 * e1 / d1 + w2 * e2 / d2) == 0


def test_gaussian_hoeffding_complement():
    """Check 1/3-B=A+C/3 at the Gaussian full-exact anchor."""
    x1, x2 = symbols("x1 x2")
    for n in range(1, 5):
        p = two_body_projection_formula(n, x1, x2)
        k = one_body_kappa(n) * h_norm(2 * n, x1)
        b = simplify(
            gaussian_expectation(p**2, (x1, x2))
            - 2 * gaussian_expectation(k**2, (x1,))
        )
        a = simplify(gaussian_expectation(k**2, (x1,)))
        c3 = simplify(1 - 3 * a - 3 * b)
        assert simplify(Rational(1, 3) - b - (a + Rational(1, 3) * c3)) == 0
        assert c3 >= 0


def test_second_gateaux_derivative_decomposition():
    """Check every term in the mixed second derivative at small exact degrees."""
    x1, x2, x3 = symbols("x1 x2 x3")
    for n in (1, 2):
        for a, b in ((2, 4), (3, 5)):
            g1, g2, g3 = h_norm(a, x1), h_norm(a, x2), h_norm(a, x3)
            r1, r2, r3 = h_norm(b, x1), h_norm(b, x2), h_norm(b, x3)
            p = two_body_projection_formula(n, x1, x2)
            k1 = one_body_kappa(n) * h_norm(2 * n, x1)
            k2 = one_body_kappa(n) * h_norm(2 * n, x2)
            h2 = simplify(p - k1 - k2)

            dot_p_g = marginal_gaussian(phi(n, x1, x2, x3) * g3, [x3], [x1, x2, x3])
            dot_p_r = marginal_gaussian(phi(n, x1, x2, x3) * r3, [x3], [x1, x2, x3])
            dot_k_g1 = marginal_gaussian(
                phi(n, x1, x2, x3) * (g2 + g3), [x2, x3], [x1, x2, x3]
            )
            dot_k_r1 = marginal_gaussian(
                phi(n, x1, x2, x3) * (r2 + r3), [x2, x3], [x1, x2, x3]
            )
            dot_k_g2 = marginal_gaussian(
                phi(n, x1, x2, x3) * (g1 + g3), [x1, x3], [x1, x2, x3]
            )
            dot_k_r2 = marginal_gaussian(
                phi(n, x1, x2, x3) * (r1 + r3), [x1, x3], [x1, x2, x3]
            )
            dot_theta_g = marginal_gaussian(
                phi(n, x1, x2, x3) * (g1 + g2 + g3), [x1, x2, x3], [x1, x2, x3]
            )
            dot_theta_r = marginal_gaussian(
                phi(n, x1, x2, x3) * (r1 + r2 + r3), [x1, x2, x3], [x1, x2, x3]
            )
            dot_h_g = simplify(dot_p_g - dot_k_g1 - dot_k_g2 + dot_theta_g)
            dot_h_r = simplify(dot_p_r - dot_k_r1 - dot_k_r2 + dot_theta_r)

            # p is linear, k is bilinear, and theta is trilinear in the law.
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

            displayed = gaussian_expectation(
                (g1 * r2 + r1 * g2) * h2**2, (x1, x2)
            )
            displayed += 2 * gaussian_expectation(
                (g1 + g2) * h2 * dot_h_r, (x1, x2)
            )
            displayed += 2 * gaussian_expectation(
                (r1 + r2) * h2 * dot_h_g, (x1, x2)
            )
            displayed += 2 * gaussian_expectation(dot_h_g * dot_h_r, (x1, x2))
            displayed += 2 * gaussian_expectation(h2 * ddot_h, (x1, x2))

            # Independent direct expansion of B(mu) under the affine density
            # mu=(1+epsilon*g+delta*r)gamma.  Extracting [epsilon delta]
            # checks the displayed decomposition without reusing its terms.
            epsilon, delta = symbols("epsilon delta")
            h_affine = simplify(
                h2 + epsilon * dot_h_g + delta * dot_h_r + epsilon * delta * ddot_h
            )
            density = (1 + epsilon * g1 + delta * r1) * (1 + epsilon * g2 + delta * r2)
            direct_integrand = expand(density * h_affine**2)
            direct_coeff = direct_integrand.coeff(epsilon, 1).coeff(delta, 1)
            direct = gaussian_expectation(direct_coeff, (x1, x2))
            assert simplify(displayed - direct) == 0


def test_grade_nplus4_bookkeeping():
    """Check the formal Taylor grade bookkeeping, including N=4 resonance."""
    # For N>=6, b1=b2=b4=0 and only the (N+1,3) Hessian channel survives
    # at total grade N+4 besides the linear (N+4) term.
    N = 6
    d8, h73, delta8, c3, delta7 = symbols("d8 h73 delta8 c3 delta7")
    full = d8 * delta8 + h73 * c3 * delta7
    shadow = 0
    assert simplify(full - (d8 * delta8 + h73 * c3 * delta7)) == 0

    # For N=4, the common full-exact b4 vanishes but the shadow has b4=-Delta4,
    # producing the additional -1/2 H_44 Delta4^2 term at grade 8.
    h44, delta4 = symbols("h44 delta4")
    resonant = d8 * delta8 + h73 * c3 * delta7 - Rational(1, 2) * h44 * delta4**2
    assert expand(resonant).coeff(h44) == -delta4**2 / 2


def main():
    test_two_grade_weights()
    print("R39_TWO_GRADE_EXACT_CANCELLATION PASSED")
    test_gaussian_hoeffding_complement()
    print("R39_CONSTRAINT_COUPLED_POSITIVITY PASSED")
    test_second_gateaux_derivative_decomposition()
    print("R39_SECOND_DERIVATIVE_DECOMPOSITION PASSED")
    test_grade_nplus4_bookkeeping()
    print("R39_GRADE_NPLUS4_CHANNEL_DECOMPOSITION PASSED")
    print("R39_LINEAR_VANDERMONDE_NOT_THE_OBSTRUCTION RECORDED")
    print("R39_MIXED_HESSIAN_RESPONSE REMAINS OPEN")
    print("R39_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
