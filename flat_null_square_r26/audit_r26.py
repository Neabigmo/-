"""Proof-level audit for the R26 flat-null-square reductions.

The audit checks the algebraic pullback, the flat Taylor jet, the leading
wrong-sign escort coefficient, and the reverse-heat square identity.  It does
not claim the missing residual-corrected domination or Gaussian rigidity.
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
    """Finite polynomial realization of exp(time*Delta/2)."""

    degree = sp.Poly(sp.expand(poly), *variables).total_degree()
    result = sp.Integer(0)
    term = sp.expand(poly)
    for order in range(degree // 2 + 2):
        result += time**order / (2**order * sp.factorial(order)) * term
        term = laplacian(term, variables)
        if term == 0:
            break
    return sp.expand(result)


def all_multi_indices(max_degree: int, dimension: int):
    for alpha in product(range(max_degree + 1), repeat=dimension):
        if sum(alpha) <= max_degree:
            yield alpha


def differentiate(poly: sp.Expr, variables: tuple[sp.Symbol, ...], alpha: tuple[int, ...]) -> sp.Expr:
    result = poly
    for variable, order in zip(variables, alpha):
        if order:
            result = sp.diff(result, variable, order)
    return sp.expand(result)


def check_posterior_pullback() -> None:
    a, t, x, y, z = sp.symbols("a t x y z")
    D = 1 + a * t
    s = y / D
    u = t / D

    # Completing the square in the forward Gaussian heat image.
    observed_exponent = (a * y**2 + 2 * x * y - t * x**2) / (2 * D)
    pulled_back_exponent = a * y**2 / (2 * D) + s * x - u * x**2 / 2
    assert sp.simplify(observed_exponent - pulled_back_exponent) == 0

    # The transported polynomial satisfies p_{t,y}((x+ay)/D)=P(x).
    coefficients = sp.symbols("c0:5")
    P = sum(coefficients[k] * x**k for k in range(5))
    p = sum(coefficients[k] * (D * z - a * y) ** k for k in range(5))
    assert sp.expand(p.subs(z, (x + a * y) / D) - P) == 0


def check_flat_parabolic_expansion() -> None:
    x, s, u = sp.symbols("x s u")
    q, m3, m4 = sp.symbols("q m3 m4")
    moments = [sp.Integer(0), sp.Integer(0), q, m3, m4]

    # Total degree two Taylor polynomial of exp(s*x-u*x^2/2).
    jet = 1 + s * x - u * x**2 / 2 + s**2 * x**2 / 2 - s * u * x**3 / 2 + u**2 * x**4 / 8
    value = one_body_expectation(jet, x, moments)
    expected = q * (s**2 - u) / 2 - m3 * s * u / 2 + m4 * u**2 / 8
    assert sp.expand(value - expected) == 0
    assert sp.expand(value.subs(u, 0)).coeff(s, 2) == q / 2
    assert sp.expand(value.subs(s, 0)).coeff(u, 1) == -q / 2


def check_escort_wrong_sign() -> None:
    a, q, t = sp.symbols("a q t", positive=True)
    D = 1 + a * t
    # The escort has E[Y^2]=t/3+O(t^2); only the displayed leading jet is used.
    expected_s_square = (t / 3) / D**2
    u = t / D
    leading = q * (expected_s_square - u) / 2
    assert sp.simplify(sp.limit(leading / t, t, 0)) == -q / 3


def check_reverse_heat_square_identity() -> None:
    a = sp.symbols("a")
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    variables = (x1, x2, x3)
    P = x**3 + 2 * x**2 - x + 1
    bar = sum(variables) / 3
    F = (x1 - bar) * P.subs(x, x1)

    G = heat(F, -a, variables)
    lhs = heat(G**2, a, variables)
    degree = sp.Poly(F, *variables).total_degree()
    rhs = sp.Integer(0)
    for alpha in all_multi_indices(degree, len(variables)):
        derivative = differentiate(F, variables, alpha)
        rhs += a ** sum(alpha) / sp.prod(sp.factorial(k) for k in alpha) * derivative**2
    assert sp.expand(lhs - rhs) == 0

    # For F_i=(X_i-bar)P(X_i), P_-a F_i has the claimed explicit form.
    hat_p = heat(P, -a, (x,))
    explicit = (x1 - bar) * hat_p.subs(x, x1) - 2 * a * sp.diff(hat_p, x).subs(x, x1) / 3
    assert sp.expand(G - explicit) == 0


def check_reverse_heat_decomposition() -> None:
    a = sp.symbols("a")
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    variables = (x1, x2, x3)
    bar = sum(variables) / 3

    # The first six moments come from the positive three-atomic Jacobi seed;
    # m8 is the R24 finite-prefix overshoot value.  Only the algebraic
    # decomposition is tested here; this is not a full-exact counterexample.
    moments = [
        sp.Integer(1),
        sp.Integer(0),
        sp.Integer(1),
        sp.Integer(1),
        sp.Integer(3),
        4 - 2 * sp.sqrt(3),
        sp.Integer(22),
        3 - 36 * sp.sqrt(3),
        109 - 64 * sp.sqrt(3),
    ]
    J = sp.Matrix(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, -1 - 2 * sp.sqrt(3)],
        ]
    )
    P = sp.expand(J.charpoly(x).as_expr())
    q = one_body_expectation(x**2 * P**2, x, moments)
    F_list = [(variable - bar) * P.subs(x, variable) for variable in variables]
    residual_square = sum(iid_expectation(Fi**2, variables, moments) for Fi in F_list)
    assert sp.simplify(residual_square - sp.Rational(4, 3) * q) == 0

    A = sp.Integer(0)
    noise = sp.Integer(0)
    for Fi in F_list:
        Gi = heat(Fi, -a, variables)
        A += iid_expectation(heat(Gi**2, a, variables), variables, moments)
        degree = sp.Poly(Fi, *variables).total_degree()
        for alpha in all_multi_indices(degree, len(variables)):
            if sum(alpha) == 0:
                continue
            derivative = differentiate(Fi, variables, alpha)
            noise += (
                a ** sum(alpha)
                / sp.prod(sp.factorial(k) for k in alpha)
                * iid_expectation(derivative**2, variables, moments)
            )
    assert sp.simplify(A - sp.Rational(4, 3) * q - noise) == 0

    # Every nonzero derivative has one-body degree at most M=3.  Thus the
    # conditional E>=0 statement uses only H_3(L)>=0, not inverse positivity
    # on arbitrary higher-degree squares.
    for Fi in F_list:
        degree = sp.Poly(Fi, *variables).total_degree()
        for alpha in all_multi_indices(degree, len(variables)):
            if sum(alpha) == 0:
                continue
            derivative = differentiate(Fi, variables, alpha)
            if derivative == 0:
                continue
            poly = sp.Poly(derivative, *variables)
            assert all(poly.degree(variable) <= 3 for variable in variables)


def main() -> None:
    checks = [
        check_posterior_pullback,
        check_flat_parabolic_expansion,
        check_escort_wrong_sign,
        check_reverse_heat_square_identity,
        check_reverse_heat_decomposition,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R26_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
