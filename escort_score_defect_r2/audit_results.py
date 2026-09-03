from __future__ import annotations
import json
from pathlib import Path
from common import result_dir

def main():
    out_dir = result_dir()
    files = sorted(out_dir.glob("*.json"))
    data = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in files if p.name != "audit_results.json"}
    text = json.dumps(data, ensure_ascii=False)
    assert "NaN" not in text and "Infinity" not in text
    lemma = data["escort_lemma.json"]
    third = data["third_order_defect.json"]
    assert lemma["status"] == "EXACT"
    assert all(v == "0" for k, v in lemma["symbolic_certificates"].items() if k.endswith("residual"))
    assert third["candidate_2_relation_included"] is True
    density_claim = bool(third.get("candidate_2_density_claim", False))
    if density_claim:
        raise AssertionError("no density counterexample may be inferred from the symbolic search")
    out = {"status": "AUDIT_OK", "result_files": sorted(data),
           "nan_inf_free": True, "candidate_2_density_claim": density_claim,
           "derived_from_results": True}
    path = out_dir / "audit_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("ESCORT_DEFECT_RESULTS_AUDIT_OK", path)

if __name__ == "__main__":
    main()
