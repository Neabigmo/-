"""R130 exact rational-box certificate for an explicit M=6 gap.

The certificate uses only exact polynomial interval arithmetic.  It combines
the R127 H4 Schur inequalities with the R129 H5-to-H6 compatibility residual.
No optimizer or floating-point feasibility scan is used.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


Q = Fraction
c, a, b = sp.symbols("c a b", real=True)


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
    result = (Q(0), Q(0))
    variables = (c, a, b)
    for powers, coefficient in sp.Poly(sp.expand(expr), *variables).terms():
        scalar = Q(int(coefficient.p), int(coefficient.q))
        term = (Q(1), Q(1))
        for variable, exponent in zip(variables, powers):
            term = interval_mul(term, interval_power(bounds[variable], exponent))
        result = interval_add(result, interval_scale(scalar, term))
    return result


def quotient_interval(
    numerator: tuple[Q, Q], denominator: tuple[Q, Q]
) -> tuple[Q, Q]:
    if denominator[0] <= 0 <= denominator[1]:
        raise ValueError("denominator interval crosses zero")
    values = [
        numerator[0] / denominator[0],
        numerator[0] / denominator[1],
        numerator[1] / denominator[0],
        numerator[1] / denominator[1],
    ]
    return min(values), max(values)


def exact_rows_symbols() -> tuple[sp.Expr, sp.Expr]:
    y6 = 15 + 7 * c**2
    y8 = 105 - 124 * c**2 + 32 * c * a
    y10 = 3 * (17 * a**2 - 280 * a * c + 20 * b * c + 470 * c**2 + 315)
    y12 = (
        10395 - 16380 * c**2 - 7749 * c**4 + 14220 * a * c
        - 1926 * a**2 - 2160 * b * c + 252 * a * b
        + 100 * c * sp.symbols("d")
    )
    return y10, y12


def check_c4_interval() -> tuple[Q, Q]:
    # Use the wider left endpoint for the R130 feasibility box, but certify
    # the sharper location of the R127 endpoint separately.
    c_left = Q(10535, 10000)
    c4_left = Q(105358, 100000)
    c_right = Q(105359, 100000)
    u = sp.symbols("u", real=True)
    polynomial = sp.Poly(
        216 * u**5 - 1919 * u**4 + 4072 * u**3
        + 4704 * u**2 - 8000 * u + 64,
        u,
    )
    assert polynomial.count_roots(1, 2) == 1
    assert sp.sign(polynomial.eval(sp.Rational(10535, 10000) ** 2)) < 0
    assert sp.sign(polynomial.eval(sp.Rational(105358, 100000) ** 2)) < 0
    assert sp.sign(polynomial.eval(sp.Rational(105359, 100000) ** 2)) > 0
    print("R130_C4_ROOT_INTERVAL_PASSED")
    print("R130_C4_ROOT_INTERVAL = (1.05358, 1.05359)")
    return c_left, c_right


def check_h4_parameter_box(c_left: Q, c_right: Q) -> dict[sp.Symbol, tuple[Q, Q]]:
    a_left = Q(75698, 10000)
    a_right = Q(7571, 1000)
    bounds = {c: (c_left, c_right), a: (a_left, a_right), b: (Q(0), Q(1))}

    d = -a**2 + 8 * a * c - 6 * c**4 - 10 * c**2 + 12
    n = 2 * a**2 + 18 * a * c**3 - 88 * a * c - 75 * c**4 + 512 * c**2 - 48
    assert polynomial_interval(sp.diff(d, a), bounds)[1] < 0
    assert polynomial_interval(sp.diff(d, c), bounds)[0] > 0
    assert polynomial_interval(sp.diff(n, a), bounds)[1] < 0
    assert polynomial_interval(sp.diff(n, c), bounds)[0] > 0

    # D(c,a_right)<0 and N(c,a_left)>0 on the whole c interval.
    d_at_right_max = d.subs({c: sp.Rational(c_right.numerator, c_right.denominator), a: sp.Rational(a_right.numerator, a_right.denominator)})
    n_at_left_min = n.subs({c: sp.Rational(c_left.numerator, c_left.denominator), a: sp.Rational(a_left.numerator, a_left.denominator)})
    assert d_at_right_max < 0
    assert n_at_left_min > 0

    # Hence every H4-PSD point in this c-window has a_left<a<a_right.
    denominator_lower = Q(2) - c_right**2
    d_max = d.subs({c: c_right, a: a_left})
    n_min = n.subs({c: c_left, a: a_right})
    s00_upper = Q(int(d_max.p), int(d_max.q)) / denominator_lower
    s11_upper = -Q(int(n_min.p), int(n_min.q)) / denominator_lower
    assert s00_upper < Q(1, 100)
    assert s11_upper < Q(1, 16)
    print("R130_H4_PARAMETER_BOX_PASSED")
    print(f"R130_S00_UPPER = {s00_upper}")
    print(f"R130_S11_UPPER = {s11_upper}")
    return bounds


def check_b_and_r1(bounds: dict[sp.Symbol, tuple[Q, Q]]) -> tuple[Q, Q]:
    b_star = (
        a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c
    ) / (c**2 - 2)
    b_star_numerator = a**2 * c - 8 * a * c**2 - 18 * a + 31 * c**3 + 42 * c
    b_star_denominator = c**2 - 2
    b_star_interval = quotient_interval(
        polynomial_interval(b_star_numerator, bounds),
        polynomial_interval(b_star_denominator, bounds),
    )
    assert b_star_interval[0] > Q(7029, 100)
    assert b_star_interval[1] < Q(704, 10)
    print("R130_BSTAR_INTERVAL_CERTIFICATE_PASSED")
    print(f"R130_BSTAR_INTERVAL = {b_star_interval}")

    # H4 PSD gives (b-b*)^2 <= S00*S11, hence |b-b*|<1/40.
    b_left = Q(702, 10)
    b_right = Q(141, 2)
    enlarged = {c: bounds[c], a: bounds[a], b: (b_left, b_right)}
    r1_numerator = (
        19 * a**2 * c**2 - 102 * a**2 + 2 * a * b
        - 485 * a * c**3 + 1974 * a * c + 53 * b * c**3
        - 132 * b * c + 472 * c**4 - 2820 * c**2 - 720
    )
    r1_interval = quotient_interval(
        polynomial_interval(r1_numerator, enlarged),
        polynomial_interval(c**2 - 2, enlarged),
    )
    assert r1_interval[0] > Q(800)
    print("R130_R1_LOWER_BOUND_CERTIFICATE_PASSED")
    print(f"R130_R1_INTERVAL = {r1_interval}")
    return b_left, b_right


def check_m6_schur_identities() -> None:
    d, e = sp.symbols("d e", real=True)
    y6 = 15 + 7 * c**2
    y8 = 105 - 124 * c**2 + 32 * c * a
    y10 = 3 * (17 * a**2 - 280 * a * c + 20 * b * c + 470 * c**2 + 315)
    y12 = (
        10395 - 16380 * c**2 - 7749 * c**4 + 14220 * a * c
        - 1926 * a**2 - 2160 * b * c + 252 * a * b + 100 * c * d
    )
    h2 = sp.Matrix([[1, 0, 1], [0, 1, c], [1, c, 3]])
    incoming = sp.Matrix([[c, 3, a, y6], [3, a, y6, b], [a, y6, b, y8]])
    bottom = sp.Matrix([[y6, b, y8, d], [b, y8, d, y10], [y8, d, y10, e], [d, y10, e, y12]])
    schur = sp.simplify(bottom - incoming.T * h2.inv() * incoming)
    n = 2 * a**2 + 18 * a * c**3 - 88 * a * c - 75 * c**4 + 512 * c**2 - 48
    r1_numerator = (
        19 * a**2 * c**2 - 102 * a**2 + 2 * a * b
        - 485 * a * c**3 + 1974 * a * c + 53 * b * c**3
        - 132 * b * c + 472 * c**4 - 2820 * c**2 - 720
    )
    assert sp.simplify(schur[1, 1] + n / (2 - c**2)) == 0
    assert sp.simplify(schur[1, 3] - r1_numerator / (c**2 - 2)) == 0
    # The last Schur diagonal is y12 minus a PSD quadratic form whenever H2>0.
    incoming_last = incoming[:, 3]
    last_expected = y12 - (incoming_last.T * h2.inv() * incoming_last)[0]
    assert sp.simplify(schur[3, 3] - last_expected) == 0
    print("R130_M6_SCHUR_IDENTITIES_PASSED")


def check_m6_psd_contradiction(bounds: dict[sp.Symbol, tuple[Q, Q]]) -> None:
    # For c in this interval, A=H2 is positive definite.  The H6 Schur
    # complement S relative to A has S13=r1 and S11=-N/(2-c^2).
    # PSD therefore gives r1^2 <= S11*S33.  Since S33<=y12 and the T6 cap
    # is y12<=4^6*6!, the rational bounds contradict r1>800 and S11<1/16.
    left = Q(800) ** 2
    right = Q(1, 16) * (Q(4) ** 6) * sp.factorial(6)
    assert left > Q(int(right.p), int(right.q))
    print("R130_M6_SCHUR_2X2_CONTRADICTION_PASSED")
    print("R130_M6_EXPLICIT_RELAXED_RADIUS_UPPER_BOUND = 1.0535")
    print("R130_M6_EXPLICIT_GAP_CERTIFICATE_PASSED")


def main() -> None:
    c_left, c_right = check_c4_interval()
    bounds = check_h4_parameter_box(c_left, c_right)
    check_b_and_r1(bounds)
    check_m6_schur_identities()
    check_m6_psd_contradiction(bounds)
    print("R130_M6_EXPLICIT_GAP_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
