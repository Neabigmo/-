# Stage27T — two-sided energy bracket

This package implements the Stage27T plan for the n=3 chi-square sample-variance project.
It does **not** run Stage28 and does **not** launch any OU-coherent multi-q campaign.

## Purpose

Stage27S produced robust-MP finite-witness lower bounds for eight diagnostic points but seven were still `outer_limit`. Stage27T therefore attacks the opposite side: construct explicit finite Hermite tails and obtain numerically audited upper bounds on the required repair energy. The key object is a two-sided bracket

    dual finite-witness LB <= repair energy on the audited numerical domain <= explicit finite-tail UB.

A small-q validated UB <= 1e-3 together with the existing C1 LB >= 0.525 at the same kappa=6.4 is recorded as `NQ_ONLY_SCALING_NUMERICALLY_REJECTED` (numerical conclusion only, not a theorem).

## Inputs

You need the already completed result trees on the remote host:

1. Stage27R PSD-repair results, containing `robust_artifacts/*.npz` for the diagnostic points.
2. Stage27S handoff/results, containing `stage27s_continuum.csv`.

The locator searches recursively, so either the outer handoff directory or its nested result directory may be supplied.

## Numerical design

* Zero-tail audit first for A, B, C3, C4, C5.
* Adaptive numerical domain: `S = 6, 8, 10, 12` and `lambda_cap = 1-1e-12, 1-1e-14, 1-1e-16`.
* Dense proposal grid: `s_grid=241`, `refine_k=20` by default.
* Final candidate density values are checked at MP dps 160 and 240.
* Finite tail lengths: L=64,128,256; C4/C5 may use L=512 if needed.
* Constraint rows are generated with MP Hermite recurrence and normalized row-by-row.
* The least-norm problem is solved in witness-space through the PSD dual Gram matrix. Explicit coefficients `v` are recovered and then corrected only by half-space feasibility projections if necessary.
* Feature Gram matrices are cross-checked between MP precisions; PSD, diagonal and correlation audits are serialized.
* Old Stage27R coefficient-space SLSQP is not used as the primary primal solver.

## Outputs

The production run writes:

- `stage27t_zero_tail_audit.csv`
- `stage27t_zero_tail_history.csv`
- `stage27t_primal_reconstruction.csv`
- `stage27t_primal_history.csv`
- `stage27t_feature_audit.csv`
- `stage27t_energy_brackets.csv`
- `stage27t_failures.csv`
- `stage27t_summary.json`
- `stage27t_run.log`
- `primal_artifacts/*.npz`

A validated NPZ stores the explicit `v`, zero-branch `u`, final witnesses, row scaling information, final slacks, worst audited point, normalized feature matrix and Gram matrix.

## Interpretation warning

This package provides numerical evidence on adaptively expanded compact domains. It does not prove positivity on the full unbounded continuum, does not prove the characterization theorem, and must not be presented as an asymptotic/global certificate.
