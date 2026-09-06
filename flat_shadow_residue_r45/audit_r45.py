"""R45 exact finite audit for the lowest N+6 resonance.

The checks are deliberately finite and symbolic.  They validate the new
degree-six Fock relation and the m=3,n=3 response regression supplied by the
web review.  No asymptotic rank or transgression claim is made here.
"""

import itertools
import sys
from functools import lru_cache
from pathlib import Path

from sympy import (
    Rational,
    cos,
    factorial,
    integrate,
    pi,
    simplify,
    sqrt,
    symbols,
)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flat_shadow_hoeffding_transgression_r37.audit_r37 import (  # noqa: E402
    gaussian_expectation,
    h_norm,
    marginal_gaussian,
    phi,
)
from flat_shadow_mixed_hessian_r40.audit_r40 import (  # noqa: E402
    mixed_hessian,
)


def check_degree_six_fock_relation():
    """Check the exact angular coefficients behind the genuine-law relation."""
    theta = symbols("theta", real=True)
    a600 = Rational(2, 3) ** 3 * integrate(
        cos(theta) ** 6, (theta, 0, 2 * pi)
    ) / (2 * pi)
    a330 = Rational(2, 3) ** 3 * integrate(
        cos(theta) ** 3 * cos(theta - 2 * pi / 3) ** 3,
        (theta, 0, 2 * pi),
    ) / (2 * pi)
    assert simplify(a600 - Rational(5, 54)) == 0
    assert simplify(a330 + Rational(7, 216)) == 0

    relation = simplify(
        -sqrt(factorial(6) / factorial(3) ** 2) * a330 / a600
    )
    assert simplify(relation - Rational(7, 10) * sqrt(5)) == 0


def factor(q, variable):
    return 1 if q == 0 else h_norm(q, variable)


def half_third_coefficient_k4(n):
    """Coefficient of eps*delta**2 for K4, i.e. half the labelled D3."""
    x1, x2, x3, x4 = symbols("x1 x2 x3 x4")
    xs = (x1, x2, x3, x4)
    total = 0
    for i in range(4):
        for j, k in itertools.combinations(
            [u for u in range(4) if u != i], 2
        ):
            qs = [0] * 4
            qs[i] = 6
            qs[j] = qs[k] = 3
            left = phi(n, x1, x2, x3) * factor(qs[2], x3)
            right = phi(n, x1, x2, x4) * factor(qs[3], x4)
            shared = factor(qs[0], x1) * factor(qs[1], x2)
            left = marginal_gaussian(left, [x3], [x1, x2, x3])
            right = marginal_gaussian(right, [x4], [x1, x2, x4])
            total += gaussian_expectation(left * right * shared, (x1, x2))
    return simplify(total)


def half_third_coefficient_k5(n):
    """Coefficient of eps*delta**2 for K5, i.e. half the labelled D3."""
    x1, x2, x3, x4, x5 = symbols("x1 x2 x3 x4 x5")
    total = 0
    for i in range(5):
        for j, k in itertools.combinations(
            [u for u in range(5) if u != i], 2
        ):
            qs = [0] * 5
            qs[i] = 6
            qs[j] = qs[k] = 3
            left = phi(n, x1, x2, x3) * factor(qs[1], x2) * factor(qs[2], x3)
            right = phi(n, x1, x4, x5) * factor(qs[3], x4) * factor(qs[4], x5)
            left = marginal_gaussian(left, [x2, x3], [x1, x2, x3])
            right = marginal_gaussian(right, [x4, x5], [x1, x4, x5])
            total += gaussian_expectation(
                left * right * factor(qs[0], x1), (x1,)
            )
    return simplify(total)


def half_third_coefficient_k6(n):
    """Coefficient of eps*delta**2 for K6 via two independent blocks."""
    xs = symbols("x1 x2 x3 x4 x5 x6")
    blocks = ((0, 1, 2), (3, 4, 5))

    @lru_cache(None)
    def block_expectation(block_id, qtuple):
        indices = blocks[block_id]
        variables = tuple(xs[index] for index in indices)
        expression = phi(n, *variables)
        for index, q in zip(indices, qtuple):
            expression *= factor(q, xs[index])
        return simplify(gaussian_expectation(expression, variables))

    total = 0
    for i in range(6):
        for j, k in itertools.combinations(
            [u for u in range(6) if u != i], 2
        ):
            term = 1
            for block_id, indices in enumerate(blocks):
                qtuple = []
                for index in indices:
                    if index == i:
                        qtuple.append(6)
                    elif index in (j, k):
                        qtuple.append(3)
                    else:
                        qtuple.append(0)
                term *= block_expectation(block_id, tuple(qtuple))
            total += term
    return simplify(total)


def check_full_law_third_variation():
    """Check the complete four/five/six-copy law-functional coefficient."""
    n = 3
    k4 = half_third_coefficient_k4(n)
    k5 = half_third_coefficient_k5(n)
    k6 = half_third_coefficient_k6(n)
    assert k4 == 376 * sqrt(5) / 729
    assert k5 == 196 * sqrt(5) / 729
    assert k6 == -28 * sqrt(5) / 81
    half_d3 = simplify(k4 - 2 * k5 + k6)
    assert half_d3 == -268 * sqrt(5) / 729
    return k4, k5, k6, half_d3


def check_m3_hessian_regressions():
    h93 = mixed_hessian(3, 9, 3)
    h75 = mixed_hessian(3, 7, 5)
    h66 = mixed_hessian(3, 6, 6)
    assert h93 == -32 * sqrt(105) / 81
    assert h75 == -800 * sqrt(42) / 729
    assert h66 == Rational(5560, 729)
    return h93, h75, h66


def main():
    check_degree_six_fock_relation()
    print("R45_DEGREE6_FOCK_RELATION PASSED")

    k4, k5, k6, half_d3 = check_full_law_third_variation()
    print(f"R45_THIRD_COEFFICIENTS K4={k4} K5={k5} K6={k6}")
    print(f"R45_HALF_D3={half_d3}")
    print("R45_FULL_LAW_THIRD_VARIATION PASSED")

    h93, h75, h66 = check_m3_hessian_regressions()
    print(f"R45_M3_HESSIANS H93={h93} H75={h75} H66={h66}")
    print("R45_M3_HESSIAN_REGRESSIONS PASSED")

    effective = simplify(7 * sqrt(5) * h66 / 10 + half_d3)
    assert effective == 1208 * sqrt(5) / 243
    print(f"R45_EFFECTIVE_J33={effective}")
    print("R45_N6_RESONANCE_COMBINATION PASSED")
    print("R45_NPLUS6_QUOTIENT_RANK REMAINS OPEN")
    print("R45_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
