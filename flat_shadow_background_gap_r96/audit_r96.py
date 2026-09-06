"""Fixed exact audits for the R96 background gap result.

This checks identities and representative finite channels only.  It does not
replace the analytic factorial-ratio proof by a numerical sweep.
"""

from math import factorial

import sympy as sp


X, z, w, q = sp.symbols("X z w q")


def eta(m: int) -> sp.Expr:
    if m % 2 == 0:
        return sp.Integer(0)
    r = (m - 1) // 2
    return sp.Rational((-1) ** (r - 1) * r * factorial(r + 1),
                       2) / sp.sqrt(factorial(2 * r + 1))


def product_coefficient(i: int, j: int, r: int) -> sp.Expr:
    m = i + j - 2 * r
    return (sp.factorial(r) * sp.binomial(i, r) * sp.binomial(j, r)
            * sp.sqrt(sp.Rational(factorial(m), factorial(i) * factorial(j))))


def actual_A(i: int, j: int) -> sp.Expr:
    return sp.simplify(sum(product_coefficient(i, j, r) * eta(i + j - 2 * r)
                           for r in range(min(i, j) + 1)))


def q_band(ell: int, a: int) -> sp.Expr:
    if ell - a - 4 < 0 or ell - 3 - 2 * a < 0:
        return sp.Integer(0)
    return sp.simplify(
        (-1) ** (a + 1)
        * sp.Rational((a + 1) * (a + 2), 2)
        * (a * a + 5 * a - 2 * (ell - 3))
        * sp.Rational(factorial(ell - a - 4), factorial(ell - 3 - 2 * a))
    )


def closed_A(ell: int, a: int) -> sp.Expr:
    k = ell - 3 - 2 * a
    return sp.simplify(-q_band(ell, a)
                       * sp.sqrt(sp.Rational(factorial(k), factorial(ell))))


def coefficient_formula(j: int, d: int, m: int, q_value: sp.Expr) -> sp.Expr:
    if (d - m) % 2:
        return sp.Integer(0)
    total = 0
    half = (d - m) // 2
    for r in range(0, j + half + 1):
        t = j + half - r
        top = (d + m) // 2 + r
        if t < 0 or top < 0 or top > m + 2 * r:
            continue
        total += ((-q_value) ** r
                  * sp.binomial(m + 2 * r, top)
                  / (sp.factorial(r) * sp.factorial(t)))
    return sp.simplify(sp.sqrt(factorial(j + d) * factorial(j)) * total)


def direct_bivariate_coefficient(j: int, d: int, m: int,
                                 q_value: sp.Expr) -> sp.Expr:
    # Only the finite total-degree truncation can contribute to z^(j+d)w^j.
    total_degree = 2 * j + d
    expr = 0
    for t in range(total_degree + 1):
        expr += (z * w) ** t / sp.factorial(t)
    expr = sum((z * w) ** t / sp.factorial(t)
               for t in range(total_degree + 1))
    expr *= sum((z + w) ** (m + 2 * r) * (-q_value) ** r
                / sp.factorial(r) for r in range(total_degree // 2 + 1))
    return sp.simplify(sp.sqrt(factorial(j + d) * factorial(j))
                       * sp.expand(expr).coeff(z, j + d).coeff(w, j))


def check_g1_matrix_channels() -> None:
    assert sp.simplify(actual_A(2, 1) - 1 / sp.sqrt(2)) == 0
    assert sp.simplify(actual_A(3, 0) - 1 / sp.sqrt(6)) == 0
    for ell in (4, 5, 7, 8, 9, 11):
        for a in range(0, min(3, (ell - 3) // 2 + 1)):
            k = ell - 3 - 2 * a
            if a == 0 and k == 0:
                continue
            assert sp.simplify(actual_A(ell, k) - closed_A(ell, a)) == 0
    for ell in range(3, 10):
        assert sp.simplify(actual_A(ell, ell - 1)) == 0
    print("R96_G1_EXACT_CHANNELS_PASSED")


def check_gap_coefficient_extractor() -> None:
    for j, d, m in ((0, 3, 3), (1, 3, 3), (2, 5, 3), (2, 5, 5), (3, 4, 6)):
        q_value = sp.Rational(1, 6)
        lhs = coefficient_formula(j, d, m, q_value)
        rhs = direct_bivariate_coefficient(j, d, m, q_value)
        assert sp.simplify(lhs - rhs) == 0
    assert coefficient_formula(2, 4, 3, sp.Rational(1, 6)) == 0
    print("R96_GAP_COEFFICIENT_EXTRACTOR_PASSED")


def check_factorial_ratio_and_lower_anchor() -> None:
    for a, k in ((2, 6), (3, 12), (5, 30)):
        ratio = sp.prod(k + r for r in range(1, a)) / sp.prod(
            k + r for r in range(a, 2 * a + 4))
        direct = (sp.factorial(k + a - 1) / sp.factorial(k)) ** 2 * (
            sp.factorial(k) / sp.factorial(k + 2 * a + 3))
        assert sp.simplify(ratio - direct) == 0
        assert k == a * (a + 1)
        assert a * a + 3 * a + 3 <= k + 2 * a + 3
    # The scalar maxima used in the R95 comparison remain exact.
    assert sp.simplify(7 * (sp.sqrt(3) / 2) ** 6 - sp.Rational(189, 64)) == 0
    print("R96_G1_FACTORIAL_RATIO_ANCHORS_PASSED")


def check_g2_endpoint_algebra() -> None:
    qs, qu, A, B, qt = sp.symbols("qs qu A B qt", nonnegative=True)
    alpha = 6 * qt * (A * qs + B * qu)
    weight_abs = (6 * qt) ** 3 * qs * qu * A ** sp.Rational(3, 2) * B ** sp.Rational(3, 2)
    reduced = sp.simplify(weight_abs / alpha ** 3)
    target = qs * qu * A ** sp.Rational(3, 2) * B ** sp.Rational(3, 2) / (A * qs + B * qu) ** 3
    assert sp.simplify(reduced - target) == 0
    x, y, U, V = sp.symbols("x y U V", positive=True)
    integral = sp.integrate(sp.integrate(x * y / (x + y) ** 3,
                                         (x, 0, U)), (y, 0, V))
    assert sp.simplify(integral - U * V / (2 * (U + V))) == 0
    assert sp.Rational(3, 8) < sp.Rational(1, 2)
    print("R96_G2_ENDPOINT_CANCELLATION_PASSED")


def check_hybrid_identity() -> None:
    j, n = sp.symbols("j n", nonnegative=True, integer=True)
    c = sp.factorial(j) ** 2 / sp.factorial(2 * j + 1)
    w_j = 16 ** j * c
    lhs = c * (4 * sp.sqrt(n)) ** (2 * j + 1)
    rhs = 4 * sp.sqrt(n) * n ** j * w_j
    assert sp.simplify(lhs - rhs) == 0
    print("R96_HYBRID_SCALE_IDENTITY_PASSED")


if __name__ == "__main__":
    check_g1_matrix_channels()
    check_gap_coefficient_extractor()
    check_factorial_ratio_and_lower_anchor()
    check_g2_endpoint_algebra()
    check_hybrid_identity()
    print("R96_BACKGROUND_GAP_AUDIT_COMPLETED")
