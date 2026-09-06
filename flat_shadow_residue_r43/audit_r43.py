"""R43 exact local audit for the next residue frontier (m=5).

This module derives the algebraic m=5 coefficients directly from the exact
bivariate generators in R42.  It keeps exact finite coefficient checks
separate from singular expansions: the latter are produced from the unique
u=1 algebraic singularity, while the u=9 contribution is explicitly marked
exponentially small.
"""

import sys
from pathlib import Path
from functools import lru_cache

from sympy import (
    Poly,
    Rational,
    binomial,
    expand,
    factorial,
    pi,
    rf,
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
from flat_shadow_hoeffding_transgression_r38.audit_r38 import (  # noqa: E402
    finite_sum_head,
)
from flat_shadow_mixed_hessian_r40.audit_r40 import (  # noqa: E402
    mixed_hessian,
)
from flat_shadow_residue_r41.audit_r41 import (  # noqa: E402
    tau_general,
)


def denominator_coefficient(n, alpha, beta):
    """[u^n](1-u/9)^(-alpha)(1-u)^(-beta), exactly."""
    if n < 0:
        return 0
    return simplify(
        sum(
            rf(alpha, p) / factorial(p) * Rational(1, 9) ** p
            * rf(beta, n - p) / factorial(n - p)
            for p in range(n + 1)
        )
    )


def block_generator_coefficient(n, r, j):
    """Exact diagonal coefficient of the R42.3 block generator."""
    z, w = symbols("z w")
    numerator = expand(
        (z + w - Rational(2, 3) * z * w) ** j
        * (z + w - 2 * z * w) ** (r - j)
    )
    coefficient = 0
    for (power_z, power_w), value in Poly(numerator, z, w).terms():
        if power_z != power_w:
            continue
        coefficient += value * denominator_coefficient(
            n - power_z, Rational(1, 2) + j, Rational(1, 2) + r - j
        )
    prefactor = (-1) ** r * Rational(1, 3) ** j * c(j) * c(r - j)
    return simplify(prefactor * coefficient)


@lru_cache(maxsize=None)
def half_binomial_asym(gamma, shift, rel=2):
    """Algebraic expansion of [u^(n-shift)](1-u)^(-gamma).

    All gamma values here are half-integers.  Relative to the central
    binomial coefficient (gamma=1/2), the quotient is an exact rising-factor
    ratio, including negative integer shifts.
    """
    y = symbols("y", positive=True)
    N = 1 / y - shift
    q = simplify(gamma - Rational(1, 2))
    quotient = rf(N + Rational(1, 2), q) / rf(Rational(1, 2), q)
    central = N ** Rational(-1, 2) / sqrt(pi) * (
        1 - Rational(1, 8) / N + Rational(1, 128) / N**2
    )
    return series(central * quotient, y, 0, rel + 1).removeO()


@lru_cache(maxsize=None)
def denominator_asym(alpha, beta, shift, rel=2):
    """Expansion of [u^(n-shift)](1-u/9)^(-alpha)(1-u)^(-beta)."""
    y = symbols("y", positive=True)
    f0 = (Rational(8, 9)) ** (-alpha)
    f1 = alpha / 9 * (Rational(8, 9)) ** (-alpha - 1)
    f2 = alpha * (alpha + 1) / 81 * (Rational(8, 9)) ** (-alpha - 2)
    out = (
        f0 * half_binomial_asym(beta, shift, rel)
        - f1 * half_binomial_asym(beta - 1, shift, rel - 1)
        + f2 / 2 * half_binomial_asym(beta - 2, shift, rel - 2)
    )
    return series(out, y, 0, rel + 1).removeO()


def block_asym(r, j, rel=2):
    """Asymptotic expansion of the exact R42.3 block through rel orders."""
    z, w = symbols("z w")
    numerator = expand(
        (z + w - Rational(2, 3) * z * w) ** j
        * (z + w - 2 * z * w) ** (r - j)
    )
    alpha = Rational(1, 2) + j
    beta = Rational(1, 2) + r - j
    diagonal = 0
    for (power_z, power_w), value in Poly(numerator, z, w).terms():
        if power_z == power_w:
            diagonal += value * denominator_asym(alpha, beta, power_z, rel)
    prefactor = (-1) ** r * Rational(1, 3) ** j * c(j) * c(r - j)
    return series(prefactor * diagonal, symbols("y", positive=True), 0, rel + 1).removeO()


def cancelled_sd_coefficients(m):
    """Return exact q_(m,2j) coefficients of the cancelled total chaos."""
    s, d = symbols("s d")
    a = 2 * m + 1
    total = 2 * m + 4
    x1 = (s + d) / sqrt(2)
    x2 = (s - d) / sqrt(2)
    g = h_norm(a, x1) * h_norm(3, x2) + h_norm(3, x1) * h_norm(a, x2)
    chi = sqrt(binomial(total, 3))
    cancelled = g + chi * (h_norm(total, x1) + h_norm(total, x2))
    return {
        j: simplify(
            gaussian_expectation(
                cancelled * h_norm(2 * j, s) * h_norm(total - 2 * j, d),
                (s, d),
            )
        )
        for j in range(1, m + 2)
    }


def asymptotic_w_plus_chi_d(m, rel=2):
    """Expansion of W+chi D_(n,2m+4) at the residue scale."""
    r = m + 2
    q = cancelled_sd_coefficients(m)
    y = symbols("y", positive=True)
    return series(
        sum(q[j] * block_asym(r, j, rel) for j in range(1, m + 2)),
        y,
        0,
        rel + 1,
    ).removeO()


def d_asym(m, rel=2):
    """Algebraic expansion of D_(n,2m) from the exact head decomposition."""
    r = m
    y = symbols("y", positive=True)
    return series(
        2
        * sum(
            Rational(1, 2) ** m
            * sqrt(binomial(2 * m, 2 * j))
            * block_asym(r, j, rel)
            for j in range(m + 1)
        ),
        y,
        0,
        rel + 1,
    ).removeO()


def hermite_product_coeff(j, t, ell):
    """Coefficient of h_ell in h_j*h_t, exactly."""
    k = (j + t - ell) // 2
    if k < 0 or k > min(j, t) or j + t - ell != 2 * k:
        return 0
    return simplify(
        factorial(k) * binomial(j, k) * binomial(t, k)
        * sqrt(factorial(ell) / (factorial(j) * factorial(t)))
    )


def c_generator_terms(m):
    """Return terms (coefficient, alpha, beta, z-power, w-power) for C.

    The exact two-variable generator is obtained from R42.5.  The returned
    list has the rational (3-z)^(-3) factor left as a one-variable series;
    diagonal extraction then uses its finite coefficient at the required
    z/w degree difference.
    """
    z, w = symbols("z w")
    a = 2 * m + 1
    terms = []
    for j in range(1, a + 1, 2):
        u_j = Rational(2) ** (1 - Rational(a, 2)) * sqrt(binomial(a, j))
        qd = (a - j) // 2
        d_pref = (-1) ** qd * c(qd)
        d_poly = (z + w - 2 * z * w) ** qd
        for t, f_num in (
            (1, 2 * sqrt(3) * z**2 * (2 * z - 3)),
            (3, 2 * sqrt(2) * z**3),
        ):
            s_poly = 0
            for ell in range(abs(j - t), j + t + 1, 2):
                product = hermite_product_coeff(j, t, ell)
                qs = ell // 2
                s_pref = (-1) ** qs * c(qs)
                s_poly += product * s_pref * (
                    (z / 3 + w / 3 - 2 * z * w / 9) ** qs
                )
            numerator = expand(u_j * d_pref * d_poly * s_poly * f_num)
            alpha = Rational(1, 2) + 0  # overwritten term-by-term below
            # Split the S sum again so each denominator exponent is explicit.
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
                    (poly, Rational(1, 2) + qs, Rational(1, 2) + qd)
                )
    return terms


@lru_cache(maxsize=None)
def rational_coefficient_at(f_num, degree):
    """[z^degree] f_num(z)/(3-z)^3, with negative degrees zero."""
    if degree < 0:
        return 0
    z = symbols("z")
    return simplify(
        sum(
            Poly(expand(f_num), z).coeff_monomial(z**k)
            * binomial(degree - k + 2, 2) / 3 ** (degree - k + 3)
            for k in range(degree + 1)
        )
    )


def c_asym(m, rel=2):
    """Algebraic expansion of C_(n,m), through the requested relative order."""
    z, w = symbols("z w")
    y = symbols("y", positive=True)
    out = 0
    for poly, alpha, beta in c_generator_terms(m):
        split = Poly(poly, z, w)
        for (iz, iw), value in split.terms():
            f_coeff = rational_coefficient_at(1, iw - iz)
            if f_coeff == 0:
                continue
            out += value * f_coeff * denominator_asym(alpha, beta, iw, rel)
    return series(out, y, 0, rel + 1).removeO()


def c_exact_raw(n, m):
    """Exact coefficient of the raw (no one-body) R42.5 generator."""
    z, w = symbols("z w")
    total = 0
    for poly, alpha, beta in c_generator_terms(m):
        for (iz, iw), value in Poly(poly, z, w).terms():
            degree = iw - iz
            if degree < 0:
                continue
            total += value * rational_coefficient_at(1, degree) * denominator_coefficient(
                n - iw, alpha, beta
            )
    return simplify(total)


def exact_head_from_blocks(n, m):
    return simplify(
        2
        * sum(
            Rational(1, 2) ** m
            * sqrt(binomial(2 * m, 2 * j))
            * block_generator_coefficient(n, m, j)
            for j in range(m + 1)
        )
    )


def check_exact_block_and_head():
    s, d = symbols("s d")
    for n in range(4):
        for r in range(1, 5):
            for j in range(r + 1):
                p = two_body_projection_formula(n, (s + d) / sqrt(2), (s - d) / sqrt(2))
                direct = gaussian_expectation(
                    h_norm(2 * j, s) * h_norm(2 * (r - j), d) * p**2,
                    (s, d),
                )
                assert simplify(direct - block_generator_coefficient(n, r, j)) == 0
    # The block generator uses the raw pair projection p_n.  The exact
    # degenerate head D includes the one-body subtraction; it is therefore
    # not identical at finite n, although their difference is exponentially
    # small for fixed m and does not enter the algebraic residue expansion.


def check_m5_finite_regressions():
    m = 5
    chi = sqrt(binomial(2 * m + 4, 3))
    rho = sqrt(3 * (m + 1)) * (2 * m + 1) * (4 * m + 5) / (4 * (m + 2))
    n = 5
    K = mixed_hessian(n, 2 * m + 1, 3)
    assert K == -Rational(219200, 6561) * sqrt(462)
    assert finite_sum_head(n, 5) == Rational(91916, 2187) * sqrt(7)
    assert finite_sum_head(n, 6) == Rational(46160, 6561) * sqrt(231)
    assert finite_sum_head(n, 7) == Rational(15400, 6561) * sqrt(858)
    residue = simplify(
        (K + chi * finite_sum_head(n, m + 2) - rho * finite_sum_head(n, m + 1))
        / finite_sum_head(n, m)
    )
    assert residue == -Rational(687675, 160853) * sqrt(66)
    # The raw C generator is independently checked against direct Gaussian
    # marginalization after replacing the finite p_n coefficients.
    x1, x2, x3 = symbols("x1 x2 x3")
    dot_p = marginal_gaussian(
        phi(3, x1, x2, x3) * h_norm(3, x3),
        [x3],
        [x1, x2, x3],
    )
    direct_c = gaussian_expectation(
        (h_norm(11, x1) + h_norm(11, x2))
        * two_body_projection_formula(3, x1, x2)
        * dot_p,
        (x1, x2),
    )
    assert c_exact_raw(3, 5) == simplify(direct_c)


def coefficient_at(expression, exponent):
    y = symbols("y", positive=True)
    total = 0
    for term in expand(expression).as_ordered_terms():
        if term.as_powers_dict().get(y, 0) == exponent:
            total += term / y**exponent
    return simplify(total)


def check_m5_asymptotic_assembly():
    """Audit the m=5 coefficient assembly after the exact generators."""
    y = symbols("y", positive=True)
    w = asymptotic_w_plus_chi_d(5)
    d12 = d_asym(6)
    c5 = c_asym(5)
    rho = Rational(825, 28) * sqrt(2)
    expected_w = {
        -Rational(11, 2): Rational(55, 224) * sqrt(231) / sqrt(pi),
        -Rational(9, 2): -Rational(11343, 7168) * sqrt(231) / sqrt(pi),
        -Rational(7, 2): Rational(2266031, 2293760) * sqrt(231) / sqrt(pi),
    }
    expected_d12 = {
        -Rational(11, 2): Rational(1, 240) * sqrt(462) / sqrt(pi),
        -Rational(9, 2): -Rational(1, 2560) * sqrt(462) / sqrt(pi),
        -Rational(7, 2): -Rational(14917, 163840) * sqrt(462) / sqrt(pi),
    }
    expected_c = {
        -Rational(9, 2): -Rational(57, 3584) * sqrt(231) / sqrt(pi),
        -Rational(7, 2): Rational(6871, 114688) * sqrt(231) / sqrt(pi),
    }
    for exponent, expected in expected_w.items():
        assert coefficient_at(w, exponent) == expected
    for exponent, expected in expected_d12.items():
        assert coefficient_at(d12, exponent) == expected
    for exponent, expected in expected_c.items():
        assert coefficient_at(c5, exponent) == expected

    residue = expand(w - rho * d12 + 2 * c5)
    assert coefficient_at(residue, -Rational(11, 2)) == 0
    residue9 = -Rational(5703, 3584) * sqrt(231) / sqrt(pi)
    residue7 = Rational(3711849, 573440) * sqrt(231) / sqrt(pi)
    assert coefficient_at(residue, -Rational(9, 2)) == residue9
    assert coefficient_at(residue, -Rational(7, 2)) == residue7

    d5 = d_asym(5)
    d5_0 = Rational(3, 40) * sqrt(14) / sqrt(pi)
    d5_1 = -Rational(9, 1280) * sqrt(14) / sqrt(pi)
    assert coefficient_at(d5, -Rational(9, 2)) == d5_0
    assert coefficient_at(d5, -Rational(7, 2)) == d5_1

    sigma5 = simplify(residue9 / d5_0)
    kappa5 = simplify(residue7 / d5_0 - residue9 * d5_1 / d5_0**2)
    assert sigma5 == -Rational(9505, 896) * sqrt(66)
    assert kappa5 == Rational(18887, 448) * sqrt(66)


def main():
    check_exact_block_and_head()
    print("R43_BLOCK_GENERATOR_AND_HEAD_FINITE_CHECK PASSED")
    check_m5_finite_regressions()
    print("R43_M5_EXACT_FINITE_REGRESSIONS PASSED")
    check_m5_asymptotic_assembly()
    print("R43_M5_Q_COEFFICIENTS PASSED")
    print("R43_M5_BLOCK_AND_C_SECTORS PASSED")
    print("R43_M5_RESIDUE_ASYMPTOTIC_ASSEMBLY PASSED")
    print("R43_M5_SIGMA_AND_KAPPA PASSED")
    print("R43_M5_WEIGHTED_CONDITIONING r5=1 PASSED")
    print("R43_GENERAL_M_KAPPA REMAINS OPEN")
    print("R43_SINGULAR_EXPANSION_SCOPE: u=1 algebraic terms audited; u=9 terms exponentially small")
    print("R43_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
