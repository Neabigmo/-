# R46 — N=6 second-residue rank lower bound

This audit is a proof-level continuation of R45.  It uses exact Gaussian
Hermite generators and formal Laurent/Darboux expansion; it does not use
finite-`n` fitting, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation.

## What is checked

- The `q=5` conditional-score generator is checked against direct Gaussian
  marginalization at `(n,m)=(3,3)`.
- The raw `H_(n;7,5)` `W` row is assembled from the exact bivariate block
  generator.
- The old `N=6` response span is
  `{D_(n,12)/D_(n,6), D_(n,10)/D_(n,6), D_(n,8)/D_(n,6), 1,
  S_(n,3)-sigma_3}`.
- The `H_(n;9,3)` and `H_(n;7,5)` rows are expanded from `n^3` through the
  first two quotient powers and reduced against that span.  The Darboux
  helper retains all analytic Taylor terms needed at the requested order;
  the lower-order R43 helper is not reused beyond its valid truncation.

## Exact output

```text
R46_H75_GENERATOR_FINITE_CHECK PASSED
R46_H93_QUOTIENT_SECOND_RESIDUE
  c32=-3970123318809*sqrt(21)/294859571200
  c33=59155049844691*sqrt(21)/8491955650560
R46_H75_QUOTIENT_SECOND_RESIDUE
  c52=1176526610081*sqrt(210)/294859571200
  c53=-2147390944445*sqrt(210)/566130376704
R46_C3RES_FIRST_TWO_ROWS_RANK_GE2
  DET=72543614649557486062397*sqrt(10)/148407681470693376000
R46_C3RES_FULL_MATRIX REMAINS OPEN
R46_AUDIT_COMPLETED
```

Thus the first two quotient rows already have a nonzero `2 x 2` minor, so
`rank(C_3^res) >= 2`.  This is a rank lower bound, not a no-go theorem: the
full four-row matrix, its determinant, the carrier norm, and the global
positive backward-tower transgression remain open.

## Boundary

The formal Hermite directions are coefficient extractors for the genuine OU
path and are not probability counterexamples.  Positivity is used only for
genuine full-exact laws; no positive flat shadow is upgraded to a full-exact
law.  Gaussian rigidity and the `P_3 K` bridge remain open.
