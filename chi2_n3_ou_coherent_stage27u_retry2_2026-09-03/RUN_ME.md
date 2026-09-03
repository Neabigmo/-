# Stage27U retry2 — run instructions

This is a numerical-repair rerun of Stage27U, not Stage28 and not a theorem certificate.


## Verify cloned package first

This retry2 transfer is intended to be cloned as a complete Git tree. No ZIP/base64 decode is required.

From the package root, run:

```bash
python verify_package.py
```

Expected:

```text
STAGE27U_RETRY2_PACKAGE_VERIFY_OK files=28
```

The repository includes `.gitattributes` forcing LF line endings for shell/Python/text files, so a Windows clone can be copied to the Linux remote without the previous CRLF decode-script problem.

## Required inputs

Set these to existing result trees:

```bash
export STAGE27R_DIR=/path/to/stage27r_psd_repair_results
export STAGE27S_DIR=/path/to/stage27s_continuum_results
```

Required under `STAGE27R_DIR` (recursive lookup):

- `q0p1_N64_ridge1em11.npz`
- `q0p1_N80_ridge1em11.npz`

Required under `STAGE27S_DIR`:

- `stage27s_continuum.csv`

Recommended if present:

- `stage27s_exchange_history.csv`

Optional prior-candidate roots:

```bash
export STAGE15_DIR=/path/to/stage15_results
export STAGE16_DIR=/path/to/stage16_results
```

## Install / selftest

```bash
python -m pip install -r requirements.txt
python python/selftest_stage27u.py
```

Expected:

```text
STAGE27U_RETRY2_SELFTEST_OK
```

## Production run

```bash
bash run_stage27u_remote.sh
```

Default output:

```text
_stage27u_retry2_results_20260903/
```

The runner performs a deterministic interior/active-set-stable gradient audit *before* the outer campaign.  It stops immediately if fewer than two stable gradient checks per N pass or the maximum relative FD error exceeds `2e-3`.

Final independent audit marker:

```text
STAGE27U_RETRY2_NUMERIC_AUDIT_OK
```

Do not interpret that marker as a theorem certificate.  It only certifies numerical bookkeeping and replay consistency for this campaign.
