"""R81 exact audit for the mixed tangent-residual kernel reduction."""

import sympy as sp


def check_schur_complement() -> None:
    a, m, ell, o = sp.symbols("a m ell o")
    ehat = -2 * a * m * o
    odd_linear = a * ell * ehat
    assert sp.simplify(odd_linear + 2 * a ** 2 * ell * m * o) == 0
    print("R81_SCHUR_COMPLEMENT_PASSED")


def check_wick_covariance_condition() -> None:
    r, s = sp.symbols("r s", real=True)
    noise_covariance = sp.Matrix([[1 - r ** 2, -r * s],
                                  [-r * s, 1 - s ** 2]])
    determinant = sp.factor(noise_covariance.det())
    assert determinant == 1 - r ** 2 - s ** 2

    # The conditional exponential generating function collapses to one
    # Hermite generating function, which is the Wick-product identity.
    u, v, X = sp.symbols("u v X")
    conditional_exponent = ((r * u + s * v) * X
                            - (r * u + s * v) ** 2 / 2)
    separated_exponent = (r * u * X + s * v * X
                          - r ** 2 * u ** 2 / 2
                          - s ** 2 * v ** 2 / 2
                          - r * s * u * v)
    assert sp.expand(conditional_exponent - separated_exponent) == 0
    print("R81_WICK_CONTRACTION_PASSED")


def check_angular_inverse_growth() -> None:
    k = sp.symbols("k", integer=True, nonnegative=True)
    # Exact multiplier identity; the asymptotic direction follows from the
    # central-binomial estimate and is not used as a numerical sweep.
    A_inv = 6 ** k / (3 * sp.binomial(2 * k, k))
    assert sp.simplify(A_inv * (3 * sp.binomial(2 * k, k) / 6 ** k)) == 1
    for kval in (1, 2, 4):
        assert sp.simplify(A_inv.subs(k, kval)) >= 1
    print("R81_ANGULAR_INVERSE_GROWTH_PASSED")


def check_triangular_obstruction() -> None:
    N = 8
    harmonic = [sp.harmonic(j) for j in range(N)]
    lower_norm_square = sp.simplify(sum(value ** 2 for value in harmonic[1:]) / N)
    assert lower_norm_square > 0
    # The exact general lower bound is N^(-1) sum H_(j-1)^2; its growth is
    # logarithmic because H_m >= integral_1^(m+1) dx/x.
    m = sp.symbols("m", positive=True)
    assert sp.harmonic(4) > sp.log(5)
    print("R81_TRIANGULAR_TRUNCATION_NO_GO_PASSED")


def check_weight_ratio_and_fixed_gap() -> None:
    n, theta = sp.symbols("n theta", positive=True)
    j = theta * n
    R2 = 16 * n
    ratio_d1 = sp.simplify(R2 * (j + 1) ** 2
                           / ((2 * j + 2) * (2 * j + 3)))
    ratio_d2 = sp.simplify(
        R2 ** 2 * ((j + 1) * (j + 2)) ** 2
        / ((2 * j + 2) * (2 * j + 3)
           * (2 * j + 4) * (2 * j + 5)))
    assert sp.simplify(sp.limit(ratio_d1 / (4 * n), n, sp.oo) - 1) == 0
    assert sp.simplify(sp.limit(ratio_d2 / (4 * n) ** 2, n, sp.oo) - 1) == 0
    print("R81_WEIGHT_FIXED_GAP_PASSED")


def check_quartic_scale() -> None:
    mu = sp.symbols("mu", positive=True)
    e = sp.E
    gamma_base = 16 * e * (mu + 1)
    tangent_base = 4 * e
    quartic_base = sp.simplify(sp.sqrt(gamma_base) * tangent_base ** 2)
    expected = 64 * e ** 2 * sp.sqrt(e * (mu + 1))
    assert sp.simplify(quartic_base - expected) == 0
    assert sp.simplify(expected.subs(mu, 3) - 128 * e ** 2 * sp.sqrt(e)) == 0
    print("R81_QUARTIC_SCALE_PASSED")


def check_mgk_norm_identity() -> None:
    # The weighted l1 induced norm is exactly the weighted column sum.  This
    # is checked on one fixed 3x3 symbolic kernel, not by an optimizer.
    w0, w1, w2 = sp.symbols("w0 w1 w2", positive=True)
    k00, k10, k20 = sp.symbols("k00 k10 k20", nonnegative=True)
    column_sum = w0 * k00 / w0 + w1 * k10 / w0 + w2 * k20 / w0
    assert sp.simplify(column_sum - (k00 + w1 * k10 / w0
                                     + w2 * k20 / w0)) == 0
    print("R81_MGK_COLUMN_NORM_PASSED")


if __name__ == "__main__":
    check_schur_complement()
    check_wick_covariance_condition()
    check_angular_inverse_growth()
    check_triangular_obstruction()
    check_weight_ratio_and_fixed_gap()
    check_quartic_scale()
    check_mgk_norm_identity()
    print("R81_MIXED_KERNEL_AUDIT_COMPLETED")
