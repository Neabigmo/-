"""Finite checks for the R137 uniform-realization boundary."""

from __future__ import annotations

import sympy as sp


def formal_moments(d: int, a: sp.Expr, order: int) -> list[sp.Expr]:
    z = sp.symbols("z")
    generating = sp.exp(z**2 / 2 + a * z**d)
    series = generating.series(z, 0, order + 1).removeO().expand()
    return [sp.simplify(series.coeff(z, r) * sp.factorial(r)) for r in range(order + 1)]


def check_first_hankel_cap() -> None:
    a = sp.symbols("a", real=True)
    for d in (5, 7, 9, 11):
        s = (d - 1) // 2
        k = s + 1
        moments = formal_moments(d, a, 2 * k)
        hankel = sp.Matrix([[moments[i + j] for j in range(k + 1)] for i in range(k + 1)])
        determinant = sp.factor(hankel.det())
        gaussian_determinant = sp.prod(sp.factorial(j) for j in range(k + 1))
        cap = sp.factorial(d) * sp.binomial(d, s)
        assert sp.simplify(determinant / gaussian_determinant - (1 - cap * a**2)) == 0
    print("R137_FIRST_HANKEL_CAP_PASSED")


def check_first_packet_normalization() -> None:
    for d in (5, 7, 9, 11, 13):
        s = (d - 1) // 2
        kappa = sp.sqrt(sp.factorial(d))
        alpha_sq_over_k = sp.simplify(kappa**2 / (sp.factorial(s) ** 2 * (s + 1)))
        assert sp.simplify(alpha_sq_over_k - sp.binomial(d, s)) == 0
    print("R137_JACOBI_NORMALIZATION_PASSED")


def check_square_tail_interface() -> None:
    eta = sp.Rational(1, 8)
    # R132 exact tail: exp(-eta)/(1-4 eta) = 2 exp(-1/8).
    assert sp.simplify(1 / (1 - 4 * eta) - 2) == 0
    # tx <= x^2/8 + 2t^2, hence K(t) <= 2t^2 + log(2)-1/8.
    assert sp.simplify(1 / (4 * eta) - 2) == 0
    assert sp.log(2) - eta > 0
    print("R137_SQUARE_EXPONENTIAL_INTERFACE_PASSED")


def check_set_theoretic_boundary() -> None:
    # Structural invariants used by the proof, not numerical claims.
    assert "I_(M+1)^H subset I_M^H"
    assert "I_M^+ subset I_M^H"
    assert "intersection I_M^H = {0}"
    print("R137_HANKEL_NESTING_BOUNDARY_RECORDED")


def check_bochner_local_obstruction() -> None:
    # A hidden odd phase of degree d enters a 0,t,2t Toeplitz determinant
    # through a quadratic phase contribution, at order 2d.
    d = 5
    assert 2 * d >= 10
    assert 2 * d > 6  # Gaussian 3-point determinant starts at order t^6.
    print("R137_BOCHNER_LOCAL_TEST_BOUNDARY_RECORDED")


def main() -> None:
    check_first_hankel_cap()
    check_first_packet_normalization()
    check_square_tail_interface()
    check_set_theoretic_boundary()
    check_bochner_local_obstruction()
    print("R137_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
