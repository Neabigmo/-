#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
import pandas as pd
from mp_features import density_mp

EXPECTED={'A','B','C1','C2','C3','C4','C5','D'}

def as_bool(x):
    if isinstance(x,(bool,np.bool_)): return bool(x)
    return str(x).strip().lower() in ('1','true','yes')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('result_dir');a=ap.parse_args();p=Path(a.result_dir)
    req=['stage27t_zero_tail_audit.csv','stage27t_primal_reconstruction.csv','stage27t_feature_audit.csv','stage27t_energy_brackets.csv','stage27t_summary.json']
    for x in req:
        if not (p/x).exists():raise SystemExit('missing '+x)
    b=pd.read_csv(p/'stage27t_energy_brackets.csv');pr=pd.read_csv(p/'stage27t_primal_reconstruction.csv');fa=pd.read_csv(p/'stage27t_feature_audit.csv')
    if set(b.label)!=EXPECTED:raise SystemExit(f'bracket labels mismatch {set(b.label)}')
    if len(fa):
        if not fa.feature_valid.fillna(False).all():raise SystemExit('feature audit has invalid row')
        if (fa.max_diag_error.astype(float)>1e-10).any():raise SystemExit('feature diag error')
        if (fa.max_corr_excess.astype(float)>1e-10).any():raise SystemExit('feature corr excess')
        if (fa.max_cross_precision_error.astype(float)>1e-10).any():raise SystemExit('feature cross precision')
    validated=pr[pr.status=='PRIMAL_UPPER_BOUND_VALIDATED'] if len(pr) else pr
    for _,r in validated.iterrows():
        zpath=p/'primal_artifacts'/f'{r.label}_L{int(r.L)}.npz'
        if not zpath.exists():raise SystemExit('missing artifact '+str(zpath))
        z=np.load(zpath);v=z['v'];u=z['u'];sl=z['final_slacks'];wp=z['worst_point']
        E=float(v@v)
        if abs(E-float(r.energy))>2e-7*(1+abs(E)):raise SystemExit(f'{r.label} energy mismatch')
        if float(np.min(sl))<-1e-8:raise SystemExit(f'{r.label} constraint violation')
        q=float(r.q);N=int(r.N);eps=q**1.5
        zz=density_mp(q,eps,N,u,v,float(wp[0]),float(wp[1]),dps=180)
        if abs(zz-float(wp[2]))>1e-6*(1+abs(zz)):raise SystemExit(f'{r.label} worst density mismatch')
        if zz<-2e-8:raise SystemExit(f'{r.label} validated negative density')
        if as_bool(r.lambda_boundary) or as_bool(r.s_boundary):raise SystemExit(f'{r.label} validated boundary unresolved')
        if float(r.energy_rel_gap)>1e-6:raise SystemExit(f'{r.label} dual/primal energy gap')
    # Bracket logic must never invent an upper bound.
    for _,r in b.iterrows():
        if np.isfinite(float(r.primal_UB)):
            if float(r.primal_UB)<0:raise SystemExit('negative UB')
            if str(r.primal_status) not in ('PRIMAL_UPPER_BOUND_VALIDATED','ZERO_TAIL_WINDOW_VALIDATED'):
                raise SystemExit(f'{r.label} UB without validation')
    s=json.loads((p/'stage27t_summary.json').read_text())
    if s.get('nq_only_scaling_status')=='NQ_ONLY_SCALING_NUMERICALLY_REJECTED':
        c1=b[b.label=='C1'].iloc[0];small=b[b.label.isin(['C3','C4','C5'])]
        if not (float(c1.dual_LB)>=0.5 and np.any(np.isfinite(small.primal_UB.astype(float)) & (small.primal_UB.astype(float)<=1e-3))):
            raise SystemExit('invalid NQ rejection logic')
    print(f"STAGE27T_AUDIT validated_primal={len(validated)} bracket_rows={len(b)}")
    print('STAGE27T_TWO_SIDED_AUDIT_OK')
if __name__=='__main__':main()
