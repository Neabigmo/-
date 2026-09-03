# Stage27U retry4 — read-only restricted-dual triage

This is the recommended next step after retry3. It does **not** rerun the campaign and does not modify NNQP.
It reads the four saved `candidate_artifacts/N{N}_best.npz` files and independently computes:

- prefix-only margin;
- best 1-witness restricted-dual tail lower bound;
- best 2-witness restricted-dual lower bound among the strongest witnesses.

The restricted problems are solved analytically and replayed with mpmath. This is meant to answer one narrow question cheaply: are the huge positive N48/N64/N80 final margins already visible without the unstable large NNQP?

Run:

```bash
python stage27u_retry4_triage/selftest_triage.py
python stage27u_retry4_triage/restricted_dual_triage.py \
  --retry3-result-dir /path/to/_stage27u_results_retry3_20260903 \
  --outdir _stage27u_retry4_triage_20260903
python stage27u_retry4_triage/audit_triage.py \
  --retry3-result-dir /path/to/_stage27u_results_retry3_20260903 \
  --triage-dir _stage27u_retry4_triage_20260903
```

Expected final marker: `STAGE27U_RETRY4_TRIAGE_AUDIT_OK`.

Interpretation is deliberately limited: this is pointwise replay of saved final candidates, not a global outer-minimax certificate and not a theorem. If N48/64/80 are pointwise positive while N32 remains negative/boundary unresolved, the next research effort should focus on N32 boundary resolution before any general NNQP rewrite.
