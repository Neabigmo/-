"""Aggregate R10 exact replays and retain the conservative B decision."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from derive_angular_moment import beta_moment, direct_moment
from derive_student_kernel import direct_kernel, fixed_band_rows, student_kernel
from replay_normalization import main as normalization_main
from exact_kernel_bound import central_binomial_replay, normalized_multinomial_bound, wiener_tail_replay


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    normalization_main()
    moment_ok = all(sp.simplify(beta_moment(n, s) - direct_moment(n, s)) == 0 for n in (4, 6) for s in range(5))
    kernel_ok = all(sp.simplify(student_kernel(j, k, degree) - direct_kernel(j, k, degree)) == 0 for degree in (4, 6) for j in range(3) for k in range(3 - j))
    fixed = fixed_band_rows()
    fixed_ok = all(row["limit_residual"] == "0" for row in fixed)
    central = central_binomial_replay()
    multinomial = normalized_multinomial_bound()
    tail = wiener_tail_replay()
    tail_ok = tail["tail_decreases_in_replay"] and sp.sympify(tail["rows"][-1]["two_high_bound"]) < 1
    # The file is produced above; inspect its exact residual fields without
    # relying on a hard-coded Gaussian outcome.
    norm = json.loads((RESULTS / "normalization.json").read_text(encoding="utf-8"))
    normalization_ok = norm["R_residual"] == "0" and norm["D_residual"] == "0"
    exact_ok = moment_ok and kernel_ok and fixed_ok and central["all_bounds_hold"] and multinomial["all_multinomial_terms_le_a_star_n"] and tail_ok and normalization_ok
    payload = {"exact_replays_pass": bool(exact_ok), "gaussian_normalization": "R=1,D_R=1", "angular_moment_status": "STUDENT_BETA_EXACT_AND_DIRECT_INTEGRAL_MATCHED" if moment_ok else "FAILED", "kernel_status": "DIRECT_SYMBOLIC_INTEGRAL_MATCHED" if kernel_ok else "FAILED", "fixed_band_status": "LIMITS_AND_FIRST_1_OVER_N_REPLAYED" if fixed_ok else "FAILED", "global_bound_status": "BENCHMARK_ONLY_ACTUAL_STAGE7_FORMULA_NOT_IMPORTED", "wiener_tail_status": "RADIUS_LOSS_FACTOR_REPLAYED" if tail_ok else "FAILED", "stage7_symbol_status": "CANDIDATE_D_R_IDENTIFIED_BUT_UNIFORM_OPERATOR_LIMIT_UNRESOLVED", "decision": "STUDENT_KERNEL_CERTIFIED_OPERATOR_GAP_REMAINS" if exact_ok else "FORMULA_CORRECTION_REQUIRED", "marker": "R10_STAGE7_STUDENT_KERNEL_AUDIT_COMPLETED" if exact_ok else "R10_AUDIT_FAILED", "precise_remaining_gap": "Import the actual Stage7 A_ijk in ordinary coefficients and prove the uniform low-pair tail/operator-norm passage after fixed-band n->infinity."}
    (RESULTS / "r10_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R10_GAUSSIAN_STATUS", payload["gaussian_normalization"])
    print("R10_STUDENT_KERNEL_STATUS", payload["kernel_status"])
    print("R10_SYMBOL_STATUS", payload["stage7_symbol_status"])
    print("R10_DECISION", payload["decision"])
    if not exact_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
