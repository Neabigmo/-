"""Independent consistency checks for the R20 theory audit."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "results" / "r20_tv_audit.json").read_text(encoding="utf-8"))
mom = data["circle_moments"]
assert mom["avg_p3"] == "0" or sp.sympify(mom["avg_p3"]) == 0
assert sp.sympify(mom["avg_p4"]) == sp.Rational(1, 2)
assert sp.sympify(mom["avg_p6"]) == sp.Rational(5, 18)
assert sp.sympify(mom["avg_p3_squared"]) == sp.Rational(1, 12)
assert sp.sympify(data["forced_h4"]) == 0
assert sp.sympify(data["compatible_h6"]) == -sp.Rational(3, 20) * sp.Symbol("h3") ** 2
gap_expr = sp.sympify(data["rademacher_tv_gap_at_(a,-a,0)"])
assert sp.simplify(gap_expr.subs(sp.Symbol("a"), 1)) < 0
assert data["rademacher_tv_strictly_fails_for_a_nonzero"] is True
assert data["status"] == "TV_NOT_CERTIFIED; circle_identity_alone_is_insufficient_at_current_jet"
print("R20_AUDIT_COMPLETED")
print("R20_RESULT_SCHEMA_VERIFIED")
