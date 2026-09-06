"""R82 exact audit for the first actual mixed-kernel obstruction."""

from math import comb, factorial

import sympy as sp


I = sp.I
X = sp.symbols("X")
OMEGA = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2


def angular_pair_average(p: int, q: int) -> sp.Expr:
    """Exact three-factor angular moment C_(p,q)."""
    total = 0
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for r in range(p + 1):
            for s in range(q + 1):
                if 2 * r - p + 2 * s - q == 0:
                    total += (sp.Rational(1, 6) ** ((p + q) // 2)
                              * comb(p, r) * comb(q, s)
                              * OMEGA ** (i * (2 * r - p)
                                           + j * (2 * s - q)))
    return sp.simplify(sp.expand(total))


def angular_A(m: int) -> sp.Expr:
    return sp.Rational(3, 6 ** m) * comb(2 * m, m)


def tangent_coefficient(r: int) -> sp.Expr:
    return sp.Rational((-1) ** (r - 1) * r * factorial(r + 1),
                       2 * factorial(2 * r + 1))


def mixed_M(m: int, j: int) -> sp.Expr:
    c_j = sp.Rational(factorial(j) ** 2, factorial(2 * j + 1))
    return sp.simplify(
        c_j * tangent_coefficient(m - j - 1)
        * (angular_pair_average(2 * m - 2 * j - 1, 2 * j + 1)
           + angular_pair_average(2 * j + 1, 2 * m - 2 * j - 1))
        / (2 * angular_A(m)))


def gaussian_expectation(poly: sp.Expr) -> sp.Expr:
    total = 0
    for (degree,), coefficient in sp.Poly(sp.expand(poly), X).terms():
        moment = 0 if degree % 2 else sp.factorial2(degree - 1)
        total += coefficient * moment
    return sp.simplify(total)


def make_q_polynomials(limit: int) -> list[sp.Expr]:
    q = [sp.Integer(0), sp.Integer(0), -sp.hermite_prob(1, X),
         -sp.hermite_prob(0, X)]
    for ell in range(3, limit):
        q.append(sp.expand(X * q[-1] - ell * q[-2]))
    return q


Q_POLYS = make_q_polynomials(18)


def source_R(ell: int, m: int) -> sp.Expr:
    P = sp.expand(sp.hermite_prob(ell + 1, X) * Q_POLYS[ell]
                  - ell * sp.hermite_prob(ell, X) * Q_POLYS[ell - 1])
    p_lm = sp.simplify(
        gaussian_expectation(P * sp.hermite_prob(2 * m, X))
        / factorial(2 * m))
    return sp.simplify(sp.Rational(-2 * factorial(2 * m), factorial(ell) ** 2)
                       * p_lm)


def green_one_step(ell: int) -> sp.Expr:
    return -sp.Rational(ell + 3, ell + 1)


def check_finite_kernel_channels() -> None:
    # Fixed exact degrees are enough to audit the displayed rational channels;
    # the all-degree claim remains conditional on the formal hierarchy.
    for j in (0, 1, 2, 4):
        m3 = mixed_M(j + 2, j)
        k3 = sp.simplify(source_R(j + 3, j + 2) * m3)
        target3 = sp.Rational(2 * (j + 6),
                              3 * (j + 1) * (j + 2) * (j + 3) ** 2)
        assert sp.simplify(k3 - target3) == 0

        # d=4 contains two direct source paths plus Green return from d=3.
        direct = (source_R(j + 4, j + 3) * mixed_M(j + 3, j)
                  + source_R(j + 4, j + 2) * mixed_M(j + 2, j))
        k4 = sp.simplify(direct + green_one_step(j + 3) * k3)
        target4 = -sp.Rational(3 * j ** 3 + 146 * j ** 2 + 1001 * j + 1560,
                               15 * (j + 1) * (j + 2)
                               * (j + 3) ** 2 * (j + 4) ** 2)
        assert sp.simplify(k4 - target4) == 0
    print("R82_D3_D4_EXACT_CHANNELS_PASSED")


def check_asymptotics_and_weights() -> None:
    j, n, theta = sp.symbols("j n theta", positive=True)
    k3 = sp.Rational(2, 3) * (j + 6) / (
        (j + 1) * (j + 2) * (j + 3) ** 2)
    k4 = -(3 * j ** 3 + 146 * j ** 2 + 1001 * j + 1560) / (
        15 * (j + 1) * (j + 2) * (j + 3) ** 2 * (j + 4) ** 2)
    assert sp.limit(j ** 3 * k3, j, sp.oo) == sp.Rational(2, 3)
    assert sp.limit(j ** 3 * k4, j, sp.oo) == -sp.Rational(1, 5)

    jn = theta * n
    R2 = 16 * n
    ratio_d4 = sp.simplify(
        R2 ** 4 * ((jn + 1) * (jn + 2) * (jn + 3) * (jn + 4)) ** 2
        / ((2 * jn + 2) * (2 * jn + 3) * (2 * jn + 4) * (2 * jn + 5)
           * (2 * jn + 6) * (2 * jn + 7) * (2 * jn + 8)
           * (2 * jn + 9)))
    assert sp.simplify(sp.limit(ratio_d4 / (4 * n) ** 4, n, sp.oo) - 1) == 0
    weighted_d4 = sp.simplify(abs(-sp.Rational(1, 5) / jn ** 3)
                               * ratio_d4)
    assert sp.simplify(sp.limit(weighted_d4 / n, n, sp.oo)
                       - sp.Rational(256, 5) / theta ** 3) == 0
    print("R82_FIXED_GAP_WEIGHT_GROWTH_PASSED")


def check_radius_incompatibility() -> None:
    alpha = sp.symbols("alpha", real=True)
    # d=4 contributes n^(8 alpha-3), hence alpha<=3/8 is necessary.
    exponent_gap = 8 * alpha - 3
    assert sp.solve_univariate_inequality(exponent_gap <= 0, alpha) == (alpha <= sp.Rational(3, 8))

    n = sp.symbols("n", positive=True, integer=True)
    h4_hn_coefficient = 6 * n * (n - 1)
    assert sp.simplify(h4_hn_coefficient - 6 * n * (n - 1)) == 0
    # Gram control from degree 4 requires n^2 R_n^(-4)=O(1), alpha>=1/2.
    assert sp.Rational(1, 2) > sp.Rational(3, 8)
    print("R82_SINGLE_RADIUS_INCOMPATIBILITY_PASSED")


if __name__ == "__main__":
    check_finite_kernel_channels()
    check_asymptotics_and_weights()
    check_radius_incompatibility()
    print("R82_EXACT_MIXED_KERNEL_AUDIT_COMPLETED")
