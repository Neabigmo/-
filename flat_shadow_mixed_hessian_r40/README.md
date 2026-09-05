# R40 local probe — mixed-Hessian two-body response

The current web research target is
`K_(n,m)=D^2 B_n(gamma)[h_(2m+1),h_3]` for `N=2m>=6`.  This small exact probe
computes the complete mixed second law-functional derivative and independently
checks it by extracting the `epsilon*delta` coefficient from the affine density
expansion.  It includes base-measure weights, conditional projection terms,
one-body subtraction, mean correction, and the mixed internal derivative.

The initial target is `m=3`, namely `K_(n,3)` for `n=1,...,5`.  These are exact
finite regression values only.  The asymptotic order, relation to
`D_(n,2m+4)`, and any response-rank conclusion remain deferred to the web
review and must not be inferred from this small table.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_mixed_hessian_r40\audit_r40.py
```

Expected markers:

```text
R40_MIXED_HESSIAN_COMPLETE_DECOMPOSITION PASSED
R40_MIXED_HESSIAN_FINITE_REGRESSION PASSED
R40_ASYMPTOTIC_RESPONSE REQUIRES_WEB_REVIEW
R40_AUDIT_COMPLETED
```

No optimizer, SDP, numerical sweep, relaxed measure-LP, or remote computation
is used.
