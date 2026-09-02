#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,traceback
from pathlib import Path
import numpy as np
import pandas as pd

from coherence_lift import (odd_indices,lift_direct_relative_error,complete_low_lift_high)
from master_kernel import feature_identity_error,direct_vs_master_prefix_error,direct_master_full_kernel_error
from candidate_loader import discover_candidates,candidate_high_odd
from outer_minimax import random_ball_starts,multistart_search,CoherentObjective,local_search
from continuum_validation import dedupe,tail_lower_bound,validate_fixed_candidate

QLOW=.05; QHIGH=.10; RIDGE=1e-11; NS=[32,48,64,80]


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
            except Exception as e:
                out_rows.append(dict(candidate=name,N=N,status='CANDIDATE_AUDIT_FAILED',error=repr(e)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stage27r-dir',required=True);ap.add_argument('--stage27s-dir',required=True)
    ap.add_argument('--stage15-dir',action='append',default=[]);ap.add_argument('--stage16-dir',action='append',default=[])
    ap.add_argument('--outdir',default='_stage27u_ou_coherent_results_20260903')
    ap.add_argument('--random-starts',type=int,default=32);ap.add_argument('--level2-finalists',type=int,default=6)
    ap.add_argument('--outer-maxiter',type=int,default=180);ap.add_argument('--continuum-max-outer',type=int,default=6)
    ap.add_argument('--Ns',default='32,48,64,80');ap.add_argument('--skip-existing-candidate-audit',action='store_true')
    a=ap.parse_args();od=Path(a.outdir);od.mkdir(parents=True,exist_ok=True);(od/'candidate_artifacts').mkdir(exist_ok=True)
    log=(od/'stage27u_run.log').open('w',encoding='utf-8',buffering=1)
    def say(*x):
        z=' '.join(map(str,x));print(z,flush=True);print(z,file=log,flush=True)
    failures=[]
    lift=regression_rows();pd.DataFrame(lift).to_csv(od/'stage27u_lift_validation.csv',index=False)
    ident=kernel_identity_rows();pd.DataFrame(ident).to_csv(od/'stage27u_kernel_identity.csv',index=False)
    pd.DataFrame(ident).to_csv(od/'stage27u_coherence_identity.csv',index=False)
    if max(r['max_relative_error'] for r in lift)>1e-7:
        raise RuntimeError('COHERENCE_IMPLEMENTATION_ERROR: direct/lift regression too large')
    if max(max(r['feature_error_160'],r['feature_error_240'],r['kernel_error']) for r in ident)>1e-20:
        raise RuntimeError('COHERENCE_IMPLEMENTATION_ERROR: feature/kernel identity failed')
    W,wsources=load_witnesses(a.stage27r_dir,a.stage27s_dir);say('WITNESS_POOL',len(W),wsources)
    cand_roots=list(a.stage15_dir)+list(a.stage16_dir)
    candidates,skipped=discover_candidates(cand_roots);say('CANDIDATES',len(candidates),'SKIPPED_ROOTS',len(skipped))
    ca=[]
    if not a.skip_existing_candidate_audit: existing_candidate_audit(candidates,W,ca)
    pd.DataFrame(ca).to_csv(od/'stage27u_existing_candidate_audit.csv',index=False)
    all_outer=[];all_hist=[];all_cont=[];support_rows=[];prev_best=None
    campaign_Ns=[int(x) for x in str(a.Ns).split(',') if str(x).strip()]
    for N in campaign_Ns:
        dim=len(odd_indices(N));starts=random_ball_starts(dim,a.random_starts,seed=20260903+N)
        if prev_best is not None:
            y=np.zeros(dim);y[:min(dim,len(prev_best))]=prev_best[:min(dim,len(prev_best))];starts.insert(1,y)
        for c in candidates:
            try:
                y=candidate_high_odd(c,N,QHIGH)
                if np.dot(y,y)<=5.0*(1+1e-12):starts.append(y)
            except Exception:pass
        level1,calls=multistart_search(N,W,starts,q_low=QLOW,q_high=QHIGH,A=5,ridge=RIDGE,dps=180,maxiter=a.outer_maxiter)
        for r in level1:
            all_outer.append(dict(N=N,phase='LEVEL1',start_id=r.get('start_id'),margin=r.get('margin'),
                                  total_lb=r.get('total_lb'),prefix_energy=r.get('prefix_energy'),tail_lb=r.get('tail_lb'),
                                  success=r.get('success'),message=r.get('message'),grad_fd_error=r.get('grad_fd_error'),
                                  y_json=(y_json(r['y']) if 'y' in r else None)))
        finalists=[r for r in level1 if 'y' in r][:max(1,a.level2_finalists)]
        pooled=list(W);validated=[]
        for rank,r in enumerate(finalists):
            try:
                cc=complete_low_lift_high(r['y'],N,QLOW,QHIGH)
                vr=validate_fixed_candidate(QHIGH,N,cc.u_high,pooled,ridge=RIDGE,dps=220,max_outer=a.continuum_max_outer)
                pooled=dedupe(pooled+vr['witnesses']);tot=cc.prefix_energy_high+max(0.0,float(vr['m2']))
                validated.append((tot-5,r['y'],cc,vr))
                all_cont.append(dict(N=N,rank=rank,status=vr['status'],margin=tot-5,total_lb=tot,
                                     prefix_energy=cc.prefix_energy_high,tail_lb=vr['m2'],witness_count=len(vr['witnesses']),
                                     y_json=y_json(r['y'])))
                for h in vr['history']:all_hist.append(dict(N=N,rank=rank,**h))
            except Exception as e:
                failures.append(dict(N=N,phase='continuum',rank=rank,error=repr(e),traceback=traceback.format_exc(limit=8)))
        refined=[];obj=CoherentObjective(N,pooled,q_low=QLOW,q_high=QHIGH,A=5,ridge=RIDGE,dps=200)
        for rank,r in enumerate(finalists[:4]):
            try:
                rr=local_search(obj,r['y'],maxiter=max(80,a.outer_maxiter//2));ev=rr['eval'];refined.append((ev.value,rr['y'],ev))
                all_outer.append(dict(N=N,phase='LEVEL2_REOPT',start_id=rank,margin=ev.value,total_lb=ev.total_lb,
                                      prefix_energy=ev.prefix_energy,tail_lb=ev.tail_lb,success=rr['success'],message=rr['message'],
                                      y_json=y_json(rr['y'])))
            except Exception as e:failures.append(dict(N=N,phase='reopt',rank=rank,error=repr(e)))
        pool_candidates=[]
        for z in validated:pool_candidates.append((z[0],z[1]))
        for z in refined:pool_candidates.append((z[0],z[1]))
        for r in finalists:pool_candidates.append((r['margin'],r['y']))
        pool_candidates.sort(key=lambda x:x[0]);_,best_y=pool_candidates[0];best_y=np.asarray(best_y,float)
        ccfinal=complete_low_lift_high(best_y,N,QLOW,QHIGH)
        try:
            vfinal=validate_fixed_candidate(QHIGH,N,ccfinal.u_high,pooled,ridge=RIDGE,dps=220,max_outer=a.continuum_max_outer)
            pooled=dedupe(pooled+vfinal['witnesses']);final_margin=ccfinal.prefix_energy_high+max(0.0,float(vfinal['m2']))-5.0
            final_status=vfinal['status']
            all_cont.append(dict(N=N,rank='FINAL',status=final_status,margin=final_margin,total_lb=final_margin+5.0,
                                 prefix_energy=ccfinal.prefix_energy_high,tail_lb=vfinal['m2'],witness_count=len(pooled),y_json=y_json(best_y)))
            for h in vfinal['history']:all_hist.append(dict(N=N,rank='FINAL',**h))
        except Exception as e:
            failures.append(dict(N=N,phase='final_continuum',error=repr(e),traceback=traceback.format_exc(limit=8)))
            fobj=CoherentObjective(N,pooled,q_low=QLOW,q_high=QHIGH,A=5,ridge=RIDGE,dps=200);fev=fobj.evaluate(best_y)
            final_margin=float(fev.value);final_status='FINAL_CONTINUUM_FAILED'
        prev_best=best_y
        all_outer.append(dict(N=N,phase='FINAL_VALIDATED',start_id=-1,margin=final_margin,total_lb=final_margin+5.0,
                              prefix_energy=ccfinal.prefix_energy_high,tail_lb=(final_margin+5.0-ccfinal.prefix_energy_high),
                              success=(final_status!='FINAL_CONTINUUM_FAILED'),message=final_status,y_json=y_json(best_y)))
        np.savez_compressed(od/'candidate_artifacts'/f'N{N}_best.npz',y_high=prev_best,witnesses=np.asarray(pooled,float),q_low=QLOW,q_high=QHIGH,N=N,
                            reported_margin=final_margin,continuum_status=np.asarray(final_status))
        for j,w in enumerate(pooled):support_rows.append(dict(N=N,index=j,lambda_=w[0],s=w[1]))
        say('STAGE27U_N',N,'BEST_MARGIN',final_margin,'STATUS',final_status,'W',len(pooled),'STARTS',len(starts),'CALLS',calls)
    pd.DataFrame(all_outer).to_csv(od/'stage27u_outer_search.csv',index=False)
    pd.DataFrame(all_hist).to_csv(od/'stage27u_outer_history.csv',index=False)
    pd.DataFrame(all_cont).to_csv(od/'stage27u_continuum_validation.csv',index=False)
    pd.DataFrame(support_rows).to_csv(od/'stage27u_active_support.csv',index=False)
    pd.DataFrame(failures).to_csv(od/'stage27u_failures.csv',index=False)
    odf=pd.DataFrame(all_outer);frows=odf[odf.phase.astype(str)=='FINAL_VALIDATED'] if len(odf) else pd.DataFrame()
    best_by_N={int(r.N):float(r.margin) for _,r in frows.iterrows()} if len(frows) else {}
    margins=list(best_by_N.values());cdf=pd.DataFrame(all_cont)
    stationary_negative=False
    if len(cdf):
        fin=cdf[cdf['rank'].astype(str)=='FINAL']
        stationary_negative=bool(np.any((fin.status.astype(str)=='COHERENT_CONTINUUM_STATIONARY') & (fin.margin.astype(float)<-0.1))) if len(fin) else False
    if margins and len(margins)==len(campaign_Ns) and min(margins)>=0.1:status='COHERENT_HIGHQ_OBSTRUCTION_STRONG_NUMERIC_EVIDENCE'
    elif stationary_negative:status='COHERENT_SURVIVOR_FOUND'
    else:status='COHERENT_OUTER_MINIMAX_UNRESOLVED'
    summary=dict(stage='Stage27U OU-coherent lifted minimax',q_low=QLOW,q_high=QHIGH,ridge=RIDGE,
                 lift_validation_max_error=max(r['max_relative_error'] for r in lift),
                 kernel_identity_max_error=max(max(r['feature_error_160'],r['feature_error_240'],r['kernel_error']) for r in ident),
                 witness_seed_count=len(W),loaded_existing_candidates=len(candidates),best_margin_by_N=best_by_N,
                 failures=len(failures),status=status,
                 note='Low-q is used only for stable Fock completion; obstruction is evaluated at high q=0.10. No Stage28 or theorem claim.')
    (od/'stage27u_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    say('STAGE27U_COMPLETED',json.dumps(summary,sort_keys=True));log.close()

if __name__=='__main__':main()
