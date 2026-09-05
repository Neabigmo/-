"""Proof-level audit for the R28 flat-shadow reduction.

The checks below verify polynomial/operator identities and the moment-degree
cancellation behind the R28 route.  Toy atomic/normal laws and formal moment
vectors are used only as algebraic witnesses; none is a genuine full-exact
counterexample.
"""

from __future__ import annotations

from itertools import product

import sympy as sp


def one_body_expectation(poly: sp.Expr, x: sp.Symbol, moments: list[sp.Expr]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), x)
    return sp.simplify(
        sum(coefficient * moments[monomial[0]] for monomial, coefficient in expanded.terms())
    )


def iid_expectation(
    poly: sp.Expr, variables: tuple[sp.Symbol, ...], moments: list[sp.Expr]
) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), *variables)
    total = sp.Integer(0)
    for monomial, coefficient in expanded.terms():
        product_moment = coefficient
        for degree in monomial:
            product_moment *= moments[degree]
        total += product_moment
    return sp.simplify(total)


def laplacian(poly: sp.Expr, variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    return sp.expand(sum(sp.diff(poly, variable, 2) for variable in variables))


def heat(poly: sp.Expr, time: sp.Expr, variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    degree = sp.Poly(sp.expand(poly), *variables).total_degree()
    result = sp.Integer(0)
    term = sp.expand(poly)
    for order in range(degree // 2 + 2):
        result += time**order / (2**order * sp.factorial(order)) * term
        term = laplacian(term, variables)
        if term == 0:
            break
    return sp.expand(result)


def normal_moments(max_degree: int) -> list[sp.Expr]:
    moments = []
    for degree in range(max_degree + 1):
        moments.append(sp.Integer(0) if degree % 2 else sp.factorial2(degree - 1))
    moments[0] = sp.Integer(1)
    return moments


def check_positive_shadow_realization() -> None:
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    variables = (x1, x2, x3)
    a = sp.Rational(1, 2)
    P = x**2 - 1
    bar = sum(variables) / 3
    F = [(variable - bar) * P.subs(x, variable) for variable in variables]
    F_minus = (F[0] - F[1]) / sp.sqrt(2)
    G_minus = heat(F_minus, -a, variables)

    nu_moments = [sp.Integer(1) if degree % 2 == 0 else sp.Integer(0) for degree in range(20)]
    rho_expect = lambda poly: iid_expectation(heat(poly, a, variables), variables, nu_moments)
    nu_expect = lambda poly: iid_expectation(poly, variables, nu_moments)

    assert sp.simplify(heat(G_minus, a, variables) - F_minus) == 0
    assert all(
        sp.simplify(F_minus.subs({x1: u, x2: v, x3: w})) == 0
        for u, v, w in product((-1, 1), repeat=3)
    )
    assert nu_expect(F_minus**2) == 0
    conditional_mean = heat(G_minus, a, variables)
    conditional_variance = heat(G_minus**2, a, variables) - conditional_mean**2
    assert sp.simplify(rho_expect(G_minus**2) - nu_expect(conditional_variance)) == 0
    assert sp.simplify(rho_expect(G_minus**2) - nu_expect(conditional_mean**2)) == rho_expect(G_minus**2)


def build_r28_objects():
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    variables = (x1, x2, x3)
    a = sp.Rational(1, 3)
    # Choose P so that R=P_(-a)P is the degree-four Hermite polynomial for the
    # normal audit law; this enforces the centered null means used below.
    R_anchor = x**4 - 6 * x**2 + 3
    P = heat(R_anchor, a, (x,))
    bar = sum(variables) / 3
    F = [(variable - bar) * P.subs(x, variable) for variable in variables]
    R = heat(P, -a, (x,))
    W = heat(x * P, -a, (x,))
    G = [heat(Fi, -a, variables) for Fi in F]
    return x1, x2, x3, x, variables, a, P, F, R, W, G


def check_one_body_and_same_factor_decomposition() -> None:
    x1, x2, x3, x, variables, a, P, F, R, W, G = build_r28_objects()
    assert sp.expand(W - (x * R - a * sp.diff(R, x))) == 0
    for index, variable in enumerate(variables):
        others = sum(other for j, other in enumerate(variables) if j != index)
        expected = sp.Rational(2, 3) * W.subs(x, variable) - sp.Rational(1, 3) * others * R.subs(x, variable)
        assert sp.expand(G[index] - expected) == 0
    assert sp.Poly(R, x).degree() == 4
    assert sp.Poly(W, x).degree() == 5


def check_hoeffding_identity() -> None:
    _, _, _, x, variables, _, _, _, R, W, G = build_r28_objects()
    moments = normal_moments(14)
    G_minus = (G[0] - G[1]) / sp.sqrt(2)
    one_body = sp.Rational(2, 3) * (W.subs(x, variables[0]) - W.subs(x, variables[1])) / sp.sqrt(2)
    two_body = G_minus - one_body
    assert one_body_expectation(R, x, moments) == 0
    assert one_body_expectation(W, x, moments) == 0
    assert iid_expectation(one_body * two_body, variables, moments) == 0

    left = iid_expectation(G_minus**2, variables, moments)
    right = (
        sp.Rational(4, 9) * one_body_expectation(W**2, x, moments)
        + sp.Rational(2, 9) * one_body_expectation(R**2, x, moments)
        - sp.Rational(1, 9) * one_body_expectation(x * R, x, moments) ** 2
    )
    assert sp.simplify(left - right) == 0


def check_shadow_moment_cancellation() -> None:
    _, _, _, x, _, a, P, _, R, W, _ = build_r28_objects()
    degree = sp.Poly(P, x).degree()
    assert degree == 4
    formal_mu = [sp.Symbol(f"m{k}") for k in range(2 * degree + 3)]
    q = sp.Symbol("q")
    formal_shadow = formal_mu.copy()
    # The shadow/support premise converts the first unfixed moment gap into q.
    formal_shadow[2 * degree + 2] = formal_mu[2 * degree + 2] - q

    assert sp.Poly(R**2, x).degree() <= 2 * degree
    assert sp.Poly(x * R, x).degree() <= degree + 1
    derivative_remainder = sp.expand(heat(W**2, a, (x,)) - (x * P) ** 2)
    assert sp.Poly(derivative_remainder, x).degree() <= 2 * degree

    mu_w2 = one_body_expectation(W**2, x, formal_mu)
    shadow_w2 = one_body_expectation(W**2, x, formal_shadow)
    assert sp.simplify(mu_w2 - shadow_w2 - q) == 0
    assert one_body_expectation(R**2, x, formal_mu) == one_body_expectation(R**2, x, formal_shadow)
    assert one_body_expectation(x * R, x, formal_mu) == one_body_expectation(x * R, x, formal_shadow)


def check_pair_sum_identity() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    D = x1 - x2
    S = x1 + x2
    Y = x3
    Q = x1**2 + x2**2 + x3**2 - (x1 + x2 + x3) ** 2 / 3
    assert sp.expand(Q - (D**2 / 2 + (S - 2 * Y) ** 2 / 6)) == 0


def main() -> None:
    checks = [
        check_positive_shadow_realization,
        check_one_body_and_same_factor_decomposition,
        check_hoeffding_identity,
        check_shadow_moment_cancellation,
        check_pair_sum_identity,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R28_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
