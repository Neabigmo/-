"""Independent replay and artifact checks for angular_fisher_r4."""

from __future__ import annotations

import json

from common import RESULTS, no_nonfinite, require
from audit_fisher_closure import run_audit


def main() -> None:
    fresh = run_audit()
    published = json.loads((RESULTS / "audit_results.json").read_text(encoding="utf-8"))
    require(published == fresh, "audit artifact does not match fresh replay")
    require(published["decision"] == "B", "unexpected decision")
    require(published["fisher_closure"] is False, "closure must be marked insufficient")
    require(no_nonfinite(published), "non-finite artifact value")
    print("ANGULAR_FISHER_FRESH_REPLAY_MATCHED")
    print("ANGULAR_FISHER_ARTIFACT_AUDIT_PASSED")


if __name__ == "__main__":
    main()

