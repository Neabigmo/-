#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PKG="$ROOT/chi2_n3_ou_coherent_stage27u_retry2_2026-09-03"
PATCH="$ROOT/stage27u_retry3_patch"
STAGE27R_DIR="${STAGE27R_DIR:?set STAGE27R_DIR}"
STAGE27S_DIR="${STAGE27S_DIR:?set STAGE27S_DIR}"
OUTDIR="${OUTDIR:-_stage27u_retry3_results_20260903}"

python "$PKG/verify_package.py"
python "$PKG/python/selftest_stage27u.py"
python "$PATCH/selftest_retry3.py"

ARGS=(--stage27r-dir "$STAGE27R_DIR" --stage27s-dir "$STAGE27S_DIR" --outdir "$OUTDIR")
if [[ -n "${STAGE15_DIR:-}" ]]; then ARGS+=(--stage15-dir "$STAGE15_DIR"); fi
if [[ -n "${STAGE16_DIR:-}" ]]; then ARGS+=(--stage16-dir "$STAGE16_DIR"); fi

python "$PATCH/run_stage27u_retry3.py" "${ARGS[@]}"
python "$PATCH/audit_retry3.py" --result-dir "$OUTDIR"
