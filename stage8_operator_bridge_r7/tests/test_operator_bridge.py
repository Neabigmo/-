from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from exact_replay import coherent_replay, gram_and_countermodel, hermite_addition_replay  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def test_operator_bridge_replay() -> None:
    hermite = hermite_addition_replay()
    coherent = coherent_replay()
    gram = gram_and_countermodel()
    assert hermite["residual_on_sphere"] == "0"
    assert coherent["normalization_residual"] == "0"
    assert coherent["parity_character_count"] == len(coherent["parity_characters"]) == 4
    assert gram["mixed"] == "-1/2"
    assert gram["tensor_mixed"] == "-1/2"
    assert gram["cs_bound_residual"] == "-3/4"

    subprocess.run([sys.executable, str(ROOT / "exact_replay.py")], check=True, cwd=ROOT)
    data = json.loads((ROOT / "results" / "operator_bridge.json").read_text(encoding="utf-8"))
    assert data["marker"] == "R7_OPERATOR_BRIDGE_AUDIT_COMPLETED"
    assert data["all_exact_replays"] is True
    assert data["hermite_addition"]["exact_on_sum_a2_eq_1"] is True
    assert data["gram_countermodel"]["gram_psd"] is True
    assert data["gram_countermodel"]["tensor_sign_negative"] is True
    assert data["gram_countermodel"]["cs_bound_residual"] == "-3/4"
    assert data["global_r5_bridge"]["algebraic_identity_exact"] is True
    assert "assumptions remain open" in data["global_r5_bridge"]["status"]
