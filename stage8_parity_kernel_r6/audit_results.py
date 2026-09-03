"""Audit only the small exact reports emitted by the three replay scripts."""
from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def finite_tree(value):
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, dict):
        return all(finite_tree(v) for v in value.values())
    if isinstance(value, list):
        return all(finite_tree(v) for v in value)
    return True


def main() -> None:
    expected = {
        "parity_algebra.json": "PARITY_HADAMARD_FACTORIZATION_CERTIFIED",
        "interior_lclt.json": "INTERIOR_HELLINGER_LCLT_NORMALIZATION_CERTIFIED",
        "backward_heat_matching.json": "BACKWARD_HEAT_SIGN_TRANSFER_REQUIRES_EXTRA_IDENTIFICATION",
    }
    checks = {}
    for name, marker in expected.items():
        path = RESULTS / name
        data = json.loads(path.read_text(encoding="utf-8"))
        checks[name] = {
            "exists": True,
            "marker_matches": data.get("marker") == marker,
            "finite": finite_tree(data),
        }
        if name == "parity_algebra.json":
            checks[name]["residual_zero"] = data.get("identity_residual") == "0"
            checks[name]["factorization_exact"] = data.get("factorization_exact") is True
        elif name == "interior_lclt.json":
            checks[name]["normalization_exact"] = data.get("normalization_exact") is True
            checks[name]["simplex_normalization"] = data.get("normalization_on_p_simplex") == "1"
            checks[name]["scale_consistent"] = data.get("raw_deviation_exponent") == "7/12"
        else:
            checks[name]["mehler_residual_zero"] = data.get("mehler_series_residual_through_degree_3") == "0"
            checks[name]["gaussian_residual_zero"] = data.get("gaussian_positive_replay_residual") == "0"
            checks[name]["gaussian_factorization_value"] = data.get("gaussian_phi") == "14" and data.get("gaussian_factorized_phi") == "14"
            checks[name]["r5_replay_exact"] = data.get("r5_replay_all_exact") is True
            checks[name]["r5_factors_present"] = all("rho**" in row.get("coefficient", "") and "kappa" in row.get("coefficient", "") for row in data.get("r5_low_mode_rows", []))
            checks[name]["gap_declared"] = "not yet uniformly identified" in data.get("sign_transfer_reason", "")
    passed = all(all(item.values()) for item in checks.values())
    payload = {
        "checks": checks,
        "passed": passed,
        "decision": "B: BACKWARD_HEAT_SIGN_TRANSFER_FAILS_AT_CURRENT_INTERFACE",
        "precise_gap": "Need a uniform double-scaling identification from Stage-8 local parity profiles to paired backward-heat amplitudes, including sign/location normalization and l2 tail tightness.",
        "marker": "R6_AUDIT_COMPLETED" if passed else "R6_AUDIT_FAILED",
    }
    (RESULTS / "audit_results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R6_DECISION", payload["decision"])
    print("R6_AUDIT_PASSED", passed)


if __name__ == "__main__":
    main()
