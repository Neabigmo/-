"""Small exact audit for R30's augmented-adjoint obstruction.

This script checks only polynomial identities.  It does not search for
multipliers, solve an SDP, or claim the open sign-compatible certificate.
"""

from __future__ import annotations

from sympy import Poly, Rational, Symbol, diff, expand, factorial, integrate, simplify, symbols


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
    """Evaluate a polynomial under an iid law with formal moments."""
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


def check_path_averaged_identity(n):
    """Check G(m)-G(r)=sum_j int(D_jG(v_s)) ds exactly."""
    width = 2 * n + 1
    m = symbols(f"m{n}_0:{width}")
    r = symbols(f"r{n}_0:{width}")
    v = symbols(f"v{n}_0:{width}")
    s = Symbol(f"s{n}")
    polynomial = G(n, v)
    path = {v[j]: r[j] + s * (m[j] - r[j]) for j in range(width)}
    averaged = 0
    for j in range(width):
        averaged += integrate(diff(polynomial, v[j]).subs(path), (s, 0, 1)) * (
            m[j] - r[j]
        )
    identity = polynomial.xreplace(dict(zip(v, m))) - polynomial.xreplace(dict(zip(v, r)))
    assert simplify(expand(identity - averaged)) == 0


def check_structural_pivots():
    for n in (2, 3):
        moments = symbols(f"p{n}_0:{2 * n + 1}")
        pivot_even = diff(G(n, moments), moments[2 * n]).subs(
            {moments[0]: 1, moments[1]: 0}
        )
        pivot_odd = diff(G(n, moments), moments[2 * n - 1]).subs(
            {moments[0]: 1, moments[1]: 0}
        )
        assert simplify(pivot_even - 3 * Rational(2, 3) ** n) == 0
        assert simplify(pivot_odd) == 0


def check_first_row():
    """For M=1, N=4, the n=2 row isolates d_4 once d_0..d_3=0."""
    m = symbols("first_m0:5")
    r = symbols("first_r0:5")
    difference = G(2, m) - G(2, r)
    lower_equal = {m[j]: r[j] for j in range(4)}
    reduced = difference.subs(lower_equal).subs({r[0]: 1, r[1]: 0})
    assert simplify(reduced - Rational(4, 3) * (m[4] - r[4])) == 0
    assert simplify(diff(G(2, m), m[4]).subs({m[0]: 1, m[1]: 0}) - Rational(4, 3)) == 0


def check_finite_adjoint_skeleton():
    """Check the exact finite multiplier identity for M=1, K=3."""
    width = 7
    m = symbols(f"adj_m0:{width}")
    r = symbols(f"adj_r0:{width}")
    v = symbols(f"adj_v0:{width}")
    s = Symbol("adj_s")
    lambdas = {2: Symbol("lambda_2"), 3: Symbol("lambda_3")}
    bar = {}
    for n in (2, 3):
        polynomial = G(n, v)
        path = {v[j]: r[j] + s * (m[j] - r[j]) for j in range(width)}
        bar[n] = {
            j: integrate(diff(polynomial, v[j]).subs(path), (s, 0, 1))
            for j in range(4, 2 * n + 1)
        }

    coefficients = {
        j: sum(lambdas[n] * bar[n].get(j, 0) for n in (2, 3))
        for j in range(4, 7)
    }
    delta_identity = sum(lambdas[n] * (G(n, m) - G(n, r)) for n in (2, 3))
    # R30 starts after the matched prefix d_0=...=d_3=0 for M=1.
    delta_identity = delta_identity.subs({m[j]: r[j] for j in range(4)})
    coefficient_identity = sum(
        coefficients[j] * (m[j] - r[j]) for j in range(4, 7)
    )
    coefficient_identity = coefficient_identity.subs({m[j]: r[j] for j in range(4)})
    assert simplify(expand(delta_identity - coefficient_identity)) == 0

    # Normalize c_4=1 using the positive first-row pivot; this is a skeleton,
    # not the missing positive-plus-remote-tail certificate.
    normalized = {lambdas[2]: Rational(3, 4), lambdas[3]: 0}
    exact_mass_centering = {m[0]: 1, r[0]: 1, m[1]: 0, r[1]: 0}
    assert simplify(
        coefficients[4].subs(normalized).subs(exact_mass_centering) - 1
    ) == 0


def check_rank_dimension_schema():
    """The equality rows leave odd-control directions after the prefix."""
    for M, K in ((1, 3), (2, 5), (3, 6)):
        row_count = K - M
        N = 2 * M + 2
        post_prefix_columns = list(range(N, 2 * K + 1))
        assert len(post_prefix_columns) == 2 * row_count - 1
        assert row_count < len(post_prefix_columns)
        even_pivots = [2 * n for n in range(M + 1, K + 1)]
        odd_slots = [2 * n - 1 for n in range(M + 2, K + 1)]
        assert all(j in post_prefix_columns for j in even_pivots)
        assert all(j in post_prefix_columns for j in odd_slots)
        assert len(odd_slots) == row_count - 1


def main():
    check_path_averaged_identity(2)
    check_path_averaged_identity(3)
    check_structural_pivots()
    check_first_row()
    check_finite_adjoint_skeleton()
    check_rank_dimension_schema()
    print("R30_AUGMENTED_ADJOINT_IDENTITY PASSED")
    print("R30_SIGN_COMPATIBLE_LOCALITY REMAINS OPEN")
    print("R30_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
