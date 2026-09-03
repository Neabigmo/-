import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from replay_r17 import (
    conditional_second_coefficients,
    fisher_dictionary_check,
    laguerre_generating_function,
    laguerre_orthogonality,
    laguerre_product_checks,
    target_moment_eliminations,
    tilted_mean_coefficients,
    triangularity_checks,
)


def test_laguerre_basics():
    assert laguerre_orthogonality()["verified"]
    assert laguerre_generating_function()["verified"]
    assert laguerre_product_checks()["verified"]


def test_tilted_mean_coefficients():
    assert tilted_mean_coefficients()["verified"]


def test_second_moment_coefficients():
    assert conditional_second_coefficients()["verified"]


def test_target_eliminations_and_triangularity():
    assert target_moment_eliminations()["verified"]
    assert triangularity_checks()["verified"]


def test_fisher_dictionary():
    assert fisher_dictionary_check()["verified"]
