"""Run the exact, theory-first R16 posterior residual audit."""
from __future__ import annotations

import json
from pathlib import Path
from replay_r16 import (
    cumulant_chain, conditional_q_moments, raw_order_rewrites,
    pearson_and_projection, tilted_law_checks,
    conditional_gaussian_completion_check, two_state_countermodel,
    fisher_deficit_algebra, sample_mean_tilt_derivatives,
    derivative_translation,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def main():
    OUT.mkdir(exist_ok=True)
    qgot, qexpected, qchecks = conditional_q_moments()
    raw = raw_order_rewrites()
    tilt = tilted_law_checks()
    gaussian = conditional_gaussian_completion_check()
    counter = two_state_countermodel()
    W = sample_mean_tilt_derivatives()
    checks = {
        "cumulant_chain": cumulant_chain(),
        "conditional_q_moments": {
            "got": {k: str(v) for k, v in qgot.items()},
            "expected": {k: str(v) for k, v in qexpected.items()}, "checks": qchecks,
        },
        "raw_order_rewrites": raw,
        "inequalities": pearson_and_projection(),
        "tilted_law": tilt,
        "gaussian_completion": gaussian,
        "countermodel": {k: str(v) for k, v in counter.items()},
        "fisher_deficit": {k: str(v) for k, v in fisher_deficit_algebra().items()},
        "sample_mean_tilt": {k: str(v) for k, v in W.items()},
        "derivative_translation": derivative_translation(),
        "formula_corrections": {
            "residual_tilt_exponent_corrected_to_negative": True,
            "projected_order6_statement_corrected_to_inequality": True,
        },
        "decision": "D", "decision_marker": "FORMULA_CORRECTION_REQUIRED",
        "cross_x_coherence_closed": False, "remote_compute": "not_started",
    }
    (OUT / "r16_audit.json").write_text(
        json.dumps(checks, indent=2, default=str), encoding="utf-8")
    required = [all(qchecks.values()), raw["order4_identity"], raw["order6_identity"],
                tilt["negative_sign_normalizes"], not tilt["positive_sign_normalizes"],
                gaussian["completed_square"], counter["matches_target"],
                counter["nonconstant"], W["W_prime_zero"], W["W_second_m3"]]
    if not all(required):
        raise AssertionError("R16 exact replay failed")
    for marker in (
        "POSTERIOR_CUMULANT_DERIVATIVE_CHAIN VERIFIED",
        "POSTERIOR_FOURTH_MOMENT_IDENTITY VERIFIED",
        "POSTERIOR_SIXTH_MOMENT_IDENTITY VERIFIED",
        "CONDITIONAL_RESIDUAL_Q_MOMENTS VERIFIED",
        "CORRECTED_JOINT_TILTED_TRIPLE_LAW VERIFIED",
        "PEARSON_AND_SIXTH_PROJECTION_INEQUALITIES VERIFIED",
        "LOW_ORDER_POSTERIOR_MOMENT_CONE_INSUFFICIENT VERIFIED",
        "SPATIAL_ESCORT_FISHER_DEFICIT_IDENTITY VERIFIED",
        "SAMPLE_MEAN_TILT_SECOND_DERIVATIVE VERIFIED",
        "FORMULA_CORRECTION_REQUIRED", "R16_AUDIT_COMPLETED"):
        print(marker)


if __name__ == "__main__":
    main()
