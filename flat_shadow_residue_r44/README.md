# R44 — general first-residue variation lemma

This audit records the proof-level boundary after the web-side R44 derivation.
It checks the new finite algebra directly from the R42/R43 exact generators;
it does not use numerical fitting, optimization, SDP, relaxed measure-LP, or
remote computation.

## Web-side candidate

For fixed `m >= 3`, with `S_(n,m) = sigma_m + kappa_m/n + O_m(n^-2)`,
the returned candidate is

```text
kappa_m = sqrt(6(2m+1))
          (608 m^4 + 672 m^3 - 386 m^2 - 207 m - 27)
          / (256 (m+1)(m+2)).
```

The same response gives the exact bivariate diagonal-moment reductions,
closed forms for `q_(m,2), q_(m,4), q_(m,6)`, the general `D` correction, and
the exact `C^(1)`/`C^(3)` pole-cancellation identities.

## Local scope

`audit_r44.py` independently checks:

1. the `A_1,A_2` Darboux coefficient rule against the existing exact
   coefficient expansion;
2. the diagonal central-binomial moments used for `j=1,2,3`;
3. the general `q_(m,2), q_(m,4), q_(m,6)` formulas for several fixed `m`;
4. the exact `C^(1)` and `C^(3)` pole cancellations;
5. the exact `C^(1)`/`C^(3)` constant-term identities;
6. positivity of the proposed numerator and the `m=3,4,5` regressions.

The imported R43 asymptotic machinery is used only for a small fixed-`m`
assembly check. Any general asymptotic statement remains a fixed-`m`
Darboux consequence; it is not a uniform-in-`m` estimate.

## Boundary

The intended passing markers are:

```text
R44_GENERAL_DARBOUX_COEFFICIENT_ALGEBRA PASSED
R44_GENERAL_BLOCK_MOMENTS PASSED
R44_C_SECTOR_POLE_CANCELLATION PASSED
R44_GENERAL_Q_FORMULAS PASSED
R44_GENERAL_KAPPA_SPECIALIZATIONS PASSED
R44_GENERAL_KAPPA_POSITIVITY PASSED
R44_NPLUS4_WEIGHTED_CONDITIONING PASSED
R44_NPLUS6_MULTI_RESPONSE REMAINS OPEN
R44_AUDIT_COMPLETED
```

This closes only the `General-m>=6 First Residue Variation Lemma` at the
fixed-`m` algebraic level. The global Constraint-Coupled Non-SOS Graded Value
Transgression, Gaussian rigidity, and the `P_3 K` bridge remain open.
