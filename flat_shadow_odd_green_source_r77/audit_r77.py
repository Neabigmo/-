"""R77 local Gram-to-source factorial estimate arithmetic audit."""

import math

import sympy as sp


def check_degree_local_gram_ball() -> None:
    ratio = sp.sqrt(3) / 2
    c_g = ratio**3 / (1 - ratio)
    assert c_g < 5
    delta = sp.Rational(1, 40)
    assert c_g * delta < sp.Rational(1, 8)
    assert 1 / (1 - c_g * delta) < sp.Rational(8, 7)

    for kval in range(3, 12):
        rho = 4 * sp.sqrt(kval)
        for mval in range(3, 2 * kval + 1):
            operator_bound = (
                2**mval * (3 * kval) ** sp.Rational(mval, 2)
                / sp.sqrt(math.factorial(mval))
            )
            weight_bound = sp.sqrt(math.factorial(mval)) / rho**mval
            assert sp.simplify(operator_bound * weight_bound - ratio**mval) == 0
    print("R77_DEGREE_LOCAL_GRAM_BALL_CHECK_PASSED")


def check_holder_hypercontractive_exponents() -> None:
    mu = sp.symbols("mu", positive=True)
    q_mu = mu + 1
    p_mu = 2 * (mu + 1) / (mu - 3)
    assert sp.simplify(1 / p_mu + 2 / q_mu - sp.Rational(1, 2)) == 0
    assert sp.simplify(q_mu - 1 - mu) == 0
    for mval in [sp.Rational(7, 2), 4, 5, 10]:
        assert sp.simplify(p_mu.subs(mu, mval)) > 0
        assert sp.simplify(q_mu.subs(mu, mval)) > 2
    # The endpoint is not finite in this Holder choice.
    assert sp.limit(p_mu, mu, 3, dir="+") == sp.oo
    print("R77_HOLDER_HYPERCONTRACTIVE_THRESHOLD_CHECK_PASSED")


def check_parity_taylor_ideal() -> None:
    a, E, Y = sp.symbols("a E Y")
    # Generic representatives after the Gaussian Y-linear term has been
    # removed. The residual must lie in a(E,Y^2)+EY+Y^3.
    A = 1 + E + Y**2 + E * Y**2 + E**2 + Y**4
    B = E * Y + Y**3 + E * Y**3
    residual = sp.Poly(sp.expand(a * A + B - a), a, E, Y)
    for pa, pe, py in residual.monoms():
        assert (
            (pa >= 1 and pe >= 1)
            or (pa >= 1 and py >= 2)
            or (pe >= 1 and py >= 1)
            or py >= 3
        )
    print("R77_PARITY_TAYLOR_IDEAL_CHECK_PASSED")


def check_local_to_top_norm() -> None:
    # The top-radius replacement is monotone because rho_k <= rho_n and all
    # coefficients enter through absolute values.
    for nval in range(3, 12):
        for kval in range(3, nval + 1):
            assert 4 * math.sqrt(kval) <= 4 * math.sqrt(nval)
    print("R77_LOCAL_TO_TOP_RADIUS_MONOTONICITY_PASSED")


def check_odd_bootstrap_exponents() -> None:
    eps = sp.symbols("eps", positive=True)
    # lambda_(3+eps)=4+eps, hence 64 lambda = 256+64 eps.
    assert sp.simplify(64 * (4 + eps) - (256 + 64 * eps)) == 0

    # U^2 contributes 1024*n*exp(320n); the signed-source prefactor is
    # n^(-1/2)*exp((256+64eps)n), leaving sqrt(n) and exponent 576+64eps.
    assert sp.simplify((256 + 64 * eps) + 320 - (576 + 64 * eps)) == 0
    assert sp.simplify(-sp.Rational(1, 2) + 1 - sp.Rational(1, 2)) == 0

    # Squaring the a-scale doubles both the polynomial and exponential powers.
    assert sp.simplify(2 * sp.Rational(1, 4) - sp.Rational(1, 2)) == 0
    assert sp.simplify(2 * (288 + 32 * eps) - (576 + 64 * eps)) == 0
    print("R77_ODD_BOOTSTRAP_EXPONENT_CHECK_PASSED")


if __name__ == "__main__":
    check_degree_local_gram_ball()
    check_holder_hypercontractive_exponents()
    check_parity_taylor_ideal()
    check_local_to_top_norm()
    check_odd_bootstrap_exponents()
    print("R77_LOCAL_FACTORIAL_SOURCE_AUDIT_COMPLETED")

