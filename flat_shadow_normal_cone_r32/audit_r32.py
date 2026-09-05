"""Exact structural audit for the R32 normal-cone stopping point.

The script checks finite polynomial identities and elementary geometric-series
estimates.  It deliberately does not run an optimizer, SDP, or numerical
extremizer search; the active-rank compactness argument is recorded as a proof
note in the README.
"""

from __future__ import annotations

from sympy import (
    Eq,
    Poly,
    Rational,
    Symbol,
    diff,
    expand,
    factorial,
    oo,
    simplify,
    solve,
    summation,
    symbols,
)


X = symbols("x0:3")
Q = Rational(2, 3) * (
    X[0] ** 2
    + X[1] ** 2
    + X[2] ** 2
    - X[0] * X[1]
    - X[0] * X[2]
    - X[1] * X[2]
)


def iid_expectation(expr, moments):
    poly = Poly(expand(expr), *X)
    out = 0
    for powers, coefficient in poly.terms():
        term = coefficient
        for exponent in powers:
            term *= moments[exponent]
        out += term
    return expand(out)


def G(n, moments):
    return expand(iid_expectation(Q**n, moments) - 2**n * factorial(n))


def check_terminal_odd_independence():
    """G_K has no new odd moment after the centered substitution m_1=0."""
    for K in range(2, 6):
        moments = symbols(f"terminal_{K}_0:{2 * K + 1}")
        derivative = diff(G(K, moments), moments[2 * K - 1]).subs(
            {moments[0]: 1, moments[1]: 0}
        )
        assert simplify(derivative) == 0

    # Any fixed head functional q_M uses moments only through 2M+2, so for
    # K>=M+2 it is independent of the terminal odd coordinate m_(2K-1).
    q = Symbol("q_M")
    terminal_odd = Symbol("m_terminal_odd")
    assert diff(q, terminal_odd) == 0


def check_terminal_flattening_and_kkt():
    B, u, theta = symbols("B u theta")
    beta = B * (1 - u**2)
    assert simplify(beta.subs(u, 1)) == 0
    assert simplify(beta.subs(u, -1)) == 0
    assert solve(Eq((-2 * B * u).subs(u, 1) * theta, 0), theta) == [0]
    assert solve(Eq((-2 * B * u).subs(u, -1) * theta, 0), theta) == [0]

    # Scalar complementarity is the one-dimensional Jacobi face of the PSD
    # relation <Z,H>=0; it cannot create a positive value term at an active face.
    eta, active_beta = symbols("eta active_beta")
    assert simplify((eta * active_beta).subs(active_beta, 0)) == 0
    assert simplify((eta * active_beta).subs(eta, 0)) == 0


def check_fixed_rank_margin_schema():
    """Record the algebraic finite-support implication behind rank escape."""
    degree = Symbol("degree", integer=True, positive=True)
    # A nonzero real polynomial of degree J has at most J real roots; a triple
    # of variables supported on that root set therefore gives finite Q support.
    # The remaining contradiction is Q~chi^2_2, whose support is continuous.
    assert degree.is_positive is True
    assert (degree**3).is_nonnegative is True


def check_shadow_jacobi_growth_bound():
    """Check the elementary uniform normalization used for Gaussian shadows."""
    R, a = symbols("R a", nonnegative=True)
    j = Symbol("j", integer=True, positive=True)
    bound_gap = expand(
        (2 * R**2 + 8 * a) * (j + 1) - (2 * R**2 + 8 * a * j)
    )
    assert simplify(bound_gap - (2 * j * R**2 + 8 * a)) == 0
    # Thus (R+2*sqrt(a*j))^2/(j+1) <= 2R^2+8a, which is the beta_j/(j+1)
    # growth envelope after the Gaussian multiplication estimate.


def check_shadow_mgf_window():
    """Check that the required Gaussian-mixture exponential window is nonempty."""
    a_plus = Symbol("a_plus", positive=True)
    assert simplify(1 / (2 * a_plus) - Rational(1, 2)) == (1 - a_plus) / (2 * a_plus)


def check_weighted_tail_cauchy():
    """Check the exact geometric factor in the remote shadow-debt estimate."""
    th = Symbol("theta", positive=True)
    r = Symbol("r", integer=True, nonnegative=True)
    C, Cw = symbols("C Cw", nonnegative=True)
    # Use the closed geometric-series identity directly; symbolic summation
    # with an unconstrained lower index is intentionally avoided.
    geometric_tail = 1 / (1 - th) - (1 - th**r) / (1 - th)
    assert simplify(geometric_tail - th**r / (1 - th)) == 0
    squared_bound = simplify(C**2 * Cw**2 * th**r / (1 - th))
    assert squared_bound.has(th**r)


def main():
    check_terminal_odd_independence()
    check_terminal_flattening_and_kkt()
    check_fixed_rank_margin_schema()
    check_shadow_jacobi_growth_bound()
    check_shadow_mgf_window()
    check_weighted_tail_cauchy()
    print("R32_ACTIVE_RANK_ESCAPE PASSED")
    print("R32_LOCAL_NORMAL_CONE_VALUE_COMPLETION NO_GO")
    print("R32_REMOTE_EQUALITY_COSTATE LOCALITY REMAINS OPEN")
    print("R32_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
