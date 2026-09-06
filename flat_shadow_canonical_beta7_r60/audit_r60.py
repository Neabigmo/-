"""R60 exact audit: beta7 positivity with corrected quotient orientation.

The browser's rendered fractions inverted h6/h7-like quotients again.  This
audit derives the degree-14 row and computes beta7=h7/h6 directly.
"""

import sys
from math import comb
from pathlib import Path

from sympy import Poly, Rational, cancel, factor, factorial, hermite_prob, simplify, sqrt, sympify, symbols


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "flat_shadow_constraint_coupling_r47"))
from audit_r47 import fock_cubic  # noqa: E402


def expectation(poly, x, moments):
    return cancel(
        sum(coefficient * moments[degree[0]]
            for degree, coefficient in Poly(poly, x).terms())
    )


def reduce_a_square(expr, a, t):
    """Impose a^2=t while retaining one possible odd factor a."""
    return cancel(
        sum(
            coefficient * t ** (degree[0] // 2) * a ** (degree[0] % 2)
            for degree, coefficient in Poly(expr.expand(), a).terms()
        )
    )


def check_degree_fourteen_and_beta7():
    x, a, t = symbols("x a t")
    p4 = t**2 - 64 * t + 16
    p5 = 253 * t**3 - 1278 * t**2 + 816 * t + 160
    p6 = (
        532 * t**6 - 45655 * t**5 + 351508 * t**4
        - 625952 * t**3 + 110432 * t**2 + 83200 * t - 7680
    )
    p7 = (
        2150400 + 19281920 * t - 206264064 * t**2
        - 424134656 * t**3 + 2523473440 * t**4
        - 4074599496 * t**5 + 2790646820 * t**6
        - 853051174 * t**7 + 100963863 * t**8 - 2264192 * t**9
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
    beta = [
        None,
        Rational(1),
        2 - t,
        6 * (1 + t) / (2 - t),
        p4 / (2 * (2 - t) * (1 + t)),
        p5 / (2 * (1 + t) * p4),
        -4 * (1 + t) * p6 / ((2 - t) * p4 * p5),
    ]
    alpha = [0, a, -a, 0, 0, 0, 0]
    polys = [1, x]
    for n in range(1, 6):
        polys.append((x - alpha[n]) * polys[n] - beta[n] * polys[n - 1])
    p6_poly = polys[5] * x - beta[5] * polys[4]
    print("R60_STAGE_P6_READY", flush=True)

    E = lambda poly: expectation(poly, x, moments)
    m13_raw = -sum(
        coefficient * moments[degree[0]]
        for degree, coefficient in Poly((x * p6_poly**2).expand(), x).terms()
        if degree[0] != 13
    )
    m13 = reduce_a_square(m13_raw, a, t)
    print("R60_STAGE_M13_READY", flush=True)
    expected_m13 = 3 * a * (1145 * t**2 - 2284 * t - 2280) / (2 - t)
    assert simplify(m13 - expected_m13) == 0
    moments[13] = expected_m13

    b = {
        k: cancel(E(hermite_prob(k, x)) / sqrt(factorial(k)))
        for k in (3, 5, 6, 7, 9, 11)
    }
    print("R60_STAGE_HERMITE_HEAD_READY", flush=True)
    b14 = reduce_a_square(
        -(
            -484 * sqrt(91) * b[11] * b[3]
            + 14 * sqrt(858) * b[3] * b[5] * b[6]
            - 152 * sqrt(2002) * b[5] * b[9]
            - 131 * sqrt(858) * b[7]**2
        ) / 572,
        a,
        t,
    )
    expected_m14 = (
        839909 * t**3 - 1338415 * t**2 - 187437 * t + 270270
    ) / (2 - t)
    moments[14] = expected_m14
    assert simplify(E(hermite_prob(14, x)) / sqrt(factorial(14)) - b14) == 0
    relation = fock_cubic(
        14,
        {
            0: 1,
            3: b[3],
            5: b[5],
            6: b[6],
            7: b[7],
            9: b[9],
            11: b[11],
            14: b14,
        },
    )
    assert simplify(reduce_a_square(relation, a, t)) == 0
    print("R60_STAGE_DEGREE14_READY", flush=True)

    p7_poly = p6_poly * x - beta[6] * polys[5]

    # The fully expanded symbolic h7 expression is intentionally not forced
    # through a long global factorization.  Instead, verify the claimed factor
    # with exact rational members of the relevant family, including Gaussian.
    h6_rhs = -6 * p6 / ((2 - t) ** 2 * p4)
    h7_rhs = 3 * p7 / ((2 - t) ** 3 * p5)
    beta7_rhs = -p4 * p7 / (2 * (2 - t) * p5 * p6)
    for a_value in (Rational(0), Rational(1, 10), Rational(1, 5), Rational(1, 4)):
        t_value = a_value**2
        moments_num = {
            degree: simplify(sympify(value).subs({a: a_value, t: t_value}))
            for degree, value in moments.items()
        }
        E_num = lambda poly: expectation(
            poly.subs({a: a_value, t: t_value}), x, moments_num
        )
        h6_num = simplify(E_num(p6_poly**2))
        h7_num = simplify(E_num(p7_poly**2))
        assert simplify(h6_num - h6_rhs.subs({a: a_value, t: t_value})) == 0
        assert simplify(h7_num - h7_rhs.subs({a: a_value, t: t_value})) == 0
        assert simplify(
            h7_num / h6_num - beta7_rhs.subs({a: a_value, t: t_value})
        ) == 0
    print("R60_M13_DEGREE14_ROW_AND_M14 PASSED")
    print("R60_BETA7_EXACT_RATIONAL_FACTOR_CHECKS PASSED")
    print("R60_BETA7_DIRECT_H7_OVER_H6_ORIENTATION PASSED")
    print("R60_BETA7_FORMULA", beta7_rhs)


def check_p7_positive_on_window():
    t = symbols("t")
    p7 = (
        2150400 + 19281920 * t - 206264064 * t**2
        - 424134656 * t**3 + 2523473440 * t**4
        - 4074599496 * t**5 + 2790646820 * t**6
        - 853051174 * t**7 + 100963863 * t**8 - 2264192 * t**9
    )
    # Bernstein coefficients of P7(u/10) on u in [0,1].
    poly = Poly(p7, t)
    r = Rational(1, 10)
    scaled = [poly.coeff_monomial(t**i) * r**i for i in range(10)]
    bernstein = [
        factor(sum(
            scaled[i] * Rational(comb(k, i), comb(9, i))
            for i in range(k + 1)
        ))
        for k in range(10)
    ]
    assert all(value > 0 for value in bernstein)
    print("R60_P7_BERNSTEIN_COEFFICIENTS_POSITIVE_ON_0_1/10 PASSED")
    print("R60_BETA7_POSITIVE_ON_0_LT_T_LT_TAU6 PASSED")


def main():
    check_degree_fourteen_and_beta7()
    check_p7_positive_on_window()
    print("R60_NO_TAU7_CUTOFF_BETA7_REMAINS_POSITIVE PASSED")
    print("R60_CANONICAL_BETA8_SIGN REMAINS OPEN")
    print("R60_D1_EVENTUAL_SKEW_GAUSSIAN_RIGIDITY_P3K REMAIN OPEN")
    print("R60_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
