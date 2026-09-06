# R48 — heat-lift null hierarchy and moving-rank threshold

This is a local exact audit of the webpage R48 theory round.  It does not
claim `Xi_K -> infinity`, does not construct a genuine all-degree bad law, and
does not turn a response-rank statement into a no-go.  The rank-two flat
shadow supplies a test polynomial only; its null relation is never imposed on
the genuine full law.

## Audited finite identities

With `v=1-a`, `c=t*sqrt(v)`, `t^2=2`, and

```text
P(x) = x^2 - c*x - v,
r_k = L_a^mu(x^k P(x)^2),
```

the inverse-Hermite defect rows are checked exactly:

```text
r_2 = sqrt(6!)*Delta_6
r_3 = sqrt(7!)*Delta_7 - 2*c*sqrt(6!)*Delta_6
r_4 = sqrt(8!)*Delta_8 - 2*c*sqrt(7!)*Delta_7
      + 28*v*sqrt(6!)*Delta_6
r_5 = sqrt(9!)*Delta_9 - 2*c*sqrt(8!)*Delta_8
      + 36*v*sqrt(7!)*Delta_7 - 54*c*v*sqrt(6!)*Delta_6
```

The genuine same-factor degree-eight relation and the rank-two shadow give

```text
b_8^mu = 8*sqrt(14)/7*b_3*b_5
Delta_8 = -9*sqrt(70)/35*v^4.
```

Consequently `r_2=18*v^3`, `r_4=-72*v^4-2*c*r_3`, and the shifted inverse-null
block has the exact determinant

```text
det [[r_2,r_3],[r_3,r_4]]
  = -(r_3+18*c*v^3)^2 - 648*v^7 < 0.
```

The audit also reconstructs the three interior heat-lift formulas for
`L_s=L_a exp((a-s)*d^2/2)`, checks their completed-square determinant form,
the unique-root bracket
`f(3/50)<0<f(1/16)` for

```text
f(x)=35*x^4+110*x^3+129*x^2+186*x-12,
```

and the OU scaling `r_k(tau)=tau^(k/2+2)*r_k`.

## Evidence boundary

The strict `2 x 2` indefiniteness closes only the direct inverse-null-positive-
Christoffel-transform route.  The collar bound and the scalar `K=1`
threshold are exact consequences of the displayed block, but the moving-rank
statement

```text
Xi_K -> infinity
```

remains OPEN.  A fixed `K` positive prefix is not an all-degree positive
full-exact law, and formal Gateaux/Hermite directions remain Taylor
coefficient extractors.  No optimizer, SDP, sweep, relaxed measure-LP, or
remote computation is used.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_heatlift_rankescape_r48\audit_r48.py
```

Expected markers:

```text
R48_NULL_DEFECT_HIERARCHY PASSED
R48_DEGREE8_BRANCH_IDENTITY PASSED
R48_SHIFTED_NULL_HANKEL_STRICTLY_INDEFINITE PASSED
R48_INTERIOR_HEAT_LIFT_FORMULAS PASSED
R48_COMPLETED_SQUARE_THRESHOLD_BRACKET PASSED
R48_XI1_SCALAR_THRESHOLD RECORDED
R48_OU_NULL_DEFECT_SCALING PASSED
R48_LIFTED_NULL_THRESHOLD_DIVERGENCE REMAINS OPEN
R48_AUDIT_COMPLETED
```
