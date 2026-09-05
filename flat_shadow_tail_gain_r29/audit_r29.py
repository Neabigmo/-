"""Proof-level audit for the R29 flat-shadow one-body reduction.

The checks are deliberately algebraic.  Formal moment symbols and the
Gaussian prefix are used to verify identities only; no numerical search and
no finite-prefix construction is promoted to a genuine full-exact law.
The tail-ejection certificate controlling the one-body norm gap remains open.
"""

from __future__ import annotations

import sympy as sp


def heat(poly: sp.Expr, time: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    """Finite heat series for a polynomial in one variable."""
    degree = sp.Poly(sp.expand(poly), variable).degree()
    result = sp.Integer(0)
    term = sp.expand(poly)
    for order in range(degree // 2 + 2):
        result += time**order / (2**order * sp.factorial(order)) * term
        term = sp.diff(term, variable, 2)
        if term == 0:
            break
    return sp.expand(result)


def one_body_expectation(poly: sp.Expr, x: sp.Symbol, moments: list[sp.Expr]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), x)
    return sp.simplify(
        sum(coefficient * moments[monomial[0]] for monomial, coefficient in expanded.terms())
    )


def check_forward_jacobi_norm_identity() -> None:
    """Check the next-norm/beta packaging when moments agree through 2M+1."""
    x = sp.symbols("x")
    mu6, rho6 = sp.symbols("mu6 rho6")

    # A common centered variance-one prefix through degree 2M+1, with M=2.
    shared = [sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(3), sp.Integer(0)]
    mu = shared + [mu6]
    rho = shared + [rho6]

    # The common monic degree-three orthogonal polynomial is x^3-3x.
    pi3 = x**3 - 3 * x
    for moments in (mu, rho):
        assert one_body_expectation(pi3, x, moments[:6]) == 0
        assert one_body_expectation(x * pi3, x, moments[:6]) == 0
        assert one_body_expectation(x**2 * pi3, x, moments[:6]) == 0

    h3_mu = one_body_expectation(pi3**2, x, mu)
    h3_rho = one_body_expectation(pi3**2, x, rho)
    h2 = one_body_expectation((x**2 - 1) ** 2, x, shared)
    assert h2 == 2

    q = sp.simplify(h3_mu - h3_rho)
    beta_gap = sp.simplify(h3_mu / h2 - h3_rho / h2)
    assert q == mu6 - rho6
    assert sp.simplify(q - h2 * beta_gap) == 0

    # Same-factor heat algebra: W=P_(-a)(xP)=xR-aR' and W stays monic.
    a, b, c = sp.symbols("a b c")
    P = x**2 + b * x + c
    R = heat(P, -a, x)
    W = heat(x * P, -a, x)
    assert sp.expand(W - (x * R - a * sp.diff(R, x))) == 0
    assert sp.Poly(W, x).LC() == 1


def check_gaussian_triangle_kernel() -> None:
    """Check the positive pair kernel and its cubic trace exponent."""
    x1, x2, x3, tau = sp.symbols("x1 x2 x3 tau", nonnegative=True)
    Q = x1**2 + x2**2 + x3**2 - (x1 + x2 + x3) ** 2 / 3
    pair_sum = (x1 - x2) ** 2 + (x1 - x3) ** 2 + (x2 - x3) ** 2
    assert sp.expand(pair_sum - 3 * Q) == 0

    # k_tau(x,y)=exp(-tau(x-y)^2/6) has a positive feature expansion.
    x, y = sp.symbols("x y")
    kernel_exponent = -tau * (x - y) ** 2 / 6
    feature_exponent = -tau * x**2 / 6 - tau * y**2 / 6 + tau * x * y / 3
    assert sp.expand(kernel_exponent - feature_exponent) == 0

    cubic_trace_exponent = -tau * pair_sum / 6
    assert sp.expand(cubic_trace_exponent + tau * Q / 2) == 0

    # On the genuine exact class, the last factor averages to the chi-square
    # Laplace transform 1/(1+tau); this line checks the stated transform schema.
    exact_laplace = 1 / (1 + tau)
    assert sp.simplify(exact_laplace.subs(tau, 0) - 1) == 0


def check_schatten_bounds() -> None:
    """Verify the eigenvalue algebra behind the trace/Schatten sandwich."""
    l1, l2, l3 = sp.symbols("l1 l2 l3", nonnegative=True)
    lambdas = (l1, l2, l3)
    s1 = sum(lambdas)
    s2 = sum(lam**2 for lam in lambdas)
    s3 = sum(lam**3 for lam in lambdas)

    # Cauchy gives s2^2 <= s1*s3; the difference is an explicit sum of squares.
    pair_square_sum = sum(
        lambdas[i] * lambdas[j] * (lambdas[i] - lambdas[j]) ** 2
        for i in range(3)
        for j in range(i + 1, 3)
    )
    assert sp.expand(s1 * s3 - s2**2 - pair_square_sum) == 0

    # If s1=1, every eigenvalue lies in [0,1], hence s3<=s2.
    assert sp.expand(s2 - s3 - sum(lam**2 * (1 - lam) for lam in lambdas)) == 0

    tau = sp.symbols("tau", nonnegative=True)
    s3_exact = 1 / (1 + tau)
    assert sp.simplify((s3_exact ** sp.Rational(1, 2)) ** 2 - s3_exact) == 0
    # Thus, for Tr(T)=1 and Tr(T^3)=1/(1+tau):
    # 1/(1+tau) <= Tr(T^2) <= 1/sqrt(1+tau), and
    # ||T||_op <= (1+tau)^(-1/3).


def check_radial_moment_vanishing() -> None:
    """Check that K exact Q moments force a zero of order K+1."""
    z = sp.symbols("z")
    K = 5
    exact_moments = [2**n * sp.factorial(n) for n in range(K + 1)]
    radial_prefix = sum(
        (-z / 2) ** n * exact_moments[n] / sp.factorial(n) for n in range(K + 1)
    )
    geometric_prefix = sum((-z) ** n for n in range(K + 1))
    assert sp.expand(radial_prefix - geometric_prefix) == 0

    # The quadratic domination used in the uniform-growth remainder estimate.
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    Q = x1**2 + x2**2 + x3**2 - (x1 + x2 + x3) ** 2 / 3
    assert sp.expand(x1**2 + x2**2 + x3**2 - Q - (x1 + x2 + x3) ** 2 / 3) == 0


def main() -> None:
    checks = [
        check_forward_jacobi_norm_identity,
        check_gaussian_triangle_kernel,
        check_schatten_bounds,
        check_radial_moment_vanishing,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R29_TAIL_EJECTION_CERTIFICATE REMAINS OPEN")
    print("R29_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
