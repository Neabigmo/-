import json
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).parents[1]))

from derive_radius_gap_bound import exact_hellinger_cauchy_schwarz, ou_scale_replay, radius_factor_bookkeeping
from replay_endpoint_symbol import endpoint_symbol_replay, fixed_band_replay
from audit_results import fredholm_defect_replay, main as audit_main


def test_exact_radius_and_cs_replays():
    cs = exact_hellinger_cauchy_schwarz()
    assert cs["sum_probability"] == "1"
    assert sp.sympify(cs["cs_slack"]) >= 0
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


def test_published_audit_artifact():
    audit_main()
    artifact = json.loads((Path(__file__).parents[1] / "results" / "r8_audit.json").read_text(encoding="utf-8"))
    assert artifact["exact_replays_pass"] is True
    assert artifact["marker"] == "R8_ANALYTIC_RADIUS_AUDIT_COMPLETED"
    assert artifact["decision"] == "RADIUS_GAP_COMPACTNESS_CERTIFIED_FREDHOLM_GAP_REMAINS"
    assert artifact["fredholm_defect_replay"]["functional_matrix_rank"] == 2
