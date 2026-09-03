from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(script: str) -> str:
    return subprocess.check_output([sys.executable, str(ROOT / script)], cwd=ROOT, text=True)

def test_bivariate_and_transport() -> None:
    assert "EXACT_BIVARIATE_TILTED_MIXTURE_VERIFIED" in run("derive_bivariate_mixture.py")
    assert "WEAK_FORM_CONTINUITY_EQUATION_VERIFIED" in run("derive_rotation_transport.py")

def test_missing_information_and_bridge() -> None:
    assert "EXACT_MIXTURE_MISSING_INFORMATION_IDENTITY_VERIFIED" in run("derive_missing_information.py")
    run("derive_stage8_bridge.py")
    data = json.loads((ROOT / "results" / "stage8_bridge.json").read_text(encoding="utf-8"))
    assert data["cases"][0]["harmonics"] == [3]
    assert data["cases"][1]["harmonics"] == [3]

def test_final_audit_replay() -> None:
    run("run_angular_transport.py")
    data = json.loads((ROOT / "results" / "audit_results.json").read_text(encoding="utf-8"))
    assert data["decision"] == "B"
    assert data["fisher_closure"] is False
    assert data["scalar_missing_information"] == "EXACT_POSTERIOR_ANGLE_FISHER_VERIFIED"
