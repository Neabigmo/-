from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import result_dir


def expectation(poly, xs, moments):
    total = 0
    for exps, coeff in sp.Poly(sp.expand(poly), *xs).terms():
        term = coeff
        for exponent in exps:
            term *= moments[exponent]
        total += term
    return sp.expand(total)


def main():
    xs = sp.symbols("x1:4")
    m = {0: sp.Integer(1), 1: sp.Integer(0)}
    m.update({k: sp.symbols(f"m{k}") for k in range(2, 9)})
    q = sp.expand(sum(x*x for x in xs) - sum(xs)**2/sp.Integer(3))
    actual = {k: expectation(q**k, xs, m) for k in range(1, 5)}
    v, m3, m4, m5, m6, m8 = (m[2], m[3], m[4], m[5], m[6], m[8])
    expected = {
        1: 2*v,
        2: sp.Rational(4, 3)*(3*v**2 + m4),
        3: sp.Rational(8, 9)*(3*v**3 + 12*v*m4 - 7*m3**2 + m6),
        4: sp.Rational(16, 27)*(24*v**2*m4 - 16*v*m3**2 + 20*v*m6 - 32*m3*m5 + 19*m4**2 + m8),
    }
    residuals = {str(k): str(sp.simplify(actual[k]-expected[k])) for k in range(1, 5)}
    assert all(value == "0" for value in residuals.values()), residuals

    # The target chi-square moments after integrating nu are exact.
    a = sp.symbols("a", nonnegative=True)
    target = {k: sp.factor(2**k * sp.factorial(k) * a**k) for k in range(1, 5)}
    out = {
        "status": "EXACT_CONDITIONAL_Q_MOMENTS",
        "conditional_moment_residuals": residuals,
        "target_Q_moments": {str(k): str(vv) for k, vv in target.items()},
        "central_moment_convention": "m1=0, mk=E[(X-E[X|Y])^k|Y]",
    }
    path = result_dir() / "conditional_q_moments.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("EXACT_CONDITIONAL_Q_MOMENTS_VERIFIED", path)


if __name__ == "__main__":
    main()
