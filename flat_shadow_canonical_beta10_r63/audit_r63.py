"""R63 exploratory exact audit: canonical degree-20 beta10 sign.

This is deliberately a finite-stage audit.  It extends the R62 canonical
family by the alpha9=0 and degree-20 same-factor constraints, then checks the
resulting moment rows and norm at exact rational points.  No global positivity
or eventual annihilation claim is made here.
"""

import sys
from pathlib import Path

from sympy import Poly, Rational, cancel, factor, factorial, hermite_prob, simplify, solve, sqrt, sympify, symbols


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "flat_shadow_canonical_beta9_r62"))
from audit_r62 import bernstein_coefficients, expectation, family_data, reduce_a  # noqa: E402
sys.path.insert(0, str(ROOT / "flat_shadow_constraint_coupling_r47"))
from audit_r47 import fock_cubic  # noqa: E402


def extended_data(a, t):
    _, _, _, _, _, _, beta, moments = family_data(a, t)
    moments = dict(moments)
    moments[19] = 9 * a * (55917589*t**5 - 184963800*t**4 + 55863471*t**3
                           + 179281750*t**2 + 11558100*t - 16463160) / (2 - t)**3
    moments[20] = (-14571660838*t**6 + 520027461774*t**5 - 2971081076052*t**4
                   + 6147868133237*t**3 - 4337195160894*t**2
                   - 8050748580*t + 5237832600) / (2 - t)**3
    return beta, moments


def build_polynomials(x, beta, a):
    polys = [Poly(1, x), Poly(x, x)]
    for n in range(1, 10):
        alpha = a if n == 1 else (-a if n == 2 else 0)
        polys.append(Poly(x - alpha, x) * polys[n] - beta[n] * polys[n - 1])
    return polys


def exact_rows_and_norms():
    x, a, t = symbols("x a t")
    beta, moments = extended_data(a, t)
    polys = build_polynomials(x, beta, a)
    p9, p10 = polys[9], polys[10]
    m19_rhs = moments[19]

    relation_symbols = {0: 1}
    relation_symbols.update({k: symbols("b" + str(k)) for k in range(1, 21)})
    relation = fock_cubic(20, relation_symbols)

    m20_unknown = symbols("m20_unknown")
    relation_moments = dict(moments)
    relation_moments[20] = m20_unknown
    relation_b = {
        degree: expectation(hermite_prob(degree, x), x, relation_moments)
        / sqrt(factorial(degree))
        for degree in range(1, 21)
    }
    m20_solved = solve(
        relation.subs({relation_symbols[k]: relation_b[k] for k in range(1, 21)}),
        m20_unknown,
    )[0]
    m20_rhs = cancel(reduce_a(m20_solved, a, t))
    assert simplify(m20_rhs - moments[20]) == 0
    moments[20] = m20_rhs
    print("R63_M20_SOLVED", m20_rhs)

    for a_value in (Rational(0), Rational(1, 10), Rational(1, 5)):
        t_value = a_value**2
        point_moments = {
            degree: simplify(sympify(value).subs({a: a_value, t: t_value}))
            for degree, value in moments.items()
        }
        p9_point = p9.as_expr().subs({a: a_value, t: t_value})
        p10_point = p10.as_expr().subs({a: a_value, t: t_value})

        m19_direct = -sum(
            coefficient * point_moments[degree[0]]
            for degree, coefficient in Poly((x * p9_point**2).expand(), x).terms()
            if degree[0] != 19
        )
        assert simplify(m19_direct - m19_rhs.subs({a: a_value, t: t_value})) == 0

        def point_expect(poly):
            return expectation(poly.subs({a: a_value, t: t_value}), x, point_moments)

        b = {
            degree: simplify(point_expect(hermite_prob(degree, x)) / sqrt(factorial(degree)))
            for degree in range(1, 21)
        }
        relation_point = relation.subs({relation_symbols[k]: b[k] for k in range(1, 21)})
        assert simplify(relation_point) == 0

        h9_direct = simplify(point_expect(p9_point**2))
        h10_direct = simplify(point_expect(p10_point**2))
        assert h9_direct == simplify((3 * family_data(a, t)[5] / ((2 - t)**4 * family_data(a, t)[3])).subs({a: a_value, t: t_value}))
        assert simplify(point_moments[20] - m20_rhs.subs({a: a_value, t: t_value})) == 0
        print("R63_DEGREE20_ROW_M19_M20_EXACT_RATIONAL_CHECKS PASSED", a_value)
        print("R63_H10_POINT", a_value, h10_direct)


def symbolic_h10_and_sign():
    x, a, t = symbols("x a t")
    beta, moments = extended_data(a, t)
    polys = build_polynomials(x, beta, a)
    p9, p10 = polys[9], polys[10]
    h10_raw = expectation((p10.as_expr()**2).expand(), x, moments)
    h10 = cancel(reduce_a(h10_raw, a, t))
    _, _, _, p7, p8, q9, _, _ = family_data(a, t)
    h9 = 3 * q9 / ((2 - t)**4 * p7)
    beta10 = cancel(h10 / h9)
    print("R63_H10_FACTOR", h10)
    print("R63_BETA10_FACTOR", beta10)
    print("R63_BETA10_AT_ZERO", simplify(beta10.subs(t, 0)))
    print("R63_BETA10_DERIVATIVE_AT_ZERO", simplify(beta10.diff(t).subs(t, 0)))
    h10_num, h10_den = h10.as_numer_denom()
    num, den = beta10.as_numer_denom()
    assert simplify(h10_den - (t - 2)**5 * p8) == 0
    assert simplify(beta10 - h10_num * p7 / (3 * (t - 2) * p8 * q9)) == 0
    print("R63_BETA10_NUM_DEGREE", Poly(num, t).degree())
    print("R63_BETA10_DEN_SIGN_FACTORS", den)
    print("R63_H10_DEN_FACTOR", factor(h10.as_numer_denom()[1]))
    print("R63_BETA10_DEN_FACTOR", factor(den))
    for point in (Rational(1, 1000), Rational(1, 200), Rational(1, 100),
                  Rational(1, 50), Rational(19, 500)):
        print("R63_H10_SIGN_POINT", point, simplify(h10.subs(t, point) > 0),
              simplify(num.subs(t, point) > 0), simplify(den.subs(t, point) > 0))
    assert all(value > 0 for value in bernstein_coefficients(
        h10_num.diff(t), t, Rational(0), Rational(1, 200), 19))
    sign_segments = (
        (Rational(1, 200), Rational(1, 100)),
        (Rational(1, 100), Rational(3, 200)),
        (Rational(3, 200), Rational(1, 50)),
        (Rational(1, 50), Rational(1, 40)),
        (Rational(1, 40), Rational(19, 500)),
    )
    segment_certificates = [
        all(value > 0 for value in bernstein_coefficients(h10_num, t, left, right, 20))
        for left, right in sign_segments
    ]
    print("R63_H10_NUM_SEGMENT_CERTIFICATES", list(zip(sign_segments, segment_certificates)))
    assert h10_num.subs(t, 0) < 0
    assert h10_num.subs(t, Rational(1, 200)) > 0
    assert all(value < 0 for value in bernstein_coefficients(
        h10_den, t, Rational(0), Rational(19, 500), 17))
    assert all(value < 0 for value in bernstein_coefficients(
        den, t, Rational(0), Rational(1, 100), 29))
    print("R63_H10_NUM_STRICTLY_INCREASING_ON_0_1/200 PASSED")
    assert all(segment_certificates)
    print("R63_H10_NUM_POSITIVE_ON_1/200_1/25 PASSED")
    print("R63_H10_DEN_NEGATIVE_ON_0_19/500 PASSED")
    print("R63_TAU10_IN_0_1/200_AND_TAU10_LT_TAU9 PASSED")
    print("R63_BETA10_SIGN_CONTRACTION_ON_PRIOR_WINDOW PASSED")


if __name__ == "__main__":
    exact_rows_and_norms()
    symbolic_h10_and_sign()
