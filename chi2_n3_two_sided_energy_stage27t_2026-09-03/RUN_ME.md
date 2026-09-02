# RUN_ME — Stage27T

From inside the extracted package:

```bash
python python/selftest_stage27t.py
```

Then run the production calculation. Example paths (adjust to the remote host):

```bash
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

python python/run_stage27t.py \
  --stage27r-dir /path/to/_stage27r_psd_repair_results_20260902 \
  --stage27s-dir /path/to/_stage27s_continuum_primal_results_20260902 \
  --outdir _stage27t_two_sided_results_20260903 \
  --s-grid 241 \
  --refine-k 20 \
  --max-outer 20 \
  2>&1 | tee _stage27t_two_sided_results_20260903/console.log
```

Optional C1 explicit upper-bracket run:

```bash
python python/run_stage27t.py ... --include-c1
```

After the calculation:

```bash
python python/audit_stage27t_results.py _stage27t_two_sided_results_20260903
```

Required success marker:

```text
STAGE27T_TWO_SIDED_AUDIT_OK
```

Do not run Stage28 after this. Return the complete result directory and audit marker to ChatGPT for independent review.
