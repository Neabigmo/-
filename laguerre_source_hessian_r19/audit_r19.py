"""Independent result-file audit for R19."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def audit(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "target_eliminations",
        "c1_c3",
        "d0_d4",
        "star_predicted_d4",
        "d4_minus_star",
        "d4_minus_star_over_c2_square",
        "corrected_d4_residual",
        "low_order_checks",
        "star_formally_refuted",
    }
    missing = sorted(required - set(data))
    if missing:
        raise AssertionError(f"missing fields: {missing}")
    if not all(data["low_order_checks"].values()):
        raise AssertionError("low-order checks failed")
    if data["d4_minus_star_over_c2_square"] != "2/3":
        raise AssertionError("unexpected d4 discrepancy")
    if data["corrected_d4_residual"] != "0":
        raise AssertionError("corrected d4 relation failed")
    if data["star_formally_refuted"] is not True:
        raise AssertionError("the proposed identity was not marked refuted")
    return {"verified": True, "d4_difference_ratio": str(sp.Rational(2, 3))}


def main() -> None:
    path = Path(__file__).resolve().parent / "results" / "r19_audit.json"
    result = audit(path)
    print("R19_RESULT_SCHEMA_VERIFIED")
    print(f"R19_D4_DIFFERENCE_RATIO {result['d4_difference_ratio']}")
    print("R19_INDEPENDENT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
