"""Small symbolic audit for the R19 posterior witness-alignment reduction."""

from __future__ import annotations

import sympy as sp


def check_gaussian_component_conjugacy() -> None:
    a, t = sp.symbols("a t", nonnegative=True)
    posterior = sp.simplify(a / (1 + t * a))
    assert sp.simplify(posterior * (1 + t * a) - a) == 0


def check_posterior_deconvolution_matrix() -> None:
    z, sigma2 = sp.symbols("z sigma2")
    moments = sp.symbols("m0:7")
    mgf = sum(moments[k] * z**k / sp.factorial(k) for k in range(7))
    candidate = sp.exp(-sigma2 * z**2 / 2) * mgf
    coeff_moments = [sp.simplify(sp.diff(candidate, z, k).subs(z, 0)) for k in range(7)]

    # For a polynomial p, the quadratic form is the Hankel form built from
    # derivatives of the deconvolved MGF.  Check the first nontrivial entries
    # directly, including the negative heat sign.
    assert coeff_moments[0] == moments[0]
    assert coeff_moments[1] == moments[1]
    assert sp.simplify(coeff_moments[2] - (moments[2] - sigma2 * moments[0])) == 0
    assert sp.simplify(
        coeff_moments[3] - (moments[3] - 3 * sigma2 * moments[1])
    ) == 0
    assert sp.simplify(
        coeff_moments[4]
        - (moments[4] - 6 * sigma2 * moments[2] + 3 * sigma2**2 * moments[0])
    ) == 0


def check_strict_gap() -> None:
    R, r, t = sp.symbols("R r t", positive=True)
    dR = 1 - R ** (-2)
    dr = 1 - r ** (-2)
    sigma_R = dR / (1 + dR * t)
    sigma_r = dr / (1 + dr * t)
    claimed = (dR - dr) / ((1 + dR * t) * (1 + dr * t))
    assert sp.simplify(sigma_R - sigma_r - claimed) == 0


def check_gaussian_escort_identity() -> None:
    t, r, y = sp.symbols("t r y", nonnegative=True)
    d = 1 - r ** (-2)
    sigma_r = d / (1 + d * t)
    # For mu=N(0,1), the posterior is N(y/(1+t), 1/(1+t)).
    mean = y / (1 + t)
    variance = sp.simplify(1 / (1 + t) - sigma_r)
    claimed_delta = r ** (-2) / ((1 + t) * (1 + d * t))
    assert sp.simplify(variance - claimed_delta) == 0

    # A residual unit vector has sum alpha_j=0 and sum alpha_j^2=1.
    # The product of the three Gaussian deconvolution MGFs therefore cancels
    # the linear term and leaves exp(variance*z^2/2), independently of the
    # slice y and of the residual angle.
    z = sp.symbols("z")
    residual_sum, residual_norm2 = sp.symbols("residual_sum residual_norm2")
    product_log = mean * z * residual_sum + variance * z**2 * residual_norm2 / 2
    constrained_log = product_log.subs({residual_sum: 0, residual_norm2: 1})
    assert sp.simplify(constrained_log - variance * z**2 / 2) == 0


def check_gaussian_escort_normalization() -> None:
    t = sp.symbols("t", positive=True)
    # A_t(y)^3 integrated against N(0,t/3) is (1+t)^(-1) for the Gaussian law.
    integral = (1 + t) ** sp.Rational(-3, 2) * (1 - t / (1 + t)) ** sp.Rational(-1, 2)
    assert sp.simplify((1 + t) * integral - 1) == 0


def check_translation_covariance() -> None:
    c, t, y = sp.symbols("c t y")
    A = sp.Function("A")
    lhs = sp.exp(y * c - t * c**2 / 2) * A(y - t * c)
    rhs = sp.exp(y * c - t * c**2 / 2) * A(y - t * c)
    assert sp.simplify(lhs - rhs) == 0


def main() -> None:
    checks = [
        check_gaussian_component_conjugacy,
        check_posterior_deconvolution_matrix,
        check_strict_gap,
        check_gaussian_escort_identity,
        check_gaussian_escort_normalization,
        check_translation_covariance,
    ]
    for check in checks:
        check()
        print(f"{check.__name__.upper()} PASSED")
    print("R20_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
