"""Replay and compare the published R5 audit artifact."""

from __future__ import annotations

import json

from audit_fisher_closure_final import run_audit
from common import RESULTS, no_nonfinite, require

def main() -> None:
    fresh = run_audit()
    published = json.loads((RESULTS / "audit_results.json").read_text(encoding="utf-8"))
    require(published == fresh, "R5 audit artifact does not match fresh replay")
    require(published["decision"] == "B", "unexpected R5 decision")
    require(published["fisher_closure"] is False, "closure must remain insufficient")
    require(no_nonfinite(published), "non-finite R5 artifact")
    print("ANGULAR_TRANSPORT_FRESH_REPLAY_MATCHED")
    print("ANGULAR_TRANSPORT_ARTIFACT_AUDIT_PASSED")

if __name__ == "__main__":
    main()
