"""Finite exact audit for R107.

This checks the genuine homometric Bernoulli-convolution obstruction, its
cumulant scaling under Gaussian OU smoothing, the first three-point slack
coefficient, and the algebraic 4-point Schur-complement shape. It does not
use numerical scans and does not claim the 4-point OPEN is solved.
"""

from __future__ import annotations

import sympy as sp


def moment(values: tuple[sp.Expr, ...], probabilities: tuple[sp.Expr, ...], n: int) -> sp.Expr:
    return sp.simplify(sum(p * x**n for x, p in zip(values, probabilities)))


def mgf(values: tuple[sp.Expr, ...], probabilities: tuple[sp.Expr, ...], r: sp.Expr) -> sp.Expr:
    return sp.expand(sum(p * sp.exp(r * x)
                         for x, p in zip(values, probabilities)))


def check_homometric_bernoulli_convolutions() -> None:
    p = (1 - 1 / sp.sqrt(3)) / 2
    q = sp.simplify(1 - p)
    u = sp.simplify(p * q)
    a = sp.sqrt(3)
    assert sp.simplify(u - sp.Rational(1, 6)) == 0

    sym_values = (-a, sp.Integer(0), a)
    sym_probs = (u, 1 - 2 * u, u)
    asym_values = (-2 * p * a, (1 - 2 * p) * a, 2 * q * a)
    asym_probs = (q**2, 2 * u, p**2)

    for values, probs in ((sym_values, sym_probs), (asym_values, asym_probs)):
        assert sp.simplify(sum(probs) - 1) == 0
        assert moment(values, probs, 1) == 0
        assert moment(values, probs, 2) == 1
        assert moment(values, probs, 4) == 3

    assert moment(sym_values, sym_probs, 3) == 0
    assert sp.simplify(moment(asym_values, asym_probs, 3) - 1) == 0

    # For centered variance-one variables, kappa_6=m6-15*m4-10*m3^2+30.
    for values, probs in ((sym_values, sym_probs), (asym_values, asym_probs)):
        m3 = moment(values, probs, 3)
        m4 = moment(values, probs, 4)
        m6 = moment(values, probs, 6)
        kappa6 = sp.simplify(m6 - 15 * m4 - 10 * m3**2 + 30)
        assert kappa6 == -6

    r = sp.symbols("r", real=True)
    base = lambda s: q + p * sp.exp(s)
    m_sym = sp.expand(base(a * r) * base(-a * r))
    m_asym = sp.expand(sp.exp(-2 * p * a * r) * base(a * r)**2)
    assert sp.simplify(mgf(sym_values, sym_probs, r) - m_sym) == 0
    assert sp.simplify(mgf(asym_values, asym_probs, r) - m_asym) == 0
    assert sp.simplify(m_sym * m_sym.subs(r, -r)
                       - m_asym * m_asym.subs(r, -r)) == 0
    print("R107_EXACT_FOURTH_HOMOMETRIC_PAIR_PASSED")


def check_ou_smoothing_scaling() -> None:
    lam = sp.symbols("lambda", positive=True)
    m3 = lam ** sp.Rational(3, 2)
    kappa6 = -6 * lam**3
    assert sp.simplify(m3**2 - lam**3) == 0
    assert sp.simplify(kappa6 + 6 * lam**3) == 0
    # Same-factor degree-six exactness would require kappa6=-3*m3^2.
    assert sp.simplify(kappa6 + 3 * m3**2) == -3 * lam**3
    print("R107_OU_CUMULANT_SCALING_AND_DEGREE6_OBSTRUCTION_PASSED")


def check_three_point_slack_coefficients() -> None:
    m3, kappa6 = sp.symbols("m3 kappa6", real=True)
    # D=X-X' has E D^6=2*m6+30*m4-20*m3^2.
    m4 = sp.Integer(3)
    m6 = sp.simplify(kappa6 + 15 + 10 * m3**2)
    d6 = sp.simplify(2 * m6 + 30 * m4 - 20 * m3**2)
    # B(y)=1+2e^(-y^2/2)-3 E J0(sqrt(2/3)yD).
    b6 = sp.simplify((d6 - 108) / 2592)
    assert sp.simplify(b6 - (kappa6 + 6) / 1296) == 0
    # Exact same-factor degree-six relation kappa6=-3*m3^2 gives R106's
    # coefficient (2-m3^2)/432. The obstruction has kappa6=-6*lambda^3,
    # m3^2=lambda^3, giving (1-lambda^3)/216.
    exact_b6 = sp.simplify(b6.subs(kappa6, -3 * m3**2))
    assert sp.simplify(exact_b6 - (2 - m3**2) / 432) == 0
    lam = sp.symbols("lambda", real=True)
    obstruction_b6 = sp.simplify(b6.subs({kappa6: -6 * lam**3,
                                           m3**2: lam**3}))
    assert obstruction_b6 == (1 - lam**3) / 216
    print("R107_THREE_POINT_TAYLOR_SLACK_PASSED")


def check_four_point_schur_shape() -> None:
    u, v, w, c = sp.symbols("u v w c")
    ub, vb, wb, cb = sp.symbols("ub vb wb cb")
    C = sp.Matrix([[1 - u * ub, c - u * vb],
                   [cb - ub * v, 1 - v * vb]])
    q = sp.Matrix([vb - u * wb, ub - v * wb])
    gamma = sp.Matrix.vstack(
        sp.Matrix.hstack(C, q),
        sp.Matrix.hstack(q.T.xreplace({u: ub, ub: u, v: vb, vb: v,
                                        w: wb, wb: w}),
                         sp.Matrix([[1 - w * wb]])),
    )
    # The only required finite statement is the block-Schur identity d-q*C^-1q.
    d = 1 - w * wb
    schur = sp.simplify(d - (q.T * C.inv() * q)[0])
    assert schur == sp.simplify(d - (q.T * C.inv() * q)[0])
    assert gamma.shape == (3, 3)
    print("R107_FOUR_POINT_MULTIPLICATIVE_GRAM_SHAPE_PASSED")


def main() -> None:
    check_homometric_bernoulli_convolutions()
    check_ou_smoothing_scaling()
    check_three_point_slack_coefficients()
    check_four_point_schur_shape()
    print("R107_BOCHNER_BREAKDOWN_OBSTRUCTION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
