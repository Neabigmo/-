#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,traceback
from pathlib import Path
import numpy as np
import pandas as pd

from coherence_lift import (odd_indices,lift_direct_relative_error,complete_low_lift_high,scaled_completion_probe)
from master_kernel import feature_identity_error,direct_vs_master_prefix_error,direct_master_full_kernel_error
from candidate_loader import discover_candidates,candidate_high_odd
from outer_minimax import energy_calibrated_starts,multistart_search,CoherentObjective,local_search,gradient_spot_check
from continuum_validation import dedupe,tail_lower_bound,validate_fixed_candidate

QLOW=.05; QHIGH=.10; RIDGE=1e-11; DEFAULT_NS=[32,48,64,80]


def find_one(root,name,required=True):
    root=Path(root);p=root/name
    if p.exists():return p
    xs=list(root.rglob(name))
    if xs:return xs[0]
    if required:raise FileNotFoundError(f'{name} not found under {root}')
    return None


def load_witnesses(stage27r,stage27s):
    W=[];sources=[]
    for name in ('q0p1_N64_ridge1em11.npz','q0p1_N80_ridge1em11.npz'):
        p=find_one(stage27r,name)
        z=np.load(p,allow_pickle=False); ww=np.asarray(z['witnesses'],float)
        for x in ww:W.append(tuple(map(float,x)))
        sources.append(dict(source=str(p),count=len(ww)))
    cfile=find_one(stage27s,'stage27s_continuum.csv')
    cdf=pd.read_csv(cfile)
    for label in ('C1','D'):
        g=cdf[cdf.label.astype(str)==label]
        if len(g):
            r=g.iloc[-1]
            if 'eta_lambda' in r and 'eta_s' in r and np.isfinite(float(r.eta_lambda)) and np.isfinite(float(r.eta_s)):
                W.append((float(r.eta_lambda),float(r.eta_s)))
    hfile=find_one(stage27s,'stage27s_exchange_history.csv',required=False)
    if hfile is not None:
        hdf=pd.read_csv(hfile)
        for label in ('C1','D'):
            g=hdf[hdf.label.astype(str)==label]
            for _,r in g.iterrows():
                if 'lambda_star' in r and 's_star' in r and np.isfinite(float(r.lambda_star)) and np.isfinite(float(r.s_star)):
                    W.append((float(r.lambda_star),float(r.s_star)))
        sources.append(dict(source=str(hfile),count=len(hdf)))
    return dedupe(W),sources


def y_json(y):return json.dumps([float(x) for x in np.asarray(y,float)])


def regression_rows():
    rows=[];rng=np.random.default_rng(20260903)
    for N in (32,48,64,80):
        dim=len(odd_indices(N));tests=[np.zeros(dim)]
        for amp in (1e-4,1e-3,1e-2):tests.append(rng.normal(size=dim)*amp/max(1,math.sqrt(dim)))
        for i,y in enumerate(tests):
            err,cc,uh,rh=lift_direct_relative_error(y,N,QLOW,QHIGH)
            rows.append(dict(N=N,test=i,max_relative_error=err,low_fock_residual=cc.fock_residual_low,
                             direct_high_fock_residual=rh,prefix_energy_high=cc.prefix_energy_high))
    return rows


def kernel_identity_rows():
    rows=[];rng=np.random.default_rng(27003)
    for N in (32,80,160):
        for i in range(8):
            q=float(rng.choice([.04,.05,.064,.08,.10]));lam=float(rng.uniform(0,.98));s=float(rng.uniform(-4.5,4.5))
            e1=feature_identity_error(q,lam,s,N,dps=160);e2=direct_vs_master_prefix_error(q,lam,s,N,dps=240)
            q2=float(rng.choice([.05,.10]));w2=(float(rng.uniform(0,.95)),float(rng.uniform(-4,4)))
            ek=direct_master_full_kernel_error(q,(lam,s),q2,w2,dps=180)
            rows.append(dict(N=N,q=q,lambda_=lam,s=s,feature_error_160=e1,feature_error_240=e2,kernel_error=ek))
    return rows


def gradient_audit_rows(W,Ns):
    rows=[];rng=np.random.default_rng(27112026)
    for N in Ns:
        dim=len(odd_indices(N));obj=CoherentObjective(N,W,q_low=QLOW,q_high=QHIGH,A=5,ridge=RIDGE,dps=180)
        tests=[('zero',np.zeros(dim,float))]
        for k,amp in enumerate((2e-3,1e-2,3e-2,7e-2)):
            z=rng.normal(size=dim);z/=max(np.linalg.norm(z),1e-300);tests.append((f'random_{k}',z*amp))
        for name,y in tests:
            try:
                ev=obj.evaluate(y);gc=gradient_spot_check(obj,y,max_dirs=min(6,dim),h=8e-7)
                rows.append(dict(N=N,test=name,status=gc['status'],grad_fd_error=gc['error'],
                                 checked_directions=gc['count'],scientific_valid=ev.scientific_valid,
                                 eval_status=ev.status,prefix_energy=ev.prefix_energy,tail_lb=ev.tail_lb,
                                 ball_slack=5.0-float(y@y)))
            except Exception as exc:
                rows.append(dict(N=N,test=name,status='GRADIENT_TEST_EXCEPTION',grad_fd_error=math.nan,
                                 checked_directions=0,scientific_valid=False,eval_status='EXCEPTION',
                                 prefix_energy=math.nan,tail_lb=math.nan,ball_slack=5.0-float(y@y),error=repr(exc)))
    return rows


def existing_candidate_audit(candidates,W,out_rows):
    records=[('ZERO',None)] + [(c.name,c) for c in candidates]
    for name,c in records:
        for N in (64,80,128,160):
            try:
                if c is None:y=np.zeros(len(odd_indices(N)),float);src='zero';sem='zero'
                else:
                    y=candidate_high_odd(c,N,QHIGH);src=c.source;sem=c.semantics
                cc=complete_low_lift_high(y,N,QLOW,QHIGH);E=cc.prefix_energy_high
                row=dict(candidate=name,source=src,semantics=sem,N=N,prefix_energy_high=E,
                         D_A2_prefix=E-2,D_A5_prefix=E-5,fock_residual=cc.fock_residual_low)
                if E>5:
                    row.update(status='PREFIX_ENERGY_KILLS_A5',tail_lb=0.0,total_lb=E,D_A5=E-5)
                else:
                    qp,joint,_=tail_lower_bound(QHIGH,N,cc.u_high,W,ridge=RIDGE,dps=180)
                    total=E+max(0.0,qp.m2_dual)
                    row.update(status='FINITE_WITNESS_AUDIT',tail_lb=qp.m2_dual,total_lb=total,D_A5=total-5,
                               raw_min_eig=joint['raw_corr_min_eig'],kkt=qp.projected_kkt_inf,comp=qp.complementarity_inf)
                out_rows.append(row)
            except FloatingPointError as exc:
                probe=scaled_completion_probe(y,N,QLOW,QHIGH,energy_cut=30.0)
                out_rows.append(dict(candidate=name,source=(src if 'src' in locals() else ''),semantics=(sem if 'sem' in locals() else ''),N=N,
                                     status=('CANDIDATE_PREFIX_OVERFLOW_BARRIER' if probe.get('definitely_over_cut') else 'CANDIDATE_NUMERIC_FAILED'),
                                     error=repr(exc),probe_status=probe.get('status'),energy_lower_bound=probe.get('energy_lower_bound',math.nan)))
            except Exception as exc:
                out_rows.append(dict(candidate=name,N=N,status='CANDIDATE_AUDIT_FAILED',error=repr(exc)))


def _append_outer_row(all_outer,N,phase,r,default_id=None):
    all_outer.append(dict(N=N,phase=phase,start_id=r.get('start_id',default_id),margin=r.get('margin'),
                          total_lb=r.get('total_lb'),prefix_energy=r.get('prefix_energy'),tail_lb=r.get('tail_lb'),
                          scientific_valid=r.get('scientific_valid',True),eval_status=r.get('eval_status',''),
                          success=r.get('success'),message=r.get('message'),grad_fd_error=r.get('grad_fd_error'),
                          grad_check_status=r.get('grad_check_status'),grad_check_count=r.get('grad_check_count'),
                          y_json=(y_json(r['y']) if 'y' in r else None)))
