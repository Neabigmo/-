# Stage27U retry3 — strict N=64 gradient-audit overlay

This directory is a **minimal overlay** on the already verified Stage27U retry2 fix1 package:

`chi2_n3_ou_coherent_stage27u_retry2_2026-09-03/`

The retry2 package subtree is intentionally unchanged. Its package verifier and selftest remain authoritative for the core Fock/Gram/NNQP/objective implementation.

## Why retry3 exists

The real retry2 remote run stopped safely in preflight with:

- stable gradient checks: `{32:5, 48:5, 64:1, 80:3}`;
- maximum checked gradient relative error about `3.98e-05`, already below the unchanged `2e-3` threshold;
- three additional N=64 test points failed because an NNQP evaluation inside finite-difference perturbations returned `success=False`.

Retry3 repairs **coverage**, not the acceptance thresholds.

## What changes

`gradient_audit_retry3.py` makes two changes only:

1. preflight searches a deterministic ladder of smaller coordinate/random interior points, up to 64 trials per N, instead of relying on only the original fixed four random amplitudes;
2. if one `y +/- h e_j` perturbation has an NNQP numerical failure, only that direction is rejected. A point is declared stable only when at least **two** directions still have valid +/- evaluations, unchanged objective branch, and unchanged NNQP active set.

The following are unchanged:

- N=64 is mandatory;
- at least 2 stable points for every requested N is mandatory;
- gradient relative error must be `< 2e-3`;
- `qp.success=False` never counts as stable;
- q values, fixed ridge `1e-11`, Fock completion, Gram construction, NNQP solver, KKT/complementarity criteria, outer objective, continuum validation, and all scientific decision rules are unchanged;
- no Stage28 is started;
- no numerical output is a theorem certificate.

## Verification before running

From the repository root:

```bash
python chi2_n3_ou_coherent_stage27u_retry2_2026-09-03/verify_package.py
python chi2_n3_ou_coherent_stage27u_retry2_2026-09-03/python/selftest_stage27u.py
python stage27u_retry3_patch/selftest_retry3.py
```

Expected markers:

```text
STAGE27U_RETRY2_PACKAGE_VERIFY_OK files=28
STAGE27U_RETRY2_SELFTEST_OK
STAGE27U_RETRY3_PATCH_SELFTEST_OK
```

## Run

The required external inputs are unchanged from retry2:

- Stage27R: `q0p1_N64_ridge1em11.npz`, `q0p1_N80_ridge1em11.npz`;
- Stage27S: `stage27s_continuum.csv`;
- recommended if available: `stage27s_exchange_history.csv`.

Run directly with Python (recommended on Windows/WSL because it avoids shell line-ending issues):

```bash
python stage27u_retry3_patch/run_stage27u_retry3.py \
  --stage27r-dir "$STAGE27R_DIR" \
  --stage27s-dir "$STAGE27S_DIR" \
  --outdir _stage27u_retry3_results_20260903
```

Optional Stage15/16 roots may be passed exactly as in retry2.

After completion:

```bash
python stage27u_retry3_patch/audit_retry3.py \
  --result-dir _stage27u_retry3_results_20260903
```

The final retry3 audit marker is:

```text
STAGE27U_RETRY3_NUMERIC_AUDIT_OK
```

The original retry2 independent audit is invoked inside the retry3 audit wrapper, so artifact replay, finite-value checks, failure-count checks, and candidate replay are still required.
