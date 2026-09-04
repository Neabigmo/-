import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from replay_r18 import audit, abel_kernel, direct_abel_kernel, endpoint_witness
import sympy as sp


def test_kernel_matches_exact_integral_formula():
    r = sp.Rational(2, 5)
    assert all(abel_kernel(i, j, r) == direct_abel_kernel(i, j, r)
               for i in range(5) for j in range(5))


def test_endpoint_witness_is_nonzero_and_noncoercive():
    got = endpoint_witness()
    assert got["m_of_t"] == "t"
    assert got["quadratic_form_at_r_1_minus_s"] == "2*s**2"
    assert got["uniform_endpoint_coercivity"] is False


def test_audit_does_not_overclaim():
    got = audit()
    assert got["claims"]["abel_formula_exact"]
    assert got["claims"]["full_D_r_derived"] is False
    assert got["claims"]["c_equals_zero_proved"] is False
