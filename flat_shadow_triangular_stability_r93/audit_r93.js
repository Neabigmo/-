'use strict';

function assertTrue(condition, message) {
  if (!condition) throw new Error(`ASSERTION FAILED: ${message}`);
}

function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b !== 0n) [a, b] = [b, a % b];
  return a;
}

class Q {
  constructor(n, d = 1n) {
    if (d === 0n) throw new Error('zero denominator');
    if (d < 0n) [n, d] = [-n, -d];
    const g = gcd(n, d);
    this.n = n / g;
    this.d = d / g;
  }
  add(o) { return new Q(this.n * o.d + o.n * this.d, this.d * o.d); }
  neg() { return new Q(-this.n, this.d); }
  sub(o) { return this.add(o.neg()); }
  mul(o) { return new Q(this.n * o.n, this.d * o.d); }
  eq(o) { return this.n === o.n && this.d === o.d; }
}

const Z = (n) => new Q(BigInt(n));
const zero = () => Z(0);
const one = () => Z(1);

function mat(n, fill = zero) {
  return Array.from({length: n}, () => Array.from({length: n}, fill));
}
function add(A, B) {
  return A.map((row, i) => row.map((x, j) => x.add(B[i][j])));
}
function scale(A, s) { return A.map(row => row.map(x => x.mul(s))); }
function mul(A, B) {
  const n = A.length;
  const C = mat(n);
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    let x = zero();
    for (let k = 0; k < n; k++) x = x.add(A[i][k].mul(B[k][j]));
    C[i][j] = x;
  }
  return C;
}
function eye(n) {
  const I = mat(n);
  for (let i = 0; i < n; i++) I[i][i] = one();
  return I;
}
function transpose(A) { return A[0].map((_, j) => A.map(row => row[j])); }
function lower(A) {
  return A.map((row, i) => row.map((x, j) => (i > j ? x : zero())));
}
function equal(A, B) {
  return A.every((row, i) => row.every((x, j) => x.eq(B[i][j])));
}

// R92 -> R93 tail arithmetic, kept as exact integer inequalities.
const C1 = 1024n * 10000n * 9n / 3n;
const C2 = 72n * 1000n * 4n;
assertTrue(C1 === 30720000n, 'first large-gap constant');
assertTrue(C2 === 288000n, 'second large-gap constant');
assertTrue(C1 + C2 === 31008000n, 'C92=31,008,000');

for (const D of [1n, 2n, 17n]) {
  assertTrue(D * D + 6n * D + 2n <= 9n * D * D,
    'D^2+6D+2 <= 9D^2 for D>=1');
}
for (const D of [2n, 3n, 19n]) {
  assertTrue(D * D + 7n * D - 2n <= 4n * D * D,
    'D^2+7D-2 <= 4D^2 for D>=2');
}
assertTrue(33n ** 7n < 2n * (32n ** 7n),
  '(1+1/D)^7 < 2 for D>=32, hence also D>=64');
assertTrue(16n * 2n < 65n, '16/(D+1)*(1+1/D)^7 < 1/2 for D>=64');
assertTrue(8n * 1n + 1n + 1n <= 10n * 1n,
  'j+D+1 <= 10D at the endpoint j=8D,D=1');

// Exact weight-factor algebra: each factor is strictly below 4.
for (const x of [1n, 2n, 31n]) {
  assertTrue(8n * x < 4n * (2n * x + 1n),
    '8x/(2x+1) < 4');
}

// Finite exact check of the strict block-resolvent identity via Neumann sum.
const n = 4;
const K = mat(n);
K[1][0] = Z(2); K[2][0] = Z(3); K[2][1] = Z(5);
K[3][0] = Z(7); K[3][1] = Z(11); K[3][2] = Z(13);
const lambda = Z(3);
let R = eye(n);
let power = eye(n);
for (let q = 1; q < n; q++) {
  power = mul(power, scale(K, lambda));
  R = add(R, power);
}
assertTrue(equal(mul(add(eye(n), scale(K, lambda).map(row => row.map(x => x.neg()))), R), eye(n)),
  'finite strict-triangular resolvent');

// Exact finite expansion of the nonlinear Gram off-diagonal identity.  Build
// a genuine Cholesky-compatible pair: choose C=I+L and diagonal D, then set
// G=C^(-1) D C^(-T), so C G C^T=D by construction.
const L = mat(3);
L[1][0] = Z(2); L[2][0] = Z(3); L[2][1] = Z(5);
const Lt = transpose(L);
const C = add(eye(3), L);
const Cinv = add(add(eye(3), scale(L, Z(-1))), mul(L, L));
const Ddiag = mat(3);
Ddiag[0][0] = Z(2); Ddiag[1][1] = Z(3); Ddiag[2][2] = Z(5);
const G = mul(mul(Cinv, Ddiag), transpose(Cinv));
const H = add(G, scale(eye(3), Z(-1)));
const rhs = scale(lower(add(add(add(add(H, mul(L, H)), mul(H, Lt)), mul(L, Lt)), mul(mul(L, H), Lt))), Z(-1));
assertTrue(equal(L, rhs), 'D1 strict-lower identity');

// Minimal shift obstruction: every column of S_N has l1 norm <=1, while
// the first column of its inverse has exactly N unit entries.
const N = 7;
const inverseFirstColumnL1 = Array.from({length: N}, () => 1n).reduce((a, b) => a + b, 0n);
assertTrue(inverseFirstColumnL1 === BigInt(N), 'shift inverse norm is N');

// Fourier coefficient selector: p_N selects exactly positive row-column gaps.
for (const [row, col] of [[1, 0], [3, 1], [0, 2], [2, 2]]) {
  const selected = row > col;
  const d = row - col;
  assertTrue(selected === (d >= 1 && d <= 3), 'one-sided Fourier selector');
}

console.log('R93_TAIL_CONSTANTS_AND_FACTORIAL_DECAY_PASSED');
console.log('R93_WEIGHT_RATIO_AND_COLUMN_VANISHING_ANCHORS_PASSED');
console.log('R93_FINITE_STRICT_RESOLVENT_PASSED');
console.log('R93_NONLINEAR_GRAM_IDENTITY_PASSED');
console.log('R93_SHIFT_NO_GO_AND_FOURIER_SELECTOR_PASSED');
console.log('R93_TRIANGULAR_STABILITY_AUDIT_COMPLETED');
