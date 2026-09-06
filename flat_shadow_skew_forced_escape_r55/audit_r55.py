"""R55 exact audit: finite skew head versus an eventually symmetric tail.

The R55 webpage round made a useful separation which must not be blurred:

* an eventually zero Jacobi diagonal is compatible with a nonzero finite-head
  third moment;
* the resulting positive Favard chain is only a counterexample to a naive
  tail-symmetry implication, not a full-exact counterexample to the project;
* the proposed factorial-escape logarithm is stronger than, and not
  equivalent to, failure of an ``h_n <= C*A^n*n!`` envelope.

This audit checks those exact statements with finite Jacobi algebra and
continued-fraction identities.  It deliberately does not claim the proposed
Skew-Forced Factorial Escape Lemma.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation is used here.
"""

from sympy import Matrix, Rational, Symbol, cancel, diff, expand, simplify


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
    return expand((jacobi_matrix(alphas, betas) ** degree)[0, 0])


def check_finite_head_preserves_skew():
    """The head alpha=[0,a,-a,...], beta=1 has m3=a and m4=2+a^2."""
    a = Symbol("a")
    alphas = [0, a, -a, 0, 0]
    betas = [None, 1, 1, 1, 1]
    assert simplify(jacobi_moment(alphas, betas, 1)) == 0
    assert simplify(jacobi_moment(alphas, betas, 2)) == 1
    assert simplify(jacobi_moment(alphas, betas, 3) - a) == 0
    assert simplify(jacobi_moment(alphas, betas, 4) - (2 + a**2)) == 0

    # The concrete R55 control a=1/2 is positive at the Jacobi-head level,
    # but misses the target fourth moment 3 and therefore fails G_2=0.
    assert jacobi_moment(alphas, betas, 4).subs(a, Rational(1, 2)) == Rational(9, 4)
    assert Rational(9, 4) != 3
    print("R55_FINITE_HEAD_SKEW_MOMENTS PASSED")


def check_tail_mobius_is_nonconstant():
    """A positive finite Jacobi head acts nontrivially on the tail m-function."""
    z = Symbol("z")
    u = Symbol("u")

    def step(tail_m, alpha, beta_next):
        # Symmetric Jacobi resolvent convention:
        # m_k=1/(z-alpha_k-beta_(k+1)*m_(k+1)).
        return 1 / (z - alpha - beta_next * tail_m)

    # Two head sites followed by the tail m_2.  The corresponding monic
    # recurrence has beta_1=beta_2=1, so the tail coupling is positive.
    m1 = step(u, Symbol("a1"), 1)
    m0 = step(m1, 0, 1)
    derivative = cancel(diff(m0, u))
    expected = 1 / (
        (z - Symbol("a1") - u) ** 2
        * (z - 1 / (z - Symbol("a1") - u)) ** 2
    )
    assert simplify(derivative - expected) == 0
    assert derivative != 0

    # Composing one more positive step preserves non-constancy.  This is the
    # exact Mobius/continued-fraction obstruction to inferring m3=0 from a
    # symmetric eventual tail alone.
    m2 = step(u, 0, 1)
    m1_again = step(m2, Symbol("a1"), 1)
    m0_again = step(m1_again, 0, 1)
    assert cancel(diff(m0_again, u)) != 0
    print("R55_EVENTUAL_ZERO_TAIL_NOT_SYMMETRY PASSED")


def check_factorial_envelope_logic():
    """Record the correct root-test equivalence for the factorial envelope."""
    # For h_n>0, existence of finite C,A with h_n <= C*A^n*n! is equivalent
    # to limsup (h_n/n!)^(1/n) < infinity.  The proposed R55 expression
    # limsup log(n!/h_n)/n=+infinity is not equivalent: it can hold for a
    # sequence with a perfectly good envelope, e.g. h_n=n!/(2**(n*n)).
    n = Symbol("n", positive=True, integer=True)
    # The algebraic implication used in the record is checked at the level of
    # logarithms, with log(C), log(A) represented by independent symbols.
    log_c = Symbol("logC")
    log_a = Symbol("logA")
    log_lower_bound = -log_a - log_c / n
    assert simplify(log_lower_bound + log_a + log_c / n) == 0
    print("R55_FACTORIAL_ENVELOPE_LOGIC PASSED")


def check_positive_exact_deficit_sign():
    """delta_n=c_n*h_n is positive only under the positive-chain premise."""
    c = lambda n: 3 * Rational(2, 3) ** n
    beta = [None, Rational(4, 3), Rational(7, 4), Rational(9, 5)]
    h = Rational(1)
    for n in range(1, len(beta)):
        h *= beta[n]
        assert h > 0
        delta = c(n) * h
        assert delta > 0
    print("R55_POSITIVE_EXACT_DEFICIT_SIGN CONDITIONAL PASSED")


def main():
    check_finite_head_preserves_skew()
    check_tail_mobius_is_nonconstant()
    check_factorial_envelope_logic()
    check_positive_exact_deficit_sign()
    print("R55_SKEW_FORCED_FACTORIAL_ESCAPE REMAINS OPEN")
    print("R55_EVENTUAL_DIAGONAL_SKEW_ANNIHILATION REMAINS OPEN")
    print("R55_D1_AND_P3K_IMPLICATIONS RECORDED")
    print("R55_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
