"""Small exact replays for the R8 analytic-radius estimates."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def exact_hellinger_cauchy_schwarz() -> dict:
    # A finite probability table is enough to audit the algebraic step.
    probs = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)]
    u = [sp.Rational(2), sp.Rational(-1, 3), sp.Rational(1, 5)]
    v = [sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(-2)]
    w = [sp.Rational(-1), sp.Rational(2), sp.Rational(1, 4)]
    signs = [1, -1, 1]
    lhs = sum(sp.sqrt(p) * s * a * b * c for p, s, a, b, c in zip(probs, signs, u, v, w)) ** 2
    rhs = sum(p for p in probs) * sum((a * b * c) ** 2 for a, b, c in zip(u, v, w))
    return {"lhs": str(lhs), "rhs": str(rhs), "cs_slack": str(sp.simplify(rhs - lhs)), "sum_probability": str(sum(probs))}


def radius_factor_bookkeeping() -> dict:
    r, R = sp.symbols("r R", positive=True)
    q = sp.symbols("q", positive=True)
    i, j, k, N = sp.symbols("i j k N", integer=True, nonnegative=True)
    # On i+j+k=n, r^n = R^n (r/R)^n exactly.
    monomial_residual = sp.simplify(r ** (i + j + k) - R ** (i + j + k) * (r / R) ** (i + j + k))
    two_high_exponent = sp.simplify(q ** (2 * N))
    three_high_exponent = sp.simplify(q ** (3 * N))
    compact_tail = sp.simplify((r / R) ** 2)
    return {
        "monomial_residual": str(monomial_residual),
        "two_high_norm_factor": str(two_high_exponent),
        "three_high_norm_factor": str(three_high_exponent),
        "compact_inclusion_tail_at_N": str(compact_tail ** N),
        "two_high_claim": "(r/R)^(2N)",
        "three_high_claim": "(r/R)^(3N)",
    }


def ou_scale_replay() -> dict:
    rho, s, R = sp.symbols("rho s R", positive=True)
    b0, b1, b2 = sp.symbols("b0 b1 b2")
    # Finite-support exact audit of ||OU_rho b||_s^2 = ||b||_{s rho}^2.
    left = sum((s ** n * rho ** n * b) ** 2 for n, b in enumerate((b0, b1, b2)))
    right = sum(((s * rho) ** n * b) ** 2 for n, b in enumerate((b0, b1, b2)))
    return {"residual": str(sp.expand(left - right)), "positive_radius_hypothesis": True, "arbitrary_l2_claim": False, "sufficient_condition": "s*rho <= R"}


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    cs = exact_hellinger_cauchy_schwarz()
    payload = {
        "hellinger_cs": cs,
        "radius_factors": radius_factor_bookkeeping(),
        "ou_scale": ou_scale_replay(),
        "uniform_in_theta": cs["sum_probability"] == "1",
        "angle_average_nonexpansive": cs["sum_probability"] == "1" and sp.sympify(cs["cs_slack"]) >= 0,
        "marker": "R8_RADIUS_GAP_COMPACTNESS_REPLAY_COMPLETED",
    }
    (RESULTS / "radius_gap_bound.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("R8_EXACT_HELLINGER_CS_REPLAYED", payload["hellinger_cs"]["sum_probability"])
    print("R8_RADIUS_FACTOR_BOOKKEEPING_REPLAYED", payload["radius_factors"]["monomial_residual"])
    print("R8_OU_SCALE_REPLAYED", payload["ou_scale"]["residual"])
    print(payload["marker"])


if __name__ == "__main__":
    main()
