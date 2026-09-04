from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def test_result_exists_and_has_conservative_status():
    data = json.loads((ROOT / "results" / "r20_tv_audit.json").read_text())
    assert data["status"].startswith("TV_NOT_CERTIFIED")
    assert data["rademacher_tv_strictly_fails_for_a_nonzero"] is True


def test_exact_jet_values():
    data = json.loads((ROOT / "results" / "r20_tv_audit.json").read_text())
    assert sp.sympify(data["forced_h4"]) == 0
    assert sp.sympify(data["compatible_h6"]) == -sp.Rational(3, 20) * sp.Symbol("h3") ** 2
