#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
STAGE27R_DIR="${STAGE27R_DIR:?set STAGE27R_DIR to Stage27R result tree}"
STAGE27S_DIR="${STAGE27S_DIR:?set STAGE27S_DIR to Stage27S result tree}"
OUTDIR="${OUTDIR:-_stage27u_retry2_results_20260903}"
python "$ROOT/python/selftest_stage27u.py"
ARGS=(--stage27r-dir "$STAGE27R_DIR" --stage27s-dir "$STAGE27S_DIR" --outdir "$OUTDIR")
if [[ -n "${STAGE15_DIR:-}" ]]; then ARGS+=(--stage15-dir "$STAGE15_DIR"); fi
if [[ -n "${STAGE16_DIR:-}" ]]; then ARGS+=(--stage16-dir "$STAGE16_DIR"); fi
python "$ROOT/python/run_stage27u.py" "${ARGS[@]}"
python "$ROOT/python/audit_stage27u_results.py" --result-dir "$OUTDIR"
