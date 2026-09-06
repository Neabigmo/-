"""R46 exact second-residue probe for the N=6 multi-response frontier.

This audit is intentionally narrower than a full transgression argument.  It
derives the first two quotient columns for the H_(9,3) and H_(7,5) rows from
the exact Gaussian generators, then checks whether those two rows already give
rank at least two after quotienting the old N=6 response span.
"""

import sys
from functools import lru_cache
from pathlib import Path

from sympy import (
    Poly,
    Rational,
    binomial,
    expand,
    factorial,
    series,
    simplify,
    sqrt,
    symbols,
)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    c,
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    phi,
    two_body_projection_formula,
)
from flat_shadow_mixed_hessian_r40.audit_r40 import (  # noqa: E402
    mixed_hessian,
)
from flat_shadow_residue_r43.audit_r43 import (  # noqa: E402
    block_generator_coefficient,
    c_exact_raw,
    c_generator_terms,
    half_binomial_asym,
    hermite_product_coeff,
    rational_coefficient_at,
)


z, w, y = symbols("z w y", positive=True)


def coefficient_at(expr, exponent):
    total = 0
    for term in expand(expr).as_ordered_terms():
        if term.as_powers_dict().get(y, 0) == exponent:
            total += term / y**exponent
    return simplify(total)


def rational_coefficient_at_power(f_num, degree, power):
    """[z**degree] f_num(z)/(3-z)**power, with negative degrees zero."""
    if degree < 0:
        return 0
    poly = Poly(expand(f_num), z)
    return simplify(
        sum(
            poly.coeff_monomial(z**k)
            * binomial(degree - k + power - 1, power - 1)
            / 3 ** (degree - k + power)
            for k in range(degree + 1)
        )
    )


def c5_generator_terms(m):
    """Exact bivariate terms for C^(5) with external h_(2m+1)."""
    a = 2 * m + 1
    terms = []
    for j in range(1, a + 1, 2):
        u_j = 2 ** (1 - Rational(a, 2)) * sqrt(binomial(a, j))
        qd = (a - j) // 2
        d_pref = (-1) ** qd * c(qd)
        d_poly = (z + w - 2 * z * w) ** qd
        sectors = (
            (1, 2 * sqrt(15) * z**3 * (2 * z - 3) ** 2),
            (3, 4 * sqrt(10) * z**4 * (2 * z - 3)),
            (5, 4 * sqrt(2) * z**5),
        )
        for t, f_num in sectors:
            for ell in range(abs(j - t), j + t + 1, 2):
                product = hermite_product_coeff(j, t, ell)
                qs = ell // 2
                s_pref = (-1) ** qs * c(qs)
                poly = expand(
                    u_j
                    * d_pref
                    * d_poly
                    * f_num
                    * product
                    * s_pref
                    * (z / 3 + w / 3 - 2 * z * w / 9) ** qs
                )
                terms.append(
                    (poly, Rational(1, 2) + qs, Rational(1, 2) + qd, 5)
                )
    return terms


def c5_exact_raw(n, m):
    total = 0
    for poly, alpha, beta, power in c5_generator_terms(m):
        for (iz, iw), value in Poly(poly, z, w).terms():
            total += value * rational_coefficient_at_power(
                1, iw - iz, power
            ) * denominator_coefficient(n - iw, alpha, beta)
    return simplify(total)


def c5_direct_raw(n, m):
    x1, x2, x3 = symbols("x1 x2 x3")
    dot_p = marginal_gaussian(
        phi(n, x1, x2, x3) * h_norm(5, x3),
        [x3],
        [x1, x2, x3],
    )
    p = two_body_projection_formula(n, x1, x2)
    return simplify(
        gaussian_expectation(
            (h_norm(2 * m + 1, x1) + h_norm(2 * m + 1, x2))
            * p
            * dot_p,
            (x1, x2),
        )
    )


def denominator_coefficient(n, alpha, beta):
    if n < 0:
        return 0
    return simplify(
        sum(
            rf(alpha, p) / factorial(p) * Rational(1, 9) ** p
            * rf(beta, n - p) / factorial(n - p)
            for p in range(n + 1)
        )
    )


@lru_cache(maxsize=None)
def c5_asym(m, rel=2):
    out = 0
    for poly, alpha, beta, power in c5_generator_terms(m):
        for (iz, iw), value in Poly(poly, z, w).terms():
            f_coeff = rational_coefficient_at_power(1, iw - iz, power)
            if f_coeff:
                out += value * f_coeff * denominator_asym_full(
                    alpha, beta, iw, rel
                )
    return series(out, y, 0, rel + 1).removeO()


def rf(alpha, n):
    if n < 0:
        return 0
    out = 1
    for k in range(n):
        out *= alpha + k
    return out


@lru_cache(maxsize=None)
def d_asym_cached(m, rel):
    return d_asym_full(m, rel)


@lru_cache(maxsize=None)
def c_asym_cached(m, rel):
    return c_asym_full(m, rel)


@lru_cache(maxsize=None)
def denominator_asym_full(alpha, beta, shift, rel=2):
    """Darboux expansion retaining every analytic Taylor term needed."""
    f0 = Rational(8, 9) ** (-alpha)
    out = 0
    for p in range(rel + 1):
        analytic = f0 * (-1) ** p * rf(alpha, p) / (
            factorial(p) * 8**p
        )
        out += analytic * half_binomial_asym(beta - p, shift, rel - p)
    return series(out, y, 0, rel + 1).removeO()


@lru_cache(maxsize=None)
def block_asym_full(r, j, rel=2):
    numerator = expand(
        (z + w - Rational(2, 3) * z * w) ** j
        * (z + w - 2 * z * w) ** (r - j)
    )
    alpha = Rational(1, 2) + j
    beta = Rational(1, 2) + r - j
    diagonal = 0
    for (power_z, power_w), value in Poly(numerator, z, w).terms():
        if power_z == power_w:
            diagonal += value * denominator_asym_full(
                alpha, beta, power_z, rel
            )
    prefactor = (-1) ** r * Rational(1, 3) ** j * c(j) * c(r - j)
    return series(prefactor * diagonal, y, 0, rel + 1).removeO()


def d_asym_full(m, rel=2):
    return series(
        2
        * sum(
            Rational(1, 2) ** m
            * sqrt(binomial(2 * m, 2 * j))
            * block_asym_full(m, j, rel)
            for j in range(m + 1)
        ),
        y,
        0,
        rel + 1,
    ).removeO()


@lru_cache(maxsize=None)
def c_asym_full(m, rel=2):
    zz, ww = symbols("z w")
    out = 0
    for poly, alpha, beta in c_generator_terms(m):
        for (iz, iw), value in Poly(poly, zz, ww).terms():
            f_coeff = rational_coefficient_at(1, iw - iz)
            if f_coeff:
                out += value * f_coeff * denominator_asym_full(
                    alpha, beta, iw, rel
                )
    return series(out, y, 0, rel + 1).removeO()


def h75_w_asym(rel=2):
    s, d = symbols("s d")
    x1 = (s + d) / sqrt(2)
    x2 = (s - d) / sqrt(2)
    polynomial = h_norm(7, x1) * h_norm(5, x2) + h_norm(5, x1) * h_norm(7, x2)
    q = {
        j: simplify(
            gaussian_expectation(
                polynomial * h_norm(2 * j, s) * h_norm(12 - 2 * j, d),
                (s, d),
            )
        )
        for j in range(7)
    }
    return series(
        sum(q[j] * block_asym_full(6, j, rel) for j in range(7)),
        y,
        0,
        rel + 1,
    ).removeO()


def h75_w_exact(n):
    s, d = symbols("s d")
    x1 = (s + d) / sqrt(2)
    x2 = (s - d) / sqrt(2)
    polynomial = h_norm(7, x1) * h_norm(5, x2) + h_norm(5, x1) * h_norm(7, x2)
    return simplify(
        sum(
            gaussian_expectation(
                polynomial * h_norm(2 * j, s) * h_norm(12 - 2 * j, d),
                (s, d),
            )
            * block_generator_coefficient(n, 6, j)
            for j in range(7)
        )
    )


@lru_cache(maxsize=None)
def h93_asym(rel=2):
    chi = sqrt(binomial(12, 3))
    return series(
        asymptotic_w_plus_chi_d(4, rel)
        + 2 * c_asym_cached(4, rel)
        - chi * d_asym_cached(6, rel),
        y,
        0,
        rel + 1,
    ).removeO()


@lru_cache(maxsize=None)
def asymptotic_w_plus_chi_d(m, rel=2):
    r = m + 2
    s, d = symbols("s d")
    a = 2 * m + 1
    total = 2 * m + 4
    x1 = (s + d) / sqrt(2)
    x2 = (s - d) / sqrt(2)
    polynomial = h_norm(a, x1) * h_norm(3, x2) + h_norm(3, x1) * h_norm(a, x2)
    polynomial += sqrt(binomial(total, 3)) * (h_norm(total, x1) + h_norm(total, x2))
    q = {
        j: simplify(
            gaussian_expectation(
                polynomial * h_norm(2 * j, s) * h_norm(total - 2 * j, d),
                (s, d),
            )
        )
        for j in range(1, m + 2)
    }
    return series(
        sum(q[j] * block_asym_full(r, j, rel) for j in range(1, m + 2)),
        y,
        0,
        rel + 1,
    ).removeO()


@lru_cache(maxsize=None)
def h75_asym(rel=2):
    return series(h75_w_asym(rel) + 2 * c5_asym(3, rel), y, 0, rel + 1).removeO()


@lru_cache(maxsize=None)
def s3_asym(rel=2):
    m = 3
    rho = sqrt(3 * (m + 1)) * (2 * m + 1) * (4 * m + 5) / (4 * (m + 2))
    numerator = (
        asymptotic_w_plus_chi_d(3, rel)
        - rho * d_asym_cached(4, rel)
        + 2 * c_asym_cached(3, rel)
    )
    return series(numerator / d_asym_cached(3, rel), y, 0, rel + 1).removeO()


def quotient_row(row, basis, min_power=-3, max_power=3):
    """Triangular formal row reduction against the old N=6 span."""
    residual = series(row, y, 0, max_power + 1).removeO().expand()
    pivots = [
        series(pivot, y, 0, max_power + 1).removeO().expand()
        for pivot in basis
    ]
    for power, pivot in zip(range(min_power, 2), pivots):
        amount = simplify(coefficient_at(residual, power) / coefficient_at(pivot, power))
        residual = expand(residual - amount * pivot)
    return {
        power: simplify(coefficient_at(residual, power))
        for power in range(2, max_power + 1)
    }


def main():
    # The q=5 generator is checked against the independently defined full
    # mixed Hessian at the first nontrivial finite point.
    c53 = c5_exact_raw(3, 3)
    assert c53 == c5_direct_raw(3, 3)
    w75 = h75_w_exact(3)

    rel = 6
    d6 = d_asym_cached(3, rel)
    d8 = d_asym_cached(4, rel)
    d10 = d_asym_cached(5, rel)
    d12 = d_asym_cached(6, rel)
    old = [
        d12 / d6,
        d10 / d6,
        d8 / d6,
        1,
        s3_asym(5) - (-7563 * sqrt(42) / 1280),
    ]
    s3 = s3_asym(5)
    assert coefficient_at(s3, 0) == -7563 * sqrt(42) / 1280
    assert coefficient_at(s3, 1) == 6327 * sqrt(42) / 512
    rows = [h93_asym(rel) / d6, h75_asym(rel) / d6]
    quotients = [quotient_row(row, old, max_power=5) for row in rows]
    determinant = simplify(
        quotients[0][2] * quotients[1][3]
        - quotients[0][3] * quotients[1][2]
    )
    assert determinant != 0
    print(f"R46_H75_GENERATOR_FINITE_CHECK PASSED C53={c53} W75_RAW={w75}")
    print(f"R46_H93_QUOTIENT_SECOND_RESIDUE c32={quotients[0][2]} c33={quotients[0][3]}")
    print(f"R46_H75_QUOTIENT_SECOND_RESIDUE c52={quotients[1][2]} c53={quotients[1][3]}")
    print(f"R46_C3RES_FIRST_TWO_ROWS_RANK_GE2 DET={determinant}")
    print("R46_C3RES_FULL_MATRIX REMAINS OPEN")
    print("R46_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
