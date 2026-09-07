"""Finite exact audit for R108.

The audit verifies the four-point Gram algebra, the bispectrum coordinates,
the angular coefficient moments, the homometric y^6 separations, and the
full-exact companion expansion.  It deliberately does not claim that the
conditional shear-alignment lemma is solved.
"""

from __future__ import annotations

import sympy as sp


def angular_average(expr: sp.Expr, theta: sp.Symbol) -> sp.Expr:
    return sp.simplify(
        sp.integrate(sp.expand_trig(expr), (theta, 0, 2 * sp.pi))
        / (2 * sp.pi)
    )


def moment_expectation(poly: sp.Expr, variables: tuple[sp.Symbol, ...], m3: sp.Expr,
                       m6: sp.Expr) -> sp.Expr:
    """Independent centered moments through degree six."""
    moments = {0: sp.Integer(1), 1: sp.Integer(0), 2: sp.Integer(1),
               3: m3, 4: sp.Integer(3), 5: sp.Integer(0), 6: m6}
    expanded = sp.Poly(sp.expand(poly), *variables)
    result = 0
    for powers, coefficient in expanded.terms():
        value = coefficient
        for power in powers:
            if power not in moments:
                raise AssertionError(f"unexpected moment degree {power}")
            value *= moments[power]
        result += value
    return sp.simplify(result)


def check_angular_geometry() -> None:
    theta, y = sp.symbols("theta y", real=True)
    a1 = sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta)
    a2 = sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta + 2 * sp.pi / 3)
    a3 = sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta - 2 * sp.pi / 3)
    assert sp.trigsimp(a1 + a2 + a3) == 0
    assert sp.trigsimp(a1**2 + a2**2 + a3**2) == 1
    s, t = a2 * y, (a1 - a2) * y
    assert sp.trigsimp(6 * (s / y)**2 + 6 * (s / y) * (t / y)
                       + 2 * (t / y)**2) == 1
    assert sp.trigsimp(a1 - a2 - sp.sqrt(2) * sp.sin(theta + sp.pi / 3)) == 0
    print("R108_ELLIPSE_BISPECTRUM_COORDINATES_PASSED")


def check_gram_and_schur_algebra() -> None:
    u, v, w, c = sp.symbols("u v w c")
    ub, vb, wb, cb = sp.symbols("ub vb wb cb")
    gamma = sp.Matrix([
        [1 - u * ub, c - u * vb, vb - u * wb],
        [cb - ub * v, 1 - v * vb, ub - v * wb],
        [v - ub * w, u - vb * w, 1 - w * wb],
    ])
    expected_det = (
        1 - c * cb - w * wb - 2 * u * ub - 2 * v * vb
        + u**2 * ub**2 + v**2 * vb**2 - 2 * u * ub * v * vb
        + c * cb * w * wb
        + 2 * c * ub * v + 2 * cb * u * vb
        + 2 * u * v * wb + 2 * ub * vb * w
        - c * ub**2 * w - cb * u**2 * wb
        - c * v**2 * wb - cb * vb**2 * w
    )
    assert sp.simplify(sp.expand(gamma.det()) - expected_det) == 0

    C = gamma[:2, :2]
    q = sp.Matrix([vb - u * wb, ub - v * wb])
    qbar = sp.Matrix([v - ub * w, u - vb * w])
    d = 1 - w * wb
    schur = sp.det(C) * (d - (qbar.T * C.inv() * q)[0])
    assert sp.simplify(sp.together(schur - gamma.det())) == 0
    print("R108_FOUR_POINT_GRAM_AND_SCHUR_PASSED")


def check_bispectrum_phase_rewrite() -> None:
    f1, f2, f3, h = sp.symbols("f1 f2 f3 h")
    f1b, f2b, f3b, hb = sp.symbols("f1b f2b f3b hb")
    # In the (s,t) coordinates: u=f1, v=conj(f2), w=h, c=conj(f3).
    u, v, w, c = f1, f2b, h, f3b
    b_exact = f1 * f2 * f3
    b_exact_bar = f1b * f2b * f3b
    b_companion = f2 * h * f1b
    psi_s = f2 * f2b
    t_integrand = c * h * f1b**2
    assert sp.simplify(c * f1b * v - b_exact_bar) == 0
    # Replace conjugation explicitly; this is the identity used at zeros-free s.
    assert sp.simplify(b_exact_bar * b_companion / psi_s
                       - t_integrand) == 0
    print("R108_BISPECTRUM_CYCLE_REWRITE_PASSED")


def check_angular_coefficient_moments() -> None:
    theta = sp.symbols("theta", real=True)
    a1 = sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta)
    a2 = sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta + 2 * sp.pi / 3)
    a3 = sp.sqrt(sp.Rational(2, 3)) * sp.cos(theta - 2 * sp.pi / 3)
    bq = (-a1, a2, a1 - a2)
    bt = (-a3, -a1, -a1, a1 - a2)
    for coefficients in (bq, bt):
        assert sp.trigsimp(sum(coefficients)) == 0

    sq2 = sum(b**2 for b in bq)
    sq3 = sum(b**3 for b in bq)
    assert angular_average(sq2, theta) == sp.Rational(5, 3)
    assert angular_average(sq2**2, theta) == sp.Rational(11, 3)
    assert angular_average(sq2**3, theta) == sp.Rational(245, 27)
    assert angular_average(sum(b**6 for b in bq), theta) == sp.Rational(145, 54)
    assert angular_average(sq3**2, theta) == sp.Rational(5, 4)

    st3 = sum(b**3 for b in bt)
    assert angular_average(st3**2, theta) == sp.Rational(4, 3)
    print("R108_ANGULAR_COEFFICIENT_MOMENTS_PASSED")


def check_q4_and_companion_series() -> None:
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    y, m3 = sp.symbols("y m3", real=True)
    m6 = 15 + 7 * m3**2  # m4=3 and kappa6=-3*m3^2.
    ecal = sp.Rational(2, 3) * (
        x1**2 + x1 * x2 - 3 * x1 * x3 + x2**2 - 3 * x2 * x3 + 3 * x3**2
    )
    e1 = moment_expectation(ecal, (x1, x2, x3), m3, m6)
    e2 = moment_expectation(ecal**2, (x1, x2, x3), m3, m6)
    e3 = moment_expectation(ecal**3, (x1, x2, x3), m3, m6)
    assert e1 == sp.Rational(10, 3)
    assert e2 == sp.Rational(88, 3)
    assert e3 == sp.Rational(3920, 9) + sp.Rational(128, 9) * m3**2
    q6 = sp.simplify(-e3 / 2304)
    assert q6 == -(245 + 8 * m3**2) / 1296

    q_gaussian = sp.exp(-sp.Rational(5, 6) * y**2) * sp.besseli(0, sp.Rational(2, 3) * y**2)
    q_gaussian_series = sp.series(q_gaussian, y, 0, 8).removeO()
    q_series = (1 - sp.Rational(5, 6) * y**2 + sp.Rational(11, 24) * y**4
                - (245 + 8 * m3**2) * y**6 / 1296)
    assert sp.expand(q_series.subs(m3, 0) - q_gaussian_series) == 0

    d2, d4, d6 = 2, 12, 120 - 6 * m3**2
    rho = sp.sqrt(sp.Rational(2, 3))
    def h_series(scale: sp.Expr) -> sp.Expr:
        return sp.expand(1 - scale**2 * d2 * y**2 / 4
                         + scale**4 * d4 * y**4 / 64
                         - scale**6 * d6 * y**6 / 2304)
    h_rho = h_series(rho)
    h_sqrt2 = h_series(sp.sqrt(2))
    companion = sp.expand(1 + 2 * q_series - 2 * h_rho - h_sqrt2)
    assert sp.expand(companion - sp.Rational(5, 144) * (2 - m3**2) * y**6) == 0
    print("R108_FULL_EXACT_SERIES_AND_COMPANION_BOUND_PASSED")


def check_homometric_y6_separation() -> None:
    lam = sp.symbols("lambda", positive=True)
    dq = -sp.Rational(5, 288) * lam**3
    dt = -sp.Rational(1, 54) * lam**3
    assert sp.simplify(dq - dt - lam**3 / 864) == 0
    # The pair has equal kappa_6, so only the kappa_3^2 term separates them.
    assert sp.simplify(sp.Rational(5, 4) / 72 - sp.Rational(5, 288)) == 0
    assert sp.simplify(sp.Rational(4, 3) / 72 - sp.Rational(1, 54)) == 0
    print("R108_HOMOMETRIC_Q4_T4_SEPARATION_PASSED")


def main() -> None:
    check_angular_geometry()
    check_gram_and_schur_algebra()
    check_bispectrum_phase_rewrite()
    check_angular_coefficient_moments()
    check_q4_and_companion_series()
    check_homometric_y6_separation()
    print("R108_FOUR_POINT_BISPECTRUM_SHEAR_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
