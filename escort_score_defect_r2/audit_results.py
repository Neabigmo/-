from __future__ import annotations
import json
from pathlib import Path

def main():
    root = Path(__file__).resolve()
    result_dir = root.parent / "results"
    files = sorted(result_dir.glob("*.json"))
    data = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in files}
    text = json.dumps(data, ensure_ascii=False)
    assert "NaN" not in text and "Infinity" not in text
    out = {"status": "AUDIT_OK", "result_files": [p.name for p in files],
           "nan_inf_free": True, "candidate_2_density_claim": False}
    path = result_dir / "audit_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("ESCORT_DEFECT_RESULTS_AUDIT_OK", path)

if __name__ == "__main__":
    main()
