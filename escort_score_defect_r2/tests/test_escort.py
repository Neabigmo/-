from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def test_bounded_run_and_statuses():
    proc = subprocess.run([sys.executable, str(ROOT / "run_escort_defect.py")], cwd=ROOT, check=False)
    assert proc.returncode == 0
    summary = json.loads((ROOT / "results" / "escort_run_summary.json").read_text(encoding="utf-8"))
    assert summary["final_outcome"] == "LOCAL_IDENTITIES_INSUFFICIENT_FOR_CANDIDATE_2"
    lemma = json.loads((ROOT / "results" / "escort_lemma.json").read_text(encoding="utf-8"))
    assert lemma["status"] == "EXACT"
    third = json.loads((ROOT / "results" / "third_order_defect.json").read_text(encoding="utf-8"))
    assert third["candidate_1_certificate_exists"]
    assert third["candidate_2_certificate_found"] is False
