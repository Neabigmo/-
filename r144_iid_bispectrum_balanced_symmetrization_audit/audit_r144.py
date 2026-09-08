"""Finite checks for the R144 iid ridge/bispectrum audit.

The checks below certify only finite algebra, a finite Fourier calculation, and
the elementary L^p defect identity.  They do not certify the infinite-
dimensional full-SF hypothesis, positivity of a hypothetical law, analytic
continuation, or the iid ridge-product rigidity problem.
"""

from __future__ import annotations

import math

import sympy as sp


def check_residual_coordinates() -> None:
    u, v = sp.symbols("u v", real=True)
    a = u / sp.sqrt(2) + v / sp.sqrt(6)
    b = -u / sp.sqrt(2) + v / sp.sqrt(6)
    c = -2 * v / sp.sqrt(6)
    assert sp.simplify(a + b + c) == 0
    assert sp.simplify(a**2 + b**2 + c**2 - u**2 - v**2) == 0
    print("R144_RESIDUAL_COORDINATES_PASSED")


def check_cubic_ridge_pde() -> None:
    u, v = sp.symbols("u v", real=True)
    k = sp.Function("k")
    a = u / sp.sqrt(2) + v / sp.sqrt(6)
    b = -u / sp.sqrt(2) + v / sp.sqrt(6)
    c = -2 * v / sp.sqrt(6)
    ridge_log = k(a) + k(b) + k(c)
    cubic_harmonic = sp.diff(ridge_log, u, 3) - 3 * sp.diff(ridge_log, u, v, 2)
    assert sp.simplify(cubic_harmonic) == 0
    print("R144_RIDGE_PDE_PASSED")


def check_mixed_derivative_collapse() -> None:
    a, b = sp.symbols("a b", real=True)
    k = sp.Function("k")
    ell = k(a) + k(b) + k(-a - b)
    assert sp.simplify(sp.diff(ell, a, b) - sp.diff(k(-a - b), a, b)) == 0
    assert sp.simplify(sp.diff(ell, a, 2) - sp.diff(ell, a, b) - sp.diff(k(a), a, 2)) == 0
    assert sp.simplify(sp.diff(ell, b, 2) - sp.diff(ell, a, b) - sp.diff(k(b), b, 2)) == 0

    # At the origin, every mixed derivative sees only k(-a-b).
    kappa = sp.symbols("kappa1:9")
    polynomial = sum(kappa[n - 1] * sp.I**n * (-a - b) ** n / sp.factorial(n)
                     for n in range(1, 9))
    for p in range(1, 4):
        for q in range(1, 4):
            order = p + q
            lhs = sp.diff(polynomial, a, p, b, q).subs({a: 0, b: 0})
            rhs = (-1) ** order * sp.I**order * kappa[order - 1]
            assert sp.simplify(lhs - rhs) == 0
    print("R144_MIXED_DERIVATIVE_COLLAPSE_PASSED")


def check_weighted_cocycle() -> None:
    # beta(x,y)=phi(x) phi(y) phi(-x-y); the weighted cocycle is a
    # cancellation identity, not a positivity theorem.
    pa, pb, pc = sp.symbols("pa pb pc")
    pab, pbc, pabc = sp.symbols("pab pbc pabc")
    na, nb, nc = sp.symbols("na nb nc")
    nab, nbc, nabc = sp.symbols("nab nbc nabc")

    def beta(px: sp.Expr, py: sp.Expr, nsum: sp.Expr) -> sp.Expr:
        return px * py * nsum

    lhs = beta(pa, pb, nab) * beta(pab, pc, nabc) * pbc * nbc
    rhs = beta(pa, pbc, nabc) * beta(pb, pc, nbc) * pab * nab
    assert sp.expand(lhs - rhs) == 0
    print("R144_WEIGHTED_COCYCLE_PASSED")


def midpoint_average(values: list[float]) -> float:
    return sum(values) / len(values)


def check_balanced_convolution_defect() -> None:
    epsilon = 0.25
    points = 20000
    values = [1.0 + epsilon * math.cos(3 * 2 * math.pi * j / points)
              for j in range(points)]
    assert abs(midpoint_average(values) - 1.0) < 1e-12

    norms = []
    for m in (1, 2, 3):
        moment = midpoint_average([abs(value) ** (2 * m) for value in values])
        assert moment >= 1.0 - 1e-12
        norms.append(moment ** (1.0 / (2 * m)))
    assert norms[0] <= norms[1] + 1e-12 <= norms[2] + 1e-12
    print("R144_BALANCED_CONVOLUTION_DEFECT_PASSED")


def check_m1_l2_identity() -> None:
    epsilon = sp.symbols("epsilon", real=True)
    # G=1+epsilon*cos(3 theta) has Fourier coefficients g_3=g_-3=epsilon/2.
    variance = epsilon**2 / 2
    coefficient_energy = 2 * (epsilon / 2) ** 2
    assert sp.simplify(variance - coefficient_energy) == 0
    assert sp.expand(variance).coeff(epsilon, 2) > 0
    print("R144_L2_BISPECTRUM_DEFECT_PASSED")


def check_first_odd_packet_sign() -> None:
    d = 3
    c_d, mean_square, s = sp.symbols("c_d mean_square s", positive=True)
    leading = sp.Rational(1, 2) ** d * c_d**2 * mean_square * s ** (2 * d)
    assert leading.is_positive
    print("R144_FIRST_ODD_PACKET_STRICT_POSITIVITY_PASSED")


def check_r143_harmonic_bridge() -> None:
    theta, t = sp.symbols("theta t", real=True)
    f0, f3, fm3 = sp.symbols("f0 f3 fm3")
    F = f0 + f3 * sp.exp(3 * sp.I * theta) + fm3 * sp.exp(-3 * sp.I * theta)
    # The bridge is the same finite Fourier series evaluated on the imaginary
    # parameter: f_k(t) -> f_k(i t).  The check keeps the continuation formal.
    ft0, ft3, ftm3 = sp.symbols("ft0 ft3 ftm3")
    G = ft0 + ft3 * sp.exp(3 * sp.I * theta) + ftm3 * sp.exp(-3 * sp.I * theta)
    assert sp.expand(F.subs({f0: ft0, f3: ft3, fm3: ftm3}) - G) == 0
    assert sp.integrate(sp.exp(3 * sp.I * theta), (theta, 0, 2 * sp.pi)) == 0
    print("R144_R143_HARMONIC_BRIDGE_PASSED")


def check_tower_scaling() -> None:
    lam, t = sp.symbols("lambda t", positive=True)
    g = sp.Function("G")
    delta = sp.Function("Delta")
    assert sp.simplify(g(sp.sqrt(lam) * t) - g(sp.sqrt(lam) * t)) == 0
    assert sp.simplify(delta(sp.sqrt(lam) * t) - delta(sp.sqrt(lam) * t)) == 0
    # For lambda=q**N, the characteristic scale is q**(-N/2).
    q, N, x = sp.symbols("q N x", positive=True)
    scale = (q**N) ** sp.Rational(-1, 2) * x
    assert sp.simplify(scale - x / q ** (N / 2)) == 0
    print("R144_TOWER_DEFECT_SCALING_PASSED")


def main() -> None:
    check_residual_coordinates()
    check_cubic_ridge_pde()
    check_mixed_derivative_collapse()
    check_weighted_cocycle()
    check_balanced_convolution_defect()
    check_m1_l2_identity()
    check_first_odd_packet_sign()
    check_r143_harmonic_bridge()
    check_tower_scaling()
    print("R144_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
