# R30 — Flat-shadow augmented-adjoint audit

This folder records the exact algebraic audit for the R30 web-theory round.
The local script checks the path-averaged Jacobian identity for the cubic
moment equations `G_n`, the even/odd structural pivots, the first-row
identification `d_(2M+2)=q_M`, a finite multiplier/telescoping skeleton, and
the remaining odd-control dimension after the matched prefix.

Run with the repository's SymPy interpreter:

```text
F:\anaconda3\python.exe -u flat_shadow_augmented_adjoint_r30\audit_r30.py
```

Expected output:

```text
R30_AUGMENTED_ADJOINT_IDENTITY PASSED
R30_SIGN_COMPATIBLE_LOCALITY REMAINS OPEN
R30_AUDIT_COMPLETED
```

The audit does not construct the required full-exact certificate

`q_M = P_K + R_K`, with `P_K >= 0` and a law-independent weighted remote-tail
dual bound. Equality-only adjoints have no sign and leave odd-control directions
(after the already matched first odd slot); the missing completion must use
genuine Hamburger/Jacobi slack such as `beta_n = B_n - S_(n-1)^2 >= 0`.

Consequently, `R30_SIGN_COMPATIBLE_LOCALITY` remains OPEN. No optimizer, SDP,
large numerical sweep, formal finite-prefix counterexample, or `P_3K` bridge is
used here. The calculation is an identity audit only and does not prove
Gaussian rigidity or produce a genuine full-exact counterexample.
