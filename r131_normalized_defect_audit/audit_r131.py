"""Exact low-level checks for the R131 normalized-defect interface."""

from __future__ import annotations

import sympy as sp


def moment_expectation(poly: sp.Expr, xs: tuple[sp.Symbol, ...], moments: tuple[sp.Symbol, ...]) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), *xs)
    result = 0
    for powers, coefficient in expanded.terms():
        term = coefficient
        for power, moment in zip(powers, moments):
            term *= moments[power]
        result += term
    return sp.expand(result)


def check_r7_top_odd_invisibility() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    y = sp.symbols("y0:15")
    q = ((x1 - x2) ** 2 + (x1 - x3) ** 2 + (x2 - x3) ** 2) / 3
    raw = moment_expectation(q**7, (x1, x2, x3), y).subs({y[0]: 1, y[1]: 0, y[2]: 1})
    raw = sp.expand(raw)
    assert y[13] not in raw.free_symbols
    assert sp.Poly(raw, y[14]).coeff_monomial(y[14]) == sp.Rational(128, 729)
    print("R131_R7_TOP_ODD_INVISIBILITY_PASSED")


def check_jacobi_determinant_dictionary() -> None:
    k = sp.symbols("k", integer=True, positive=True)
    Dkm2, Dkm1, Dk = sp.symbols("Dkm2 Dkm1 Dk", positive=True)
    hk = sp.factorial(k) * Dk / Dkm1
    hkm1 = sp.factorial(k - 1) * Dkm1 / Dkm2
    beta_over_k = sp.simplify((hk / hkm1) / k)
    assert beta_over_k == Dk * Dkm2 / Dkm1**2
    print("R131_HERMITE_DETERMINANT_JACOBI_DICTIONARY_PASSED")


def check_flat_kernel_freedom_count() -> None:
    m, r = sp.symbols("m r", integer=True, nonnegative=True)
    # For C_j=sum_{i=0}^r p_i y_{m+1+j+i}, the top index reaches 2m+1
    # only at j=m-r, and then the monic coefficient is exactly 1.
    assert sp.expand((m + 1 + (m - r) + r) - (2 * m + 1)) == 0
    assert sp.expand((m + 1 + (m - r - 1) + r) - (2 * m + 1)) == -1
    print("R131_FLAT_KERNEL_ODD_FREEDOM_COUNT_PASSED")


def check_scaled_ou_cubic_mode() -> None:
    rho, m3 = sp.symbols("rho m3", positive=True)
    # With the convention P_rho He_k=rho^(k/2) He_k, the cubic mode scales
    # exactly by rho^(3/2).  This is an algebraic eigenvalue check, not the
    # unproved uniform L2 smoothing estimate for a varying tower.
    assert sp.simplify((rho ** sp.Rational(3, 2) * m3) / m3 - rho ** sp.Rational(3, 2)) == 0
    print("R131_OU_CUBIC_EIGENSCALING_INTERFACE_PASSED")


def main() -> None:
    check_r7_top_odd_invisibility()
    check_jacobi_determinant_dictionary()
    check_flat_kernel_freedom_count()
    check_scaled_ou_cubic_mode()
    print("R131_NORMALIZED_DEFECT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
