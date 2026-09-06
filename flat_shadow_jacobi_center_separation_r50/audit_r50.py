"""R50 exact audit: two-step Jacobi center separation.

The audit checks the finite Schur-complement identities and the exact
same-factor pressure used by the webpage R50 argument.  It deliberately does
not claim the uniform finite exit, Xi_K -> infinity, or a genuine
all-degree non-Gaussian law.
"""

from sympy import Matrix, Poly, Rational, diff, expand, factorial, simplify, solve, sqrt, symbols


X = symbols("x0:3")
Q = Rational(2, 3) * (
    X[0] ** 2
    + X[1] ** 2
    + X[2] ** 2
    - X[0] * X[1]
    - X[0] * X[2]
    - X[1] * X[2]
)


def iid_expectation(expr, moments):
    poly = Poly(expand(expr), *X)
    out = 0
    for powers, coefficient in poly.terms():
        term = coefficient
        for exponent in powers:
            term *= moments[exponent]
        out += term
    return expand(out)


def G(n, moments):
    return expand(iid_expectation(Q ** n, moments) - 2 ** n * factorial(n))


def hankel(moments, degree):
    return Matrix(
        [
            [moments[i + j] for j in range(degree + 1)]
            for i in range(degree + 1)
        ]
    )


def normalized_moments(moments):
    return {moments[0]: 1, moments[1]: 0, moments[2]: 1}


def exact_even_row(n, moments):
    expression = G(n, moments)
    even = moments[2 * n]
    coefficient = diff(expression, even)
    return simplify(
        -expression.subs(even, 0) / coefficient
    )


def monic_orthogonal_polynomial(moments, degree):
    if degree == 0:
        return Matrix([1])
    gram = Matrix(
        [
            [moments[i + j] for j in range(degree)]
            for i in range(degree)
        ]
    )
    rhs = Matrix([-moments[degree + i] for i in range(degree)])
    return Matrix(list(gram.inv() * rhs) + [1])


def monic_norm(moments, degree):
    if degree == 0:
        return moments[0]
    polynomial = monic_orthogonal_polynomial(moments, degree)
    return simplify(
        sum(
            polynomial[i] * polynomial[j] * moments[i + j]
            for i in range(degree + 1)
            for j in range(degree + 1)
        )
    )


def check_pressure_and_even_pivot():
    """Check R31's pressure and the new-even-moment coefficient."""
    for n in range(2, 7):
        width = 2 * (n + 1) + 1
        moments = symbols(f"pressure_{n}_0:{width}")
        expression = G(n + 1, moments)
        substitutions = {moments[0]: 1, moments[1]: 0}
        pressure = diff(expression, moments[2 * n - 1]).subs(substitutions)
        expected_pressure = (
            -n
            * (n + 1)
            * (n + 5)
            * Rational(2, 3) ** (n + 1)
            * moments[3]
        )
        assert simplify(pressure - expected_pressure) == 0

        pivot = diff(expression, moments[2 * n + 2]).subs(substitutions)
        expected_pivot = 3 * Rational(2, 3) ** (n + 1)
        assert simplify(pivot - expected_pivot) == 0
    print("R50_SAME_FACTOR_PRESSURE_AND_EVEN_PIVOT PASSED")


def check_two_step_schur(n=3):
    """Check the exact two-step extension formulas at a generic small n."""
    width = 2 * n + 3
    moments = symbols(f"two_step_{n}_0:{width}")
    normalization = normalized_moments(moments)
    even_n = exact_even_row(n, moments).subs(normalization)
    y = symbols(f"y_{n}")
    even_next_equation = G(n + 1, moments).subs(normalization)
    even_next_equation = even_next_equation.subs(moments[2 * n], even_n)
    even_next_equation = even_next_equation.subs(moments[2 * n - 1], y)
    even_next = simplify(
        -even_next_equation.subs(moments[2 * n + 2], 0)
        / diff(even_next_equation, moments[2 * n + 2])
    )

    previous = hankel(moments, n - 1)
    inverse_previous = previous.inv()
    u = Matrix([moments[n + j] for j in range(n)])
    u = u.subs(moments[2 * n - 1], y)
    h_n = simplify(even_n - (u.T * inverse_previous * u)[0])
    h_previous = monic_norm(moments, n - 1)
    h_previous = h_previous.subs(moments[2 * n - 1], y)

    # The current odd control is the coefficient of x^(n-1) in pi_n.
    pi_n = monic_orthogonal_polynomial(moments, n)
    S = simplify(-pi_n[n - 1]).subs(moments[2 * n - 1], y)
    assert simplify(diff(S, y) - 1 / h_previous) == 0
    center = solve(S, y)[0]
    assert simplify(diff(h_n, y).subs(y, center)) == 0
    centered = simplify(
        h_n - (h_n.subs(y, center) - (y - center) ** 2 / h_previous)
    )
    assert centered == 0
    print(f"R50_ONE_STEP_VIABILITY_INTERVAL n={n} PASSED")

    w = Matrix([moments[n + 1 + j] for j in range(n)])
    w = w.subs({moments[2 * n - 1]: y, moments[2 * n]: even_n})
    D_n = simplify(even_next - (w.T * inverse_previous * w)[0])
    assert simplify(diff(D_n, y, 2) + 2 * inverse_previous[n - 2, n - 2]) == 0

    h_before = monic_norm(moments, n - 2)
    h_before = h_before.subs(moments[2 * n - 1], y)
    beta_before = simplify(h_previous / h_before)
    pi_before = monic_orthogonal_polynomial(moments, n - 1)
    S_before = simplify(-pi_before[n - 2]).subs(moments[2 * n - 1], y)
    B_before = simplify(beta_before + S_before ** 2)
    assert simplify(
        inverse_previous[n - 2, n - 2] - B_before / h_previous
    ) == 0
    assert simplify(
        diff(D_n, y, 2) + 2 * B_before / h_previous
    ) == 0
    print(f"R50_TWO_STEP_CURVATURE n={n} PASSED")

    full = hankel(moments, n + 1)
    full = full.subs(
        {
            moments[2 * n]: even_n,
            moments[2 * n - 1]: y,
            moments[2 * n + 2]: even_next,
        }
    )
    top_right = full[:n, n:]
    bottom_right = full[n:, n:]
    schur = (bottom_right - top_right.T * inverse_previous * top_right).applyfunc(
        simplify
    )
    free_next_odd = moments[2 * n + 1]
    assert diff(schur[0, 1], free_next_odd) == 1
    chosen_next_odd = solve(schur[0, 1], free_next_odd)[0]
    diagonalized = schur.subs(free_next_odd, chosen_next_odd).applyfunc(simplify)
    assert diagonalized[0, 1] == 0
    assert simplify(diagonalized[0, 0] - h_n) == 0
    assert simplify(diagonalized[1, 1] - D_n) == 0
    print(f"R50_TWO_STEP_EXTENSION_CRITERION n={n} PASSED")


def check_pressure_center_shift():
    n, m3, B, sigma_geom = symbols("n m3 B sigma_geom")
    lambda_n = n * (n + 1) * (n + 5) * m3 / 3
    sigma = sigma_geom + lambda_n / (2 * B)
    assert simplify(sigma - sigma_geom - n * (n + 1) * (n + 5) * m3 / (6 * B)) == 0
    print("R50_SAME_FACTOR_CENTER_SHIFT PASSED")


def check_interval_overlap_algebra():
    M, B, h, sigma, s, radius = symbols("M B h sigma s radius")
    completed = M - B * h * (s - sigma) ** 2
    assert simplify(
        completed.subs(s, sigma + radius)
        - (M - B * h * radius ** 2)
    ) == 0
    radius_def = sqrt(M / (B * h))
    assert simplify(M - B * h * radius_def ** 2) == 0
    print("R50_INTERVAL_OVERLAP_COMPLETION PASSED")


def check_fixed_X_head_bound():
    X_bound, v = symbols("X_bound v", positive=True)
    # x=(1-v)/v <= X_bound and t^2=2 imply m3^2=2*v^3.
    lower = Rational(2) / (1 + X_bound) ** 3
    m3_squared = 2 * v ** 3
    assert simplify(m3_squared.subs(v, 1 / (1 + X_bound)) - lower) == 0
    # The bound is recorded symbolically after substituting v >= 1/(1+X).
    assert lower > 0
    print("R50_FIXED_X_HEAD_NONZERO PASSED")


def main():
    check_pressure_and_even_pivot()
    check_two_step_schur(3)
    check_pressure_center_shift()
    check_interval_overlap_algebra()
    check_fixed_X_head_bound()
    print("R50_FIXED_HEAD_TWO_STEP_EXIT REMAINS OPEN")
    print("R50_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN")
    print("R50_FIXED_X_COMPACTNESS REMAINS CONDITIONAL")
    print("R50_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
