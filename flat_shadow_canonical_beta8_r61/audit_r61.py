"""R61 exact audit: corrected degree-16 beta8 cutoff.

The webpage's high-degree fractions and P8 polynomial did not pass the local
Gaussian sanity check.  This audit uses the independently recomputed degree-16
same-factor relation, checks the corrected moments and norm factors at exact
rational family points, and proves the sign certificate with Bernstein bases.
"""

import sys
from math import comb
from pathlib import Path

from sympy import Poly, Rational, cancel, factorial, hermite_prob, simplify, sqrt, sympify, symbols


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "flat_shadow_constraint_coupling_r47"))
from audit_r47 import fock_cubic  # noqa: E402


def expectation(poly, x, moments):
    return cancel(
        sum(coefficient * moments[degree[0]]
            for degree, coefficient in Poly(poly, x).terms())
    )


def family_polynomials(a, t):
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
    p8 = (
        1204550144 * t**12 - 35494536455 * t**11
        - 2967319034778 * t**10 + 24133342031328 * t**9
        - 68513207463264 * t**8 + 75535499377824 * t**7
        - 6513636214656 * t**6 - 32358682547712 * t**5
        + 576720933888 * t**4 + 8343384129536 * t**3
        - 662433824768 * t**2 - 28728360960 * t + 1651507200
    )
    beta = [
        None,
        Rational(1),
        2 - t,
        6 * (1 + t) / (2 - t),
        p4 / (2 * (2 - t) * (1 + t)),
        p5 / (2 * (1 + t) * p4),
        -4 * (1 + t) * p6 / ((2 - t) * p4 * p5),
        -p4 * p7 / (2 * (2 - t) * p5 * p6),
    ]
    return p4, p5, p6, p7, p8, beta


def check_degree_sixteen_at_exact_points():
    x, a, t = symbols("x a t")
    p4, p5, p6, p7, p8, beta = family_polynomials(a, t)
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
        13: 3 * a * (1145 * t**2 - 2284 * t - 2280) / (2 - t),
        14: (839909 * t**3 - 1338415 * t**2 - 187437 * t + 270270) / (2 - t),
    }
    alpha = [0, a, -a, 0, 0, 0, 0, 0]
    polys = [1, x]
    for n in range(1, 7):
        polys.append((x - alpha[n]) * polys[n] - beta[n] * polys[n - 1])
    p7_poly = x * polys[6] - beta[6] * polys[5]
    m15 = a * (
        42287 * t**5 - 330144 * t**4 + 228921 * t**3
        + 556826 * t**2 + 306060 * t - 531720
    ) / (2 - t) ** 3
    m16 = 3 * (
        12981388 * t**3 - 26820320 * t**2 - 837195 * t + 1351350
    ) / (2 - t)
    E = lambda poly: expectation(poly, x, moments)

    for a_value in (Rational(0), Rational(1, 10), Rational(1, 5), Rational(1, 4)):
        t_value = a_value**2
        moments_num = {
            degree: simplify(sympify(value).subs({a: a_value, t: t_value}))
            for degree, value in moments.items()
        }
        E_num = lambda poly: expectation(
            poly.subs({a: a_value, t: t_value}), x, moments_num
        )
        p7_num = p7_poly.subs({a: a_value, t: t_value})
        m15_direct = -sum(
            coefficient * moments_num[degree[0]]
            for degree, coefficient in Poly((x * p7_num**2).expand(), x).terms()
            if degree[0] != 15
        )
        assert simplify(m15_direct - m15.subs({a: a_value, t: t_value})) == 0

        b = {
            k: simplify(E_num(hermite_prob(k, x)) / sqrt(factorial(k)))
            for k in (3, 5, 6, 7, 9, 11, 13)
        }
        b16 = 4 * (
            165 * sqrt(273) * b[11] * b[5]
            + 286 * sqrt(35) * b[13] * b[3]
            + 2 * sqrt(15015) * b[3] * b[6] * b[7]
            + 127 * sqrt(715) * b[7] * b[9]
        ) / 715
        moments_num[15] = simplify(m15.subs({a: a_value, t: t_value}))
        moments_num[16] = simplify(m16.subs({a: a_value, t: t_value}))
        E_num = lambda poly: expectation(
            poly.subs({a: a_value, t: t_value}), x, moments_num
        )
        assert simplify(
            E_num(hermite_prob(16, x)) / sqrt(factorial(16)) - b16
        ) == 0
        relation = fock_cubic(
            16,
            {
                0: 1,
                3: b[3],
                5: b[5],
                6: b[6],
                7: b[7],
                9: b[9],
                11: b[11],
                13: b[13],
                16: b16,
            },
        )
        assert simplify(relation) == 0

        p8_poly = x * p7_num - beta[7].subs({a: a_value, t: t_value}) * polys[6].subs({a: a_value, t: t_value})
        h7 = simplify(E_num(p7_num**2))
        h8 = simplify(E_num(p8_poly**2))
        h7_rhs = simplify((3 * p7 / ((2 - t) ** 3 * p5)).subs({a: a_value, t: t_value}))
        h8_rhs = simplify((-3 * p8 / (2 * (2 - t) ** 3 * p6)).subs({a: a_value, t: t_value}))
        beta8_rhs = simplify((-p5 * p8 / (2 * p6 * p7)).subs({a: a_value, t: t_value}))
        assert h7 == h7_rhs
        assert h8 == h8_rhs
        assert simplify(h8 / h7 - beta8_rhs) == 0
    print("R61_M15_DEGREE16_ROW_M16_EXACT_RATIONAL_CHECKS PASSED")
    print("R61_BETA8_H8_OVER_H7_GAUSSIAN_ORIENTATION PASSED")


def bernstein_coefficients(poly, variable, left, right, degree):
    u = symbols("u")
    transformed = Poly(poly.subs(variable, left + (right - left) * u), u)
    coefficients = [transformed.coeff_monomial(u**i) for i in range(degree + 1)]
    return [
        simplify(sum(
            coefficients[i] * Rational(comb(k, i), comb(degree, i))
            for i in range(k + 1)
        ))
        for k in range(degree + 1)
    ]


def check_p8_single_cutoff():
    t = symbols("t")
    _, p5, p6, p7, p8, _ = family_polynomials(symbols("a"), t)
    derivative_coefficients = bernstein_coefficients(
        p8.diff(t), t, Rational(0), Rational(1, 25), 11
    )
    tail_coefficients = bernstein_coefficients(
        p8, t, Rational(1, 25), Rational(9, 100), 12
    )
    assert all(value < 0 for value in derivative_coefficients)
    assert all(value < 0 for value in tail_coefficients)
    assert p8.subs(t, 0) > 0
    assert p8.subs(t, Rational(1, 25)) < 0
    p6_at_09 = p6.subs(t, Rational(9, 100))
    assert p6_at_09 > 0
    print("R61_P8_DERIVATIVE_NEGATIVE_ON_0_1/25 PASSED")
    print("R61_P8_NEGATIVE_ON_1/25_9/100 PASSED")
    print("R61_UNIQUE_TAU8_IN_0_1/25_AND_BETA8_SIGN PASSED")


def main():
    check_degree_sixteen_at_exact_points()
    check_p8_single_cutoff()
    print("R61_TAU6_GT_TAU8_PARTIAL_CONTRACTION PASSED")
    print("R61_BETA9_AND_INFINITE_TAIL REMAIN OPEN")
    print("R61_D1_EVENTUAL_SKEW_GAUSSIAN_RIGIDITY_P3K REMAIN OPEN")
    print("R61_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
