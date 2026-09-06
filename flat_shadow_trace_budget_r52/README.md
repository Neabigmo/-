# R52 — global route audit and trace–budget obstruction

The webpage R52 round first audited the whole route and then pushed the
R51 ordinary-Jacobi budget one step further.  The global conclusion is that
R36–R51 made three mechanism-level reductions—two-body Laguerre–Hoeffding
carriers, finite-grade residue/rank separation, and inverse-heat/Christoffel
compression to ordinary Jacobi tail—but the remaining problem is now a
global coherence barrier.  More fixed-grade determinants or finite response
rows would be local repetition.

The most mature self-contained reportable packages are:

1. R11–R13: exact-class square-exponential tail, OU closure, and exclusion
   of projectively compatible non-Gaussian fixed-factor towers.
2. R36–R44: two-body Laguerre–Hoeffding carrier, fixed-head asymptotics, and
   constraint-coupled finite-grade transgression.
3. R48–R51: inverse-heat/Christoffel-to-ordinary-Jacobi reduction and the
   optimized two-step budget.

These are mathematical theorem packages, not a claim of literature novelty.
The P_3 K bridge has not been obtained: fixed `m_3`, rank-two head, Jacobi
exit, and `P_3 K != 0` remain logically distinct. A final Gaussian rigidity
theorem could bypass the bridge, but it has not been proved.

## Exact R52 identities

For monic Jacobi recurrence

```text
x*pi_k = pi_(k+1) + alpha_k*pi_k + beta_k*pi_(k-1),  beta_k>0,
S_k = sum_(j=0)^k alpha_j,  S_(-1)=0,
B_k = beta_k + S_(k-1)^2,
```

write `T_k = tr(J_k^3)`.  Full-exact Jacobi walk counting gives

```text
T_k - T_(k-1)
  = alpha_k^3 + 3*beta_k*(alpha_(k-1)+alpha_k),                 (A.2)

T_k - T_(k-1)
  = (S_k-S_(k-1))^3
    + 3*(B_k-S_(k-1)^2)*(S_k-S_(k-2)).                         (A.3)
```

For fixed old prefix `S=S_(n-2)`, current `s=S_(n-1)`, and next `t=S_n`,
the two-control exact trace law is

```text
tr(J_n(s,t)^3) - tr((J_n^circ)^3)
  = 3*B_(n-1)*s + t^3 - 3*s*t^2 + 3*B_n*t.                    (A.4)
```

At `t=0`, the cubic-trace center defect is

```text
A_n = B_(n-1)*sigma_n
    = n*(n+1)*(n+5)*m_3/6 - tr((J_n^circ)^3)/3.                (A.5)
```

These are full-exact Jacobi identities.  They do not use a Gateaux
perturbation and do not turn a fixed-K prefix into a probability law.

## Centered budget and the sharp cone

The R51 transfer identity, retained in two-control form, is

```text
(B_n-s^2)*B_(n+1)(s)
  = B_n*B_(n+1) + 2*A_n*s - B_(n-1)*s^2.                     (A.7)
```

On the actual compatible chain,

```text
B_n*B_(n+1)
  = beta_n*beta_(n+1) + beta_n*S_n^2
    + B_(n-1)*S_(n-1)^2 - 2*A_n*S_(n-1),                     (A.8)

B_n*B_(n+1)
  = beta_n*beta_(n+1) + beta_n*S_n^2
    + B_(n-1)*(S_(n-1)-A_n/B_(n-1))^2
    - A_n^2/B_(n-1).                                        (A.9)
```

Thus `B_(n+1) > -A_n^2/(B_(n-1)*B_n)` and
`B_(n+1)<0` forces `A_n*S_(n-1)>0`.  Put

```text
a_n = |A_n|/(B_(n-1)*sqrt(B_n)),
Phi(a) = a^2       for 0<=a<=1,
         2*a - 1   for a>=1.
```

Optimizing the current odd control over `|S_(n-1)|<sqrt(B_n)` yields the
sharp necessary compatibility cone

```text
B_(n+1)/B_(n-1) + Phi(a_n) > 0.                              (A.13)
```

Therefore the optimal conditional exit condition is `theta > Phi(kappa)`:
if, for some `n <= N(X)`,

```text
|A_n| <= kappa_X*B_(n-1)*sqrt(B_n),
B_(n+1) <= -theta_X*B_(n-1),
theta_X > Phi(kappa_X),
```

then the two-step viability value is negative and ordinary Jacobi exit
occurs.  This improves the older sufficient threshold `theta>kappa^2` for
the large-trace regime `kappa>1`, where `Phi(kappa)=2*kappa-1`.

## What remains open

The global Uniform Cubic-Trace Tracking + Centered-Budget Negativity Lemma
is not proved.  The obstruction is structural: the cubic trace controls the
linear/center channel, while the centered budget is an independent constant
channel.  Finite same-factor identities and rank-two residue information do
not collapse those channels.

The recommended weaker target is **canonical centered-tail rigidity**.  Fix
a R47-compatible bounded-X head, set every newly opened odd coordinate to
`S_k=0`, and determine each new even moment from exact `G_(k+1)=0`.  The
candidate theorem is

```text
for every finite X, the canonical centered branch reaches B_k<=0 at finite k.
                                                                    (D.1)
```

This is genuinely weaker than the arbitrary-control uniform lemma.  Its
value is a sharp dichotomy: if (D.1) fails, all `B_k>0` give a positive
Jacobi chain and hence a Hamburger representing law; exact `G_k=0` yields
the full chi-square moments `E[Q^k]=2^k*k!`.  Since the centered branch has
eventually `S_k=0`, its Jacobi diagonal is eventually zero, producing a
highly structured genuine infinite-chain candidate rather than a formal
prefix.  Such a candidate would still need a positive backward OU preimage
to address the original rigidity problem.

The local audit checks only the exact algebra above.  It does not claim
(D.1), the arbitrary-control tail lemma, Gaussian rigidity, or the `P_3 K`
bridge.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_trace_budget_r52\audit_r52.py
```

Expected markers:

```text
R52_FULL_EXACT_JACOBI_TRACE_INCREMENT PASSED
R52_S_COORDINATE_TRACE_INCREMENT PASSED
R52_TWO_CONTROL_CUBIC_TRACE_LAW PASSED
R52_CENTERED_BUDGET_COMPLETE_SQUARE PASSED
R52_SHARP_RESCUE_CONE_AND_CONDITIONAL_EXIT PASSED
R52_UNIFORM_TRACE_BUDGET_LEMMA REMAINS OPEN
R52_CANONICAL_CENTERED_BRANCH_EXIT REMAINS OPEN
R52_GAUSSIAN_RIGIDITY REMAINS OPEN
R52_P3K_BRIDGE REMAINS OPEN
R52_AUDIT_COMPLETED
```
