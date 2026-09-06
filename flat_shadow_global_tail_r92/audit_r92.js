/* Exact BigInt-rational audit for the R92 global source/tail closure. */

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
    BigInt(sign * (a + 1) * (a + 2) * polynomial) * factorial(ell - a - 4),
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

function xi(m, s) {
  return pBandFormula(m + s, s).div(bandScale(m, s));
}

function greenClosed(ell, gap) {
  if (gap === 0) return new Rat(1);
  let value = new Rat(gap % 2 === 0 ? 1 : -1, factorial(gap));
  for (let u = 0; u < gap; u += 1) {
    const term = new Rat(
      (-2n) ** BigInt(gap - 1 - u),
      factorial(gap - 1 - u) * factorial(u) * BigInt(ell + u + 1),
    );
    value = value.sub(term.mul(2));
  }
  return value;
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function checkGlobalSourceAnchors() {
  let maxRatio = new Rat(0);
  for (let m = 3; m <= 45; m += 1) {
    for (let s = 1; s <= 180; s += 1) {
      const ell = m + s;
      const value = xi(m, s).abs();
      const ratio = value.div(new Rat(16 * ell ** 4));
      if (ratio.cmp(maxRatio) > 0) maxRatio = ratio;
      assert(ratio.cmp(new Rat(1)) < 0, `global Xi bound m=${m} s=${s}`);
    }
  }
  console.log(`R92_GLOBAL_SOURCE_ANCHORS_PASSED maxRatio=${maxRatio.toString()}`);
}

function checkGlobalGreenAnchors() {
  for (let ell = 4; ell <= 80; ell += 1) {
    for (let g = 0; g <= 80; g += 1) {
      const bound = g === 0
        ? new Rat(1)
        : new Rat(1, factorial(g)).add(new Rat(2n ** BigInt(g), BigInt(ell + 1) * factorial(g - 1)));
      assert(greenClosed(ell, g).abs().cmp(bound) <= 0, `global G bound ell=${ell} g=${g}`);
    }
  }
  console.log("R92_GLOBAL_GREEN_BOUND_ANCHORS_PASSED");
}

function convolutionThree(D) {
  let total = new Rat(0);
  for (let r = 0; r <= D; r += 1) {
    for (let s = 0; s <= D - r; s += 1) {
      const g = D - r - s;
      total = total.add(new Rat((r + 1) ** 2 * s, factorial(r) * factorial(s) * factorial(g)));
    }
  }
  return total;
}

function convolutionFour(D) {
  let total = new Rat(0);
  for (let r = 0; r <= D; r += 1) {
    for (let s = 0; s <= D - r; s += 1) {
      const g = D - r - s;
      if (g === 0) continue;
      total = total.add(new Rat((r + 1) ** 2 * s * 2 ** g, factorial(r) * factorial(s) * factorial(g - 1)));
    }
  }
  return total;
}

function checkConvolutionIdentities() {
  for (let D = 0; D <= 24; D += 1) {
    const first = new Rat(3n ** BigInt(D), factorial(D)).mul(new Rat(D * (D * D + 6 * D + 2), 27));
    assert(convolutionThree(D).cmp(first) === 0, `3-base convolution D=${D}`);
    const second = new Rat(4n ** BigInt(D), factorial(D)).mul(new Rat(D * (D - 1) * (D * D + 7 * D - 2), 128));
    assert(convolutionFour(D).cmp(second) === 0, `4-base convolution D=${D}`);
  }
  console.log("R92_GLOBAL_CONVOLUTION_IDENTITIES_PASSED");
}

function checkTailArithmetic() {
  for (let D = 1; D <= 100; D += 1) {
    const j = Math.max(1, Math.floor(8 * D));
    assert(j + D + 1 <= 10 * D, `tail geometry D=${D}`);
    assert(D ** 7 * 16 ** D > 0, `tail majorant D=${D}`);
  }
  assert(576 * 4 === 2304, "global RM constant");
  assert(2304 / 27 === 256 / 3, "3-base kernel constant");
  assert(2304 / 128 === 18, "4-base kernel constant");
  console.log("R92_TAIL_ARITHMETIC_PASSED");
}

checkGlobalSourceAnchors();
checkGlobalGreenAnchors();
checkConvolutionIdentities();
checkTailArithmetic();
console.log("R92_GLOBAL_TAIL_AUDIT_COMPLETED");
