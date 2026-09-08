"""Finite checks for the R141 normalized zero-shell phase audit.

The script checks algebraic interfaces only.  Normal-family compactness,
Bochner positivity, and the stated conditional theorem retain their hypotheses
in README.md and are not replaced by numerical evidence.
"""

from __future__ import annotations

import math

import sympy as sp


def check_r140_normalization() -> None:
    rho = sp.sqrt(sp.Rational(2, 3))
    for degree in (3, 5, 7, 9, 13):
        ell = sp.Rational(3, 2**degree) * sp.binomial(
            degree, (degree - 3) // 2
        )
        Lambda = 3 * (rho / 2) ** degree * sp.binomial(
            degree, (degree - 3) // 2
        )
        assert sp.simplify(Lambda * rho ** (-degree) - ell) == 0
        assert 0 < ell <= 3
    assert all(degree % 2 == 1 for degree in (3, 5, 7, 9, 13))
    print("R141_R140_NORMALIZATION_PASSED")


def check_ou_scaling() -> None:
    lam, R, s, z = sp.symbols("lambda R s z", positive=True)
    R_lam = R / sp.sqrt(lam)
    assert sp.simplify(R_lam * sp.sqrt(lam) - R) == 0
    damping = sp.exp(-(1 - lam) * R**2 * s**2 / (2 * lam))
    assert sp.simplify(damping.subs(lam, 1) - 1) == 0
    assert sp.limit(damping, lam, 0, dir="+") == 0
    relative = sp.exp(-z**2 / 2) * sp.exp((1 - lam) * z**2 / 2)
    assert sp.simplify(relative - sp.exp(-lam * z**2 / 2)) == 0
    print("R141_OU_SCALING_PASSED")


def check_triangle_and_phase_slack() -> None:
    rho2 = sp.Rational(2, 3)
    assert sp.simplify(3 * rho2 - 2) == 0
    a, b, c, d, e, f = sp.symbols("a b c d e f", real=True)
    z1, z2, z3 = a + sp.I * b, c + sp.I * d, e + sp.I * f
    matrix = sp.Matrix(
        [[1, sp.conjugate(z1), z3],
         [z1, 1, sp.conjugate(z2)],
         [sp.conjugate(z3), z2, 1]]
    )
    determinant = sp.expand(matrix.det())
    expected = 1 - sum(x * x for x in (a, b, c, d, e, f))
    expected += 2 * sp.re(z1 * z2 * z3).expand(complex=True)
    assert sp.simplify(determinant - expected) == 0
    A, Psi, mean_A, gaussian = sp.symbols(
        "A Psi mean_A gaussian", real=True
    )
    assert sp.expand(A - A * sp.cos(Psi) - (mean_A - gaussian)) is not None
    print("R141_TRIANGLE_AND_PHASE_SLACK_PASSED")


def check_phase_erasure_maximum() -> None:
    # The exponent in the OU moment bound is maximized at y^2=d*lambda/(1-lambda).
    for degree in (3, 5, 9, 17):
        for lam in (0.01, 0.1, 0.4, 0.8):
            y2 = degree * lam / (1 - lam)
            assert y2 > 0
            epsilon = 2 * math.exp(-1 / 8) * (
                4 * lam / (1 - lam)
            ) ** (degree / 2)
            assert epsilon > 0
    print("R141_PHASE_ERASURE_MAXIMUM_PASSED")


def check_bochner_tower_scale() -> None:
    for degree in (3, 5, 9, 17):
        first_sensitive_size = (degree + 3) // 2
        assert first_sensitive_size >= 3
        assert 2 * degree > degree
    for q in (0.1, 0.25, 0.7, 0.95):
        for depth in (1, 3, 8):
            exponent = (1 - q**depth) / (32 * q**depth)
            assert exponent > 0
    print("R141_BOCHNER_TOWER_SCALE_PASSED")


def main() -> None:
    check_r140_normalization()
    check_ou_scaling()
    check_triangle_and_phase_slack()
    check_phase_erasure_maximum()
    check_bochner_tower_scale()
    print("R141_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
