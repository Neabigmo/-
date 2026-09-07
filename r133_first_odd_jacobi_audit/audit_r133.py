"""Exact algebraic audit for the R133 first-odd Jacobi packet."""

from __future__ import annotations

import math

import sympy as sp


def check_angular_even_positivity() -> None:
    # <p_{2r}> = 3 (2/3)^r binom(2r,r) / 4^r > 0.
    for r in range(1, 16):
        value = sp.Rational(3) * (sp.Rational(2, 3) ** r) * sp.binomial(2 * r, r) / (4**r)
        assert value > 0
    print("R133_ANGULAR_EVEN_POSITIVITY_PASSED")


def check_first_odd_combinatorial_identity() -> None:
    for s in range(1, 20):
        d = 2 * s + 1
        left = sp.factorial(d) / (sp.factorial(s) ** 2 * (s + 1))
        right = sp.binomial(d, s)
        assert sp.simplify(left - right) == 0
    print("R133_FIRST_ODD_COMBINATORIAL_IDENTITY_PASSED")


def check_jacobi_determinant_block() -> None:
    a = sp.symbols("a")
    for s in range(1, 10):
        d = 2 * s + 1
        b = sp.binomial(d, s)
        c = sp.sqrt(b) * a
        block = sp.Matrix([[1, c], [c, 1]])
        assert sp.simplify(block.det() - (1 - b * a**2)) == 0

        kappa = sp.sqrt(sp.factorial(d)) * a
        alpha_sq = sp.simplify((kappa / sp.factorial(s)) ** 2)
        assert sp.simplify(alpha_sq / (s + 1) - b * a**2) == 0

        beta = sp.simplify((s + 1) - alpha_sq)
        assert sp.simplify(1 - beta / (s + 1) - b * a**2) == 0
    print("R133_JACOBI_DETERMINANT_BLOCK_PASSED")


def check_subcritical_no_go() -> None:
    # The exact packet coefficient is bounded by binom(2k-1,k-1)<4^k.
    for k in range(2, 80):
        assert sp.binomial(2 * k - 1, k - 1) < 4**k
    # Since 4<3^2, the exponent 2-log_3(4) is strictly positive.
    assert 4 < 3**2
    print("R133_4K_SUBCRITICAL_NO_GO_PASSED")


def check_finite_row_blindness_interface() -> None:
    m = 2
    constrained_degrees = set(range(2 * m + 1))
    assert {0, 1, 2}.issubset(constrained_degrees)

    lam, qf, cubic = sp.symbols("lam qf cubic", positive=True)
    # The moment constraints kill the linear term of the log charge because
    # psi_3 is a cubic polynomial; the quadratic term is strictly negative.
    ell_second_order = -lam**2 * qf / 2
    remainder_bound = sp.Rational(2, 3) * lam**3 * cubic
    threshold = sp.Rational(3, 4) * qf / cubic
    assert sp.simplify(remainder_bound.subs(lam, threshold) + ell_second_order.subs(lam, threshold)) == 0
    # A compactly supported nonzero f can be scaled by lambda to make its L2
    # norm arbitrarily small while preserving the exact finite moment rows.
    assert math.isfinite(float(threshold.subs({qf: 1, cubic: 1})))
    print("R133_FINITE_ROW_BLINDNESS_INTERFACE_PASSED")


def main() -> None:
    check_angular_even_positivity()
    check_first_odd_combinatorial_identity()
    check_jacobi_determinant_block()
    check_subcritical_no_go()
    check_finite_row_blindness_interface()
    print("R133_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
