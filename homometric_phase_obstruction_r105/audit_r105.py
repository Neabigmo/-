"""Finite exact audit for R105.

This file checks only finite symbolic identities.  The homometric pair is a
genuine probability obstruction to real-axis autocorrelation recovery, but it
is explicitly tested against the fourth-order full-exact condition so it is
not misreported as a counterexample to the project.
"""

from __future__ import annotations

import sympy as sp


r = sp.symbols("r", real=True)
K = sp.Function("K")


def mgf(values: tuple[sp.Rational, ...],
        probabilities: tuple[sp.Rational, ...],
        argument: sp.Expr) -> sp.Expr:
    return sp.expand(sum(p * sp.exp(argument * x)
                         for x, p in zip(values, probabilities)))


def moment(values: tuple[sp.Rational, ...],
           probabilities: tuple[sp.Rational, ...], order: int) -> sp.Expr:
    return sp.simplify(sum(p * x**order
                           for x, p in zip(values, probabilities)))


def check_slack_identities() -> None:
    ke = (K(r) + K(-r)) / 2
    J = sp.Rational(3, 2) * r**2 - 3 * ke

    first_slack = sp.simplify(
        sp.Rational(3, 2) * r**2 - J
        - sp.Rational(3, 2) * (K(r) + K(-r))
    )
    assert first_slack == 0

    second_slack = sp.simplify(
        3 - sp.diff(J, r, 2)
        - sp.Rational(3, 2) * (sp.diff(K(r), r, 2)
                               + sp.diff(K(-r), r, 2))
    )
    assert second_slack == 0

    derivative_slack = sp.simplify(
        3 * r - sp.diff(J, r)
        - sp.Rational(3, 2) * (sp.diff(K(r), r)
                               + sp.diff(K(-r), r))
    )
    assert derivative_slack == 0
    print("R105_SCHUR_ABEL_SLACK_IDENTITIES_PASSED")


def check_homometric_pair() -> None:
    sym_values = (sp.Rational(-3, 2), sp.Integer(0), sp.Rational(3, 2))
    sym_probabilities = (sp.Rational(2, 9), sp.Rational(5, 9),
                         sp.Rational(2, 9))
    asym_values = (sp.Integer(-1), sp.Rational(1, 2), sp.Integer(2))
    asym_probabilities = (sp.Rational(4, 9), sp.Rational(4, 9),
                          sp.Rational(1, 9))

    for values, probabilities in ((sym_values, sym_probabilities),
                                  (asym_values, asym_probabilities)):
        assert sum(probabilities) == 1
        assert moment(values, probabilities, 1) == 0
        assert moment(values, probabilities, 2) == 1
        assert moment(values, probabilities, 4) == sp.Rational(9, 4)

    assert moment(sym_values, sym_probabilities, 3) == 0
    assert moment(asym_values, asym_probabilities, 3) == sp.Rational(1, 2)

    m = lambda x: sp.Rational(2, 3) + sp.exp(x) / 3
    m_sym = sp.expand(m(sp.Rational(3, 2) * r)
                      * m(-sp.Rational(3, 2) * r))
    m_asym = sp.expand(sp.exp(-r) * m(sp.Rational(3, 2) * r)**2)
    assert sp.simplify(mgf(sym_values, sym_probabilities, r) - m_sym) == 0
    assert sp.simplify(mgf(asym_values, asym_probabilities, r) - m_asym) == 0
    assert sp.simplify(m_sym * m_sym.subs(r, -r)
                       - m_asym * m_asym.subs(r, -r)) == 0
    print("R105_HOMOMETRIC_BERNOULLI_PAIR_PASSED")


def check_fourth_order_exact_obstruction() -> None:
    # a_j = sqrt(2/3) cos(theta+2*pi*j/3).  The constant Fourier coefficient
    # of sum_j a_j^4 is 3*binom(4,2)/6^2 = 1/2.
    p4_average = sp.Rational(3) * sp.binomial(4, 2) / 6**2
    assert p4_average == sp.Rational(1, 2)

    kappa4 = sp.symbols("kappa4")
    coefficient_z4 = sp.simplify(kappa4 * p4_average / sp.factorial(4))
    assert coefficient_z4 == kappa4 / 48

    # Centered variance-one: m4 = kappa4 + 3.
    assert sp.simplify((kappa4 + 3).subs(kappa4, 0) - 3) == 0
    assert sp.Rational(9, 4) != 3
    print("R105_FOURTH_ORDER_EXACTNESS_OBSTRUCTION_PASSED")


def main() -> None:
    check_slack_identities()
    check_homometric_pair()
    check_fourth_order_exact_obstruction()
    print("R105_HOMOMETRIC_PHASE_OBSTRUCTION_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
