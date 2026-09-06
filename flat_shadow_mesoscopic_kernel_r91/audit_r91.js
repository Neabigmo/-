/* Exact BigInt-rational audit for the R91 mesoscopic closure. */

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

function rootFilterRatio(r, j) {
  const p = 2 * r + 1;
  const q = 2 * j + 1;
  const center = j + r + 1;
  let numerator = 0n;
  for (let a = 0; a <= p; a += 1) {
    if ((p - 2 * a) % 3 !== 0) continue;
    const chosen = center - a;
    if (0 <= chosen && chosen <= q) numerator += binomial(p, a) * binomial(q, chosen);
  }
  return new Rat(3n * numerator, binomial(p + q, center));
}

function angularB(r, j) {
  return rootFilterRatio(r, j).sub(1).div(2);
}

function angularM(j, r) {
  const c = new Rat(factorial(j) ** 2n, factorial(2 * j + 1));
  const sign = r % 2 === 1 ? 1 : -1;
  const upsilon = new Rat(BigInt(sign * r) * factorial(r + 1), 2n * factorial(2 * r + 1));
  return c.mul(upsilon).mul(angularB(r, j));
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

function checkCentralBinomialInduction() {
  for (let k = 1; k <= 120; k += 1) {
    const left = binomial(2 * k, k) ** 2n * BigInt(4 * k);
    const right = 16n ** BigInt(k);
    assert(left >= right, `central lower bound k=${k}`);
    const ratioSquaredLeft = BigInt((2 * k + 1) ** 2);
    const ratioSquaredRight = BigInt(4 * k * (k + 1));
    assert(ratioSquaredLeft >= ratioSquaredRight, `induction step k=${k}`);
  }
  console.log("R91_CENTRAL_BINOMIAL_INDUCTION_PASSED");
}

function checkAngularBounds() {
  for (let j = 1; j <= 100; j += 1) {
    const c = new Rat(factorial(j) ** 2n, factorial(2 * j + 1));
    const cBoundSquared = new Rat(1, 4n ** BigInt(2 * j) * BigInt(j));
    assert(c.mul(c).cmp(cBoundSquared) <= 0, `c bound j=${j}`);
    for (let r = 1; r <= 100; r += 1) {
      const rho = rootFilterRatio(r, j);
      assert(rho.cmp(new Rat(0)) >= 0 && rho.cmp(new Rat(3)) <= 0, `rho range j=${j} r=${r}`);
      assert(angularB(r, j).abs().cmp(new Rat(1)) <= 0, `B bound j=${j} r=${r}`);
      const rhsSquared = new Rat(
        BigInt((r + 1) ** 4),
        4n ** BigInt(2 * (j + r)) * BigInt(j) * factorial(r) ** 2n,
      );
      assert(angularM(j, r).abs().mul(angularM(j, r).abs()).cmp(rhsSquared) <= 0, `M bound j=${j} r=${r}`);
    }
  }
  console.log("R91_ANGULAR_MAJORANT_ANCHORS_PASSED");
}

function checkGreenWindow() {
  for (let j = 16; j <= 200; j += 1) {
    for (let D = 0; D <= Math.floor(j / 8); D += 1) {
      for (let r = 1; r <= D; r += 1) {
        for (let s = 1; s <= D - r; s += 1) {
          const g = D - r - s;
          const ell = j + r + s + 1;
          const bound = new Rat(9, 7n * factorial(g));
          assert(greenClosed(ell, g).abs().cmp(bound) <= 0, `G bound j=${j} D=${D} r=${r} s=${s}`);
        }
      }
    }
  }
  console.log("R91_GREEN_WINDOW_BOUND_PASSED");
}

function convolutionSum(D) {
  let total = new Rat(0);
  for (let r = 0; r <= D; r += 1) {
    for (let s = 0; s <= D - r; s += 1) {
      const g = D - r - s;
      total = total.add(new Rat((r + 1) ** 2 * s, factorial(r) * factorial(s) * factorial(g)));
    }
  }
  return total;
}

function checkConvolutionIdentity() {
  for (let D = 0; D <= 24; D += 1) {
    const rhs = new Rat(3n ** BigInt(D), factorial(D)).mul(new Rat(D * (D * D + 6 * D + 2), 27));
    assert(convolutionSum(D).cmp(rhs) === 0, `convolution identity D=${D}`);
  }
  assert(1008 * 4 * 9 / 7 === 5184, "single-path constant");
  assert(5184 / 27 === 192, "convolution constant");
  assert(768 * 3132 === 2405376, "weighted column constant");
  console.log("R91_CONVOLUTION_IDENTITY_AND_CONSTANTS_PASSED");
}

checkCentralBinomialInduction();
checkAngularBounds();
checkGreenWindow();
checkConvolutionIdentity();
console.log("R91_MESOSCOPIC_KERNEL_AUDIT_COMPLETED");
