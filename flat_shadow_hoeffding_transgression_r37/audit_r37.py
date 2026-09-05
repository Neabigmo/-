"""R37 exact audit: two-body Laguerre--Hoeffding Gaussian anchor.

The browser-side R36 result identified the two-body projection as the next
open direction.  This local audit derives its Gaussian conditional generating
function and checks the resulting exact anchor norm.  It intentionally does
not claim the fixed-head derivative or a full transgression: those remain the
web-side R37 target.
"""

from sympy import Poly, Rational, binomial, factorial, simplify, sqrt, symbols


def laguerre(n, x, alpha=0):
    return sum(
        (-1) ** k
        * binomial(n + alpha, n - k)
        * x**k
        / factorial(k)
        for k in range(n + 1)
    )


def hermite_prob(n, x):
    return sum(
        (-1) ** k
        * factorial(n)
        * x ** (n - 2 * k)
        / (2**k * factorial(k) * factorial(n - 2 * k))
        for k in range(n // 2 + 1)
    )


def h_norm(n, x):
    return hermite_prob(n, x) / sqrt(factorial(n))


def gaussian_moment(power):
    if power % 2:
        return 0
    return factorial(power) / (2 ** (power // 2) * factorial(power // 2))


def gaussian_expectation(poly, variables):
    out = 0
    for powers, coeff in Poly(poly.expand(), *variables).terms():
        term = coeff
        for power in powers:
            term *= gaussian_moment(power)
        out += term
    return simplify(out)


def marginal_gaussian(poly, integrated, all_variables):
    """Integrate selected independent standard Gaussian variables exactly."""
    remaining = [v for v in all_variables if v not in integrated]
    out = 0
    for powers, coeff in Poly(poly.expand(), *all_variables).terms():
        term = coeff
        for variable, power in zip(all_variables, powers):
            if variable in integrated:
                term *= gaussian_moment(power)
            else:
                term *= variable**power
        out += term
    # `remaining` is only used to keep the intent explicit; SymPy simplifies
    # the returned polynomial independently of its generator list.
    _ = remaining
    return simplify(out)


def phi(n, x1, x2, x3):
    mean = (x1 + x2 + x3) / 3
    t = sum((x - mean) ** 2 for x in (x1, x2, x3)) / 2
    return laguerre(n, t)


def c(n):
    return sqrt(factorial(2 * n)) / (2**n * factorial(n))


def one_body_kappa(n):
    return (-1) ** n * c(n) * Rational(2, 3) ** n


def two_body_projection_formula(n, x1, x2):
    s = (x1 + x2) / sqrt(2)
    d = (x1 - x2) / sqrt(2)
    return simplify(
        sum(
            Rational(1, 3) ** b
            * (-1) ** (n - b)
            * c(n - b)
            * h_norm(2 * (n - b), d)
            * (-1) ** b
            * c(b)
            * h_norm(2 * b, s)
            for b in range(n + 1)
        )
    )


def check_conditional_projection_and_one_body():
    x1, x2, x3 = symbols("x1 x2 x3")
    for n in range(0, 5):
        p_direct = marginal_gaussian(phi(n, x1, x2, x3), [x3], [x1, x2, x3])
        p_formula = two_body_projection_formula(n, x1, x2)
        assert simplify(p_direct - p_formula) == 0

        if n >= 1:
            k_direct = marginal_gaussian(phi(n, x1, x2, x3), [x2, x3], [x1, x2, x3])
            k_formula = one_body_kappa(n) * h_norm(2 * n, x1)
            assert simplify(k_direct - k_formula) == 0


def check_two_body_anchor_norm():
    x1, x2, x3 = symbols("x1 x2 x3")
    for n in range(1, 5):
        p = two_body_projection_formula(n, x1, x2)
        p_norm = gaussian_expectation(p**2, (x1, x2))
        weights = [binomial(2 * j, j) / 4**j for j in range(n + 1)]
        convolution = simplify(
            sum(Rational(1, 9) ** b * weights[n - b] * weights[b] for b in range(n + 1))
        )
        assert simplify(p_norm - convolution) == 0

        k = one_body_kappa(n) * h_norm(2 * n, x1)
        k_norm = gaussian_expectation(k**2, (x1,))
        expected_k_norm = simplify(binomial(2 * n, n) / 9**n)
        assert simplify(k_norm - expected_k_norm) == 0

        # The degenerate pair sector is the orthogonal remainder after both
        # one-body projections.  Symmetry gives ||h2||^2=||p||^2-2||k||^2.
        b_norm = simplify(p_norm - 2 * k_norm)
        assert b_norm == simplify(convolution - 2 * expected_k_norm)
        assert b_norm > 0


def check_anchor_generating_function():
    z = symbols("z")
    # w_j=binom(2j,j)/4^j has generating function (1-z)^(-1/2).
    # Therefore the pair-projection norm has exact generating function
    # (1-z)^(-1/2)(1-z/9)^(-1/2).
    # This coefficient identity is checked through degree four exactly.
    left = (1 - z) ** Rational(-1, 2) * (1 - z / 9) ** Rational(-1, 2)
    for n in range(5):
        coefficient = left.series(z, 0, n + 1).removeO().expand().coeff(z, n)
        weights = [binomial(2 * j, j) / 4**j for j in range(n + 1)]
        convolution = simplify(
            sum(Rational(1, 9) ** b * weights[n - b] * weights[b] for b in range(n + 1))
        )
        assert simplify(coefficient - convolution) == 0


def check_two_body_head_sensitivity_preview():
    """Compute the full first-variation decomposition for small exact cases.

    This is deliberately a preview: it checks all measure/projection terms but
    does not infer the n->infinity theorem from a finite table.  The webpage
    review is still required for the asymptotic conclusion.
    """
    x1, x2, x3, x4 = symbols("x1 x2 x3 x4")
    for N in (2, 4):
        values = []
        for n in range(1, 5):
            p = two_body_projection_formula(n, x1, x2)
            k = one_body_kappa(n) * h_norm(2 * n, x1)
            f123 = phi(n, x1, x2, x3)
            f124 = phi(n, x1, x2, x4)
            hN1 = h_norm(N, x1)
            hN2 = h_norm(N, x2)
            hN3 = h_norm(N, x3)

            # P=||p||^2 has two shared and two leaf measure derivatives.
            s2 = gaussian_expectation(hN1 * p**2, (x1, x2))
            l2 = gaussian_expectation(hN3 * f123 * f124, (x1, x2, x3, x4))
            # K=||k||^2 has one shared and four leaf derivatives; p/k
            # already include the derivative of the conditional projections.
            s1 = gaussian_expectation(hN1 * k**2, (x1,))
            l1 = gaussian_expectation(hN2 * p * k, (x1, x2))
            derivative = simplify(2 * (s2 + l2) - 2 * (s1 + 4 * l1))
            values.append(derivative)
        print(f"R37_LOCAL_HEAD_PREVIEW_N{N}: {values}")


def main():
    check_conditional_projection_and_one_body()
    print("R37_TWO_BODY_CONDITIONAL_PROJECTION PASSED")
    check_two_body_anchor_norm()
    print("R37_TWO_BODY_DEGENERATE_NORM PASSED")
    check_anchor_generating_function()
    print("R37_TWO_BODY_ANCHOR_POLYNOMIAL_DECAY PASSED")
    check_two_body_head_sensitivity_preview()
    print("R37_TWO_BODY_HEAD_SENSITIVITY_LOCAL_PREVIEW RECORDED")
    print("R37_TWO_BODY_HEAD_SENSITIVITY REQUIRES WEB_REVIEW")
    print("R37_CONSTRAINT_COUPLED_TRANSGRESSION REMAINS OPEN")
    print("R37_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
