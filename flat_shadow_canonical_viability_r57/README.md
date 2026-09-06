# R57 — canonical viability replaces factorial escape

R57 was a continuation in the same ChatGPT Project conversation after the
R56 correction.  It produced the first useful route change in this segment:
an all-positive canonical exact branch already satisfies an upper factorial
envelope, so a nonzero finite-head skew cannot be forced out by “growth too
fast”.  The remaining question is a genuine finite sign exit versus an
infinite positive exact chain.

## Exact all-positive upper bound

On a positive `n`-point product Gauss rule, `Q_n>=0`.  If

```text
delta_n = 2^n*n! - E[Q_n]
```

and the exact canonical row gives

```text
delta_n = c_n*h_n,   c_n=3*(2/3)^n,
```

then every positive step has

```text
0 < delta_n <= 2^n*n!,
0 < h_n <= 3^(n-1)*n!.
```

Therefore the proposed factorial-escape route is impossible on any branch
that remains positive.  This is stronger than the R12 upper envelope and
does not use a lower-growth argument.

The exact dichotomy is now

```text
finite sign exit: delta_n<=0 (equivalently beta_n<=0),
or infinite positive exact viability: delta_n>0 for every n.
```

The second alternative is not a finite-prefix counterexample: Favard/Hamburger
would promote it to a genuine positive full-exact law, subject to the usual
moment determinacy and backward-OU requirements.

## A finite-stage skew family

Put `a=m_3`, with centered variance one, and impose the canonical controls
`alpha_2=-a` and `alpha_n=0` for `n>=3`.  The first exact rows give

```text
m_4=3,   m_5=4a,   m_6=15+7a^2,
m_7=15a, m_8=105+4a^2,
m_9=a*(96-112a^2-49a^4)/(2-a^2),
m_10=945-234a^2.
```

The associated monic polynomials begin

```text
pi_2=x^2-a*x-1,
pi_3=x^3-3*x-a,
```

and the exact norms are

```text
h_2=2-a^2,
h_3=6*(1+a^2).
```

With the convention used throughout the project,

```text
beta_n=h_n/h_(n-1),
```

so in particular

```text
beta_2=2-a^2,
beta_3=6*(1+a^2)/(2-a^2).
```

The browser's flattened fraction display made the orientation of later beta
fractions easy to misread; the local audit recomputes `beta_4=h_4/h_3` and
`beta_5=h_5/h_4` directly.  At `a=1/10`, all of `beta_2,...,beta_5` are
strictly positive.  Thus nonzero skew is not automatically killed by the
first five exact/canonical levels.  This is only a finite-stage family, not a
full-exact counterexample, because positivity for `beta_6,beta_7,...` is not
proved.

## Backward-OU positivity gives a different bound

If `mu=P_lambda nu`, `0<lambda<1`, write

```text
X=sqrt(lambda)*Y + sqrt(1-lambda)*Z,
```

with `Z` standard Gaussian.  For every monic degree-`n` polynomial, the
conditional polynomial in `Z` has leading coefficient
`(1-lambda)^(n/2)`.  Orthogonality of Gaussian Hermites gives

```text
h_n(mu) >= (1-lambda)^n*n!.
```

At the second exact row, `h_2=2-m_3^2`, hence

```text
m_3^2 <= 2*lambda*(2-lambda).
```

Consequently, arbitrarily deep positive OU divisibility (`lambda_j -> 0`)
forces `m_3=0`, even without eventual zero diagonal or all higher exact rows.
For a fixed-factor infinite compatible backward tower, the base point has
arbitrarily small `lambda`, so this conditional skew-annihilation lemma is
available.  It does not by itself prove D.1 for a single eventual-zero tail,
and it does not close Gaussian rigidity or the `P_3 K` bridge.

## Global status and next target

R57 rules out the factorial-growth version of R56 and makes the global choice
cleaner:

```text
canonical D.1  <=>  prove finite sign exit for the moving deficit,
```

unless one can construct an all-positive infinite exact chain.  The next
target is therefore a viability/zero-set theorem for the one-parameter (or
finite-head) deficit sequence, not another growth estimate:

```text
for surviving 0<a^2<32-12*sqrt(7), does delta_n(a) change sign at finite n?
```

The interval displayed is the first nontrivial sign window from the webpage
calculation; its global exhaustion is still OPEN.  Any future use of the OU
bound must distinguish “deep backward divisibility forces `m_3=0`” from the
separate eventual-diagonal problem.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_canonical_viability_r57\audit_r57.py
```

The audit checks the finite moments, Jacobi beta orientation, finite-stage
positivity, the positive-branch upper envelope, and the OU norm inequality.
