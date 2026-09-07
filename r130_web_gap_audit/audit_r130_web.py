"""Exact audit of the stronger explicit-gap proof returned by the web task.

The audit uses rational interval arithmetic and exact symbolic reduction only.
It is deliberately separate from the earlier R130 box certificate because the
web proof uses a moving endpoint boundary and an R6-dependent y12 bound.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


Q = Fraction
c, s, a, b, d = sp.symbols("c s a b d", real=True)


def interval_mul(left: tuple[Q, Q], right: tuple[Q, Q]) -> tuple[Q, Q]:
    values = [left[0] * right[0], left[0] * right[1], left[1] * right[0], left[1] * right[1]]
    return min(values), max(values)


def interval_add(left: tuple[Q, Q], right: tuple[Q, Q]) -> tuple[Q, Q]:
    return left[0] + right[0], left[1] + right[1]


def interval_scale(scalar: Q, value: tuple[Q, Q]) -> tuple[Q, Q]:
    if scalar >= 0:
        return scalar * value[0], scalar * value[1]
    return scalar * value[1], scalar * value[0]


def interval_power(value: tuple[Q, Q], exponent: int) -> tuple[Q, Q]:
    result = (Q(1), Q(1))
    for _ in range(exponent):
        result = interval_mul(result, value)
    return result


def polynomial_interval(expr: sp.Expr, bounds: dict[sp.Symbol, tuple[Q, Q]]) -> tuple[Q, Q]:
    variables = (c, a, b, d)
    result = (Q(0), Q(0))
    for powers, coefficient in sp.Poly(sp.expand(expr), *variables).terms():
        scalar = Q(int(coefficient.p), int(coefficient.q))
        term = (Q(1), Q(1))
        for variable, exponent in zip(variables, powers):
            term = interval_mul(term, interval_power(bounds[variable], exponent))
        result = interval_add(result, interval_scale(scalar, term))
    return result


def quotient_interval(numerator: tuple[Q, Q], denominator: tuple[Q, Q]) -> tuple[Q, Q]:
    if denominator[0] <= 0 <= denominator[1]:
        raise ValueError("denominator interval crosses zero")
    values = [
        numerator[0] / denominator[0],
        numerator[0] / denominator[1],
        numerator[1] / denominator[0],
        numerator[1] / denominator[1],
    ]
    return min(values), max(values)


def reduce_in_s(expr: sp.Expr, relation: sp.Expr) -> sp.Expr:
    numerator, denominator = sp.fraction(sp.together(expr))
    remainder = sp.rem(sp.Poly(sp.expand(numerator), s), sp.Poly(relation, s)).as_expr()
    return sp.factor(remainder / denominator)


def check_exact_identities() -> None:
    relation = s**2 - 6 * (2 - c**2) * (1 + c**2)
    u = c**2
    a_plus = 4 * c + s
    b_star = (a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c) / (c**2 - 2)
    r1 = (
        19 * a**2 * c**2 - 102 * a**2 + 2 * a * b
        - 485 * a * c**3 + 1974 * a * c + 53 * b * c**3
        - 132 * b * c + 472 * c**4 - 2820 * c**2 - 720
    ) / (c**2 - 2)
    C = (
        30 * c**8 - 124 * c**6 + 23 * c**5 * s + 3 * c**4
        - 62 * c**3 * s + 516 * c**2 - 40 * c * s - 208
    )
    delta = -18 * C / (c**2 - 2) ** 2
    F = -15 * c**4 + 204 * c**2 - 24 - 18 * (4 - c**2) * c * s
    G = -15 * c**4 + 204 * c**2 - 24 + 18 * (4 - c**2) * c * s
    P = 216 * u**5 - 1919 * u**4 + 4072 * u**3 + 4704 * u**2 - 8000 * u + 64
    N = 2 * a**2 + 18 * a * c**3 - 88 * a * c - 75 * c**4 + 512 * c**2 - 48

    assert reduce_in_s(N.subs(a, a_plus) - F, relation) == 0
    assert reduce_in_s(9 * P - F * G, relation) == 0
    r_plus = r1.subs({a: a_plus, b: b_star.subs(a, a_plus)})
    rhs = F * (3 * (23 * u**2 - 68 * u - 280) + G) / (18 * (u - 4) * (u - 2) ** 2)
    assert reduce_in_s(r_plus - delta - rhs, relation) == 0
    print("R130W_EXACT_F_BOUNDARY_IDENTITY_PASSED")
    print("R130W_EXACT_9P_FG_FACTORISATION_PASSED")
    print("R130W_EXACT_RPLUS_DELTA_IDENTITY_PASSED")


def check_moving_window_constants() -> None:
    # u in [1.1, 1.12].  All square-root statements below are certified by
    # squaring rational endpoints and the signs of the relevant derivatives.
    u_left, u_right = Q(11, 10), Q(28, 25)
    assert u_left >= 1
    assert u_right < 2

    w2 = lambda u: 6 * u * (2 - u) * (1 + u)
    # w^2 is increasing on this interval, and w^2(1.1)>3.5^2,
    # w^2(1.12)<3.6^2.
    assert 12 + 12 * u_right - 18 * u_right**2 > 0
    assert w2(u_left) > Q(7, 2) ** 2
    assert w2(u_right) < Q(18, 5) ** 2
    # s^2=6(2-u)(1+u) is decreasing here.
    assert 6 * (2 - u_right) * (1 + u_right) > Q(167, 50) ** 2
    assert 6 * (2 - u_left) * (1 + u_left) < Q(337, 100) ** 2

    # The polynomial part of C is increasing but remains below 247.
    c0 = 30 * sp.Symbol("u") ** 4 - 124 * sp.Symbol("u") ** 3 + 3 * sp.Symbol("u") ** 2 + 516 * sp.Symbol("u") - 208
    uu = sp.Symbol("u")
    c0 = 30 * uu**4 - 124 * uu**3 + 3 * uu**2 + 516 * uu - 208
    c0_prime = 120 * uu**3 - 372 * uu**2 + 6 * uu + 516
    assert c0_prime.subs(uu, sp.Rational(11, 10)) > 0
    # A direct rational interval lower bound on c0' is positive.
    c0_prime_lower = (
        120 * Q(11, 10) ** 3 - 372 * Q(28, 25) ** 2 + 6 * Q(11, 10) + 516
    )
    assert c0_prime_lower > 0
    assert c0.subs(uu, sp.Rational(28, 25)) < 247

    # K(u)=23u^2-62u-40 is decreasing and K<-80.
    K = 23 * uu**2 - 62 * uu - 40
    assert 46 * u_right - 62 < 0
    assert K.subs(uu, sp.Rational(11, 10)) < -80
    # Thus C < 247 - 80*(7/2) = -33, and t=2-u<0.9.
    assert Q(247) - Q(80) * Q(7, 2) == -33
    assert -18 * Q(-33) / (Q(9, 10) ** 2) > 700
    print("R130W_MOVING_WINDOW_SQRT_BOUNDS_PASSED")
    print("R130W_C_POLYNOMIAL_TIGHT_BOUND_PASSED")
    print("R130W_DELTA_LOWER_BOUND_PASSED")

    # On the same interval F is strictly increasing.  With
    # w^2=6u(2-u)(1+u), h'=12+12u-18u^2 is positive, so
    # F'=204-30u+18w-9(4-u)h'/w.  The rational bounds below give
    # 0<F'<266, which justifies x=-F(u)>=0 for u<=u4 and the mean-value step.
    fp_lower = Q(204) - Q(30) * u_right + Q(18) * Q(7, 2) - Q(9) * Q(29, 10) * Q(7, 2) / Q(7, 2)
    fp_upper = Q(204) - Q(30) * u_left + Q(18) * Q(18, 5)
    assert fp_lower > 0
    assert fp_upper < 266
    print("R130W_F_DERIVATIVE_RANGE_PASSED")


def check_parameter_and_tail_bounds() -> None:
    # If x=-F<=1/2, the web proof gives h<=x/40<=1/80.  The elementary
    # sqrt bounds above imply 7.48<a<7.61; b is then locked by H4.
    bounds = {
        c: (Q(26, 25), Q(53, 50)),
        a: (Q(187, 25), Q(761, 100)),
        b: (Q(67), Q(72)),
        d: (Q(-2000), Q(2000)),
    }
    # The endpoint height E(c)=18c^3-72c+4s is decreasing on
    # [1.04,1.06], and E(1.04)<-40.  Thus -partial_a N>40 for a<=a+.
    assert 54 * Q(106, 100) ** 2 - 72 < 0
    assert 18 * Q(104, 100) ** 3 - 72 * Q(104, 100) + 4 * Q(17, 5) < -40
    # h<=x/40 and x<=1/2 imply the displayed rational a-box.
    assert 4 * Q(104, 100) + Q(167, 50) - Q(1, 80) > Q(748, 100)
    assert 4 * Q(106, 100) + Q(337, 100) == Q(761, 100)
    assert Q(17, 88) * Q(25, 22) < Q(1, 2) ** 2
    print("R130W_H4_LOCAL_MONOTONICITY_AND_LOCKING_CONSTANTS_PASSED")
    b_star = (a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c) / (c**2 - 2)
    # Both derivatives are positive on this rational box.  Their signs are
    # checked before using endpoint monotonicity.
    b_a_num = a * c - 4 * c**2 - 9
    b_c_num = a**2 * c**2 + 2 * a**2 - 68 * a * c - 31 * c**4 + 228 * c**2 + 84
    assert polynomial_interval(b_a_num, bounds)[1] < 0
    assert polynomial_interval(b_c_num, bounds)[1] < 0
    den = polynomial_interval(c**2 - 2, bounds)
    assert den[1] < 0
    b_min = Q(489248, 7175)  # b_*(1.04,7.48)
    b_max = Q(31278223, 438200)  # b_*(1.06,7.61)
    assert b_min > 68
    assert b_max < 72
    assert b_min - Q(1, 4) > 67
    assert b_max + Q(1, 4) < 72
    print("R130W_BSTAR_MONOTONE_BOX_PASSED")
    print(f"R130W_BSTAR_ENDPOINTS = ({b_min}, {b_max})")
    print("R130W_B_POSITIVITY_AND_ABS_BOUND_PASSED")

    # d_* is the H5 compatibility value.  Use the already locked b interval;
    # the natural exact interval is deliberately much wider than needed.
    d_star_num = (
        a**2 * c - a * b * c + 4 * a * c**2 + 24 * a
        + 7 * b * c**2 + 12 * b - 49 * c**5 - 189 * c**3 - 180 * c
    )
    d_star = -d_star_num / (c**2 - 2)
    d_star_interval = quotient_interval(
        interval_scale(Q(-1), polynomial_interval(d_star_num, bounds)), den
    )
    assert d_star_interval[0] > 0
    assert d_star_interval[1] < 1400
    print("R130W_DSTAR_INTERVAL_PASSED")
    print(f"R130W_DSTAR_INTERVAL = {d_star_interval}")

    # B<=25/44 when x<=1/2, and the R125 cap is y10<=4^5*5!.
    assert Q(25, 44) * Q(4) ** 5 * sp.factorial(5) < Q(265) ** 2
    # Both component estimates are strict, so their sum is strict even though
    # the displayed rational endpoints add exactly to 1665.
    assert Q(1400) + Q(265) == Q(1665)
    print("R130W_D_COMPATIBILITY_TAIL_BOUND_PASSED")


def check_r1_and_y12_bounds() -> None:
    bounds = {
        c: (Q(26, 25), Q(53, 50)),
        a: (Q(187, 25), Q(761, 100)),
        b: (Q(67), Q(72)),
        d: (Q(-1665), Q(1665)),
    }
    r1_num = (
        19 * a**2 * c**2 - 102 * a**2 + 2 * a * b
        - 485 * a * c**3 + 1974 * a * c + 53 * b * c**3
        - 132 * b * c + 472 * c**4 - 2820 * c**2 - 720
    )
    r1_interval = quotient_interval(
        polynomial_interval(r1_num, bounds),
        polynomial_interval(c**2 - 2, bounds),
    )
    # The web proof needs only the derivative bounds here; r1 itself is
    # controlled by the exact r_plus-delta identity and |r1-delta|<240x.
    drdb_interval = quotient_interval(
        polynomial_interval(2 * a + 53 * c**3 - 132 * c, bounds),
        polynomial_interval(c**2 - 2, bounds),
    )
    fixed_da_interval = quotient_interval(
        polynomial_interval(38 * a * c**2 - 204 * a - 485 * c**3 + 1974 * c + 2 * b, bounds),
        polynomial_interval(c**2 - 2, bounds),
    )
    dbda_interval = quotient_interval(
        polynomial_interval(2 * (a * c - 4 * c**2 - 9), bounds),
        polynomial_interval(c**2 - 2, bounds),
    )
    drdb_abs = max(abs(drdb_interval[0]), abs(drdb_interval[1]))
    fixed_da_abs = max(abs(fixed_da_interval[0]), abs(fixed_da_interval[1]))
    dbda_abs = max(abs(dbda_interval[0]), abs(dbda_interval[1]))
    print(f"R130W_R1_DERIVATIVE_RAW = {fixed_da_interval}")
    print(f"R130W_BSTAR_DERIVATIVE_RAW = {dbda_interval}")
    print(f"R130W_DRDB_RAW = {drdb_interval}")
    assert max(abs(drdb_interval[0]), abs(drdb_interval[1])) < 250
    assert fixed_da_abs + drdb_abs * dbda_abs < 3000
    print("R130W_R1_DERIVATIVE_BOUNDS_PASSED")
    print(f"R130W_R1_INTERVAL_RAW = {r1_interval}")
    print(f"R130W_DRDB_INTERVAL = {drdb_interval}")
    print("R130W_DA_R1_COMPOSED_BOUND_PASSED")

    # The coefficient multiplying F in the exact r_plus-delta identity
    # simplifies to A/((u-4)(u-2)^2), where
    # A=3u^2-48+(4-u)w.  Rational endpoint bounds give |A|<35 and the
    # denominator absolute value >2, hence the web constant 37 is safe.
    u_left, u_right = Q(11, 10), Q(28, 25)
    A_lower = Q(3) * u_left**2 - Q(48) + (Q(4) - u_right) * Q(7, 2)
    A_upper = Q(3) * u_right**2 - Q(48) + (Q(4) - u_left) * Q(18, 5)
    denominator_abs_lower = (Q(4) - u_right) * (Q(2) - u_right) ** 2
    assert A_lower > -35
    assert A_upper < -33
    assert denominator_abs_lower > 2
    assert Q(35, 2) < 37
    print("R130W_F_COEFFICIENT_BOUND_PASSED")

    # Under x<=1/2: delta>700, h<=x/40, |b-b*|<=x/2, so
    # |r1-delta|<(37+75+125)x<240x and r1>580.
    assert Q(37) + Q(75) + Q(125) < Q(240)
    assert Q(700) - Q(240) * Q(1, 2) == Q(580)
    assert Q(580) ** 2 > Q(25, 44) * Q(453000)
    print("R130W_R1_LOWER_UNDER_SMALL_X_PASSED")

    # With b>0, the negative terms in the exact y12 row can be discarded;
    # use the web proof's deliberately loose bounds.
    y12_upper = (
        Q(10395)
        + Q(14220) * Q(191, 25) * Q(53, 50)
        + Q(252) * Q(191, 25) * Q(78)
        + Q(100) * Q(53, 50) * Q(1665)
    )
    assert y12_upper < Q(453000)
    print("R130W_Y12_R6_UPPER_BOUND_PASSED")
    print(f"R130W_Y12_UPPER = {y12_upper}")


def check_outer_gap() -> None:
    c4_lower = Q(105358, 100000)
    sqrt_11_upper = Q(1049, 1000)
    target = Q(25, 28196)
    assert c4_lower - sqrt_11_upper > target
    # The web proof's mean-value step uses |F'|<266 and c+c4<53/25.
    assert Q(1, 532) / Q(53, 25) == target
    print("R130W_SMALL_U_DIRECT_GAP_PASSED")
    print("R130W_MEAN_VALUE_CONSTANT_PASSED")
    print("R130W_EXPLICIT_GAP_CANDIDATE_AUDIT_COMPLETED")


def main() -> None:
    check_exact_identities()
    check_moving_window_constants()
    check_parameter_and_tail_bounds()
    check_r1_and_y12_bounds()
    check_outer_gap()


if __name__ == "__main__":
    main()
