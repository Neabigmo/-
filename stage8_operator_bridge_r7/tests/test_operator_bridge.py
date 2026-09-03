from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_operator_bridge_replay() -> None:
    subprocess.run([sys.executable, str(ROOT / "exact_replay.py")], check=True, cwd=ROOT)
    data = json.loads((ROOT / "results" / "operator_bridge.json").read_text(encoding="utf-8"))
    assert data["marker"] == "R7_OPERATOR_BRIDGE_AUDIT_COMPLETED"
    assert data["all_exact_replays"] is True
    assert data["hermite_addition"]["exact_on_sum_a2_eq_1"] is True
    assert data["gram_countermodel"]["gram_psd"] is True
    assert data["gram_countermodel"]["tensor_sign_negative"] is True
    assert data["gram_countermodel"]["cs_bound_residual"] == "-3/4"
