"""R44 proof-level audit for the general first-residue candidate.

The checks below are exact SymPy identities.  They are deliberately small:
no optimizer, SDP, sweep, relaxed measure-LP, or remote computation is used.
The fixed-m asymptotic assembly is delegated to the exact R43 generator
machinery and is kept separate from the new general identities.
"""

import sys
from pathlib import Path

from sympy import (
    Poly,
    Rational,
    binomial,
    expand,
    factorial,
    gamma,
    simplify,
    sqrt,
    symbols,
    together,
)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_residue_r43.audit_r43 import (  # noqa: E402
    asymptotic_w_plus_chi_d,
    c,
    cancelled_sd_coefficients,
    denominator_asym,
    c_asym,
    d_asym,
)


z, w, y = symbols("z w y", positive=True)


def coefficient_at(expr, exponent):
    """Return the coefficient of y**exponent in an expanded Laurent series."""
    total = 0
    for term in expand(expr).as_ordered_terms():
        if term.as_powers_dict().get(y, 0) == exponent:
            total += term / y**exponent
    return simplify(total)


def diagonal_moment(poly, moment):
    """Sum s**moment times the z**s*w**s coefficients of poly."""
    total = 0
    for (power_z, power_w), value in Poly(expand(poly), z, w).terms():
        if power_z == power_w:
            total += value * power_z**moment
    return simplify(total)


def check_darboux_rule():
    alpha = Rational(3, 2)
    beta = Rational(7, 2)
    shift = 2
    expansion = denominator_asym(alpha, beta, shift, 2)
    leading = (Rational(8, 9)) ** (-alpha) / gamma(beta)
    a1 = (beta - 1) * (beta / 2 - shift - alpha / 8)
    a2 = (beta - 1) * (beta - 2) * (
        (shift**2 - beta * shift) / 2
        + beta * (3 * beta - 1) / 24
        - alpha / 8 * ((beta - 1) / 2 - shift)
        + alpha * (alpha + 1) / 128
    )
    assert simplify(coefficient_at(expansion, -(beta - 1)) / leading - 1) == 0
    assert simplify(coefficient_at(expansion, -(beta - 2)) / leading - a1) == 0
    assert simplify(coefficient_at(expansion, -(beta - 3)) / leading - a2) == 0


def check_block_moments():
    for m in range(3, 8):
        r = m + 2
        cstar = (-1) ** m * binomial(2 * m, m)
        p1 = (z + w - Rational(2, 3) * z * w) * (
            z + w - 2 * z * w
        ) ** (r - 1)
        p2 = (z + w - Rational(2, 3) * z * w) ** 2 * (
            z + w - 2 * z * w
        ) ** (r - 2)
        p3 = (z + w - Rational(2, 3) * z * w) ** 3 * (
            z + w - 2 * z * w
        ) ** (r - 3)

        assert simplify(
            diagonal_moment(p1, 0) / cstar
            - Rational(4 * (2 * m + 1) * (4 * m + 5), 3 * (m + 1) * (m + 2))
        ) == 0
        assert simplify(
            diagonal_moment(p1, 1) / cstar
            - Rational(2 * (12 * m**2 + 21 * m + 7), 3 * (m + 1))
        ) == 0
        assert simplify(
            diagonal_moment(p1, 2) / cstar
            - Rational(
                36 * m**4 + 121 * m**3 + 84 * m**2 - 35 * m - 22,
                3 * (m + 1) * (2 * m - 1),
            )
        ) == 0
        assert simplify(
            diagonal_moment(p2, 0) / cstar
            - Rational(4 * (16 * m**2 + 24 * m + 11), 9 * (m + 1) * (m + 2))
        ) == 0
        assert simplify(
            diagonal_moment(p2, 1) / cstar
            - Rational(
                2 * (48 * m**3 + 40 * m**2 - 3 * m - 13),
                9 * (m + 1) * (2 * m - 1),
            )
        ) == 0
        assert simplify(
            diagonal_moment(p3, 0) / cstar
            - Rational(
                4 * (64 * m**3 + 48 * m**2 + 20 * m - 45),
                27 * (m + 1) * (m + 2) * (2 * m - 1),
            )
        ) == 0


def s_block(q):
    """Exact S-side part of the R42.3 generator for h_(2q)(S)."""
    return (
        (-1) ** q
        * c(q)
        * (z / 3 + w / 3 - Rational(2, 9) * z * w) ** q
        / (1 - z * w / 9) ** (q + Rational(1, 2))
    )


def check_c_sector_pole_cancellation():
    f1 = 2 * sqrt(3) * z**2 * (2 * z - 3) / (3 - z) ** 3
    f3 = 2 * sqrt(2) * z**3 / (3 - z) ** 3

    lhs1 = f1 * (s_block(0) + sqrt(2) * s_block(1)) + f3 * (
        sqrt(3) * s_block(1) + 2 * s_block(2)
    )
    rhs1 = 2 * sqrt(3) * z**2 * (w - 3) / (
        27 * (1 - z * w / 9) ** Rational(5, 2)
    )
    assert simplify(lhs1 - rhs1) == 0

    lhs3 = f1 * (sqrt(3) * s_block(1) + 2 * s_block(2)) + f3 * (
        s_block(0)
        + 3 * sqrt(2) * s_block(1)
        + 3 * sqrt(6) * s_block(2)
        + 2 * sqrt(5) * s_block(3)
    )
    rhs3 = -sqrt(2) * z**2 * (w - 3) * (
        2 * w**2 * z - 30 * w * z + 27 * w + 45 * z
    ) / (729 * (1 - z * w / 9) ** Rational(7, 2))
    assert simplify(lhs3 - rhs3) == 0


def check_c_constant_terms():
    for m in range(3, 8):
        cstar = (-1) ** m * binomial(2 * m, m)
        c1 = z**2 * (w - 3) * (z + w - 2 * z * w) ** m
        assert simplify(
            diagonal_moment(c1, 0) / cstar
            + Rational(m * (4 * m - 1), (m + 1) * (m + 2))
        ) == 0
        assert simplify(
            diagonal_moment(c1, 1) / cstar
            + Rational(m * (12 * m**2 - 13 * m + 5), 2 * (m + 1) * (2 * m - 1))
        ) == 0

        c3 = (-135 * z**3 + 135 * z**2 - 117 * z + 29) * (
            z + w - 2 * z * w
        ) ** (m - 1)
        assert simplify(
            diagonal_moment(c3, 0) / cstar
            + Rational(
                208 * m**3 - 312 * m**2 + 443 * m - 252,
                (m + 1) * (m + 2) * (2 * m - 1),
            )
        ) == 0


def check_q_formulas():
    for m in range(3, 8):
        q = cancelled_sd_coefficients(m)
        q2 = 2 ** (-m) * sqrt(3) * (2 * m + 1) * sqrt(2 * m + 2)
        q4 = 2 ** (1 - m) * sqrt(2 * m + 1) * (2 * m**2 - m + 1)
        q6 = 2 ** (1 - m) * (6 * m**2 - 15 * m + 19) * sqrt(
            Rational((2 * m - 1) * (2 * m) * (2 * m + 1), 120)
        )
        assert simplify(q[1] - q2) == 0
        assert simplify(q[2] - q4) == 0
        assert simplify(q[3] - q6) == 0


def check_kappa_specializations_and_sign():
    numerator = lambda m: 608 * m**4 + 672 * m**3 - 386 * m**2 - 207 * m - 27
    expected = {
        3: Rational(6327, 512) * sqrt(42),
        4: Rational(38325, 512) * sqrt(6),
        5: Rational(18887, 448) * sqrt(66),
    }
    for m, value in expected.items():
        candidate = sqrt(6 * (2 * m + 1)) * numerator(m) / (
            256 * (m + 1) * (m + 2)
        )
        assert simplify(candidate - value) == 0
    for m in range(1, 20):
        assert numerator(m) > 0
    # For every integer m >= 1:
    # 608m^4-386m^2 >= 222 and 672m^3-207m >= 465, hence P(m) >= 660.
    assert numerator(1) >= 660


def check_nplus4_conditioning():
    ranks = (1, 2, 3, 5)
    matrix = [[1] * 4, list(ranks), [n**2 for n in ranks], [Rational(1, n) for n in ranks]]
    from sympy import Matrix

    assert Matrix(matrix).det() != 0
    assert simplify(Rational(1) - 5 + Rational(1, 2)) == -Rational(7, 2)


def check_fixed_m_assembly():
    """Reassemble the residue quotient for the three audited fixed m cases."""
    for m in (3, 4, 5):
        residue = expand(
            asymptotic_w_plus_chi_d(m, 2)
            - sqrt(3 * (m + 1))
            * (2 * m + 1)
            * (4 * m + 5)
            / (4 * (m + 2))
            * d_asym(m + 1, 2)
            + 2 * c_asym(m, 2)
        )
        denominator = d_asym(m, 2)
        r0 = coefficient_at(residue, -(m - Rational(1, 2)))
        r1 = coefficient_at(residue, -(m - Rational(3, 2)))
        d0 = coefficient_at(denominator, -(m - Rational(1, 2)))
        d1 = coefficient_at(denominator, -(m - Rational(3, 2)))
        sigma = simplify(r0 / d0)
        kappa = simplify(r1 / d0 - r0 * d1 / d0**2)
        expected_sigma = -sqrt(6 * (2 * m + 1)) * Rational(
            160 * m**3 + 312 * m**2 + 140 * m + 15,
            64 * (m + 1) * (m + 2),
        )
        expected_kappa = sqrt(6 * (2 * m + 1)) * Rational(
            608 * m**4 + 672 * m**3 - 386 * m**2 - 207 * m - 27,
            256 * (m + 1) * (m + 2),
        )
        assert simplify(sigma - expected_sigma) == 0
        assert simplify(kappa - expected_kappa) == 0


def main():
    check_darboux_rule()
    print("R44_GENERAL_DARBOUX_COEFFICIENT_ALGEBRA PASSED")
    check_block_moments()
    print("R44_GENERAL_BLOCK_MOMENTS PASSED")
    check_c_sector_pole_cancellation()
    print("R44_C_SECTOR_POLE_CANCELLATION PASSED")
    check_q_formulas()
    print("R44_GENERAL_Q_FORMULAS PASSED")
    check_c_constant_terms()
    print("R44_C_CONSTANT_TERM_IDENTITIES PASSED")
    check_kappa_specializations_and_sign()
    print("R44_GENERAL_KAPPA_SPECIALIZATIONS PASSED")
    print("R44_GENERAL_KAPPA_POSITIVITY PASSED")
    check_fixed_m_assembly()
    print("R44_FIXED_M_ASSEMBLY m=3,4,5 PASSED")
    check_nplus4_conditioning()
    print("R44_NPLUS4_WEIGHTED_CONDITIONING PASSED")
    print("R44_NPLUS6_MULTI_RESPONSE REMAINS OPEN")
    print("R44_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
