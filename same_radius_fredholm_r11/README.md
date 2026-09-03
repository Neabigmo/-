# R11 — same-radius Fredholm audit

This is a finite, exact audit of the R10 correction and the proposed
same-radius Fredholm reduction.  It does not run remote jobs, optimization,
SDP, numerical zero searches, or a new Stage-7 campaign.

Run from this directory with the workspace Python:

```text
python audit_same_radius.py
python -m pytest -q
```

The audit deliberately separates three claims:

1. the corrected Student/Beta angular moments and the exact finite angular
   kernel;
2. the coefficient and tail estimates needed for a same-radius compact
   remainder;
3. the even Wiener multiplication index replay.

The original Stage-7 source normalization is now explicitly identified and
the normalized even domain is conjugated exactly to the `w^2` ideal.  The
same-radius compact-perturbation theorem therefore has the decision
`SAME_RADIUS_FREDHOLM_LINEARIZATION_CERTIFIED`.  This still is not Gaussian
rigidity: the next open question is whether probability/OU coherence can
exclude a negative normalized-even Fredholm index.
