"""Exact symbolic audit for the R103 Herglotz/same-factor advances."""

from __future__ import annotations

import sympy as sp


u, z, eps = sp.symbols("u z eps", nonzero=True)
rho = sp.sqrt(sp.Rational(2, 3))
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2


def direction(j: int) -> sp.Expr:
    phase = omega**j
    return sp.expand(rho * (phase * u + sp.conjugate(phase) / u) / 2)


def p(m: int) -> sp.Expr:
    return sp.expand(sum(direction(j) ** m for j in range(3)))


def average(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand(expr).coeff(u, 0))


def lam(m: int, r: int) -> sp.Expr:
    k = (m - 3 * r) // 2
    if k < 0 or m - 3 * r < 0 or (m - 3 * r) % 2:
        return sp.Integer(0)
    return sp.simplify(3 * (rho / 2) ** m * sp.binomial(m, k))


def admissible(m: int) -> tuple[int, ...]:
    return tuple(r for r in range(1, m // 3 + 1, 2) if (m - 3 * r) % 2 == 0)


def check_predictor_algebra() -> None:
    c1, c2 = sp.symbols("c1 c2", real=True)
    b = c2 - c1**2
    # Fourier expansion of |1-c1*e^(3it)-b*e^(6it)|^2 against c_r.
    rhs = 1 + c1**2 + b**2 - 2 * c1**2 - 2 * b * c2 + 2 * c1 * b * c1
    assert sp.expand(rhs - (1 - c1**2 - b**2)) == 0
    # The Jensen step is a scalar exact identity once the predictor is chosen.
    assert sp.expand((1 - c1**2 - b**2) - (1 - c1**2 - (c2 - c1**2) ** 2)) == 0
    print("R103_PREDICTOR_ALGEBRA_PASSED")


def check_first_odd_energy() -> None:
    for d in (3, 5, 7, 9, 11):
        rs = admissible(d)
        assert rs == tuple(range(1, (d // 3) + 1, 2))
        assert sp.simplify(average(p(d) ** 2) -
                           2 * sum(lam(d, r) ** 2 for r in rs)) == 0
        A2d = average(p(2 * d))
        assert A2d.is_positive is True
        kd = sp.symbols(f"kappa{d}")
        k2d = -sp.factorial(2 * d) / (2 * sp.factorial(d) ** 2)
        k2d *= average(p(d) ** 2) / A2d * kd**2
        lhs = sp.simplify(-k2d * A2d / sp.factorial(2 * d))
        rhs = sp.simplify(sum((kd * lam(d, r) / sp.factorial(d)) ** 2
                              for r in rs))
        assert sp.expand(lhs - rhs) == 0
    print("R103_FIRST_ODD_ALL_CHARGE_ENERGY_PASSED")


def check_higher_charge_tax() -> None:
    values = {}
    for d in (3, 5, 7, 9, 11):
        rs = admissible(d)
        T = sp.simplify(sum(lam(d, r) ** 2 for r in rs) / lam(d, 1) ** 2)
        values[d] = T
    assert values[3] == values[5] == values[7] == 1
    assert values[9] > 1 and values[11] > 1

    for d, expected in ((3, sp.Rational(1, 20)),
                        (5, sp.Rational(5, 28)),
                        (7, sp.Rational(7, 24))):
        A2d = average(p(2 * d))
        eta = sp.simplify(
            average(p(d) ** 2) * lam(2 * d, 2) /
            (2 * A2d * lam(d, 1) ** 2)
        )
        assert eta == expected
        assert eta == sp.binomial(2 * d, d - 3) / sp.binomial(2 * d, d)
    print("R103_HIGHER_CHARGE_TAX_AND_ETA_PASSED")


def check_explicit_probability_obstruction() -> None:
    # Gaussian transforms of sin(s*x), followed by the selected cancellation.
    H = sp.exp(-sp.Rational(1, 2)) * (sp.sin(z) - sp.sin(2 * z) / 2)
    assert sp.simplify(
        sp.series(H, z, 0, 7).removeO() - sp.exp(-sp.Rational(1, 2)) *
        (z**3 / 2 - z**5 / 8)
    ) == 0
    q = eps * sp.exp(-sp.Rational(1, 2)) / 2
    U, v = sp.symbols("U v", nonzero=True)
    log_w = sp.series(sp.log(1 + U * (v + v**-1)), U, 0, 3).removeO()
    R = sp.simplify(sp.expand(log_w).coeff(v, 0))
    Q2 = sp.simplify(sp.expand(log_w).coeff(v, 2))
    assert R == -U**2
    assert Q2 == -U**2 / 2
    assert sp.expand(sp.series(R.subs(U, eps * H), z, 0, 7).removeO() + q**2 * z**6) == 0
    assert sp.expand(sp.series(Q2.subs(U, eps * H), z, 0, 7).removeO() +
                     q**2 * z**6 / 2) == 0

    A6 = average(p(6))
    assert A6 == sp.Rational(5, 18)
    assert lam(6, 2) == sp.Rational(1, 72)
    assert sp.simplify(lam(6, 2) / A6) == sp.Rational(1, 20)
    # The explicit family has Q2/R = 1/2, so the fingerprint is incompatible.
    assert sp.Rational(1, 2) != sp.Rational(1, 20)
    print("R103_EXPLICIT_NONFACTORIZATION_OBSTRUCTION_PASSED")


def check_formal_same_factor_jet() -> None:
    k3 = sp.symbols("kappa3")
    K = k3 * z**3 * p(3) / sp.factorial(3)
    K += -3 * k3**2 * z**6 * p(6) / sp.factorial(6)
    expK = sp.expand(1 + K + K**2 / 2)
    assert sp.simplify(average(expK).coeff(z, 6)) == 0
    assert sp.simplify(average(expK).coeff(z, 3)) == 0
    print("R103_FORMAL_SAME_FACTOR_JET_THROUGH_DEGREE6_PASSED")


def main() -> None:
    check_predictor_algebra()
    check_first_odd_energy()
    check_higher_charge_tax()
    check_explicit_probability_obstruction()
    check_formal_same_factor_jet()
    print("R103_ASYMMETRIC_EXCLUSION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
