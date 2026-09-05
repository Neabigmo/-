"""Proof-level audit for the R27 residual Gram and covariance no-go.

The checks separate polynomial identities from the conditional positivity and
the unresolved residual-jet contraction.  The finite-prefix moments used below
are only an algebraic seed; they are not a full-exact counterexample.
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


def seed_data():
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    variables = (x1, x2, x3)
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
    bar = sum(variables) / 3
    F_list = [(variable - bar) * P.subs(x, variable) for variable in variables]
    q = one_body_expectation(x**2 * P**2, x, moments)
    return variables, x, P, F_list, moments, q


def check_flat_orthogonality_gram() -> None:
    variables, _, _, F_list, moments, q = seed_data()
    gram = sp.Matrix(
        [
            [iid_expectation(Fi * Fj, variables, moments) for Fj in F_list]
            for Fi in F_list
        ]
    )
    assert gram == sp.Rational(4, 9) * q * sp.eye(3)


def check_matrix_heat_decomposition() -> None:
    a = sp.symbols("a")
    variables, _, _, F_list, moments, q = seed_data()
    G_list = [heat(Fi, -a, variables) for Fi in F_list]
    degree = max(sp.Poly(Fi, *variables).total_degree() for Fi in F_list)

    A = sp.Matrix(
        [
            [iid_expectation(heat(Gi * Gj, a, variables), variables, moments) for Gj in G_list]
            for Gi in G_list
        ]
    )
    E = sp.zeros(3, 3)
    for i, Fi in enumerate(F_list):
        for j, Fj in enumerate(F_list):
            value = sp.Integer(0)
            for alpha in all_multi_indices(degree, len(variables)):
                if sum(alpha) == 0:
                    continue
                dFi = differentiate(Fi, variables, alpha)
                dFj = differentiate(Fj, variables, alpha)
                value += (
                    a ** sum(alpha)
                    / sp.prod(sp.factorial(k) for k in alpha)
                    * iid_expectation(dFi * dFj, variables, moments)
                )
            E[i, j] = sp.simplify(value)

    assert all(sp.simplify((A - E)[i, j] - (sp.Rational(4, 9) * q if i == j else 0)) == 0
               for i in range(3) for j in range(3))
    c = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    assert sp.simplify((c.T * (A - E) * c)[0] - sp.Rational(4, 9) * q) == 0


def check_antisymmetric_factorization() -> None:
    x1, x2, x3, x = sp.symbols("x1 x2 x3 x")
    P = x**3 + 2 * x**2 - x + 1
    d1 = (2 * x1 - x2 - x3) / 3
    d2 = (2 * x2 - x1 - x3) / 3
    quotient = sp.cancel((P.subs(x, x1) - P.subs(x, x2)) / (x1 - x2))
    H = (P.subs(x, x1) + P.subs(x, x2)) / 2 + (x1 + x2 - 2 * x3) * quotient / 6
    assert sp.expand(d1 * P.subs(x, x1) - d2 * P.subs(x, x2) - (x1 - x2) * H) == 0


def check_residual_covariance_budget() -> None:
    q, t, r1, r2 = sp.symbols("q t r1 r2", nonnegative=True)
    trace = t * (r1 + r2)
    coefficient = sp.factor(q * (trace - 2 * t) / 2)
    assert coefficient == sp.Rational(1, 2) * q * t * (r1 + r2 - 2)

    # Endpoint/interior samples certify the advertised budget orientation;
    # the general implication is the elementary spectral bound 0<=r_i<=1.
    samples = [(0, 0), (0, 1), (sp.Rational(1, 4), sp.Rational(3, 4)), (1, 1)]
    assert all(coefficient.subs({r1: u, r2: v}) <= 0 for u, v in samples)
    assert sp.simplify(coefficient.subs({r1: 1, r2: 1})) == 0


def main() -> None:
    checks = [
        check_flat_orthogonality_gram,
        check_matrix_heat_decomposition,
        check_antisymmetric_factorization,
        check_residual_covariance_budget,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R27_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
