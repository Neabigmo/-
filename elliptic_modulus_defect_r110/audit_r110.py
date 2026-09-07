"""Exact symbolic audit for R110.

The audit checks the finite algebra behind the Gaussian-relative modulus defect,
the OU and elliptic scalings, the d=3 positive local coefficient, and the
genuine R107 varying-bottom obstruction.  It does not claim the uniform
modulus envelope or the final rigidity theorem.
"""

from __future__ import annotations

import sympy as sp


def moment(values: tuple[sp.Expr, ...], probabilities: tuple[sp.Expr, ...], n: int) -> sp.Expr:
    return sp.simplify(sum(p * x**n for x, p in zip(values, probabilities)))


def check_ou_defect_transport() -> None:
    r, tau = sp.symbols("r tau", positive=True)
    cancellation = sp.simplify(-(1 - tau) * r**2 / 2 + r**2 / 2 - tau * r**2 / 2)
    assert cancellation == 0
    q, N = sp.symbols("q N", positive=True)
    assert sp.simplify((q**(N / 2))**6 - q**(3 * N)) == 0
    print("R110_OU_RELATIVE_MODULUS_TRANSPORT_PASSED")


def check_positivity_majorant_and_ellipse() -> None:
    q, N, s, t = sp.symbols("q N s t", positive=True)
    y2 = 6 * s**2 + 6 * s * t + 2 * t**2
    radii = (s, s + t, 2 * s + t)
    assert sp.expand(sum(x**2 for x in radii) - y2) == 0
    assert sp.expand(
        sum(-(1 - q**N) * x**2 / 2 for x in radii)
        + (1 - q**N) * y2 / 2
    ) == 0
    remainder = sp.Poly(sp.expand(y2**3 - sum(x**6 for x in radii)), s, t)
    assert all(coefficient >= 0 for coefficient in remainder.coeffs())
    print("R110_POSITIVITY_MAJORANT_AND_ELLIPSE_PASSED")


def check_first_odd_d3_coefficient() -> None:
    r, kappa3, kappa6 = sp.symbols("r kappa3 kappa6", real=True)
    exactness = sp.simplify((kappa6 + 3 * kappa3**2).subs(kappa6, -3 * kappa3**2))
    assert exactness == 0
    coefficient = sp.simplify((-kappa6 / sp.factorial(6)).subs(kappa6, -3 * kappa3**2))
    assert coefficient == kappa3**2 / 240
    print("R110_D3_POSITIVE_MODULUS_COEFFICIENT_PASSED")


def check_r107_varying_bottom_obstruction() -> None:
    p = (1 - 1 / sp.sqrt(3)) / 2
    q = sp.simplify(1 - p)
    a = sp.sqrt(3)
    u = sp.simplify(p * q)
    assert u == sp.Rational(1, 6)

    values = (-2 * p * a, (1 - 2 * p) * a, 2 * q * a)
    probs = (q**2, 2 * u, p**2)
    assert sp.simplify(sum(probs) - 1) == 0
    assert moment(values, probs, 1) == 0
    assert moment(values, probs, 2) == 1
    assert moment(values, probs, 3) == 1
    assert moment(values, probs, 4) == 3
    m6 = moment(values, probs, 6)
    kappa6 = sp.simplify(m6 - 15 * 3 - 10 * 1**2 + 30)
    assert kappa6 == -6

    tau = sp.symbols("tau", positive=True)
    kappa3_tau = tau ** sp.Rational(3, 2)
    kappa6_tau = -6 * tau**3
    assert sp.simplify(kappa3_tau**2 - tau**3) == 0
    assert sp.simplify(kappa6_tau + 6 * tau**3) == 0
    local_defect = sp.simplify(-kappa6_tau / sp.factorial(6))
    assert local_defect == tau**3 / 120
    assert sp.simplify(kappa6_tau + 3 * kappa3_tau**2) == -3 * tau**3
    print("R110_R107_VARYING_BOTTOM_OBSTRUCTION_PASSED")


def check_conditional_uniform_theorem() -> None:
    q, N = sp.symbols("q N", positive=True)
    x1, x2, x3 = sp.symbols("x1 x2 x3", nonnegative=True)
    polynomial = sp.Poly(
        sp.expand((x1 + x2 + x3)**3 - (x1**3 + x2**3 + x3**3)),
        x1, x2, x3,
    )
    assert all(coefficient >= 0 for coefficient in polynomial.coeffs())
    assert sp.simplify((q**(N / 2))**6 - q**(3 * N)) == 0
    print("R110_CONDITIONAL_UNIFORM_Q3N_SCALE_ALGEBRA_PASSED")


def main() -> None:
    check_ou_defect_transport()
    check_positivity_majorant_and_ellipse()
    check_first_odd_d3_coefficient()
    check_r107_varying_bottom_obstruction()
    check_conditional_uniform_theorem()
    print("R110_ELLIPTIC_MODULUS_DEFECT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
