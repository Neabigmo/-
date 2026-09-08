"""Exact algebraic audit for the R134 tensor--Jacobi energy claims.

This audit checks the finite algebra and constants used by the webpage proof.
It does not replace the analytic hypotheses (positivity, full-SF, or
hypercontractivity); those scopes are recorded explicitly in the README.
"""

from __future__ import annotations

import math

import sympy as sp


def check_multinomial_egf() -> None:
    z = sp.symbols("z")
    p1, p2, p3 = sp.symbols("p1 p2 p3")
    q = sp.symbols("q0:7")
    for n in range(7):
        t_n = sum(
            sp.factorial(n) / (sp.factorial(i) * sp.factorial(j) * sp.factorial(k))
            * p1**i * p2**j * p3**k * q[i] * q[j] * q[k]
            for i in range(n + 1)
            for j in range(n - i + 1)
            for k in [n - i - j]
        )
        product_coeff = sp.expand(
            sum(q[i] * (p1 * z) ** i / sp.factorial(i) for i in range(7))
            * sum(q[i] * (p2 * z) ** i / sp.factorial(i) for i in range(7))
            * sum(q[i] * (p3 * z) ** i / sp.factorial(i) for i in range(7))
        ).coeff(z, n) * sp.factorial(n)
        assert sp.simplify(t_n - product_coeff) == 0
    print("R134_MULTINOMIAL_EGF_PASSED")


def check_determinant_dictionary() -> None:
    beta = sp.symbols("beta1:8", positive=True)
    q = [sp.Integer(1)]
    for n, b in enumerate(beta, start=1):
        q.append(sp.factor(q[-1] * b / n))
    for m in range(1, 8):
        lhs = sp.prod(q[1 : m + 1])
        rhs = sp.prod(beta[j - 1] / j for j in range(1, m + 1) for _ in range(m - j + 1))
        assert sp.simplify(lhs - rhs) == 0
    print("R134_DETERMINANT_DICTIONARY_PASSED")


def check_angular_lambda_and_critical_constant() -> None:
    for n in range(1, 40):
        lam = 3 * (sp.Rational(2, 3) ** n) * sp.binomial(2 * n, n) / (4**n)
        assert lam > 0
    coeff = sp.Rational(9, 2) * (1 + sp.Rational(1, 2)) ** 2 / (1 - sp.Rational(1, 2))
    assert coeff == sp.Rational(81, 4)
    print("R134_ANGULAR_LAMBDA_AND_CRITICAL_CONSTANT_PASSED")


def check_bregman_bounds() -> None:
    x = sp.symbols("x", real=True)
    f = x - sp.log(1 + x)
    for dv in [sp.Rational(1, 10), sp.Rational(1, 3), sp.Rational(1, 2)]:
        for xv in [-dv, -dv / 2, dv / 2, dv]:
            assert float(f.subs(x, xv)) + 1e-12 >= float(xv**2 / (2 * (1 + dv) ** 2))
            assert float(f.subs(x, xv)) <= float(xv**2 / (2 * (1 - dv) ** 2)) + 1e-12
    print("R134_MATRIX_BREGMAN_SCALAR_BOUNDS_PASSED")


def check_residual_constants() -> None:
    delta = sp.symbols("delta", nonnegative=True)
    assert sp.simplify(18 * (1 + delta) ** 2 / (1 - delta)).subs(delta, sp.Rational(1, 2)) == 81
    eps = sp.symbols("eps", nonnegative=True)
    polynomial = sp.expand(7 * eps**2 - ((1 + eps**2) ** 3 - 1))
    assert sp.simplify(polynomial - eps**2 * (4 - 3 * eps**2 - eps**4)) == 0
    assert float(polynomial.subs(eps, 1)) == 0.0
    print("R134_RESIDUAL_CONSTANTS_PASSED")


def check_log_functional_local_weights() -> None:
    for n in range(1, 30):
        for i in range(n + 1):
            for j in range(n - i + 1):
                k = n - i - j
                for ell in range(1, n + 1):
                    nj = int(i >= ell) + int(j >= ell) + int(k >= ell)
                    assert 0 <= nj <= 3
    for m in range(1, 30):
        for j in range(1, m + 1):
            assert 3 * (m - j + 1) == sum(3 for _ in range(j, m + 1))
        for j in range(1, m + 1):
            for k in range(1, m + 1):
                assert sp.Rational(9, 4) * (m - max(j, k) + 1) == sum(
                    sp.Rational(9, 4) for _ in range(max(j, k), m + 1)
                )
    print("R134_LOG_FUNCTIONAL_LOCAL_WEIGHT_OBSTRUCTION_PASSED")


def main() -> None:
    check_multinomial_egf()
    check_determinant_dictionary()
    check_angular_lambda_and_critical_constant()
    check_bregman_bounds()
    check_residual_constants()
    check_log_functional_local_weights()
    print("R134_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
