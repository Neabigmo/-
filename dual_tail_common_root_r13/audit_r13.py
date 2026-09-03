"""R13 audit of the dual-tail route and its explicit remaining hypothesis."""
from __future__ import annotations

import json
from pathlib import Path

from replay_tail_locality import (
    common_root_spectral_toy_replay,
    finite_support_dual_replay,
    lower_triangular_replay,
    tail_locality_sufficient_bound_replay,
    tail_normalization_selection_replay,
)

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> dict:
    lower = lower_triangular_replay()
    tail = tail_locality_sufficient_bound_replay()
    selection = tail_normalization_selection_replay()
    finite = finite_support_dual_replay()
    spectral = common_root_spectral_toy_replay()
    checks = {
        "lower_triangular_exact_diagonal": bool(lower["exact_diagonal_one"] and lower["lower_triangular"]),
        "synthetic_tail_bound": bool(tail["finite_model_bound_holds"]),
        "tail_selection": bool(selection["all_selected_ratio_at_least_half"] and selection["selection_is_strictly_increasing"]),
        "finite_support_dual": bool(finite["finite_support_nonzero_contradiction"]),
        "common_root_spectral_toy": bool(spectral["common_case_has_root"] and spectral["disjoint_case_has_no_common_root"]),
    }
    payload = {
        "actual_stage7_kernel_status": "ACTUAL_STAGE7_KERNEL_IDENTIFIED_IN_R11",
        "dual_annihilator_status": "DUAL_DEFECT_CHARACTERIZATION_FORMALIZED",
        "tail_normalized_limit_status": "TAIL_NORMALIZATION_SELECTION_LEMMA_REPLAYED",
        "simultaneous_recurrence_status": "CONDITIONAL_ON_TAIL_LOCAL_REMAINDER",
        "common_root_spectral_status": "COMMON_ROOT_REDUCTION_CONDITIONAL_ON_TAIL_LOCALITY",
        "checks": checks,
        "all_replays_pass": all(checks.values()),
        "tail_local_remainder_status": "TAIL_LOCAL_REMAINDER_LEMMA_NOT_DERIVED_FROM_R11_COMPACTNESS",
        "exact_defect_map_status": "UNRESOLVED_UNTIL_TAIL_LOCALITY_IS_PROVED",
        "decision": "TAIL_LOCALITY_GAP",
        "single_remaining_gap": "Prove the relative high-column estimate for K_e^* and K_o^* after division by the dual tail envelope b_i; R11 compactness alone is insufficient.",
        "marker": "R13_DUAL_TAIL_COMMON_ROOT_AUDIT_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r13_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in [
        payload["dual_annihilator_status"],
        payload["tail_normalized_limit_status"],
        payload["common_root_spectral_status"],
        payload["marker"],
    ]:
        print(marker)
    print("R13_EXACT_REPLAYS", payload["all_replays_pass"])
    print("R13_TAIL_LOCAL_REMAINDER", payload["tail_local_remainder_status"])
    print("R13_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()
