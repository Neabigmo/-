from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from replay_tail_locality import (  # noqa: E402
    common_root_spectral_toy_replay,
    finite_support_dual_replay,
    lower_triangular_replay,
    tail_locality_sufficient_bound_replay,
    tail_normalization_selection_replay,
    compact_lower_triangular_column_replay,
    compact_without_triangularity_counterexample,
    actual_lower_triangular_support_audit,
    relative_dual_tail_inequality_replay,
)


def test_normalized_principal_diagonal_is_one():
    data = lower_triangular_replay()
    assert data["lower_triangular"]
    assert data["exact_diagonal_one"]


def test_tail_locality_sufficient_model_is_only_a_model():
    data = tail_locality_sufficient_bound_replay()
    assert data["finite_model_bound_holds"]
    assert data["r11_compactness_implies_this"] is False


def test_tail_normalization_selection():
    data = tail_normalization_selection_replay()
    assert data["all_selected_ratio_at_least_half"]
    assert data["selection_is_strictly_increasing"]


def test_finite_support_dual_terminal_contradiction():
    assert finite_support_dual_replay()["finite_support_nonzero_contradiction"]


def test_common_root_spectral_toy():
    data = common_root_spectral_toy_replay()
    assert data["common_case_has_root"]
    assert data["disjoint_case_has_no_common_root"]


def test_compact_lower_triangular_column_lemma_replay():
    data = compact_lower_triangular_column_replay()
    assert data["lower_triangular"]
    assert data["column_norms_decrease"]
    assert data["finite_model_column_norms_tend_to_zero"]


def test_compact_without_triangularity_is_not_enough():
    data = compact_without_triangularity_counterexample()
    assert data["compact"]
    assert not data["lower_triangular"]


def test_stage7_support_and_relative_dual_bound():
    assert actual_lower_triangular_support_audit()["output_index_ge_input_index"]
    assert relative_dual_tail_inequality_replay()["inequality_holds"]


def test_audit_artifact_is_conservative_after_run():
    artifact = HERE / "results" / "r13_audit.json"
    if artifact.exists():
        data = json.loads(artifact.read_text(encoding="utf-8"))
        assert data["decision"] == "EXACT_DEFECT_SURJECTIVITY_AWAY_FROM_COMMON_ZEROS_CERTIFIED"
        assert data["ou_coherence_contradiction"] if "ou_coherence_contradiction" in data else True
