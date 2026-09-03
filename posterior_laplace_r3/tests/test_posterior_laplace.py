from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from audit_results import validate_artifacts


def test_exact_pipeline_in_isolated_artifact_dir():
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["LAPLACE_RESULTS_DIR"] = tmp
        proc = subprocess.run([sys.executable, str(ROOT / "run_posterior_laplace.py")], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
        if proc.returncode != 0:
            raise AssertionError(proc.stderr)
        summary = json.loads((Path(tmp) / "posterior_laplace_run_summary.json").read_text(encoding="utf-8"))
        if summary["final_outcome"] != "EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE":
            raise AssertionError(summary)
        moments = json.loads((Path(tmp) / "conditional_q_moments.json").read_text(encoding="utf-8"))
        if not all(v == "0" for v in moments["conditional_moment_residuals"].values()):
            raise AssertionError(moments)
        bridge = json.loads((Path(tmp) / "semigroup_bridge.json").read_text(encoding="utf-8"))
        if bridge["Gaussian_K_y_independent"] is not True:
            raise AssertionError(bridge)


def test_audit_rejects_tampered_exact_artifact():
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["LAPLACE_RESULTS_DIR"] = tmp
        proc = subprocess.run([sys.executable, str(ROOT / "run_posterior_laplace.py")], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
        if proc.returncode != 0:
            raise AssertionError(proc.stderr)
        data = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in Path(tmp).glob("*.json") if p.name != "audit_results.json"}
        data["critical_kernel_audit.json"]["exact_K"] = "fabricated"
        with pytest.raises(RuntimeError):
            validate_artifacts(data)


def test_optimized_runner_preserves_verification_gates():
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["LAPLACE_RESULTS_DIR"] = tmp
        proc = subprocess.run([sys.executable, "-O", str(ROOT / "run_posterior_laplace.py")], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
        if proc.returncode != 0:
            raise AssertionError(proc.stderr)
        audit = json.loads((Path(tmp) / "audit_results.json").read_text(encoding="utf-8"))
        if audit.get("fresh_regeneration") is not True:
            raise AssertionError(audit)


def test_critical_kernel_matches_independent_quadrature():
    mp.mp.dps = 50
    phi = lambda variance, z: mp.exp(-(z*z)/(2*variance)) / mp.sqrt(2*mp.pi*variance)
    pv = lambda x: (phi(1, x + 1) + phi(1, x - 1)) / 2
    pt0 = (phi(2, 1) + phi(2, -1)) / 2
    numerator = mp.quad(lambda x: phi(mp.mpf(1)/3, -x) * pv(x)**3, [-mp.inf, mp.inf])
    measured = numerator / pt0**3
    expected = mp.mpf(1)/2 + mp.mpf(3)/2 * mp.exp(-mp.mpf(2)/3)
    if abs(measured - expected) > mp.mpf("1e-35"):
        raise AssertionError((measured, expected))
