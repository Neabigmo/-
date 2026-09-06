"""R56 audit: the factorial-escape gap is not closed by an upper envelope.

R56 was asked to prove or refute a skew-forced factorial escape lemma.  The
webpage response isolated the right missing implication but did not prove it,
and it repeated an invalid "or equivalently" between two growth statements.
This audit records the correction exactly and checks the already-established
conditional recurrence constants.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation is used here.
"""

from math import factorial, log
from sympy import Rational, simplify


def check_upper_envelope_does_not_give_lower_growth():
    """A valid envelope can coexist with the proposed reversed-log escape."""
    # h_n=n!/2^(n^2) satisfies h_n <= n! (C=A=1), while
    # log(n!/h_n)/n = n*log(2) tends to +infinity.
    values = []
    for n in range(1, 18):
        h = factorial(n) / (2 ** (n * n))
        assert h <= factorial(n)
        values.append(log(factorial(n) / h) / n)
    assert values[-1] > 10
    print("R56_UPPER_ENVELOPE_NOT_LOWER_GROWTH PASSED")


def check_correct_root_test_form():
    """The correct failure criterion is unbounded root growth of h_n/n!."""
    # h_n=n!*2^(n^2) has no finite C*A^n*n! envelope because its normalized
    # nth root is 2^n -> infinity; the reversed logarithm tends to -infinity.
    normalized_roots = []
    reversed_logs = []
    for n in range(1, 18):
        h = factorial(n) * (2 ** (n * n))
        normalized_roots.append((h / factorial(n)) ** (1 / n))
        reversed_logs.append(log(factorial(n) / h) / n)
    assert normalized_roots[-1] > 1000
    assert reversed_logs[-1] < -10
    print("R56_CORRECT_FACTORIAL_ROOT_TEST PASSED")


def check_canonical_deficit_constants():
    """Check delta=c*h and beta=(3/2) delta_n/delta_(n-1)."""
    c = lambda n: 3 * Rational(2, 3) ** n
    beta = [None, Rational(5, 4), Rational(7, 3), Rational(11, 5)]
    h = {0: Rational(1)}
    for n in range(1, len(beta)):
        h[n] = beta[n] * h[n - 1]
    delta = {n: c(n) * h[n] for n in h}
    for n in range(1, len(beta)):
        assert simplify(beta[n] - Rational(3, 2) * delta[n] / delta[n - 1]) == 0
        assert delta[n] > 0
    print("R56_CANONICAL_DEFICIT_CONSTANTS PASSED")


def main():
    check_upper_envelope_does_not_give_lower_growth()
    check_correct_root_test_form()
    check_canonical_deficit_constants()
    print("R56_SKEW_FORCED_FACTORIAL_ESCAPE REMAINS OPEN")
    print("R56_EVENTUAL_DIAGONAL_SKEW_ANNIHILATION REMAINS OPEN")
    print("R56_D1_GAUSSIAN_RIGIDITY_P3K BRIDGES REMAIN DISTINCT")
    print("R56_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
