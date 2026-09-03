"""Run and validate the complete bounded angular Fisher audit."""

from __future__ import annotations

import json
from pathlib import Path

from common import RESULTS, jsonable, no_nonfinite, require, write_json
from derive_angular_geometry import main as geometry_main
from derive_fisher_budget import derive_budget, algebraic_gap_witness
from derive_first_odd_mode import mode_data
from optional_symmetrization import main as parseval_main


def run_audit() -> dict[str, object]:
    geometry_main()
    parseval_main()
    budget = derive_budget()
    witness = algebraic_gap_witness()
    modes = [mode_data(d) for d in (3, 5, 7, 9, 11)]
    require(all(mode["surviving_harmonics"][0] == 3 for mode in modes), "first harmonic is not 3")
    require(witness["C_squared_nonzero"], "gap witness unexpectedly vanished")
    payload = {
        "status": "FISHER_CLOSURE_INSUFFICIENT",
        "decision": "B",
        "exact_geometry": True,
        "tilted_mixture_budget": True,
        "general_first_odd_mode": True,
        "parseval_diagnostic": True,
        "fisher_closure": False,
        "gap_witness": witness,
        "remaining_gap": "No available implication from Cramer-Rao + Stam + D3 Poincare + the polar budget forces E_z[C_z^2]=0. A missing cross-theta equality/transport inequality is required.",
        "recommended_next_route": "Stage8 critical Hellinger/parity continuum normal form with backward-heat positivity",
        "no_nonfinite_fields": True,
        # Exclude the artifact being written; this keeps replay comparison
        # deterministic on a clean run and on subsequent reruns.
        "files_generated": sorted(
            path.name for path in RESULTS.glob("*.json") if path.name != "audit_results.json"
        ),
    }
    require(no_nonfinite(payload), "non-finite serialized field detected")
    # Return the same JSON-normalized object that is persisted so a fresh
    # replay compares bytes-of-meaning, not Python-vs-JSON SymPy wrappers.
    normalized = jsonable(payload)
    write_json("audit_results.json", normalized)
    return normalized


def main() -> None:
    data = run_audit()
    print("EXACT_ANGULAR_FISHER_AUDIT_COMPLETED")
    print("FISHER_CLOSURE_INSUFFICIENT")
    print("DECISION_B_FISHER_CLOSURE_INSUFFICIENT_BUT_NEW_EXACT_LEMMA")


if __name__ == "__main__":
    main()
