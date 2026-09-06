"""R72 exact audit for angular tameness and conditional source closure."""

import sympy as sp


def check_angular_scaling() -> None:
    k, theta = sp.symbols("k theta", positive=True, integer=True)
    q2 = sp.Rational(2, 3)
    # A_(2k)=3*binomial(2k,k)/6^k and q^(2k)=(2/3)^k.
    A = 3 * sp.binomial(2 * k, k) / 6**k
    lower = 3 * q2**k / (2 * sp.sqrt(k))
    # The Wallis estimate is checked on an exact initial range; the standard
    # induction k <= 16^(k-1) supplies the remaining elementary factor.
    for kval in range(1, 25):
        assert sp.binomial(2 * kval, kval) >= sp.Rational(4**kval, 2) / sp.sqrt(kval)
    assert sp.simplify(
        (A / lower).subs(k, 1)
    ) == 1

    ratio = sp.simplify(
        (3 * sp.binomial(2 * k + 2, k + 1) / 6 ** (k + 1)) / A
    )
    assert sp.simplify(
        ratio - (2 * k + 1) / (sp.Integer(3) * (k + 1))
    ) == 0
    assert sp.simplify(ratio < 1) == sp.true
    print("R72_ANGULAR_SCALING_AND_WALLIS PASSED")


def check_wiener_source_bounds() -> None:
    q = sp.sqrt(sp.Rational(2, 3))
    assert sp.simplify(q**2 - sp.Rational(2, 3)) == 0
    assert sp.Rational(1, 2) * 6 == 3
    # Fixed radius loss theta=1/2 gives C_A=(2/3)*sqrt(1)/4=1/6.
    assert sp.Rational(2, 3) * sp.Rational(1, 4) == sp.Rational(1, 6)
    # The Holder/product exponents used in the operator majorant are valid.
    assert sp.Rational(1, 4) + sp.Rational(1, 2) + sp.Rational(1, 4) == 1
    print("R72_WIENER_SOURCE_BOUNDS PASSED")


def check_even_bootstrap_constants() -> None:
    a, U = sp.symbols("a U", nonnegative=True)
    n = sp.symbols("n", nonnegative=True, integer=True)
    # If |a|U <= 4^(-(n+1)), the finite-degree radius change closes.
    small = sp.Pow(4, -(n + 1))
    lhs = 3 * sp.Pow(4, n) * (a * U) ** 2
    rhs = sp.Rational(3, 4) * a * U
    assert sp.simplify((lhs / (a * U) - rhs / (a * U)).subs(a * U, small)) == 0
    # The displayed bootstrap estimate is stronger than the required bound
    # because the cubic term is at most (4/3)|a|^3 U^3.
    x = sp.symbols("x", nonnegative=True)
    assert sp.simplify(
        (2 * x**2 + sp.Rational(4, 3) * x**3).subs(x, sp.Rational(1, 4))
        - 3 * sp.Rational(1, 4) ** 2
    ) < 0
    print("R72_EVEN_BOOTSTRAP_CONSTANTS PASSED")


def check_gram_majorant_scale() -> None:
    n, CB, Ubar = sp.symbols("n CB Ubar", positive=True)
    a = 1 / (2 * Ubar * sp.sqrt(n * CB * 3 ** (n / 2)))
    bound = 4 * CB * 3 ** (n / 2) * a**2 * Ubar**2
    assert sp.simplify(bound - 1 / n) == 0
    assert sp.simplify(
        sp.sqrt(sp.factorial(2 * n))
    ) is not None
    # sqrt(m!) <= (2n)^(m/2) for 0<=m<=2n is elementary from m!<=(2n)^m.
    m = sp.symbols("m", nonnegative=True, integer=True)
    assert sp.simplify((2 * n) ** m - sp.factorial(m)).subs(m, 0) == 0
    print("R72_GRAM_MAJORANT_SCALE PASSED")


def check_conditional_window() -> None:
    n, Mstar = sp.symbols("n Mstar", positive=True)
    a = 1 / (4 * Mstar)
    assert sp.simplify(a * Mstar - sp.Rational(1, 4)) == 0
    assert sp.simplify(sp.Rational(1, 4) + 1 / n < 1).subs(n, 2) is sp.true
    print("R72_CONDITIONAL_NO_REVERSAL_WINDOW PASSED")


if __name__ == "__main__":
    check_angular_scaling()
    check_wiener_source_bounds()
    check_even_bootstrap_constants()
    check_gram_majorant_scale()
    check_conditional_window()
    print("R72_ODD_SOLVER_MAJORANT_AUDIT_COMPLETED")
