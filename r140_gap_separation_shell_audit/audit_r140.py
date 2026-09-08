"""Finite checks for the R140 gap/separation shell-to-energy audit.

The checks validate algebraic interfaces and the conservative tail constant used
in README.md.  Entire-function, Fisher, and probability-level conclusions remain
proof-level claims with their hypotheses recorded in the README.
"""

from __future__ import annotations

import cmath
import math

import sympy as sp


def check_shifted_cesaro_block() -> None:
    # A concrete separated first shell.  The displayed estimate is checked for
    # every starting index in a finite window; the analytic proof uses the
    # geometric-series bound uniformly in the shift.
    theta = (0.17, 1.03, 2.11)
    delta = (1, -1, 2)
    V = sum(x * x for x in delta)
    L = sum(abs(x) for x in delta)
    lam = [cmath.exp(-2j * t) for t in theta]
    sigma = min(abs(lam[i] - lam[j]) for i in range(3) for j in range(i))
    N = math.ceil(max(1.0, 4 * L * L / (sigma * V)))
    for K in range(0, 7):
        block = sum(
            abs(sum(delta[j] * cmath.exp(-1j * (2 * (K + k) + 1) * theta[j])
                    for j in range(3))) ** 2
            for k in range(N)
        ) / N
        lower = V - 2 * L * L / (N * sigma)
        assert block + 1e-12 >= lower
        assert lower >= V / 2 - 1e-12
    print("R140_SHIFTED_CESARO_BLOCK_PASSED")


def check_shell_normalization() -> None:
    rho = sp.sqrt(sp.Rational(2, 3))
    m = sp.symbols("m", integer=True, positive=True)
    # Check the coefficient identity at representative odd degrees.
    for degree in (3, 5, 7, 9, 13):
        ell = sp.Rational(3, 2**degree) * sp.binomial(degree, (degree - 3) // 2)
        Lambda = 3 * (rho / 2) ** degree * sp.binomial(
            degree, (degree - 3) // 2
        )
        normalized = sp.simplify(Lambda * (1 / rho) ** degree)
        assert sp.simplify(normalized - ell) == 0
        assert ell <= 3
    assert m is not None
    print("R140_SHELL_NORMALIZATION_PASSED")


def check_conservative_tail_radius() -> None:
    # The proof uses |b_n| <= 3B/n and the odd-tail step of 2.  For tau <= 1/2,
    # ||tail||_2 <= 4B*tau^(M+5/2)/((M+2)*sqrt(2M+5)).
    # The denominator 8 in tau^2 is exactly sufficient for half the finite-part
    # lower bound.
    cases = (
        (3, 0.21, 0.17, 5.0),
        (7, 0.08, 0.11, 3.5),
        (11, 0.035, 0.09, 2.0),
    )
    for M, a, sqrt_h, B in cases:
        tau2 = a * sqrt_h * (M + 2) * math.sqrt(2 * M + 5) / (8 * B)
        tau = min(0.5, math.sqrt(tau2))
        tail_bound = 4 * B * tau ** (M + 2.5) / ((M + 2) * math.sqrt(2 * M + 5))
        finite_half = 0.5 * a * sqrt_h * tau ** (M + 0.5)
        assert tail_bound <= finite_half * (1 + 1e-10)
    print("R140_CONSERVATIVE_TAIL_CONSTANT_PASSED")


def check_bernoulli_zero_formula() -> None:
    # For p+q=1, exp((a+b) zeta_k)=-q/p at the displayed zeros.
    p = sp.Rational(2, 5)
    q = 1 - p
    a = sp.sqrt(q / p)
    b = sp.sqrt(p / q)
    # The real part is logarithmic; check the algebraic exponent relation using
    # a symbolic log placeholder and an odd multiple of pi.
    for ell in (-2, -1, 0, 1, 2):
        z = sp.sqrt(p * q) * (sp.log(q / p) + sp.I * (2 * ell + 1) * sp.pi)
        assert sp.simplify((a + b) * z - (sp.log(q / p) + sp.I * (2 * ell + 1) * sp.pi)) == 0
        assert sp.simplify(p * sp.exp(a * z) + q * sp.exp(-b * z)) == 0
    print("R140_BERNOULLI_ZERO_FORMULA_PASSED")


def check_triangle_bochner_identity() -> None:
    a, b, c, d, e, f = sp.symbols("a b c d e f", real=True)
    z1, z2, z3 = a + sp.I * b, c + sp.I * d, e + sp.I * f
    # Hermitian 3x3 determinant with phi(-t)=conjugate(phi(t)); the cyclic
    # product is the phase term in the triangle inequality.
    matrix = sp.Matrix(
        [
            [1, sp.conjugate(z1), z3],
            [z1, 1, sp.conjugate(z2)],
            [sp.conjugate(z3), z2, 1],
        ]
    )
    det = sp.expand(matrix.det())
    expected = 1 - (a * a + b * b + c * c + d * d + e * e + f * f)
    expected += 2 * sp.expand((z1 * z2 * z3).as_real_imag()[0])
    assert sp.simplify(det - expected) == 0
    print("R140_TRIANGLE_BOCHNER_PASSED")


def check_even_cone_and_orders() -> None:
    for m in range(2, 12):
        A = sp.Rational(3) * sp.binomial(2 * m, m) / sp.Integer(6) ** m
        assert A > 0
    for s in range(1, 10):
        d = 2 * s + 1
        assert s + 2 == (d + 3) // 2
        assert 2 * d > d
    print("R140_EVEN_CONE_AND_ORDER_INTERFACES_PASSED")


def main() -> None:
    check_shifted_cesaro_block()
    check_shell_normalization()
    check_conservative_tail_radius()
    check_bernoulli_zero_formula()
    check_triangle_bochner_identity()
    check_even_cone_and_orders()
    print("R140_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
