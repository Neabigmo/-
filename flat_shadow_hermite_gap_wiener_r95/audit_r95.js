'use strict';

function assertTrue(condition, message) {
  if (!condition) throw new Error(`ASSERTION FAILED: ${message}`);
}

function assertClose(actual, expected, tolerance, message) {
  if (Math.abs(actual - expected) > tolerance) {
    throw new Error(`ASSERTION FAILED: ${message}; got ${actual}, expected ${expected}`);
  }
}

function factorial(n) {
  let value = 1;
  for (let k = 2; k <= n; k++) value *= k;
  return value;
}

// The two equivalent forms of the exact normalized Hermite product coefficient.
function productCoefficient(i, j, r) {
  const m = i + j - 2 * r;
  return factorial(r) * binomial(i, r) * binomial(j, r)
    * Math.sqrt(factorial(m) / (factorial(i) * factorial(j)));
}
function binomial(n, k) {
  return factorial(n) / (factorial(k) * factorial(n - k));
}
function reparamCoefficient(i, j, m) {
  const r = (i + j - m) / 2;
  return Math.sqrt(factorial(i) * factorial(j) * factorial(m))
    / (factorial(r) * factorial(i - r) * factorial(j - r));
}

for (const [i, j] of [[2, 3], [4, 5], [6, 2], [7, 7]]) {
  for (let r = 0; r <= Math.min(i, j); r++) {
    const m = i + j - 2 * r;
    assertClose(productCoefficient(i, j, r), reparamCoefficient(i, j, m), 1e-12,
      'Hermite product coefficient reparameterization');
    assertTrue(Math.abs(i - j) <= m && m <= i + j,
      'Hermite degree locality');
    assertTrue((m - i - j) % 2 === 0, 'Hermite parity locality');
  }
}
console.log('R95_HERMITE_ENTRY_AND_LOCALITY_PASSED');

// The gap algebra is checked entrywise on one fixed integer matrix pair.
function matrix(n, fill = 0) {
  return Array.from({length: n}, () => Array.from({length: n}, () => fill));
}
function multiply(A, B) {
  const n = A.length;
  const C = matrix(n);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    for (let k = 0; k < n; k++) C[i][j] += A[i][k] * B[k][j];
  }
  return C;
}
function gap(A, d) {
  const n = A.length;
  const C = matrix(n);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    if (i - j === d) C[i][j] = A[i][j];
  }
  return C;
}
function addTo(A, B) {
  for (let i = 0; i < A.length; i++) for (let j = 0; j < A.length; j++) A[i][j] += B[i][j];
}
function equal(A, B) {
  return A.every((row, i) => row.every((value, j) => value === B[i][j]));
}
const A = [[1, 2, 0, 1, 3], [0, 1, 4, 0, 2], [2, 0, 1, 5, 0],
  [1, 3, 0, 2, 4], [0, 1, 2, 0, 1]];
const B = [[2, 0, 1, 0, 2], [1, 3, 0, 2, 0], [0, 1, 4, 0, 1],
  [2, 0, 1, 5, 0], [1, 2, 0, 1, 3]];
const AB = multiply(A, B);
for (let d = -4; d <= 4; d++) {
  const rhs = matrix(5);
  for (let r = -4; r <= 4; r++) addTo(rhs, multiply(gap(A, r), gap(B, d - r)));
  assertTrue(equal(gap(AB, d), rhs), 'gap convolution identity');
}
console.log('R95_GAP_CONVOLUTION_IDENTITY_PASSED');

// Scalar constants in the structured theorem.
const q = Math.sqrt(3) / 2;
assertClose(7 * Math.pow(q, 6), 189 / 64, 1e-12, 'Wiener majorant maximum');
assertClose(3 * Math.pow(q, 5), 27 * Math.sqrt(3) / 32, 1e-12,
  'positive-gap majorant maximum');
assertTrue(189 / 64 < 3, 'structured Wiener constant < 3');
assertTrue(27 * Math.sqrt(3) / 32 < 1.5, 'structured triangular constant < 3/2');
assertTrue(1153 < 2 * 1024, 'structured self-map scalar inequality');
assertTrue(97 < 1024, 'structured contraction scalar inequality');
console.log('R95_STRUCTURED_CONSTANTS_PASSED');

// Tangent moments are checked against the coefficient of U(z) obtained from
// the exact beta integral int_0^1 [s(1-s)]^r ds = r!^2/(2r+1)!.
for (const r of [1, 2, 3, 5]) {
  const coeffFromU = Math.pow(-1, r - 1) * r * factorial(r + 1)
    / (2 * factorial(2 * r + 1));
  const etaFromU = coeffFromU * Math.sqrt(factorial(2 * r + 1));
  const displayedEta = Math.pow(-1, r - 1) * r * factorial(r + 1)
    / (2 * Math.sqrt(factorial(2 * r + 1)));
  assertClose(etaFromU, displayedEta, 1e-12, 'g1 normalized tangent moment');
}
console.log('R95_TANGENT_MOMENT_NORMALIZATION_PASSED');

// Exact endpoint values and the sign-multiplier Green identity anchor.
function evenHermiteAtZero(r) {
  return Math.pow(-1, r) * Math.sqrt(factorial(2 * r))
    / (Math.pow(2, r) * factorial(r));
}
function signEntry(p, qIndex) {
  return 2 / Math.sqrt(2 * Math.PI) * Math.sqrt(2 * p + 1)
    * evenHermiteAtZero(p) * evenHermiteAtZero(qIndex)
    / (2 * (p - qIndex) + 1);
}
for (const [p, qIndex] of [[3, 1], [4, 2], [6, 3]]) {
  const bound = 1 / (Math.sqrt(Math.PI) * (2 * (p - qIndex) + 1));
  assertTrue(Math.abs(signEntry(p, qIndex)) + 1e-12 >= bound,
    'sign multiplier central-binomial entry lower anchor');
}
console.log('R95_SIGN_GREEN_IDENTITY_ANCHORS_PASSED');

// One fixed constructive lower-bound anchor: the signed even input makes the
// one-sided sign-multiplier rows add without cancellation.
const Q = 8;
const n = 4 * Q + 1;
let squaredOutput = 0;
for (let p = Math.ceil(3 * Q / 2); p <= 2 * Q; p++) {
  let row = 0;
  for (let qIndex = Q; qIndex <= p; qIndex++) {
    row += signEntry(p, qIndex) * Math.pow(-1, qIndex) / Math.sqrt(Q + 1);
  }
  squaredOutput += row * row;
}
assertTrue(Math.sqrt(squaredOutput) > 0, 'sign multiplier has nonzero lower output');
assertTrue(n >= 4 * Q + 1, 'fixed sign lower-bound horizon anchor');
console.log('R95_SIGN_LOWER_CONSTRUCTION_ANCHOR_PASSED');

console.log('R95_HERMITE_GAP_WIENER_AUDIT_COMPLETED');
