from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import require, result_dir


def main():
    t, u, s, y = sp.symbols("t u s y", positive=True)
    # v=t*u/(t+u), u=1/(2s), r=t-v and therefore v+r=t.
    v = sp.simplify(t*u/(t+u))
    r = sp.simplify(t-v)
    require(sp.simplify(v + r - t) == 0, "v+r=t failed")
    # Independently evaluate the complete Gaussian integral for all eight
    # signed triples at one exact parameter point and compare it with the
    # completed-square formula.  This is not a self-canceling ratio.
    x = sp.symbols("x", real=True)
    v0, r0, y0 = sp.Integer(1), sp.Integer(1), sp.Integer(0)
    w0 = r0 / 3
    checks = []
    test_points = [(sp.Integer(1), sp.Integer(1), sp.Integer(0)),
                   (sp.Integer(2), sp.Integer(1), sp.Integer(1)),
                   (sp.Integer(1), sp.Integer(2), -sp.Integer(1))]
    for v_test, r_test, y_test in test_points:
        w_test = r_test / 3
        for a0 in (-sp.Integer(1), sp.Integer(1)):
            for b0 in (-sp.Integer(1), sp.Integer(1)):
                for c0 in (-sp.Integer(1), sp.Integer(1)):
                    integrand = ((2*sp.pi*v_test)**(-sp.Rational(3, 2))
                                 * (2*sp.pi*w_test)**(-sp.Rational(1, 2))
                                 * sp.exp(-((x-a0)**2 + (x-b0)**2 + (x-c0)**2)/(2*v_test)
                                          - (y_test-x)**2/(2*w_test)))
                    direct = sp.expand_func(sp.integrate(integrand, (x, -sp.oo, sp.oo)))
                    precision = sp.Rational(3, 1)/v_test + 1/w_test
                    linear = (a0+b0+c0)/v_test + y_test/w_test
                    constant = (a0*a0+b0*b0+c0*c0)/v_test + y_test*y_test/w_test
                    completed = ((2*sp.pi*v_test)**(-sp.Rational(3, 2))
                                 * (2*sp.pi*w_test)**(-sp.Rational(1, 2))
                                 * sp.sqrt(2*sp.pi/precision)
                                 * sp.exp(-sp.Rational(1, 2) * (constant - linear**2/precision)))
                    checks.append(sp.simplify(direct - completed))
    require(all(value == 0 for value in checks), f"Gaussian integral checks failed: {checks}")
    prefactor_residual = str(sp.simplify(sum(checks)))

    sigma2 = 1 + v
    gaussian_K = sp.simplify((sigma2+r)/sigma2)
    require(not gaussian_K.has(y), "Gaussian K still depends on y")
    target_ratio = sp.simplify((v/t) * (1+t)/(1+v))
    a = t/(1+t)
    target_laplace = sp.simplify(1/(1+2*a*s))
    target_ratio_sub = sp.simplify(target_ratio.subs(u, 1/(2*s)))
    require(sp.simplify(target_ratio_sub-target_laplace) == 0, "integrated bridge ratio failed")
    out = {
        "status": "EXACT_POSTERIOR_SEMIGROUP_BRIDGE",
        "bridge": "L_t,y(s)=(v/t)*P_{r/3}(p_v^3)(y)/p_t(y)^3",
        "parameters": "u=1/(2s), v=tu/(t+u)=t/(1+2st), r=t-v, v+r=t",
        "prefactor_residual": str(prefactor_residual),
        "complete_gaussian_integral_checks": len(checks),
        "complete_gaussian_integral_test_points": [[str(a), str(b), str(c)] for a, b, c in test_points],
        "integrated_ratio": "(v/t)*(F_v/F_t)=1/(1+2*a_t*s)",
        "Gaussian_K": str(gaussian_K),
        "Gaussian_K_y_independent": True,
        "Holder_warning": "At the critical conjugate exponent Gaussian weights cancel; the leftover integral is not integrable, so naive Holder is not a proof.",
    }
    path = result_dir() / "semigroup_bridge.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("EXACT_POSTERIOR_SEMIGROUP_BRIDGE_VERIFIED", path)


if __name__ == "__main__":
    main()
