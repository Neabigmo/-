# Running Stage27U

## Required external inputs

Set two directories:

- `STAGE27R_DIR`: a Stage27R result tree containing the two q=.10 robust artifact NPZ files
  listed in `MANIFEST.txt`.
- `STAGE27S_DIR`: a Stage27S result tree containing `stage27s_continuum.csv`.
  `stage27s_exchange_history.csv` is optional but recommended and is automatically used when present.

Optional:

- `STAGE15_DIR`: prior Stage15 result tree for conservative candidate discovery.
- `STAGE16_DIR`: prior Stage16 result tree for conservative candidate discovery.

The candidate loader accepts only files with explicit q metadata and normalized-u semantics;
ambiguous old vectors are ignored rather than guessed.

## Install and selftest

```bash
python -m pip install -r requirements.txt
python python/selftest_stage27u.py
```

Expected marker:

    STAGE27U_SELFTEST_OK

## Production run

```bash
export STAGE27R_DIR=/path/to/stage27r_results
export STAGE27S_DIR=/path/to/stage27s_results
# optional:
# export STAGE15_DIR=/path/to/stage15_results
# export STAGE16_DIR=/path/to/stage16_results

bash run_stage27u_remote.sh
```

The default campaign is exactly N=32,48,64,80 with 32 random energy-bounded starts per N,
plus zero, previous-N continuation, and any safely loaded prior candidates.

The runner does not start Stage28.

## Independent audit

The shell runner automatically executes

```bash
python python/audit_stage27u_results.py --result-dir _stage27u_ou_coherent_results_20260903
```

Expected success marker:

    STAGE27U_OU_COHERENT_AUDIT_OK

After that marker, stop and return the complete result directory to ChatGPT for independent review.
