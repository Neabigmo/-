from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def run(script: str) -> None:
    subprocess.run([sys.executable, str(ROOT / script)], check=True, cwd=ROOT)


def test_exact_replays_and_audit() -> None:
    run("derive_parity_algebra.py")
    run("derive_interior_lclt.py")
    run("derive_backward_heat_matching.py")
    run("audit_results.py")
    audit = json.loads((RESULTS / "audit_results.json").read_text(encoding="utf-8"))
    assert audit["passed"] is True
    assert audit["decision"] == "B: BACKWARD_HEAT_SIGN_TRANSFER_FAILS_AT_CURRENT_INTERFACE"
    assert audit["checks"]["parity_algebra.json"]["residual_zero"] is True
    assert audit["checks"]["interior_lclt.json"]["scale_consistent"] is True
    assert audit["checks"]["backward_heat_matching.json"]["r5_replay_exact"] is True
    assert audit["checks"]["backward_heat_matching.json"]["gaussian_factorization_value"] is True
    assert audit["checks"]["backward_heat_matching.json"]["r5_factors_present"] is True
