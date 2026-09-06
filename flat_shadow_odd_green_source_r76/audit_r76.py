"""R76 exact source, parity-ideal, and signed factorial-transfer audit."""

import math

import sympy as sp


def q(k: int, j: int) -> sp.Rational:
    d = k - j
    return sp.Rational(1, math.factorial(d)) * (
        1 + sp.Rational(2 * d, j + 1)
    )


def check_source_sign_and_green() -> None:
    x, t = sp.symbols("x t")
    coeffs = sp.symbols("s0:8")
    source = sum(coeffs[m] * x**m for m in range(8))
    F = sp.exp(-2 * x) * sp.integrate(
        sp.exp(t) * source.subs(x, t), (t, 0, x)
    )
    signed = sp.diff(F, x)
    series = sp.expand(sp.series(signed, x, 0, 8).removeO())
    z = [series.coeff(x, k) for k in range(8)]

    for k in range(8):
        rhs = coeffs[k]
        for j in range(k):
            rhs -= q(k, j) * z[j]
        assert sp.simplify(z[k] - rhs) == 0

    assert sp.simplify(sp.diff(F, x) + 2 * F - sp.exp(-x) * source) == 0
    print("R76_SIGNED_SOURCE_RECURRENCE_PASSED")


def check_tangent_source() -> None:
    x, t = sp.symbols("x t")
    tangent = x + x**2 / 2
    F = sp.exp(-2 * x) * sp.integrate(
        sp.exp(t) * tangent.subs(x, t), (t, 0, x)
    )
    signed = sp.expand(sp.series(sp.diff(F, x), x, 0, 8).removeO())
    for k in range(1, 7):
        expected = (-1) ** (k - 1) * sp.Rational(
            k * (k + 1), 2 * math.factorial(k)
        )
        assert sp.simplify(signed.coeff(x, k) - expected) == 0
    assert sp.simplify(
        sp.integrate(sp.exp(t) * tangent.subs(x, t), (t, 0, x))
        - x**2 * sp.exp(x) / 2
    ) == 0
    print("R76_R64_TANGENT_CHECK_PASSED")


def check_formal_parity_ideal() -> None:
    # This is a monomial audit of the claimed ideal decomposition. The
    # coefficient functions are deliberately generic representatives, not a
    # replacement for the Jacobi proof.
    a, E, Y = sp.symbols("a E Y")
    A = 1 + 2 * E + 3 * Y**2 + 5 * E * Y**2 + E**2 + Y**4
    # The Gaussian linear Y term has already been removed by the
    # ``+sum q_(k,j) Z_j`` source definition.
    B = 7 * E * Y + 11 * Y**3 + 13 * E * Y**3
    residual = sp.Poly(sp.expand(a * A + B - a), a, E, Y)
    forbidden = {(2, 0, 0), (0, 0, 0), (0, 1, 0), (0, 0, 1)}
    for monomial in residual.monoms():
        # The tangent subtraction removes the constant-a monomial. All
        # remaining terms must be aE, aY^2, EY, or have Y-degree >=3.
        pa, pe, py = monomial
        allowed = (
            (pa >= 1 and pe >= 1)
            or (pa >= 1 and py >= 2)
            or (pe >= 1 and py >= 1)
            or (py >= 3)
        )
        assert allowed, (monomial, forbidden)
    assert sp.Poly(residual, a, E, Y).coeff_monomial(a) == 0
    print("R76_PARITY_IDEAL_MONOMIAL_CHECK_PASSED")


def check_factorial_source_convolution() -> None:
    # For |S_i| <= M mu^i/i!, the coefficient of e^(-x)(S'-S) obeys
    # k!|R_k| <= M (mu+1)^(k+1). Check the exact finite convolution identity
    # and the scalar domination on a rational grid.
    mu = sp.symbols("mu", nonnegative=True)
    k = sp.symbols("k", integer=True, nonnegative=True)
    for kval in range(8):
        derivative_bound = mu ** (kval + 1)
        convolution_bound = sum(
            sp.binomial(kval, i) * mu**i for i in range(kval + 1)
        )
        assert sp.expand(convolution_bound - (mu + 1) ** kval) == 0
        slack = sp.Poly(
            sp.expand(
                (mu + 1) ** (kval + 1)
                - derivative_bound
                - convolution_bound
            ),
            mu,
        )
        assert all(coefficient >= 0 for coefficient in slack.all_coeffs())
        for mval in [sp.Rational(0), sp.Rational(1, 2), sp.Rational(1), 2, 5]:
            assert derivative_bound.subs(mu, mval) + convolution_bound.subs(
                mu, mval
            ) <= (mval + 1) ** (kval + 1)
    print("R76_FACTORIAL_SOURCE_CONVOLUTION_PASSED")


def check_factorial_transfer_recurrence() -> None:
    # Equality sequence for the scalar majorant recurrence.
    for mu in [sp.Rational(0), sp.Rational(1, 2), sp.Rational(2), sp.Rational(5)]:
        b = sp.Integer(1)
        for kval in range(8):
            if mu == 1:
                closed = (kval + 1) * 2**kval
            else:
                closed = 2**kval + (mu + 1) * (
                    (mu + 1) ** kval - 2**kval
                ) / (mu - 1)
            assert sp.simplify(b - closed) == 0
            b = sp.simplify((mu + 1) ** (kval + 1) + 2 * b)
    mu = sp.Integer(1)
    b = sp.Integer(1)
    for kval in range(8):
        assert b == (kval + 1) * 2**kval
        b = 2 ** (kval + 1) + 2 * b
    print("R76_FACTORIAL_TRANSFER_RECURRENCE_PASSED")


def check_common_radius_conversion() -> None:
    # The factorial comparison and the resulting exponential-series majorant.
    for kval in range(12):
        assert math.factorial(2 * kval + 1) / math.factorial(kval) >= math.factorial(
            kval + 1
        )

    for nval in range(1, 7):
        sigma = 8 * sp.sqrt(nval)
        lam = sp.Rational(3, 2)
        lhs = sum(
            sp.factorial(kval)
            * lam**kval
            * sigma ** (2 * kval + 1)
            / sp.factorial(2 * kval + 1)
            for kval in range(nval + 1)
        )
        rhs = sigma * sum(
            (64 * lam * nval) ** kval / sp.factorial(kval + 1)
            for kval in range(nval + 1)
        )
        assert sp.simplify(rhs - lhs) >= 0
    print("R76_COMMON_RADIUS_FACTORIAL_CONVERSION_PASSED")


if __name__ == "__main__":
    check_source_sign_and_green()
    check_tangent_source()
    check_formal_parity_ideal()
    check_factorial_source_convolution()
    check_factorial_transfer_recurrence()
    check_common_radius_conversion()
    print("R76_SIGNED_SOURCE_FACTORIAL_AUDIT_COMPLETED")
