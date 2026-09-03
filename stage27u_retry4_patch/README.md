# Stage27U retry4A — single-witness dual-prune overlay

Use this only after the retry3 overlay branch. It does **not** replace or relax NNQP.
It handles only the specific case where the full NNQP reports `success=False`, but a
single explicit witness already proves the current evaluation point has a very large
positive lower margin.

For one coordinate `alpha=t e_j`,

`m_tail^2 >= min(c_j,0)^2 / (C_jj eps^2)`.

Retry4 independently recomputes the selected witness with mpmath and only prunes when
`prefix_energy + one_witness_lb - A >= 25`. If that test fails, the original numerical
failure remains a failure.

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

Success of the retry4 independent audit is marked by
`STAGE27U_RETRY4_DUAL_PRUNE_AUDIT_OK`.

Even a completely clean retry4 run is not a theorem certificate. In particular, a
negative/boundary-unresolved N=32 result remains unresolved and must be studied next.
