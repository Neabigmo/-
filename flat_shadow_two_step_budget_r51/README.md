# R51 — optimized two-step Jacobi budget

This is a local exact audit of the new identities from the webpage R51 round.
It does not claim the uniform finite ordinary-Jacobi exit, the stronger
root-leverage exit, `Xi_K -> infinity`, or Gaussian rigidity.  Fixed-K formal
prefixes, genuine all-degree full-exact laws, and formal Gateaux/Hermite
extractors remain distinct.

## Audited identities

For a viable prefix with current odd coordinate
`s=S_(n-1)=(y-y_n^0)/h_(n-1)`, the free next odd coordinate can cancel the
two-step Schur off-diagonal, which is equivalent to `S_n=0`.  Let
`widehat B_(n+1)` be the next Jacobi budget in the doubly-centered formal
extension `S_(n-1)=S_n=0`.  The audit checks

```text
D_n(0) / h_(n-1) = B_n * widehat B_(n+1)
D_n(s) / h_(n-1)
  = B_n * widehat B_(n+1)
    + 2 * B_(n-1) * sigma_n * s
    - B_(n-1) * s^2.
```

Consequently

```text
(R_n^+)^2
  = sigma_n^2 + B_n * widehat B_(n+1) / B_(n-1).
```

Optimizing over the current interval `|s|<sqrt(B_n)` gives the exact
two-step viability value

```text
V_n = B_n * widehat B_(n+1)
      + B_(n-1) * Psi_(sqrt(B_n))(sigma_n),
```

where `Psi_r(sigma)=sigma^2` for `|sigma|<=r` and
`Psi_r(sigma)=2*r*|sigma|-r^2` otherwise.  Thus strict two-step extension is
possible exactly when `V_n>0`; ordinary two-step exit is `V_n<=0`.
The rescue term is nonnegative, so a large same-factor center pressure does
not itself force exit.  In particular, if `widehat B_(n+1)>=0`, the radius
identity prevents the proposed pressure-vs-radius separation argument from
working by itself.

The geometric center is identified by the doubly-centered Jacobi truncation
`J_n^circ`:

```text
B_(n-1) * sigma_n
  = n*(n+1)*(n+5)*m_3/6 - tr((J_n^circ)^3)/3.
sigma_n^geom = -tr((J_n^circ)^3)/(3*B_(n-1)).
```

For the formal tail with current `S_(n-1)=s` and next `S_n=0`, the audit
checks the affine trace law

```text
tr(J_n(s)^3) = tr((J_n^circ)^3) + 3*B_(n-1)*s.
```

Writing `A_n=B_(n-1)*sigma_n`, the rescue term is exactly

```text
R_n = A_n^2/B_(n-1),
      if |A_n| <= B_(n-1)*sqrt(B_n),
R_n = 2*|A_n|*sqrt(B_n)-B_(n-1)*B_n,
      otherwise.
```

## Conditional theorem and evidence boundary

The webpage gives a valid conditional sufficient theorem: for fixed finite
`X`, if every compatible prefix has some `4<=n<=N(X)` with

```text
|A_n| <= kappa_X * B_(n-1) * sqrt(B_n)
widehat B_(n+1) <= -theta_X * B_(n-1)
theta_X > kappa_X^2,
```

then `V_n<0` and ordinary Jacobi exit occurs by `N(X)+1`.  The audit checks
this implication algebraically only.  It does not prove either tail
hypothesis.  The actual missing result remains a uniform centered-budget /
cubic-trace tracking estimate, with the stronger root-leverage-dominated
exit still strictly downstream.

No optimizer, SDP, large sweep, relaxed measure-LP, or remote computation is
used.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_two_step_budget_r51\audit_r51.py
```

Expected markers:

```text
R51_DOUBLY_CENTERED_TRANSFER_IDENTITY PASSED
R51_RADIUS_AND_OPTIMIZED_FUNCTIONAL PASSED
R51_CENTERED_BUDGET_EXIT_ALGEBRA PASSED
R51_CUBIC_JACOBI_TRACE_AFFINE_LAW PASSED
R51_CUBIC_TRACE_CENTER_REDUCTION PASSED
R51_FIXED_HEAD_TWO_STEP_EXIT REMAINS OPEN
R51_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN
R51_XI_DIVERGENCE REMAINS OPEN
R51_AUDIT_COMPLETED
```
