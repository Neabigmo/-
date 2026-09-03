from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from common import require, result_dir

ROOT = Path(__file__).resolve().parent


def run(name, env=None):
    command = [sys.executable]
    if sys.flags.optimize:
        command.append("-O")
    command.append(str(ROOT/name))
    proc = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    stdout = (proc.stdout or "").strip()
    return {"script": str(name), "returncode": proc.returncode, "stdout_marker": stdout.split()[0] if stdout else "", "stderr": (proc.stderr or "").strip()}


def main():
    out_dir = result_dir()
    # Build and audit in an isolated staging directory.  Existing published
    # artifacts are never overwritten before the fresh run has passed audit.
    with tempfile.TemporaryDirectory(prefix="posterior_laplace_stage_") as staging:
        stage_env = os.environ.copy()
        stage_env["LAPLACE_RESULTS_DIR"] = staging
        rows = [run(Path("derive_posterior_triple.py"), stage_env), run(Path("derive_conditional_q_moments.py"), stage_env), run(Path("certify_moment_countermodel.py"), stage_env), run(Path("derive_semigroup_bridge.py"), stage_env), run(Path("audit_critical_kernel.py"), stage_env)]
        require(all(row["returncode"] == 0 for row in rows), f"derivation failed: {rows}")
        audit = run(Path("audit_results.py"), stage_env)
        require(audit["returncode"] == 0, f"audit failed: {audit}")
        for artifact in Path(staging).glob("*.json"):
            shutil.copy2(artifact, out_dir / artifact.name)
    final = json.loads((out_dir / "critical_kernel_audit.json").read_text(encoding="utf-8"))["status"]
    out = {"status": "EXECUTED", "scripts": rows, "audit": audit, "stage28_started": False, "large_compute_started": False, "final_outcome": final}
    path = out_dir / "posterior_laplace_run_summary.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print("POSTERIOR_LAPLACE_R3_COMPLETED", path)


if __name__ == "__main__":
    main()
