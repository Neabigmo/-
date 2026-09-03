from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1]))

from derive_radius_gap_bound import exact_hellinger_cauchy_schwarz, ou_scale_replay, radius_factor_bookkeeping
from replay_endpoint_symbol import endpoint_symbol_replay, fixed_band_replay
from audit_results import fredholm_defect_replay


def test_exact_radius_and_cs_replays():
    assert exact_hellinger_cauchy_schwarz()["sum_probability"] == "1"
    assert radius_factor_bookkeeping()["monomial_residual"] == "0"
    assert ou_scale_replay()["residual"] == "0"


def test_high_high_exponents():
    factors = radius_factor_bookkeeping()
    assert factors["two_high_claim"] == "(r/R)^(2N)"
    assert factors["three_high_claim"] == "(r/R)^(3N)"


def test_endpoint_and_gaussian_symbol():
    assert endpoint_symbol_replay()["residual"] == "0"
    assert endpoint_symbol_replay()["D_at_zero"] == "1"
    assert fixed_band_replay()["all_fixed_band_limits_exact"]


def test_fredholm_defect_functionals():
    replay = fredholm_defect_replay()
    assert replay["range_defect_residuals"] == ["0", "0"]
    assert replay["functional_matrix_rank"] == replay["multiplicity"] == 2
