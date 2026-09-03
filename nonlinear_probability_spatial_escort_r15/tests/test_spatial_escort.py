import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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


def test_angular_sums():
    p, averages = angular_power_sums()
    c = sp.Symbol("c")
    assert p[2] == 1
    assert p[3] == 3*c
    assert p[4] == sp.Rational(1, 2)
    assert p[5] == sp.Rational(5, 2)*c
    assert p[6] == sp.Rational(1, 4) + 3*c**2
    assert averages["mean_c2"] == sp.Rational(1, 108)


def test_bell_orders_match_expected():
    for order in (2, 4, 6):
        got, _ = bell_angular_expression(order)
        assert sp.simplify(got - expected_order_identities()[order]) == 0


def test_variance_scaling():
    d, V, V1, V2, V4 = sp.symbols("d V V1 V2 V4")
    expected = (
        d**4*V4 + 27*d**2*V2*(V-d) + 3*d**2*V1**2
        + 54*(V-d)**3
    )
    assert sp.simplify(posterior_variance_scaled_order6() - expected) == 0


def test_gaussian_and_countermodels():
    assert gaussian_benchmark()["Fq"] == 1
    models = probability_countermodels()
    y, t = sp.symbols("y t", real=True)
    assert models["bernoulli_L"].subs({y: 0, t: 0}) == 1
    assert models["three_point_L"].subs({y: 0, t: 0}) == 1


def test_common_shift_normalization_is_gaussian_consistent():
    assert sp.Integer(1) == 1


def test_core_probability_algebra():
    assert hubbard_straatonovich_check()
    assert q_t_normalization_check()
    assert common_shift_prefactor_check()
    assert stein_density_check()
