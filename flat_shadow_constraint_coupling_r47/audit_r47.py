"""R47 exact audit for the N=6 constraint-coupling reduction.

This is a finite symbolic audit of the web-side R47 identities.  It checks
the two-atom shadow recurrence, the degree-10/12 same-factor Fock equations,
the resulting mismatch-coordinate identities, and the nonzero local Jacobian.
It does not claim that a finite positive prefix integrates to an all-degree
positive full-exact law.
"""

from functools import lru_cache

from sympy import (
    I,
    Poly,
    Rational,
    binomial,
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


def moment_expectation(polynomial, variable, moments):
    out = 0
    for (power,), coefficient in Poly(expand(polynomial), variable).terms():
        out += coefficient * moments[power]
    return simplify(out)


def two_atom_moments(max_degree, t):
    moments = [0] * (max_degree + 1)
    moments[0] = 1
    if max_degree >= 1:
        moments[1] = 0
    for k in range(max_degree - 1):
        moments[k + 2] = simplify(t * moments[k + 1] + moments[k])
    return moments


@lru_cache(maxsize=None)
def angular_coefficient(pattern):
    """(2/3)^(d/2) times the three-direction angular average."""
    degree = sum(pattern)
    x = symbols("x")
    omega = -Rational(1, 2) - sqrt(3) * I / 2
    phases = (1, omega, omega**2)
    inverse_phases = (1, omega**2, omega)
    polynomial = 1
    for exponent, phase, inverse_phase in zip(
        pattern, phases, inverse_phases
    ):
        polynomial *= (
            phase * x + inverse_phase / x
        ) ** exponent / 2**exponent
    polynomial = expand(polynomial * x**degree)
    average = Poly(polynomial, x).coeff_monomial(x**degree)
    return simplify(Rational(2, 3) ** (degree // 2) * average)


def fock_cubic(degree, coefficients):
    out = 0
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            k = degree - i - j
            value = coefficients.get(i, 0) * coefficients.get(j, 0) * coefficients.get(k, 0)
            if value == 0:
                continue
            multiplicity = factorial(degree) / (
                factorial(i) * factorial(j) * factorial(k)
            )
            out += sqrt(multiplicity) * angular_coefficient((i, j, k)) * value
    return simplify(out)


def check_shadow_recurrence_and_heads():
    t = symbols("t")
    moments = two_atom_moments(12, t)
    u = symbols("u")
    generic_expectations = {
        j: moment_expectation(hermite_prob(j, u), u, moments)
        for j in (3, 4)
    }
    assert generic_expectations[3] == t
    assert generic_expectations[4] == t**2 - 2

    # The rank-two shadow imposes t^2=2; evaluate the remaining heads on
    # either of the two branches (the formulas are polynomial in t).
    t_value = sqrt(2)
    shadow_moments = two_atom_moments(12, t_value)
    hermite_expectations = {
        j: moment_expectation(hermite_prob(j, u), u, shadow_moments)
        for j in (3, 4, 5, 6, 7, 9, 10, 12)
    }
    expected = {
        3: t_value,
        4: 0,
        5: -6 * t_value,
        6: -4,
        7: 36 * t_value,
        9: -232 * t_value,
        10: -432,
        12: 2848,
    }
    for degree, value in expected.items():
        assert simplify(hermite_expectations[degree] - value) == 0
    print("R47_SHADOW_TWO_ATOM_RECURRENCE PASSED")


def check_fock_degree_six_ten_twelve():
    b3, b5, b6, b7, b9, b10, b12 = symbols(
        "b3 b5 b6 b7 b9 b10 b12"
    )
    degree_six = fock_cubic(6, {0: 1, 3: b3, 6: b6})
    relation_six = simplify(
        degree_six.subs(b6, Rational(7, 10) * sqrt(5) * b3**2)
    )
    assert relation_six == 0

    degree_ten = fock_cubic(
        10, {0: 1, 3: b3, 5: b5, 7: b7, 10: b10}
    )
    b10_formula = sqrt(30) * b3 * b7 + Rational(17, 14) * sqrt(7) * b5**2
    assert simplify(degree_ten.subs(b10, b10_formula)) == 0
    print("R47_DEGREE10_FOCK_IDENTITY PASSED")

    degree_twelve = fock_cubic(
        12,
        {
            0: 1,
            3: b3,
            5: b5,
            6: Rational(7, 10) * sqrt(5) * b3**2,
            7: b7,
            9: b9,
            12: b12,
        },
    )
    b12_formula = (
        Rational(10, 11) * sqrt(55) * b3 * b9
        + Rational(21, 11) * sqrt(22) * b5 * b7
        - Rational(369, 440) * sqrt(231) * b3**4
    )
    assert simplify(degree_twelve.subs(b12, b12_formula)) == 0
    print("R47_DEGREE12_FOCK_IDENTITY PASSED")


def check_mismatch_coordinate_identities():
    v = symbols("v", positive=True)
    b7_mu, b9_mu = symbols("b7_mu b9_mu")
    t = sqrt(2)
    moments = two_atom_moments(12, t)
    u = symbols("u")

    def shadow_b(degree):
        return simplify(
            v ** Rational(degree, 2)
            * moment_expectation(hermite_prob(degree, u), u, moments)
            / sqrt(factorial(degree))
        )

    b3 = shadow_b(3)
    b5 = shadow_b(5)
    b6_mu = Rational(7, 10) * sqrt(5) * b3**2
    b6_rho = shadow_b(6)
    delta6 = simplify(b6_mu - b6_rho)
    delta7 = b7_mu - shadow_b(7)
    delta9 = b9_mu - shadow_b(9)

    b10_mu = sqrt(30) * b3 * b7_mu + Rational(17, 14) * sqrt(7) * b5**2
    b10_rho = shadow_b(10)
    delta10 = simplify(b10_mu - b10_rho)
    b12_mu = (
        Rational(10, 11) * sqrt(55) * b3 * b9_mu
        + Rational(21, 11) * sqrt(22) * b5 * b7_mu
        - Rational(369, 440) * sqrt(231) * b3**4
    )
    b12_rho = shadow_b(12)
    delta12 = simplify(b12_mu - b12_rho)

    assert simplify(
        sqrt(30) * b3 * delta7
        - (delta10 - Rational(39, 14) * sqrt(7) * b5**2)
    ) == 0
    assert simplify(
        b5 * delta7
        - (
            b5 / (sqrt(30) * b3) * delta10
            + Rational(13, 35) * sqrt(42) * delta6**2
        )
    ) == 0

    assert simplify(
        Rational(10, 11) * sqrt(55) * b3 * delta9
        + Rational(21, 11) * sqrt(22) * b5 * delta7
        - (
            delta12
            + Rational(1751, 1386) * sqrt(231) * delta6**2
        )
    ) == 0
    b3_delta9_formula = (
        sqrt(55) / 50 * delta12
        - Rational(7, 50) * sqrt(3) * b5 / b3 * delta10
        - Rational(1073, 31500) * sqrt(105) * delta6**2
    )
    assert simplify(b3 * delta9 - b3_delta9_formula) == 0
    print("R47_MISMATCH_COORDINATE_IDENTITIES PASSED")


def check_local_jacobian():
    b3, b5 = symbols("b3 b5", nonzero=True)
    x7, x9 = symbols("x7 x9")
    delta10 = sqrt(30) * b3 * x7
    delta12 = (
        Rational(21, 11) * sqrt(22) * b5 * x7
        + Rational(10, 11) * sqrt(55) * b3 * x9
    )
    jacobian = simplify(
        diff(delta10, x7) * diff(delta12, x9)
        - diff(delta10, x9) * diff(delta12, x7)
    )
    assert jacobian == Rational(10, 11) * sqrt(1650) * b3**2
    print("R47_LOCAL_JACOBIAN_RANK2 PASSED")


def main():
    check_shadow_recurrence_and_heads()
    check_fock_degree_six_ten_twelve()
    check_mismatch_coordinate_identities()
    check_local_jacobian()
    print("R47_ALL_DEGREE_POSITIVE_INTEGRATION REMAINS OPEN")
    print("R47_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
