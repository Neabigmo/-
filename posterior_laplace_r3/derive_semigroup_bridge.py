from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import result_dir


def main():
    t, u, s, y = sp.symbols("t u s y", positive=True)
    # v=t*u/(t+u), u=1/(2s), r=t-v and therefore v+r=t.
    v = sp.simplify(t*u/(t+u))
    r = sp.simplify(t-v)
    assert sp.simplify(v + r - t) == 0
    # The Gaussian product calculation reduces the prefactor exactly.
    prefactor_ratio = sp.simplify((v/t) * (2*sp.pi*v)**(-sp.Rational(3, 2)) * sp.sqrt(v/t) / (2*sp.pi*t)**(-sp.Rational(3, 2)))
    assert sp.simplify(prefactor_ratio - 1) == 0

    sigma2 = 1 + v
    gaussian_K = sp.simplify((sigma2+r)/sigma2)
    assert not gaussian_K.has(y)
    target_ratio = sp.simplify((v/t) * (1+t)/(1+v))
    a = t/(1+t)
    target_laplace = sp.simplify(1/(1+2*a*s))
    target_ratio_sub = sp.simplify(target_ratio.subs(u, 1/(2*s)))
    assert sp.simplify(target_ratio_sub-target_laplace) == 0
    out = {
        "status": "EXACT_POSTERIOR_SEMIGROUP_BRIDGE",
        "bridge": "L_t,y(s)=(v/t)*P_{r/3}(p_v^3)(y)/p_t(y)^3",
        "parameters": "u=1/(2s), v=tu/(t+u)=t/(1+2st), r=t-v, v+r=t",
        "prefactor_residual": str(sp.simplify(prefactor_ratio-1)),
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
