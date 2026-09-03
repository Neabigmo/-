#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np, pandas as pd
from restricted_dual_triage import restricted_bounds


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--retry3-result-dir',required=True); ap.add_argument('--triage-dir',required=True); a=ap.parse_args()
    rd=Path(a.retry3_result_dir); td=Path(a.triage_dir)
    df=pd.read_csv(td/'stage27u_retry4_triage.csv')
    assert set(df.N.astype(int))=={32,48,64,80}
    for _,r in df.iterrows():
        N=int(r.N); z=np.load(rd/'candidate_artifacts'/f'N{N}_best.npz',allow_pickle=False)
        rr=restricted_bounds(N,np.asarray(z['y_high'],float),np.asarray(z['witnesses'],float),dps=340,topk=16)
        for key in ('prefix_energy','single_lb','pair_lb'):
            old=float(r[key]); new=float(rr[key])
            if not np.isfinite(old) or not np.isfinite(new): raise AssertionError((N,key,old,new))
            if key=='prefix_energy':
                if abs(old-new)>2e-8*(1+abs(old)+abs(new)): raise AssertionError((N,key,old,new))
            else:
                if new+2e-7*(1+abs(old)+abs(new)) < old: raise AssertionError((N,key,old,new))
        status=str(r.status)
        if status.endswith('POINTWISE_POSITIVE') and max(rr['prefix_margin'],rr['single_margin'],rr['pair_margin'])<0.1:
            raise AssertionError((N,'positive status failed high precision replay',rr))
    print('STAGE27U_RETRY4_TRIAGE_AUDIT_OK')

if __name__=='__main__': main()
