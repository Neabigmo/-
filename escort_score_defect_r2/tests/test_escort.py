from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def test_bounded_run_and_statuses():
    with tempfile.TemporaryDirectory() as tmp:
        env = os.environ.copy()
        env["ESCORT_RESULTS_DIR"] = tmp
        proc = subprocess.run([sys.executable, str(ROOT / "run_escort_defect.py")], cwd=ROOT, env=env, check=False)
        assert proc.returncode == 0
        summary = json.loads((Path(tmp) / "escort_run_summary.json").read_text(encoding="utf-8"))
        assert summary["final_outcome"] in {"LOCAL_IDENTITIES_INSUFFICIENT_FOR_CANDIDATE_2", "EXACT_RIGIDITY_LEMMA"}
        lemma = json.loads((Path(tmp) / "escort_lemma.json").read_text(encoding="utf-8"))
        assert lemma["status"] == "EXACT"
        assert all(v == "0" for k, v in lemma["symbolic_certificates"].items() if k.endswith("residual"))
        third = json.loads((Path(tmp) / "third_order_defect.json").read_text(encoding="utf-8"))
        gaussian = json.loads((Path(tmp) / "gaussian_exact_replay.json").read_text(encoding="utf-8"))
        assert gaussian["status"] == "GAUSSIAN_EXACT_REPLAY"
        assert all(gaussian["checks"].values())
        assert third["candidate_1_certificate_exists"]
        assert third["candidate_2_relation_included"] is True
        assert third["candidate_2_density_claim"] is False
