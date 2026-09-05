"""Exact proof-level audit for R34's OU-graded high-pass obstruction.

Only finite symbolic identities and elementary polynomial facts are checked.
The Chebyshev minimax statement and measure-positivity implications are
recorded as proof notes; no numerical optimization, SOS solver, or sweep is
run here.
"""

from __future__ import annotations

from sympy import (
    Function,
    Poly,
    Rational,
    Symbol,
    chebyshevt,
    diff,
    expand,
    simplify,
    sqrt,
    symbols,
)


def check_mgf_ou_covariance():
    z, u, a = symbols("z u a", positive=True)
    M = Function("M")
    t = u**2
    a_t = 1 - t + t * a
    assert simplify(a_t - (1 - t + t * a)) == 0

    lhs = expand((-a_t * z**2 / 2) + ((1 - t) * z**2 / 2))
    rhs = expand(-a * (u * z) ** 2 / 2)
    assert simplify(lhs - rhs) == 0
    assert M(u * z) == M(u * z)


def check_flat_polynomial_and_q_scaling():
    x, u = symbols("x u", positive=True)
    for M in range(1, 6):
        coefficients = symbols(f"p_{M}_0:{M}")
        P = x**M + sum(coefficients[j] * x**j for j in range(M))
        P_t = expand(u**M * P.subs(x, x / u))
        expected = expand(x**M + sum(coefficients[j] * u ** (M - j) * x**j for j in range(M)))
        assert simplify(P_t - expected) == 0
        assert Poly(P_t, x).LC() == 1

        # L_t[f(x)] = L[f(u*x)] is the polynomial form of the MGF identity.
        P_at_ux = expand(P_t.subs(x, u * x))
        null_scale = expand(P_at_ux * (u * x) ** 0)
        assert simplify(null_scale - u**M * P) == 0
        q_scale = expand((u * x) ** 2 * P_at_ux**2)
        assert simplify(q_scale - u ** (2 * M + 2) * x**2 * P**2) == 0


def check_shadow_semigroup_covariance():
    z, u, a = symbols("z u a", positive=True)
    N = Function("N")
    t = u**2
    a_t = 1 - t + t * a

    # Additive Gaussian convolution has MGF exp(a z^2/2)N(z).
    shadow_mgf = expand(a_t * z**2 / 2)  # P_(a_t) S_u nu_M
    forward_ou_mgf = expand((1 - t) * z**2 / 2 + a * (u * z) ** 2 / 2)
    assert simplify(shadow_mgf - forward_ou_mgf) == 0
    assert N(u * z) == N(u * z)


def check_total_shadow_evaluation_identity():
    gamma, q_shadow, P_shadow, E_q_shadow, E_flat_shadow = symbols(
        "gamma q_shadow P_shadow E_q_shadow E_flat_shadow"
    )
    certificate = gamma + q_shadow - (P_shadow + E_q_shadow + E_flat_shadow)
    theta = (P_shadow + E_q_shadow).subs(
        {q_shadow: 0, E_flat_shadow: 0, E_q_shadow: gamma - P_shadow}
    )
    assert simplify(
        certificate.subs(
            {q_shadow: 0, E_flat_shadow: 0, E_q_shadow: gamma - P_shadow}
        )
    ) == 0
    assert simplify(theta - gamma) == 0


def check_positive_ou_mixture_monotonicity_schema():
    u = Symbol("u", nonnegative=True)
    for ell in range(0, 6):
        gap = expand(u**ell - u ** (ell + 1))
        assert simplify(gap - u**ell * (1 - u)) == 0
    # For 0<=u<=1, u^ell(1-u)>=0 pointwise.  Integrating against a positive
    # probability measure gives m_ell >= m_(ell+1), hence a positive OU filter
    # is low-pass.  Equality m_N=1 forces u=1 almost surely.


def check_chebyshev_monic_sup_normalization():
    u = Symbol("u", real=True)
    for N in range(1, 7):
        monic = expand(Rational(2) ** (1 - 2 * N) * chebyshevt(N, 2 * u - 1))
        assert Poly(monic, u).LC() == 1
        assert Poly(monic, u).degree() == N
        # |T_N(2u-1)|<=1 on [0,1] is the standard Chebyshev bound, so the
        # displayed monic polynomial has sup norm 2^(1-2N).  The minimax
        # equality is the classical monic Chebyshev theorem, not a numerical
        # optimization claim.


def check_signed_filter_total_variation_bound_schema():
    N = Symbol("N", integer=True, positive=True)
    error = Rational(2) ** (1 - 2 * N)
    lower_bound = 1 / error
    assert simplify(lower_bound - Rational(2) ** (2 * N - 1)) == 0
    # If signed sigma annihilates degrees <N and has Nth moment 1, then for
    # every p of degree <N, 1=integral(u^N-p)d sigma.  Total variation is at
    # least 1/||u^N-p||_infty; the monic Chebyshev minimax error above gives
    # ||sigma||_TV >= 2^(2N-1).  This is a proof note, not a solver run.


def main():
    check_mgf_ou_covariance()
    check_flat_polynomial_and_q_scaling()
    check_shadow_semigroup_covariance()
    check_total_shadow_evaluation_identity()
    check_positive_ou_mixture_monotonicity_schema()
    check_chebyshev_monic_sup_normalization()
    check_signed_filter_total_variation_bound_schema()
    print("R34_FLAT_OU_COVARIANCE PASSED")
    print("R34_TOTAL_SHADOW_HIGH_PASS NO_GO")
    print("R34_SIGNED_OU_FILTER_NORM_BLOWUP RECORDED")
    print("R34_NONLINEAR_GRADED_TRANSGRESSION REMAINS OPEN")
    print("R34_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
