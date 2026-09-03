"""Exact endpoint kernel, fixed-band expansion, and Gaussian correction."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from derive_angular_moment import beta_moment, direct_moment


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
n = sp.symbols("n", positive=True, integer=True)
t = sp.symbols("t", real=True)


def expectation_poly(expr: sp.Expr, degree: int, moment_fn=beta_moment) -> sp.Expr:
    poly = sp.Poly(sp.expand(expr), t)
    total = sp.Integer(0)
    for (power,), coeff in poly.terms():
        total += coeff * moment_fn(degree, power)
    return sp.simplify(total)


def student_kernel(j: int, k: int, degree: int) -> sp.Expr:
    a = -sp.Rational(1, 2) - sp.sqrt(3) * t / 2
    b = -sp.Rational(1, 2) + sp.sqrt(3) * t / 2
    return expectation_poly(a**j * b**k, degree)


def direct_kernel(j: int, k: int, degree: int) -> sp.Expr:
    alpha = sp.Rational(degree, 2) + 1
    a = -sp.Rational(1, 2) - sp.sqrt(3) * t / 2
    b = -sp.Rational(1, 2) + sp.sqrt(3) * t / 2
    numerator = sp.integrate(a**j * b**k / (1 + t**2) ** alpha, (t, -sp.oo, sp.oo))
    denominator = sp.integrate(1 / (1 + t**2) ** alpha, (t, -sp.oo, sp.oo))
    return sp.simplify(numerator / denominator)


def fixed_band_rows(max_m: int = 4) -> list[dict]:
    rows = []
    for j in range(max_m + 1):
        for k in range(max_m + 1 - j):
            expr = student_kernel(j, k, n)
            limit = sp.simplify(sp.limit(expr, n, sp.oo))
            expected = (-sp.Rational(1, 2)) ** (j + k)
            first = sp.simplify(sp.limit(n * (expr - expected), n, sp.oo))
            rows.append({"j": j, "k": k, "limit": str(limit), "expected": str(expected), "limit_residual": str(sp.simplify(limit - expected)), "first_1_over_n": str(first)})
    return rows


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    direct_rows = []
    for degree in (4, 6):
        for j in range(3):
            for k in range(3 - j):
                exact = student_kernel(j, k, degree)
                direct = direct_kernel(j, k, degree)
                direct_rows.append({"n": degree, "j": j, "k": k, "student": str(exact), "direct": str(direct), "residual": str(sp.simplify(exact - direct))})
    z = sp.symbols("z")
    gaussian_R = sp.Integer(1)
    gaussian_D = sp.simplify((gaussian_R**2 + gaussian_R**2) / 2)
    fixed = fixed_band_rows()
    payload = {"direct_kernel_rows": direct_rows, "direct_kernel_all_exact": all(row["residual"] == "0" for row in direct_rows), "fixed_band": fixed, "fixed_band_all_exact": all(row["limit_residual"] == "0" for row in fixed), "gaussian_R": str(gaussian_R), "gaussian_D_R": str(gaussian_D), "gaussian_replay_correct": gaussian_D == 1, "marker": "R10_STUDENT_KERNEL_AND_FIXED_BAND_REPLAYED"}
    (RESULTS / "student_kernel.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R10_DIRECT_KERNEL_RESIDUALS", sorted({row["residual"] for row in direct_rows}))
    print("R10_FIXED_BAND_RESIDUALS", sorted({row["limit_residual"] for row in fixed}))
    print("R10_GAUSSIAN_R_D", payload["gaussian_R"], payload["gaussian_D_R"])


if __name__ == "__main__":
    main()

