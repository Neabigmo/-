#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PATCH4 = Path(__file__).resolve().parent
REPO = PATCH4.parent
PATCH3 = REPO / 'stage27u_retry3_patch'
PKG_ROOT = REPO / 'chi2_n3_ou_coherent_stage27u_retry2_2026-09-03'
PKG_PY = PKG_ROOT / 'python'
sys.path.insert(0, str(PKG_PY))
sys.path.insert(0, str(PATCH3))
sys.path.insert(0, str(PATCH4))

from coherence_lift import complete_low_lift_high
from dual_prune_retry4 import single_witness_mp_lb, CERT_MARGIN


def audit_prunes(result_dir: Path):
    p = result_dir / 'stage27u_retry4_dual_prune.csv'
    if not p.exists():
        raise AssertionError('missing stage27u_retry4_dual_prune.csv')
    df = pd.read_csv(p)
    if len(df) == 0:
        return 0
    required = {
        'N','q_high','q_low','A','ridge','prefix_energy','witness_lambda','witness_s',
        'dual_lb_mp_low','dual_lb_mp_high','dual_lb_conservative','mp_rel_gap',
        'margin_lb_conservative','dps_low','dps_high','qp_success','y_json','status'
    }
    missing = required - set(df.columns)
    if missing:
        raise AssertionError(f'missing retry4 prune columns: {sorted(missing)}')

    for i, r in df.iterrows():
        if str(r.status) != 'POINTWISE_SINGLE_WITNESS_PRUNE':
            raise AssertionError((i,'unexpected prune status',r.status))
        if str(r.qp_success).lower() in ('true','1'):
            raise AssertionError((i,'prune row came from successful full QP'))
        N=int(r.N); qh=float(r.q_high); ql=float(r.q_low); A=float(r.A); ridge=float(r.ridge)
        y=np.asarray(json.loads(r.y_json),float)
        cc=complete_low_lift_high(y,N,ql,qh)
        w=(float(r.witness_lambda),float(r.witness_s))
        rep=single_witness_mp_lb(qh,N,cc.u_high,w,ridge=ridge,dps=max(360,int(r.dps_high)+40))
        replay_margin=float(cc.prefix_energy_high)+float(rep['lb'])-A
        recorded=float(r.margin_lb_conservative)
        if not np.isfinite(replay_margin) or replay_margin < CERT_MARGIN:
            raise AssertionError((i,'replayed prune margin below certificate threshold',replay_margin))
        if replay_margin + 2e-8*(1+abs(replay_margin)+abs(recorded)) < recorded:
            raise AssertionError((i,'retry4 conservative replay violated',replay_margin,recorded))
        if float(r.mp_rel_gap) > 1e-10:
            raise AssertionError((i,'runtime MP pair not stable',float(r.mp_rel_gap)))
    return len(df)


def run_retry3_audit(result_dir: Path):
    import audit_retry3 as a3
    saved=sys.argv[:]
    try:
        sys.argv=['audit_retry3.py','--result-dir',str(result_dir)]
        a3.main()
    finally:
        sys.argv=saved


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--result-dir',required=True); a=ap.parse_args()
    rd=Path(a.result_dir)
    n=audit_prunes(rd)
    run_retry3_audit(rd)
    print(f'STAGE27U_RETRY4_DUAL_PRUNE_AUDIT_OK prunes={n}')

if __name__=='__main__':
    main()
