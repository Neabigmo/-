/* Exact BigInt-rational audit for the corrected R90 source theorem. */

class Rat {
  constructor(n, d = 1n) {
    if (n instanceof Rat) {
      this.n = n.n;
      this.d = n.d;
      return;
    }
    if (typeof n === "number") n = BigInt(n);
    if (typeof d === "number") d = BigInt(d);
    if (d < 0n) {
      n = -n;
      d = -d;
    }
    const g = gcd(n < 0n ? -n : n, d);
    this.n = n / g;
    this.d = d / g;
  }

  add(other) {
    other = asRat(other);
    return new Rat(this.n * other.d + other.n * this.d, this.d * other.d);
  }

  sub(other) {
    other = asRat(other);
    return new Rat(this.n * other.d - other.n * this.d, this.d * other.d);
  }

  mul(other) {
    other = asRat(other);
    return new Rat(this.n * other.n, this.d * other.d);
  }

  div(other) {
    other = asRat(other);
    return new Rat(this.n * other.d, this.d * other.n);
  }

  abs() {
    return new Rat(this.n < 0n ? -this.n : this.n, this.d);
  }

  cmp(other) {
    other = asRat(other);
    const left = this.n * other.d;
    const right = other.n * this.d;
    return left < right ? -1 : left > right ? 1 : 0;
  }

  toString() {
    return `${this.n}/${this.d}`;
  }
}

function asRat(value) {
  return value instanceof Rat ? value : new Rat(value);
}

function gcd(a, b) {
  while (b !== 0n) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a === 0n ? 1n : a;
}

const factorialCache = [1n];
function factorial(n) {
  for (let k = factorialCache.length; k <= n; k += 1) {
    factorialCache[k] = factorialCache[k - 1] * BigInt(k);
  }
  return factorialCache[n];
}

function binomial(n, k) {
  if (k < 0 || k > n) return 0n;
  return factorial(n) / (factorial(k) * factorial(n - k));
}

function qBandCoefficient(ell, a) {
  const sign = a % 2 === 0 ? -1 : 1;
  const polynomial = a * a + 5 * a - 2 * (ell - 3);
  return new Rat(
    BigInt(sign * (a + 1) * (a + 2) * polynomial) *
      factorial(ell - a - 4),
    2n * factorial(ell - 3 - 2 * a),
  );
}

function pBandFormula(ell, s) {
  let first = new Rat(0);
  for (let a = 0; a < s; a += 1) {
    if (ell - 3 - 2 * a < 0 || ell - a - 4 < 0) continue;
    first = first.add(
      qBandCoefficient(ell, a)
        .mul(factorial(s - a - 1))
        .mul(binomial(ell + 1, s - a - 1))
        .mul(binomial(ell - 3 - 2 * a, s - a - 1)),
    );
  }

  let second = new Rat(0);
  for (let a = 0; a < s - 1; a += 1) {
    if (ell - 4 - 2 * a < 0 || ell - a - 5 < 0) continue;
    second = second.add(
      qBandCoefficient(ell - 1, a)
        .mul(ell)
        .mul(factorial(s - a - 2))
        .mul(binomial(ell, s - a - 2))
        .mul(binomial(ell - 4 - 2 * a, s - a - 2)),
    );
  }
  return first.sub(second);
}

function bandScale(m, s) {
  const ell = m + s;
  return 2n * factorial(s - 1) * binomial(ell + 1, s - 1) * binomial(ell - 3, s - 1);
}

function directNormalizedTerm(m, s, a, kind) {
  const ell = m + s;
  const T = bandScale(m, s);
  if (kind === "A") {
    if (a > s - 1 || ell - 3 - 2 * a < 0 || ell - a - 4 < 0) return new Rat(0);
    return qBandCoefficient(ell, a)
      .mul(factorial(s - a - 1))
      .mul(binomial(ell + 1, s - a - 1))
      .mul(binomial(ell - 3 - 2 * a, s - a - 1))
      .div(T);
  }
  if (a > s - 2 || ell - 4 - 2 * a < 0 || ell - a - 5 < 0) return new Rat(0);
  return qBandCoefficient(ell - 1, a)
    .mul(ell)
    .mul(factorial(s - a - 2))
    .mul(binomial(ell, s - a - 2))
    .mul(binomial(ell - 4 - 2 * a, s - a - 2))
    .div(T);
}

function correctedTerm(m, s, a, kind) {
  const ell = m + s;
  if (kind === "A") {
    if (a > s - 1 || ell - 3 - 2 * a < 0 || ell - a - 4 < 0) return new Rat(0);
    return new Rat((a % 2 === 0 ? -1 : 1) * (a + 1) * (a + 2), 4)
      .mul(a * a + 5 * a - 2 * ell + 6)
      .mul(new Rat(factorial(ell - a - 4), factorial(ell - 3)))
      .mul(new Rat(factorial(s - 1), factorial(s - a - 1)))
      .mul(new Rat(factorial(m + 2), factorial(m + a + 2)))
      .mul(new Rat(factorial(m - 2), factorial(m - a - 2)));
  }
  if (a > s - 2 || ell - 4 - 2 * a < 0 || ell - a - 5 < 0) return new Rat(0);
  return new Rat((a % 2 === 0 ? -1 : 1) * (a + 1) * (a + 2), 4)
    .mul(a * a + 5 * a - 2 * ell + 8)
    .mul(new Rat(ell, ell + 1))
    .mul(new Rat(factorial(ell - a - 5), factorial(ell - 3)))
    .mul(new Rat(factorial(s - 1), factorial(s - a - 2)))
    .mul(new Rat(factorial(m + 2), factorial(m + a + 2)))
    .mul(new Rat(factorial(m - 2), factorial(m - a - 2)));
}

function xi(m, s) {
  let value = new Rat(0);
  for (let a = 0; a < s; a += 1) {
    value = value.add(directNormalizedTerm(m, s, a, "A"));
    value = value.sub(directNormalizedTerm(m, s, a, "B"));
  }
  return value;
}

function powRat(base, exponent) {
  let value = new Rat(1);
  for (let k = 0; k < exponent; k += 1) value = value.mul(base);
  return value;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function checkCorrectedClosedForms() {
  for (let m = 8; m <= 44; m += 1) {
    for (let s = 1; s <= Math.floor(m / 8); s += 1) {
      const normalized = pBandFormula(m + s, s).div(bandScale(m, s));
      let reconstructed = new Rat(0);
      for (let a = 0; a < s; a += 1) {
        const aTerm = directNormalizedTerm(m, s, a, "A");
        const bTerm = directNormalizedTerm(m, s, a, "B");
        assert(aTerm.cmp(correctedTerm(m, s, a, "A")) === 0, `A mismatch m=${m} s=${s} a=${a}`);
        assert(bTerm.cmp(correctedTerm(m, s, a, "B")) === 0, `B mismatch m=${m} s=${s} a=${a}`);
        reconstructed = reconstructed.add(aTerm).sub(bTerm);
      }
      assert(reconstructed.cmp(normalized) === 0, `Xi mismatch m=${m} s=${s}`);
    }
  }
  console.log("R90_CORRECTED_A_B_FORMS_PASSED");
}

function checkLiteralWebOrientationRejected() {
  const m = 8;
  const s = 1;
  const ell = m + s;
  const directA0 = directNormalizedTerm(m, s, 0, "A");
  const literalWebA0 = new Rat(ell - 3).mul(new Rat(factorial(ell - 3), factorial(ell - 4)));
  assert(directA0.cmp(new Rat(1)) === 0, "A0 is not normalized to one");
  assert(literalWebA0.cmp(directA0) !== 0, "literal webpage orientation was not rejected");
  const webpageP = new Rat(m + 3, m - 2);
  assert(webpageP.cmp(new Rat(1)) > 0, "webpage P contraction should fail literally");
  console.log("R90_LITERAL_WEB_FORM_REJECTED");
}

function checkUniformTermMajorants() {
  let xiMax = new Rat(0);
  for (let m = 8; m <= 220; m += 1) {
    for (let s = 1; s <= Math.floor(m / 8); s += 1) {
      const q = new Rat(s, m - 2);
      let qPower = new Rat(1);
      for (let a = 0; a < s; a += 1) {
        const aTerm = directNormalizedTerm(m, s, a, "A");
        const bTerm = directNormalizedTerm(m, s, a, "B");
        const aBound = new Rat((a + 3) ** 4, 8).mul(qPower);
        const bBound = new Rat((a + 4) ** 4, 8).mul(qPower).mul(q);
        assert(aTerm.abs().cmp(aBound) <= 0, `A majorant m=${m} s=${s} a=${a}`);
        assert(bTerm.abs().cmp(bBound) <= 0, `B majorant m=${m} s=${s} a=${a}`);
        qPower = qPower.mul(q);
      }
      const value = xi(m, s).abs();
      if (value.cmp(xiMax) > 0) xiMax = value;
      assert(value.cmp(new Rat(28)) < 0, `Xi bound m=${m} s=${s}`);
    }
  }
  console.log(`R90_UNIFORM_TERM_AND_XI_ANCHORS_PASSED maxXi=${xiMax.toString()}`);
}

function stirlingSecondKind(n, k, cache = new Map()) {
  const key = `${n},${k}`;
  if (cache.has(key)) return cache.get(key);
  if (n === 0 && k === 0) return 1;
  if (k < 1 || k > n) return 0;
  const value = stirlingSecondKind(n - 1, k - 1, cache) + k * stirlingSecondKind(n - 1, k, cache);
  cache.set(key, value);
  return value;
}

function shiftedFourthPowerSum(shift) {
  const q = new Rat(1, 6);
  const cache = new Map();
  let result = new Rat(0);
  for (let h = 0; h <= 4; h += 1) {
    const binomialCoefficient = [1, 4, 6, 4, 1][h];
    for (let k = 0; k <= h; k += 1) {
      let fallingFactorial = new Rat(1);
      for (let j = 1; j <= k; j += 1) fallingFactorial = fallingFactorial.mul(j);
      const coefficient = binomialCoefficient * shift ** (4 - h) * stirlingSecondKind(h, k, cache);
      result = result.add(
        new Rat(coefficient).mul(fallingFactorial).mul(powRat(q, k)).div(powRat(new Rat(1).sub(q), k + 1)),
      );
    }
  }
  return result;
}

function checkExactGeometricSum() {
  const total = shiftedFourthPowerSum(3).add(shiftedFourthPowerSum(4).mul(new Rat(1, 6))).div(8);
  assert(total.cmp(new Rat(681843, 25000)) === 0, `sum=${total}`);
  assert(total.cmp(new Rat(28)) < 0, "geometric majorant constant is not below 28");
  console.log(`R90_EXACT_GEOMETRIC_SUM_PASSED ${total.toString()}`);
}

function checkSourceBoundAnchors() {
  for (let m = 8; m <= 100; m += 1) {
    for (let s = 1; s <= Math.floor(m / 8); s += 1) {
      const ell = m + s;
      const p = pBandFormula(ell, s);
      const source = new Rat(-2n * factorial(2 * m), factorial(ell) ** 2n).mul(p);
      const lhsSquared = source.abs().mul(source.abs()).mul(m ** 5).mul(factorial(s - 1) ** 2n);
      const rhsSquared = new Rat(1008n ** 2n * 16n ** BigInt(m));
      assert(lhsSquared.cmp(rhsSquared) <= 0, `source bound m=${m} s=${s}`);
    }
  }
  console.log("R90_EXPLICIT_SOURCE_BOUND_ANCHORS_PASSED");
}

function checkWeightRatio() {
  for (const j of [1, 3, 7, 20, 80]) {
    for (const D of [1, 2, 4, 8]) {
      let ratio = new Rat(16n ** BigInt(D));
      for (let h = 1; h <= D; h += 1) ratio = ratio.mul(new Rat((j + h) ** 2));
      for (let h = 1; h <= 2 * D; h += 1) ratio = ratio.div(new Rat(2 * j + 1 + h));
      assert(ratio.cmp(new Rat(4n ** BigInt(D))) < 0, `weight ratio j=${j} D=${D}`);
    }
  }
  console.log("R90_WEIGHT_PRODUCT_AND_BOUND_PASSED");
}

checkCorrectedClosedForms();
checkLiteralWebOrientationRejected();
checkUniformTermMajorants();
checkExactGeometricSum();
checkSourceBoundAnchors();
checkWeightRatio();
console.log("R90_CORRECTED_SOURCE_MAJORANT_AUDIT_COMPLETED");
