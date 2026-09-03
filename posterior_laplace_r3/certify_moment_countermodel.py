from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import result_dir


def main():
    rt3 = sp.sqrt(3)
    vm = (9 - 3*rt3)/4
    vp = (9 + 3*rt3)/4
    probs = [sp.Rational(1, 9), (4+2*rt3)/9, (4-2*rt3)/9]
    vals = [sp.Integer(0), vm, vp]
    moments = {k: sp.simplify(sum(p*v**k for p, v in zip(probs, vals))) for k in range(1, 5)}
    expected_v = {1: sp.Integer(1), 2: sp.Rational(3, 2), 3: sp.Rational(27, 8), 4: sp.Rational(81, 8)}
    assert moments == expected_v, moments
    q_moments = {k: sp.simplify(sp.Rational(3, 4)*(sp.Rational(8, 3))**k*moments[k]) for k in range(1, 5)}
    target_q = {k: sp.Integer(2)**k*sp.factorial(k) for k in range(1, 5)}
    assert q_moments == target_q, q_moments
    p_q_zero = sp.simplify(sp.Rational(1, 9) + sp.Rational(8, 9)*sp.Rational(1, 4))
    assert p_q_zero == sp.Rational(1, 3)
    assert sp.simplify(moments[2] - moments[1]**2) == sp.Rational(1, 2)
    out = {
        "status": "EXACT_MOMENT_RELAXATION_COUNTERMODEL",
        "V_values": [str(v) for v in vals],
        "V_probabilities": [str(p) for p in probs],
        "V_moments": {str(k): str(v) for k, v in moments.items()},
        "Q_moments": {str(k): str(v) for k, v in q_moments.items()},
        "Q_target_moments": {str(k): str(v) for k, v in target_q.items()},
        "P_Q_zero": str(p_q_zero),
        "Var_V": "1/2",
        "warning": "Formal hierarchical moment model only; not a posterior family from a common prior and not an actual solution.",
    }
    path = result_dir() / "moment_countermodel.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("EXACT_MOMENT_RELAXATION_COUNTERMODEL_VERIFIED", path)


if __name__ == "__main__":
    main()
