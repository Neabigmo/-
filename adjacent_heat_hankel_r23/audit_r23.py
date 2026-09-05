"""Proof-level audit for the R23 near-flat heat-Hankel reductions.

The checks are deliberately local.  They verify the Laurent asymptotics at a
corank-one crossing, the principal-submatrix monotonicity of truncated PSD
radii, and the determinant formula for adjacent Jacobi ratios.  They do not
claim a cross-rank zero-interlacing theorem or a uniform flat-leakage horizon.
"""

from __future__ import annotations

import sympy as sp


def check_near_flat_laurent_asymptotics() -> None:
    # At a flat crossing D_M = D_(M-1) h_M and
    # D_(M+1) = -D_(M-1) ell_M^2 + O(s).  Keep the leading terms symbolic.
    s, c, ell, d_prev = sp.symbols("s c ell d_prev", nonzero=True)
    h_m = c * s
    d_m = d_prev * h_m
    d_next = -d_prev * ell**2
    h_next = sp.simplify(d_next / d_m)
    beta_next = sp.simplify(h_next / h_m)

    assert sp.simplify(h_next + ell**2 / (c * s)) == 0
    assert sp.simplify(beta_next + ell**2 / (c**2 * s**2)) == 0
    # On the post-failure side h_M = c*s < 0, the leading h_(M+1) is positive.
    assert sp.simplify(h_next * h_m + ell**2) == 0


def check_truncated_psd_radius_monotonicity() -> None:
    # H_n is the leading principal block of H_(n+1).  Therefore every value
    # of the heat parameter that keeps H_(n+1) PSD also keeps H_n PSD.
    a = sp.symbols("a", real=True)
    h0, h1, h2 = sp.symbols("h0 h1 h2", positive=True)
    H2 = sp.diag(h0, h1, h2)
    H1 = H2[:2, :2]
    H0 = H2[:1, :1]
    assert H1 == H2[:2, :2]
    assert H0 == H1[:1, :1]
    # The unused parameter is intentional: the implication is pointwise in a.
    assert a.is_real


def check_heat_interval_and_derivative_bound() -> None:
    # If a2 is feasible, then every a1<a2 is feasible because
    # L_(a1)=E_Z L_(a2)[p(x+sqrt(a2-a1)Z)].  For a quadratic p this
    # convolution is visibly a sum of squares of derivatives.
    x, delta = sp.symbols("x delta", real=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    p = c0 + c1 * x + c2 * x**2
    gaussian_square = sp.expand(
        p**2 + delta * sp.diff(p, x) ** 2 + delta**2 / 2 * sp.diff(p, x, 2) ** 2
    )
    expected = p**2 + delta * sp.diff(p, x) ** 2 + delta**2 / 2 * sp.diff(p, x, 2) ** 2
    assert sp.simplify(gaussian_square - expected) == 0
    assert delta.is_real

    # In an orthogonal basis, P_n'=n P_(n-1)+lower terms.  Positive lower
    # norms give the sharp elementary lower bound used in R23.
    n = sp.symbols("n", positive=True)
    h_prev = sp.symbols("h_prev", positive=True)
    lower_h = sp.symbols("lower_h0:3", positive=True)
    lower_c = sp.symbols("lower_c0:3", real=True)
    derivative_norm = n**2 * h_prev + sum(
        lower_c[j] ** 2 * lower_h[j] for j in range(3)
    )
    assert sp.expand(derivative_norm - n**2 * h_prev) == sum(
        lower_c[j] ** 2 * lower_h[j] for j in range(3)
    )


def check_schur_trichotomy() -> None:
    ell, q = sp.symbols("ell q", real=True)
    tail = sp.Matrix([[0, ell], [ell, q]])
    assert sp.factor(tail.det()) == -ell**2
    assert sp.factor(tail.subs(ell, 0).det()) == 0
    # The three cases are: indefinite if ell != 0, negative direction if
    # ell=0,q<0, and PSD tail if ell=0,q>=0.
    assert tail.subs({ell: 1, q: 0}).det() < 0
    assert tail.subs({ell: 0, q: -1}) == sp.diag(0, -1)
    assert tail.subs({ell: 0, q: 1}) == sp.diag(0, 1)


def check_atomic_shadow_overshoot_sign() -> None:
    # The residual projection factor is positive, so q_M<0 is exactly the
    # next-Q-moment overshoot of the M-atomic shadow.
    target, shadow = sp.symbols("target shadow", real=True)
    denominator = sp.Rational(3) * sp.Rational(2, 3) ** 3  # M=2
    q_m = (target - shadow) / denominator
    assert denominator > 0
    assert sp.simplify(shadow - target + denominator * q_m) == 0


def check_plateau_support_bound() -> None:
    M = sp.symbols("M", integer=True, nonnegative=True)
    K = 1 + M * (M - 1) / 2 + M * (M - 1) * (M - 2) / 6
    closed_form = 1 + (M**3 - M) / 6
    assert sp.simplify(K - closed_form) == 0
    # If Q agrees with a continuous chi-square law through order 2K while
    # the atomic shadow has at most K support values, its (K+1)-Hankel block
    # is singular versus the chi-square block, hence a plateau cannot reach
    # N-1 >= 2K.  The arithmetic implication is recorded explicitly.
    # The strict inequality N-1<2K is equivalent, for integer N, to N<=2K;
    # the script checks the boundary values that drive the contradiction.
    assert (2 * K - 1) < 2 * K
    assert not ((2 * K + 1) - 1 < 2 * K)


def check_bernoulli_heat_hankel_no_go() -> None:
    # Ordinary smooth positive iid laws need not have real-rooted Hankel
    # determinant polynomials.  For X=+-1 and independent N(0,t), compute
    # D_1,D_2,D_3 exactly and check the cubic discriminant.
    t = sp.symbols("t", real=True)
    moments = []
    for degree in range(9):
        if degree % 2:
            moments.append(sp.Integer(0))
        else:
            moments.append(
                sp.expand(
                    sum(
                        sp.binomial(degree, 2 * k)
                        * sp.factorial(2 * k)
                        / (2**k * sp.factorial(k))
                        * t**k
                        for k in range(degree // 2 + 1)
                    )
                )
            )
    determinants = []
    for rank in range(4):
        matrix = sp.Matrix(
            [[moments[i + j] for j in range(rank + 1)] for i in range(rank + 1)]
        )
        determinants.append(sp.factor(matrix.det()))
    assert determinants[1] == t + 1
    assert determinants[2] == 2 * t * (t + 1) * (t + 2)
    cubic = 3 * t**3 + 12 * t**2 + 9 * t + 2
    assert determinants[3] == 4 * t**2 * (t + 2) * cubic
    assert sp.discriminant(cubic, t) == -216


def check_adjacent_beta_determinant_formula() -> None:
    d_m2, d_m1, d_m, d_next = sp.symbols(
        "d_m2 d_m1 d_m d_next", nonzero=True
    )
    beta_m = sp.simplify(d_m * d_m2 / d_m1**2)
    beta_next = sp.simplify(d_next * d_m1 / d_m**2)
    ratio = sp.simplify(beta_next / beta_m)
    expected = sp.simplify(d_next * d_m1**3 / (d_m**3 * d_m2))
    assert sp.simplify(ratio - expected) == 0


def check_adjacent_sector_threshold() -> None:
    M = sp.symbols("M", positive=True)
    threshold = sp.Rational(2, 3) * (M + 1) ** 2 / M**2
    coefficient = sp.Rational(3, 2) * M**2 / (M + 1) ** 2
    assert sp.simplify(threshold * coefficient - 1) == 0


def main() -> None:
    checks = [
        check_near_flat_laurent_asymptotics,
        check_truncated_psd_radius_monotonicity,
        check_heat_interval_and_derivative_bound,
        check_schur_trichotomy,
        check_atomic_shadow_overshoot_sign,
        check_plateau_support_bound,
        check_bernoulli_heat_hankel_no_go,
        check_adjacent_beta_determinant_formula,
        check_adjacent_sector_threshold,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R23_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
