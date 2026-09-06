"""R48 exact audit: heat-lift null defects and the moving-rank threshold.

This audit checks the finite identities extracted from the webpage R48
analysis.  It deliberately stops short of claiming the open statement
Xi_K -> infinity or a genuine all-degree counterexample.  The three layers
remain separate: a positive full law, its formal inverse-heat moments, and
the rank-two positive flat shadow used only to define the test polynomial.
"""

from functools import lru_cache

from sympy import (
    I,
    Poly,
    Rational,
    diff,
    expand,
    factorial,
    simplify,
    sqrt,
    symbols,
)


def hermite_prob(n, x):
    return sum(
        (-1) ** k
        * factorial(n)
        * x ** (n - 2 * k)
        / (2**k * factorial(k) * factorial(n - 2 * k))
        for k in range(n // 2 + 1)
    )


def reduce_relation(expr, variable, relation):
    """Reduce a polynomial modulo one quadratic algebraic relation."""
    polynomial = Poly(expand(expr), variable, domain="EX")
    divisor = Poly(relation, variable, domain="EX")
    return simplify(polynomial.rem(divisor).as_expr())


def monomial_hermite_difference(power, deltas, variance, x):
    """Return the difference of inverse moments of x**power.

    We use the variance-`variance` Hermite basis:
    x**p = p! * sum_k variance**k H_(p-2k)
    /(2**k k! (p-2k)!).
    The normalized Hermite-coordinate difference is sqrt(j!)*Delta_j.
    """
    out = 0
    for k in range(power // 2 + 1):
        degree = power - 2 * k
        coefficient = factorial(power) / (
            2**k * factorial(k) * factorial(degree)
        )
        out += (
            coefficient
            * variance**k
            * sqrt(factorial(degree))
            * deltas.get(degree, 0)
        )
    return simplify(out)


def two_atom_moments(max_degree, t):
    moments = [0] * (max_degree + 1)
    moments[0] = 1
    if max_degree >= 1:
        moments[1] = 0
    for k in range(max_degree - 1):
        moments[k + 2] = simplify(t * moments[k + 1] + moments[k])
    return moments


def moment_expectation(polynomial, variable, moments):
    out = 0
    for (power,), coefficient in Poly(expand(polynomial), variable).terms():
        out += coefficient * moments[power]
    return simplify(out)


@lru_cache(maxsize=None)
def angular_coefficient(pattern):
    """Three-direction constant term, including the (2/3)^(d/2) factor."""
    degree = sum(pattern)
    x = symbols("x")
    omega = -Rational(1, 2) - sqrt(3) * I / 2
    phases = (1, omega, omega**2)
    inverse_phases = (1, omega**2, omega)
    polynomial = 1
    for exponent, phase, inverse_phase in zip(
        pattern, phases, inverse_phases
    ):
        polynomial *= (phase * x + inverse_phase / x) ** exponent / 2**exponent
    polynomial = expand(polynomial * x**degree)
    average = Poly(polynomial, x).coeff_monomial(x**degree)
    return simplify(Rational(2, 3) ** (degree // 2) * average)


def fock_cubic(degree, coefficients):
    out = 0
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            k = degree - i - j
            value = (
                coefficients.get(i, 0)
                * coefficients.get(j, 0)
                * coefficients.get(k, 0)
            )
            if value == 0:
                continue
            multiplicity = factorial(degree) / (
                factorial(i) * factorial(j) * factorial(k)
            )
            out += sqrt(multiplicity) * angular_coefficient((i, j, k)) * value
    return simplify(out)


def heat_lift(polynomial, variable, delta):
    """Apply exp(delta*d^2/2) to a polynomial exactly."""
    degree = Poly(expand(polynomial), variable).degree()
    out = 0
    for j in range(degree // 2 + 1):
        out += delta**j / (2**j * factorial(j)) * diff(polynomial, variable, 2 * j)
    return expand(out)


def null_defect_rows():
    v, c = symbols("v c")
    d6, d7, d8, d9 = symbols("Delta6 Delta7 Delta8 Delta9")
    x = symbols("x")
    deltas = {6: d6, 7: d7, 8: d8, 9: d9}
    # On the rank-two branch c**2=2*v, so the x**2 coefficient in P**2
    # vanishes.  Use that reduced polynomial explicitly in the row audit.
    P2 = expand(x**4 - 2 * c * x**3 + 2 * c * v * x + v**2)

    def r(k):
        return simplify(
            sum(
                coefficient * monomial_hermite_difference(
                    power, deltas, v, x
                )
                for (power,), coefficient in Poly(
                    expand(x**k * P2), x
                ).terms()
            )
        )

    expected = {
        0: 0,
        1: 0,
        2: sqrt(factorial(6)) * d6,
        3: sqrt(factorial(7)) * d7 - 2 * c * sqrt(factorial(6)) * d6,
        4: (
            sqrt(factorial(8)) * d8
            - 2 * c * sqrt(factorial(7)) * d7
            + 28 * v * sqrt(factorial(6)) * d6
        ),
        5: (
            sqrt(factorial(9)) * d9
            - 2 * c * sqrt(factorial(8)) * d8
            + 36 * v * sqrt(factorial(7)) * d7
            - 54 * c * v * sqrt(factorial(6)) * d6
        ),
    }
    for degree, value in expected.items():
        assert simplify(r(degree) - value) == 0

    # The two displayed defect coordinates are just triangular rearrangements.
    assert simplify(sqrt(factorial(7)) * d7 - (r(3) + 2 * c * r(2))) == 0
    assert reduce_relation(
        sqrt(factorial(9)) * d9
        - (r(5) + 2 * c * r(4) - 28 * v * r(3) - 58 * c * v * r(2)),
        c,
        c**2 - 2 * v,
    ) == 0
    print("R48_NULL_DEFECT_HIERARCHY PASSED")
    return r, (v, c, d6, d7, d8, d9, x, P2)


def degree_eight_shadow_and_flat_block():
    b3, b5, b8 = symbols("b3 b5 b8")
    relation = fock_cubic(8, {0: 1, 3: b3, 5: b5, 8: b8})
    b8_formula = Rational(8, 7) * sqrt(14) * b3 * b5
    assert simplify(relation.subs(b8, b8_formula)) == 0

    w, t = symbols("w t", positive=True)
    v = w**2
    u = symbols("u")
    moments = two_atom_moments(8, t)
    heads = {
        j: simplify(
            w**j
            * moment_expectation(hermite_prob(j, u), u, moments)
            / sqrt(factorial(j))
        )
        for j in (3, 5, 6, 8)
    }
    heads = {j: reduce_relation(value, t, t**2 - 2) for j, value in heads.items()}
    b3_shadow, b5_shadow, b8_shadow = heads[3], heads[5], heads[8]
    b8_full = b8_formula.subs({b3: b3_shadow, b5: b5_shadow})
    delta8 = reduce_relation(
        b8_full - b8_shadow, t, t**2 - 2
    )
    assert reduce_relation(
        delta8 + Rational(9, 35) * sqrt(70) * w**8,
        t,
        t**2 - 2,
    ) == 0

    # The same inputs force the two scalar defect rows used by the shifted
    # inverse-null block.
    c = t * w
    delta6 = reduce_relation(
        Rational(7, 10) * sqrt(5) * b3_shadow**2 - heads[6],
        t,
        t**2 - 2,
    )
    d7 = symbols("Delta7")
    r2 = sqrt(factorial(6)) * delta6
    r3 = sqrt(factorial(7)) * d7 - 2 * c * r2
    r4 = (
        sqrt(factorial(8)) * delta8
        - 2 * c * sqrt(factorial(7)) * d7
        + 28 * v * r2
    )
    assert reduce_relation(r2 - 18 * w**6, t, t**2 - 2) == 0
    assert reduce_relation(r4 - (-72 * w**8 - 2 * c * r3), t, t**2 - 2) == 0
    print("R48_DEGREE8_BRANCH_IDENTITY PASSED")
    return heads


def flat_shifted_determinant():
    v, c, r3 = symbols("v c r3", positive=True)
    r2 = 18 * v**3
    r4 = -72 * v**4 - 2 * c * r3
    determinant = expand(r2 * r4 - r3**2)
    completed = -(r3 + 18 * c * v**3) ** 2 - 648 * v**7
    assert reduce_relation(determinant - completed, c, c**2 - 2 * v) == 0
    assert reduce_relation(determinant, c, c**2 - 2 * v) != 0
    print("R48_SHIFTED_NULL_HANKEL_STRICTLY_INDEFINITE PASSED")


def interior_shift_formulas():
    # Use the shadow inverse moments plus Hermite-coordinate defects.  This
    # independently reconstructs L_s = L_a exp(delta*d^2/2) on the three
    # test polynomials, rather than assuming the displayed formulas.
    w, t, delta, r3 = symbols("w t delta r3", positive=True)
    v = w**2
    c = t * w
    x = symbols("x")
    u = symbols("u")
    shadow_moments = two_atom_moments(10, t)

    d6 = Rational(3, 10) * sqrt(5) * w**6
    d7 = (r3 + 2 * c * sqrt(factorial(6)) * d6) / sqrt(factorial(7))
    r4 = -72 * w**8 - 2 * c * r3
    d8 = (
        r4
        + 2 * c * sqrt(factorial(7)) * d7
        - 28 * v * sqrt(factorial(6)) * d6
    ) / sqrt(factorial(8))
    deltas = {6: d6, 7: d7, 8: d8}

    def inverse_moment(power):
        baseline = w**power * shadow_moments[power]
        correction = monomial_hermite_difference(power, deltas, v, x)
        return baseline + correction

    def inverse_expectation(polynomial):
        return simplify(
            sum(
                coefficient * inverse_moment(power)
                for (power,), coefficient in Poly(
                    expand(polynomial), x
                ).terms()
            )
        )

    P = x**2 - c * x - v
    expected = {
        2: 3 * (delta + 3 * v) * (5 * delta**2 + 2 * v**2),
        3: r3 + c * (-30 * delta**3 + 21 * delta**2 * v + 6 * delta * v**2),
        4: (
            -2 * c * r3
            + 105 * delta**4
            + 420 * delta**3 * v
            + 213 * delta**2 * v**2
            + 522 * delta * v**3
            - 72 * v**4
        ),
    }
    for degree, value in expected.items():
        computed = inverse_expectation(heat_lift(x**degree * P**2, x, delta))
        difference = reduce_relation(computed - value, t, t**2 - 2)
        assert simplify(difference) == 0
    print("R48_INTERIOR_HEAT_LIFT_FORMULAS PASSED")


def completed_square_and_threshold():
    x, R, t, w = symbols("x R t w", positive=True)
    A = 30 * x**3 - 132 * x**2 - 24 * x - 36
    f = 35 * x**4 + 110 * x**3 + 129 * x**2 + 186 * x - 12
    assert diff(f, x) == 140 * x**3 + 330 * x**2 + 258 * x + 186
    assert f.subs(x, Rational(3, 50)) < 0
    assert f.subs(x, Rational(1, 16)) > 0

    # Reconstruct the determinant from the three interior formulas, then
    # normalize by v^7=w^14.  This is the displayed completed square, checked
    # in the quadratic field t^2=2 rather than asserted tautologically.
    v = w**2
    c = t * w
    delta = x * w**2
    r3 = R * w**7
    l2 = 3 * (delta + 3 * v) * (5 * delta**2 + 2 * v**2)
    l3 = r3 + c * (-30 * delta**3 + 21 * delta**2 * v + 6 * delta * v**2)
    l4 = (
        -2 * c * r3
        + 105 * delta**4
        + 420 * delta**3 * v
        + 213 * delta**2 * v**2
        + 522 * delta * v**3
        - 72 * v**4
    )
    normalized_determinant = expand((l2 * l4 - l3**2) / w**14)
    completed = -(R - t * A / 2) ** 2 + 9 * (x + 3) * (5 * x**2 + 2) * f
    assert reduce_relation(
        normalized_determinant - completed, t, t**2 - 2
    ) == 0

    # At fixed x, the square can be cancelled by choosing R=t*A/2.  Thus the
    # scalar K=1 feasibility threshold is exactly the unique nonnegative root
    # of f, while the divergence of Xi_K is not asserted here.
    print("R48_COMPLETED_SQUARE_THRESHOLD_BRACKET PASSED")
    print("R48_XI1_SCALAR_THRESHOLD RECORDED")


def ou_scaling():
    u = symbols("u", positive=True)
    v, c, r3 = symbols("v c r3")
    d6, d7, d8, d9 = symbols("d6 d7 d8 d9")
    r = {
        2: sqrt(factorial(6)) * d6,
        3: sqrt(factorial(7)) * d7 - 2 * c * sqrt(factorial(6)) * d6,
        4: (
            sqrt(factorial(8)) * d8
            - 2 * c * sqrt(factorial(7)) * d7
            + 28 * v * sqrt(factorial(6)) * d6
        ),
        5: (
            sqrt(factorial(9)) * d9
            - 2 * c * sqrt(factorial(8)) * d8
            + 36 * v * sqrt(factorial(7)) * d7
            - 54 * c * v * sqrt(factorial(6)) * d6
        ),
    }
    scaled = {
        2: u**2 * d6,
        3: u**3 * d7,
        4: u**4 * d8,
        5: u**5 * d9,
    }
    for degree, value in r.items():
        transformed = value.subs(
            {
                v: u**2 * v,
                c: u * c,
                d6: u**6 * d6,
                d7: u**7 * d7,
                d8: u**8 * d8,
                d9: u**9 * d9,
            },
            simultaneous=True,
        )
        assert simplify(transformed - u ** (degree + 4) * value) == 0
    print("R48_OU_NULL_DEFECT_SCALING PASSED")


def main():
    null_defect_rows()
    degree_eight_shadow_and_flat_block()
    flat_shifted_determinant()
    interior_shift_formulas()
    completed_square_and_threshold()
    ou_scaling()
    print("R48_LIFTED_NULL_THRESHOLD_DIVERGENCE REMAINS OPEN")
    print("R48_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
