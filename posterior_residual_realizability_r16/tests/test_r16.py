from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from replay_r16 import (
    cumulant_chain, conditional_q_moments, raw_order_rewrites,
    pearson_and_projection, tilted_law_checks,
    conditional_gaussian_completion_check, two_state_countermodel,
    fisher_deficit_algebra, sample_mean_tilt_derivatives,
)


def test_cumulant_chain():
    assert cumulant_chain()["exact_scale_audit"]


def test_raw_rewrites():
    got = raw_order_rewrites()
    assert got["order4_identity"] and got["order6_identity"]


def test_q_moments():
    assert all(conditional_q_moments()[2].values())


def test_corrected_tilt():
    got = tilted_law_checks()
    assert got["negative_sign_normalizes"]
    assert not got["positive_sign_normalizes"]
    assert conditional_gaussian_completion_check()["completed_square"]


def test_cone_and_countermodel():
    assert two_state_countermodel()["matches_target"]
    assert two_state_countermodel()["nonconstant"]


def test_fisher_and_tilt():
    assert "1/3" in str(fisher_deficit_algebra()["deduced"])
    W = sample_mean_tilt_derivatives()
    assert W["W_prime_zero"] and W["W_second_m3"]
