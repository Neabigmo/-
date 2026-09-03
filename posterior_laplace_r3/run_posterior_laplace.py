from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from common import result_dir

ROOT = Path(__file__).resolve().parent


def run(name):
    proc = subprocess.run([sys.executable, str(ROOT/name)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    return {"script": str(name), "returncode": proc.returncode, "stdout": (proc.stdout or "").strip(), "stderr": (proc.stderr or "").strip()}


def main():
    rows = [run(Path("derive_posterior_triple.py")), run(Path("derive_conditional_q_moments.py")), run(Path("certify_moment_countermodel.py")), run(Path("derive_semigroup_bridge.py")), run(Path("audit_critical_kernel.py"))]
    assert all(row["returncode"] == 0 for row in rows), rows
    audit = run(Path("audit_results.py"))
    assert audit["returncode"] == 0, audit
    final = json.loads((result_dir() / "critical_kernel_audit.json").read_text(encoding="utf-8"))["status"]
    out = {"status": "EXECUTED", "scripts": rows, "audit": audit, "stage28_started": False, "large_compute_started": False, "final_outcome": final}
    path = result_dir() / "posterior_laplace_run_summary.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print("POSTERIOR_LAPLACE_R3_COMPLETED", path)


if __name__ == "__main__":
    main()
