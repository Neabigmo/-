# R55 — finite skew head, eventual zero tail, and the factorial-escape target

R55 was a continuation in the same ChatGPT Project conversation after the
R53 canonical-tail record.  It asked for an exact finite Jacobi-head plus
eventual symmetric-tail analysis, and for a proof or refutation of a proposed
factorial-growth obstruction.

## What R55 established

For the monic recurrence

```text
x*pi_n = pi_(n+1) + alpha_n*pi_n + beta_n*pi_(n-1),
```

with centered variance one (`alpha_0=0`, `beta_1=1`), the finite head

```text
alpha_0=0, alpha_1=a, alpha_2=-a, alpha_n=0 (n>=3),
beta_n=1,
```

has

```text
m_1=0, m_2=1, m_3=a, m_4=2+a^2.
```

Thus `a != 0` preserves a nonzero third moment even though the Jacobi
diagonal is eventually zero.  The choice `a=1/2` gives `m_4=9/4 != 3`, so it
fails the second full-exact cubic row.  This is not a counterexample to the
project's full-exact problem; it is a precise obstruction to the inference

```text
eventually zero Jacobi diagonal  ==>  original law symmetric.
```

The all-`beta_n=1` infinite chain is a bounded positive Jacobi/Favard control
example with a compactly supported representing law.  It only demonstrates
that positivity plus an eventually symmetric tail is insufficient by itself;
it does not satisfy all `G_n=0` rows.

## Exact tail decomposition

For the symmetric Jacobi resolvent convention

```text
m_k(z) = 1 / (z - alpha_k - beta_(k+1)*m_(k+1)(z)),
```

any finite positive Jacobi head is an iterated linear-fractional (Mobius)
map of the tail m-function.  Its derivative with respect to the tail is a
nonzero rational function whenever the intervening `beta`s are positive.
Therefore a symmetric associated tail does not erase the finite-head skew
coupling.  The first target that could still do so is the entire full-exact
moment system, not eventual diagonal vanishing alone.

## The factorial-envelope correction

R55 proposed that a nonzero finite-head skew might force

```text
limsup (1/n)*log(n!/h_n) = +infinity.
```

This is not equivalent to failure of the R12-type envelope

```text
h_n <= C*A^n*n!  for some finite C,A.
```

For positive `h_n`, the correct root-test equivalence is

```text
there exist finite C,A with h_n <= C*A^n*n!
  <=>  limsup (h_n/n!)^(1/n) < infinity,
```

or, in logarithmic form, failure of the envelope requires

```text
limsup (1/n)*log(h_n/n!) = +infinity,
```

equivalently `liminf (1/n)*log(n!/h_n)=-infinity`.  A positive limsup of the
reversed logarithm can occur even for a sequence with a valid envelope, so it
cannot be used as the contradiction without further lower-growth information.

## Global implications and evidence boundary

The exact dichotomy remains:

1. If the canonical centered branch reaches `B_n<=0`, this proves the D.1
   finite-exit target for that fixed head.
2. If every `B_n>0`, Favard/Hamburger yields a genuine positive full-exact
   candidate with an eventually zero Jacobi diagonal.  R55 shows that this
   candidate need not be symmetric merely from its tail shape.
3. A theorem `mu in E and alpha_n=0 eventually => m_3(mu)=0` would still imply
   D.1 against the bounded-X R47 head, but R55 does not prove it.
4. The `P_3 K` bridge is independent: D.1 or eventual skew annihilation does
   not by itself identify the Gaussian law or prove `P_3 K=0`.

The proposed next lemma is therefore a genuine open target:

```text
R56 — Skew-Forced Factorial Escape Lemma.
```

It must either derive a valid invariant from the full-exact recurrence and
the factorial norm envelope, or identify the weakest additional tail-transfer
condition under which such an implication is true.  No genuine full-exact
non-Gaussian counterexample was found in R55.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_skew_forced_escape_r55\audit_r55.py
```

The local audit checks the moments, the nonconstant Mobius tail coupling, the
correct envelope logic, and the conditional deficit sign.  It explicitly
leaves skew-forced escape, D.1, Gaussian rigidity, and the `P_3 K` bridge open.
