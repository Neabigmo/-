"""R62 exact audit: corrected degree-18 beta9 cutoff.

The audit checks the degree-18 same-factor row at exact rational family
points, the alpha8=0 odd row, the corrected h8/h9/beta9 orientation, and
the Bernstein sign certificates for the new Q9 cutoff.  It intentionally
keeps the statement finite-stage and does not claim full positive viability.
"""

import sys
from math import comb
from pathlib import Path

from sympy import Poly, Rational, cancel, factorial, hermite_prob, simplify, sqrt, sympify, symbols


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "flat_shadow_constraint_coupling_r47"))
from audit_r47 import fock_cubic  # noqa: E402


def reduce_a(expr, a, t):
    """Reduce powers of a using a^2=t, retaining the odd a factor."""
    out = 0
    for (power,), coefficient in Poly(expr.expand(), a).terms():
        out += coefficient * (a * t ** ((power - 1) // 2) if power % 2 else t ** (power // 2))
    return cancel(out)


def expectation(poly, x, moments):
    return cancel(sum(coefficient * moments[degree[0]]
                      for degree, coefficient in Poly(poly, x).terms()))


def family_data(a, t):
    p4 = t**2 - 64*t + 16
    p5 = 253*t**3 - 1278*t**2 + 816*t + 160
    p6 = (532*t**6 - 45655*t**5 + 351508*t**4 - 625952*t**3
          + 110432*t**2 + 83200*t - 7680)
    p7 = (2150400 + 19281920*t - 206264064*t**2 - 424134656*t**3
          + 2523473440*t**4 - 4074599496*t**5 + 2790646820*t**6
          - 853051174*t**7 + 100963863*t**8 - 2264192*t**9)
    p8 = (1204550144*t**12 - 35494536455*t**11 - 2967319034778*t**10
          + 24133342031328*t**9 - 68513207463264*t**8
          + 75535499377824*t**7 - 6513636214656*t**6
          - 32358682547712*t**5 + 576720933888*t**4
          + 8343384129536*t**3 - 662433824768*t**2
          - 28728360960*t + 1651507200)
    q9 = (3165494381056*t**16 + 30325981442862714*t**15
          - 374454388483999229*t**14 + 1980117276228617592*t**13
          - 5948703596679826184*t**12 + 11525374336730958528*t**11
          - 15614218470552621360*t**10 + 14603518104424932288*t**9
          - 6281195243972625024*t**8 - 4538141298321788672*t**7
          + 7271911315244371968*t**6 - 2538108384598913024*t**5
          - 76181770793263104*t**4 - 23999642267549696*t**3
          - 2927350178119680*t**2 + 45013480243200*t
          + 4161798144000)
    beta = [
        None,
        Rational(1),
        2 - t,
        6 * (1 + t) / (2 - t),
        p4 / (2 * (2 - t) * (1 + t)),
        p5 / (2 * (1 + t) * p4),
        -4 * (1 + t) * p6 / ((2 - t) * p4 * p5),
        -p4 * p7 / (2 * (2 - t) * p5 * p6),
        -p5 * p8 / (2 * p6 * p7),
        -2 * p6 * q9 / ((2 - t) * p7 * p8),
    ]
    moments = {
        0: 1, 1: 0, 2: 1, 3: a, 4: 3, 5: 4*a,
        6: 15 + 7*t, 7: 15*a, 8: 105 + 4*t,
        9: a*(96 - 112*t - 49*t**2)/(2 - t),
        10: 945 - 234*t,
        11: a*(140*t**2 - 913*t - 30)/(2 - t),
        12: (2849*t**3 - 19102*t**2 - 15987*t + 20790)/(2 - t),
        13: 3*a*(1145*t**2 - 2284*t - 2280)/(2 - t),
        14: (839909*t**3 - 1338415*t**2 - 187437*t + 270270)/(2 - t),
        15: a*(42287*t**5 - 330144*t**4 + 228921*t**3
               + 556826*t**2 + 306060*t - 531720)/(2 - t)**3,
        16: 3*(12981388*t**3 - 26820320*t**2 - 837195*t + 1351350)/(2 - t),
        17: 2*a*(5799325*t**5 - 17049855*t**4 + 3925920*t**3
                 + 13603108*t**2 + 3127296*t - 4435200)/(2 - t)**3,
        18: (2948477*t**6 + 1914655626*t**5 - 11976383460*t**4
             + 24318362039*t**3 - 15915490026*t**2
             - 432574380*t + 275675400)/(2 - t)**3,
    }
    return p4, p5, p6, p7, p8, q9, beta, moments


def build_polynomials(x, beta, a):
    alpha = [None, a, -a, 0, 0, 0, 0, 0, 0]
    polys = [Poly(1, x), Poly(x, x)]
    for n in range(1, 8):
        polys.append(Poly(x - alpha[n], x) * polys[n] - beta[n] * polys[n - 1])
    p8 = Poly(x, x) * polys[7] - beta[7] * polys[6]
    p9 = Poly(x, x) * p8 - beta[8] * polys[7]
    return polys, p8, p9


def check_exact_rows_and_norms():
    x, a, t = symbols("x a t")
    p4, p5, p6, p7, p8, q9, beta, moments = family_data(a, t)
    polys, p8_poly, p9_poly = build_polynomials(x, beta, a)
    h8_rhs = -3*p8 / (2*(2 - t)**3*p6)
    h9_rhs = 3*q9 / ((2 - t)**4*p7)
    m17_rhs = moments[17]
    m18_rhs = moments[18]

    relation = fock_cubic(18, {
        0: 1,
        3: symbols("b3"), 5: symbols("b5"), 6: symbols("b6"),
        7: symbols("b7"), 9: symbols("b9"), 11: symbols("b11"),
        13: symbols("b13"), 15: symbols("b15"), 18: symbols("b18"),
    })

    for a_value in (Rational(0), Rational(1, 10), Rational(1, 5)):
        t_value = a_value**2
        point_moments = {
            degree: simplify(sympify(value).subs({a: a_value, t: t_value}))
            for degree, value in moments.items()
        }
        point_E = lambda poly: expectation(
            poly.subs({a: a_value, t: t_value}), x, point_moments
        )
        p8_point = p8_poly.subs({a: a_value, t: t_value})
        p9_point = p9_poly.subs({a: a_value, t: t_value})

        m17_direct = -sum(
            coefficient * point_moments[degree[0]]
            for degree, coefficient in Poly((x*p8_point**2).expand(), x).terms()
            if degree[0] != 17
        )
        assert simplify(m17_direct - m17_rhs.subs({a: a_value, t: t_value})) == 0

        b = {
            degree: simplify(point_E(hermite_prob(degree, x)) / sqrt(factorial(degree)))
            for degree in (3, 5, 6, 7, 9, 11, 13, 15, 18)
        }
        relation_point = relation.subs({
            symbols("b3"): b[3], symbols("b5"): b[5], symbols("b6"): b[6],
            symbols("b7"): b[7], symbols("b9"): b[9], symbols("b11"): b[11],
            symbols("b13"): b[13], symbols("b15"): b[15], symbols("b18"): b[18],
        })
        assert simplify(relation_point) == 0

        h8_direct = simplify(point_E(p8_point**2))
        h9_direct = simplify(point_E(p9_point**2))
        assert h8_direct == simplify(h8_rhs.subs({a: a_value, t: t_value}))
        assert h9_direct == simplify(h9_rhs.subs({a: a_value, t: t_value}))
        assert simplify(h9_direct/h8_direct - beta[9].subs({a: a_value, t: t_value})) == 0
        assert simplify(point_moments[18] - m18_rhs.subs({a: a_value, t: t_value})) == 0
    print("R62_DEGREE18_ROW_M17_M18_EXACT_RATIONAL_CHECKS PASSED")
    print("R62_BETA9_H9_OVER_H8_GAUSSIAN_ORIENTATION PASSED")


def bernstein_coefficients(poly, variable, left, right, degree):
    u = symbols("u")
    transformed = Poly(poly.subs(variable, left + (right - left)*u).expand(), u)
    coefficients = [transformed.coeff_monomial(u**i) for i in range(degree + 1)]
    return [
        cancel(sum(coefficients[i] * Rational(comb(k, i), comb(degree, i))
                   for i in range(k + 1)))
        for k in range(degree + 1)
    ]


def check_q9_cutoff():
    t = symbols("t")
    _, _, p6, p7, p8, q9, _, _ = family_data(symbols("a"), t)
    q9_left = bernstein_coefficients(q9, t, Rational(0), Rational(1, 100), 16)
    q9_derivative = bernstein_coefficients(q9.diff(t), t, Rational(1, 100), Rational(1, 25), 15)
    p8_derivative = bernstein_coefficients(p8.diff(t), t, Rational(0), Rational(1, 25), 11)
    assert all(value > 0 for value in q9_left)
    assert all(value < 0 for value in q9_derivative)
    assert all(value < 0 for value in p8_derivative)
    assert q9.subs(t, Rational(1, 100)) > 0
    assert q9.subs(t, Rational(19, 500)) < 0
    assert q9.subs(t, Rational(1, 25)) < 0
    assert p8.subs(t, Rational(19, 500)) > 0
    assert p8.subs(t, Rational(1, 25)) < 0
    assert p6.subs(t, Rational(1, 25)) < 0
    assert all(value > 0 for value in bernstein_coefficients(p7, t, Rational(0), Rational(1, 25), 9))
    print("R62_Q9_POSITIVE_ON_0_1/100 PASSED")
    print("R62_Q9_DERIVATIVE_NEGATIVE_ON_1/100_1/25 PASSED")
    print("R62_TAU9_IN_1/100_19/500_AND_TAU8_GT_19/500 PASSED")
    print("R62_BETA9_SIGN_CONTRACTION PASSED")


def main():
    check_exact_rows_and_norms()
    check_q9_cutoff()
    print("R62_TAU6_GT_TAU8_GT_TAU9_POSITIVE_PARTIAL_PATTERN PASSED")
    print("R62_INFINITE_TAIL_D1_GAUSSIAN_RIGIDITY_P3K REMAIN OPEN")
    print("R62_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
