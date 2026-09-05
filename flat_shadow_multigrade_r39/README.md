# R39 exact audit — first two-grade two-body cancellation

The R39 web review sharpened the R38 carrier window.  For fixed `N=2m`, two
normalized two-body Hoeffding carriers can preserve the grade-`N` head and
cancel the clean linear grade-`N+2` term.  The first new obstruction is at
grade `N+4`, where a mixed Hessian response channel may coexist with the
linear `D_(n,N+4)` channel.

This local audit checks only finite identities:

1. exact `2 x 2` cancellation weights for the grade-`N` and grade-`N+2`
   linear responses;
2. the Gaussian full-exact Hoeffding complement
   `1/3-B_n=A_n+C_n^(3)/3`;
3. all terms in the mixed second Gateaux derivative of the law-dependent
   two-body energy, including base-measure weights, conditional projections,
   one-body subtractions, mean correction, and mixed internal derivatives;
4. the formal `N+4` Taylor bookkeeping, including the extra `N=4` resonance.

The audit does not claim that the positive flat shadow is full-exact, and does
not turn the finite two-grade lemma into a remote transgression theorem.  The
remaining question is whether the mixed-Hessian response family has a uniform
finite-grade span/conditioning and whether positive shadow evaluations admit
the required remote analytic bound.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_multigrade_r39\audit_r39.py
```

Expected markers:

```text
R39_TWO_GRADE_EXACT_CANCELLATION PASSED
R39_CONSTRAINT_COUPLED_POSITIVITY PASSED
R39_SECOND_DERIVATIVE_DECOMPOSITION PASSED
R39_GRADE_NPLUS4_CHANNEL_DECOMPOSITION PASSED
R39_LINEAR_VANDERMONDE_NOT_THE_OBSTRUCTION RECORDED
R39_MIXED_HESSIAN_RESPONSE REMAINS OPEN
R39_AUDIT_COMPLETED
```

No optimizer, SDP, numerical sweep, relaxed measure-LP, or remote computation
is used.
