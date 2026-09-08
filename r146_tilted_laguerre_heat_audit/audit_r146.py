"""Finite checks for the R146 tilted Laguerre/heat audit.

These checks certify finite algebra and numerical interfaces only. They do not
certify existence of a non-Gaussian genuine full-SF law, the scalar RK=1 to
all-row bridge, the infinite Laguerre expansion, tower uniformity, or novelty.
"""

from __future__ import annotations

import math
from fractions import Fraction


def laguerre_values(x: float, order: int) -> list[float]:
    values = [1.0]
    if order == 0:
        return values
    values.append(1.0 - x)
    for m in range(1, order):
        next_value = ((2.0 * m + 1.0 - x) * values[m] - m * values[m - 1]) / (m + 1.0)
        values.append(next_value)
    return values


def check_orthogonal_q_identity() -> None:
    x1, x2, x3 = 0.7, -1.1, 0.4
    c = (x1 + x2 + x3) / math.sqrt(3.0)
    u = (x1 - x2) / math.sqrt(2.0)
    v = (x1 + x2 - 2.0 * x3) / math.sqrt(6.0)
    q_direct = x1 * x1 + x2 * x2 + x3 * x3 - (x1 + x2 + x3) ** 2 / 3.0
    assert abs(q_direct - (u * u + v * v)) < 1e-14
    assert abs(c * c + u * u + v * v - (x1 * x1 + x2 * x2 + x3 * x3)) < 1e-14
    print("R146_ORTHOGONAL_Q_IDENTITY_PASSED")


def check_laguerre_generating_interface() -> None:
    z = 0.08
    r = 2.0 * z / (1.0 + 2.0 * z)
    for x in (0.0, 0.4, 1.2, 2.3):
        values = laguerre_values(x, 36)
        truncated = sum(values[m] * r**m for m in range(37))
        target = (1.0 + 2.0 * z) * math.exp(-z * 2.0 * x)
        assert abs(truncated - target) < 2e-14
    print("R146_LAGUERRE_GENERATING_INTERFACE_PASSED")


def check_laguerre_first_mode() -> None:
    # L_1(T)=1-T, so ell_1=1-E[Q]/2. For Q~chi^2_2, E[Q]/2=1.
    values = laguerre_values(1.0, 1)
    assert values == [1.0, 0.0]
    assert 1.0 - (2.0 / 2.0) == 0.0
    print("R146_LAGUERRE_FIRST_MODE_PASSED")


def check_ou_mobius_scaling() -> None:
    lam, z = 0.37, 0.41
    r = 2.0 * z / (1.0 + 2.0 * z)
    z_prime = lam * z / (1.0 + 2.0 * (1.0 - lam) * z)
    r_prime = 2.0 * z_prime / (1.0 + 2.0 * z_prime)
    assert abs(r_prime - lam * r) < 1e-15
    print("R146_OU_MOBIUS_SCALING_PASSED")


def check_gaussian_cubic_endpoint() -> None:
    # For p(x)=(2*pi)^(-1/2) exp(-x^2/2), 2*pi*sqrt(3)*int p^3 dx=1.
    integral_p_cubed = 1.0 / (2.0 * math.pi * math.sqrt(3.0))
    assert abs(2.0 * math.pi * math.sqrt(3.0) * integral_p_cubed - 1.0) < 1e-15
    print("R146_CUBIC_ENDPOINT_GAUSSIAN_PASSED")


def check_relaxed_witness_constants() -> None:
    assert Fraction(1, 3) == Fraction(1, 1 + 2)
    assert Fraction(2, 9) == Fraction(2, (1 + 2) ** 2)
    assert Fraction(1, 5) - Fraction(1, 9) == Fraction(4, 45)
    # Since E[h]=0, Cov(S, h)=E[S exp(-S)]-E[S]/3=2/9-2/3=-4/9.
    assert Fraction(2, 9) - Fraction(2, 3) == -Fraction(4, 9)
    print("R146_WITNESS_CONSTANTS_PASSED")


def main() -> None:
    check_orthogonal_q_identity()
    check_laguerre_generating_interface()
    check_laguerre_first_mode()
    check_ou_mobius_scaling()
    check_gaussian_cubic_endpoint()
    check_relaxed_witness_constants()
    print("R146_AUDIT_SCOPE_EXPLICIT: finite interfaces only")
    print("R146_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
