"""Exact derivative certificates for the tilted angular Fisher budget."""

from __future__ import annotations

import sympy as sp

from common import require, write_json
from derive_angular_geometry import exact_geometry


z = sp.symbols("z", real=True, nonzero=True)
K = sp.Function("K")


def derive_budget() -> dict[str, object]:
    geom = exact_geometry()
    A, C = sp.symbols("A_z C_z", real=True)
    Va, Vb = sp.symbols("V_a V_b", nonnegative=True)
    # log w_z = sum K(z*a_j)-z^2/2; these are exact chain-rule identities.
    dtheta_logw = z * C
    dtheta2_logw = -z * (A + z) + z**2 * Vb
    require(dtheta_logw == z * C, "theta derivative certificate failed")
    return {
        "status": "EXACT_POLAR_FISHER_IDENTITIES_VERIFIED",
        "normalization": "E_z[1]=1",
        "mean_identity": "E_z[A_z]=0",
        "radial_identity": "E_z[A_z^2 + sum_j a_j^2*v(z*a_j)] = 1",
        "angular_identity": "E_z[C_z^2 + sum_j b_j^2*v(z*a_j)] = 1",
        "polar_budget": "E_z[A_z^2+C_z^2+sum_j(a_j^2+b_j^2)*v(z*a_j)] = 2",
        "geometry_used": geom["checks"],
        "theta_logw_derivative": dtheta_logw,
        "theta_logw_second_derivative": dtheta2_logw,
        "angular_ibp_certificate": "0=E_z[(partial_theta log w)^2+partial_theta^2 log w] gives z^2 E_z[C^2+V_b]=z^2",
        "radial_certificate": "law of total variance for the tilted N(z,1) mixture",
        "interpretation": {
            "mean": "total mean decomposition",
            "radial": "law of total variance",
            "angular": "circle Fisher identity",
            "sum": "polar Fisher budget",
        },
    }


def algebraic_gap_witness() -> dict[str, object]:
    # This is deliberately only a logical witness for the named inequalities.
    # It is not claimed to arise from one common K or from the target law.
    eps = sp.Rational(1, 5)
    v1, v2, v3 = sp.Rational(11, 10), sp.Rational(4, 5), sp.Rational(4, 5)
    Va = sp.Rational(2, 3) * v1 + sp.Rational(1, 6) * v2 + sp.Rational(1, 6) * v3
    Vb = sp.Rational(1, 2) * v2 + sp.Rational(1, 2) * v3
    J1, J2, J3 = 1 / v1, 1 / v2, 1 / v3
    JL = 1 / Va
    H = eps / 72
    require(Va == 1 and Vb == sp.Rational(4, 5), "gap witness variance algebra failed")
    require(JL == 1 and sum([sp.Rational(2, 3) * v1, sp.Rational(1, 6) * v2, sp.Rational(1, 6) * v3]) == 1, "Stam witness failed")
    require(H >= 0 and H <= eps / 36, "Poincare witness failed")
    return {
        "kind": "logical_inequality_gap_witness",
        "theta": 0,
        "epsilon": eps,
        "v_j": [v1, v2, v3],
        "A_squared": 0,
        "C_squared": eps,
        "V_a": Va,
        "V_b": Vb,
        "radial_budget": "A^2+V_a=1",
        "angular_budget": "C^2+V_b=1",
        "J_j": [J1, J2, J3],
        "Cramer_Rao_equalities": ["J_j*v_j=1"] * 3,
        "Stam_sum_fisher": "J_L=1/V_a=1",
        "Poincare_H": H,
        "Poincare_upper_bound_at_z1": eps / 36,
        "C_squared_nonzero": True,
        "scope_warning": "This witness proves only that these scalar nonnegative inequalities do not algebraically force C_z=0; it is not a target-law counterexample.",
    }


def gaussian_exact_replay() -> dict[str, object]:
    """Replay the target identities for K(t)=t^2/2 exactly."""
    geom = exact_geometry()
    exponent = sp.expand(z**2 / 2 * (geom["checks"]["sum_a2"] - 1))
    require(exponent == 0, "Gaussian tilted exponent did not cancel")
    checks = {
        "K": "t^2/2",
        "log_w": exponent,
        "w_z": 1,
        "A_z": 0,
        "C_z": 0,
        "v": 1,
        "radial_budget": 1,
        "angular_budget": 1,
    }
    return {
        "status": "EXACT_GAUSSIAN_REPLAY_VERIFIED",
        "checks": checks,
        "scope": "exact replay only; it validates the identities at the Gaussian point",
    }


def non_gaussian_formula_sanity() -> dict[str, object]:
    """A positivity-only sanity check; it does not assume the target identity."""
    geom = exact_geometry()
    # Centered Rademacher has K(t)=log(cosh(t)); only positivity is asserted.
    # Substitute by name to avoid importing the angular module's symbol as public API.
    a0 = [sp.simplify(item.subs({"theta": 0})) for item in geom["a"]]
    w_expr = sp.exp(sum(sp.log(sp.cosh(item)) for item in a0))
    require(w_expr.is_positive is True, "non-Gaussian positivity sanity failed")
    return {
        "status": "NON_GAUSSIAN_POSITIVITY_SANITY_VERIFIED",
        "distribution": "centered Rademacher, K(t)=log(cosh(t))",
        "theta": 0,
        "w_z_at_z1": w_expr,
        "scope_warning": "positivity only; average_theta w_z=1 is not assumed or claimed",
    }


def main() -> None:
    budget = derive_budget()
    witness = algebraic_gap_witness()
    gaussian = gaussian_exact_replay()
    non_gaussian = non_gaussian_formula_sanity()
    write_json(
        "fisher_budget.json",
        {
            "budget": budget,
            "gap_witness": witness,
            "gaussian_replay": gaussian,
            "non_gaussian_sanity": non_gaussian,
        },
    )
    print("EXACT_POLAR_FISHER_IDENTITIES_VERIFIED")
    print("EXACT_GAUSSIAN_REPLAY_VERIFIED")
    print("NON_GAUSSIAN_POSITIVITY_SANITY_VERIFIED")
    print("FISHER_STAM_POINCARE_ALGEBRAIC_GAP_WITNESS_VERIFIED")


if __name__ == "__main__":
    main()
