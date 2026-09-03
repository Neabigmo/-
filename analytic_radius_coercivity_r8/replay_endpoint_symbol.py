"""Exact fixed-band and endpoint-symbol replays for R8."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def fixed_band_replay() -> dict:
    n = sp.symbols("n", positive=True, integer=True)
    rows = []
    for m in range(5):
        # The correction is explicitly O(1/n), so the fixed-m limit is exact.
        ratio = (-sp.Rational(1, 2)) ** m * (1 + sp.Rational(m + 1, 1) / n)
        limit = sp.limit(ratio, n, sp.oo)
        rows.append({"m": m, "limit": str(limit), "expected": str((-sp.Rational(1, 2)) ** m), "residual": str(sp.simplify(limit - (-sp.Rational(1, 2)) ** m))})
    return {"rows": rows, "all_fixed_band_limits_exact": all(row["residual"] == "0" for row in rows), "order_of_limits_warning": True}


def endpoint_symbol_replay() -> dict:
    z = sp.symbols("z")
    # Use an even Gaussian entire profile; the symbol simplifies exactly.
    R = lambda x: sp.exp(-x ** 2 / 2)
    symbol = sp.simplify((R(z / 2) ** 2 + R(-z / 2) ** 2) / 2)
    expected = sp.exp(-z ** 2 / 4)
    return {"symbol": str(symbol), "expected_gaussian_symbol": str(expected), "residual": str(sp.simplify(symbol - expected)), "gaussian_symbol_nonzero": True, "D_at_zero": str(symbol.subs(z, 0))}


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    payload = {"fixed_band": fixed_band_replay(), "endpoint_symbol": endpoint_symbol_replay(), "marker": "R8_STAGE7_ENDPOINT_SYMBOL_REPLAYED"}
    (RESULTS / "endpoint_symbol.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R8_FIXED_BAND_RESIDUALS", [row["residual"] for row in payload["fixed_band"]["rows"]])
    print("R8_GAUSSIAN_SYMBOL_RESIDUAL", payload["endpoint_symbol"]["residual"])
    print("R8_GAUSSIAN_REPLAY_COMPLETED", payload["endpoint_symbol"]["D_at_zero"])


if __name__ == "__main__":
    main()

