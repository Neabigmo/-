from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from common import result_dir


ROOT = Path(__file__).resolve().parent
REQUIRED = [
    "posterior_triple.json",
    "conditional_q_moments.json",
    "moment_countermodel.json",
    "semigroup_bridge.json",
    "critical_kernel_audit.json",
]


def validate_artifacts(data):
    """Validate values, not merely marker strings or file names."""
    text = json.dumps(data, ensure_ascii=False)
    if "NaN" in text or "Infinity" in text:
        raise RuntimeError("NaN/Infinity found in exact artifacts")
    missing = [name for name in REQUIRED if name not in data]
    if missing:
        raise RuntimeError(f"missing artifacts: {missing}")

    triple = data["posterior_triple.json"]
    if triple.get("status") != "EXACT_POSTERIOR_TRIPLE_LAPLACE_IDENTITY":
        raise RuntimeError("posterior triple status mismatch")
    if triple.get("quadratic_decomposition_residual") != "0":
        raise RuntimeError("posterior triple decomposition is not exact")
    if triple.get("laplace_normalization_residual") != "0":
        raise RuntimeError("posterior triple Laplace residual is not zero")
    if triple.get("chi2_target_laplace_status") != "CONDITIONAL_ON_Q_LAW":
        raise RuntimeError("conditional target-law status missing")

    moments = data["conditional_q_moments.json"]
    if moments.get("status") != "EXACT_CONDITIONAL_Q_MOMENTS":
        raise RuntimeError("conditional moment status mismatch")
    residuals = moments.get("conditional_moment_residuals", {})
    if set(residuals) != {"1", "2", "3", "4"} or any(v != "0" for v in residuals.values()):
        raise RuntimeError(f"conditional moment residual mismatch: {residuals}")
    expected_target = {"1": "2*a", "2": "8*a**2", "3": "48*a**3", "4": "384*a**4"}
    if moments.get("target_Q_moments") != expected_target:
        raise RuntimeError("target Q moments mismatch")

    counter = data["moment_countermodel.json"]
    if counter.get("status") != "EXACT_MOMENT_RELAXATION_COUNTERMODEL":
        raise RuntimeError("countermodel status mismatch")
    if counter.get("V_moments") != {"1": "1", "2": "3/2", "3": "27/8", "4": "81/8"}:
        raise RuntimeError("countermodel V moments mismatch")
    if counter.get("Q_moments") != {"1": "2", "2": "8", "3": "48", "4": "384"}:
        raise RuntimeError("countermodel Q moments mismatch")
    if counter.get("P_Q_zero") != "1/3" or counter.get("Var_V") != "1/2":
        raise RuntimeError("countermodel scalar checks mismatch")

    bridge = data["semigroup_bridge.json"]
    if bridge.get("status") != "EXACT_POSTERIOR_SEMIGROUP_BRIDGE":
        raise RuntimeError("semigroup bridge status mismatch")
    if bridge.get("prefactor_residual") != "0" or bridge.get("complete_gaussian_integral_checks") != 8 or bridge.get("Gaussian_K_y_independent") is not True:
        raise RuntimeError("semigroup bridge exact checks mismatch")

    kernel = data["critical_kernel_audit.json"]
    if kernel.get("status") != "EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE":
        raise RuntimeError("critical-kernel status mismatch")
    if kernel.get("exact_K") != "1/2 + 3*exp(-2/3)/2":
        raise RuntimeError("critical-kernel exact value mismatch")
    if kernel.get("strict_exact_comparison") != "K < 3/2":
        raise RuntimeError("critical-kernel comparison mismatch")


def regenerate_and_load():
    with tempfile.TemporaryDirectory(prefix="posterior_laplace_audit_") as tmp:
        env = os.environ.copy()
        env["LAPLACE_RESULTS_DIR"] = tmp
        scripts = [
            "derive_posterior_triple.py",
            "derive_conditional_q_moments.py",
            "certify_moment_countermodel.py",
            "derive_semigroup_bridge.py",
            "audit_critical_kernel.py",
        ]
        rows = []
        for script in scripts:
            proc = subprocess.run(
                [sys.executable, str(ROOT / script)],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            rows.append({"script": script, "returncode": proc.returncode, "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()})
            if proc.returncode != 0:
                raise RuntimeError(f"fresh regeneration failed: {rows}")
        data = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in Path(tmp).glob("*.json")}
        validate_artifacts(data)
        return rows


def main():
    out_dir = result_dir()
    rows = regenerate_and_load()
    out = {
        "status": "AUDIT_OK",
        "required_files": REQUIRED,
        "fresh_regeneration": True,
        "regeneration": rows,
        "nan_inf_free": True,
    }
    (out_dir / "audit_results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("POSTERIOR_LAPLACE_RESULTS_AUDIT_OK", out_dir / "audit_results.json")


if __name__ == "__main__":
    main()
