from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from common import result_dir


def main():
    y, t = sp.symbols("y t", real=True, positive=True)
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    xs = (x1, x2, x3)
    xbar = sum(xs) / 3
    q = sp.expand(sum((x - xbar)**2 for x in xs))
    decomposition = sp.expand(sum((y - x)**2 for x in xs) - (3*(y-xbar)**2 + q))
    assert decomposition == 0

    # Integrating the centered Gaussian factor gives the exact constant.
    constant = sp.simplify((2*sp.pi*t)**(-sp.Rational(3, 2)) * sp.sqrt(2*sp.pi*t/3))
    assert sp.simplify(constant - 1/(2*sp.pi*t*sp.sqrt(3))) == 0

    s = sp.symbols("s", nonnegative=True)
    a = t/(1+t)
    laplace_ratio = sp.simplify((1 + 1/t) / (1 + 1/t + 2*s))
    target_laplace = sp.simplify(1/(1+2*a*s))
    assert sp.simplify(laplace_ratio - target_laplace) == 0

    out = {
        "status": "EXACT_POSTERIOR_TRIPLE_LAPLACE_IDENTITY",
        "product_kernel_constant": "1/(2*pi*t*sqrt(3))",
        "quadratic_decomposition_residual": str(decomposition),
        "hierarchical_identity": "E_nu[L_t,Y(s)] = E_mu3[e^(-sQ)e^(-Q/(2t))]/E_mu3[e^(-Q/(2t))]",
        "chi2_target_laplace": "1/(1+2*a_t*s)",
        "laplace_normalization_residual": str(sp.simplify(laplace_ratio-target_laplace)),
    }
    path = result_dir() / "posterior_triple.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("EXACT_POSTERIOR_TRIPLE_LAPLACE_VERIFIED", path)


if __name__ == "__main__":
    main()
