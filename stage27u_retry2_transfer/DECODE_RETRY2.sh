#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
B64="$ROOT/chi2_n3_ou_coherent_stage27u_retry2_2026-09-03.zip.b64"
ZIP="$ROOT/chi2_n3_ou_coherent_stage27u_retry2_2026-09-03.zip"
EXPECTED="06891c56715dc9da13a927ee34d77db8b8c725d59a2ddbe5eabc165bbf1d25f3"
base64 -d "$B64" > "$ZIP"
ACTUAL="$(sha256sum "$ZIP" | awk '{print $1}')"
if [[ "$ACTUAL" != "$EXPECTED" ]]; then
  echo "SHA256_MISMATCH expected=$EXPECTED actual=$ACTUAL" >&2
  rm -f "$ZIP"
  exit 2
fi
echo "STAGE27U_RETRY2_ZIP_SHA256_OK $ACTUAL"
echo "$ZIP"
