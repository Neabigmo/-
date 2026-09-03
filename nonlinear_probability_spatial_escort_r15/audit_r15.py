"""Produce a compact, machine-readable R15 audit result."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

from replay_spatial_escort import (
    angular_power_sums,
    bell_angular_expression,
    expected_order_identities,
    posterior_variance_scaled_order6,
    gaussian_benchmark,
    probability_countermodels,
    hubbard_straatonovich_check,
    q_t_normalization_check,
    common_shift_prefactor_check,
    stein_density_check,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def main():
    OUT.mkdir(exist_ok=True)
    p, averages = angular_power_sums()
    b2, _ = bell_angular_expression(2)
    b4, _ = bell_angular_expression(4)
    b6, _ = bell_angular_expression(6)
    expected = expected_order_identities()
    variance6 = posterior_variance_scaled_order6()
    d, V, V1, V2, V4 = sp.symbols("d V V1 V2 V4")
    expected_variance6 = (
        d**4 * V4 + 27*d**2*V2*(V-d) + 3*d**2*V1**2
        + 54*(V-d)**3
    )
    bell_ok = all(
        sp.simplify(got - expected[k]) == 0
        for k, got in ((2, b2), (4, b4), (6, b6))
    )
    variance_ok = sp.simplify(variance6 - expected_variance6) == 0
    core_checks = {
        "hubbard_straatonovich": hubbard_straatonovich_check(),
        "q_t_normalization": q_t_normalization_check(),
        "common_shift_prefactor": common_shift_prefactor_check(),
        "stein_density": stein_density_check(),
    }
    checks = {
        "angular_power_sums": {str(k): str(v) for k, v in p.items()},
        "angular_averages": {k: str(v) for k, v in averages.items()},
        "bell_order_2": str(b2),
        "bell_order_4": str(b4),
        "bell_order_6": str(b6),
        "expected_order_identities": {str(k): str(v) for k, v in expected.items()},
        "posterior_variance_order6": str(variance6),
        "posterior_variance_order6_expected": str(expected_variance6),
        "gaussian_benchmark": {k: str(v) for k, v in gaussian_benchmark().items()},
        "countermodels": {k: str(v) for k, v in probability_countermodels().items()},
        "common_shift_identity": "E_{N(0,q/3),theta} prod_j F_q(X+d*z*alpha_j)=1",
        "decision": "B",
        "decision_marker": "NEW_ODD_SQUARE_IDENTITY_CERTIFIED_CLOSURE_REMAINS",
        "coercivity_closed": False,
        "exact_identity_status": bool(bell_ok and variance_ok and all(core_checks.values())),
        "core_symbolic_checks": core_checks,
    }
    (OUT / "r15_audit.json").write_text(
        json.dumps(checks, indent=2), encoding="utf-8"
    )
    if not (bell_ok and variance_ok and all(core_checks.values())):
        raise AssertionError("symbolic order or variance identity replay failed")
    print("DAMPED_LAPLACE_FOCK_IDENTITY VERIFIED")
    print("POSITIVE_COMMON_SHIFT_FOCK_IDENTITY VERIFIED")
    print("SPATIAL_ESCORT_VARIANCE_HIERARCHY_THROUGH_ORDER6 VERIFIED")
    print("NEW_ODD_SQUARE_IDENTITY_CERTIFIED_CLOSURE_REMAINS")
    print("COERCIVITY_CLOSED False")
    print("R15_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
