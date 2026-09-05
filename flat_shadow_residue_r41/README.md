# R41 local audit — renormalized mixed-Hessian residue

The web review reduced the R40 mixed-Hessian frontier to the normalized
residue `S_(n,m)`, supplied the exact block sum (R41.1), a closed candidate
for `sigma_m`, and an `m=3` first `1/n` coefficient.  This audit checks the
new finite block identity against direct Gaussian projection, the new `S,D`
coefficients, exact small residue values, the algebraic `m=3` quotient, and
the leading determinant identity.

The audit deliberately separates finite exact checks from the web-derived
asymptotic expansion.  It does not claim that a finite regression proves the
general `1/n` coefficient `kappa_m`, and it uses no optimizer, SDP, numerical
sweep, relaxed measure-LP, or remote computation.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_residue_r41\audit_r41.py
```

Expected markers:

```text
R41_BLOCK_FORMULA_FINITE_CHECK PASSED
R41_Q_COEFFICIENTS_FINITE_CHECK PASSED
R41_SIGMA_SPECIALIZATION_AND_SIGN PASSED
R41_M3_FIRST_VARIATION_ALGEBRA PASSED
R41_EXACT_RESIDUE_REGRESSION PASSED
R41_4X4_DETERMINANT_IDENTITY PASSED
R41_GENERAL_M_FIRST_VARIATION REMAINS OPEN
R41_ASYMPTOTIC_CLAIMS REMAIN_WEB_DERIVED_UNAUDITED
R41_AUDIT_COMPLETED
```
