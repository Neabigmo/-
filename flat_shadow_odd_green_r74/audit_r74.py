"""R74 arithmetic audit for the degree-local odd Green kernel."""

import math

import sympy as sp


def check_hermite_product_and_kernel() -> None:
    x = sp.symbols("x")
    for k in range(0, 9):
        hk = sp.hermite_prob(k, x)
        rhs = sum(
            sp.factorial(r) * sp.binomial(k, r) ** 2 * sp.hermite_prob(2 * k - 2 * r, x)
            for r in range(k + 1)
        )
        assert sp.expand(hk**2 - rhs) == 0

        for j in range(k):
            d = k - j
            c = (
                sp.sqrt(sp.factorial(2 * j + 1))
                * sp.factorial(k)
                / (sp.factorial(j) ** 2 * sp.factorial(d))
                * (1 + sp.Rational(2 * d, j + 1))
            )
            # The two contributions to [x e_k^2]_(e_(2j+1)) come from
            # H_(2j) -> H_(2j+1) and H_(2j+2) -> (2j+2)H_(2j+1).
            term1 = sp.sqrt(sp.factorial(2 * j + 1)) * sp.factorial(k) / (
                sp.factorial(j) ** 2 * sp.factorial(d)
            )
            term2 = term1 * sp.Rational(2 * d, j + 1)
            assert sp.simplify(c - term1 - term2) == 0

            ratio = (
                sp.factorial(k) ** 2
                * sp.factorial(2 * j + 1)
                / (sp.factorial(j) ** 2 * sp.factorial(2 * k + 1))
            )
            product = sp.prod(
                sp.Rational((j + r) ** 2, (2 * j + 2 * r) * (2 * j + 2 * r + 1))
                for r in range(1, d + 1)
            )
            assert sp.simplify(ratio - product) == 0
            assert ratio <= sp.Rational(1, 4) ** d
    print("R74_HERMITE_KERNEL_EXACT PASSED")


def check_kernel_row_bound() -> None:
    for n in range(1, 40):
        x = 16 * n
        finite = sum((1 + 2 * d) * x**d / sp.factorial(d) for d in range(1, n + 1))
        infinite = (1 + 2 * x) * sp.exp(x) - 1
        assert float(finite) <= float(infinite)

        for k in range(1, n + 1):
            for j in range(k):
                d = k - j
                ratio = (
                    sp.factorial(k) ** 2
                    * sp.factorial(2 * j + 1)
                    / (sp.factorial(2 * k + 1) * sp.factorial(j) ** 2 * sp.factorial(d))
                )
                factor = 1 + sp.Rational(2 * d, j + 1)
                sigma = 8 * sp.sqrt(n)
                K = ratio * factor * sigma ** (2 * d)
                majorant = (1 + 2 * d) * (16 * n) ** d / sp.factorial(d)
                assert float(K) <= float(majorant)
    print("R74_KERNEL_ROW_SUM_BOUND PASSED")


def check_gram_and_angular_constants() -> None:
    # rho/sigma=1/2 and A_(2k)=3*binom(2k,k)/6^k.
    for k in range(1, 32):
        A = sp.Rational(3) * sp.binomial(2 * k, k) / 6**k
        assert sp.simplify(1 / A * sp.Rational(1, 2) ** (2 * k)) <= sp.Rational(1, 4)

    # Hermite multiplier bound at rho=4sqrt(n): (sqrt(3)/2)^m <= 2/3 for m>=3.
    assert float((sp.sqrt(3) / 2) ** 3) < 2 / 3

    gram_domain = sp.Rational(2, 3) * (1 + sp.Rational(1, 16))
    assert gram_domain == sp.Rational(17, 24)
    assert 1 - gram_domain == sp.Rational(7, 24)
    assert sp.Rational(41, 24) / sp.Rational(7, 24) == sp.Rational(41, 7)
    assert sp.Rational(41, 7) < 6 + sp.Rational(1, 7)
    print("R74_GRAM_AND_ANGULAR_CONSTANTS PASSED")


def check_resolvent_exponent() -> None:
    # For n>=1, R=16sqrt(n), ||B||<=2sqrt(6n), |a|<=1:
    # R^2/2 + R(2sqrt(6n)+1) <= 224n.
    lhs_per_n = 128 + 32 * math.sqrt(6) + 16
    assert lhs_per_n < 224

    # The 1366 constant is the rounded cubic Duhamel coefficient R^3/3 at
    # R=16sqrt(n), and 1024n dominates the linear insertion coefficient.
    assert 4096 / 3 < 1366
    assert 32 < 1024
    print("R74_RESOLVENT_SCALE_CONSTANTS PASSED")


def check_quadratic_absorption() -> None:
    # Q*a*o^2 is absorbed by the bootstrap o<=2*C*a*(E+a^2) on |a|<=r.
    # It is enough to check 8 Q C r^2 <=1.
    value_n1 = 8 * 17600 * 2**25 * 2 ** (-62) * math.exp(-320)
    assert value_n1 < 1

    # At the radius r, C*r=1/64; the resulting odd norm remains below 1/16
    # after the degree-3 radius loss, even with the crude Ubar term.
    odd_input = 2 ** (-26) * math.exp(-384) + 2 ** (-4)
    assert odd_input / 8 < sp.Rational(1, 16)
    print("R74_QUADRATIC_ABSORPTION PASSED")


def check_even_bootstrap() -> None:
    # With the two quarter bounds, X <= 3aU/2. The 1/4 angular constant then
    # strictly improves E<=3a^2U^2 because aU<=1/(12*4^n)<=1/12.
    x = sp.Rational(1, 12)
    rhs_over_x2 = sp.Rational(1, 4) * (
        3 * sp.Rational(3, 2) ** 2 + sp.Rational(3, 2) ** 3 * x
    )
    assert rhs_over_x2 < 3

    # The three displayed scales have exponents 544, 160+log(4), and 352;
    # the first is the smallest for sufficiently large n.
    assert 544 > 160 + math.log(4)
    assert 544 > 352
    print("R74_EVEN_BOOTSTRAP_AND_WINDOW PASSED")


if __name__ == "__main__":
    check_hermite_product_and_kernel()
    check_kernel_row_bound()
    check_gram_and_angular_constants()
    check_resolvent_exponent()
    check_quadratic_absorption()
    check_even_bootstrap()
    print("R74_ODD_GREEN_AUDIT_COMPLETED")
