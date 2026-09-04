from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from replay_r19 import compute_exact_audit
from audit_r19 import audit


def test_exact_d4_discrepancy_and_low_orders() -> None:
    result = compute_exact_audit()
    assert all(result["low_order_checks"].values())
    assert result["d4_minus_star_over_c2_square"] == "2/3"
    assert result["corrected_d4_residual"] == "0"
    assert result["star_formally_refuted"] is True


def test_result_audit_round_trip() -> None:
    result = compute_exact_audit()
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "r19_audit.json"
        path.write_text(json.dumps(result), encoding="utf-8")
        assert audit(path)["verified"] is True
