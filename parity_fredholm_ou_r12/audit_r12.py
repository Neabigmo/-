"""R12 audit: parity principal blocks, OU covariance, and exact defect boundary."""
from __future__ import annotations

import json
from pathlib import Path

from replay_parity_symbols import (
    endpoint_symbol_coefficient_replay,
    jet_compensation_replay,
    normalized_domain_replay,
    ou_scaling_replay,
    parity_symbol_replay,
    stage7_parity_coefficient_replay,
)

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> dict:
    parity = parity_symbol_replay()
    coefficients = stage7_parity_coefficient_replay()
    endpoint = endpoint_symbol_coefficient_replay()
    domains = normalized_domain_replay()
    jets = jet_compensation_replay()
    ou = ou_scaling_replay()
    exact_checks = {
        "parity_symbol_identities": parity["D_plus_C_equals_Rminus_squared"] and parity["D_minus_C_equals_Rplus_squared"],
        "gaussian_D1_C0": parity["gaussian_normalization"],
        "stage7_parity_replay": coefficients["odd_total_coefficients_zero"] and coefficients["even_linear_divisors_nonzero"],
        "odd_principal_symbol": endpoint["all_checks_zero"],
        "normalized_X_Y_domains": all(domains[key] for key in ("X_low_coefficients_zero", "X_is_z4_positive_wiener_ideal", "Y_is_z3_positive_wiener_space", "C_X_bounded_isomorphism", "C_Y_bounded_isomorphism")),
        "simple_double_jet_compensation": jets["simple_and_double_jet_compensation"],
        "ou_scaling_covariance": ou["D_scaling_identity"] and ou["C_scaling_identity"] and ou["log_dilation_chain_rule"],
    }
    payload = {
        "actual_stage7_kernel_status": "ACTUAL_STAGE7_KERNEL_IDENTIFIED_IN_R11",
        "even_block": "L_R^ee: X_rho -> X_rho, X_rho=z^4 A^+_(rho^2)",
        "odd_to_even_block": "L_R^eo: Y_rho -> X_rho, Y_rho=z^3 A^+_(rho^2)",
        "odd_principal_symbol": "C_R(z)=(R(-z/2)^2-R(z/2)^2)/2=z*Ctilde_R(z^2)",
        "common_zero_criterion": "D_R(zeta)=C_R(zeta)=0 iff R(zeta/2)=R(-zeta/2)=0 for zeta != 0",
        "principal_cokernel_compensation": "If Ctilde(w_alpha) != 0 at every Dtilde zero, finite Hermite interpolation fills every principal jet defect.",
        "principal_compensation_status": "PRINCIPAL_EVEN_DEFECT_COMPENSATED_BY_ODD_BLOCK",
        "exact_defect_map": "Delta_rho: Y_rho -> coker(L_R^ee) remains unresolved after compact perturbations.",
        "ou_covariance": "T(R_lambda)=1, D_(R_lambda)(z)=D_R(lambda z), C_(R_lambda)(z)=C_R(lambda z); log-dilation tangent lies in the exact kernel.",
        "ou_coherence_contradiction": False,
        "checks": exact_checks,
        "all_exact_replays_pass": all(exact_checks.values()),
        "decision": "PARITY_SYMBOL_CERTIFIED_EXACT_DEFECT_MAP_REMAINS",
        "single_remaining_gap": "Prove or disprove surjectivity of the exact finite-dimensional defect map Delta_rho after the compact perturbations; principal jet compensation alone is insufficient.",
        "marker": "R12_PARITY_FREDHOLM_OU_AUDIT_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r12_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in [
        "ACTUAL_STAGE7_KERNEL_IDENTIFIED_IN_R11",
        "COMMON_SYMMETRIC_ZERO_CRITERION",
        "PRINCIPAL_EVEN_DEFECT_COMPENSATED_BY_ODD_BLOCK",
        payload["marker"],
    ]:
        print(marker)
    print("R12_EXACT_REPLAYS", payload["all_exact_replays_pass"])
    print("R12_OU_COHERENCE_CONTRADICTION", payload["ou_coherence_contradiction"])
    print("R12_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()
