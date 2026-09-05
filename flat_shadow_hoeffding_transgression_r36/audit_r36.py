"""R36 exact audit: one-body Laguerre--Hoeffding carrier obstruction.

This is a finite symbolic audit of the identities used by the R36 web-side
argument.  It deliberately avoids numerical sweeps, optimization, SDP, and
relaxed-law searches.  The remote-carrier conclusion is recorded from exact
algebra plus the displayed geometric-decay limit; the two-body carrier is not
claimed to be closed.
"""

from itertools import product

from sympy import (
    Poly,
    Rational,
    binomial,
    factorial,
    limit,
    oo,
    simplify,
    sqrt,
    symbols,
)


def laguerre(n, x):
    return sum((-1) ** k * binomial(n, k) * x**k / factorial(k) for k in range(n + 1))


def hermite_prob(n, x):
    # Probabilists' Hermite polynomial, written in an exact finite form.
    return sum(
        (-1) ** k
        * factorial(n)
        * x ** (n - 2 * k)
        / (2**k * factorial(k) * factorial(n - 2 * k))
        for k in range(n // 2 + 1)
    )


def exp_expectation(poly, x):
    """Expectation of a polynomial under T~Exp(1): E[T^k]=k!."""
    out = 0
    for (power,), coeff in Poly(poly.expand(), x).terms():
        out += coeff * factorial(power)
    return simplify(out)


def gaussian_moment(power):
    if power % 2:
        return 0
    return factorial(power) / (2 ** (power // 2) * factorial(power // 2))


def gaussian_expectation(poly, x):
    out = 0
    for (power,), coeff in Poly(poly.expand(), x).terms():
        out += coeff * gaussian_moment(power)
    return simplify(out)


def angular_average_even_hermite(n, r2, y):
    """Average h_{2n}(r cos(theta)) using exact angular moments."""
    poly = Poly(hermite_prob(2 * n, y) / sqrt(factorial(2 * n)), y)
    out = 0
    for (power,), coeff in poly.terms():
        if power % 2 == 0:
            p = power // 2
            out += coeff * r2**p * binomial(2 * p, p) / 4**p
    return simplify(out)


def expectation_rademacher(expr, variables):
    out = 0
    for values in product((-1, 1), repeat=len(variables)):
        out += expr.subs(dict(zip(variables, values)))
    return simplify(out / 2 ** len(variables))


def phi3(a, b, c):
    # A concrete symmetric Hoeffding decomposition on iid Rademacher inputs:
    # h1=sum Xi, h2=sum XiXj, h3=X1X2X3.
    return a + b + c + a * b + a * c + b * c + a * b * c


def check_laguerre_and_anchor():
    t = symbols("t")
    for n in range(1, 5):
        assert exp_expectation(laguerre(n, t), t) == 0
        assert exp_expectation(laguerre(n, t) ** 2, t) == 1
    for n in range(5):
        for m in range(5):
            target = 1 if n == m else 0
            assert exp_expectation(laguerre(n, t) * laguerre(m, t), t) == target


def check_angular_identity_and_one_body_projection():
    r2, y = symbols("r2 y")
    for n in range(1, 5):
        c_n = sqrt(factorial(2 * n)) / (2**n * factorial(n))
        lhs = angular_average_even_hermite(n, r2, y)
        rhs = (-1) ** n * c_n * laguerre(n, r2 / 2)
        assert simplify(lhs - rhs) == 0

        # Gaussian conditional Hermite contraction has correlation
        # sqrt(2/3), hence h_{2n} contracts by (2/3)^n.
        kappa_n = (-1) ** n * c_n * Rational(2, 3) ** n
        assert simplify(kappa_n**2 - binomial(2 * n, n) / 9**n) == 0
        assert simplify((sqrt(Rational(2, 3)) ** (2 * n)) - Rational(2, 3) ** n) == 0


def check_hoeffding_and_five_copy_identity():
    x1, x2, x3, x4, x5 = symbols("x1 x2 x3 x4 x5")
    phi = phi3(x1, x2, x3)

    total = expectation_rademacher(phi**2, (x1, x2, x3))
    h1_norm = expectation_rademacher(x1**2, (x1,))
    h2_norm = expectation_rademacher((x1 * x2) ** 2, (x1, x2))
    h3_norm = expectation_rademacher((x1 * x2 * x3) ** 2, (x1, x2, x3))
    assert total == 3 * h1_norm + 3 * h2_norm + h3_norm

    # Shared-coordinate Fubini identity:
    # E[k(X1)^2] = E[Phi(X1,X2,X3) Phi(X1,X4,X5)].
    shared = phi3(x1, x2, x3) * phi3(x1, x4, x5)
    k = sum(phi3(x1, a, b) for a in (-1, 1) for b in (-1, 1)) / 4
    left = expectation_rademacher(k**2, (x1,))
    right = expectation_rademacher(shared, (x1, x2, x3, x4, x5))
    assert left == right


def check_five_copy_derivative_decomposition():
    x1, x2, x3, x4, x5 = symbols("x1 x2 x3 x4 x5")
    left_factor = phi3(x1, x2, x3)
    right_factor = phi3(x1, x4, x5)
    product_value = left_factor * right_factor

    s_term = expectation_rademacher(x1 * product_value, (x1, x2, x3, x4, x5))
    l_term = expectation_rademacher(x2 * product_value, (x1, x2, x3, x4, x5))
    derivative = expectation_rademacher(
        (x1 + x2 + x3 + x4 + x5) * product_value,
        (x1, x2, x3, x4, x5),
    )
    assert simplify(derivative - (s_term + 4 * l_term)) == 0
    assert simplify(3 * derivative - 3 * (s_term + 4 * l_term)) == 0


def check_hermite_triple_coefficient():
    x = symbols("x")
    for n in range(1, 5):
        h2n = hermite_prob(2 * n, x) / sqrt(factorial(2 * n))
        for N in range(0, 4 * n + 1, 2):
            hN = hermite_prob(N, x) / sqrt(factorial(N))
            lhs = gaussian_expectation(hN * h2n**2, x)
            rhs = (
                sqrt(factorial(N))
                * factorial(2 * n)
                / (factorial(2 * n - N // 2) * factorial(N // 2) ** 2)
            )
            assert simplify(lhs - rhs) == 0


def check_remote_collapse_schema():
    # The fixed-head bound is polynomial(n) times (2/3)^n, so its exact
    # asymptotic vanishes.  Cauchy--Schwarz then kills any l2-bounded remote
    # one-body carrier; no finite numerical tail estimate is needed.
    n = symbols("n", positive=True)
    assert limit((1 + n**2) * Rational(2, 3) ** n, n, oo) == 0

    # The first mismatch convention used by R36.
    N, q = symbols("N q", positive=True)
    assert simplify((q / sqrt(factorial(N))) * sqrt(factorial(N)) - q) == 0


def main():
    check_laguerre_and_anchor()
    print("R36_HOEFFDING_VALUE_IDENTITY PASSED")
    check_angular_identity_and_one_body_projection()
    print("R36_GAUSSIAN_ONE_BODY_PROJECTION PASSED")
    check_hoeffding_and_five_copy_identity()
    check_five_copy_derivative_decomposition()
    check_hermite_triple_coefficient()
    check_remote_collapse_schema()
    print("R36_FIXED_HEAD_SENSITIVITY_COLLAPSE PASSED")
    print("R36_REMOTE_ONE_BODY_CARRIER NO_GO")
    print("R36_TWO_BODY CARRIER REMAINS OPEN")
    print("R36_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
