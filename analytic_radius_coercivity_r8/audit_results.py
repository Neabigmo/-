"""Aggregate the bounded R8 audit and make the conservative decision."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from derive_radius_gap_bound import exact_hellinger_cauchy_schwarz, ou_scale_replay, radius_factor_bookkeeping
from replay_endpoint_symbol import endpoint_symbol_replay, fixed_band_replay


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def fredholm_defect_replay() -> dict:
    """Verify the local range conditions for a toy multiplier zero."""
    z, zeta = sp.symbols("z zeta")
    m = 2
    D = (z - zeta) ** m
    source = 1 + 2 * z + 3 * z**2
    image = sp.expand(D * source)
    defects = [sp.diff(image, z, j).subs(z, zeta) for j in range(m)]
    # The two functionals are independent on 1 and (z-zeta).
    probes = [1, z - zeta]
    matrix = sp.Matrix([[sp.diff(probe, z, j).subs(z, zeta) for probe in probes] for j in range(m)])
    return {
        "multiplicity": m,
        "range_defect_residuals": [str(sp.simplify(v)) for v in defects],
        "functional_matrix_rank": int(matrix.rank()),
        "radius_condition": "|zeta| < r",
        "functionals": ["g(zeta)", "g'(zeta)"],
    }


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    radius = radius_factor_bookkeeping()
    endpoint = endpoint_symbol_replay()
    fixed = fixed_band_replay()
    fredholm = fredholm_defect_replay()
    cs = exact_hellinger_cauchy_schwarz()
    ou = ou_scale_replay()
    fredholm = fredholm_defect_replay()
    exact_ok = (
        cs["sum_probability"] == "1"
        and radius["monomial_residual"] == "0"
        and ou["residual"] == "0"
        and endpoint["residual"] == "0"
    )
    fixed_ok = fixed["all_fixed_band_limits_exact"]
    fredholm_ok = (
        fredholm["functional_matrix_rank"] == fredholm["multiplicity"]
        and all(value == "0" for value in fredholm["range_defect_residuals"])
    )
    payload = {
        "exact_replays_pass": bool(exact_ok and fixed_ok),
        "probability_to_analytic_scale": "CONDITIONAL_ON_POSITIVE_RADIUS_HERMITE_MEMBERSHIP",
        "radius_gap_compactness": "CERTIFIED_CONDITIONALLY_ON_H_R_TO_H_r_AND_HELLINGER_BOUND",
        "endpoint_toeplitz": "REPLAYED_FIXED_BAND_AND_CANDIDATE_SYMBOL; FULL_NORMALIZATION_REMAINS",
        "fredholm_zero_status": "EXPLICIT_FUNCTIONALS_WITH_RADIUS_CONDITION; RANGE_IDENTIFICATION_REMAINS",
        "fredholm_defect_replay": fredholm,
        "characteristic_solvability_defects": "Lambda_zeta_j(nonlinear_high_high_remainder + finite_n_correction)=0",
        "positivity_status": "POSITIVITY_ACTION_ON_FREDHOLM_DEFECT_UNRESOLVED",
        "r6_r7_compatibility": "RADIUS_LOSS_IS_NEW_COMPACTNESS_MECHANISM; DOES_NOT_REPAIR_R6_POINTWISE_SIGN_GAP_OR_R7_OPERATOR_COUNTERMODEL",
        "decision": "RADIUS_GAP_COMPACTNESS_CERTIFIED_FREDHOLM_GAP_REMAINS" if exact_ok and fixed_ok and fredholm_ok else "FORMULA_CORRECTION_REQUIRED",
        "marker": "R8_ANALYTIC_RADIUS_AUDIT_COMPLETED" if exact_ok and fixed_ok and fredholm_ok else "R8_AUDIT_FAILED",
    }
    (RESULTS / "r8_audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R8_RADIUS_GAP_COMPACTNESS", payload["radius_gap_compactness"])
    print("R8_FREDHOLM_STATUS", payload["fredholm_zero_status"])
    print("R8_DECISION", payload["decision"])
    if not exact_ok or not fixed_ok or not fredholm_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
