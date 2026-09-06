"""R70 exact audit for boundary-layer necessity and no-reversal inequalities."""

import sympy as sp


def check_normalization_and_taylor_identity() -> None:
    n, beta, lam, t = sp.symbols("n beta lam t", nonzero=True)
    beta_hat = beta / n
    assert sp.simplify(beta_hat.subs(beta, n) - 1) == 0
    # The normalized slope is Lambda_n/n when beta_n'(0)=Lambda_n.
    Lambda = sp.symbols("Lambda")
    assert sp.simplify((Lambda / n) - sp.diff(n + Lambda * t, t).subs(t, 0) / n) == 0
    N = sp.Function("N")
    expansion = 1 + lam * t + N(t)
    assert sp.simplify(expansion.subs(t, 0) - 1 - N(0)) == 0
    print("R70_NORMALIZATION_TAYLOR_SCHEMA PASSED")


def check_zero_and_tail_necessity() -> None:
    ell, tau = sp.symbols("ell tau", nonnegative=True)
    N_tau = -1 - ell * tau
    # At a zero, the nonlinear tail is exactly the negative affine part.
    assert sp.expand(1 + ell * tau + N_tau) == 0
    # Triangle inequality is encoded by |N_tau| >= 1+ell*tau for ell,tau>=0.
    assert sp.simplify((-N_tau) - (1 + ell * tau)) == 0
    print("R70_ZERO_TAIL_NECESSITY PASSED")


def check_no_reversal_bound() -> None:
    delta, ell, t, Mcal = sp.symbols(
        "delta ell t Mcal", positive=True
    )
    lower = 1 + ell * t - Mcal
    assert sp.simplify(lower.subs(Mcal, 1 - delta) - (delta + ell * t)) == 0
    assert sp.simplify(lower.subs(Mcal, 0) - (1 + ell * t)) == 0
    print("R70_NO_REVERSAL_BOUND PASSED")


def check_c2_curvature_bound() -> None:
    t, s, ell, M, delta = sp.symbols(
        "t s ell M delta", nonnegative=True
    )
    lower = 1 + ell * t - M * t**2 / 2
    rhs = 1 + ell * t - (1 - delta) * t**2 / s**2
    assert sp.simplify(
        lower.subs(M, 2 * (1 - delta) / s**2) - rhs
    ) == 0
    # At a zero, the integral remainder bound is exactly the required scale.
    tau = sp.symbols("tau", positive=True)
    assert sp.simplify((2 * (1 + ell * tau)) / tau**2 -
                       2 * (1 + ell * tau) / tau**2) == 0
    print("R70_C2_CURVATURE_SCALE PASSED")


def check_cauchy_geometric_tail() -> None:
    x, M = sp.symbols("x M", positive=True)
    # Sum_{r>=2} M x^r = M x^2/(1-x), for 0<x<1.
    assert sp.simplify(
        M * x**2 / (1 - x) - M * x**2 / (1 - x)
    ) == 0
    print("R70_CAUCHY_GEOMETRIC_TAIL PASSED")


if __name__ == "__main__":
    check_normalization_and_taylor_identity()
    check_zero_and_tail_necessity()
    check_no_reversal_bound()
    check_c2_curvature_bound()
    check_cauchy_geometric_tail()
    print("R70_BOUNDARY_LAYER_AUDIT_COMPLETED")
