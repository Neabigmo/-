# Stage27U retry2 — OU-coherent lifted minimax numerical repair

This package repairs the numerical pathologies seen in Stage27U retry1 while preserving the same scientific question:

- complete the triangular Fock recurrence at `q_low=0.05`;
- lift the *same* Hermite coefficient sequence coherently to `q_high=0.10`;
- evaluate high-q prefix energy plus a robust finite-witness infinite-tail lower bound;
- refine only the best outer candidates with continuum reduced-cost exchange.

It does **not** run Stage28, does not scan `N*q^alpha`, and does not claim a global theorem.

## Retry1 issues addressed

1. **Invalid gradient finite-difference audit.**  Retry1 clipped `y +/- h e_j` back into the energy ball and compared that constrained directional derivative with the unconstrained analytic gradient. Retry2 checks only interior points and requires the NNQP active set and objective branch to remain stable.

2. **`nonfinite b` / Inf pollution.**  Ordinary float `b_n` conversion can overflow in regions whose coherent prefix energy is already astronomically larger than `A=5`. Retry2 probes the scaled Fock recurrence first; only when it can verify the prefix is already above a harmless cutoff is the point mapped to a finite algorithmic `PREFIX_OVERFLOW_BARRIER`. Barrier points are `scientific_valid=False` and cannot become finalists or certificates.

3. **Pathological high-dimensional random starts.** Uniform-in-volume starts concentrate near the odd-energy sphere and, under coherent completion, usually have huge even-prefix energy. Retry2 calibrates each random direction to target high-q prefix-energy layers around `1.05, 1.15, 1.30, 1.60, 2.20, 3.00, 4.20, 4.75`.

4. **Failure accounting.** Unexpected exceptions are recorded separately and the independent audit requires zero unexpected failures. No `+/-Inf` value is permitted in scientific CSV fields.

## Main outputs

- `stage27u_gradient_audit.csv`
- `stage27u_lift_validation.csv`
- `stage27u_kernel_identity.csv`
- `stage27u_existing_candidate_audit.csv`
- `stage27u_outer_search.csv`
- `stage27u_outer_history.csv`
- `stage27u_continuum_validation.csv`
- `stage27u_active_support.csv`
- `stage27u_failures.csv`
- `stage27u_summary.json`
- `candidate_artifacts/N{32,48,64,80}_best.npz`

See `RUN_ME.md` and `MANIFEST.txt`.

## Transfer integrity

The authoritative retry2 delivery is the complete Git source tree, not a decoded ZIP wrapper. Run `python verify_package.py` after cloning. `PACKAGE_INTEGRITY.json` stores SHA256 for every package file except itself. `.gitattributes` forces LF for scripts/text so Windows checkout does not recreate the retry1 transfer problem.
