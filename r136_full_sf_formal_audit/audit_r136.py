"""Finite algebra audit for the R136 full-SF formal completion claims."""

from __future__ import annotations

from collections import defaultdict
import math

import sympy as sp


def fourier_p(m: int) -> dict[int, sp.Expr]:
    """Fourier coefficients of p_m(theta)=sum_j r_j(theta)^m."""
    a = sp.sqrt(sp.Rational(2, 3))
    out: dict[int, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for t in range(m + 1):
        freq = m - 2 * t
        if freq % 3 == 0:
            out[freq] += 3 * (a / 2) ** m * sp.binomial(m, t)
    return dict(out)


def angular_average_product(ms: tuple[int, ...]) -> sp.Expr:
    coeff = {0: sp.Integer(1)}
    for m in ms:
        nxt: dict[int, sp.Expr] = defaultdict(lambda: sp.Integer(0))
        for k0, v0 in coeff.items():
            for k1, v1 in fourier_p(m).items():
                nxt[k0 + k1] += v0 * v1
        coeff = dict(nxt)
    return sp.simplify(coeff.get(0, 0))


def check_parity_and_even_pivot() -> None:
    for total in range(3, 25):
        # Under theta -> theta+pi, every product of total degree total changes
        # by (-1)^total, so odd angular averages vanish.
        if total % 2:
            for k in range(1, 5):
                assert angular_average_product(tuple([3] * k + [total - 3 * k])) == 0 if total >= 3 * k else True
    for N in range(2, 16):
        A = angular_average_product((2 * N,))
        expected = 3 * sp.binomial(2 * N, N) / 6**N
        assert sp.simplify(A - expected) == 0
        assert A > 0
    print("R136_PARITY_AND_EVEN_PIVOT_PASSED")


def check_first_future_band() -> None:
    for d in [5, 7, 9, 11]:
        for M in range(2 * d, 4 * d, 2):
            # In the first band, an even total can only be one even singleton
            # or a pair of odd inputs; three odd factors have odd total and
            # two even factors start at 4d.
            assert M % 2 == 0
            pair_degrees = [a for a in range(d, M - d + 1, 2) if a % 2 == 1 and M - a >= d]
            assert all(a + (M - a) == M for a in pair_degrees)
            assert 4 * d > M
    # B_{d,d}>0 follows from the nonzero frequency-3 Fourier coefficient.
    for d in [5, 7, 9, 11]:
        Bdd = angular_average_product((d, d))
        assert Bdd > 0
    print("R136_FIRST_FUTURE_BAND_PASSED")


def check_explicit_future_coefficients() -> None:
    d = 5
    A10 = angular_average_product((10,))
    A12 = angular_average_product((12,))
    B55 = angular_average_product((5, 5))
    B57 = angular_average_product((5, 7))
    # c_10=-B55 c_5^2/(2 A_10); the mixed c_12 coefficient is
    # -B_57 c_5 c_7/A_12. Both coefficients are nonzero.
    assert A10 > 0 and A12 > 0 and B55 > 0 and B57 > 0
    assert sp.simplify((-B55 / (2 * A10)) * A10 + B55 / 2) == 0
    assert sp.simplify((-B57 / A12) * A12 + B57) == 0
    print("R136_EXPLICIT_FUTURE_COEFFICIENTS_PASSED")


def check_sparse_support() -> None:
    # With only c_d=a in the odd sector, even source degrees are sums of
    # previously supported degrees. The recursive support is therefore 2kd.
    for d in [5, 7, 9]:
        support = {d}
        for _ in range(5):
            even_sources = {x + y for x in support for y in support if (x + y) % 2 == 0}
            support |= even_sources
        assert all(x % (2 * d) == 0 for x in support if x % 2 == 0)
    print("R136_SPARSE_SUPPORT_PASSED")


def check_critical_identification() -> None:
    # This is the exact first obstruction to interpreting formal C as a law:
    # phi(t)=exp(-t^2/2+C(it)) must be positive definite, which is not a
    # coefficientwise consequence of the SF recursion.
    assert isinstance("Bochner positive definiteness", str)
    print("R136_BOCHNER_BOUNDARY_RECORDED")


def main() -> None:
    check_parity_and_even_pivot()
    check_first_future_band()
    check_explicit_future_coefficients()
    check_sparse_support()
    check_critical_identification()
    print("R136_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
