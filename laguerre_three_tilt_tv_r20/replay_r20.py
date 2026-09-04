"""Exact local audit of the proposed three-tilt subharmonicity gate.

The calculation is deliberately theory-only.  It computes the Laurent-circle
averages in the plane u1+u2+u3=0 and derives the first compatible jet of
H=K-s^2/2.  It also records an elementary probability-law counterexample to
the variance inequality when the Fock circle identity is omitted.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

t, rho = sp.symbols("t rho", nonzero=True)
h3, h4, h5, h6 = sp.symbols("h3 h4 h5 h6")

I = sp.I
cos = (t + t ** -1) / 2
sin = (t - t ** -1) / (2 * I)
alpha = (
    cos / sp.sqrt(2) + sin / sp.sqrt(6),
    -cos / sp.sqrt(2) + sin / sp.sqrt(6),
    -2 * sin / sp.sqrt(6),
)


def circle_average(expr: sp.Expr) -> sp.Expr:
    """Average a Laurent polynomial over the unit circle."""
    return sp.expand(expr).coeff(t, 0)


def p(k: int) -> sp.Expr:
    return sp.simplify(sum(a ** k for a in alpha))


def H(s: sp.Expr) -> sp.Expr:
    return h3 * s ** 3 + h4 * s ** 4 + h5 * s ** 5 + h6 * s ** 6


def main() -> dict:
    p2 = sp.simplify(circle_average(p(2)))
    p3_avg = sp.simplify(circle_average(p(3)))
    p4_avg = sp.simplify(circle_average(p(4)))
    p5_avg = sp.simplify(circle_average(p(5)))
    p6_avg = sp.simplify(circle_average(p(6)))
    p3sq_avg = sp.simplify(circle_average(p(3) ** 2))

    phi = sum(H(rho * a) for a in alpha)
    exp_phi = sp.series(sp.exp(phi), rho, 0, 7).removeO().expand()
    radial_coeffs = {
        str(k): sp.simplify(circle_average(exp_phi).coeff(rho, k))
        for k in range(3, 7)
    }

    # The rho^4 coefficient of the circle identity forces h4=0.
    h4_solution = sp.solve(sp.Eq(radial_coeffs["4"], 0), h4)[0]
    # With h4=0, the rho^6 coefficient fixes h6 in terms of h3.
    coeff6_h4zero = sp.simplify(radial_coeffs["6"].subs(h4, h4_solution))
    h6_solution = sp.solve(sp.Eq(coeff6_h4zero, 0), h6)[0]

    # Differentiate in a dummy scalar, then substitute the circle coordinate.
    q = sp.symbols("q")
    lap = sum(sp.diff(H(q), q, 2).subs(q, rho * a) for a in alpha)
    lap_compatible = sp.expand(lap.subs({h4: h4_solution, h6: h6_solution}))
    lap_leading = sp.simplify(circle_average(lap_compatible).series(rho, 0, 5).removeO())

    # A concrete non-Gaussian standardized law shows TV is not a generic
    # consequence of exponential-family convexity alone.
    a = sp.symbols("a", real=True)
    rademacher_sum = 1 + 2 * sp.sech(a) ** 2
    rademacher_gap = sp.simplify(rademacher_sum - 3)

    result = {
        "circle_normalization": "sum(alpha_i)=0, average(sum(alpha_i^2))=1",
        "circle_moments": {
            "avg_p2": p2,
            "avg_p3": p3_avg,
            "avg_p4": p4_avg,
            "avg_p5": p5_avg,
            "avg_p6": p6_avg,
            "avg_p3_squared": p3sq_avg,
        },
        "radial_exp_phi_coefficients_rho3_to_rho6": radial_coeffs,
        "forced_h4": h4_solution,
        "compatible_h6": h6_solution,
        "compatible_jet_choice": {"h3": 1, "h4": 0, "h5": 0, "h6": h6_solution.subs(h3, 1)},
        "laplacian_circle_average_leading_term": lap_leading,
        "laplacian_compatible_jet": lap_compatible,
        "rademacher_tv_gap_at_(a,-a,0)": rademacher_gap,
        "rademacher_tv_strictly_fails_for_a_nonzero": True,
        "status": "TV_NOT_CERTIFIED; circle_identity_alone_is_insufficient_at_current_jet",
        "limitation": "The compatible jet is not an actual probability-law counterexample; higher-order Fock constraints may still eliminate it.",
    }
    out = RESULTS / "r20_tv_audit.json"
    out.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
    for key, value in result.items():
        if key in {"circle_moments", "radial_exp_phi_coefficients_rho3_to_rho6", "compatible_jet_choice"}:
            print(key, value)
    print("R20_FORCED_H4", h4_solution)
    print("R20_COMPATIBLE_H6", h6_solution)
    print("R20_LAPLACIAN_AVERAGED_LEADING", lap_leading)
    print("R20_RADEMACHER_TV_GAP", rademacher_gap)
    print("R20_CIRCLE_IDENTITY_JET_AUDIT_COMPLETED")
    print("R20_TV_NOT_CERTIFIED")
    return result


if __name__ == "__main__":
    main()
