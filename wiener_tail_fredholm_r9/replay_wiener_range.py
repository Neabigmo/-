"""Exact range-condition replay for one simple and one multiple zero."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def division_replay(zeta=sp.Rational(1, 3), multiplicity: int = 2) -> dict:
    z = sp.symbols("z")
    D = (z - zeta) ** multiplicity
    source = 1 + 2 * z + 3 * z**2
    in_range = sp.expand(D * source)
    quotient, good_remainder = sp.div(in_range, D, domain=sp.QQ)
    outside = sp.expand(2 + z + 4 * z**2 + 3 * z**3)
    _, bad_remainder = sp.div(outside, D, domain=sp.QQ)
    good_defects = [sp.diff(good_remainder, z, j).subs(z, zeta) for j in range(multiplicity)]
    bad_defects = [sp.diff(bad_remainder, z, j).subs(z, zeta) for j in range(multiplicity)]
    return {"zeta": str(zeta), "multiplicity": multiplicity, "good_remainder": str(good_remainder), "range_functionals_on_good_remainder": [str(v) for v in good_defects], "outside_remainder": str(bad_remainder), "defect_functionals_on_outside_remainder": [str(v) for v in bad_defects], "division_exact": sp.expand(in_range - (quotient * D + good_remainder)) == 0, "outside_has_nonzero_defect": any(v != 0 for v in bad_defects)}


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    simple = division_replay(multiplicity=1)
    double = division_replay(multiplicity=2)
    payload = {"simple_zero": simple, "double_zero": double, "radius_condition": "abs(zeta)<r", "marker": "R9_SINGLE_RADIUS_RANGE_REPLAYED"}
    (RESULTS / "wiener_range.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R9_SIMPLE_DIVISION_EXACT", simple["division_exact"])
    print("R9_DOUBLE_DIVISION_EXACT", double["division_exact"])
    print("R9_DOUBLE_RANGE_DEFECTS", double["range_functionals_on_good_remainder"])


if __name__ == "__main__":
    main()
