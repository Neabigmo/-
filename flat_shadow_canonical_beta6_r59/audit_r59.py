"""R59 exact audit: beta6 contraction with corrected quotient orientation.

The browser's flattened fraction display inverted some h/delta quotients.
This audit derives the sixth norm from the exact degree-12 same-factor row and
then computes beta6=h6/h5 directly.
"""

import sys
from pathlib import Path

from sympy import (
    Poly,
    Rational,
    factor,
    factorial,
    hermite_prob,
    limit,
    simplify,
    sqrt,
    symbols,
)


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "flat_shadow_constraint_coupling_r47"))
from audit_r47 import fock_cubic  # noqa: E402


def expectation(poly, x, moments):
    return simplify(
        sum(coefficient * moments[degree[0]]
            for degree, coefficient in Poly(poly, x).terms())
    )


def check_degree_twelve_row_and_beta6():
    x, a = symbols("x a")
    t = a**2
    p4 = t**2 - 64 * t + 16
    p5 = 253 * t**3 - 1278 * t**2 + 816 * t + 160
    p6 = (
        532 * t**6 - 45655 * t**5 + 351508 * t**4
        - 625952 * t**3 + 110432 * t**2 + 83200 * t - 7680
    )
    moments = {
        0: 1,
        1: 0,
        2: 1,
        3: a,
        4: 3,
        5: 4 * a,
        6: 15 + 7 * t,
        7: 15 * a,
        8: 105 + 4 * t,
        9: a * (96 - 112 * t - 49 * t**2) / (2 - t),
        10: 945 - 234 * t,
        11: a * (140 * t**2 - 913 * t - 30) / (2 - t),
        12: (2849 * t**3 - 19102 * t**2 - 15987 * t + 20790) / (2 - t),
    }

    E = lambda poly: expectation(poly, x, moments)
    b = {
        k: simplify(E(hermite_prob(k, x)) / sqrt(factorial(k)))
        for k in (3, 5, 6, 7, 9)
    }
    b12 = -(
        4 * sqrt(1155) * b[3]**2 * b[6]
        - 140 * sqrt(55) * b[3] * b[9]
        - 294 * sqrt(22) * b[5] * b[7]
        + 47 * sqrt(231) * b[6]**2
    ) / 154
    relation = fock_cubic(
        12,
        {0: 1, 3: b[3], 5: b[5], 6: b[6], 7: b[7], 9: b[9], 12: b12},
    )
    assert simplify(relation) == 0

    beta = [
        None,
        Rational(1),
        2 - t,
        6 * (1 + t) / (2 - t),
        p4 / (2 * (2 - t) * (1 + t)),
        p5 / (2 * (1 + t) * p4),
    ]
    alpha = [0, a, -a, 0, 0, 0]
    polys = [1, x]
    norms = [Rational(1), Rational(1)]
    for n in range(1, 6):
        polys.append((x - alpha[n]) * polys[n] - beta[n] * polys[n - 1])
        norms.append(factor(E(polys[n + 1] ** 2)))
    p6_poly = x * polys[5] - beta[5] * polys[4]
    h6 = factor(E(p6_poly**2))
    beta6 = factor(h6 / norms[5])
    assert simplify(norms[5] - 3 * p5 / (2 * (2 - t) * (1 + t))) == 0
    assert simplify(h6 + 6 * p6 / ((2 - t) ** 2 * p4)) == 0
    assert simplify(
        beta6 + 4 * (1 + t) * p6 / ((2 - t) * p4 * p5)
    ) == 0
    print("R59_DEGREE12_SAME_FACTOR_ROW PASSED")
    print("R59_BETA6_DIRECT_H6_OVER_H5_ORIENTATION PASSED")
    print("R59_BETA6_FORMULA", beta6)


def check_beta6_sign_contraction():
    t = symbols("t", nonnegative=True)
    r = 32 - 12 * sqrt(7)
    p4 = t**2 - 64 * t + 16
    p5 = 253 * t**3 - 1278 * t**2 + 816 * t + 160
    p6 = (
        532 * t**6 - 45655 * t**5 + 351508 * t**4
        - 625952 * t**3 + 110432 * t**2 + 83200 * t - 7680
    )
    p6_prime = simplify(p6.diff(t))
    r0 = Rational(13, 50)
    # r<13/50.  On [0,r0], discard positive t^3,t^5 terms and bound
    # t^2<=r0*t, t^4<=r0^3*t in the negative terms.
    linear_coeff = 220864 - 1877856 * r0 - 228275 * r0**3
    lower_at_r0 = simplify(83200 + linear_coeff * r0)
    assert simplify(r0 - r) > 0
    assert linear_coeff < 0
    assert lower_at_r0 > 0
    assert p6_prime.subs(t, 0) > 0

    # p4 has roots r and 32+12*sqrt(7), so it is positive on (0,r).
    assert simplify(p4.subs(t, r)) == 0
    assert simplify(p4.subs(t, 0)) > 0
    # p5 >= 160 + (816-1278*r)*t > 0 on [0,r].
    assert simplify(816 - 1278 * r0) > 0
    assert simplify(p5.subs(t, 0)) > 0

    assert p6.subs(t, Rational(1, 20)) < 0
    assert p6.subs(t, Rational(1, 10)) > 0
    print("R59_P6_STRICT_MONOTONICITY_ON_SURVIVING_INTERVAL PASSED")
    print("R59_P6_SIGN_BRACKET_AND_UNIQUE_TAU6 PASSED")
    print("R59_BETA2_TO_BETA6_POSITIVE_IFF_0_LT_T_LT_TAU6 CONDITIONALLY PASSED")


def check_conditional_ou_consequence():
    lam, r = symbols("lambda r", nonnegative=True)
    assert simplify(2 - 2 * (1 - lam) ** 2 - 2 * lam * (2 - lam)) == 0
    assert limit(2 * r * (2 - r), r, 0, dir="+") == 0
    print("R59_OU_FAVARD_BRIDGE_NOT_AUTOMATICALLY_AVAILABLE REMAINS OPEN")
    print("R59_CONDITIONAL_DEEP_OU_M3_ZERO PASSED")


def main():
    check_degree_twelve_row_and_beta6()
    check_beta6_sign_contraction()
    check_conditional_ou_consequence()
    print("R59_CANONICAL_BETA7_CONTRACTION REMAINS OPEN")
    print("R59_D1_AND_EVENTUAL_SKEW_ANNIHILATION REMAIN OPEN")
    print("R59_GAUSSIAN_RIGIDITY_AND_P3K REMAIN DISTINCT OPEN")
    print("R59_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
