#!/usr/bin/env bash
set -euo pipefail
: "${STAGE27U_RETRY3_DIR:?set STAGE27U_RETRY3_DIR}"
OUT="${STAGE27U_RETRY4_TRIAGE_OUT:-_stage27u_retry4_triage_20260903}"
python stage27u_retry4_triage/selftest_triage.py
python stage27u_retry4_triage/restricted_dual_triage.py \
  --retry3-result-dir "$STAGE27U_RETRY3_DIR" \
  --outdir "$OUT"
python stage27u_retry4_triage/audit_triage.py \
  --retry3-result-dir "$STAGE27U_RETRY3_DIR" \
  --triage-dir "$OUT"
