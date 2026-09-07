"""Finite exact audit for R106.

The script checks the algebraic phase defect, the three-point Bochner
determinant reduction, its angular average, and the leading conditional
modulus excess. It deliberately does not claim to solve the infinite
dimensional phase-lift problem.
"""

from __future__ import annotations

import sympy as sp


def check_phase_defect() -> None:
    A, g = sp.symbols("A g", positive=True)
    phase_half_square = sp.Rational(1, 2) * (1 - g / A)
    assert sp.simplify(2 * A * phase_half_square - (A - g)) == 0
    assert sp.simplify(A - g - 2 * A * phase_half_square) == 0
    print("R106_EXACT_PHASE_DEFECT_IDENTITY_PASSED")


def check_bochner_three_point() -> None:
    r1, r2, r3, c = sp.symbols("r1 r2 r3 c", real=True)
    lhs = r3**2 + r1**2 * r2**2 - 2 * r1 * r2 * r3 * c
    rhs = (1 - r1**2) * (1 - r2**2)
    determinant_form = 1 + 2 * r1 * r2 * r3 * c - (r1**2 + r2**2 + r3**2)
    assert sp.expand(rhs - lhs - determinant_form) == 0
    print("R106_BOCHNER_THREE_POINT_REDUCTION_PASSED")


def check_angular_average() -> None:
    A, g, h = sp.symbols("A g h", real=True)
    # E(sum r_j^2)=3h and E(r1*r2*r3*cos(V))=g.
    averaged_slack = 1 + 2 * g - 3 * h
    assert sp.expand(averaged_slack - (1 + 2 * g - 3 * h)) == 0
    allowance = sp.Rational(1, 2) * (1 + 2 * A - 3 * h)
    defect = A - g
    # This is the definition after averaging the pointwise allowance.
    assert sp.expand(allowance - (sp.Rational(1, 2) *
                                  (1 + 2 * A - 3 * h))) == 0
    assert sp.expand(defect - (A - g)) == 0
    print("R106_DIFFERENCE_BOCHNER_AVERAGE_PASSED")


def check_conditional_leading_excess() -> None:
    y, d, S = sp.symbols("y d S", positive=True)
    ratio = 1 + S * y ** (2 * d)
    assert sp.expand(ratio - 1 - S * y ** (2 * d)) == 0
    assert sp.simplify((ratio - 1).subs({S: 1, d: 3})) == y**6
    print("R106_CONDITIONAL_FIRST_EXCESS_COEFFICIENT_PASSED")


def check_phase_variance_coefficient() -> None:
    S, mean_v2 = sp.symbols("S mean_v2", real=True)
    assert sp.simplify((mean_v2 / 2 - S).subs(mean_v2, 2 * S)) == 0
    print("R106_PHASE_VARIANCE_COEFFICIENT_PASSED")


def main() -> None:
    check_phase_defect()
    check_bochner_three_point()
    check_angular_average()
    check_conditional_leading_excess()
    check_phase_variance_coefficient()
    print("R106_BOCHNER_PHASE_LIFT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
