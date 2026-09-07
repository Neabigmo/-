"""Finite exact audit for R109.

This verifies the parallelogram Gram Schur algebra, the cocycle disk
factorization, the shear Taylor polynomial, and the degree-six exactness
defect.  It does not claim the elliptic modulus-saturation lemma.
"""

from __future__ import annotations

import sympy as sp


def check_parallelogram_schur() -> None:
    a, b, c, d = sp.symbols("a b c d")
    ab, bb, cb, db = sp.symbols("ab bb cb db")
    gram = sp.Matrix([
        [1, ab, cb, db],
        [a, 1, bb, cb],
        [c, b, 1, ab],
        [d, c, a, 1],
    ])
    edge = gram[:2, :2]
    complement = gram[2:, 2:] - gram[2:, :2] * edge.inv() * gram[:2, 2:]
    delta0 = 1 + a * b * cb + ab * bb * c - a * ab - b * bb - c * cb
    delta1 = 1 + a * c * db + ab * cb * d - a * ab - c * cb - d * db
    n = ab * (1 - a * ab + c * cb) - b * cb - c * db + a * b * db
    nbar = a * (1 - a * ab + c * cb) - bb * c - cb * d + ab * bb * d
    target = sp.Matrix([[delta0, n], [nbar, delta1]]) / (1 - a * ab)
    assert all(sp.simplify(sp.together(x)) == 0
               for x in (complement - target))
    assert sp.simplify(sp.together(gram.det()
                                   - edge.det() * complement.det())) == 0
    print("R109_PARALLELOGRAM_SCHUR_DECOMPOSITION_PASSED")


def check_cocycle_disk_factorization() -> None:
    # Use formal unit phase monomials A,B,C,D and their inverses.  This is
    # algebraically identical to A=exp(i*alpha), etc., but avoids a slow
    # transcendental ``expand_complex`` simplification.
    r0, r1, r2, r3 = sp.symbols("r0 r1 r2 r3", nonzero=True)
    A, B, C, D = sp.symbols("A B C D", nonzero=True)
    a = r0 * A
    b = r1 * B
    c = r2 * C
    d = r3 * D
    ab = r0 / A
    bb = r1 / B
    cb = r2 / C
    db = r3 / D
    n = ab * (1 - a * ab + c * cb) - b * cb - c * db + a * b * db
    phase0 = A * B / C
    phase1 = A * C / D
    phase_minus_eta = phase1 / phase0
    p = 1 - r0**2 + r2**2 - r1 * r2 / r0 * phase0
    q = phase0 * (-r2 * r3 / r0 + r1 * r3 * phase0)
    xi = sp.cancel(n / ab)
    assert sp.factor(xi - (p + phase_minus_eta * q)) == 0
    print("R109_COCYCLE_DISK_FACTORIZATION_PASSED")


def check_shear_expansion_and_exactness_gap() -> None:
    s, t, kappa3, kappa6, lam = sp.symbols(
        "s t kappa3 kappa6 lambda", real=True
    )
    cubic_bracket = sp.expand(t**3 - 2 * (s + t)**3 + (2 * s + t)**3)
    assert sp.factor(cubic_bracket) == 6 * s**2 * (s + t)
    eta_cubic = sp.simplify(-kappa3 * cubic_bracket / 6)
    assert eta_cubic == -kappa3 * s**2 * (s + t)

    z = sp.symbols("z")
    coeff = (kappa6 + 3 * kappa3**2) / 2592
    obstruction = sp.simplify(coeff.subs({kappa6: -6 * lam**3,
                                          kappa3**2: lam**3}))
    assert obstruction == -lam**3 / 864
    characteristic_axis = sp.simplify(obstruction * sp.I**6)
    assert characteristic_axis == lam**3 / 864
    print("R109_SHEAR_AND_DEGREE6_EXACTNESS_GAP_PASSED")


def check_elliptic_geometry() -> None:
    s, t, y = sp.symbols("s t y")
    assert sp.expand(s**2 + (s + t)**2 + (2 * s + t)**2
                     - (6 * s**2 + 6 * s * t + 2 * t**2)) == 0
    print("R109_ELLIPTIC_PRODUCT_GEOMETRY_PASSED")


def main() -> None:
    check_parallelogram_schur()
    check_cocycle_disk_factorization()
    check_shear_expansion_and_exactness_gap()
    check_elliptic_geometry()
    print("R109_PARALLELOGRAM_BOCHNER_COCYCLE_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
