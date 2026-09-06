# R53 — canonical centered tail and moving Gauss deficit

The webpage R53 round was run in the same ChatGPT Project conversation after
reading the local framework, worklog, and R36–R52 audit assets.  It did not
close the large Gaussian-rigidity problem.  Its global contribution is a
sharper all-degree reduction of the canonical centered branch.

## Global status

R11–R13, R36–R44, and R48–R52 are sufficiently self-contained to be organized
as three reportable mathematical packages, with different roles:

1. exact-class tail/OU closure and projectively compatible tower rigidity;
2. two-body Laguerre–Hoeffding carriers, fixed-head asymptotics, and
   finite-grade constraint-coupled response;
3. inverse-heat/Christoffel compression to ordinary Jacobi geometry, including
   the exact two-step budget and sharp cubic-trace rescue cone.

This is a self-containment assessment, not a checked novelty claim.  R45–R47
are best treated as the bridge between packages two and three.  The `P_3 K`
charge bridge and Gaussian rigidity remain logically separate OPEN problems.

The canonical centered-tail problem is the correct next model problem, but not
the final equivalent theorem: setting all new `S_k=0` removes the odd controls
that can provide rescue in the arbitrary-control chain.

## Exact canonical recurrence

For the monic Jacobi recurrence

```text
x*pi_n = pi_(n+1) + alpha_n*pi_n + beta_n*pi_(n-1),
h_n = ||pi_n||^2,
beta_n = h_n/h_(n-1),
S_n = sum_(j=0)^n alpha_j,
B_n = beta_n + S_(n-1)^2,
```

the full-exact factorization has the form

```text
G_n = c_n*h_(n-1)*(beta_n + S_(n-1)^2 - B_n),
c_n = 3*(2/3)^n.
```

On a canonical tail, `S_j=0` for every newly opened slot.  Hence, for every
tail index `n` after two centered slots,

```text
alpha_n = 0,
B_n = beta_n,
pi_(n+1)(x) = x*pi_n(x) - B_n*pi_(n-1)(x),
h_n = B_n*h_(n-1) = h_K*product_(j=K+1)^n B_j.
```

Finite exit is therefore exactly the first index with `B_n<=0`, provided the
preceding Jacobi block is positive.

## Gauss-quadrature deficit identity

Let `nu_(n-1)` be the spectral measure of the `n`-point Jacobi truncation.  It
matches the current moment functional through degree `2n-1`.  With

```text
q_r(n) = integral x^r d nu_(n-1)(x),
```

the monic polynomial `pi_n` vanishes at all quadrature nodes, so

```text
m_(2n) - q_(2n)(n) = h_n,
m_(2n+1) - q_(2n+1)(n) = (S_n + S_(n-1))*h_n.
```

The second formula includes the `2*S_(n-1)` contribution from the degree
`2n` error; omitting it would incorrectly replace the coefficient by
`alpha_n`.  Thus the canonical choice `S_(n-1)=S_n=0` is exactly

```text
m_(2n+1) = q_(2n+1)(n).
```

Let `delta_n` denote the target chi-square cubic-product moment defect from
the `n`-point product quadrature.  The same-factor exact row gives

```text
delta_n = c_n*h_n,
h_n = (3^(n-1) / 2^n)*delta_n,
B_n = beta_n = (3/2)*(delta_n/delta_(n-1))
```

on the canonical tail.  Consequently,

```text
B_n <= 0  <=>  delta_n <= 0
```

as long as the preceding norm is positive.  This is the cleanest R53
reformulation of D.1: does the moving product Gauss rule necessarily
overshoot the target moment at a finite stage?

## Conditional dichotomy and obstruction

If every canonical `B_n` remains positive, the monic orthogonal norms remain
positive.  Favard/Hamburger then gives a genuine positive representing law for
the full moment functional, and the exact `G_n=0` rows give the full target
chi-square moment sequence `E[Q^n]=2^n*n!`.  Since the centered tail has
eventually zero Jacobi diagonal, this is a genuine full-exact candidate, not a
finite prefix or Gateaux extractor.  It still needs a positive backward-OU
preimage to address the original rigidity problem.

The converse finite-exit claim remains OPEN:

```text
canonical centered tail reaches B_n<=0 at finite n.                 (D.1)
```

The current obstruction is precise.  Eventual zero Jacobi diagonal does not by
itself force the original measure to be symmetric: a finite Jacobi head can
retain skewness while the associated tail is symmetric.  Likewise, cubic trace
stabilization does not determine the moving quadrature deficit sign, and the
R12 square-exponential raw-tail estimate does not control the moving nodes,
weights, or inverse-Hankel conditioning.

A sufficient weaker theorem would be:

```text
mu in E and alpha_n=0 eventually  ==>  m_3(mu)=0.
```

This already contradicts the bounded-X R47 head, whose nonzero third moment is
uniformly lower-bounded.  A stronger eventual-tail-symmetry theorem would
imply Gaussianity by the exact triangular moment rows, but is not currently
available.

## Local audit and evidence boundary

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_canonical_tail_r53\audit_r53.py
```

The audit checks the Jacobi, quadrature, deficit-ratio, and cubic-stabilization
identities.  Its realization marker is explicitly conditional on all future
`beta_n>0`; it does not prove positivity of the canonical branch.  It does not
claim D.1, eventual skew annihilation, Gaussian rigidity, the `P_3 K` bridge,
ordinary-Jacobi exit for arbitrary controls, `Xi_K -> infinity`, or global
transgression.

Expected output includes:

```text
R53_CANONICAL_JACOBI_TAIL_RECURRENCE PASSED
R53_GAUSS_QUADRATURE_DEFICIT_IDENTITY PASSED
R53_EVEN_ODD_QUADRATURE_UPDATE PASSED
R53_DEFICIT_BETA_NORM_RATIO PASSED
R53_CUBIC_TRACE_STABILIZATION PASSED
R53_POSITIVE_BRANCH_FULL_EXACT_REALIZATION CONDITIONAL_ON_ALL_BETA_POSITIVE PASSED
R53_CANONICAL_CENTERED_TAIL_RIGIDITY REMAINS OPEN
R53_EVENTUAL_DIAGONAL_SKEW_ANNIHILATION REMAINS OPEN
R53_AUDIT_COMPLETED
```
