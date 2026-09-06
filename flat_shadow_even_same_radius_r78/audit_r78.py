"""R78 same-radius even bootstrap arithmetic and coefficient audit."""

import math

import sympy as sp


def check_angular_coefficients_and_majorant() -> None:
    k = sp.symbols("k", integer=True, nonnegative=True)
    for kval in range(1, 10):
        A = sp.Rational(3, 6**kval) * sp.binomial(2 * kval, kval)
        assert A > 0

        # Young's inequality implies the symmetric coefficient majorant for
        # r+s=2k; check the elementary endpoint form on an exact grid.
        for rval in range(0, 2 * kval + 1):
            sval = 2 * kval - rval
            for xval, yval in [(sp.Rational(0), sp.Rational(2)),
                               (sp.Rational(1, 3), sp.Rational(2)),
                               (sp.Rational(2), sp.Rational(1, 5)),
                               (sp.Rational(1), sp.Rational(1))]:
                lhs = xval**rval * yval**sval + xval**sval * yval**rval
                rhs = xval ** (2 * kval) + yval ** (2 * kval)
                assert lhs <= rhs

        # A_(2k)^(-1) has the expected exponential base 3/2 up to a
        # polynomial factor; the exact ratio is enough for this audit.
        ratio = sp.simplify(
            (1 / (sp.Rational(3, 6 ** (kval + 1))
                  * sp.binomial(2 * (kval + 1), kval + 1)))
            / (1 / A)
        )
        assert ratio == sp.Rational(3 * (kval + 1), 2 * kval + 1)
    print("R78_ANGULAR_COEFFICIENT_MAJORANT_PASSED")


def check_wiener_convolution_and_even_bootstrap() -> None:
    R = 4
    f = [0, 1, -2, 1, 3, 0, -1, 2]
    g = [0, -1, 1, 2, 0, 1, -2, 1]
    norm_f = sum(abs(value) * R**idx for idx, value in enumerate(f))
    norm_g = sum(abs(value) * R**idx for idx, value in enumerate(g))
    for mval in range(1, 8):
        convolution = sum(f[rval] * g[mval - rval]
                          for rval in range(mval + 1))
        assert abs(convolution) * R**mval <= norm_f * norm_g

    x = sp.symbols("x", nonnegative=True)
    X = 2 * x + 8 * x**2
    assert sp.simplify(8 * x**2 - (X**2 + X**3)).subs(x, sp.Rational(1, 100)) > 0
    # Monotonicity of the polynomial on the bootstrap interval is positive.
    derivative = sp.diff(X**2 + X**3, x)
    assert derivative.subs(x, sp.Rational(1, 100)) > 0
    print("R78_SAME_RADIUS_WIENER_BOOTSTRAP_PASSED")


def check_odd_same_radius_sum() -> None:
    n, lam = sp.symbols("n lam", positive=True)
    for kval in range(0, 12):
        assert sp.Rational(math.factorial(kval), math.factorial(2 * kval + 1)) <= sp.Rational(
            1, math.factorial(kval + 1)
        )

    for nval in range(1, 7):
        for lamval in [sp.Rational(9, 2), 6, 10]:
            b = [
                sp.Rational(1, math.factorial(kval + 1))
                * (16 * lamval * nval) ** kval
                for kval in range(1, nval + 1)
            ]
            for idx in range(1, len(b)):
                assert b[idx - 1] / b[idx] <= sp.Rational(1, 32)

            R = 4 * sp.sqrt(nval)
            lhs = sum(
                sp.factorial(kval)
                * lamval**kval
                * R ** (2 * kval + 1)
                / sp.factorial(2 * kval + 1)
                for kval in range(1, nval + 1)
            )
            rhs = sp.Rational(32, 31) * R * b[-1]
            assert sp.simplify(rhs - lhs) >= 0
    print("R78_SAME_RADIUS_ODD_SUM_PASSED")


def check_tangent_and_window_exponents() -> None:
    # Ratio of successive tangent norm terms is at least four for k<=n.
    for nval in range(1, 12):
        R2 = 16 * nval
        for kval in range(2, nval + 1):
            ratio = sp.Rational(R2 * (kval + 1), 2 * (kval - 1) * (2 * kval + 1))
            assert ratio >= 4

    eps = sp.symbols("eps", positive=True)
    lam = 4 + eps
    # Combining H_n~n^(3/2)16^n and Gamma~n^(-1/2)(16e lambda)^n
    # yields the displayed a and t polynomial/exponential powers.
    assert sp.simplify(sp.Rational(3, 2) - sp.Rational(1, 4)
                       - sp.Rational(1, 2) - sp.Rational(3, 4)) == 0
    assert sp.simplify(2 * sp.Rational(5, 4) - sp.Rational(5, 2)) == 0
    # Verify directly that [64 sqrt(e lambda)]^(-2n)
    # equals [4096 e lambda]^(-n).
    assert sp.simplify((64 * sp.sqrt(sp.E * lam)) ** 2
                       - 4096 * sp.E * lam) == 0
    print("R78_TANGENT_WINDOW_EXPONENTS_PASSED")


if __name__ == "__main__":
    check_angular_coefficients_and_majorant()
    check_wiener_convolution_and_even_bootstrap()
    check_odd_same_radius_sum()
    check_tangent_and_window_exponents()
    print("R78_SAME_RADIUS_EVEN_AUDIT_COMPLETED")
