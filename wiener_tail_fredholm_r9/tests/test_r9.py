import json
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).parents[1]))

from audit_results import main as audit_main
from exact_kernel_bound import central_binomial_replay, normalized_multinomial_bound, wiener_tail_replay
from replay_normalization import fixed_band_replay, normalization_replay
from replay_wiener_range import division_replay


def test_normalization_and_fixed_band():
    assert normalization_replay()["residual"] == "0"
    assert fixed_band_replay()["all_limits_exact"]


def test_kernel_and_wiener_bounds():
    assert central_binomial_replay()["all_bounds_hold"]
    assert normalized_multinomial_bound()["all_multinomial_terms_le_a_star_n"]
    tail = wiener_tail_replay()
    assert tail["tail_decreases_in_replay"]
    assert sp.sympify(tail["rows"][-1]["two_high_bound"]) < 1


def test_single_radius_division():
    assert division_replay(multiplicity=1)["division_exact"]
    assert division_replay(multiplicity=2)["division_exact"]
    replay = division_replay(multiplicity=2)
    assert replay["range_functionals_on_good_remainder"] == ["0", "0"]
    assert replay["outside_has_nonzero_defect"]


def test_published_audit_artifact():
    audit_main()
    artifact = json.loads((Path(__file__).parents[1] / "results" / "r9_audit.json").read_text(encoding="utf-8"))
    assert artifact["exact_replays_pass"] is True
    assert artifact["marker"] == "R9_WIENER_TAIL_FREDHOLM_AUDIT_COMPLETED"
    assert artifact["decision"] == "NORMALIZATION_REPAIRED_BUT_SYMBOL_LIMIT_NOT_UNIFORM"
