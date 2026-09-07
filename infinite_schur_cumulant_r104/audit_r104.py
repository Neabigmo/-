"""Exact symbolic audit for the R104 Schur--cumulant cascade.

The audit is deliberately finite-grade and symbolic.  It checks the algebraic
interfaces used by the webpage derivation without claiming that a formal
Schur cascade is itself a probability realization.
"""

from __future__ import annotations

import sympy as sp


u, z = sp.symbols("u z", nonzero=True)
rho = sp.sqrt(sp.Rational(2, 3))
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
omega_bar = -sp.Rational(1, 2) - sp.sqrt(3) * sp.I / 2
NMAX = 12


def direction(j: int) -> sp.Expr:
    return sp.expand(rho * (omega**j * u + omega_bar**j / u) / 2)


def p(m: int) -> sp.Expr:
    return sp.expand(sum(direction(j) ** m for j in range(3)))


def average(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand(expr).coeff(u, 0))


def fourier(expr: sp.Expr, charge: int) -> sp.Expr:
    """Coefficient of exp(i*3*charge*theta), i.e. c_charge."""
    return sp.simplify(sp.expand(expr).coeff(u, 3 * charge))


def lam(m: int, r: int) -> sp.Expr:
    gap = m - 3 * r
    if gap < 0 or gap % 2:
        return sp.Integer(0)
    return sp.simplify(3 * (rho / 2) ** m * sp.binomial(m, gap // 2))


def truncate(expr: sp.Expr, order: int = NMAX) -> sp.Expr:
    expanded = sp.expand(expr)
    return sp.expand(sum(expanded.coeff(z, degree) * z**degree
                          for degree in range(order + 1)))


def exp_truncated(expr: sp.Expr, order: int = NMAX) -> sp.Expr:
    # Every term in mathscr K has degree at least three.
    return truncate(sum(expr**j / sp.factorial(j) for j in range(order // 3 + 1)), order)


def z_div_series(numerator: sp.Expr, denominator: sp.Expr,
                 order: int = NMAX) -> sp.Expr:
    """Divide two z-series while keeping Laurent polynomials in u explicit."""
    numerator = sp.expand(numerator)
    denominator = sp.expand(denominator)
    d0 = denominator.coeff(z, 0)
    assert d0 != 0
    quotient: dict[int, sp.Expr] = {}
    for degree in range(order + 1):
        remainder = numerator.coeff(z, degree)
        remainder -= sum(denominator.coeff(z, j) * quotient[degree - j]
                         for j in range(1, degree + 1))
        quotient[degree] = sp.expand(remainder / d0)
    return sp.expand(sum(value * z**degree for degree, value in quotient.items()))


def neg_log_one_minus_square(alpha: sp.Expr, order: int = NMAX) -> sp.Expr:
    """Return -log(1-alpha^2) as a finite z-adic series."""
    return truncate(sum(alpha**(2 * j) / j for j in range(1, order + 1)), order)


def check_d3_geometry_and_harmonics() -> None:
    for m in range(3, 15):
        for r in range(1, m // 3 + 1):
            direct = fourier(p(m), r)
            expected = lam(m, r)
            assert sp.simplify(direct - expected) == 0
        if m % 2 == 0:
            assert all(lam(m, r) == 0 for r in range(1, m // 3 + 1, 2))

    for n in range(1, 7):
        expected = 3 * sp.binomial(2 * n, n) / 6**n
        assert sp.simplify(average(p(2 * n)) - expected) == 0

    print("R104_D3_GEOMETRY_AND_HARMONIC_WEIGHTS_PASSED")


def solve_forced_even_cumulants() -> tuple[dict[int, sp.Expr], dict[int, sp.Symbol]]:
    odd = {3: sp.symbols("kappa3"), 5: sp.Integer(0), 7: sp.Integer(0),
           9: sp.Integer(0), 11: sp.Integer(0)}
    even_symbols = {2 * n: sp.symbols(f"kappa{2 * n}") for n in range(2, 7)}
    cumulants: dict[int, sp.Expr] = {**odd, **even_symbols}
    solved: dict[int, sp.Expr] = {}

    for degree in range(4, NMAX + 1, 2):
        substitutions = {even_symbols[m]: value for m, value in solved.items()}
        current = {m: value.subs(substitutions) if isinstance(value, sp.Expr) else value
                   for m, value in cumulants.items()}
        log_weight = sum(current[m] * z**m * p(m) / sp.factorial(m)
                         for m in range(3, NMAX + 1))
        exact_series = average(exp_truncated(log_weight))
        equation = sp.expand(exact_series).coeff(z, degree)
        solved[degree] = sp.factor(sp.solve(equation, even_symbols[degree])[0])

    return solved, even_symbols


def build_forced_branch(solved: dict[int, sp.Expr], even_symbols: dict[int, sp.Symbol]) -> sp.Expr:
    cumulants: dict[int, sp.Expr] = {
        3: sp.symbols("kappa3"), 5: sp.Integer(0), 7: sp.Integer(0),
        9: sp.Integer(0), 11: sp.Integer(0)
    }
    cumulants.update({m: solved[m] for m in even_symbols})
    return sp.expand(sum(cumulants[m] * z**m * p(m) / sp.factorial(m)
                         for m in range(3, NMAX + 1)))


def check_forced_even_and_szego_budget() -> None:
    solved, even_symbols = solve_forced_even_cumulants()
    k3 = sp.symbols("kappa3")
    assert solved[4] == 0
    assert sp.simplify(solved[6] + 3 * k3**2) == 0

    log_weight = build_forced_branch(solved, even_symbols)
    exact_series = average(exp_truncated(log_weight))
    assert sp.simplify(exact_series - 1) == 0

    c1 = fourier(exp_truncated(log_weight), 1)
    c2 = fourier(exp_truncated(log_weight), 2)
    alpha0 = truncate(c1)
    alpha1 = z_div_series(c2 - c1**2, 1 - c1**2)

    assert sp.simplify(alpha0 - c1) == 0
    assert sp.simplify(alpha1.subs(z, 0)) == 0
    assert sp.simplify(alpha1 - truncate(alpha1)) == 0

    def lowest_degree(expr: sp.Expr) -> int | None:
        poly = sp.Poly(sp.expand(expr), z)
        degrees = [monom[0] for monom, coeff in poly.terms() if coeff != 0]
        return min(degrees) if degrees else None

    assert lowest_degree(alpha0) == 3
    assert lowest_degree(alpha1) == 6

    # alpha_0 has odd z-parity and alpha_1 has even z-parity.
    for degree in range(0, NMAX + 1):
        assert sp.simplify(alpha0.coeff(z, degree)) == 0 if degree % 2 == 0 else True
        assert sp.simplify(alpha1.coeff(z, degree)) == 0 if degree % 2 == 1 else True

    R = average(log_weight)
    schur_budget = truncate(neg_log_one_minus_square(alpha0) +
                            neg_log_one_minus_square(alpha1))
    # alpha_2 starts at z^9, so alpha_2^2 starts beyond the audited grade.
    assert sp.simplify(truncate(schur_budget + R)) == 0

    for n in range(2, 7):
        A = 3 * sp.binomial(2 * n, n) / 6**n
        B = sp.expand(schur_budget).coeff(z, 2 * n)
        assert sp.simplify(solved[2 * n] / sp.factorial(2 * n) + B / A) == 0

    print("R104_FORCED_EVEN_RECURSION_AND_FINITE_SZEGO_BUDGET_PASSED")


def check_schur_first_steps_and_abel_multiplier() -> None:
    c1, c2 = sp.symbols("c1 c2", real=True)
    alpha0 = c1
    alpha1 = (c2 - c1**2) / (1 - c1**2)
    E1 = 1 - alpha0**2
    E2 = sp.factor(E1 * (1 - alpha1**2))
    expected = 1 - c1**2 - (c2 - c1**2)**2 / (1 - c1**2)
    assert sp.simplify(E2 - expected) == 0

    # A[r^(2n)] = binom(2n,n)/4^n * r^(2n), and r=rho*z.
    for n in range(1, 7):
        abel_multiplier = 3 * sp.binomial(2 * n, n) / 4**n * rho**(2 * n)
        radial_multiplier = 3 * sp.binomial(2 * n, n) / 6**n
        assert sp.simplify(abel_multiplier - radial_multiplier) == 0

    print("R104_SCHUR_FIRST_STEPS_AND_ABEL_MULTIPLIER_PASSED")


def check_ou_and_first_odd_vector() -> None:
    t = sp.symbols("t", positive=True)
    # The exact OU statement is argument substitution, so every audited
    # coefficient has grade m/2.
    k3 = sp.symbols("kappa3")
    for r in (1, 3):
        m = 3 if r == 1 else 9
        assert sp.simplify(lam(m, r) - fourier(p(m), r)) == 0
        lhs = lam(m, r) * k3 * (sp.sqrt(t) * z) ** m / sp.factorial(m)
        rhs = (t ** sp.Rational(m, 2)) * lam(m, r) * k3 * z**m / sp.factorial(m)
        assert sp.simplify(lhs - rhs) == 0

    for d in (3, 5, 7, 9, 11):
        admissible = tuple(r for r in range(1, d // 3 + 1, 2))
        assert all(lam(d, r) > 0 for r in admissible)
        assert all(lam(d, r) == 0 for r in range(1, d // 3 + 1) if r not in admissible)

    print("R104_OU_GRADE_AND_FIRST_ODD_SCHUR_VECTOR_PASSED")


def main() -> None:
    check_d3_geometry_and_harmonics()
    check_forced_even_and_szego_budget()
    check_schur_first_steps_and_abel_multiplier()
    check_ou_and_first_odd_vector()
    print("R104_INFINITE_SCHUR_CUMULANT_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
