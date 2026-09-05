# R31 — Jacobi-slack adjoint completion audit

This folder records the exact audit of the R31 `Jacobi-Slack Adjoint
Completion` round.  It checks the top odd Jacobi derivatives, canonical
`beta=B(1-u^2)` control formulas, the all-degree odd-pressure identity

`dG_(n+1)/d m_(2n-1) = -n(n+1)(n+5)(2/3)^(n+1)m_3`,

for `n=2,...,6`, the exact rational delayed-slack sign test at
`s=1/20,c=-1`, and the path-slack zero insertion that exposes the non-remote
shadow debt.

Run with:

```text
F:\anaconda3\python.exe -u flat_shadow_jacobi_slack_r31\audit_r31.py
```

Expected output:

```text
R31_JACOBI_SLACK_STRUCTURE PASSED
R31_POSITIVE_ADJOINT_INF_SUP REMAINS OPEN
R31_AUDIT_COMPLETED
```

The audit confirms structural obstructions, not a full-exact counterexample.
The same-level slack can lose its odd pivot; a fixed one-step delayed slack has
no universal positive sign; and inserting a nonnegative slack difference into
the path adjoint leaves a shadow-slack debt.  A genuine multi-level
full-exact-specific normal-cone completion remains possible in principle, but
it still requires a positive conic inf-sup, active-rank escape, shadow balance,
and a law-independent weighted dual bound.  Those requirements remain OPEN.

No optimizer, SDP, large sweep, formal finite-prefix counterexample, or `P_3K`
bridge is used here.  The audit does not prove Gaussian rigidity.
