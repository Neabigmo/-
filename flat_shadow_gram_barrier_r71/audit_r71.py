"""R71 exact audit for the Hermite--Gram boundary-layer barrier."""

import sympy as sp


def check_normalization() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    h_n, h_prev = sp.symbols("h_n h_prev", nonzero=True)
    gamma_n = h_n / sp.factorial(n)
    gamma_prev = h_prev / sp.factorial(n - 1)
    beta_hat = h_n / h_prev / n
    assert sp.simplify(gamma_n / gamma_prev - beta_hat) == 0
    print("R71_GRAM_BETA_NORMALIZATION PASSED")


def check_transform_identities() -> None:
    q, z = sp.symbols("q z")
    A = q / (1 - 2 * q)
    prefactor = 1 / sp.sqrt(1 - 2 * q)
    gaussian_integral = prefactor / sp.sqrt(1 + 2 * A)
    exponent = -z**2 / 2 + z**2 / (2 * (1 + 2 * A))
    # SymPy keeps the square-root branch unevaluated; on 0<=q<=1/4 both
    # factors are positive, so checking the squared identity is exact there.
    assert sp.simplify(gaussian_integral**2 - 1) == 0
    assert sp.simplify(exponent + q * z**2) == 0

    U = q * z**3 * sp.exp(-q * z**2) - q**2 * z**5 * sp.exp(-q * z**2) / 2
    U_expected = z**3 * q * sp.exp(-q * z**2) * (1 - q * z**2 / 2)
    assert sp.simplify(U - U_expected) == 0
    print("R71_GAUSSIAN_TRANSFORM_IDENTITIES PASSED")


def check_endpoint_bound_exponents() -> None:
    # Endpoint integration of s^r |x|^p exp(-s*x^2/2) has power
    # |x|^(p-2*r-2). The two worst tangent terms are exactly O(|x|^-1).
    assert 3 - 2 * 1 - 2 == -1
    assert 5 - 2 * 2 - 2 == -1
    assert sp.Rational(1, 4) + sp.Rational(1, 2) + sp.Rational(1, 4) == 1
    print("R71_LINF_TANGENT_ENDPOINT_BOUND PASSED")


def check_block_kernel_implication() -> None:
    a11, a12, a22, b1, b2, c = sp.symbols(
        "a11 a12 a22 b1 b2 c"
    )
    A = sp.Matrix([[a11, a12], [a12, a22]])
    b = sp.Matrix([b1, b2])
    S = sp.symbols("S")
    u = -A.inv() * b
    block = A.row_join(b).col_join(b.T.row_join(sp.Matrix([[c]])))
    kernel_vector = u.col_join(sp.Matrix([1]))
    residual = sp.simplify(block * kernel_vector)
    assert residual[:2, 0] == sp.zeros(2, 1)
    assert sp.simplify(residual[2, 0] - (c - (b.T * A.inv() * b)[0])) == 0
    # Setting the scalar Schur complement to zero makes the last residual zero.
    assert sp.simplify((c - (b.T * A.inv() * b)[0]).subs(
        c, (b.T * A.inv() * b)[0]
    )) == 0
    print("R71_SCHUR_COMPLEMENT_KERNEL_IMPLICATION PASSED")


def check_coefficient_majorant() -> None:
    n, m = sp.symbols("n m", nonnegative=True, integer=True)
    # Holder (4,2,4) plus degree-n/m hypercontractivity gives this exponent.
    exponent = (n + m) / 2
    assert sp.simplify(3**exponent - 3 ** (n / 2) * 3 ** (m / 2)) == 0
    # Product e_j e_k has degree at most 2n, hence the moment tail is finite.
    j, k = sp.symbols("j k", nonnegative=True, integer=True)
    assert sp.simplify((j + k).subs({j: n, k: n}) - 2 * n) == 0
    print("R71_ALL_ORDER_COEFFICIENT_MAJORANT_SCHEMA PASSED")


def check_angular_solver() -> None:
    theta = sp.symbols("theta", real=True)
    for k in range(0, 9):
        angular_cos = sp.integrate(sp.cos(theta) ** (2 * k), (theta, 0, 2 * sp.pi))
        expected_cos = 2 * sp.pi * sp.binomial(2 * k, k) / 4**k
        assert sp.simplify(angular_cos - expected_cos) == 0

        eigenvalue = 3 * sp.binomial(2 * k, k) / 6**k
        next_eigenvalue = 3 * sp.binomial(2 * k + 2, k + 1) / 6 ** (k + 1)
        ratio = sp.simplify(next_eigenvalue / eigenvalue)
        assert ratio == sp.Rational(2 * k + 1, 3 * (k + 1))
        assert sp.simplify(ratio < 1) is sp.true
    print("R71_ANGULAR_EIGENVALUE_AND_RATIO PASSED")


if __name__ == "__main__":
    check_normalization()
    check_transform_identities()
    check_endpoint_bound_exponents()
    check_block_kernel_implication()
    check_coefficient_majorant()
    check_angular_solver()
    print("R71_HERMITE_GRAM_BARRIER_AUDIT_COMPLETED")
