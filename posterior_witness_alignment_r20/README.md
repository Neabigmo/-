# R20 — posterior witness alignment proof-level audit

This audit records the algebraic checks needed after the web-side R19
analysis.  It deliberately separates identities that are unconditional
algebra from the still-open step that would align high-rank negative
Wick–Hankel witnesses across posterior slices.

The replay checks:

- Gaussian-component conjugacy under quadratic/Esscher posteriorization;
- the formal posterior Gaussian deconvolution and its Wick–Hankel moments;
- the strict `R>r` Gaussian variance gap;
- normalization and the same-factor posterior cubic identity in the Gaussian
  reference law;
- translation covariance of the posterior source.

The Gaussian reference check is only a consistency test.  It is not evidence
for Gaussian rigidity and does not prove the missing reverse-Schur theorem.

Expected terminal marker: `R20_AUDIT_COMPLETED`.
