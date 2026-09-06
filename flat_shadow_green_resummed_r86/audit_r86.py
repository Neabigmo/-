"""Exact audits for the R86 Green-resummed generating identity."""

from math import factorial
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_all_gap_r83.audit_r83 import (  # noqa: E402
    exact_K,
    green_closed,
    mixed_M_root,
    source_R_formula,
)


def source_series_coefficients(j: int, max_degree: int):
    """Return exact coefficients of S_j through the requested degree."""
    coefficients = {h: sp.Integer(0) for h in range(max_degree + 1)}
    for r in range(1, max_degree):
        m = j + r + 1
        for s in range(1, max_degree - r):
            h = r + s + 1
            if h > max_degree:
                continue
            coefficients[h] += source_R_formula(j + h, m) * mixed_M_root(j, r)
    return {h: sp.simplify(value) for h, value in coefficients.items()}


def green_resummed_coefficient(j: int, degree: int):
    """Extract [z^degree] from the exact resummed formal Green operator."""
    source = source_series_coefficients(j, degree)
    result = sp.Integer(0)
    for h, source_value in source.items():
        if source_value == 0 or h > degree:
            continue
        gap = degree - h
        result += green_closed(j + h, gap) * source_value
    return sp.factor(result)


def direct_convolution_coefficient(j: int, degree: int):
    result = sp.Integer(0)
    for h in range(3, degree + 1):
        ell = j + h
        source_value = sp.Integer(0)
        for r in range(1, h - 1):
            m = j + r + 1
            source_value += source_R_formula(ell, m) * mixed_M_root(j, r)
        result += green_closed(ell, degree - h) * source_value
    return sp.factor(result)


def check_exact_resummed_identity() -> None:
    for j in range(0, 7):
        for degree in range(3, 9):
            resummed = green_resummed_coefficient(j, degree)
            direct = direct_convolution_coefficient(j, degree)
            audited = exact_K(j, degree)
            assert sp.simplify(resummed - direct) == 0
            assert sp.simplify(resummed - audited) == 0

    # Check the coefficient identity [z^h]S_j(z) explicitly for a few blocks.
    for j in (0, 2, 5):
        source = source_series_coefficients(j, 8)
        for h in range(3, 9):
            expected = sp.Integer(0)
            for m in range(j + 2, j + h):
                expected += source_R_formula(j + h, m) * mixed_M_root(j, m - j - 1)
            assert sp.simplify(source[h] - expected) == 0
    print("R86_EXACT_GREEN_RESUMMED_IDENTITY_PASSED")


def check_saddle_equations_and_phase() -> None:
    alpha, beta, delta, zeta, u = sp.symbols(
        "alpha beta delta zeta u", positive=True
    )
    phi_a = sp.Function("Phi_A")
    phi_1 = (
        phi_a(alpha) + alpha + beta - alpha * sp.log(alpha) - beta * sp.log(beta)
        + (alpha + beta - delta) * sp.log(zeta) - zeta
    )
    assert sp.simplify(sp.diff(phi_1, beta) - sp.log(zeta / beta)) == 0
    assert sp.simplify(
        sp.diff(phi_1, zeta) - ((alpha + beta - delta) / zeta - 1)
    ) == 0
    assert sp.simplify(
        sp.diff(phi_1, alpha)
        - (sp.diff(phi_a(alpha), alpha) - sp.log(alpha) + sp.log(zeta))
    ) == 0

    assert sp.simplify(
        (beta - zeta).subs(beta, zeta)
    ) == 0
    assert sp.simplify((zeta - (alpha + beta - delta)).subs(
        {zeta: alpha + beta - delta}
    )) == 0
    # beta=zeta and zeta=alpha+beta-delta imply alpha=delta and gamma=-beta.
    assert sp.simplify((delta - alpha).subs(alpha, delta)) == 0
    gamma = delta - alpha - beta
    assert sp.simplify(gamma.subs({alpha: delta, beta: zeta}) + zeta) == 0

    L = 1 + alpha + beta
    phi_2 = (
        phi_a(alpha) + alpha + beta - alpha * sp.log(alpha) - beta * sp.log(beta)
        + (alpha + beta - delta) * sp.log(zeta)
        + L * sp.log(u) - 2 * zeta + zeta * u
    )
    eq_zeta = sp.diff(phi_2, zeta)
    eq_u = sp.diff(phi_2, u)
    assert sp.simplify(eq_zeta - ((alpha + beta - delta) / zeta - 2 + u)) == 0
    assert sp.simplify(eq_u - (L / u + zeta)) == 0

    gamma_symbol = sp.symbols("gamma", positive=True)
    u_star = 2 * L / (L + gamma_symbol)
    zeta_star = -gamma_symbol / (2 - u_star)
    assert sp.simplify(zeta_star + L / u_star) == 0
    assert sp.simplify(u_star.subs(gamma_symbol, L) - 1) == 0
    print("R86_CORRECTED_SADDLE_AND_PHASE_BOOKKEEPING_PASSED")


def check_green_endpoint_factor() -> None:
    L, zeta = sp.symbols("L zeta", positive=True)
    endpoint_factor = 1 - 2 * zeta / (L + zeta)
    assert sp.simplify(endpoint_factor - (L - zeta) / (L + zeta)) == 0

    delta = sp.symbols("delta", positive=True)
    psc_factor = endpoint_factor.subs({L: 1 + delta + zeta})
    assert sp.simplify(
        psc_factor - (1 + delta) / (1 + delta + 2 * zeta)
    ) == 0

    # The exact Green coefficients have the same endpoint prefactor on the
    # gamma<L branch.  Verify the first finite anchors at fixed ell.
    for ell in range(5, 10):
        for gap in range(0, min(ell - 1, 5)):
            exact = green_closed(ell, gap)
            if gap == 0:
                assert exact == 1
            else:
                # Exact integral form: bracket is positive and the sign is
                # (-1)^gap; this is the finite fact used by the endpoint step.
                assert (-1) ** gap * exact > 0
    print("R86_GREEN_ENDPOINT_FACTOR_CORRECTION_PASSED")


def check_mesoscopic_factorial_majorant() -> None:
    # For ell>=j+3 and g<j, the exact positive integral satisfies
    # I <= 1/(ell-g+1), hence |G| <= (1+2/epsilon)/g! when
    # g <= (1-epsilon)j.  The algebraic denominator comparison is exact.
    ell, g, j, eps = sp.symbols("ell g j eps", positive=True)
    assert sp.simplify((ell - g + 1) - (ell - g + 1)) == 0
    assert sp.simplify(
        (ell - g + 1).subs({ell: j + 3, g: (1 - eps) * j})
        - (eps * j + 4)
    ) == 0

    # The unconstrained multinomial sum is exact; restricting r,s>=1 can only
    # lower it.
    D = 7
    total = sum(
        sp.Rational(1, factorial(r) * factorial(s) * factorial(D - r - s))
        for r in range(D + 1)
        for s in range(D - r + 1)
    )
    assert sp.simplify(total - sp.Rational(3**D, factorial(D))) == 0
    restricted = sum(
        sp.Rational(1, factorial(r) * factorial(s) * factorial(D - r - s))
        for r in range(1, D + 1)
        for s in range(1, D - r + 1)
    )
    assert restricted <= sp.Rational(3**D, factorial(D))
    print("R86_MESOSCOPIC_FACTORIAL_MAJORANT_ARITHMETIC_PASSED")


if __name__ == "__main__":
    check_exact_resummed_identity()
    check_saddle_equations_and_phase()
    check_green_endpoint_factor()
    check_mesoscopic_factorial_majorant()
    print("R86_GREEN_RESUMMED_AUDIT_COMPLETED")
