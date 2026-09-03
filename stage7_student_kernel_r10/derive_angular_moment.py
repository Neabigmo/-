"""Exact Student/Beta moments and direct symbolic integral checks."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
t = sp.symbols("t", real=True)


def beta_moment(n: int, s: int) -> sp.Expr:
    if s % 2:
        return sp.Integer(0)
    q = s // 2
    n_expr = sp.sympify(n)
    return sp.rf(sp.Rational(1, 2), q) / sp.rf((n_expr + 1) / 2 - q, q)


def direct_moment(n: int, s: int) -> sp.Expr:
    alpha = sp.Rational(n, 2) + 1
    numerator = sp.integrate(t**s / (1 + t**2) ** alpha, (t, -sp.oo, sp.oo))
    denominator = sp.integrate(1 / (1 + t**2) ** alpha, (t, -sp.oo, sp.oo))
    return sp.simplify(numerator / denominator)


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    rows = []
    for n in (4, 6, 8):
        for s in range(5):
            beta = sp.simplify(beta_moment(n, s))
            direct = sp.simplify(direct_moment(n, s))
            rows.append({"n": n, "degree": s, "beta": str(beta), "direct": str(direct), "residual": str(sp.simplify(beta - direct))})
    payload = {"rows": rows, "all_residuals_zero": all(row["residual"] == "0" for row in rows), "second_moment_formula": "1/(n-1)", "marker": "R10_EXACT_STUDENT_BETA_MOMENTS_REPLAYED"}
    (RESULTS / "angular_moments.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R10_DIRECT_INTEGRAL_RESIDUALS", sorted({row["residual"] for row in rows}))
    print("R10_SECOND_MOMENT_N4", beta_moment(4, 2))


if __name__ == "__main__":
    main()
