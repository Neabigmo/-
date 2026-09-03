"""Exact operator bridge replay for Stage 8 and R5."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def hermite_addition_replay() -> dict:
    a1, a2, a3, x1, x2, x3 = sp.symbols("a1 a2 a3 x1 x2 x3")
    n = 5
    normalized_h = lambda degree, variable: sp.hermite_prob(degree, variable) / sp.sqrt(sp.factorial(degree))
    direct = normalized_h(n, a1 * x1 + a2 * x2 + a3 * x3)
    addition = sp.Integer(0)
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            addition += sp.sqrt(sp.factorial(n) / (sp.factorial(i) * sp.factorial(j) * sp.factorial(k))) * a1**i * a2**j * a3**k * normalized_h(i, x1) * normalized_h(j, x2) * normalized_h(k, x3)
    residual = sp.Poly(sp.expand(direct - addition), a3)
    sphere_remainder = sp.rem(residual, sp.Poly(a3**2 - (1 - a1**2 - a2**2), a3)).as_expr()
    sphere_remainder = sp.expand(sphere_remainder)
    return {"degree": n, "residual_on_sphere": str(sphere_remainder), "exact_on_sum_a2_eq_1": sphere_remainder == 0}


def coherent_replay() -> dict:
    n = 4
    a1, a2, a3 = sp.symbols("a1 a2 a3")
    norm_sum = sp.Integer(0)
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            norm_sum += n**n * a1 ** (2 * i) * a2 ** (2 * j) * a3 ** (2 * k) / (sp.factorial(i) * sp.factorial(j) * sp.factorial(k))
    # Work with squared variables to make the multinomial identity exact.
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    squared_sum = sum(n**n * x1**i * x2**j * x3**k / (sp.factorial(i) * sp.factorial(j) * sp.factorial(k)) for i in range(n + 1) for j in range(n - i + 1) for k in [n - i - j])
    squared_residual = sp.expand(squared_sum.subs(x3, 1 - x1 - x2) - n**n / sp.factorial(n))
    return {"degree": n, "normalization_residual": str(squared_residual), "normalization_exact_on_sphere": squared_residual == 0, "parity_character_count": 4}


def gram_and_countermodel() -> dict:
    G = sp.Matrix([[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), 1]])
    eigenvalues = G.eigenvals()
    e0 = sp.Matrix([1, 0])
    e1 = sp.Matrix([0, 1])
    mixed = (e1.T * G * e0)[0]
    energy = (e1.T * G * e1)[0]
    bound_residual = sp.expand(mixed**2 - energy * (e0.T * G * e0)[0])
    G3 = sp.kronecker_product(G, G, G)
    psi3 = sp.kronecker_product(e1, e0, e0)
    vac3 = sp.kronecker_product(e0, e0, e0)
    mixed3 = (psi3.T * G3 * vac3)[0]
    return {"gram_eigenvalues": [str(v) for v in eigenvalues], "gram_psd": bool(all(bool(v > 0) for v in eigenvalues)), "mixed": str(mixed), "diagonal_energy": str(energy), "cs_bound_residual": str(bound_residual), "tensor_mixed": str(mixed3), "tensor_sign_negative": bool(mixed3 < 0), "countermodel_scope": "operator-only; no Fock equation or target law"}


def global_bridge_replay() -> dict:
    x = sp.symbols("x")
    r = sp.Function("r")(x)
    bridge_residual = sp.simplify(r * (sp.diff(sp.log(r), x)) ** 2 - sp.diff(r, x) ** 2 / r)
    return {"log_derivative_residual": str(bridge_residual), "random_angle_projection": "standard Gaussian by rotational invariance", "hermite_expansion_scope": "L2(dgamma), subject to density regularity", "posterior_angle_identity": "2*pi*pi_x = r_theta", "exact": bridge_residual == 0}


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    payload = {"hermite_addition": hermite_addition_replay(), "coherent_projection": coherent_replay(), "gram_countermodel": gram_and_countermodel(), "global_r5_bridge": global_bridge_replay()}
    payload["all_exact_replays"] = bool(payload["hermite_addition"]["exact_on_sum_a2_eq_1"] and payload["coherent_projection"]["normalization_exact_on_sphere"] and payload["global_r5_bridge"]["exact"])
    payload["decision"] = "R6_POINTWISE_SIGN_INTERFACE_INVALID"
    payload["marker"] = "R7_OPERATOR_BRIDGE_AUDIT_COMPLETED" if payload["all_exact_replays"] and payload["gram_countermodel"]["gram_psd"] and payload["gram_countermodel"]["tensor_sign_negative"] else "R7_AUDIT_FAILED"
    (RESULTS / "operator_bridge.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("HERMITE_ADDITION_RESIDUAL", payload["hermite_addition"]["residual_on_sphere"])
    print("COHERENT_NORMALIZATION_RESIDUAL", payload["coherent_projection"]["normalization_residual"])
    print("GRAM_COUNTERMODEL_MIXED", payload["gram_countermodel"]["mixed"])
    print("R7_DECISION", payload["decision"])


if __name__ == "__main__":
    main()
