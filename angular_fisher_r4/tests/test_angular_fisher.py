from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def run(script: str) -> str:
    return subprocess.check_output([sys.executable, str(ROOT / script)], cwd=ROOT, text=True)


def test_exact_geometry_and_modes() -> None:
    out = run("derive_angular_geometry.py")
    assert "EXACT_D3_GEOMETRY_VERIFIED" in out
    run("derive_first_odd_mode.py")
    data = json.loads((ROOT / "results" / "first_odd_mode.json").read_text(encoding="utf-8"))
    assert data["status"] == "EXACT_FIRST_ODD_MODE_FORMULAS_VERIFIED"
    assert data["cases"][0]["surviving_harmonics"] == [3]
    assert data["cases"][1]["surviving_harmonics"] == [3]


def test_fisher_budget_and_gap_witness() -> None:
    out = run("derive_fisher_budget.py")
    assert "FISHER_STAM_POINCARE_ALGEBRAIC_GAP_WITNESS_VERIFIED" in out
    data = json.loads((ROOT / "results" / "fisher_budget.json").read_text(encoding="utf-8"))
    witness = data["gap_witness"]
    assert witness["C_squared_nonzero"] is True
    assert sp.Rational(witness["V_a"]) == 1
    assert sp.Rational(witness["V_b"]) == sp.Rational(4, 5)


def test_full_audit_replay() -> None:
    run("audit_results.py")
    data = json.loads((ROOT / "results" / "audit_results.json").read_text(encoding="utf-8"))
    assert data["decision"] == "B"
    assert data["fisher_closure"] is False
    assert data["no_nonfinite_fields"] is True

