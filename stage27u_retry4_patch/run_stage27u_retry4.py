#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

PATCH4 = Path(__file__).resolve().parent
REPO = PATCH4.parent
PATCH3 = REPO / 'stage27u_retry3_patch'
PKG_ROOT = REPO / 'chi2_n3_ou_coherent_stage27u_retry2_2026-09-03'
PKG_PY = PKG_ROOT / 'python'

sys.path.insert(0, str(PKG_PY))
sys.path.insert(0, str(PATCH3))
sys.path.insert(0, str(PATCH4))

import outer_minimax as om
from dual_prune_retry4 import install_retry4, write_prune_csv
install_retry4(om)

import run_stage27u_preflight as pre
from gradient_audit_retry3 import gradient_audit_rows_retry3, gradient_spot_check_retry3
om.gradient_spot_check = gradient_spot_check_retry3
pre.gradient_audit_rows = gradient_audit_rows_retry3

import run_stage27u_campaign as campaign
import run_stage27u as base
base.run_preflight = pre.run_preflight
base.run_campaign = campaign.run_campaign


def _outdir_from_argv():
    default = '_stage27u_retry4_results_20260903'
    for i, a in enumerate(sys.argv[:-1]):
        if a == '--outdir':
            return Path(sys.argv[i+1])
        if a.startswith('--outdir='):
            return Path(a.split('=',1)[1])
    sys.argv.extend(['--outdir', default])
    return Path(default)


if __name__ == '__main__':
    od = _outdir_from_argv()
    try:
        base.main()
    finally:
        od.mkdir(parents=True, exist_ok=True)
        write_prune_csv(od / 'stage27u_retry4_dual_prune.csv')
