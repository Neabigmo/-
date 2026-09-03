#!/usr/bin/env bash
set -euo pipefail
: "${STAGE27R_DIR:?set STAGE27R_DIR}"
: "${STAGE27S_DIR:?set STAGE27S_DIR}"
OUT="${STAGE27U_RETRY4_OUT:-_stage27u_retry4_results_20260903}"
python stage27u_retry4_patch/selftest_retry4.py
python stage27u_retry4_patch/run_stage27u_retry4.py \
  --stage27r-dir "$STAGE27R_DIR" \
  --stage27s-dir "$STAGE27S_DIR" \
  --outdir "$OUT"
python stage27u_retry4_patch/audit_retry4.py --result-dir "$OUT"
