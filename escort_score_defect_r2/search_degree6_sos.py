from __future__ import annotations
import json
from pathlib import Path

def main():
    out = {"status": "OPEN", "degree": 6,
           "candidate": "nonnegative closure for escort-score defect",
           "sos_found": False,
           "reason": "no SOS certificate was asserted without a specified Gram basis",
           "next_step": "choose a finite weighted monomial basis and solve exact rational Gram equations"}
    path = Path(__file__).resolve().parent / "results" / "degree6_sos_search.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("DEGREE6_SOS_SEARCH_BOUNDED_AND_LEFT_OPEN", path)

if __name__ == "__main__":
    main()
