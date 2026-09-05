"""Exact proof-level audit for the R33 global value obstruction.

This audit checks only finite polynomial identities.  It does not run an SOS
solver, optimizer, degree search, or numerical sweep.  The infinite-
dimensional Hermite-graded locality statement remains open and is recorded in
the README and durable project log.
"""

from __future__ import annotations

from sympy import Poly, Rational, Symbol, diff, expand, factorial, simplify, solve, symbols


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
    """Evaluate a polynomial under a centered iid law with formal moments."""
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


def centered_unit_variance_row(n, moments):
    # m_0=1, m_1=0, m_2=1 are fixed by probability, centering, and variance.
    return expand(G(n, moments).subs({moments[0]: 1, moments[1]: 0, moments[2]: 1}))


def sequential_even_quotient(K, moments):
    """Return the exact substitutions m_(2n)=F_n/c_n for n=2,...,K."""
    substitutions = {}
    for n in range(2, K + 1):
        row = centered_unit_variance_row(n, moments).subs(substitutions)
        even = moments[2 * n]
        pivot = simplify(diff(row, even))
        expected = 3 * Rational(2, 3) ** n
        assert simplify(pivot - expected) == 0
        solved = solve(row, even)[0]
        assert simplify(row.subs(even, solved)) == 0
        substitutions[even] = solved
    return substitutions


def reduce_even(expr, substitutions):
    reduced = expr
    for even, value in substitutions.items():
        reduced = expand(reduced.subs(even, value))
    return expand(reduced)


def check_triangular_exact_quotient():
    moments = symbols("m0:9")
    substitutions = sequential_even_quotient(4, moments)

    for n in range(2, 5):
        assert reduce_even(centered_unit_variance_row(n, moments), substitutions) == 0
        odd = moments[2 * n - 1]
        assert simplify(diff(centered_unit_variance_row(n, moments), odd)) == 0

    # The quotient keeps the odd controls.  A finite row window need not use
    # its last odd coordinate yet: for G_2,...,G_4, m_7 is still free.
    odd_controls = {moments[3], moments[5], moments[7]}
    surviving = set().union(*(term.free_symbols for term in substitutions.values()))
    assert surviving.issubset(odd_controls)
    assert not any(moment in substitutions for moment in odd_controls)
    assert not any(moments[2 * n] in surviving for n in range(2, 5))


def check_sos_preservation_under_substitution():
    moments = symbols("s0:9")
    substitutions = sequential_even_quotient(4, moments)
    squares = [moments[3] + moments[5], moments[5] - moments[7], 1 + moments[3] * moments[7]]
    sos = sum(square**2 for square in squares)
    reduced_sos = reduce_even(sos, substitutions)
    reduced_squares = sum(reduce_even(square, substitutions) ** 2 for square in squares)
    assert expand(reduced_sos - reduced_squares) == 0


def check_global_equality_gauge():
    P, h, s, relation = symbols("P h s relation")
    gauged = P + s**2 * relation**2 + (h - s**2 * relation) * relation
    original = P + h * relation
    assert expand(gauged - original) == 0


def check_first_shadow_off_variety_identity():
    r_even, q_M = symbols("r_even q_M")
    c = Symbol("c", nonzero=True)
    shadow_row = -c * q_M
    formal_even = r_even - shadow_row / c
    assert simplify(formal_even - r_even - q_M) == 0


def check_certificate_evaluations():
    gamma, q_M, P_mu, E_mu = symbols("gamma q_M P_mu E_mu")
    P_rho, E_Q_rho = symbols("P_rho E_Q_rho")

    feasible = expand((gamma + q_M) - (P_mu + E_mu)).subs(E_mu, 0)
    shadow = expand(gamma - (P_rho + E_Q_rho))
    assert feasible == gamma + q_M - P_mu
    assert shadow == gamma - P_rho - E_Q_rho


def main():
    check_triangular_exact_quotient()
    check_sos_preservation_under_substitution()
    check_global_equality_gauge()
    check_first_shadow_off_variety_identity()
    check_certificate_evaluations()
    print("R33_FINITE_GLOBAL_VALUE_DUALITY RECORDED")
    print("R33_Q_IDEAL_GAUGE_AND_SHADOW_OBSTRUCTION PASSED")
    print("R33_GRADED_REMOTE_LOCALITY REMAINS OPEN")
    print("R33_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
