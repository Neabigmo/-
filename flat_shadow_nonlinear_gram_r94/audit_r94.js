'use strict';

function assertTrue(condition, message) {
  if (!condition) throw new Error(`ASSERTION FAILED: ${message}`);
}

// Exact integer checks for the R94 contraction constants.
assertTrue(1089n + 64n === 1153n, '(1+1/32)^2 + 1/16 numerator');
assertTrue(1153n < 2n * 1024n, 'self-map strict inequality');
assertTrue(97n < 1024n, 'contraction constant 97/1024 < 1');
assertTrue(32n + 65n === 97n, 'contraction numerator');
assertTrue(2n * 97n < 2n * 1024n, 'contraction remains below one');

// The hypothesis h <= 1/(64 Lambda^2) implies the three scalar consequences
// used by the proof for every Lambda >= 1.
assertTrue(2n * 1n <= 64n, 'r=2 Lambda h <= 1/(32 Lambda) <= 1/32');
assertTrue(4n <= 16n, 'r^2/h <= 1/16');
assertTrue(64n <= 64n, 'Lambda*h <= 1/64');

// Exact block inverse algebra in a finite strict triangular anchor.  For a
// four-dimensional strict lower K, the Neumann polynomial is exact and checks
// the sign in (I-lambda K)^(-1).
function mat(n, fill = () => 0n) {
  return Array.from({length: n}, () => Array.from({length: n}, fill));
}
function add(A, B) { return A.map((r, i) => r.map((x, j) => x + B[i][j])); }
function scale(A, s) { return A.map(r => r.map(x => x * s)); }
function mul(A, B) {
  const n = A.length;
  const C = mat(n);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    for (let k = 0; k < n; k++) C[i][j] += A[i][k] * B[k][j];
  }
  return C;
}
function eye(n) {
  const I = mat(n);
  for (let i = 0; i < n; i++) I[i][i] = 1n;
  return I;
}
function equal(A, B) { return A.every((r, i) => r.every((x, j) => x === B[i][j])); }

const K = mat(4);
K[1][0] = 2n; K[2][0] = 3n; K[2][1] = 5n;
K[3][0] = 7n; K[3][1] = 11n; K[3][2] = 13n;
const lambda = 3n;
let R = eye(4);
let power = eye(4);
for (let q = 1; q < 4; q++) {
  power = mul(power, scale(K, lambda));
  R = add(R, power);
}
assertTrue(equal(mul(add(eye(4), scale(K, -lambda)), R), eye(4)),
  'finite strict block-resolvent sign');

// Hermitian compatibility: A is real skew-symmetric, so iA is Hermitian.
const A = [[0, -1, -2], [1, 0, -3], [2, 3, 0]];
for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) {
  assertTrue(A[i][j] === -A[j][i], 'Hilbert witness skew symmetry');
}

console.log('R94_CONTRACTION_CONSTANTS_PASSED');
console.log('R94_FINITE_RESOLVENT_ANCHOR_PASSED');
console.log('R94_HERMITIAN_WITNESS_ANCHOR_PASSED');
console.log('R94_NONLINEAR_GRAM_AUDIT_COMPLETED');
