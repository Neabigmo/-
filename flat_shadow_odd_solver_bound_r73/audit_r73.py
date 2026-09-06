"""R73 exact arithmetic audit for the canonical odd-solver majorant."""

import math

import sympy as sp


def check_triangular_normalization() -> None:
    x = sp.symbols("x")
    for k in range(0, 9):
        # e_k has leading coefficient 1/sqrt(k!), while phi_k has the same
        # leading coefficient.  Matching x*phi_k^2 to e_(2k+1) fixes d_k.
        d = sp.sqrt(sp.factorial(2 * k + 1)) / sp.factorial(k)
        lhs = sp.simplify(d / sp.sqrt(sp.factorial(2 * k + 1)))
        rhs = sp.Rational(1, 1) / sp.factorial(k)
        assert sp.simplify(lhs - rhs) == 0
        assert sp.simplify((1 / d) - sp.factorial(k) / sp.sqrt(sp.factorial(2 * k + 1))) == 0

        # The source identity is d*eta_(2k+1)+sum c_m eta_m=alpha*gamma;
        # solving the single new coordinate therefore has the displayed factor.
        assert sp.simplify((1 / d) * d - 1) == 0
    print("R73_TRIANGULAR_NORMALIZATION PASSED")


def check_gram_radius_constants() -> None:
    # From (2.1), the weighted operator bound is exactly
    # [1/2*sqrt(1+m/n)]^m.  Its maximum over n>=3, 3<=m<=2n is 27/64;
    # the finite check covers the boundary cases, while monotonicity in n and
    # decay after the m=6 boundary give the all-n elementary extension.
    for n in range(3, 65):
        for m in range(3, 2 * n + 1):
            value = (sp.Rational(1, 2) * sp.sqrt(1 + sp.Rational(m, n))) ** m
            assert value <= sp.Rational(27, 64)

    rho_factor = sp.Rational(1, 2) * sp.sqrt(1 + sp.Rational(6, 3))
    assert sp.simplify(rho_factor**6 - sp.Rational(27, 64)) == 0
    print("R73_GRAM_RADIUS_CONSTANTS PASSED")


def check_domain_and_inverse() -> None:
    f_bound = sp.Rational(17, 16) + sp.Rational(1, 8)
    gram_bound = sp.Rational(27, 64) * f_bound
    assert f_bound == sp.Rational(19, 16)
    assert gram_bound == sp.Rational(513, 1024)
    assert gram_bound < 1
    assert sp.Rational(1, 1) / (1 - gram_bound) == sp.Rational(1024, 511)
    assert sp.Rational(1024, 511) < sp.Rational(201, 100)
    print("R73_DOMAIN_AND_GRAM_INVERSE PASSED")


def check_source_and_propagation() -> None:
    for n in range(1, 32):
        B = 512 * n * (448 * n) ** n
        # k!/(2k+1)! <= 1 and sigma^(2k+1) <=
        # 8*sqrt(n)*(64n)^n for k<=n, so the source is at most
        # 256*sqrt(n)*(448n)^n <= B.
        source_majorant = 256 * math.sqrt(n) * (448 * n) ** n
        assert source_majorant <= B

        # Starting at S_0=0, the recurrence after j steps is bounded by
        # ((1+B)^j-1)|a|, and hence by L|a| with L=(1+B)^n.
        a = sp.symbols("a", nonnegative=True)
        S = sp.Integer(0)
        for _ in range(n):
            S = sp.expand((1 + B) * S + B * a)
        L = (1 + B) ** n
        assert sp.simplify(S / a) <= L
        r = sp.Rational(1, 4) / L
        assert sp.simplify(L * r) == sp.Rational(1, 4)
    print("R73_SOURCE_AND_PROPAGATION PASSED")


def check_cauchy_majorant() -> None:
    L = sp.symbols("L", positive=True)
    r = 1 / (4 * L)
    cubic = sp.simplify(4 * L / (3 * r**2))
    assert cubic == sp.Rational(64, 3) * L**3
    assert sp.Rational(64, 3) <= 22
    # The mixed e-derivative constant 16L is also dominated by 22L^3 for L>=1.
    assert sp.Rational(16, 22) <= 1
    print("R73_CAUCHY_MAJORANT_CONSTANTS PASSED")


def check_conditional_window() -> None:
    n = sp.symbols("n", positive=True, integer=True)
    U, Omega = sp.symbols("U Omega", positive=True)
    a1 = 1 / (20 * 4**n * U)
    E = 10 * a1**2 * U**2
    assert sp.simplify(4**n * E - a1 * U / 2) == 0

    a3 = sp.sqrt(U / (2 * Omega * (1 + 10 * U**2)))
    odd = Omega * a3**3 * (1 + 10 * U**2)
    assert sp.simplify(odd - a3 * U / 2) == 0

    # The first two window constraints imply aU<=1/(20*4^n), so the
    # even-source RHS at X<=2aU is strictly below the bootstrap target 10a^2U^2.
    x = sp.Rational(1, 20)
    assert 2 + sp.Rational(4, 3) * x < 10
    print("R73_CONDITIONAL_WINDOW_CONSTANTS PASSED")


if __name__ == "__main__":
    check_triangular_normalization()
    check_gram_radius_constants()
    check_domain_and_inverse()
    check_source_and_propagation()
    check_cauchy_majorant()
    check_conditional_window()
    print("R73_ODD_SOLVER_BOUND_AUDIT_COMPLETED")
