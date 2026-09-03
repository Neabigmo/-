from __future__ import annotations

import json
import sympy as sp

from common import require, result_dir


def gaussian_product_convolution(a_values, y, variance, convolution_variance):
    """Exact integral of three N(a_i, variance) kernels times N(y, w)."""
    w = convolution_variance
    precision = sp.Rational(3, 1) / variance + 1 / w
    linear = sum(a_values) / variance + y / w
    constant = sum(a*a for a in a_values) / variance + y*y / w
    exponent = sp.simplify(-sp.Rational(1, 2) * (constant - linear**2 / precision))
    prefactor = ((2*sp.pi*variance)**(-sp.Rational(3, 2))
                 * (2*sp.pi*w)**(-sp.Rational(1, 2))
                 * sp.sqrt(2*sp.pi/precision))
    return sp.simplify(prefactor * sp.exp(exponent))


def exact_two_point_kernel():
    # K_{v,r}f(y)=P_{r/3}((P_v mu)^3)(y)/(P_{v+r}mu(y))^3.
    # Expand the cube into its eight signed Gaussian triples and integrate
    # each term exactly by completing the square.
    v = sp.Integer(1)
    r = sp.Integer(1)
    t = v + r
    y = sp.Integer(0)
    signs = (-sp.Integer(1), sp.Integer(1))
    numerator = sp.simplify(sum(
        gaussian_product_convolution((a, b, c), y, v, r/3)
        for a in signs for b in signs for c in signs
    ) / 8)
    heat_kernel = lambda variance, point: (2*sp.pi*variance)**(-sp.Rational(1, 2)) * sp.exp(-point**2/(2*variance))
    denominator_base = sp.simplify(sum(heat_kernel(t, y - a) for a in signs) / 2)
    kernel = sp.simplify(numerator / denominator_base**3)
    return kernel, numerator, denominator_base


def main():
    k, numerator, denominator_base = exact_two_point_kernel()
    expected_k = sp.Rational(1, 2) + sp.Rational(3, 2)*sp.exp(-sp.Rational(2, 3))
    gaussian_lower_bound = sp.Rational(3, 2)
    require(sp.simplify(k - expected_k) == 0, f"direct kernel expansion mismatch: {k}")
    require(k < gaussian_lower_bound, f"kernel is not below Gaussian value: {k}")
    out = {
        "status": "EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE",
        "prior": "(delta_-1+delta_+1)/2",
        "v": 1,
        "r": 1,
        "y": 0,
        "exact_K": str(k),
        "exact_numerator": str(numerator),
        "exact_smoothed_denominator_at_y": str(denominator_base),
        "gaussian_equality_value": "3/2",
        "strict_exact_comparison": "K < 3/2",
        "tested_mechanism": "universal Gaussian-equality lower bound K_{v,r}f >= K_Gaussian",
        "warning": "This refutes only the tested one-sided kernel inequality; it is not a counterexample to the original characterization.",
    }
    path = result_dir() / "critical_kernel_audit.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE_VERIFIED", path)


if __name__ == "__main__":
    main()
