"""R49 exact audit: Christoffel compression of the lifted-null hierarchy.

This audit checks the all-degree identities extracted from the webpage R49
round.  It does not claim Xi_K -> infinity, ordinary Jacobi exit, or a
genuine all-degree branch exclusion.  The polynomial q is a test multiplier;
no shadow null relation is imposed on the full law.
"""

from sympy import Matrix, Poly, Rational, expand, factorial, simplify, sqrt, symbols


def polynomial_coefficients(polynomial, variable, degree):
    poly = Poly(expand(polynomial), variable)
    return Matrix([poly.coeff_monomial(variable ** j) for j in range(degree + 1)])


def hankel(moments, degree):
    return Matrix(
        [
            [moments[i + j] for j in range(degree + 1)]
            for i in range(degree + 1)
        ]
    )


def q_polynomial(variable, v, c):
    return variable * (variable ** 2 - c * variable - v)


def direct_lifted_gram(moments, K, variable, v, c):
    q = q_polynomial(variable, v, c)
    return Matrix(
        [
            [
                sum(
                    coefficient * moments[power]
                    for (power,), coefficient in Poly(
                        expand(variable ** (i + j) * q ** 2), variable
                    ).terms()
                )
                for j in range(K + 1)
            ]
            for i in range(K + 1)
        ]
    ).applyfunc(simplify)


def compression_matrix(K, variable, v, c):
    q = q_polynomial(variable, v, c)
    return Matrix.hstack(
        *[
            polynomial_coefficients(variable ** j * q, variable, K + 3)
            for j in range(K + 1)
        ]
    )


def check_gram_compression():
    variable = symbols("x")
    v, c = symbols("v c")
    moments = symbols("m0:20")
    for K in range(4):
        Q = compression_matrix(K, variable, v, c)
        H = hankel(moments, K + 3)
        compressed = (Q.T * H * Q).applyfunc(simplify)
        direct = direct_lifted_gram(moments, K, variable, v, c)
        assert (compressed - direct).applyfunc(simplify) == Matrix.zeros(K + 1)
    print("R49_CHRISTOFFEL_COMPRESSION_IDENTITY PASSED")


def monic_orthogonal_data(moments, maximum_degree):
    """Return monic OP coefficient vectors and squared norms exactly."""
    polynomials = []
    norms = []
    variable = symbols("x")
    for degree in range(maximum_degree + 1):
        if degree == 0:
            coefficients = Matrix([1])
        else:
            gram = Matrix(
                [
                    [moments[i + j] for j in range(degree)]
                    for i in range(degree)
                ]
            )
            rhs = Matrix([-moments[degree + i] for i in range(degree)])
            lower = gram.inv() * rhs
            coefficients = Matrix(list(lower) + [1])
        norm = sum(
            coefficients[i] * coefficients[j] * moments[i + j]
            for i in range(degree + 1)
            for j in range(degree + 1)
        )
        polynomials.append(coefficients)
        norms.append(simplify(norm))
    return polynomials, norms


def evaluate_coefficients(coefficients, point):
    return simplify(sum(value * point ** degree for degree, value in enumerate(coefficients)))


def kernel_matrix(polynomials, norms, last_degree, roots):
    return Matrix(
        [
            [
                sum(
                    evaluate_coefficients(polynomials[j], left)
                    * evaluate_coefficients(polynomials[j], right)
                    / norms[j]
                    for j in range(last_degree + 1)
                )
                for right in roots
            ]
            for left in roots
        ]
    ).applyfunc(simplify)


def transformed_moments(moments, maximum_degree, variable, v, c):
    q2 = expand(q_polynomial(variable, v, c) ** 2)
    return [
        simplify(
            sum(
                coefficient * moments[power]
                for (power,), coefficient in Poly(
                    expand(variable ** degree * q2), variable
                ).terms()
            )
        )
        for degree in range(maximum_degree + 1)
    ]


def exact_gaussian_moments(maximum_degree):
    return [
        0 if degree % 2 else factorial(degree) / (2 ** (degree // 2) * factorial(degree // 2))
        for degree in range(maximum_degree + 1)
    ]


def exact_five_point_moments(maximum_degree):
    """A normalized positive five-point law, used as a second exact test."""
    moments = []
    for degree in range(maximum_degree + 1):
        if degree == 0:
            moments.append(Rational(1))
        elif degree % 2:
            moments.append(0)
        else:
            moments.append(Rational(1, 2) + Rational(1, 8) * 4 ** (degree // 2))
    return moments


def root_data(v, c):
    discriminant = simplify(c ** 2 + 4 * v)
    roots = [0, (c + sqrt(discriminant)) / 2, (c - sqrt(discriminant)) / 2]
    vandermonde_square = simplify(
        (roots[0] - roots[1]) ** 2
        * (roots[0] - roots[2]) ** 2
        * (roots[1] - roots[2]) ** 2
    )
    return roots, vandermonde_square


def check_three_root_schur_formula(moments, label, maximum_K):
    variable = symbols("x")
    v = Rational(1, 2)
    c = 1
    roots, vandermonde_square = root_data(v, c)
    assert vandermonde_square == 6 * v ** 3

    original_polynomials, original_norms = monic_orthogonal_data(
        moments, maximum_K + 3
    )
    lifted_mom = transformed_moments(
        moments, 2 * maximum_K, variable, v, c
    )
    lifted_polynomials, lifted_norms = monic_orthogonal_data(
        lifted_mom, maximum_K
    )

    # D_n is det K_n, where K_n uses pi_0,...,pi_n.  This indexing makes
    # D_2 the first non-singular three-root evaluation kernel.
    D = {}
    kernels = {}
    for n in range(2, maximum_K + 4):
        kernels[n] = kernel_matrix(
            original_polynomials, original_norms, n, roots
        )
        D[n] = simplify(kernels[n].det())
        assert D[n] != 0

    for K in range(maximum_K + 1):
        N = K + 3
        kernel_for_schur = kernels[K + 2]
        pN = Matrix(
            [evaluate_coefficients(original_polynomials[N], root) for root in roots]
        )
        schur = simplify(
            original_norms[N]
            + (pN.T * kernel_for_schur.inv() * pN)[0]
        )
        assert simplify(lifted_norms[K] - schur) == 0

        gamma = direct_lifted_gram(moments, K, variable, v, c)
        H = hankel(moments, K + 3)
        factorized = simplify(H.det() * D[K + 3] / (6 * v ** 3))
        assert simplify(gamma.det() - factorized) == 0

    for K in range(1, maximum_K + 1):
        transformed_beta = simplify(lifted_norms[K] / lifted_norms[K - 1])
        original_beta = simplify(original_norms[K + 3] / original_norms[K + 2])
        rhs = simplify(
            original_beta
            * D[K + 3]
            * D[K + 1]
            / D[K + 2] ** 2
        )
        assert simplify(transformed_beta - rhs) == 0

    print(f"R49_THREE_ROOT_SCHUR_FORMULA {label} PASSED")
    print(f"R49_HANKEL_KERNEL_DETERMINANT_FACTORIZATION {label} PASSED")
    print(f"R49_TRANSFORMED_JACOBI_RECURSION {label} PASSED")


def main():
    check_gram_compression()
    check_three_root_schur_formula(
        exact_gaussian_moments(2 * (4 + 3)), "GAUSSIAN", 4
    )
    check_three_root_schur_formula(
        exact_five_point_moments(2 * (1 + 3)), "FIVE_POINT", 1
    )
    print("R49_LIFTED_GRAM_NO_INDEPENDENT_SIGN_PRESSURE RECORDED")
    print("R49_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN")
    print("R49_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
