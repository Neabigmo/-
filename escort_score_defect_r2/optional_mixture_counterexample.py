from __future__ import annotations
import json
from pathlib import Path

def main():
    out = {"status": "NOT_RUN_BY_DESIGN", "family": "at most three Gaussian components",
           "reason": "candidate 2 was not promoted to a density claim; bounded exact identities were audited first",
           "actual_density_counterexample_certified": False}
    path = Path(__file__).resolve().parent / "results" / "mixture_search.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("OPTIONAL_MIXTURE_SEARCH_NOT_RUN", path)

if __name__ == "__main__":
    main()
