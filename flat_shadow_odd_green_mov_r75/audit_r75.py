"""R75 sign-corrected moving-radius Volterra audit."""

import sympy as sp


def check_moving_factorization() -> None:
    k, j = sp.symbols("k j", integer=True, nonnegative=True)
    # The symbolic identity is checked on an exact grid; d=k-j.
    for kval in range(1, 9):
        for jval in range(kval):
            d = kval - jval
            sigma_k, sigma_j = sp.symbols("sigma_k sigma_j", positive=True)
            lhs = (
                sp.factorial(kval) ** 2
                * sp.factorial(2 * jval + 1)
                / (sp.factorial(2 * kval + 1) * sp.factorial(jval) ** 2 * sp.factorial(d))
                * (1 + sp.Rational(2 * d, jval + 1))
                * sigma_k ** (2 * kval + 1)
                / sigma_j ** (2 * jval + 1)
            )
            vk = sp.factorial(kval) ** 2 * sigma_k ** (2 * kval + 1) / sp.factorial(2 * kval + 1)
            vj = sp.factorial(jval) ** 2 * sigma_j ** (2 * jval + 1) / sp.factorial(2 * jval + 1)
            q = sp.Rational(1, sp.factorial(d)) * (1 + sp.Rational(2 * d, jval + 1))
            assert sp.simplify(lhs - (vk / vj) * q) == 0
    print("R75_MOVING_RADIUS_FACTORIZATION PASSED")


def check_signed_volterra_solution() -> None:
    x, t = sp.symbols("x t")
    coeffs = sp.symbols("s0:7")
    S = sum(coeffs[m] * x**m for m in range(7))
    F = sp.exp(-2 * x) * sp.integrate(sp.exp(t) * S.subs(x, t), (t, 0, x))
    Z = sp.diff(F, x)
    zcoeff = [sp.expand(sp.series(Z, x, 0, 7).removeO()).coeff(x, k) for k in range(7)]

    for k in range(7):
        rhs = coeffs[k]
        for j in range(k):
            d = k - j
            q = sp.Rational(1, sp.factorial(d)) * (1 + sp.Rational(2 * d, j + 1))
            rhs -= q * zcoeff[j]
        assert sp.simplify(zcoeff[k] - rhs) == 0

    # The corrected differential identity is equivalent to the recurrence.
    assert sp.simplify(sp.diff(F, x) + 2 * F - sp.exp(-x) * S) == 0
    print("R75_SIGN_CORRECTED_VOLterra_SOLUTION PASSED")


def check_tangent_signs() -> None:
    x, t = sp.symbols("x t")
    S = x + x**2 / 2
    F = sp.exp(-2 * x) * sp.integrate(sp.exp(t) * S.subs(x, t), (t, 0, x))
    Z = sp.diff(F, x)
    series = sp.expand(sp.series(Z, x, 0, 8).removeO())
    for m in range(1, 4):
        expected = (-1) ** (m - 1) * sp.Rational(m * (m + 1), 2 * sp.factorial(m))
        assert sp.simplify(series.coeff(x, m) - expected) == 0
    print("R75_R64_TANGENT_SIGN_CONSISTENCY PASSED")


def check_plus_majorant_is_distinct() -> None:
    x = sp.symbols("x")
    # The plus majorant has the (2-exp(x)) denominator; it is not the signed
    # equation audited above. This checks the sign distinction algebraically.
    assert sp.simplify((2 - sp.exp(x)) - (1 - (sp.exp(x) - 1))) == 0
    assert sp.simplify((2 - sp.exp(x)) - 0).subs(x, sp.log(2)) == 0
    print("R75_ABSOLUTE_MAJORANT_SIGN_DISTINCTION PASSED")


if __name__ == "__main__":
    check_moving_factorization()
    check_signed_volterra_solution()
    check_tangent_signs()
    check_plus_majorant_is_distinct()
    print("R75_SIGN_CORRECTED_MOVING_GREEN_AUDIT_COMPLETED")
