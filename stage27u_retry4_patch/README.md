# Stage27U retry4A — auditable single-witness dual pruning

This is a small overlay on top of the retry3 branch. It does **not** alter the NNQP
solver, ridge, Fock completion, OU lift, Gram construction, continuum exchange, or
final candidate replay.

When the full NNQP returns `success=False`, retry4A asks a narrower question: does one
explicit witness already prove that this evaluation point is far above the minimax
boundary? For one coordinate `alpha=t e_j`,

`m_tail^2 >= min(c_j,0)^2 / (C_jj eps^2)`.

Runtime acceptance is deliberately strict:

- float arithmetic only ranks candidate witnesses;
- the selected witness is recomputed at 220 dps and at least 300 dps;
- the two bounds must agree to relative error <= `1e-10`;
- the smaller bound is shrunk by `1e-12`;
- only a resulting pointwise margin >= `+25` is pruned;
- otherwise the original `NNQP invalid success=False` remains a numerical failure.

Every prune is saved in `stage27u_retry4_dual_prune.csv`. The independent retry4 audit
replays each one at >=360 dps and then runs the full retry3 + retry2 audits.

Recommended remote sequence:

```bash
python chi2_n3_ou_coherent_stage27u_retry2_2026-09-03/verify_package.py
python chi2_n3_ou_coherent_stage27u_retry2_2026-09-03/python/selftest_stage27u.py
python stage27u_retry3_patch/selftest_retry3.py
python stage27u_retry4_patch/selftest_retry4.py

export STAGE27R_DIR=/path/to/stage27r
export STAGE27S_DIR=/path/to/stage27s
bash stage27u_retry4_patch/run_retry4_remote.sh
```

Successful independent audit marker:

`STAGE27U_RETRY4_DUAL_PRUNE_AUDIT_OK`

A clean retry4 run is still not a theorem certificate. In particular, the negative /
boundary-unresolved N=32 result remains the key scientific obstruction. No Stage28.
