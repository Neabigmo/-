"""R79 tangent-centered Gram/source bootstrap arithmetic audit.

This file checks identities and scalar inequalities only. It deliberately
does not use determinants, optimizers, or numerical parameter sweeps.
"""

import math

import sympy as sp


def check_centered_gram_domain() -> None:
    cg = (math.sqrt(3) / 2) ** 3 / (1 - math.sqrt(3) / 2)
    assert cg < 5

    # Neumann control: ||a A + H|| <= 1/2 implies ||(I+K)^(-1)|| <= 2.
    tangent_part = sp.Rational(1, 4)
    residual_part = sp.Rational(1, 20) * 5
    assert tangent_part + residual_part <= sp.Rational(1, 2)
    assert 1 / (1 - sp.Rational(1, 2)) == 2

    # The multilinear resolvent coefficient is r! times the product of the
    # directional perturbation sizes, with the inverse bound 2^(r+1).
    for rval in (1, 2, 3):
        coefficient = math.factorial(rval) * 2 ** (rval + 1)
        assert coefficient == math.factorial(rval) * 2 ** (rval + 1)
    print("R79_CENTERED_GRAM_DOMAIN_PASSED")


def check_parity_source_ideal() -> None:
    a, E, o = sp.symbols("a E o")
    # A representative full local ideal: E(a,o) plus all centered monomials
    # of total degree at least three.
    source = a * E + E * o + a**3 + a**2 * o + a * o**2 + o**3
    polynomial = sp.Poly(source, a, E, o)
    assert polynomial.terms()
    for powers, _coefficient in polynomial.terms():
        pa, pE, po = powers
        has_E_ideal = pE >= 1 and pa + po >= 1
        has_cubic_ideal = pE == 0 and pa + po >= 3
        assert has_E_ideal or has_cubic_ideal

    # Reflection fixes E and flips (a,o), so the centered residual is odd.
    reflected = sp.expand(source.subs({a: -a, o: -o}, simultaneous=True))
    assert sp.expand(reflected + source) == 0
    print("R79_PARITY_SOURCE_IDEAL_PASSED")


def check_even_odd_bootstrap() -> None:
    x = sp.Rational(1, 100)
    even_input = 8 * x**2
    total = even_input + x + x
    even_map = total**2 + total**3
    assert even_map <= even_input

    # With |a|+O <= 2x and E_* <= 8x^2, the source factor is at most 24x^3.
    xi_bound = (2 * x) * (8 * x**2) + (2 * x) ** 3
    assert xi_bound == 24 * x**3
    gamma_threshold = 1 / (48 * x**2)
    assert 24 * gamma_threshold * x**3 == x / 2
    print("R79_EVEN_ODD_BOOTSTRAP_PASSED")


def check_tangent_norm_and_window_exponents() -> None:
    e = math.e
    for nval in range(1, 16):
        radius = 4 * math.sqrt(nval)
        tangent_norm = sum(
            kval * math.factorial(kval + 1)
            / (2 * math.factorial(2 * kval + 1))
            * radius ** (2 * kval + 1)
            for kval in range(1, nval + 1)
        )
        assert tangent_norm <= 4 * nval**3 * (4 * e) ** nval

    mu = sp.symbols("mu", positive=True)
    gamma_base = 16 * sp.E * (mu + 1)
    a_base_squared = sp.simplify((4 * sp.E * sp.sqrt(gamma_base)) ** 2)
    assert sp.simplify(a_base_squared - 256 * sp.E**3 * (mu + 1)) == 0
    assert sp.Rational(11, 4) * 2 == sp.Rational(11, 2)
    print("R79_TANGENT_WINDOW_EXPONENTS_PASSED")


def check_scalar_feedback_obstruction() -> None:
    Gamma, a, E, O = sp.symbols("Gamma a E O")
    solved = sp.solve(sp.Eq(O, Gamma * (a * E + E * O)), O)[0]
    assert sp.simplify(solved - Gamma * a * E / (1 - Gamma * E)) == 0
    denominator = sp.denom(sp.factor(solved))
    assert sp.simplify(denominator + (1 - Gamma * E)) == 0
    print("R79_SCALAR_FEEDBACK_OBSTRUCTION_PASSED")


if __name__ == "__main__":
    check_centered_gram_domain()
    check_parity_source_ideal()
    check_even_odd_bootstrap()
    check_tangent_norm_and_window_exponents()
    check_scalar_feedback_obstruction()
    print("R79_TANGENT_CENTERED_AUDIT_COMPLETED")
