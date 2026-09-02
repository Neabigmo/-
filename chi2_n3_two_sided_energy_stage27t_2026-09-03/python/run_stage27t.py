#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,math,re,sys,traceback
from pathlib import Path
import numpy as np
import pandas as pd

from zero_tail_audit import audit_zero_tail
from stable_primal_tail import adaptive_reconstruct
from zero_branch import zero_branch_state

TARGETS={
 'A':(.05,80,4.0),'B':(.05,96,4.8),'C1':(.10,64,6.4),'C2':(.08,80,6.4),
 'C3':(.064,100,6.4),'C4':(.05,128,6.4),'C5':(.04,160,6.4),'D':(.10,80,8.0),
}
ZERO_LABELS=['A','B','C3','C4','C5']
PRIMAL_LABELS=['A','B','C2','C3','C4','C5']

def find_one(root,name):
    root=Path(root)
    p=root/name
    if p.exists():return p
    xs=list(root.rglob(name))
    if len(xs)==1:return xs[0]
    if not xs:raise FileNotFoundError(f'{name} not found under {root}')
    return xs[0]

def tag(q,n,ridge=1e-11):
    return f"q{q:.12g}".replace('.','p').replace('-','m')+f"_N{n}_ridge{ridge:.0e}".replace('-','m').replace('+','p')

def locate_artifact(root,q,n):
    name=tag(q,n)+'.npz'; return find_one(root,name)

def support_from_artifact(path,max_count=48):
    z=np.load(path,allow_pickle=False);W=np.asarray(z['witnesses'],float)
    a=np.asarray(z['alpha'],float) if 'alpha' in z else np.zeros(len(W));s=np.asarray(z['slack'],float) if 'slack' in z else np.zeros(len(W))
    ath=max(1e-14,1e-8*max(float(np.max(np.abs(a))) if len(a) else 0,1e-300));idx=list(np.where(a>ath)[0])
    for j in np.argsort(s):
        if int(j) not in idx:idx.append(int(j))
        if len(idx)>=max_count:break
    return [tuple(map(float,W[i])) for i in idx[:max_count]],np.asarray(z['u'],float)

def load_lower_bounds(stage27s):
    f=find_one(stage27s,'stage27s_continuum.csv');df=pd.read_csv(f);return {str(r.label):r.to_dict() for _,r in df.iterrows()}

def save_npz(od,label,L,sol,aud,W,u):
    pd=(od/'primal_artifacts');pd.mkdir(exist_ok=True)
    np.savez_compressed(pd/f'{label}_L{L}.npz',v=sol.v,u=u,witnesses=np.asarray(W,float),
                        row_scales=sol.system.row_scales,row_scales_log10=sol.system.row_scales_log10,
                        final_slacks=sol.system.Phi@sol.v-sol.system.b,
                        worst_point=np.asarray([aud['lambda_star'],aud['s_star'],aud['min_density']],float),
                        Phi=sol.system.Phi,b=sol.system.b,G=sol.system.G)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stage27r-dir',required=True);ap.add_argument('--stage27s-dir',required=True);ap.add_argument('--outdir',default='_stage27t_two_sided_results_20260903')
    ap.add_argument('--s-grid',type=int,default=241);ap.add_argument('--refine-k',type=int,default=20);ap.add_argument('--max-outer',type=int,default=20)
    ap.add_argument('--include-c1',action='store_true')
    a=ap.parse_args();od=Path(a.outdir);od.mkdir(parents=True,exist_ok=True);(od/'primal_artifacts').mkdir(exist_ok=True)
    log=(od/'stage27t_run.log').open('w',encoding='utf-8',buffering=1)
    def say(*x):
        s=' '.join(map(str,x));print(s,flush=True);print(s,file=log,flush=True)
    lbs=load_lower_bounds(a.stage27s_dir);fail=[];zero_rows=[];zero_hist=[];pr_rows=[];pr_hist=[];feat=[]
    states={};supports={}
    for label,(q,n,k) in TARGETS.items():
        try:
            W,u= support_from_artifact(locate_artifact(a.stage27r_dir,q,n)); st=zero_branch_state(q,n);states[label]=st;supports[label]=W
            if np.max(np.abs(st.u-u))>1e-8*(1+np.max(np.abs(st.u))): say('WARN_U_MISMATCH',label)
        except Exception as e: fail.append(dict(label=label,phase='input',error=repr(e),traceback=traceback.format_exc(limit=8)))
    for label in ZERO_LABELS:
        if label not in states:continue
        st=states[label]
        try:
            r,h=audit_zero_tail(st.q,st.eps,st.N,st.u,s_grid=a.s_grid,refine_k=a.refine_k);r.update(label=label,q=st.q,N=st.N,kappa=st.kappa);zero_rows.append(r)
            for x in h: zero_hist.append(dict(label=label,q=st.q,N=st.N,kappa=st.kappa,**x))
            say('STAGE27T_ZERO',label,r['status'],'min=',r['min_density'])
        except Exception as e:fail.append(dict(label=label,phase='zero',error=repr(e),traceback=traceback.format_exc(limit=8)))
    zero_map={r['label']:r for r in zero_rows}
    labels=list(PRIMAL_LABELS)+(['C1'] if a.include_c1 else [])
    for label in labels:
        if label not in states:continue
        st=states[label]
        if label in zero_map and zero_map[label]['status']=='ZERO_TAIL_WINDOW_VALIDATED':
            say('STAGE27T_PRIMAL_SKIP_ZERO',label);continue
        Ls=[256] if label=='C1' else [64,128,256]
        any_valid=False
        for L in Ls:
            try:
                sol,aud,h,W,status=adaptive_reconstruct(st.q,st.eps,st.N,st.u,supports[label],L,max_outer=a.max_outer,s_grid=a.s_grid,refine_k=a.refine_k)
                row=dict(label=label,q=st.q,N=st.N,kappa=st.kappa,L=L,status=status,energy=sol.energy,dual_energy=sol.dual_energy,
                         min_constraint_slack=sol.min_slack,dual_projected_grad=sol.dual_projected_grad,complementarity=sol.complementarity,
                         energy_rel_gap=sol.energy_rel_gap,projection_updates=sol.projection_updates,min_density=aud['min_density'],
                         lambda_star=aud['lambda_star'],s_star=aud['s_star'],mp_density_error=aud['mp_error'],S_final=aud['S'],lambda_cap_final=aud['lambda_cap'],
                         lambda_boundary=aud['lambda_boundary'],s_boundary=aud['s_boundary'],feature_min_eigenvalue=sol.system.min_eigenvalue,
                         feature_max_diag_error=sol.system.max_diag_error,feature_max_corr_excess=sol.system.max_corr_excess,
                         feature_cross_precision_error=sol.cross_precision_error,dps_final=sol.dps_final,witness_count=len(W))
                pr_rows.append(row);save_npz(od,label,L,sol,aud,W,st.u)
                for x in h:pr_hist.append(dict(label=label,q=st.q,N=st.N,kappa=st.kappa,**x))
                feat.append(dict(label=label,q=st.q,N=st.N,kappa=st.kappa,L=L,support_count=len(sol.system.witnesses),
                                 min_eigenvalue=sol.system.min_eigenvalue,max_diag_error=sol.system.max_diag_error,max_corr_excess=sol.system.max_corr_excess,
                                 max_cross_precision_error=sol.cross_precision_error,dps_final=sol.dps_final,feature_valid=sol.feature_valid))
                say('STAGE27T_PRIMAL',label,'L',L,status,'E=',sol.energy,'mindens=',aud['min_density']);any_valid |= status=='PRIMAL_UPPER_BOUND_VALIDATED'
            except Exception as e:fail.append(dict(label=label,L=L,phase='primal',error=repr(e),traceback=traceback.format_exc(limit=10)));say('STAGE27T_PRIMAL_FAIL',label,L,repr(e))
        if label in ('C4','C5') and not any_valid:
            L=512
            try:
                sol,aud,h,W,status=adaptive_reconstruct(st.q,st.eps,st.N,st.u,supports[label],L,max_outer=a.max_outer,s_grid=a.s_grid,refine_k=a.refine_k)
                row=dict(label=label,q=st.q,N=st.N,kappa=st.kappa,L=L,status=status,energy=sol.energy,dual_energy=sol.dual_energy,
                         min_constraint_slack=sol.min_slack,dual_projected_grad=sol.dual_projected_grad,complementarity=sol.complementarity,
                         energy_rel_gap=sol.energy_rel_gap,projection_updates=sol.projection_updates,min_density=aud['min_density'],lambda_star=aud['lambda_star'],s_star=aud['s_star'],
                         mp_density_error=aud['mp_error'],S_final=aud['S'],lambda_cap_final=aud['lambda_cap'],lambda_boundary=aud['lambda_boundary'],s_boundary=aud['s_boundary'],
                         feature_min_eigenvalue=sol.system.min_eigenvalue,feature_max_diag_error=sol.system.max_diag_error,feature_max_corr_excess=sol.system.max_corr_excess,
                         feature_cross_precision_error=sol.cross_precision_error,dps_final=sol.dps_final,witness_count=len(W));pr_rows.append(row);save_npz(od,label,L,sol,aud,W,st.u)
                for x in h:pr_hist.append(dict(label=label,q=st.q,N=st.N,kappa=st.kappa,**x))
                feat.append(dict(label=label,q=st.q,N=st.N,kappa=st.kappa,L=L,support_count=len(sol.system.witnesses),min_eigenvalue=sol.system.min_eigenvalue,
                                 max_diag_error=sol.system.max_diag_error,max_corr_excess=sol.system.max_corr_excess,max_cross_precision_error=sol.cross_precision_error,dps_final=sol.dps_final,feature_valid=sol.feature_valid))
                say('STAGE27T_PRIMAL',label,'L',L,status,'E=',sol.energy,'mindens=',aud['min_density'])
            except Exception as e:fail.append(dict(label=label,L=L,phase='primal512',error=repr(e),traceback=traceback.format_exc(limit=10)))
    zdf=pd.DataFrame(zero_rows);pdf=pd.DataFrame(pr_rows);fdf=pd.DataFrame(feat)
    zdf.to_csv(od/'stage27t_zero_tail_audit.csv',index=False);pd.DataFrame(zero_hist).to_csv(od/'stage27t_zero_tail_history.csv',index=False)
    pdf.to_csv(od/'stage27t_primal_reconstruction.csv',index=False);pd.DataFrame(pr_hist).to_csv(od/'stage27t_primal_history.csv',index=False);fdf.to_csv(od/'stage27t_feature_audit.csv',index=False)
    pd.DataFrame(fail).to_csv(od/'stage27t_failures.csv',index=False)
    brackets=[]
    for label,(q,n,k) in TARGETS.items():
        lb=float(lbs[label]['m2']) if label in lbs else math.nan;ub=math.nan;bestL=math.nan;pstat='NOT_ATTEMPTED';dstat=str(lbs[label].get('status','MISSING')) if label in lbs else 'MISSING'
        zr=zero_map.get(label)
        if zr and zr['status']=='ZERO_TAIL_WINDOW_VALIDATED':ub=0.;bestL=0;pstat=zr['status']
        if len(pdf):
            g=pdf[(pdf.label==label)&(pdf.status=='PRIMAL_UPPER_BOUND_VALIDATED')]
            if len(g):
                rr=g.iloc[int(np.argmin(g.energy.astype(float)))];ub=float(rr.energy);bestL=int(rr.L);pstat=str(rr.status)
            elif label in set(pdf.label):pstat='PRIMAL_ATTEMPTED_NO_VALIDATED_UB'
        brackets.append(dict(label=label,q=q,N=n,kappa=k,dual_LB=lb,primal_UB=ub,best_L=bestL,
                             log10_LB=(math.log10(lb) if lb>0 else -math.inf),log10_UB=(math.log10(ub) if ub>0 else (-math.inf if ub==0 else math.nan)),
                             gap_log10=(math.log10(ub/lb) if lb>0 and ub>0 else math.nan),dual_status=dstat,primal_status=pstat,
                             domain_status=(zr['status'] if zr else 'NO_ZERO_AUDIT')))
    bdf=pd.DataFrame(brackets);bdf.to_csv(od/'stage27t_energy_brackets.csv',index=False)
    c1=bdf[bdf.label=='C1'];small=bdf[bdf.label.isin(['C3','C4','C5'])]
    reject=bool(len(c1) and float(c1.iloc[0].dual_LB)>=0.5 and np.any(np.isfinite(small.primal_UB.astype(float)) & (small.primal_UB.astype(float)<=1e-3)))
    summary=dict(stage='Stage27T two-sided energy bracket',zero_tail_rows=len(zdf),primal_rows=len(pdf),validated_primal_rows=int((pdf.status=='PRIMAL_UPPER_BOUND_VALIDATED').sum()) if len(pdf) else 0,
                 failures=len(fail),nq_only_scaling_status=('NQ_ONLY_SCALING_NUMERICALLY_REJECTED' if reject else 'NQ_SCALING_UNRESOLVED_DUE_TO_PRIMAL_UPPER_BOUND'),
                 next_theory_direction='OU-coherent simultaneous-q tail if small-q upper bounds validate; do not auto-run.',notes='Numerical brackets on adaptively audited compact domains; no theorem or Stage28 claim.')
    (od/'stage27t_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');say('STAGE27T_FINISHED',json.dumps(summary,sort_keys=True));log.close()
if __name__=='__main__':main()
