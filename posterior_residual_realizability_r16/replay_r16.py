"""Exact symbolic replay for the R16 posterior-residual audit."""
from __future__ import annotations

import sympy as sp


def iid_expect(expr, moments):
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    poly = sp.Poly(sp.expand(expr), x1, x2, x3)
    out = 0
    for powers, coeff in poly.terms():
        term = coeff
        for p in powers:
            term *= moments[p]
        out += term
    return sp.expand(out)


def symbols():
    return sp.symbols("V mu3 mu4 mu5 mu6 d q", real=True)


def centered_moments():
    V, mu3, mu4, mu5, mu6, d, q = symbols()
    return {0: sp.Integer(1), 1: sp.Integer(0), 2: V,
            3: mu3, 4: mu4, 5: mu5, 6: mu6}


def cumulant_chain():
    V, mu3, mu4, mu5, mu6, d, q = symbols()
    k4 = mu4 - 3 * V**2
    k5 = mu5 - 10 * V * mu3
    k6 = mu6 - 15 * V * mu4 - 10 * mu3**2 + 30 * V**3
    return {
        "m_prime": V / d,
        "V_prime": mu3 / d,
        "V_second": k4 / d**2,
        "V_third": k5 / d**3,
        "V_fourth": k6 / d**4,
        "kappa6": k6,
        "exact_scale_audit": sp.simplify(d**4 * k6 / d**4 - k6) == 0,
    }


def residual_polynomials():
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    bar = (x1 + x2 + x3) / 3
    Q = x1**2 + x2**2 + x3**2 - (x1 + x2 + x3)**2 / 3
    return bar, sp.expand(Q)


def conditional_q_moments():
    V, mu3, mu4, mu5, mu6, d, q = symbols()
    mom = centered_moments()
    _, Q = residual_polynomials()
    got = {"Q": iid_expect(Q, mom), "Q2": iid_expect(Q**2, mom),
           "Q3": iid_expect(Q**3, mom)}
    expected = {
        "Q": 2 * V,
        "Q2": sp.Rational(4, 3) * (mu4 + 3 * V**2),
        "Q3": sp.Rational(8, 9) * (mu6 + 12 * V * mu4 - 7 * mu3**2 + 3 * V**3),
    }
    return got, expected, {k: sp.simplify(got[k] - expected[k]) == 0 for k in got}


def raw_order_rewrites():
    V, mu3, mu4, mu5, mu6, d, q = symbols()
    e4 = (mu4 - 3 * V**2) / 2 + 3 * (V - d)**2
    e6 = (mu6 - 15 * V * mu4 - 10 * mu3**2 + 30 * V**3) \
        + 27 * (mu4 - 3 * V**2) * (V - d) + 3 * mu3**2 \
        + 54 * (V - d)**3
    e4_expected = (mu4 + 3 * V**2) / 2 - 6 * d * V + 3 * d**2
    e6_expected = mu6 + 12 * V * mu4 - 7 * mu3**2 + 3 * V**3 \
        - 27 * d * (mu4 + 3 * V**2) + 162 * d**2 * V - 54 * d**3
    return {
        "order4": sp.expand(e4), "order4_expected": sp.expand(e4_expected),
        "order4_identity": sp.simplify(e4 - e4_expected) == 0,
        "order6": sp.expand(e6), "order6_expected": sp.expand(e6_expected),
        "order6_identity": sp.simplify(e6 - e6_expected) == 0,
        "order4_expectation_consequence": "E[mu4+3V^2]=6d^2 when E[V]=d",
        "order6_expectation_consequence": "E[mu6+12Vmu4-7mu3^2+3V^3]=54d^3",
    }


def pearson_and_projection():
    V, mu3, mu4, mu5, mu6, d, q = symbols()
    pearson_gap = sp.expand(V * (mu4 - V**2) - mu3**2)
    sixth_gap = sp.factor(mu6 - mu3**2 - mu4**2 / V)
    projected_gap = sp.factor(mu6 + 12 * V * mu4 - 7 * mu3**2 + 3 * V**3
                              - (mu4 + 3 * V**2)**2 / V)
    return {
        "pearson_gap": pearson_gap, "sixth_projection_gap": sixth_gap,
        "projected_order6_gap": projected_gap,
        "pearson_statement": "mu3^2 <= V*(mu4-V^2), with V=0 handled separately",
        "sixth_statement": "mu6 >= mu3^2+mu4^2/V for V>0",
        "projected_order6_statement": "mu6+12Vmu4-7mu3^2+3V^3 >= (mu4+3V^2)^2/V",
    }


def tilted_law_checks():
    q = sp.Rational(1, 3)
    d = 1 - q
    negative_laplace = sp.simplify(1 / (1 + q / d))
    positive_laplace = sp.simplify(1 / (1 - q / d))
    return {
        "d": d, "negative_laplace": negative_laplace,
        "negative_normalized": sp.simplify(negative_laplace / d),
        "positive_normalized": sp.simplify(positive_laplace / d),
        "negative_sign_normalizes": sp.simplify(negative_laplace / d) == 1,
        "positive_sign_normalizes": sp.simplify(positive_laplace / d) == 1,
    }


def conditional_gaussian_completion_check():
    x, q = sp.symbols("x q", positive=True)
    d = 1 - q
    u1, u2, u3 = sp.symbols("u1 u2 u3")
    S = u1 + u2 + u3
    sumsq = u1**2 + u2**2 + u3**2
    Q = sumsq - S**2 / 3
    lhs = -3*x**2 / (2*d) - 3*x**2 / (2*q) + x*S/d - q*sumsq/(2*d)
    rhs = -3*(x - q*S/3)**2/(2*q*d) - q*Q/(2*d)
    return {"completed_square": sp.simplify(lhs - rhs) == 0,
            "residual_exponent": "-q*Q/(2*d)",
            "conditional_mean": "q*(u1+u2+u3)/3",
            "conditional_variance": "q*d/3"}


def two_state_countermodel():
    wA, wB = sp.Rational(8, 9), sp.Rational(1, 9)
    VA, VB = sp.Rational(3, 4), sp.Integer(3)
    EV = wA * VA + wB * VB
    order4 = wA * (VA**2 + 3*VA**2) + wB * (VB**2 + 3*VB**2)
    order6 = wA * (VA**3 + 12*VA**3 + 3*VA**3) \
        + wB * (VB**3 + 12*VB**3 + 3*VB**3)
    variance = sp.simplify(wA * VA**2 + wB * VB**2 - EV**2)
    return {"weight_A": wA, "weight_B": wB, "V_A": VA, "V_B": VB,
            "E_V": EV, "E_order4": order4, "E_order6": order6,
            "variance_of_V": variance, "nonconstant": variance > 0,
            "matches_target": (EV == 1 and order4 == 6 and order6 == 54)}


def fisher_deficit_algebra():
    q, d, var_nu, var_kprime, var_bar = sp.symbols(
        "q d var_nu var_kprime var_bar", positive=True)
    return {"stein": sp.Eq(var_nu, q/3 + q**2*var_kprime),
            "triple": sp.Eq(var_nu, q*d/3 + q**2*var_bar),
            "deduced": sp.Eq(var_bar, sp.Rational(1, 3) + var_kprime)}


def sample_mean_tilt_derivatives():
    m3, m4, m5, m6 = sp.symbols("m3 m4 m5 m6")
    moments = {0: 1, 1: 0, 2: 1, 3: m3, 4: m4, 5: m5, 6: m6}
    bar, Q = residual_polynomials()
    E = lambda p: iid_expect(p, moments)
    Z = 1 - sp.Symbol("t")*E(Q)/2 + sp.Symbol("t")**2*E(Q**2)/8
    A = sp.Symbol("t")*(-E(bar*Q)/2) + sp.Symbol("t")**2*E(bar*Q**2)/8
    B = E(bar**2) - sp.Symbol("t")*E(bar**2*Q)/2 + sp.Symbol("t")**2*E(bar**2*Q**2)/8
    t = sp.Symbol("t")
    W = sp.series(B/Z - (A/Z)**2, t, 0, 3).removeO().expand()
    w1 = sp.simplify(W.coeff(t, 1))
    w2 = sp.simplify(2*W.coeff(t, 2))
    return {"W0": sp.simplify(W.coeff(t, 0)),
            "W_prime_general": w1, "W_second_general": w2,
            "W_prime_under_Q2": sp.simplify(w1.subs(m4, 3)),
            "W_second_under_Q2Q3": sp.simplify(w2.subs({m4: 3, m6: 15 + 7*m3**2})),
            "W_prime_zero": sp.simplify(w1.subs(m4, 3)) == 0,
            "W_second_m3": sp.simplify(w2.subs({m4: 3, m6: 15 + 7*m3**2})) == m3**2/9}


def derivative_translation():
    V, V1, V2, V4, d = sp.symbols("V V1 V2 V4 d")
    mu3 = d*V1
    mu4 = d**2*V2 + 3*V**2
    mu6 = d**4*V4 + 15*V*mu4 + 10*mu3**2 - 30*V**3
    pearson = sp.expand(V*(mu4-V**2)-mu3**2)
    projection = sp.factor(mu6 - mu3**2 - mu4**2/V)
    return {"pearson_derivative_gap": pearson,
            "pearson_derivative_inequality": "d^2(V')^2 <= V*(d^2 V''+2V^2)",
            "sixth_derivative_gap": projection,
            "sixth_derivative_inequality": "d^4V''''+9d^2VV''+9d^2(V')^2+6V^3 >= d^4(V'')^2/V"}
