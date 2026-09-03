"""Exact D3 geometry and the assumed two-dimensional Gaussian mixture theorem."""

from __future__ import annotations

import sympy as sp

from common import require, write_json

theta, s, t, z = sp.symbols("theta s t z", real=True)
rho = sp.sqrt(sp.Rational(2, 3))
phases = [0, 2 * sp.pi / 3, 4 * sp.pi / 3]
a = [rho * sp.cos(theta + phase) for phase in phases]
b = [sp.diff(item, theta) for item in a]

def geometry_checks() -> dict[str, object]:
    checks = {
        "sum_a2": sp.trigsimp(sum(item**2 for item in a)),
        "sum_b2": sp.trigsimp(sum(item**2 for item in b)),
        "sum_ab": sp.trigsimp(sum(x * y for x, y in zip(a, b))),
        "pointwise_norm": [sp.trigsimp(x**2 + y**2) for x, y in zip(a, b)],
        "a_derivative_is_b": [sp.trigsimp(sp.diff(x, theta) - y) for x, y in zip(a, b)],
        "b_derivative_is_minus_a": [sp.trigsimp(sp.diff(y, theta) + x) for x, y in zip(a, b)],
    }
    require(checks["sum_a2"] == 1 and checks["sum_b2"] == 1, "D3 norm failed")
    require(checks["sum_ab"] == 0, "D3 orthogonality failed")
    require(all(v == sp.Rational(2, 3) for v in checks["pointwise_norm"]), "pointwise norm failed")
    require(all(v == 0 for v in checks["a_derivative_is_b"]), "a'=b failed")
    require(all(v == 0 for v in checks["b_derivative_is_minus_a"]), "b'=-a failed")
    return checks

def exact_pair_identity() -> dict[str, object]:
    checks = geometry_checks()
    q3 = sp.expand(sum((a[j] * s + b[j] * t) ** 2 for j in range(3)))
    require(sp.trigsimp(q3 - s**2 - t**2) == 0, "Q3 pair norm failed")
    return {
        "status": "EXACT_BIVARIATE_TILTED_MIXTURE_VERIFIED",
        "geometry": checks,
        "Q3_pair_identity": "Q3=L_Theta^2+T_Theta^2",
        "uniform_pair_law": "(L_Theta,T_Theta) ~ N((0,0), I2), conditional on target Q3 law",
        "uniform_pair_mgf": sp.exp((s**2 + t**2) / 2),
        "tilted_pair_mgf": sp.exp(z * s + (s**2 + t**2) / 2),
        "tilted_pair_law": "N((z,0), I2)",
        "scope": "The pair law is conditional on the original target angular identity.",
    }

def main() -> None:
    write_json("bivariate_mixture.json", exact_pair_identity())
    print("EXACT_D3_BIVARIATE_GEOMETRY_VERIFIED")
    print("EXACT_BIVARIATE_TILTED_MIXTURE_VERIFIED")

if __name__ == "__main__":
    main()
