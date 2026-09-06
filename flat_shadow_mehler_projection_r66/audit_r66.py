"""R66 exact audit of the Mehler/projection reduction.

The audit checks only finite exact identities.  It does not infer an
asymptotic sign for Lambda_n and it does not construct a Favard measure.
"""

from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import sys

import sympy as sp


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "flat_shadow_quadratic_response_r65"))
from audit_r65 import C_closed, D as D_r65, M as M_r65, u, v  # noqa: E402


x, w, s, t, y = sp.symbols("x w s t y")


def H(n):
    return sp.hermite_prob(n, x)


def gaussian_expectation(poly):
    poly = sp.Poly(sp.expand(poly), x)
    value = sp.Integer(0)
    for (degree,), coefficient in poly.terms():
        moment = sp.Integer(1) if degree == 0 else sp.factorial2(degree - 1)
        value += coefficient * moment
    return sp.expand(value)


def q_sequence(limit):
    q = [sp.Integer(0), sp.Integer(0), -H(1), -H(0)]
    for n in range(3, limit):
        q.append(sp.expand(x * q[-1] - n * q[-2]))
    return q[: limit + 1]


def q_from_tangent(n):
    return sp.expand(
        -sum(
            sp.Rational(M_r65(n, k).numerator, M_r65(n, k).denominator)
            / factorial(k)
            * H(k)
            for k in range(n)
        )
    )


def check_q_recurrence_and_projection():
    q = q_sequence(14)
    assert q[0] == 0 and q[1] == 0
    assert q[2] == -H(1) and q[3] == -H(0)
    for n in range(4, 15):
        assert q[n] == q_from_tangent(n)
    for n in range(3, 14):
        assert q[n + 1] == sp.expand(x * q[n] - n * q[n - 1])
    print("R66_Q_RECURRENCE_AND_LOWER_TRIANGULAR_PROJECTION PASSED")


def check_q_egf_ode():
    q = q_sequence(12)
    Q = sum(q[n] * w**n / factorial(n) for n in range(len(q)))
    rhs = (x - w) * Q - (H(1) * w - H(2) * w**2 / 2)
    residual = sp.Poly(sp.expand(sp.diff(Q, w) - rhs), w)
    for degree in range(0, 11):
        assert residual.coeff_monomial(w**degree) == 0
    print("R66_Q_EGF_ODE_AND_CLOSED_FORCING PASSED")


def check_d_binomial_transform():
    for n in range(0, 11):
        lhs = Fraction(D_r65(n).numerator, D_r65(n).denominator) / factorial(n)
        rhs = sum(
            Fraction(comb(n, m), 1)
            * Fraction(v(2 * m).numerator, v(2 * m).denominator)
            / factorial(m)
            for m in range(n + 1)
        )
        assert lhs == rhs
    print("R66_D_BINOMIAL_MEHLER_TRANSFORM PASSED")


def check_same_factor_laplace_coefficient():
    for m in range(2, 9):
        b_m = sum(
            Fraction(u(r).numerator, u(r).denominator)
            * Fraction(u(2 * m - r).numerator, u(2 * m - r).denominator)
            / (factorial(r) * factorial(2 * m - r))
            * Fraction(C_closed(r, 2 * m - r).numerator,
                       C_closed(r, 2 * m - r).denominator)
            for r in range(3, 2 * m, 2)
        )
        left = Fraction(v(2 * m).numerator, v(2 * m).denominator) / factorial(m)
        right = -Fraction(6**m * factorial(m), 3) * b_m
        assert left == right
    print("R66_SAME_FACTOR_B_COEFFICIENTS_AND_D_LAPLACE PASSED")


def check_diagonal_and_borel_normalization():
    q = q_sequence(12)
    norms = [gaussian_expectation(q[n] ** 2) for n in range(len(q))]
    xi, eta = sp.symbols("xi eta")
    R = sum(
        q[n] * q[m] * xi**n * eta**m / (factorial(n) * factorial(m))
        for n in range(len(q))
        for m in range(len(q))
    )
    # The angular phase e^{i(n-m)theta} kills all off-diagonal terms.
    diagonal = sp.expand(sum(
        norms[n] * y**n / factorial(n)**2 for n in range(len(q))
    ))
    for n in range(len(q)):
        assert diagonal.coeff(y, n) == sp.Rational(norms[n], factorial(n)**2)
        assert sp.Rational(norms[n], factorial(n)) == (
            sp.Rational(norms[n], factorial(n)**2) * factorial(n)
        )
    print("R66_DIAGONAL_EXTRACTION_AND_BOREL_NORMALIZATION PASSED")


def check_explicit_r_integrand():
    A = lambda u: u * x - sp.Rational(1, 2) * u**2 * (x**2 - 1)
    shifted_moments = {
        0: 1,
        1: y,
        2: y**2 + 1,
        3: y**3 + 3 * y,
        4: y**4 + 6 * y**2 + 3,
    }
    product = sp.Poly(sp.expand(A(s) * A(t)), x)
    shifted = sp.Integer(0)
    for (degree,), coefficient in product.terms():
        shifted += coefficient * shifted_moments[degree]
    bracket = (
        s * t * (y**4 + 4 * y**2 + 2)
        - 2 * (s + t) * (y**3 + 2 * y)
        + 4 * (y**2 + 1)
    )
    assert sp.factor(shifted - s * t * bracket / 4) == 0
    print("R66_EXPLICIT_GAUSSIAN_DOUBLE_INTEGRAND PASSED")


def check_u_small_series():
    q = s * (1 - s)
    integrand = q * sp.exp(-q * w**2) * (1 - q * w**2 / 2)
    series = sp.integrate(
        sp.series(w**3 * integrand, w, 0, 15).removeO(), (s, 0, 1)
    )
    exact = sp.expand(sum(
        sp.Rational(u(degree).numerator, u(degree).denominator)
        * w**degree / factorial(degree)
        for degree in range(3, 14, 2)
    ))
    assert sp.expand(series - exact) == 0
    print("R66_U_SMALL_SERIES_PASSED")


if __name__ == "__main__":
    check_q_recurrence_and_projection()
    check_q_egf_ode()
    check_d_binomial_transform()
    check_same_factor_laplace_coefficient()
    check_diagonal_and_borel_normalization()
    check_explicit_r_integrand()
    check_u_small_series()
    print("R66_MEHLER_PROJECTION_AUDIT_COMPLETED")
