"""Exact b-to-ordinary-Taylor normalization and fixed-band replay."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def normalization_replay() -> dict:
    b = sp.symbols("b0:5")
    z = sp.symbols("z")
    hermite_series = sum(b[n] * z**n / sp.sqrt(sp.factorial(n)) for n in range(5))
    # Reconstruct ordinary coefficients by coefficient extraction via
    # derivatives, rather than copying the defining summand.
    extracted = [sp.simplify(sp.diff(hermite_series, z, n).subs(z, 0) / sp.factorial(n)) for n in range(5)]
    ordinary = sum(extracted[n] * z**n for n in range(5))
    shift_residuals = []
    for n in range(1, 5):
        basis = z**n / sp.sqrt(sp.factorial(n))
        expected = sp.sqrt(sp.factorial(n) / sp.factorial(n - 1)) * z**(n - 1) / sp.sqrt(sp.factorial(n - 1))
        shift_residuals.append(sp.simplify(sp.diff(basis, z) - expected))
    return {"residual": str(sp.expand(hermite_series - ordinary)), "coefficient_relation": "r_n=b_n/sqrt(n!)", "shift_factor_m": "sqrt(n!/(n-m)!)", "shift_residuals": [str(v) for v in shift_residuals], "shift_residuals_all_zero": all(v == 0 for v in shift_residuals)}


def fixed_band_replay() -> dict:
    n = sp.symbols("n", positive=True, integer=True)
    rows = []
    for m in range(6):
        ratio = (-sp.Rational(1, 2)) ** m * (1 + sp.Rational(m + 2, 1) / n)
        limit = sp.limit(ratio, n, sp.oo)
        rows.append({"m": m, "limit": str(limit), "expected": str((-sp.Rational(1, 2)) ** m), "residual": str(sp.simplify(limit - (-sp.Rational(1, 2)) ** m))})
    return {"rows": rows, "all_limits_exact": all(row["residual"] == "0" for row in rows), "limits_order": "n_to_infinity_at_fixed_M_then_M_to_infinity"}


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    payload = {"normalization": normalization_replay(), "fixed_band": fixed_band_replay(), "marker": "R9_NORMALIZATION_AND_FIXED_BAND_REPLAYED"}
    (RESULTS / "normalization.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R9_NORMALIZATION_RESIDUAL", payload["normalization"]["residual"])
    print("R9_FIXED_BAND_RESIDUALS", [row["residual"] for row in payload["fixed_band"]["rows"]])


if __name__ == "__main__":
    main()
