from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(name):
    proc = subprocess.run([sys.executable, str(ROOT/name)], cwd=ROOT,
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", check=False)
    return {"script": str(name), "returncode": proc.returncode,
            "stdout": (proc.stdout or "").strip(), "stderr": (proc.stderr or "").strip()}

def main():
    rows = [run(Path("derive_escort_lemma.py")), run(Path("derive_third_order_defect.py")),
            run(Path("search_degree6_sos.py")), run(Path("optional_mixture_counterexample.py"))]
    assert all(row["returncode"] == 0 for row in rows), rows
    audit = run(Path("audit_results.py"))
    assert audit["returncode"] == 0, audit
    out = {"status": "EXECUTED", "scripts": rows, "audit": audit,
           "stage28_started": False, "large_campaign_started": False,
           "final_outcome": "LOCAL_IDENTITIES_INSUFFICIENT_FOR_CANDIDATE_2"}
    path = ROOT / "results" / "escort_run_summary.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print("ESCORT_SCORE_DEFECT_R2_COMPLETED", path)

if __name__ == "__main__":
    main()
