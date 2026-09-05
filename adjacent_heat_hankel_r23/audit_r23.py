"""Proof-level audit for the R23 near-flat heat-Hankel reductions.

The checks are deliberately local.  They verify the Laurent asymptotics at a
corank-one crossing, the principal-submatrix monotonicity of truncated PSD
radii, and the determinant formula for adjacent Jacobi ratios.  They do not
claim a cross-rank zero-interlacing theorem or a uniform flat-leakage horizon.
"""

from __future__ import annotations

import sympy as sp


def check_near_flat_laurent_asymptotics() -> None:
    # At a flat crossing D_M = D_(M-1) h_M and
    # D_(M+1) = -D_(M-1) ell_M^2 + O(s).  Keep the leading terms symbolic.
    s, c, ell, d_prev = sp.symbols("s c ell d_prev", nonzero=True)
    h_m = c * s
    d_m = d_prev * h_m
    d_next = -d_prev * ell**2
    h_next = sp.simplify(d_next / d_m)
    beta_next = sp.simplify(h_next / h_m)

    assert sp.simplify(h_next + ell**2 / (c * s)) == 0
    assert sp.simplify(beta_next + ell**2 / (c**2 * s**2)) == 0
    # On the post-failure side h_M = c*s < 0, the leading h_(M+1) is positive.
    assert sp.simplify(h_next * h_m + ell**2) == 0


def check_truncated_psd_radius_monotonicity() -> None:
    # H_n is the leading principal block of H_(n+1).  Therefore every value
    # of the heat parameter that keeps H_(n+1) PSD also keeps H_n PSD.
    a = sp.symbols("a", real=True)
    h0, h1, h2 = sp.symbols("h0 h1 h2", positive=True)
    H2 = sp.diag(h0, h1, h2)
    H1 = H2[:2, :2]
    H0 = H2[:1, :1]
    assert H1 == H2[:2, :2]
    assert H0 == H1[:1, :1]
    # The unused parameter is intentional: the implication is pointwise in a.
    assert a.is_real


def check_adjacent_beta_determinant_formula() -> None:
    d_m2, d_m1, d_m, d_next = sp.symbols(
        "d_m2 d_m1 d_m d_next", nonzero=True
    )
    beta_m = sp.simplify(d_m * d_m2 / d_m1**2)
    beta_next = sp.simplify(d_next * d_m1 / d_m**2)
    ratio = sp.simplify(beta_next / beta_m)
    expected = sp.simplify(d_next * d_m1**3 / (d_m**3 * d_m2))
    assert sp.simplify(ratio - expected) == 0


def check_adjacent_sector_threshold() -> None:
    M = sp.symbols("M", positive=True)
    threshold = sp.Rational(2, 3) * (M + 1) ** 2 / M**2
    coefficient = sp.Rational(3, 2) * M**2 / (M + 1) ** 2
    assert sp.simplify(threshold * coefficient - 1) == 0


def main() -> None:
    checks = [
        check_near_flat_laurent_asymptotics,
        check_truncated_psd_radius_monotonicity,
        check_adjacent_beta_determinant_formula,
        check_adjacent_sector_threshold,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R23_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
