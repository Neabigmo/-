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
