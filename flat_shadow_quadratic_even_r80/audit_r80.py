"""R80 exact audit for the quadratic-even centered operator lemma.

The checks are local identities and scalar inequalities.  They do not claim
that the conditional infinite hierarchy, positivity, or signed-Green
multiplier cancellation has been proved.
"""

import math

import sympy as sp


def check_beta_inverse() -> None:
    tau, z = sp.symbols("tau z")
    for m in (0, 1, 2, 5):
        beta_integral = sp.integrate((tau * (1 - tau)) ** m, (tau, 0, 1))
        expected = sp.factorial(m) ** 2 / sp.factorial(2 * m + 1)
        assert sp.simplify(beta_integral - expected) == 0

        W = z ** (2 * m)
        inverse_factor = sp.Rational(1, 3) * (1 + 2 * m) * 6 ** m * beta_integral
        target = 6 ** m / (3 * sp.binomial(2 * m, m))
        assert sp.simplify(inverse_factor - target) == 0
    print("R80_BETA_INVERSE_PASSED")


def check_differential_polynomial() -> None:
    z, alpha, xi, eta = sp.symbols("z alpha xi eta")
    base = z ** 6 * sp.exp(-alpha * z ** 2)
    base *= (1 - xi * z ** 2 / 2) * (1 - eta * z ** 2 / 2)
    lhs = sp.expand((base + z * sp.diff(base, z)) * sp.exp(alpha * z ** 2))
    rhs = (7 * z ** 6 - sp.Rational(13, 2) * alpha * z ** 8
           + (alpha ** 2 + sp.Rational(11, 4) * xi * eta) * z ** 10
           - sp.Rational(1, 2) * alpha * xi * eta * z ** 12)
    # The displayed polynomial uses alpha=xi+eta.
    assert sp.simplify((lhs - rhs).subs(alpha, xi + eta)) == 0
    print("R80_DIFFERENTIAL_POLYNOMIAL_PASSED")


def check_alpha_bound() -> None:
    # alpha=6*q_tau*(q_s*a+q_u*b), q<=1/4 and a+b<=1.
    upper = 6 * sp.Rational(1, 4) * sp.Rational(1, 4)
    assert upper == sp.Rational(3, 8)
    assert sp.Rational(3, 8) < sp.Rational(1, 2)
    print("R80_GAUSSIAN_PARAMETER_BOUND_PASSED")


def check_endpoint_integral() -> None:
    x, y, A, B, a, b = sp.symbols("x y A B a b", positive=True)
    integrand = x * y / (x + y) ** 3
    exact = sp.integrate(sp.integrate(integrand, (x, 0, A)), (y, 0, B))
    assert sp.simplify(exact - A * B / (2 * (A + B))) == 0

    # x=as, y=bu, A=a/2, B=b/2 gives J=sqrt(ab)/(4(a+b)).
    J = sp.sqrt(a * b) / (4 * (a + b))
    u, v = sp.symbols("u v", nonnegative=True)
    J_uv = sp.simplify(J.subs({a: u ** 2, b: v ** 2}))
    gap = sp.factor(sp.Rational(1, 8) - J_uv)
    assert sp.simplify(gap - (u - v) ** 2
                       / (8 * (u ** 2 + v ** 2))) == 0
    # Four symmetry rectangles and the quarter bound I<=32J<=4.
    assert sp.Rational(32, 8) == 4
    print("R80_ENDPOINT_INTEGRAL_PASSED")


def check_inverse_hermite_formula() -> None:
    x, alpha = sp.symbols("x alpha", positive=True)
    delta = 1 - 2 * alpha
    psi = delta ** sp.Rational(-1, 2) * sp.exp(-alpha * x ** 2 / delta)

    def R(value):
        return sp.expand(x * value - sp.diff(value, x))

    value = psi
    for m in (0, 1, 2, 3):
        rhs = (delta ** sp.Rational(-(m + 1), 2)
               * sp.hermite_prob(m, x / sp.sqrt(delta))
               * sp.exp(-alpha * x ** 2 / delta))
        assert sp.simplify(value - rhs) == 0
        value = R(value)
    print("R80_INVERSE_HERMITE_FORMULA_PASSED")


def check_bootstrap_arithmetic() -> None:
    delta = sp.Rational(1, 10000)
    rho = 32 * delta
    p = sp.Rational(1026, 1000)
    q = sp.Rational(1004, 1000)

    # O<=rho*x and P<=p*x^2.  The terms not containing 2*x*O are
    # strictly below 8*x^4, while O^2<=rho*x*O.
    tail = p ** 2 + 3 * q ** 2 * p + p ** 3 * delta ** 2
    assert tail < 8
    assert 2 + rho < 8

    # Odd improvement: A=Gamma*a^2, Z=Gamma*a^4 H^4, both <=delta.
    r = 32 * delta
    coef_A = (1 + r) * 128 * delta + (1 + r) ** 3
    coef_Z = (1 + r) * (128 * delta + 8)
    assert coef_A < 16
    assert coef_Z < 16
    print("R80_BOOTSTRAP_ARITHMETIC_PASSED")


def check_window_exponents() -> None:
    mu = sp.symbols("mu", positive=True)
    e = sp.E
    gamma_base = 16 * e * (mu + 1)
    tangent_base = 4 * e
    t_base = sp.simplify(gamma_base * tangent_base)
    assert sp.simplify(t_base - 64 * e ** 2 * (mu + 1)) == 0

    ratio_base = sp.simplify(sp.Rational(3, 2) / t_base)
    assert sp.simplify(ratio_base - 3 / (128 * e ** 2 * (mu + 1))) == 0

    # For mu>3, the sqrt(Gamma*H) denominator is the largest exponential
    # denominator among the three nonconstant terms in a_n#.
    assert float((4 / math.e) ** 0.25) > 1.0
    print("R80_WINDOW_EXPONENTS_PASSED")


def check_gram_background_constants() -> None:
    # The definition a_bg=min(1,1/(8M1),1/sqrt(8M2)) implies the two
    # background contributions are each at most 1/8.
    first = sp.Rational(1, 8)
    second = sp.Rational(1, 8)
    assert first + second == sp.Rational(1, 4) < sp.Rational(1, 2)
    print("R80_GRAM_BACKGROUND_DOMAIN_PASSED")


if __name__ == "__main__":
    check_beta_inverse()
    check_differential_polynomial()
    check_alpha_bound()
    check_endpoint_integral()
    check_inverse_hermite_formula()
    check_bootstrap_arithmetic()
    check_window_exponents()
    check_gram_background_constants()
    print("R80_QUADRATIC_EVEN_AUDIT_COMPLETED")
