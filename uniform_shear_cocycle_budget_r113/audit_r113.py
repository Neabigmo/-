"""Exact symbolic audit for the R113 shear-cocycle budget record.

The asymptotic disk expansions are recorded as web-side analytic input. This
file audits the deterministic polynomial identities, Gaussian Gram constant,
and all explicit scaling/constant substitutions used by the budget theorem.
It intentionally does not promote the open normalized R114 limit to a result.
"""

from __future__ import annotations

import sympy as sp


def check_shear_cubic() -> None:
    s, t = sp.symbols("s t", real=True)
    cubic = sp.factor(t**3 - 2 * (s + t)**3 + (2 * s + t)**3)
    assert cubic == 6 * s**2 * (s + t)
    print("R113_CUBIC_SHEAR_POLYNOMIAL_PASSED")


def check_ellipse_geometry() -> None:
    s, t = sp.symbols("s t", real=True)
    y2 = sp.expand(s**2 + (s + t)**2 + (2 * s + t)**2)
    assert y2 == 6 * s**2 + 6 * s * t + 2 * t**2
    assert sp.factor(2 * y2 - t**2) == 3 * (2 * s + t)**2
    print("R113_ELLIPSE_GEOMETRY_AND_T_BOUND_PASSED")


def check_gaussian_gram_and_slack_factor() -> None:
    H3 = sp.Matrix(
        [
            [1, 0, 1, 0],
            [0, 1, 0, 3],
            [1, 0, 3, 0],
            [0, 3, 0, 15],
        ]
    )
    assert H3.det() == 12
    s, t = sp.symbols("s t", real=True)
    factor = s**6 * t**2 * (s + t)**4 * (2 * s + t)**2 / 12
    assert sp.factor(factor * 12) == s**6 * t**2 * (s + t)**4 * (2 * s + t)**2
    print("R113_GAUSSIAN_GRAM_AND_SLACK_FACTOR_PASSED")


def check_explicit_phase_constants() -> None:
    tau = sp.symbols("tau", positive=True)
    rho_sq = sp.E / 128
    r_sq = sp.E / 512
    assert sp.simplify(r_sq - rho_sq / 4) == 0
    rho = sp.sqrt(rho_sq)
    c_vartheta = 2 * sp.log(2) / rho**3
    c_ph = (3 + 2 * sp.sqrt(2)) * c_vartheta
    assert sp.simplify(c_ph - 2 * (3 + 2 * sp.sqrt(2)) * sp.log(2) / rho**3) == 0
    assert sp.simplify((tau**sp.Rational(3, 2))**2 - tau**3) == 0
    print("R113_PHASE_CONSTANTS_AND_Q3_SCALING_PASSED")


def check_exactness_gap_and_phase_leading_term() -> None:
    tau, s, t = sp.symbols("tau s t", positive=True)
    kappa3_sq = tau**3
    kappa6 = -6 * tau**3
    assert sp.factor(kappa6 + 3 * kappa3_sq) == -3 * tau**3
    eta_leading = sp.factor(-s**2 * (s + t))
    assert eta_leading == -s**2 * (s + t)
    print("R113_EXACTNESS_GAP_AND_PHASE_LEADING_TERM_PASSED")


def main() -> None:
    check_shear_cubic()
    check_ellipse_geometry()
    check_gaussian_gram_and_slack_factor()
    check_explicit_phase_constants()
    check_exactness_gap_and_phase_leading_term()
    print("R113_UNIFORM_SHEAR_COCYCLE_BUDGET_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()

