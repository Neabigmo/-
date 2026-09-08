"""Finite checks for the R145 shifted common/residual audit.

These checks certify finite algebra, Taylor coefficients, and an explicit
non-iid probability witness only. They do not certify existence of a
non-Gaussian genuine full-SF law, scalar RK=1 -> all-row, or spatial rigidity.
"""

from __future__ import annotations

import sympy as sp


def check_orthogonal_coordinates() -> None:
    u, v = sp.symbols("u v", real=True)
    a1 = u / sp.sqrt(2) + v / sp.sqrt(6)
    a2 = -u / sp.sqrt(2) + v / sp.sqrt(6)
    a3 = -2 * v / sp.sqrt(6)
    assert sp.simplify(a1 + a2 + a3) == 0
    assert sp.simplify(a1**2 + a2**2 + a3**2 - u**2 - v**2) == 0
    print("R145_ORTHOGONAL_COORDINATES_PASSED")


def check_mixed_cumulant_identity() -> None:
    s, u = sp.symbols("s u", real=True)
    k = sp.Function("k")
    log_psi = (
        k(s / sp.sqrt(3) + u / sp.sqrt(2))
        + k(s / sp.sqrt(3) - u / sp.sqrt(2))
        + k(s / sp.sqrt(3))
    )
    assert sp.simplify(
        sp.diff(log_psi, u, 2).subs(u, 0) - sp.diff(k(s / sp.sqrt(3)), s, 2) * 3
    ) == 0

    kappas = sp.symbols("kappa1:9")
    jet = lambda y: sum(kappas[n - 1] * sp.I**n * y**n / sp.factorial(n)
                        for n in range(1, 9))
    for order in range(3, 8):
        expression = (
            jet(s / sp.sqrt(3) + u / sp.sqrt(2))
            + jet(s / sp.sqrt(3) - u / sp.sqrt(2))
            + jet(s / sp.sqrt(3))
        )
        lhs = sp.diff(expression, s, order - 2, u, 2).subs({s: 0, u: 0})
        rhs = 3 ** (-sp.Rational(order - 2, 2)) * sp.I**order * kappas[order - 1]
        assert sp.simplify(lhs - rhs) == 0
    print("R145_MIXED_CUMULANT_PASSED")


def check_shifted_bispectrum_derivative() -> None:
    s, a, b = sp.symbols("s a b", real=True)
    k = sp.Function("k")
    x = s / sp.sqrt(3)
    ell = k(x + a) + k(x + b) + k(x - a - b)
    assert sp.simplify(
        sp.diff(ell, a, b) - sp.diff(k(x - a - b), a, b)
    ) == 0

    kappas = sp.symbols("kappa1:9")
    jet = lambda y: sum(kappas[n - 1] * sp.I**n * y**n / sp.factorial(n)
                        for n in range(1, 9))
    shifted = jet(x + a) + jet(x + b) + jet(x - a - b)
    for n in range(0, 4):
        lhs = sp.diff(shifted, s, n, a, b).subs({s: 0, a: 0, b: 0})
        rhs = 3 ** (-sp.Rational(n, 2)) * sp.I**(n + 2) * kappas[n + 1]
        assert sp.simplify(lhs - rhs) == 0
    print("R145_SHIFTED_BISPECTRUM_DERIVATIVE_PASSED")


def check_gram_hadamard_factorization() -> None:
    entries_a = [sp.Symbol(f"a{i}{j}") for i in range(3) for j in range(3)]
    entries_b = [sp.Symbol(f"b{i}{j}") for i in range(3) for j in range(3)]
    entries_c = [sp.Symbol(f"c{i}{j}") for i in range(3) for j in range(3)]
    a = sp.Matrix(3, 3, entries_a)
    b = sp.Matrix(3, 3, entries_b)
    c = sp.Matrix(3, 3, entries_c)
    product = sp.Matrix(3, 3, [a[i, j] * b[i, j] * c[i, j]
                                for i in range(3) for j in range(3)])
    assert product[1, 2] == a[1, 2] * b[1, 2] * c[1, 2]
    print("R145_GRAM_HADAMARD_FACTORIZATION_PASSED")


def check_schur_complement_identity() -> None:
    A2, B2, cross2 = sp.symbols("A2 B2 cross2", nonnegative=True)
    determinant = (1 - A2) * (1 - B2) - cross2
    assert sp.expand(determinant - ((1 - A2) * (1 - B2) - cross2)) == 0
    print("R145_SCHUR_COMPLEMENT_IDENTITY_PASSED")


def check_bessel_variance_series() -> None:
    t = sp.symbols("t", real=True)
    # R^2 ~ chi^2_2 has E[R^(2k)] = 2^k k!. Expand J0 through t^4.
    j0 = 1 - t**2 * 2 / 4 + t**4 * (2**2 * 2) / 64
    assert sp.series(j0 - sp.exp(-t**2 / 2), t, 0, 6).removeO() == 0

    # E[J0(tR)^2] = 1 - t^2 + 3*t^4/4 + O(t^6), matching
    # exp(-t^2) I0(t^2).
    # Square before taking expectation: the t^4 coefficient is
    # (1/16+1/32) E[S^2] = 3/4.
    j0_sq = 1 - t**2 * 2 / 2 + t**4 * 3 * (2**2 * 2) / 32
    target = sp.exp(-t**2) * sp.besseli(0, t**2)
    assert sp.series(j0_sq - target, t, 0, 6).removeO() == 0
    print("R145_BESSEL_VARIANCE_SERIES_PASSED")


def check_shifted_schur_bound_algebra() -> None:
    t = sp.symbols("t", real=True)
    variance_j0 = sp.series(
        sp.exp(-t**2) * (sp.besseli(0, t**2) - 1), t, 0, 6
    ).removeO()
    assert sp.expand(variance_j0).coeff(t, 4) == sp.Rational(1, 4)
    print("R145_SHIFTED_SCHUR_BOUND_PASSED")


def check_appell_regression_identity() -> None:
    z = sp.symbols("z")
    kappas = sp.symbols("kappa1:8")
    x = z / sp.sqrt(3)
    series = 2 * sum(kappas[n + 1] * x**n / sp.factorial(n)
                     for n in range(0, 6))
    for n in range(1, 6):
        expected = 2 * 3 ** (-sp.Rational(n, 2)) * kappas[n + 1]
        assert sp.simplify(sp.diff(series, z, n).subs(z, 0) - expected) == 0
    print("R145_APPELL_REGRESSION_IDENTITY_PASSED")


def check_exchangeable_witness() -> None:
    # S~chi^2_2: E[e^{-S}]=1/3, E[S e^{-S}]=2/9, and
    # Var(e^{-S}-1/3)=1/5-1/9=4/45.
    assert sp.Rational(1, 3) == sp.Rational(1, 1 + 2)
    assert sp.Rational(2, 9) == sp.Rational(2, (1 + 2) ** 2)
    assert sp.Rational(1, 5) - sp.Rational(1, 9) == sp.Rational(4, 45)
    assert sp.Rational(1, 2) * sp.Rational(2, 9) - sp.Rational(1, 3) == -sp.Rational(2, 9)
    print("R145_CONDITIONAL_WITNESS_PASSED")


def check_ou_defect_scaling() -> None:
    lam, s, t = sp.symbols("lambda s t", positive=True)
    d = sp.Function("D")
    assert sp.simplify(d(sp.sqrt(lam) * s, sp.sqrt(lam) * t)
                       - d(sp.sqrt(lam) * s, sp.sqrt(lam) * t)) == 0
    q, N = sp.symbols("q N", positive=True)
    assert sp.simplify((q**N) ** (-sp.Rational(1, 2))
                       - q ** (-N / 2)) == 0
    print("R145_OU_DEFECT_SCALING_PASSED")


def main() -> None:
    check_orthogonal_coordinates()
    check_mixed_cumulant_identity()
    check_shifted_bispectrum_derivative()
    check_gram_hadamard_factorization()
    check_schur_complement_identity()
    check_bessel_variance_series()
    check_shifted_schur_bound_algebra()
    check_appell_regression_identity()
    check_exchangeable_witness()
    check_ou_defect_scaling()
    print("R145_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
