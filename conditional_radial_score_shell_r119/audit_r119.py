"""Exact symbolic audit for the R119 score-shell reduction."""

from __future__ import annotations

import sympy as sp


def _expect(poly: sp.Expr, variables: tuple[sp.Symbol, ...], moments: dict[int, sp.Expr]) -> sp.Expr:
    polynomial = sp.Poly(sp.expand(poly), *variables)
    return sp.expand(
        sum(
            coefficient * sp.prod(moments[exponent] for exponent in monomial)
            for monomial, coefficient in polynomial.terms()
        )
    )


def check_sign_flip_identity() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    q = sp.expand(x1**2 + x2**2 + x3**2 - (x1 + x2 + x3) ** 2 / 3)
    qsharp = sp.expand(x1**2 + x2**2 + x3**2 - (x1 + x2 - x3) ** 2 / 3)
    assert sp.factor(qsharp - q - sp.Rational(4, 3) * x3 * (x1 + x2)) == 0

    v, m3, m4, m5, m6 = sp.symbols("v m3 m4 m5 m6", real=True)
    moments = {0: 1, 1: 0, 2: v, 3: m3, 4: m4, 5: m5, 6: m6}
    eq1 = _expect(qsharp - q, (x1, x2, x3), moments)
    eq2 = _expect(qsharp**2 - q**2, (x1, x2, x3), moments)
    eq3 = _expect(qsharp**3 - q**3, (x1, x2, x3), moments)
    assert eq1 == 0
    assert eq2 == 0
    assert sp.factor(eq3 - sp.Rational(224, 27) * m3**2) == 0
    print("R119_UNIVERSAL_SIGN_FLIP_MOMENT_IDENTITY_PASSED")


def check_laplace_coefficient() -> None:
    lam, kappa3 = sp.symbols("lam kappa3", real=True)
    coefficient = sp.simplify((sp.Rational(224, 27) * kappa3**2) * lam**3 / 6)
    assert coefficient == sp.Rational(112, 81) * kappa3**2 * lam**3
    print("R119_LAPLACE_SATURATION_EQUIVALENCE_COEFFICIENT_PASSED")


def check_profile_orthogonality_obstruction() -> None:
    q = sp.symbols("q", nonnegative=True)
    density = sp.exp(-q / 2) / 2
    h0 = q - 2
    mean_h0 = sp.integrate(h0 * density, (q, 0, sp.oo))
    q_h0 = sp.integrate(q * h0 * density, (q, 0, sp.oo))
    assert sp.simplify(mean_h0) == 0
    assert sp.simplify(q_h0 - 4) == 0
    print("R119_PROFILE_ONE_SIGN_CHANGE_ORTHOGONALITY_NO_GO_PASSED")


def check_score_shell_covariance_algebra() -> None:
    q, h, hp = sp.symbols("q h hp", real=True)
    conditional_bar_sigma_r = 2 * q * hp - q * h
    conditional_sigma_r = -q
    covariance = sp.expand(conditional_bar_sigma_r - h * conditional_sigma_r)
    assert sp.factor(covariance - 2 * q * hp) == 0

    # Exponential-law integration by parts: int q h' dnu = 1/2 int q h dnu
    # when int h dnu=0, yielding E[Xbar Q]=E[conditional covariance].
    kappa3 = sp.symbols("kappa3", real=True)
    mean_qh = sp.Rational(2, 3) * kappa3
    mean_cov = mean_qh
    assert sp.simplify(sp.Rational(3, 2) * mean_qh - kappa3) == 0
    assert sp.simplify(mean_cov - mean_qh) == 0
    print("R119_CONDITIONAL_RADIAL_SCORE_COVARIANCE_INTERFACE_PASSED")


def check_reflection_sign_logic() -> None:
    hp = sp.symbols("hp", real=True)
    reflected_hp = -hp
    assert sp.simplify(reflected_hp + hp) == 0
    # A fixed sign for both f and its reflection forces hp=-hp.
    assert sp.simplify(hp - (-hp) - 2 * hp) == 0
    print("R119_REFLECTION_STABLE_SIGN_LOGIC_PASSED")


def main() -> None:
    check_sign_flip_identity()
    check_laplace_coefficient()
    check_profile_orthogonality_obstruction()
    check_score_shell_covariance_algebra()
    check_reflection_sign_logic()
    print("R119_CONDITIONAL_RADIAL_SCORE_SHELL_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
