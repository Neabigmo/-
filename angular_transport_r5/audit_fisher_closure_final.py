"""Final bounded audit: transport closes the identity, but not its equality."""

from __future__ import annotations

try:
    from .common import jsonable, no_nonfinite, require, write_json
    from .derive_bivariate_mixture import exact_pair_identity
    from .derive_missing_information import bivariate_identity, scalar_identity
    from .derive_rotation_transport import weak_form_certificate
    from .derive_stage8_bridge import bridge_data
except ImportError:
    from common import jsonable, no_nonfinite, require, write_json
    from derive_bivariate_mixture import exact_pair_identity
    from derive_missing_information import bivariate_identity, scalar_identity
    from derive_rotation_transport import weak_form_certificate
    from derive_stage8_bridge import bridge_data

def closure_obstruction() -> dict[str, object]:
    # Logical witness for inequality directions only; not one common target-law K.
    return {
        "epsilon": "1/5",
        "v_j": ["11/10", "4/5", "4/5"],
        "V_a": "1", "V_b": "4/5", "A_squared": "0", "C_squared": "1/5",
        "J_j": ["10/11", "5/4", "5/4"],
        "component_Cramer_Rao_equalities": True,
        "Stam_sum_equality": True,
        "Poincare_value": "1/360", "Poincare_upper_bound_at_z1": "1/180",
        "gap": "Named scalar budgets hold while C_squared remains 1/5 > 0.",
        "scope_warning": "Logical witness only; not a target-law counterexample.",
    }

def build_audit() -> dict[str, object]:
    payload = {
        "status": "MISSING_INFORMATION_GAP_REMAINS",
        "decision": "B",
        "bivariate_tilted_mixture": exact_pair_identity()["status"],
        "rotation_transport": weak_form_certificate()["status"],
        "scalar_missing_information": scalar_identity()["status"],
        "bivariate_relative_fisher": bivariate_identity()["status"],
        "closure_obstruction": closure_obstruction(),
        "fisher_closure": False,
        "remaining_gap": "MI is exact, but product structure plus Cramer-Rao/Stam gives lower/equality directions, not the missing upper bound that would force H(x)=0.",
        "next_authorized_route": "Stage8 critical Hellinger/parity continuum normal form plus Stage19 backward-heat positivity",
        "stage8_bridge": [bridge_data(d) for d in (3, 5, 7, 9)],
        "no_nonfinite_fields": True,
    }
    normalized = jsonable(payload)
    require(no_nonfinite(normalized), "non-finite audit field")
    return normalized

def run_audit() -> dict[str, object]:
    normalized = build_audit()
    write_json("audit_results.json", normalized)
    return normalized

def main() -> None:
    run_audit()
    print("EXACT_ANGULAR_TRANSPORT_AUDIT_COMPLETED")
    print("MISSING_INFORMATION_GAP_REMAINS")
    print("DECISION_B_MISSING_INFORMATION_GAP_REMAINS_STAGE8_REQUIRED")

if __name__ == "__main__":
    main()
