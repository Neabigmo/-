# R38 exact audit — complete two-body Hoeffding head derivative

R37's web review derived the normalized two-body expansion, the complete
Gateaux derivative of the degenerate Hoeffding energy, and the finite Hermite
sum for the fixed head.  This audit checks the new finite identities exactly
at small degrees.  It treats `dmu=(1+epsilon*g)d_gamma` only as a coefficient
extractor for a real positive-law OU-path Taylor coefficient; it is not used
as a probability counterexample.

The audit checks:

1. the normalized `S,D` coefficient formula for `h_(2,n)`;
2. the separate conditional-kernel, one-body subtraction, mean, and base
   measure-weight derivatives;
3. exact orthogonality of all internal Hoeffding derivatives against the
   degenerate Gaussian pair kernel;
4. the finite triple-Hermite sum for
   `partial_(b_(2m)) ||h_(2,n)||^2|_gamma`;
5. the small exact values
   `D_(1,2)=2sqrt(2)/9`, `D_(2,2)=28sqrt(2)/27`, and
   `D_(2,4)=2sqrt(6)/3`, together with the n=3,4 regressions.

The web-side asymptotic remains a theorem-level review result:

`B_n^gamma ~ 3/(2sqrt(2 pi n))`,

and for fixed `N=2m`,

`partial_(b_(2m)) B_n|_gamma ~
  3sqrt((2m)!)/(sqrt(2 pi)(m!)^2) n^(m-1/2)`.

The local audit does not infer that asymptotic from the finite table.  It only
confirms its exact finite formula and regression values.  The normalized
two-body carrier therefore passes the anchor/head screening, while uniform
multi-grade cancellation and its condition number remain OPEN.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_hoeffding_transgression_r38\audit_r38.py
```

Expected markers:

```text
R38_TWO_BODY_NORMALIZED_EXPANSION PASSED
R38_TWO_BODY_FULL_DERIVATIVE PASSED
R38_INTERNAL_HOEFFDING_DERIVATIVES_CANCEL PASSED
R38_FIXED_HEAD_FINITE_SUM PASSED
R38_TWO_BODY_CARRIER_WINDOW WEB_REVIEWED_LOCAL_FINITE_CHECK PASSED
R38_MULTI_GRADE_CONDITIONING REMAINS OPEN
R38_AUDIT_COMPLETED
```

No optimizer, SDP, numerical sweep, relaxed measure-LP, or remote computation
is used.
