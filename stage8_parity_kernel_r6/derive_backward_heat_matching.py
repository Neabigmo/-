"""Exact Hermite/Mehler replay and conservative sign-transfer decision."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    y, t, rho = sp.symbols("y t rho")
    generating = sp.exp(rho * y * t - (rho * t) ** 2 / 2)
    hermite = sp.hermite_prob(0, y) + rho * sp.hermite_prob(1, y) * t
    hermite += rho**2 * sp.hermite_prob(2, y) * t**2 / 2
    hermite += rho**3 * sp.hermite_prob(3, y) * t**3 / 6
    # The equality is checked through order three at t=0.
    series_residual = sp.expand(sp.series(generating - hermite, t, 0, 4).removeO())
    e1, e2, e3, o1, o2, o3 = sp.symbols("E1 E2 E3 O1 O2 O3")
    s1, s2, s3 = sp.symbols("s1 s2 s3")
    parity_phi = e1 * e2 * e3 + s2 * s3 * e1 * o2 * o3
    parity_phi += s1 * s3 * o1 * e2 * o3 + s1 * s2 * o1 * o2 * e3
    parity_factorized = sp.Rational(1, 2) * (
        (e1 + s1 * o1) * (e2 + s2 * o2) * (e3 + s3 * o3)
        + (e1 - s1 * o1) * (e2 - s2 * o2) * (e3 - s3 * o3)
    )
    gaussian_values = {e1: 2, e2: 2, e3: 2, o1: 1, o2: 1, o3: 1, s1: 1, s2: 1, s3: 1}
    gaussian_phi = sp.simplify(parity_phi.subs(gaussian_values))
    gaussian_factorized_phi = sp.simplify(parity_factorized.subs(gaussian_values))
    gaussian_positive_residual = sp.simplify(gaussian_phi - gaussian_factorized_phi)

    rows = []
    rho = sp.symbols("rho", positive=True)
    for d in (3, 5, 7, 9):
        kappa, mean_p_sq = sp.symbols(f"kappa{d} mean_p{d}_sq", positive=True)
        coefficient = rho ** (2 * d) * kappa**2 * mean_p_sq / sp.factorial(d - 1) ** 2
        replayed = (rho**d * kappa) ** 2 * mean_p_sq / sp.factorial(d - 1) ** 2
        residual = sp.simplify(coefficient - replayed)
        rows.append({"d": d, "coefficient": str(coefficient), "replay_residual": str(residual), "positive_under": "rho>0, kappa_d!=0, mean[p_d^2]>0", "positive_symbolically": residual == 0})
    payload = {
        "mehler_series_residual_through_degree_3": str(series_residual),
        "gaussian_phi": str(gaussian_phi),
        "gaussian_factorized_phi": str(gaussian_factorized_phi),
        "gaussian_positive_replay_residual": str(gaussian_positive_residual),
        "rho_mode_multiplier": "rho**m",
        "double_scaling_location": "not certified from the present interface",
        "r5_low_mode_rows": rows,
        "r5_replay_all_exact": all(row["replay_residual"] == "0" for row in rows),
        "sign_transfer_outcome": "BACKWARD_HEAT_SIGN_TRANSFER_FAILS",
        "sign_transfer_reason": "Stage-8 parity profiles are not yet uniformly identified with paired backward-heat amplitudes; normalization, location/sign map, and l2 tail tightness remain hypotheses.",
        "marker": "BACKWARD_HEAT_SIGN_TRANSFER_REQUIRES_EXTRA_IDENTIFICATION" if series_residual == 0 else "FAILED",
    }
    (RESULTS / "backward_heat_matching.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("MEHLER_SERIES_RESIDUAL", series_residual)
    print("SIGN_TRANSFER_OUTCOME", payload["sign_transfer_outcome"])
    print("R5_LOW_MODE_COUNT", len(rows))


if __name__ == "__main__":
    main()
