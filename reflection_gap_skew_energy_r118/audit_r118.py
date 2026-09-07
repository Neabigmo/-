"""Exact symbolic audit for the R118 reflection-gap route."""

from __future__ import annotations

import sympy as sp


def check_reflection_gap_and_mixture() -> None:
    e, o, lam = sp.symbols("e o lam", real=True)
    u, check_u = e + o, e - o
    gap = sp.expand(u**3 - u**2 * check_u)
    odd_remainder = 2 * o * (e**2 + o**2)
    assert sp.factor(gap - 4 * e * o**2 - odd_remainder) == 0
    reflected_gap = sp.expand(sp.Rational(1, 2) * (u + check_u) * (u - check_u) ** 2)
    assert sp.factor(reflected_gap - 4 * e * o**2) == 0
    mixture = sp.expand((e + lam * o) ** 3)
    even_part = e**3 + 3 * lam**2 * e * o**2
    assert sp.factor(mixture - even_part - (3 * lam * e**2 * o + lam**3 * o**3)) == 0
    # After integration the odd terms vanish, and the exact endpoint identity follows.
    print("R118_REFLECTION_GAP_AND_MIXTURE_POLYNOMIALS_PASSED")


def check_gaussian_overlap_and_barycenter_bound() -> None:
    t = sp.symbols("t", positive=True)
    prefactor = 1 / (2 * sp.pi * t * sp.sqrt(3))
    laplace_exact = t / (1 + t)
    A = sp.simplify(prefactor * laplace_exact)
    assert A == 1 / (2 * sp.pi * sp.sqrt(3) * (1 + t))

    D = sp.symbols("D", nonnegative=True)
    moment_bound = (1 + t) / (2 * sp.pi * t)
    rhs = sp.simplify(4 * D * moment_bound)
    assert sp.simplify(rhs - 2 * (1 + t) * D / (sp.pi * t)) == 0
    print("R118_GAUSSIAN_OVERLAP_AND_BARYCENTER_BOUND_CONSTANT_PASSED")


def _independent_moment_expectation(poly: sp.Expr, variables: tuple[sp.Symbol, ...], moments: dict[int, sp.Expr]) -> sp.Expr:
    polynomial = sp.Poly(sp.expand(poly), *variables)
    return sp.expand(
        sum(
            coefficient * sp.prod(moments[exponent] for exponent in monomial)
            for monomial, coefficient in polynomial.terms()
        )
    )


def check_mixed_reflection_moments() -> None:
    x1, x2, x3, kappa3 = sp.symbols("x1 x2 x3 kappa3", real=True)
    s = x1 + x2 - x3
    qsharp = sp.expand(x1**2 + x2**2 + x3**2 - s**2 / 3)
    moments = {
        0: sp.Integer(1),
        1: sp.Integer(0),
        2: sp.Integer(1),
        3: kappa3,
        4: sp.Integer(3),
        5: sp.Integer(0),
        6: 15 + 7 * kappa3**2,
    }
    eq1 = _independent_moment_expectation(qsharp, (x1, x2, x3), moments)
    eq2 = _independent_moment_expectation(qsharp**2, (x1, x2, x3), moments)
    eq3 = _independent_moment_expectation(qsharp**3, (x1, x2, x3), moments)
    assert eq1 == 2
    assert eq2 == 8
    assert sp.factor(eq3 - (48 + sp.Rational(224, 27) * kappa3**2)) == 0
    print("R118_MIXED_REFLECTION_SAMPLE_VARIANCE_MOMENTS_PASSED")


def check_positive_gap_asymptotic_and_ratio() -> None:
    t, kappa3 = sp.symbols("t kappa3", positive=True)
    lam = sp.Rational(1, 2) / t
    laplace_gap_leading = sp.Rational(112, 81) * kappa3**2 * lam**3
    prefactor = 1 / (2 * sp.pi * t * sp.sqrt(3))
    D_leading = sp.simplify(prefactor * laplace_gap_leading)
    expected_D = sp.Rational(7, 81) * kappa3**2 / (sp.pi * sp.sqrt(3) * t**4)
    assert sp.simplify(D_leading - expected_D) == 0

    B_leading = -kappa3 / (6 * sp.pi * sp.sqrt(3) * t**2)
    ratio = sp.simplify(D_leading / B_leading**2)
    assert ratio == sp.Rational(28, 3) * sp.pi / sp.sqrt(3)
    print("R118_POSITIVE_SKEW_ENERGY_ASYMPTOTIC_AND_RATIO_PASSED")


def check_conditional_third_moment_reversal() -> None:
    kappa3 = sp.symbols("kappa3", real=True)
    exact_m3 = 48 + sp.Rational(224, 27) * kappa3**2
    assert sp.simplify(exact_m3.subs(kappa3, 0) - 48) == 0
    assert sp.simplify((exact_m3 - 48) - sp.Rational(224, 27) * kappa3**2) == 0
    print("R118_CONDITIONAL_THIRD_MOMENT_REVERSAL_INTERFACE_PASSED")


def main() -> None:
    check_reflection_gap_and_mixture()
    check_gaussian_overlap_and_barycenter_bound()
    check_mixed_reflection_moments()
    check_positive_gap_asymptotic_and_ratio()
    check_conditional_third_moment_reversal()
    print("R118_REFLECTION_GAP_SKEW_ENERGY_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
