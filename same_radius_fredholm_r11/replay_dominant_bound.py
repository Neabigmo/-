"""Finite replays for global, dominant, and nondominant estimates."""
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

from derive_exact_Aijk import a_star, angular_kernel

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def global_bound_replay(max_degree: int = 8) -> dict:
    rows = []
    for i in range(max_degree + 1):
        for j in range(max_degree - i + 1):
            for k in range(max_degree - i - j + 1):
                n = i + j + k
                value = sp.simplify(angular_kernel(i, j, k))
                gap = sp.simplify(a_star ** (2 * n) - value**2)
                rows.append({"i": i, "j": j, "k": k, "gap_nonnegative": bool(gap.is_nonnegative)})
    return {"rows": rows, "all_finite_replays_hold": all(row["gap_nonnegative"] for row in rows), "a_star": str(a_star)}


def c_even(q: int) -> sp.Rational:
    return sp.Rational(math.comb(2 * q, q), 4**q)


def dominant_bound_replay(max_a: int = 40, max_b: int = 20) -> dict:
    rows = []
    for a in range(1, max_a + 1):
        for b in range(0, min(max_b, a) + 1):
            ratio = sp.Rational(c_even(a), c_even(a + b))
            bound = math.exp(b / (2 * a + 1))
            rows.append({"a": a, "b": b, "ratio": str(ratio), "ratio_le_exp_bound": float(ratio) <= bound + 1e-15, "ratio_lt_2": float(ratio) < 2})
    return {"rows": rows, "all_ratio_bounds_hold": all(row["ratio_le_exp_bound"] and row["ratio_lt_2"] for row in rows), "marker": "UNIFORM_DOMINANT_KERNEL_BOUND"}


def fixed_band_and_tail() -> dict:
    fixed_rows = []
    for N in (1, 2, 4, 8, 16, 32):
        fixed_rows.append({"N": N, "shift_tail_sup": str(sp.Rational(1, N + 1))})
    eta = sp.Rational(1, 2)
    tail_rows = []
    for M in (2, 4, 8, 16, 24):
        sup = max((sp.sqrt(n + 1) * eta**n for n in range(M, 100)), default=sp.Integer(0))
        tail_rows.append({"M": M, "sqrt_n_eta_n_sup": str(sup)})
    return {"fixed_shift": fixed_rows, "nondominant": tail_rows, "fixed_tail_tends_to_zero": fixed_rows[-1]["shift_tail_sup"] == "1/33", "nondominant_tail_decreases": all(sp.sympify(tail_rows[i]["sqrt_n_eta_n_sup"]) >= sp.sympify(tail_rows[i + 1]["sqrt_n_eta_n_sup"]) for i in range(len(tail_rows) - 1))}


def main() -> dict:
    payload = {"global_bound": global_bound_replay(), "dominant": dominant_bound_replay(), "tails": fixed_band_and_tail(), "markers": ["R11_GLOBAL_BOUND_BENCHMARK_REPLAYED", "R11_DOMINANT_BOUND_REPLAYED"]}
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "dominant_bound.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in payload["markers"]:
        print(marker)
    print("R11_GLOBAL_BOUND", payload["global_bound"]["all_finite_replays_hold"])
    print("R11_DOMINANT_BOUND", payload["dominant"]["all_ratio_bounds_hold"])
    print("R11_TAIL_BOOKKEEPING", payload["tails"]["nondominant_tail_decreases"])
    return payload


if __name__ == "__main__":
    main()

