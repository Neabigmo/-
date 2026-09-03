from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_exact_pipeline_in_isolated_artifact_dir():
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["LAPLACE_RESULTS_DIR"] = tmp
        proc = subprocess.run([sys.executable, str(ROOT / "run_posterior_laplace.py")], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
        assert proc.returncode == 0, proc.stderr
        summary = json.loads((Path(tmp) / "posterior_laplace_run_summary.json").read_text(encoding="utf-8"))
        assert summary["final_outcome"] == "EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE"
        moments = json.loads((Path(tmp) / "conditional_q_moments.json").read_text(encoding="utf-8"))
        assert all(v == "0" for v in moments["conditional_moment_residuals"].values())
        bridge = json.loads((Path(tmp) / "semigroup_bridge.json").read_text(encoding="utf-8"))
        assert bridge["Gaussian_K_y_independent"] is True
