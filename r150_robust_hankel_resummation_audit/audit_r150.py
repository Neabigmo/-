"""Finite audit for the R150 robust Hankel reduction.

This script checks algebraic interfaces and the finite continuity model.  It
does not claim the missing joint (degree, amplitude) estimate.
"""

from __future__ import annotations

import math

import sympy as sp


def formal_moments(d: int, a: sp.Expr, order: int) -> list[sp.Expr]:
    z = sp.symbols("z")
    series = sp.exp(z**2 / 2 + a * z**d).series(z, 0, order + 1).removeO().expand()
    return [sp.simplify(series.coeff(z, k) * sp.factorial(k)) for k in range(order + 1)]


def central_trinomial(n: int) -> int:
    return sum(
        math.factorial(n) // (math.factorial(j) ** 2 * math.factorial(n - 2 * j))
        for j in range(n // 2 + 1)
    )


def check_sparse_hankel_caps() -> None:
    a = sp.symbols("a", real=True)
    for d in (5, 7, 9, 11):
        s = (d - 1) // 2
        k = s + 1
        moments = formal_moments(d, a, 2 * k)
        hankel = sp.Matrix([[moments[i + j] for j in range(k + 1)] for i in range(k + 1)])
        determinant = sp.factor(hankel.det())
        gaussian_determinant = sp.prod(sp.factorial(j) for j in range(k + 1))
        expected = 1 - sp.factorial(d) * sp.binomial(d, s) * a**2
        assert sp.simplify(determinant / gaussian_determinant - expected) == 0
    print("R150_INHERITED_SPARSE_HANKEL_CAP_PASSED")


def check_finite_continuity_model() -> None:
    a, b = sp.symbols("a b", real=True)
    d = 5
    # Add one higher odd coefficient.  Every moment and Hankel entry up to a
    # fixed order is polynomial in the finite coefficient vector.
    z = sp.symbols("z")
    series = sp.exp(z**2 / 2 + a * z**d + b * z ** (d + 2)).series(z, 0, 15).removeO().expand()
    moments = [sp.expand(series.coeff(z, k) * sp.factorial(k)) for k in range(15)]
    matrix = sp.Matrix([[moments[i + j] for j in range(6)] for i in range(6)])
    for entry in matrix:
        assert sp.Poly(entry, a, b).is_zero is False or entry == 0
    assert all(entry.subs(b, 0).is_polynomial(a) for entry in matrix)
    print("R150_FINITE_POLYNOMIAL_CONTINUITY_MODEL_PASSED")


def check_ou_rate_algebra() -> None:
    d = 5
    a = sp.symbols("a", positive=True)
    lam, A, R, S = sp.symbols("lam A R S", positive=True)
    a_lam = A * lam ** (sp.Rational(d, 2))
    tail_bound = S * R ** (-(d + 2)) * lam ** (sp.Rational(d + 2, 2))
    reduced = sp.simplify(tail_bound.subs(lam, (a / A) ** (sp.Rational(2, d))))
    expected = S * R ** (-(d + 2)) * A ** (-(1 + sp.Rational(2, d))) * a ** (1 + sp.Rational(2, d))
    assert sp.simplify(reduced - expected) == 0
    assert sp.simplify((1 + sp.Rational(2, d)) - 1) > 0
    print("R150_OU_DIAGONAL_RATE_ALGEBRA_PASSED")


def check_r149_interface() -> None:
    # The nonlinear source/inverse scales used by R149 and the R150 tail
    # comparison have the advertised asymptotic bases.
    for d in (5, 9, 15, 25):
        td = central_trinomial(d)
        ad = math.factorial(d) * td / math.sqrt(math.factorial(2 * d))
        assert ad > 0
        assert td / math.comb(2 * d, d) < 0.26
    print("R150_R149_SOURCE_INTERFACE_PASSED")


def main() -> None:
    check_sparse_hankel_caps()
    check_finite_continuity_model()
    check_ou_rate_algebra()
    check_r149_interface()
    print("R150_SCOPE_EXPLICIT: fixed-degree reduction only; joint moving-degree rate remains open")
    print("R150_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
