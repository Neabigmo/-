from __future__ import annotations
import numpy as np
from scipy.optimize import minimize
from mp_features import density_ld,density_mp,lambda_grid,lambda_to_t,t_to_lambda,boundary_flags


def audit_zero_tail(q,eps,N,u,s_grid=241,refine_k=20,tol=1e-10):
    v=np.zeros(0,float); S_levels=[6.,8.,10.,12.]; caps=[1-1e-12,1-1e-14,1-1e-16]
    si=0;ci=0;history=[]
    for step in range(12):
        S=S_levels[si];cap=caps[ci];vals=[]
        for lam in lambda_grid(cap):
            for s in np.linspace(-S,S,s_grid):
                try:z=density_ld(q,eps,N,u,v,lam,s)
                except Exception:continue
                if np.isfinite(z):vals.append((z,float(lam),float(s)))
        vals.sort(key=lambda x:x[0]);seeds=[]
        for _,lam,s in vals:
            t=lambda_to_t(lam)
            if all(abs(t-lambda_to_t(a))>0.06 or abs(s-b)>0.08 for a,b in seeds):seeds.append((lam,s))
            if len(seeds)>=refine_k:break
        tmax=lambda_to_t(cap);cands=vals[:24]
        for lam,s in seeds:
            try:
                op=minimize(lambda x:density_ld(q,eps,N,u,v,t_to_lambda(float(x[0])),float(x[1])),
                            [lambda_to_t(lam),s],method='Powell',bounds=[(0,tmax),(-S,S)],
                            options=dict(maxiter=160,xtol=1e-7,ftol=1e-10))
                la=t_to_lambda(float(op.x[0]));sv=float(op.x[1]);cands.append((density_ld(q,eps,N,u,v,la,sv),la,sv))
            except Exception:pass
        checks=[]
        for _,lam,s in sorted(cands)[:24]:
            z1=density_mp(q,eps,N,u,v,lam,s,dps=160);z2=density_mp(q,eps,N,u,v,lam,s,dps=240)
            checks.append((z2,lam,s,abs(z2-z1)))
        checks.sort(key=lambda x:x[0]);z,lam,s,err=checks[0];lb,sb=boundary_flags(lam,s,cap,S)
        history.append(dict(step=step,min_density=z,lambda_star=lam,s_star=s,mp_error=err,S=S,lambda_cap=cap,lambda_boundary=lb,s_boundary=sb))
        expanded=False
        if sb and si<len(S_levels)-1:si+=1;expanded=True
        if lb and ci<len(caps)-1:ci+=1;expanded=True
        if expanded:continue
        status='ZERO_TAIL_WINDOW_VALIDATED' if z>=-tol and not lb and not sb else ('ZERO_TAIL_BOUNDARY_UNRESOLVED' if lb or sb else 'ZERO_TAIL_NEGATIVE')
        return dict(status=status,min_density=float(z),lambda_star=float(lam),s_star=float(s),mp_error=float(err),S=S,lambda_cap=cap,lambda_boundary=lb,s_boundary=sb),history
    last=history[-1]
    return dict(status='ZERO_TAIL_AUDIT_LIMIT',**{k:last[k] for k in last if k!='step'}),history
