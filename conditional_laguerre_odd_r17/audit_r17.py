"""Run the small exact R17 audit and fail on any checked identity."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from replay_r17 import run_all


def main():
    result = run_all()
    checks = [
        result["laguerre_orthogonality"]["verified"],
        result["laguerre_generating_function"]["verified"],
        result["laguerre_product"]["verified"],
        result["tilted_mean_coefficients"]["verified"],
        result["conditional_second_coefficients"]["verified"],
        result["target_moment_eliminations"]["verified"],
        result["triangularity"]["verified"],
        result["fisher_dictionary"]["verified"],
    ]
    if not all(checks):
        raise SystemExit("R17 exact audit failed")
    out = Path(__file__).resolve().parent / "results" / "r17_audit.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
    print("LAGUERRE_PARSEVAL_BRIDGE VERIFIED")
    print("TILTED_MEAN_GENERATING_FUNCTION VERIFIED")
    print("CONDITIONAL_VARIANCE_REALIZABILITY RECORDED")
    print("R16_FISHER_DICTIONARY VERIFIED")
    print("CUBE_ROOT_REDUNDANCY_AUDIT RECORDED")
    print("DECISION B")
    print("LAGUERRE_ODD_BRIDGE_CERTIFIED_INFINITE_POSITIVITY_GAP_REMAINS")
    print("R17_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
