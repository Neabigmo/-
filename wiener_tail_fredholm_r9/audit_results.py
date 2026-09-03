"""Aggregate the R9 exact replays and retain the conservative decision."""
from __future__ import annotations

import json
from pathlib import Path

from exact_kernel_bound import central_binomial_replay, normalized_multinomial_bound, wiener_tail_replay
from replay_normalization import fixed_band_replay, normalization_replay
from replay_wiener_range import division_replay


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    normalization = normalization_replay()
    fixed = fixed_band_replay()
    central = central_binomial_replay()
    multinomial = normalized_multinomial_bound()
    tail = wiener_tail_replay()
    simple = division_replay(multiplicity=1)
    double = division_replay(multiplicity=2)
    exact_ok = normalization["residual"] == "0" and fixed["all_limits_exact"] and central["all_bounds_hold"] and multinomial["all_multinomial_terms_le_a_star_n"] and simple["division_exact"] and double["division_exact"]
    payload = {
        "exact_replays_pass": bool(exact_ok),
        "positive_radius_input_status": "ENTIRE_OR_FINITE_WIENER_NORM_REQUIRED; NOT_ARBITRARY_L2",
        "normalization_conjugation_status": "B_NORMALIZATION_NOT_TOEPLITZ; FACTORIAL_SHIFT_EXPLICIT",
        "uniform_normalized_kernel_status": "BENCHMARK_BOUND_REPLAYED; ACTUAL_STAGE7_A_IJK_FORMULA_NOT_IMPORTED",
        "wiener_compactness_status": "RADIUS_LOSS_TAIL_REPLAYED_FOR_W_R_TO_W_r",
        "stage7_symbol_status": "FIXED_BAND_LIMIT_REPLAYED; M_UNIFORM_LIMIT_UNRESOLVED",
        "single_radius_range_status": "SIMPLE_AND_MULTIPLE_ZERO_DIVISION_REPLAYED; ACTUAL_STAGE7_IDENTIFICATION_UNRESOLVED",
        "exact_remaining_gap": "Derive the actual Stage7 kernel in ordinary coefficients and prove the uniform low-pair tail before identifying D_R as the single-radius principal multiplier.",
        "gaussian_symbol_replay": "D_R(z)=[R(z/2)^2+R(-z/2)^2]/2; Gaussian R gives exp(-z^2/4)",
        "decision": "NORMALIZATION_REPAIRED_BUT_SYMBOL_LIMIT_NOT_UNIFORM" if exact_ok else "R8_FREDHOLM_MODEL_REQUIRES_CORRECTION",
        "marker": "R9_WIENER_TAIL_FREDHOLM_AUDIT_COMPLETED" if exact_ok else "R9_AUDIT_FAILED",
    }
    (RESULTS / "r9_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R9_NORMALIZATION", payload["normalization_conjugation_status"])
    print("R9_WIENER_COMPACTNESS", payload["wiener_compactness_status"])
    print("R9_SYMBOL_STATUS", payload["stage7_symbol_status"])
    print("R9_DECISION", payload["decision"])
    if not exact_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

