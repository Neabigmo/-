"""R64 exact audit of the structural quadratic-response formulas.

The checks are finite but exact.  They validate the all-degree formulas against
the audited canonical moments through degree 20; the general statement in the
README is conditional on the full same-factor hierarchy.
"""

from math import comb, factorial
from pathlib import Path
import sys

from sympy import I, Poly, Rational, expand, hermite_prob, simplify, sqrt, symbols


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "flat_shadow_canonical_beta9_r62"))
from audit_r62 import family_data  # noqa: E402


def canonical_data(a, t):
    _, _, _, _, _, _, beta, moments = family_data(a, t)
    moments = dict(moments)
    moments[19] = 9 * a * (55917589*t**5 - 184963800*t**4 + 55863471*t**3
                           + 179281750*t**2 + 11558100*t - 16463160) / (2 - t)**3
    moments[20] = (-14571660838*t**6 + 520027461774*t**5
                   - 2971081076052*t**4 + 6147868133237*t**3
                   - 4337195160894*t**2 - 8050748580*t + 5237832600) / (2 - t)**3
    return beta, moments


def expectation(poly, x, moments):
    return simplify(sum(coefficient * moments[degree[0]]
                        for degree, coefficient in Poly(poly, x).terms()))


def root_of_unity_pair_average(r, s):
    """Exact C_(r,s)=<sum_{i<j} r_i^r r_j^s> for the three-factor angles."""
    omega = -Rational(1, 2) + I * sqrt(3) / 2
    total = 0
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for p in range(r + 1):
            for q in range(s + 1):
                if 2*p - r + 2*q - s == 0:
                    total += (Rational(1, 6) ** ((r + s) // 2)
                              * comb(r, p) * comb(s, q)
                              * omega ** (i*(2*p-r) + j*(2*q-s)))
    return simplify(expand(total))


def odd_tangent_and_even_convolution():
    a, t, x = symbols("a t x")
    _, moments = canonical_data(a, t)

    def hermite_value(n):
        return expectation(hermite_prob(n, x), x, moments)

    def odd_tangent(n):
        return simplify(hermite_value(n).coeff(a).subs(t, 0))

    for m in range(1, 10):
        degree = 2*m + 1
        target = (-1)**(m - 1) * Rational(m * factorial(m + 1), 2)
        assert odd_tangent(degree) == target
    print("R64_ALL_DEGREE_ODD_HERMITE_TANGENT_THROUGH_19 PASSED")

    def u(degree):
        m = (degree - 1) // 2
        return (-1)**(m - 1) * Rational(m * factorial(m + 1), 2)

    for n in range(2, 11):
        degree = 2*n
        v = simplify(hermite_value(degree).diff(t).subs({t: 0, a: 0}))
        rhs = 0
        for r in range(3, degree, 2):
            s = degree - r
            if s >= 3:
                rhs += (u(r) * u(s) / (factorial(r) * factorial(s))
                        * root_of_unity_pair_average(r, s))
        A = Rational(3, 6**n) * comb(2*n, n)
        assert simplify(v / factorial(degree) + rhs / A) == 0
    print("R64_SAME_FACTOR_EVEN_QUADRATIC_CONVOLUTION_THROUGH_20 PASSED")


def norm_curvature_formula():
    a, t, x = symbols("a t x")
    beta, moments = canonical_data(a, t)

    def L(poly):
        return expectation(poly, x, moments)

    def L1(poly):
        return simplify(expand(L(poly)).coeff(a).subs(t, 0))

    def L2(poly):
        return simplify(expand(L(poly)).diff(t).subs({t: 0, a: 0}))

    K = {}
    for n in range(0, 11):
        Hn = hermite_prob(n, x)
        value = L2(Hn**2)
        for k in range(n):
            Hk = hermite_prob(k, x)
            value -= L1(Hn * Hk)**2 / factorial(k)
        K[n] = simplify(value)

    for n in range(2, 11):
        predicted = simplify((K[n] - n*K[n-1]) / factorial(n - 1))
        expected = (simplify(beta[n].diff(t).subs(t, 0)) if n < len(beta)
                    else Rational(-1481, 21))
        assert predicted == expected
    print("R64_NORM_CURVATURE_BETA_SLOPES_THROUGH_10 PASSED")


if __name__ == "__main__":
    odd_tangent_and_even_convolution()
    norm_curvature_formula()
    print("R64_STRUCTURAL_RESPONSE_AUDIT_COMPLETED")
