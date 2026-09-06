# R42 local audit — bivariate residue generators and the `m=4` case

The web review supplied two new exact generating identities and a complete
`m=4` residue assembly.  This audit checks the exact identities against the
finite Hermite formulas, checks the `m=4` cancelled-polynomial coefficients,
checks the exact finite residue value, and verifies the algebraic assembly of
the displayed asymptotic coefficients.

The singular expansions themselves remain web-derived: finite exact checks and
quotient algebra do not prove their general asymptotic derivation.  The audit
does not use an optimizer, SDP, numerical sweep, relaxed measure-LP, or remote
computation.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_residue_r42\audit_r42.py
```

Expected markers:

```text
R42_BLOCK_BIVARIATE_GENERATOR PASSED
R42_DOTP3_GENERATOR PASSED
R42_M4_Q_COEFFICIENTS PASSED
R42_M4_RESIDUE_QUOTIENT_ALGEBRA PASSED
R42_M4_EXACT_RESIDUE_REGRESSION PASSED
R42_M4_WEIGHTED_CONDITIONING PASSED
R42_M4_SINGULAR_EXPANSIONS REMAIN_WEB_DERIVED_UNAUDITED
R42_GENERAL_M_KAPPA REMAINS OPEN
R42_AUDIT_COMPLETED
```
