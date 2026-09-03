"""Exact D3 geometry and small-z angular-mode formulas."""

from __future__ import annotations

import sympy as sp

from common import require, write_json


theta, z, kappa = sp.symbols("theta z kappa", real=True)
rho = sp.sqrt(sp.Rational(2, 3))
phases = [0, 2 * sp.pi / 3, 4 * sp.pi / 3]
a = [rho * sp.cos(theta + phase) for phase in phases]
b = [sp.diff(item, theta) for item in a]


def exact_geometry() -> dict[str, object]:
    checks = {
        "sum_a": sp.trigsimp(sum(a)),
        "sum_b": sp.trigsimp(sum(b)),
        "sum_a2": sp.trigsimp(sum(item**2 for item in a)),
        "sum_b2": sp.trigsimp(sum(item**2 for item in b)),
        "sum_ab": sp.trigsimp(sum(x * y for x, y in zip(a, b))),
        "pointwise_a2_plus_b2": [sp.trigsimp(x**2 + y**2) for x, y in zip(a, b)],
    }
    require(checks["sum_a"] == 0, "sum a_j is not zero")
    require(checks["sum_b"] == 0, "sum b_j is not zero")
    require(checks["sum_a2"] == 1, "sum a_j^2 is not one")
    require(checks["sum_b2"] == 1, "sum b_j^2 is not one")
    require(checks["sum_ab"] == 0, "sum a_j b_j is not zero")
    require(all(item == sp.Rational(2, 3) for item in checks["pointwise_a2_plus_b2"]), "pointwise norm failed")
    return {"a": a, "b": b, "checks": checks}


def p_d(d: int) -> sp.Expr:
    require(d >= 0, "d must be nonnegative")
    return sp.expand_trig(sum(item**d for item in a))


def positive_harmonic_coefficients(d: int) -> list[dict[str, object]]:
    require(d % 2 == 1 and d >= 3, "d must be odd and at least three")
    out = []
    for m in range(3, d + 1, 6):
        coeff = 3 * rho**d * sp.Rational(2 ** (1 - d)) * sp.binomial(d, (d - m) // 2)
        out.append({"m": m, "cos_coefficient": sp.simplify(coeff)})
    return out


def verify_fourier_formula(d: int) -> dict[str, object]:
    coeffs = positive_harmonic_coefficients(d)
    # Compare Laurent polynomials in q=exp(i*theta), avoiding fragile trig
    # simplification with shifted angles.  omega is an exact third root of unity.
    q = sp.symbols("q", nonzero=True)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    omega_bar = -sp.Rational(1, 2) - sp.sqrt(3) * sp.I / 2
    roots = [1, omega, omega_bar]
    a_laurent = [rho / 2 * (q * roots[j] + q**-1 * roots[(-j) % 3]) for j in range(3)]
    lhs = sp.cancel(sum(item**d for item in a_laurent))
    rhs = sp.expand(
        sum(item["cos_coefficient"] * (q**item["m"] + q**(-item["m"])) / 2 for item in coeffs)
    )
    residual = sp.expand(sp.cancel(lhs - rhs))
    require(residual == 0, f"Fourier formula failed for d={d}: {residual}")
    return {
        "d": d,
        "surviving_harmonics": [item["m"] for item in coeffs],
        "coefficients": coeffs,
        "formula_verified": True,
    }


def main() -> None:
    geometry = exact_geometry()
    fourier = [verify_fourier_formula(d) for d in (3, 5, 7, 9, 11)]
    write_json(
        "angular_geometry.json",
        {
            "status": "EXACT_D3_GEOMETRY_VERIFIED",
            "geometry": geometry["checks"],
            "fourier_checks": fourier,
        },
    )
    print("EXACT_D3_GEOMETRY_VERIFIED")
    print("EXACT_P_D_FOURIER_FORMULA_VERIFIED", len(fourier))


if __name__ == "__main__":
    main()
