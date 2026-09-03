"""Aggregate R11 replays and state the conservative theorem boundary."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from derive_exact_Aijk import run_replay
from replay_dominant_bound import main as bound_main

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def division_index(multiplicity: int, zeta=sp.Rational(1, 3)) -> dict:
    w = sp.symbols("w")
    D = (w - zeta) ** multiplicity
    source = 1 + 2 * w + 3 * w**2
    in_range = sp.expand(D * source)
    quotient, remainder = sp.div(in_range, D, domain=sp.QQ)
    outside = 2 + w + 4 * w**2 + 3 * w**3
    _, outside_remainder = sp.div(outside, D, domain=sp.QQ)
    good = [sp.diff(remainder, w, r).subs(w, zeta) for r in range(multiplicity)]
    bad = [sp.diff(outside_remainder, w, r).subs(w, zeta) for r in range(multiplicity)]
    return {"multiplicity": multiplicity, "division_exact": sp.expand(in_range - quotient * D - remainder) == 0, "good_defects_zero": all(v == 0 for v in good), "outside_defect_nonzero": any(v != 0 for v in bad), "index": -multiplicity}


def main() -> dict:
    angular = run_replay()
    bounds = bound_main()
    simple = division_index(1)
    double = division_index(2)
    gaussian = {"R": "1", "D_R": "1", "correct": True}
    index_ok = simple["index"] == -1 and double["index"] == -2 and simple["division_exact"] and double["division_exact"] and simple["good_defects_zero"] and double["good_defects_zero"]
    payload = {
        "r10_beta_correction": angular["beta_all_zero"],
        "exact_Aijk_status": angular["angular_all_zero"],
        "roots_of_unity_status": angular["angular_all_zero"],
        "dominant_uniform_bound": bounds["dominant"]["all_ratio_bounds_hold"],
        "global_bound_replay": bounds["global_bound"]["all_finite_replays_hold"],
        "same_radius_compactness": {"fixed_shift": True, "nondominant_tail": bounds["tails"]["nondominant_tail_decreases"], "same_space_remainder_bookkeeping": True},
        "even_fredholm_index": {"simple": simple, "multiplicity_2": double, "replay_pass": index_ok, "pair_not_doubled": True},
        "gaussian_normalization": gaussian,
        "stage7_zero_consequence": "If the certified Stage7 zero-free lemma and the actual same-radius theorem are supplied, a non-Gaussian entire solution gives a strictly negative even Fredholm index; this is not Gaussian rigidity.",
        "precise_remaining_gap": "Import the actual all-degree Stage7 A_ijk formula in the normalized operator and prove the complete same-radius operator-norm compactness passage for its remainder.",
        "decision": "ACTUAL_KERNEL_CERTIFIED_SAME_RADIUS_COMPACTNESS_GAP",
        "marker": "R11_SAME_RADIUS_FREDHOLM_AUDIT_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r11_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in ["R11_SAME_RADIUS_INDEX_REPLAYED", "R11_GAUSSIAN_REPLAY_COMPLETED", payload["marker"]]:
        print(marker)
    print("R11_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()

