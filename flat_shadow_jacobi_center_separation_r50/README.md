# R50 — Fixed-head two-step Jacobi center separation

This is a local exact audit of the webpage R50 theory round.  It does not
claim a uniform finite ordinary-Jacobi exit, `Xi_K -> infinity`, or a genuine
all-degree non-Gaussian law.  Fixed-K prefixes, genuine full-exact laws, and
formal Gateaux/Hermite coefficient extractors remain distinct.

## Audited identities

For the project moment functional, with `H_(n-1)>0`, let `y=m_(2n-1)` be the
current odd control and let the exact `G_n=0` row determine `m_(2n)=E_n(y)`.
The audit checks the exact square completion

```text
h_n(y) = h_(n-1)*B_n - (y-y_n^0)^2/h_(n-1),
S_(n-1) = (y-y_n^0)/h_(n-1),
|S_(n-1)| < sqrt(B_n).
```

The next exact row determines `m_(2n+2)=E_(n+1)(y)`.  With

```text
w_n(y)=(m_(n+1),...,m_(2n-2),y,m_(2n))^T,
D_n(y)=E_(n+1)(y)-w_n(y)^T H_(n-1)^(-1) w_n(y),
```

the two-step Hankel Schur complement has a free off-diagonal coordinate
`m_(2n+1)`.  Choosing it to zero makes the extension positive exactly when
`h_n(y)>0` and `D_n(y)>0`.  The audit checks

```text
D_n''(y) = -2*(H_(n-1)^(-1))_(n-2,n-2)
          = -2*B_(n-1)/h_(n-1).
```

It also rechecks the exact same-factor pressure and even pivot, for `n=2,...,6`:

```text
partial_(m_(2n-1)) G_(n+1)
  = -n*(n+1)*(n+5)*(2/3)^(n+1)*m_3,
partial_(m_(2n+2)) G_(n+1)
  = 3*(2/3)^(n+1).
```

Therefore, when `m_3` is held fixed as a lower head, the exact-row center
shift is

```text
Delta S_n = n*(n+1)*(n+5)*m_3/(6*B_(n-1)).
```

The interval-overlap completion and the fixed-`X` nonzero-head bound are also
checked symbolically.  The generic two-step Schur identities are checked at
`n=3`, where the current odd control is `m_5` and is distinct from the fixed
lower head `m_3`.

## Evidence boundary

The audit confirms a concrete moving-tail pressure, but does not control
`B_n`, `H_(n-1)^(-1)`, the geometric center, or the next interval radius
uniformly in `n`.  Consequently it does not prove ordinary Jacobi exit or the
stronger root-leverage-dominated exit.  The fixed-`X` compactness dichotomy is
recorded as conditional and is logically related to the earlier R25
finite-prefix compactness argument; it is not a new coercivity mechanism.

No optimizer, SDP, numerical sweep, relaxed measure-LP, or remote computation
is used.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_jacobi_center_separation_r50\audit_r50.py
```

Expected markers:

```text
R50_SAME_FACTOR_PRESSURE_AND_EVEN_PIVOT PASSED
R50_ONE_STEP_VIABILITY_INTERVAL n=3 PASSED
R50_TWO_STEP_CURVATURE n=3 PASSED
R50_TWO_STEP_EXTENSION_CRITERION n=3 PASSED
R50_SAME_FACTOR_CENTER_SHIFT PASSED
R50_INTERVAL_OVERLAP_COMPLETION PASSED
R50_FIXED_X_HEAD_NONZERO PASSED
R50_FIXED_HEAD_TWO_STEP_EXIT REMAINS OPEN
R50_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN
R50_FIXED_X_COMPACTNESS REMAINS CONDITIONAL
R50_AUDIT_COMPLETED
```
