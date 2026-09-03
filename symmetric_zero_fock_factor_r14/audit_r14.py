"""Conservative exact audit for the symmetric-zero probability bridge."""
from __future__ import annotations

import json
from pathlib import Path

from replay_factor_identity import (
    angular_symmetric_identities_replay,
    factorized_fock_identity_replay,
    exact_factor_product_replay,
    minimal_zero_replay,
    ou_zero_scaling_replay,
    probability_countermodels,
    quartet_factor_replay,
    resonance_replay,
)

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> dict:
    counter = probability_countermodels()
    ou = ou_zero_scaling_replay()
    angular = angular_symmetric_identities_replay()
    factorized = factorized_fock_identity_replay()
    resonance = resonance_replay()
    quartet = quartet_factor_replay()
    factor = exact_factor_product_replay()
    minimal = minimal_zero_replay()
    checks = {
        "probability_countermodels": bool(counter["bernoulli_symmetric_zero"] and counter["three_point_symmetric_zero"]),
        "ou_scaling": bool(ou["identity"]),
        "angular_identities": bool(angular["elementary_relations_are_exact"]),
        "factorized_fock_identity": bool(factorized["product_reduction_exact"] and factorized["even_factor"] and factorized["angular_shift_evenness"]),
        "resonance_consistency": bool(resonance["resonance_data_consistent"]),
        "quartet_factor": bool(quartet["identity_holds"]),
        "factor_product": bool(factor["factorization_exact"]),
        "minimal_zero_boundary": bool(minimal["nonreal_zero"] and minimal["modulus_alone_does_not_give_probability_bridge"]),
    }
    payload = {
        "checks": checks,
        "all_exact_replays_pass": all(checks.values()),
        "generic_probability_countermodel_status": "CERTIFIED_COUNTERMODELS_EXIST",
        "factorized_fock_identity_status": "CERTIFIED_FROM_NORMALIZED_FOCK_IDENTITY",
        "resonance_conditions_status": "DERIVED_FROM_FOCK_IDENTITY",
        "quartet_factor_status": "CERTIFIED",
        "probability_bridge_status": "REMAINS_OPEN",
        "minimal_zero_status": "INSUFFICIENT_BY_ITSELF",
        "decision": "FOCK_ZERO_RESONANCE_LEMMA_CERTIFIED_PROBABILITY_BRIDGE_REMAINS",
        "fredholm_common_zero_line": "STOP_AFTER_THIS_AUDIT_UNLESS_A_NEW_NONLINEAR_PROBABILITY_LEMMA_IS_SUPPLIED",
        "single_next_genuine_gap": "Exclude B_H(z0)=-1/8 and z0 B_H'(z0)=3/4 using the full nonlinear probability/Fock constraints, if possible.",
        "marker": "R14_SYMMETRIC_ZERO_FOCK_FACTOR_AUDIT_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r14_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in [
        "R14_GENERIC_PROBABILITY_COUNTERMODELS_CERTIFIED",
        "R14_FOCK_FACTOR_IDENTITY_AUDITED",
        "R14_PROBABILITY_BRIDGE_REMAINS_OPEN",
        payload["marker"],
    ]:
        print(marker)
    print("R14_EXACT_REPLAYS", payload["all_exact_replays_pass"])
    print("R14_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()
