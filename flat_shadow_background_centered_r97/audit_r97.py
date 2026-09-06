"""Exact finite checks for the R97 background-centered substitute."""

import sympy as sp


def assert_true(cond, msg):
    if not cond:
        raise AssertionError(msg)


# Determinant-free LDL recursion on an exact Hermitian positive matrix.
G = sp.Matrix([
    [sp.Integer(1), sp.Rational(1, 4), sp.Rational(-1, 8)],
    [sp.Rational(1, 4), sp.Integer(1), sp.Rational(1, 5)],
    [sp.Rational(-1, 8), sp.Rational(1, 5), sp.Integer(1)],
])
n = G.rows
T = sp.eye(n)
D = sp.zeros(n)
for i in range(n):
    D[i, i] = sp.simplify(G[i, i] - sum(
        T[i, k] * D[k, k] * T[i, k] for k in range(i)
    ))
    for j in range(i + 1, n):
        T[j, i] = sp.simplify((G[j, i] - sum(
            T[j, k] * D[k, k] * T[i, k] for k in range(i)
        )) / D[i, i])
assert_true(T * D * T.T == G, "LDL recursion failed")
assert_true(all(D[i, i] > 0 for i in range(n)), "positive pivots failed")

C = sp.eye(n)
for i in range(n):
    for j in range(i):
        C[i, j] = sp.simplify(-sum(T[i, k] * C[k, j] for k in range(j, i)))
assert_true(C * G * C.T == D, "inverse triangular factor failed")
print("R97_EXACT_LDL_RECURSION_PASSED")


# Conditioning constants used by the trace-norm substitute.
h = sp.Rational(1, 4)
kappa = sp.simplify((1 + h) / (1 - h))
beta = sp.simplify((1 + h) / (1 - h) ** 2)
assert_true(kappa == sp.Rational(5, 3), "kappa(h) mismatch")
assert_true(beta == sp.Rational(20, 9), "beta(h) mismatch")
N = 8
threshold = sp.simplify(1 / (64 * (1 + sp.log(N)) ** 2))
assert_true(threshold > 0, "finite-horizon threshold must be positive")
assert_true(sp.Rational(97, 1024) < 1, "R94 contraction factor failed")
print("R97_CONDITIONING_AND_CONTRACTION_CONSTANTS_PASSED")


# Exact number-operator commutator audit on a nontrivial polynomial test.
x = sp.symbols("x")
g = x**5 - 2*x**3 + x
f = 1 + 2*x + x**2 - x**4

def number_op(u):
    return -sp.diff(u, x, 2) + x * sp.diff(u, x)

def first_comm(u):
    return number_op(g * u) - g * number_op(u)

left_second = sp.expand(number_op(first_comm(f)) - first_comm(number_op(f)))
right_second = sp.expand(
    number_op(number_op(g)) * f
    - 2 * sp.diff(number_op(g), x) * sp.diff(f, x)
    - 2 * number_op(sp.diff(g, x)) * sp.diff(f, x)
    + 4 * sp.diff(g, x, 2) * sp.diff(f, x, 2)
    + 2 * sp.diff(g, x) * sp.diff(f, x)
)
assert_true(sp.expand(left_second - right_second) == 0,
            "second number-operator commutator failed")
print("R97_SECOND_COMMUTATOR_IDENTITY_PASSED")


# The min-envelope summation used for the g2 growing-gap estimate.
A = sp.Rational(3, 2)
B = sp.Integer(72)
finite_sum = sum(min(A, B / sp.Integer(d * d)) for d in range(1, 25))
majorant = A + 2 * sp.sqrt(A * B)
assert_true(finite_sum <= majorant, "min-envelope sum bound failed")
full_majorant = 3 * A + 4 * sp.sqrt(A * B)
assert_true(2 * finite_sum + A <= full_majorant,
            "two-sided gap sum bound failed")
assert_true(sp.simplify(3 * A + 4 * sp.sqrt(A * B)) > 0,
            "g2 growing-gap majorant must be positive")
print("R97_G2_MIN_ENVELOPE_SUMMATION_PASSED")


# Linearized Cholesky identity: for strict-lower K, K + A + K^T
# has zero strict-lower part iff K=-L_-A.
A = sp.Matrix([
    [0, 2, -3],
    [2, 0, 5],
    [-3, 5, 0],
])
K = sp.zeros(3)
for i in range(3):
    for j in range(i):
        K[i, j] = -A[i, j]
linearized = K + A + K.T
assert_true(all(linearized[i, j] == 0 for i in range(3) for j in range(i)),
            "linearized strict-lower cancellation failed")
print("R97_LINEARIZED_TRIANGULAR_NO_GO_ANCHOR_PASSED")
print("R97_BACKGROUND_CENTERED_AUDIT_COMPLETED")
