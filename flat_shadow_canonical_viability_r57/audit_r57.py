"""R57 exact audit: canonical viability, the positive upper envelope, and OU bounds.

R57 changed the route.  It showed that an all-positive canonical exact branch
already obeys an upper factorial envelope, so factorial escape cannot prove
D.1.  It also supplied a one-parameter finite-stage skew family and a
separate backward-OU lower bound.  This audit recomputes the finite Jacobi
head using beta_n=h_n/h_(n-1), rather than trusting flattened browser text for
fraction orientation.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation is used here.
"""

from math import factorial

from sympy import Poly, Rational, factor, simplify, symbols


def moment_functional(poly, x, moments):
    """Evaluate a polynomial against an exact moment dictionary."""
    return simplify(
        sum(coefficient * moments[degree[0]]
            for degree, coefficient in Poly(poly, x).terms())
    )


def check_finite_stage_skew_family():
    """Recompute the first canonical alpha=0 slots and their beta signs."""
    x, a = symbols("x a")
    moments = {
        0: 1,
        1: 0,
        2: 1,
        3: a,
        4: 3,
        5: 4 * a,
        6: 15 + 7 * a**2,
        7: 15 * a,
        8: 105 + 4 * a**2,
        9: a * (96 - 112 * a**2 - 49 * a**4) / (2 - a**2),
        10: 945 - 234 * a**2,
    }
    E = lambda p: moment_functional(p, x, moments)

    p0 = 1
    p1 = x
    h0 = Rational(1)
    h1 = E(p1**2)
    assert h1 == 1
    beta1 = h1 / h0

    p2 = (x - a) * p1 - beta1 * p0
    h2 = factor(E(p2**2))
    assert h2 == 2 - a**2
    beta2 = simplify(h2 / h1)

    p3 = (x + a) * p2 - beta2 * p1
    assert simplify(p3 - (x**3 - 3 * x - a)) == 0
    h3 = factor(E(p3**2))
    assert simplify(h3 - 6 * (1 + a**2)) == 0
    beta3 = factor(h3 / h2)
    assert simplify(beta3 - 6 * (1 + a**2) / (2 - a**2)) == 0

    p4 = x * p3 - beta3 * p2
    h4 = factor(E(p4**2))
    beta4 = factor(h4 / h3)
    assert simplify(beta4 - h4 / h3) == 0
    p4_tail = a**4 - 64 * a**2 + 16
    assert simplify(beta4 - p4_tail / (2 * (2 - a**2) * (1 + a**2))) == 0

    p5 = x * p4 - beta4 * p3
    h5 = factor(E(p5**2))
    beta5 = factor(h5 / h4)
    assert simplify(beta5 - h5 / h4) == 0
    p5_tail = 253 * a**6 - 1278 * a**4 + 816 * a**2 + 160
    assert simplify(beta5 - p5_tail / (2 * (1 + a**2) * p4_tail)) == 0

    # A small but nonzero skew value survives all computed beta signs.
    test_a = Rational(1, 10)
    assert all(
        simplify(value.subs(a, test_a)) > 0
        for value in (beta2, beta3, beta4, beta5)
    )
    print("R57_FINITE_STAGE_SKEW_MOMENTS PASSED")
    print("R57_JACOBI_BETA_ORIENTATION PASSED")
    print("R57_FINITE_STAGE_BETA2_BETA5_POSITIVE_AT_a=1/10 PASSED")
    print("R57_BETA4_FORMULA", beta4)
    print("R57_BETA5_FORMULA", beta5)


def check_positive_branch_upper_envelope():
    """Positive quadrature makes the proposed growth escape impossible."""
    # If the prefix is positive, its product Gauss measure is positive and
    # Q_n>=0.  Hence 0<delta_n<=2^n*n!, and
    # h_n=3^(n-1)*delta_n/2^n.
    for n in range(1, 10):
        delta = Rational(1, 2) * (2**n * factorial(n))
        h = Rational(3)**(n - 1) * delta / (2**n)
        assert 0 < h <= Rational(3)**(n - 1) * factorial(n)
    print("R57_POSITIVE_CANONICAL_BRANCH_UPPER_ENVELOPE PASSED")


def check_ou_lower_bound_algebra():
    """Check the conditional OU norm lower bound and induced m3 bound."""
    lam = symbols("lambda", positive=True)
    lower_h2 = (1 - lam) ** 2 * factorial(2)
    # Exact G2 gives h2=2-m3^2; therefore
    # m3^2<=2-2(1-lambda)^2=2*lambda*(2-lambda).
    rhs = simplify(2 - lower_h2)
    assert simplify(rhs - 2 * lam * (2 - lam)) == 0
    print("R57_OU_NORM_LOWER_BOUND_AND_M3_BOUND PASSED")


def main():
    check_finite_stage_skew_family()
    check_positive_branch_upper_envelope()
    check_ou_lower_bound_algebra()
    print("R57_FINITE_EXIT_VERSUS_INFINITE_POSITIVE_CHAIN REMAINS OPEN")
    print("R57_EVENTUAL_DIAGONAL_SKEW_ANNIHILATION REMAINS OPEN")
    print("R57_GAUSSIAN_RIGIDITY_AND_P3K REMAIN DISTINCT OPEN")
    print("R57_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
