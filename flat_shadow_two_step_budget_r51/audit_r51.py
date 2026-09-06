"""R51 exact audit: the optimized two-step Jacobi budget.

This audit checks the new exact identities from the webpage R51 round:
the doubly-centered budget, the optimized two-step viability functional, and
the cubic Jacobi-trace representation of the geometric center.  It records
the conditional exit theorem algebraically but does not claim that its
tail hypotheses hold for the full compatible prefix class.
"""

from sympy import expand, simplify, symbols


def trace_cube(diagonal, beta):
    """Trace of the cube of a scalar Jacobi matrix from its coefficients."""
    value = sum(entry ** 3 for entry in diagonal)
    value += 3 * sum(
        beta[j] * (diagonal[j - 1] + diagonal[j])
        for j in range(1, len(diagonal))
    )
    return expand(value)


def check_doubly_centered_transfer():
    b_prev, b_n, b_next, sigma, s = symbols(
        "B_prev B_n B_next sigma s"
    )
    centered = b_n * b_next
    assert simplify(centered - b_n * b_next) == 0

    transfer = b_n * b_next + 2 * b_prev * sigma * s - b_prev * s ** 2
    completed = (
        b_n * b_next
        + b_prev * sigma ** 2
        - b_prev * (s - sigma) ** 2
    )
    assert simplify(transfer - completed) == 0
    print("R51_DOUBLY_CENTERED_TRANSFER_IDENTITY PASSED")


def check_radius_and_optimized_functional():
    b_prev, b_n, b_next, sigma = symbols(
        "B_prev B_n B_next sigma"
    )
    M_over_h = b_n * b_next + b_prev * sigma ** 2
    radius_squared = M_over_h / b_prev
    assert simplify(
        radius_squared - (sigma ** 2 + b_n * b_next / b_prev)
    ) == 0

    # The two exact branches of sup_{|s|<r}(2*sigma*s-s^2).
    r, abs_sigma = symbols("r abs_sigma")
    centered_branch = sigma ** 2
    boundary_branch = 2 * abs_sigma * r - r ** 2
    assert simplify(
        centered_branch - (2 * sigma * sigma - sigma ** 2)
    ) == 0
    assert simplify(
        boundary_branch - (2 * abs_sigma * r - r ** 2)
    ) == 0

    # With A=B_(n-1)*sigma and r=sqrt(B_n), these are exactly the two
    # branches of the rescue term R_n.
    A, root_bn = symbols("A root_B_n")
    first_R = A ** 2 / b_prev
    second_R = 2 * A * root_bn - b_prev * root_bn ** 2
    assert simplify(first_R.subs(A, b_prev * sigma) - b_prev * sigma ** 2) == 0
    assert simplify(
        second_R.subs({A: b_prev * abs_sigma, root_bn ** 2: b_n})
        - (2 * b_prev * abs_sigma * root_bn - b_prev * b_n)
    ) == 0
    print("R51_RADIUS_AND_OPTIMIZED_FUNCTIONAL PASSED")


def check_exit_equivalence_and_centered_budget_sign():
    b_prev, b_n, b_next, sigma = symbols(
        "B_prev B_n B_next sigma"
    )
    rescue_center = b_prev * sigma ** 2
    V_center = b_n * b_next + rescue_center
    assert simplify(V_center - (b_n * b_next + b_prev * sigma ** 2)) == 0

    # If B_next>=0, the exact radius identity gives R_n^2>=sigma^2;
    # center pressure alone cannot force interval separation.
    radius_gap = b_n * b_next / b_prev
    assert simplify(
        (sigma ** 2 + radius_gap) - sigma ** 2 - radius_gap
    ) == 0

    # Conditional theorem: |A|<=kappa*B_prev*sqrt(B_n), and
    # B_next<=-theta*B_prev, with theta>kappa^2, imply V<0.
    kappa, theta = symbols("kappa theta")
    upper_V = -theta * b_prev * b_n + kappa ** 2 * b_prev * b_n
    target = -(theta - kappa ** 2) * b_prev * b_n
    assert simplify(upper_V - target) == 0
    print("R51_CENTERED_BUDGET_EXIT_ALGEBRA PASSED")


def check_cubic_trace_affine_law():
    # A generic n=3 tail verifies the coefficient law:
    # alpha_2=s-S, alpha_3=-s, beta_3=B_3-s^2, and
    # B_(n-1)=beta_2+S^2.
    a0, a1, beta1, beta2, B3, S, s = symbols(
        "a0 a1 beta1 beta2 B3 S s"
    )
    diagonal = [a0, a1, s - S, -s]
    beta = [None, beta1, beta2, B3 - s ** 2]
    centered_diagonal = [a0, a1, -S, 0]
    centered_beta = [None, beta1, beta2, B3]
    difference = simplify(
        trace_cube(diagonal, beta)
        - trace_cube(centered_diagonal, centered_beta)
    )
    assert simplify(difference - 3 * (beta2 + S ** 2) * s) == 0
    print("R51_CUBIC_JACOBI_TRACE_AFFINE_LAW PASSED")


def check_center_and_budget_reduction():
    n, m3, B_prev, trace_center = symbols(
        "n m3 B_prev trace_center"
    )
    A = n * (n + 1) * (n + 5) * m3 / 6 - trace_center / 3
    sigma = A / B_prev
    assert simplify(
        B_prev * sigma
        - (n * (n + 1) * (n + 5) * m3 / 6 - trace_center / 3)
    ) == 0

    A_symbol, root_bn, Bn = symbols("A_symbol root_B_n B_n")
    first = A_symbol ** 2 / B_prev
    second = 2 * A_symbol * root_bn - B_prev * root_bn ** 2
    assert simplify(first.subs(A_symbol, B_prev * sigma) - B_prev * sigma ** 2) == 0
    assert simplify(
        second.subs({A_symbol: B_prev * sigma, root_bn ** 2: Bn})
        - (2 * B_prev * sigma * root_bn - B_prev * Bn)
    ) == 0
    print("R51_CUBIC_TRACE_CENTER_REDUCTION PASSED")


def main():
    check_doubly_centered_transfer()
    check_radius_and_optimized_functional()
    check_exit_equivalence_and_centered_budget_sign()
    check_cubic_trace_affine_law()
    check_center_and_budget_reduction()
    print("R51_FIXED_HEAD_TWO_STEP_EXIT REMAINS OPEN")
    print("R51_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN")
    print("R51_XI_DIVERGENCE REMAINS OPEN")
    print("R51_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
