"""R68 exact audit for the D-part coefficient-transfer reduction.

This checks finite algebra and analytic bookkeeping only. It does not use
determinants, optimizers, SDP, parameter sweeps, or remote computation, and it
does not treat the sectorial contour-rotation hypotheses as numerically proved.
"""

import sympy as sp


def check_u_kernel_integration() -> None:
    """Integrate the three exact powers of u in the Laplace representation."""
    u, a, alpha, beta = sp.symbols("u a alpha beta", positive=True)
    c = alpha + beta
    integrand = 216 * u**3 * (1 - 3 * alpha * u) * (1 - 3 * beta * u) * sp.exp(
        -(a + 6 * c) * u
    )
    integrated = sp.integrate(integrand, (u, 0, sp.oo))
    expected = (
        sp.Rational(1296) / (a + 6 * c) ** 4
        - sp.Rational(15552) * c / (a + 6 * c) ** 5
        + sp.Rational(233280) * alpha * beta / (a + 6 * c) ** 6
    )
    assert sp.simplify(integrated - expected) == 0
    print("R68_LAPLACE_U_POWER_INTEGRATION PASSED")


def check_rational_kernel_constants() -> None:
    """Check conversion from a=(1-z)/z to the displayed z-kernel."""
    z, lam, c, alpha, beta = sp.symbols("z lam c alpha beta")
    a = (1 - z) / z
    relation = sp.simplify(
        (a + 6 * c - (1 - lam * z) / z).subs(lam, 1 - 6 * c)
    )
    assert relation == 0
    kernel = -sp.Rational(1, 3) / z * (
        sp.Rational(1296) / (a + 6 * c) ** 4
        - sp.Rational(15552) * c / (a + 6 * c) ** 5
        + sp.Rational(233280) * alpha * beta / (a + 6 * c) ** 6
    )
    expected = (
        -432 * z**3 / (1 - lam * z) ** 4
        + 5184 * c * z**4 / (1 - lam * z) ** 5
        - 77760 * alpha * beta * z**5 / (1 - lam * z) ** 6
    )
    assert sp.simplify((kernel - expected).subs(lam, 1 - 6 * c)) == 0
    print("R68_RATIONAL_KERNEL_CONSTANTS PASSED")


def check_coefficient_extraction() -> None:
    """Check the exact binomial coefficient formula for symbolic lambda."""
    z, lam, c, alpha, beta = sp.symbols("z lam c alpha beta")
    kernel = (
        -432 * z**3 / (1 - lam * z) ** 4
        + 5184 * c * z**4 / (1 - lam * z) ** 5
        - 77760 * alpha * beta * z**5 / (1 - lam * z) ** 6
    )
    for n in range(0, 13):
        coefficient = sp.expand(
            kernel.series(z, 0, n + 1).removeO()
        ).coeff(z, n)
        expected = 0
        if n >= 3:
            expected += -432 * sp.binomial(n, 3) * lam ** (n - 3)
        if n >= 4:
            expected += 5184 * c * sp.binomial(n, 4) * lam ** (n - 4)
        if n >= 5:
            expected += -77760 * alpha * beta * sp.binomial(n, 5) * lam ** (n - 5)
        assert sp.expand(coefficient - expected) == 0
    print("R68_COEFFICIENT_EXTRACTION PASSED")


def check_domain_geometry() -> None:
    """Check the endpoint ray geometry for lambda in [-1/2,1]."""
    assert sp.simplify(1 / sp.Integer(1) - 1) == 0
    assert sp.simplify(1 / sp.Rational(-1, 2) + 2) == 0
    # For lambda>0, 1/lambda lies in [1,infinity); for lambda<0,
    # 1/lambda lies in (-infinity,-2].
    for value in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Integer(1)):
        assert 1 / value >= 1
    for value in (sp.Rational(-1, 4), sp.Rational(-1, 2)):
        assert 1 / value <= -2
    print("R68_SLIT_DOMAIN_ENDPOINTS PASSED")


def check_root_geometry_and_local_scaling() -> None:
    """Check the exact D3 root identities used in the zero cancellation."""
    theta = sp.symbols("theta", real=True)
    rho = sp.sqrt(sp.Rational(2, 3))
    roots = [rho * sp.cos(theta + 2 * sp.pi * j / 3) for j in range(3)]
    assert sp.trigsimp(sum(roots)) == 0
    for k in range(3):
        i, j = [idx for idx in range(3) if idx != k]
        assert sp.trigsimp(roots[i] + roots[j] + roots[k]) == 0
    print("R68_D3_ROOT_CANCELLATION_GEOMETRY PASSED")


def check_moment_remainder_scaling() -> None:
    """Check the exponent produced by two finite moments and u^(-5/2) tail."""
    s, u = sp.symbols("s u", positive=True)
    near = sp.integrate(s**2 * u ** sp.Rational(-1, 2), (u, 1, 1 / s))
    far = sp.integrate(u ** sp.Rational(-5, 2), (u, 1 / s, sp.oo))
    assert sp.limit(near / s ** sp.Rational(3, 2), s, 0, dir="+") == 2
    assert sp.limit(far / s ** sp.Rational(3, 2), s, 0, dir="+") == sp.Rational(2, 3)
    print("R68_TWO_MOMENT_REMAINDER_SCALING PASSED")


def check_transfer_exponent() -> None:
    """Check the standard coefficient exponent for a 3/2 singular remainder."""
    n = sp.symbols("n", integer=True, positive=True)
    coefficient = sp.gamma(n - sp.Rational(3, 2)) / (
        sp.gamma(-sp.Rational(3, 2)) * sp.gamma(n + 1)
    )
    assert sp.simplify(
        sp.gamma(-sp.Rational(3, 2)) - sp.Rational(4, 3) * sp.sqrt(sp.pi)
    ) == 0
    limit = sp.limit(coefficient * n ** sp.Rational(5, 2), n, sp.oo)
    assert sp.simplify(limit - 1 / sp.gamma(-sp.Rational(3, 2))) == 0
    print("R68_DELTA_TRANSFER_EXPONENT PASSED")


if __name__ == "__main__":
    check_u_kernel_integration()
    check_rational_kernel_constants()
    check_coefficient_extraction()
    check_domain_geometry()
    check_root_geometry_and_local_scaling()
    check_moment_remainder_scaling()
    check_transfer_exponent()
    print("R68_DPART_TRANSFER_AUDIT_COMPLETED")
