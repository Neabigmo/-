"""Exact low-complexity audit for the R31 Jacobi-slack obstruction.

Only symbolic identities and exact rational sign tests are checked.  This
script does not search for multipliers, optimize a cone, or claim a
full-exact counterexample.
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


def path_linearization(polynomial, variables, m, r, parameter):
    path = {
        variables[j]: r[j] + parameter * (m[j] - r[j])
        for j in range(len(variables))
    }
    average = sum(
        integrate(diff(polynomial, variables[j]).subs(path), (parameter, 0, 1))
        * (m[j] - r[j])
        for j in range(len(variables))
    )
    endpoint_difference = polynomial.xreplace(dict(zip(variables, m))) - polynomial.xreplace(
        dict(zip(variables, r))
    )
    return simplify(expand(endpoint_difference - average))


def check_jacobi_odd_block():
    """Check the top odd derivative in the first two Jacobi coordinates."""
    s, m5, B3 = symbols("s m5 B3")
    p = 2 - s**2
    S1 = s
    S2 = (m5 - 4 * s) / p
    beta2 = symbols("B2") - S1**2
    beta3 = B3 - S2**2
    assert simplify(diff(S1, s) - 1) == 0
    assert simplify(diff(S2, m5) - 1 / p) == 0
    assert simplify(diff(beta2, s) + 2 * S1) == 0
    assert simplify(diff(beta3, m5) + 2 * S2 / p) == 0


def check_canonical_controls():
    Bn, un, uk = symbols("Bn un uk")
    beta = Bn * (1 - un**2)
    assert simplify(diff(beta, un) + 2 * Bn * un) == 0
    B = Symbol("B")
    u = Symbol("u")
    assert simplify(diff(B * (1 - u**2), B) - (1 - u**2)) == 0


def check_odd_pressure_formula():
    """Replay dG_(n+1)/d m_(2n-1) for n=2,...,6 exactly."""
    for n in range(2, 7):
        width = 2 * (n + 1) + 1
        moments = symbols(f"pressure_{n}_0:{width}")
        derivative = diff(G(n + 1, moments), moments[2 * n - 1]).subs(
            {moments[0]: 1, moments[1]: 0}
        )
        expected = -n * (n + 1) * (n + 5) * Rational(2, 3) ** (n + 1) * moments[3]
        assert simplify(derivative - expected) == 0


def check_next_slack_rational_sign():
    """Check the exact s=1/20,c=-1 delayed-slack sign obstruction."""
    s, c = symbols("s c")
    p = 2 - s**2
    B3 = 18 / p - 6
    beta3 = B3 - c**2
    t = p * c - 6 * s
    F = 105 * s**4 + 18 * s**3 * t - 168 * s**2 - 48 * s * t + 2 * t**2 - 48
    B4 = -F / (p**2 * beta3)
    point = {s: Rational(1, 20), c: -1}
    assert simplify(p.subs(point) - Rational(799, 400)) == 0
    assert simplify(B3.subs(point) - Rational(2406, 799)) == 0
    assert simplify(beta3.subs(point) - Rational(1607, 799)) == 0
    assert simplify(B4.subs(point) - Rational(51765601, 12839930)) == 0
    assert simplify(diff(B4, c).subs(point) + Rational(5809029, 5164898)) == 0
    dG4_dc = -Rational(512, 27) * s * p
    assert simplify(dG4_dc.subs(point) + Rational(6392, 3375)) == 0


def check_path_slack_augmentation():
    """Check the exact zero insertion that exposes the shadow-slack debt."""
    variables = symbols("b0:3")
    m = symbols("aug_m0:3")
    r = symbols("aug_r0:3")
    z = Symbol("aug_z")
    B = variables[0] + variables[1] * variables[2]
    S = variables[1] + variables[2]
    slack = expand(B - S**2)
    assert path_linearization(slack, variables, m, r, z) == 0

    eta, lam, c0, c1, c2 = symbols("eta lam c0 c1 c2")
    d = [m[j] - r[j] for j in range(3)]
    path = {variables[j]: r[j] + z * d[j] for j in range(3)}
    H = [integrate(diff(slack, variables[j]).subs(path), (z, 0, 1)) for j in range(3)]
    q_base = -lam - sum([c0, c1, c2][j] * d[j] for j in range(3))
    zero_inserted = eta * (
        slack.xreplace(dict(zip(variables, m)))
        - slack.xreplace(dict(zip(variables, r)))
        - sum(H[j] * d[j] for j in range(3))
    )
    assert simplify(expand(zero_inserted)) == 0
    grouped = (
        -lam
        + eta * slack.xreplace(dict(zip(variables, m)))
        - eta * slack.xreplace(dict(zip(variables, r)))
        - sum((([c0, c1, c2][j] + eta * H[j]) * d[j]) for j in range(3))
    )
    # The grouped form is q_base with the exact zero inserted; its debt term is
    # explicit and is not a remote Hermite tail.
    assert simplify(expand(grouped - q_base)) == 0


def main():
    check_jacobi_odd_block()
    check_canonical_controls()
    check_odd_pressure_formula()
    check_next_slack_rational_sign()
    check_path_slack_augmentation()
    print("R31_JACOBI_SLACK_STRUCTURE PASSED")
    print("R31_POSITIVE_ADJOINT_INF_SUP REMAINS OPEN")
    print("R31_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
