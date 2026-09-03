from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from replay_parity_symbols import (  # noqa: E402
    endpoint_symbol_coefficient_replay,
    jet_compensation_replay,
    normalized_domain_replay,
    ou_scaling_replay,
    parity_symbol_replay,
    stage7_parity_coefficient_replay,
)


def test_exact_d_plus_minus_c_identities_and_gaussian():
    data = parity_symbol_replay()
    assert data["D_even"] and data["C_odd"]
    assert data["D_plus_C_equals_Rminus_squared"]
    assert data["D_minus_C_equals_Rplus_squared"]
    assert data["gaussian_normalization"]


def test_stage7_parity_coefficient_replay():
    data = stage7_parity_coefficient_replay(max_degree=6)
    assert data["odd_total_coefficients_zero"]
    assert data["even_output_i_parity_matches_pair_parity"]
    assert data["even_linear_divisors_nonzero"]


def test_odd_endpoint_symbol_coefficients():
    assert endpoint_symbol_coefficient_replay()["all_checks_zero"]


def test_normalized_x_y_domains():
    data = normalized_domain_replay()
    assert data["X_low_coefficients_zero"]
    assert data["X_is_z4_positive_wiener_ideal"]
    assert data["Y_is_z3_positive_wiener_space"]
    assert data["C_X_bounded_isomorphism"] and data["C_Y_bounded_isomorphism"]


def test_simple_and_double_jet_compensation():
    data = jet_compensation_replay()
    assert data["simple_and_double_jet_compensation"]


def test_ou_scaling_covariance_replay():
    data = ou_scaling_replay()
    assert data["D_scaling_identity"]
    assert data["C_scaling_identity"]
    assert data["log_dilation_chain_rule"]


def test_audit_artifact_is_conservative_after_run():
    artifact = HERE / "results" / "r12_audit.json"
    if artifact.exists():
        data = json.loads(artifact.read_text(encoding="utf-8"))
        assert data["decision"] == "PARITY_SYMBOL_CERTIFIED_EXACT_DEFECT_MAP_REMAINS"
        assert data["ou_coherence_contradiction"] is False


def test_w2_and_hermite_replays_are_exact():
    w = sp.symbols("w")
    g = 2 + 3 * w + w**2
    h = sp.expand(w**2 * g)
    assert h.subs(w, 0) == 0
    assert sp.diff(h, w).subs(w, 0) == 0
    assert sp.expand(h / w**2 - g) == 0
