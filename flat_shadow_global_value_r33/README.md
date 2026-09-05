# R33 — Global value duality, exact-Q gauge, and shadow obstruction

This folder records the finite algebra audit requested after the R33 theory
round.  It is deliberately proof-level: no SOS solver, optimizer, degree
search, large sweep, or remote computation is used.

Run with:

```text
F:\anaconda3\python.exe -u flat_shadow_global_value_r33\audit_r33.py
```

Expected output:

```text
R33_FINITE_GLOBAL_VALUE_DUALITY RECORDED
R33_Q_IDEAL_GAUGE_AND_SHADOW_OBSTRUCTION PASSED
R33_GRADED_REMOTE_LOCALITY REMAINS OPEN
R33_AUDIT_COMPLETED
```

## Audited finite identities

For centered unit-variance moments (`m_0=1`, `m_1=0`, `m_2=1`) and

`G_n = E[Q^n] - 2^n n!`,

the exact rows `G_2,G_3,G_4` have the triangular form

`G_n = c_n m_(2n) - F_n(m_3,...,m_(2n-2))`,

with `c_n=3(2/3)^n>0` and no `m_(2n-1)` term.  Recursive elimination of the
even moments therefore kills the exact rows and leaves the odd controls.  A
sum of squares remains a sum of squares after this substitution because each
square is substituted before it is squared.

The equality ideal has the usual polynomial gauge.  For arbitrary formal
`P,h,s,G`,

`P + s^2 G^2 + (h-s^2 G)G = P+hG`.

Thus individual equality multipliers are not canonical even when the
quadratic-module part stays visibly nonnegative.

For a positive flat shadow `rho_M`, the first unmatching exact row is
`G_(M+1)(rho_M)=-c_(M+1)q_M`.  The formal exact-Q quotient continuation changes
the corresponding even moment by exactly `q_M`; consequently the quotient
anchor is generally off the actual positive shadow whenever `q_M != 0`.

If a certificate is written as `gamma+q=P+E_Q+E_flat`, evaluation at a genuine
feasible law gives `gamma+q(mu)=P(mu)`, while evaluation at the flat shadow
gives `gamma=P(rho_M)+E_Q(rho_M)` because the flat ideal vanishes there and
`q(rho_M)=0`.  Only the total shadow evaluation is gauge-invariant; separate
positive/equality debt pieces are not.

## Global theorem boundary

For each fixed finite `K`, the compact Archimedean feasible set gives the
standard value-duality statement: for every strict upper bound
`gamma > Omega_K`, a Positivstellensatz certificate exists.  This does not
imply `Omega_K -> 0`.  The equivalent certificate formulation is:

`Omega_K -> 0` iff for every `epsilon>0` there is a finite `K(epsilon)` with
`epsilon+q_M` in the corresponding quadratic module plus exact ideal.

Therefore unstructured global SOS existence is not the missing theorem.  The
remaining target is a shadow-compatible, gauge-invariant, Hermite-graded
certificate whose fixed/intermediate Hermite content vanishes and whose remote
dual norm is uniform in `K` and in the law.  High constraint rank alone does
not imply high Hermite degree because each `G_n` still depends on the whole
moment prefix.  The measure-LP relaxation is also insufficient: replacing the
same-factor triple law by a general positive triple law loses the rank-one
product structure.

The resulting minimum OPEN is **Shadow-Compatible Graded Global
Positivstellensatz**, equivalently gauge-invariant global value-level remote
adjoint locality.  Gaussian rigidity and the `P_3K` bridge remain OPEN and
logically disconnected from this audit.
