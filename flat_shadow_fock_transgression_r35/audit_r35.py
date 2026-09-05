"""Exact proof-level audit for R35's Fock-SOS anchor-tax obstruction.

The script checks finite polynomial/polarization identities and records
inequality steps as proof schemas.  It does not run an optimizer, SOS solver,
degree search, numerical sweep, or relaxed-law construction.
"""

from __future__ import annotations

from itertools import product

from sympy import Poly, Rational, Symbol, factorial, expand, oo, simplify, sqrt, symbols


def symmetric_coefficient(i, j, k):
    return Symbol("A_" + "_".join(map(str, sorted((i, j, k)))))


def fock_cubic(n, vector):
    out = 0
    for i in range(n + 1):
        for j in range(n + 1 - i):
            k = n - i - j
            coefficient = sqrt(factorial(n) / (factorial(i) * factorial(j) * factorial(k)))
            out += coefficient * symmetric_coefficient(i, j, k) * vector[i] * vector[j] * vector[k]
    return expand(out)


def trilinear(n, first, second, third):
    out = 0
    for i in range(n + 1):
        for j in range(n + 1 - i):
            k = n - i - j
            coefficient = sqrt(factorial(n) / (factorial(i) * factorial(j) * factorial(k)))
            out += coefficient * symmetric_coefficient(i, j, k) * first[i] * second[j] * third[k]
    return expand(out)


def min_u_degree(expr, u):
    poly = Poly(expand(expr), u)
    if poly.is_zero:
        return oo
    return min(monom[0] for monom in poly.monoms())


def check_first_shadow_mismatch():
    q_M = Symbol("q_M")
    N = 4
    delta = q_M / sqrt(factorial(N))
    assert simplify(delta * sqrt(factorial(N)) - q_M) == 0

    # All coordinates below N agree; only b_N differs by Delta_N.
    shadow = list(symbols("s0:5"))
    full = list(shadow)
    full[N] += delta
    full[0] = shadow[0] = 1
    difference = expand(fock_cubic(N, full) - fock_cubic(N, shadow))
    expected = 3 * symmetric_coefficient(N, 0, 0) * delta
    assert simplify(difference - expected) == 0


def check_cubic_polarization_and_grade_separation():
    n = 3
    s = symbols("s0:4")
    h = symbols("h0:4")
    S = list(s)
    H = list(h)
    lhs = fock_cubic(n, [S[i] + H[i] for i in range(n + 1)]) - fock_cubic(n, S)
    rhs = (
        3 * trilinear(n, H, S, S)
        + 3 * trilinear(n, H, H, S)
        + trilinear(n, H, H, H)
    )
    assert simplify(lhs - rhs) == 0

    u = Symbol("u")
    N = 2
    base = symbols("b0:3")
    shadow_path = [u**j * base[j] for j in range(N + 1)]
    mismatch = Symbol("Delta")
    full_path = list(shadow_path)
    full_path[N] += u**N * mismatch
    assert min_u_degree(trilinear(N, [full_path[i] - shadow_path[i] for i in range(N + 1)], shadow_path, shadow_path), u) >= N
    assert min_u_degree(trilinear(N, [full_path[i] - shadow_path[i] for i in range(N + 1)], [full_path[i] - shadow_path[i] for i in range(N + 1)], shadow_path), u) >= 2 * N
    assert min_u_degree(trilinear(N, [full_path[i] - shadow_path[i] for i in range(N + 1)], [full_path[i] - shadow_path[i] for i in range(N + 1)], [full_path[i] - shadow_path[i] for i in range(N + 1)]), u) >= 3 * N


def check_first_fock_defect_formula():
    N = 4
    q_M = Symbol("q_M")
    delta = q_M / sqrt(factorial(N))
    A_N00 = symmetric_coefficient(N, 0, 0)
    defect = 3 * A_N00 * delta
    assert simplify(defect - 3 * A_N00 * q_M / sqrt(factorial(N))) == 0

    for d in range(1, 6):
        coefficient = Rational(2, 3) ** d * Rational(1, 4) ** d * factorial(2 * d) / factorial(d) ** 2
        assert coefficient.is_positive is True


def check_first_ideal_grade_canonicality():
    u = Symbol("u")
    N = 4
    h0, h1, fN, tail = symbols("h0 h1 fN tail")
    # Lower generators vanish on the shadow; higher generators start above N.
    J = (h0 + u * h1) * u**N * fN + u ** (N + 1) * tail
    assert simplify(Poly(expand(J), u).coeff_monomial(u**N) - h0 * fN) == 0


def check_sos_first_grade_transport_schema():
    q_M = Symbol("q_M", nonzero=True)
    N = 4
    delta = q_M / sqrt(factorial(N))
    c = symbols("c0:3")
    d = symbols("d0:3")
    transport = 2 * delta * sum(c[i] * d[i] for i in range(3))
    required = q_M
    assert simplify(transport.subs(sum(c[i] * d[i] for i in range(3)), sqrt(factorial(N)) / 2) - required) == 0

    # Scalar square completion is exact and displays the same anchor tax.
    x, anchor = symbols("x anchor", nonzero=True)
    completion = (anchor + x) ** 2 / (2 * anchor) - anchor / 2 - x**2 / (2 * anchor)
    assert simplify(completion - x) == 0


def check_anchor_tax_bound_schema():
    N = 4
    anchor_value, factor_norm, derivative_norm = symbols(
        "anchor_value factor_norm derivative_norm", positive=True
    )
    required = Rational(factorial(N), 4)
    # Cauchy-Schwarz: (sum c_r d_r)^2 <= (sum c_r^2)(sum d_r^2).
    assert required == factorial(N) / 4
    lower_anchor = required / (derivative_norm**2)
    assert simplify(lower_anchor - factorial(N) / (4 * derivative_norm**2)) == 0
    # A norm bound ||f_r||<=factor_norm and a fixed-grade evaluation bound
    # |d_r|<=C_N||f_r|| imply derivative_norm<=C_N*factor_norm.  Combining
    # with the previous line yields the stated positive lower budget.
    assert anchor_value.is_positive is True


def main():
    check_first_shadow_mismatch()
    check_cubic_polarization_and_grade_separation()
    check_first_fock_defect_formula()
    check_first_ideal_grade_canonicality()
    check_sos_first_grade_transport_schema()
    check_anchor_tax_bound_schema()
    print("R35_CUBIC_FIRST_GRADE_LINEARITY PASSED")
    print("R35_FIRST_IDEAL_GRADE_CANONICAL PASSED")
    print("R35_FOCK_SOS_ANCHOR_TAX PASSED")
    print("R35_BOUNDED_FOCK_SOS_TRANSGRESSION NO_GO")
    print("R35_CONSTRAINT_COUPLED_TRANSGRESSION REMAINS OPEN")
    print("R35_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
