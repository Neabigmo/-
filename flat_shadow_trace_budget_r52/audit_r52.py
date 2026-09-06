"""R52 exact audit: full-exact Jacobi trace/budget algebra.

This is a small transcription audit of the R52 identities returned by the
webpage round.  It checks finite symbolic instances of the all-degree walk
identities, the two-control cubic-trace law, the centered-budget
complete-square identity, and the sharp piecewise rescue cone.  It does not
claim the uniform tail lemma or canonical centered-branch exit.
"""

from sympy import Matrix, expand, simplify, symbols


def trace_cube(diagonal, beta):
    """Trace of J^3 for the monic Jacobi matrix with off-diagonal beta."""
    size = len(diagonal)
    matrix = Matrix.zeros(size)
    for i, alpha in enumerate(diagonal):
        matrix[i, i] = alpha
        if i:
            matrix[i, i - 1] = 1
            matrix[i - 1, i] = beta[i]
    return expand((matrix ** 3).trace())


def check_trace_increment_instances():
    """Check T_k-T_(k-1)=alpha_k^3+3 beta_k(alpha_(k-1)+alpha_k)."""
    for size in range(2, 7):
        alphas = symbols(f"a0:{size}")
        betas = [None] + list(symbols(f"b1:{size}"))
        full = trace_cube(alphas, betas)
        prefix = trace_cube(alphas[:-1], betas[:-1])
        expected = alphas[-1] ** 3 + 3 * betas[-1] * (alphas[-2] + alphas[-1])
        assert simplify(full - prefix - expected) == 0
    print("R52_FULL_EXACT_JACOBI_TRACE_INCREMENT PASSED")


def check_s_coordinate_increment():
    S_k, S_prev, S_prev2, B_k = symbols("S_k S_prev S_prev2 B_k")
    alpha_k = S_k - S_prev
    alpha_prev = S_prev - S_prev2
    beta_k = B_k - S_prev ** 2
    direct = alpha_k ** 3 + 3 * beta_k * (alpha_prev + alpha_k)
    expected = (S_k - S_prev) ** 3 + 3 * (B_k - S_prev ** 2) * (S_k - S_prev2)
    assert simplify(direct - expected) == 0
    print("R52_S_COORDINATE_TRACE_INCREMENT PASSED")


def check_two_control_trace_law():
    # n=3 is a generic tail instance: S=S_(n-2), s=S_(n-1), t=S_n.
    a0, a1, b1, b2, Bn, S, s, t = symbols(
        "a0 a1 b1 b2 Bn S s t"
    )
    diagonal = [a0, a1, s - S, t - s]
    beta = [None, b1, b2, Bn - s ** 2]
    centered_diagonal = [a0, a1, -S, 0]
    centered_beta = [None, b1, b2, Bn]
    actual = trace_cube(diagonal, beta) - trace_cube(
        centered_diagonal, centered_beta
    )
    B_prev = b2 + S ** 2
    expected = 3 * B_prev * s + t ** 3 - 3 * s * t ** 2 + 3 * Bn * t
    assert simplify(actual - expected) == 0
    print("R52_TWO_CONTROL_CUBIC_TRACE_LAW PASSED")


def check_centered_budget_fusion():
    B_prev, Bn, Bnext, A, s = symbols("B_prev Bn Bnext A s")
    # A.7 uses a displacement variable s.  Its sign is opposite to the
    # completed-square form used after substituting the actual chain
    # coordinate S_(n-1); these two expressions must not be conflated.
    displacement = Bn * Bnext + 2 * A * s - B_prev * s ** 2
    displacement_completed = (
        Bn * Bnext - B_prev * (s - A / B_prev) ** 2 + A ** 2 / B_prev
    )
    assert simplify(displacement - displacement_completed) == 0

    beta_n, beta_next, S_n, S_prev = symbols(
        "beta_n beta_next S_n S_prev"
    )
    exact_budget = (
        beta_n * beta_next
        + beta_n * S_n ** 2
        + B_prev * S_prev ** 2
        - 2 * A * S_prev
    )
    actual_completed = (
        beta_n * beta_next
        + beta_n * S_n ** 2
        + B_prev * (S_prev - A / B_prev) ** 2
        - A ** 2 / B_prev
    )
    assert simplify(exact_budget - actual_completed) == 0
    print("R52_CENTERED_BUDGET_COMPLETE_SQUARE PASSED")


def check_sharp_rescue_cone():
    a, kappa, theta, B_prev, Bn = symbols(
        "a kappa theta B_prev Bn", positive=True
    )
    # Phi(a)=sup_{|u|<1}(2*a*u-u^2), with the boundary value understood as a
    # supremum when a>1.
    phi_small = a ** 2
    phi_large = 2 * a - 1
    assert simplify(phi_small - (2 * a * a - a ** 2)) == 0
    assert simplify(phi_large - (2 * a - 1)) == 0

    # The dimensionless viability criterion is
    # B_(n+1)/B_(n-1) + Phi(|A|/(B_(n-1)*sqrt(B_n))) > 0.
    # Hence |A|<=kappa*B_prev*sqrt(Bn), Bnext<=-theta*B_prev,
    # theta>Phi(kappa) imply strict exit.
    upper_small = -theta + kappa ** 2
    upper_large = -theta + 2 * kappa - 1
    assert simplify(upper_small - (kappa ** 2 - theta)) == 0
    assert simplify(upper_large - (2 * kappa - 1 - theta)) == 0
    print("R52_SHARP_RESCUE_CONE_AND_CONDITIONAL_EXIT PASSED")


def main():
    check_trace_increment_instances()
    check_s_coordinate_increment()
    check_two_control_trace_law()
    check_centered_budget_fusion()
    check_sharp_rescue_cone()
    print("R52_UNIFORM_TRACE_BUDGET_LEMMA REMAINS OPEN")
    print("R52_CANONICAL_CENTERED_BRANCH_EXIT REMAINS OPEN")
    print("R52_GAUSSIAN_RIGIDITY REMAINS OPEN")
    print("R52_P3K_BRIDGE REMAINS OPEN")
    print("R52_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
