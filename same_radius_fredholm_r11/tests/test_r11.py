from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from audit_same_radius import division_index
from complete_proof_audit import all_degree_formula_certificate, operator_proof_certificate
from derive_exact_Aijk import angular_kernel, direct_angular_constant, roots_of_unity_filter, beta_moment, direct_beta_integral
from replay_dominant_bound import dominant_bound_replay, global_bound_replay


def test_beta_correction_small_exact_set():
    assert all(sp.simplify(beta_moment(n, p) - direct_beta_integral(n, p)) == 0 for n in (8, 10, 12) for p in range(7))


def test_angular_kernel_matches_both_extractions_through_degree_8():
    for i in range(9):
        for j in range(9 - i):
            for k in range(9 - i - j):
                assert sp.simplify(angular_kernel(i, j, k) - direct_angular_constant(i, j, k)) == 0
                assert sp.simplify(angular_kernel(i, j, k) - roots_of_unity_filter(i, j, k)) == 0


def test_global_and_dominant_replays():
    assert global_bound_replay()["all_finite_replays_hold"]
    assert dominant_bound_replay()["all_ratio_bounds_hold"]


def test_even_index_simple_and_double_zero():
    for m in (1, 2):
        row = division_index(m)
        assert row["division_exact"] and row["good_defects_zero"] and row["outside_defect_nonzero"]
        assert row["index"] == -m


def test_published_audit_artifact_has_conservative_boundary(tmp_path):
    # The published artifact is checked for schema without rewriting it.
    artifact = HERE / "results" / "r11_audit.json"
    if artifact.exists():
        data = json.loads(artifact.read_text(encoding="utf-8"))
        assert data["decision"] == "ACTUAL_KERNEL_CERTIFIED_SAME_RADIUS_COMPACTNESS_GAP"
        assert data["gaussian_normalization"] == {"R": "1", "D_R": "1", "correct": True}


def test_all_degree_and_same_radius_proof_certificates():
    assert all_degree_formula_certificate()["all_degree_symbolic_proof"]
    assert operator_proof_certificate()["symbolic_sanity"]
