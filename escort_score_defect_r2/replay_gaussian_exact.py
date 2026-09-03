from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import result_dir


def main():
    tau = sp.symbols("tau", positive=True)
    x = sp.symbols("x", real=True)
    p = sp.exp(-x**2 / (2*tau)) / sp.sqrt(2*sp.pi*tau)
    F = sp.simplify(sp.integrate(p**3, (x, -sp.oo, sp.oo)))
    rho = sp.simplify(sp.diff(sp.log(p), x))
    c = sp.simplify(sp.diff(rho, x))
    nu_weight = sp.simplify(p**3 / F)
    m2 = sp.simplify(sp.integrate(nu_weight*rho**2, (x, -sp.oo, sp.oo)))
    m4 = sp.simplify(sp.integrate(nu_weight*rho**4, (x, -sp.oo, sp.oo)))
    ec = sp.simplify(sp.integrate(nu_weight*c, (x, -sp.oo, sp.oo)))
    b_over_f = sp.simplify(sp.integrate(p*(sp.diff(p, x, 2))**2, (x, -sp.oo, sp.oo)) / F)
    var_c = sp.simplify(sp.integrate(nu_weight*c**2, (x, -sp.oo, sp.oo)) - ec**2)
    checks = {
        "F_equals_C_over_tau": sp.simplify(F - 1/(2*sp.pi*sp.sqrt(3)*tau)) == 0,
        "E_rho2": m2 == 1/(3*tau),
        "E_c": ec == -1/tau,
        "E_rho4": m4 == 1/(3*tau**2),
        "B_over_F": b_over_f == sp.Rational(2, 3)/tau**2,
        "variance_defect": var_c == m4 - 3*m2**2,
    }
    assert all(checks.values()), checks
    out = {"status": "GAUSSIAN_EXACT_REPLAY", "checks": checks}
    path = result_dir() / "gaussian_exact_replay.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("GAUSSIAN_EXACT_REPLAY_PASSED", path)


if __name__ == "__main__":
    main()
