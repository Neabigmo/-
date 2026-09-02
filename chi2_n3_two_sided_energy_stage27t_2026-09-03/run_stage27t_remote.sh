#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 2 ]; then
  echo "usage: $0 STAGE27R_RESULT_DIR STAGE27S_RESULT_DIR [OUTDIR]" >&2
  exit 2
fi
R="$1"; S="$2"; O="${3:-_stage27t_two_sided_results_20260903}"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
python python/selftest_stage27t.py
mkdir -p "$O"
python python/run_stage27t.py --stage27r-dir "$R" --stage27s-dir "$S" --outdir "$O" --s-grid 241 --refine-k 20 --max-outer 20 2>&1 | tee "$O/console.log"
python python/audit_stage27t_results.py "$O" | tee "$O/audit.log"
