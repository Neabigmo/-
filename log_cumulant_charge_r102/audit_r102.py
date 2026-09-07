"""Exact symbolic audit for the R102 log-cumulant charge formulas."""

from __future__ import annotations

from itertools import product

import sympy as sp


u, z, t = sp.symbols("u z t", nonzero=True)
rho = sp.sqrt(sp.Rational(2, 3))
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2


def direction(j: int) -> sp.Expr:
    """Exact Laurent form of sqrt(2/3)*cos(theta+2*pi*j/3)."""
    phase = omega**j
    return sp.expand(rho * (phase * u + sp.conjugate(phase) / u) / 2)


def harmonic_coefficient(m: int, charge: int = 1) -> sp.Expr:
    """Coefficient of exp(3*i*charge*theta) in sum_j direction(j)^m."""
    expr = sp.expand(u**m * sum(direction(j) ** m for j in range(3)))
    exponent = m + 3 * charge
    return sp.simplify(expr.coeff(u, exponent))


def lambda_m(m: int) -> sp.Expr:
    return sp.simplify(
        3 * (rho / 2) ** m * sp.binomial(m, (m - 3) // 2)
    )


def check_geometry() -> None:
    assert sp.simplify(sum(direction(j) for j in range(3))) == 0
    assert sp.simplify(sum(direction(j) ** 2 for j in range(3)) - 1) == 0
    for m in range(3, 16, 2):
        # The complex Fourier coefficient of cos(3 theta) is one half of its
        # cosine coefficient, hence it is Lambda_m rather than 2*Lambda_m.
        assert sp.simplify(harmonic_coefficient(m) - lambda_m(m)) == 0
        assert lambda_m(m).is_positive is True
    for m in range(0, 16):
        if m < 3 or m % 2 == 0:
            assert harmonic_coefficient(m) == 0
    print("R102_D3_GEOMETRY_AND_LAMBDA_CONSTANTS_PASSED")


def check_cumulant_projection() -> None:
    kappas = {m: sp.symbols(f"kappa{m}") for m in range(3, 14)}
    q3 = sp.expand(
        sum(kappas[m] * lambda_m(m) * z**m / sp.factorial(m)
            for m in range(3, 14, 2))
    )
    # Directly project the finite cumulant germ.  The -z^2/2 term is angularly
    # constant and must disappear from charge 3.
    direct = 0
    for m in range(3, 14):
        direct += kappas[m] * harmonic_coefficient(m) * z**m / sp.factorial(m)
    assert sp.expand(q3 - direct) == 0
    assert sp.expand(direct.subs({kappas[m]: 0 for m in range(3, 14, 2)})) == 0
    print("R102_EXACT_CUMULANT_PROJECTION_PASSED")


def check_reflection_and_ou() -> None:
    kappas = {m: sp.symbols(f"kappa{m}") for m in range(3, 14, 2)}
    q3 = sp.expand(
        sum(kappas[m] * lambda_m(m) * z**m / sp.factorial(m)
            for m in range(3, 14, 2))
    )
    reflected = sp.expand(q3.subs({k: -k for k in kappas.values()}))
    assert sp.expand(reflected + q3) == 0

    ou = sp.expand(q3.subs({kappas[m]: t ** (sp.Rational(m, 2)) * kappas[m]
                            for m in kappas}))
    assert sp.expand(ou - q3.subs(z, sp.sqrt(t) * z)) == 0
    print("R102_REFLECTION_AND_OU_COVARIANCE_PASSED")


def hermite_charge(m: int, r: int, coefficients: dict[int, sp.Expr]) -> sp.Expr:
    """R101 same-factor cubic charge map in exact Laurent arithmetic."""
    out = 0
    for k1 in range(m + 1):
        for k2 in range(m - k1 + 1):
            k3 = m - k1 - k2
            degree = k1 + k2 + k3
            expr = sp.expand(
                u**degree
                * direction(0)**k1
                * direction(1)**k2
                * direction(2)**k3
            )
            filt = sp.simplify(expr.coeff(u, degree + 3 * r))
            out += (
                sp.sqrt(sp.factorial(m) /
                        (sp.factorial(k1) * sp.factorial(k2) * sp.factorial(k3)))
                * filt
                * coefficients.get(k1, 0)
                * coefficients.get(k2, 0)
                * coefficients.get(k3, 0)
            )
    return sp.simplify(out)


def check_first_odd_sector() -> None:
    # Symbolic minimality: all lower odd Hermite coefficients vanish, while
    # even coefficients remain arbitrary.  The charge map then has only the
    # (d,0,0) permutations at total degree d.
    for d in (3, 5, 7, 9, 11):
        coeffs = {m: sp.symbols(f"a{m}") for m in range(d + 1)}
        coeffs[0] = sp.Integer(1)
        coeffs[1] = sp.Integer(0)
        for m in range(3, d, 2):
            coeffs[m] = sp.Integer(0)
        coeffs[d] = sp.symbols(f"a{d}")
        value = hermite_charge(d, 1, coeffs)
        assert sp.simplify(value - lambda_m(d) * coeffs[d]) == 0
    print("R102_FIRST_ODD_SECTOR_BETA_COMPARISON_PASSED")


def main() -> None:
    check_geometry()
    check_cumulant_projection()
    check_reflection_and_ou()
    check_first_odd_sector()
    print("R102_LOG_CUMULANT_CHARGE_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
