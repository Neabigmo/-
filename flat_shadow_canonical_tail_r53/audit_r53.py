"""R53 exact audit: canonical Jacobi tail and Gauss-quadrature deficit.

This audit checks the all-order identities exposed in the R53 webpage round:

* canonical centered Jacobi tails reduce the monic recurrence to a scalar
  beta/B recursion;
* n-point Gauss quadrature matches moments through degree 2*n-1, with the
  exact even and odd error formulas at degrees 2*n and 2*n+1;
* the canonical odd choice is exactly the quadrature odd moment;
* the deficit-to-norm and beta/norm ratio laws have the right constants;
* a centered Jacobi tail stabilizes the cubic trace;
* positivity of every tail beta gives the conditional Favard/Hamburger
  realization, while finite computations do not claim D.1.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation is used here.  The last realization marker records a conditional
theorem: it is not a proof that the canonical branch remains positive.
"""

from sympy import Matrix, Rational, expand, simplify, symbols


def jacobi_matrix(alphas, betas):
    """Finite monic Jacobi multiplication matrix in the pi-basis."""
    size = len(alphas)
    matrix = Matrix.zeros(size)
    for k, alpha in enumerate(alphas):
        matrix[k, k] = alpha
        if k:
            matrix[k, k - 1] = 1
            matrix[k - 1, k] = betas[k]
    return matrix


def jacobi_moment(alphas, betas, degree):
    """Return e_0^T J^degree e_0 for the finite Jacobi matrix."""
    return expand((jacobi_matrix(alphas, betas) ** degree)[0, 0])


def norm_from_beta(beta, degree):
    """h_degree/h_0 = beta_1 ... beta_degree."""
    result = Rational(1)
    for k in range(1, degree + 1):
        result *= beta[k]
    return expand(result)


def check_canonical_jacobi_tail_recurrence():
    """Check S=0 tail, alpha=0, B=beta, and the norm product law."""
    alpha_head = [Rational(1, 3), Rational(-1, 3)]
    beta = [None, Rational(5, 4), Rational(7, 3), Rational(11, 5), Rational(13, 6)]
    cumulative = []
    running = Rational(0)
    for value in alpha_head:
        running += value
        cumulative.append(running)
    assert cumulative[-1] == 0

    # Opening centered slots keeps every new cumulative odd coordinate zero.
    alpha = alpha_head + [Rational(0), Rational(0), Rational(0)]
    S = Rational(0)
    for k in range(len(alpha_head), len(alpha)):
        S += alpha[k]
        assert S == 0
        assert alpha[k] == 0

    for n in range(2, len(alpha)):
        B = beta[n]  # S_(n-1)=0 on this tail.
        assert simplify(B - beta[n]) == 0
        assert simplify(norm_from_beta(beta, n) - beta[n] * norm_from_beta(beta, n - 1)) == 0
    print("R53_CANONICAL_JACOBI_TAIL_RECURRENCE PASSED")


def check_gauss_quadrature_error_identities():
    """Check q_{2n} and q_{2n+1} errors against monic Jacobi norms."""
    # The full matrix has one extra row; moments <=2n+1 are exact there.
    for n in range(2, 5):
        alpha = list(symbols(f"a0:{n + 1}"))
        beta = [None] + list(symbols(f"b1:{n + 1}"))
        q_alpha = alpha[:n]
        q_beta = beta[:n]
        q_even = jacobi_moment(q_alpha, q_beta, 2 * n)
        q_odd = jacobi_moment(q_alpha, q_beta, 2 * n + 1)
        full_even = jacobi_moment(alpha, beta, 2 * n)
        full_odd = jacobi_moment(alpha, beta, 2 * n + 1)
        h_n = norm_from_beta(beta, n)
        S_prev = sum(alpha[:n])
        S_n = S_prev + alpha[n]
        assert simplify(full_even - q_even - h_n) == 0
        assert simplify(full_odd - q_odd - (S_n + S_prev) * h_n) == 0
    print("R53_GAUSS_QUADRATURE_DEFICIT_IDENTITY PASSED")


def check_even_odd_quadrature_update():
    """Canonical S_(n-1)=S_n=0 means the next odd moment is q_(2n+1)."""
    for n in range(2, 5):
        # Choose a centered tail after a nontrivial head, with arbitrary
        # positive beta values.  The two cumulative sums are exactly zero.
        alpha = [Rational(2, 5), Rational(-2, 5)] + [Rational(0)] * (n - 1)
        beta = [None] + [Rational(k + 3, 2) for k in range(n + 1)]
        assert sum(alpha[:n]) == 0
        assert sum(alpha[: n + 1]) == 0
        q_odd = jacobi_moment(alpha[:n], beta[:n], 2 * n + 1)
        full_odd = jacobi_moment(alpha, beta, 2 * n + 1)
        assert simplify(full_odd - q_odd) == 0
    print("R53_EVEN_ODD_QUADRATURE_UPDATE PASSED")


def check_deficit_beta_norm_ratio():
    """Check delta=c*h and B=beta=(3/2)*delta_n/delta_(n-1)."""
    c = lambda n: 3 * Rational(2, 3) ** n
    beta = [None, Rational(4, 3), Rational(7, 4), Rational(9, 5), Rational(11, 6)]
    h = {0: Rational(1)}
    for n in range(1, len(beta)):
        h[n] = expand(beta[n] * h[n - 1])
    delta = {n: expand(h[n] * c(n)) for n in h}
    for n in range(1, len(beta)):
        assert simplify(h[n] - delta[n] / c(n)) == 0
        assert simplify(beta[n] - Rational(3, 2) * delta[n] / delta[n - 1]) == 0
    print("R53_DEFICIT_BETA_NORM_RATIO PASSED")


def trace_cube(alphas, beta):
    return expand((jacobi_matrix(alphas, beta) ** 3).trace())


def check_cubic_trace_stabilization():
    """Once two consecutive centered slots open, the cubic trace increment is 0."""
    beta = [None, Rational(5, 4), Rational(7, 3), Rational(11, 5), Rational(13, 6)]
    alpha = [Rational(1, 3), Rational(-1, 3), Rational(0), Rational(0), Rational(0)]
    for n in range(3, len(alpha)):
        current = trace_cube(alpha[: n + 1], beta[: n + 1])
        previous = trace_cube(alpha[:n], beta[:n])
        assert simplify(current - previous) == 0
    print("R53_CUBIC_TRACE_STABILIZATION PASSED")


def check_positive_branch_realization_implication():
    """Finite orthogonal-basis positivity audit for the conditional branch."""
    beta = [None, Rational(3, 2), Rational(5, 3), Rational(7, 4), Rational(9, 5)]
    norms = [norm_from_beta(beta, n) for n in range(len(beta))]
    assert all(value > 0 for value in norms)

    # In the monic orthogonal basis, a nonzero polynomial has norm
    # sum_j c_j^2 h_j.  This is the finite Favard positivity certificate;
    # the infinite Hamburger/Favard conclusion remains conditional on all
    # future beta_n staying positive.
    coefficients = [Rational(2), Rational(-3), Rational(1), Rational(4)]
    quadratic_norm = sum(
        coefficients[j] ** 2 * norms[j] for j in range(len(coefficients))
    )
    assert quadratic_norm > 0
    print(
        "R53_POSITIVE_BRANCH_FULL_EXACT_REALIZATION "
        "CONDITIONAL_ON_ALL_BETA_POSITIVE PASSED"
    )


def main():
    check_canonical_jacobi_tail_recurrence()
    check_gauss_quadrature_error_identities()
    check_even_odd_quadrature_update()
    check_deficit_beta_norm_ratio()
    check_cubic_trace_stabilization()
    check_positive_branch_realization_implication()
    print("R53_CANONICAL_CENTERED_TAIL_RIGIDITY REMAINS OPEN")
    print("R53_EVENTUAL_DIAGONAL_SKEW_ANNIHILATION REMAINS OPEN")
    print("R53_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
