from __future__ import annotations
import math
from dataclasses import dataclass
import numpy as np
from scipy.optimize import minimize

from normalized_kkt_stage26 import scaled_hermites_ld
from mp_features import (build_feature_system,cross_precision_feature_error,density_ld,density_mp,
                         lambda_grid,lambda_to_t,t_to_lambda,boundary_flags)


def dedupe_witnesses(W, ltol=2e-8, stol=2e-7):
    out=[]
    for a,b in W:
        w=(float(a),float(b))
        if not (0<=w[0]<1 and np.isfinite(w[0]) and np.isfinite(w[1])): continue
        if not any(abs(w[0]-x)<ltol and abs(w[1]-y)<stol for x,y in out): out.append(w)
    return out


def dual_coordinate_qp(G,b,tol=1e-11,max_sweeps=30000):
    G=np.asarray(G,float); b=np.asarray(b,float); J=len(b)
    y=np.zeros(J,float); grad=-b.copy(); diag=np.diag(G).copy()
    diag=np.where(diag>1e-15,diag,1.0)
    iters=0
    for sweep in range(max_sweeps):
        if J==0: break
        pg=np.where(y>0,grad,np.minimum(grad,0.0))
        i=int(np.argmax(np.abs(pg))); err=float(abs(pg[i]))
        if err <= tol*(1+float(np.max(np.abs(b))) if J else 1):
            iters=sweep; break
        yn=max(0.0,y[i]-grad[i]/diag[i]); delta=yn-y[i]
        if delta==0:
            # try the next largest projected-gradient coordinate
            order=np.argsort(-np.abs(pg)); moved=False
            for ii in order[:min(8,J)]:
                yn=max(0.0,y[ii]-grad[ii]/diag[ii]); delta=yn-y[ii]
                if delta!=0: i=int(ii); moved=True; break
            if not moved:
                iters=sweep; break
        y[i]=yn; grad += delta*G[:,i]; iters=sweep+1
    pg=np.where(y>0,grad,np.minimum(grad,0.0))
    return y,float(np.max(np.abs(pg)) if J else 0.0),iters


def feasibility_projection(Phi,b,v,tol=2e-11,max_updates=200000):
    Phi=np.asarray(Phi,float);b=np.asarray(b,float);v=np.asarray(v,float).copy()
    updates=0
    norms=np.sum(Phi*Phi,axis=1)+1e-300
    while updates<max_updates:
        slack=Phi@v-b; i=int(np.argmin(slack)); z=float(slack[i])
        if z>=-tol: return v,slack,updates
        v += (-z/norms[i])*Phi[i]; updates+=1
    return v,Phi@v-b,updates

@dataclass
class TailSolve:
    v: np.ndarray
    energy: float
    dual_energy: float
    min_slack: float
    dual_projected_grad: float
    complementarity: float
    energy_rel_gap: float
    projection_updates: int
    system: object
    cross_precision_error: float
    dps_final: int
    feature_valid: bool


def solve_tail(q,eps,N,u,W,L,dps1=160,dps2=240):
    err,a,bld=cross_precision_feature_error(q,eps,N,u,W,L,dps1=dps1,dps2=dps2)
    sys=bld; dps_final=dps2
    if err>1e-12:
        err2,b2,b3=cross_precision_feature_error(q,eps,N,u,W,L,dps1=dps2,dps2=360)
        err=err2; sys=b3; dps_final=360
    ev_tol=-max(5e-10,100*len(sys.b)*np.finfo(float).eps)
    feature_valid=bool(sys.min_eigenvalue>=ev_tol and sys.max_diag_error<=1e-10 and sys.max_corr_excess<=1e-10 and err<=1e-10)
    if not feature_valid:
        raise FloatingPointError(f'feature audit failed eig={sys.min_eigenvalue} diag={sys.max_diag_error} corr={sys.max_corr_excess} cross={err}')
    y,pg,it=dual_coordinate_qp(sys.G,sys.b,tol=1e-12,max_sweeps=40000)
    v0=sys.Phi.T@y
    v,slack,updates=feasibility_projection(sys.Phi,sys.b,v0,tol=2e-11)
    energy=float(v@v); dual_energy=float(v0@v0)
    grad=sys.G@y-sys.b; comp=float(np.max(np.abs(y*(sys.Phi@v0-sys.b))) if len(y) else 0.0)
    gap=abs(energy-dual_energy)/(1+abs(energy)+abs(dual_energy))
    return TailSolve(v,energy,dual_energy,float(np.min(slack)),pg,comp,gap,updates,sys,float(err),dps_final,feature_valid)


def fast_density_grid(q,eps,N,u,v,lambda_cap,S,s_grid=241,refine_k=20):
    lams=lambda_grid(lambda_cap); ss=np.linspace(-S,S,int(s_grid)); vals=[]
    for lam in lams:
        for s in ss:
            try: z=density_ld(q,eps,N,u,v,lam,s)
            except Exception: continue
            if np.isfinite(z): vals.append((z,float(lam),float(s)))
    if not vals: raise RuntimeError('density grid found no finite points')
    vals.sort(key=lambda x:x[0]); seeds=[]
    for z,lam,s in vals:
        t=lambda_to_t(lam)
        if all(abs(t-lambda_to_t(a))>0.06 or abs(s-b)>0.08 for a,b in seeds): seeds.append((lam,s))
        if len(seeds)>=refine_k: break
    tmax=lambda_to_t(lambda_cap); refined=[]
    for lam,s in seeds:
        try:
            op=minimize(lambda x:density_ld(q,eps,N,u,v,t_to_lambda(float(x[0])),float(x[1])),
                        np.array([lambda_to_t(lam),s]),method='Powell',bounds=[(0,tmax),(-S,S)],
                        options=dict(maxiter=180,xtol=1e-7,ftol=1e-10,disp=False))
            la=t_to_lambda(float(op.x[0])); sv=float(op.x[1]); zz=density_ld(q,eps,N,u,v,la,sv)
            if np.isfinite(zz): refined.append((zz,la,sv))
        except Exception: pass
    cand=vals[:max(20,refine_k)]+refined; cand.sort(key=lambda x:x[0])
    return cand


def robust_density_audit(q,eps,N,u,v,lambda_cap,S,s_grid=241,refine_k=20,dps1=160,dps2=240):
    cand=fast_density_grid(q,eps,N,u,v,lambda_cap,S,s_grid=s_grid,refine_k=refine_k)
    checked=[]
    for _,lam,s in cand[:max(24,refine_k)]:
        z1=density_mp(q,eps,N,u,v,lam,s,dps=dps1); z2=density_mp(q,eps,N,u,v,lam,s,dps=dps2)
        checked.append((z2,lam,s,abs(z2-z1)))
    checked.sort(key=lambda x:x[0]); z,lam,s,err=checked[0]
    lb,sb=boundary_flags(lam,s,lambda_cap,S)
    return dict(min_density=float(z),lambda_star=float(lam),s_star=float(s),mp_error=float(err),
                lambda_boundary=lb,s_boundary=sb,lambda_cap=float(lambda_cap),S=float(S),
                checked_points=len(checked),grid_candidates=len(cand))


def adaptive_reconstruct(q,eps,N,u,W,L,max_outer=20,s_grid=241,refine_k=20,density_tol=1e-8):
    W=dedupe_witnesses(W)[:48]; hist=[]; S_levels=[6.0,8.0,10.0,12.0]
    cap_levels=[1-1e-12,1-1e-14,1-1e-16]
    si=0;ci=0;last=None
    for it in range(max_outer):
        sol=solve_tail(q,eps,N,u,W,L)
        aud=robust_density_audit(q,eps,N,u,sol.v,cap_levels[ci],S_levels[si],s_grid=s_grid,refine_k=refine_k)
        hist.append(dict(iteration=it,L=L,witness_count=len(W),energy=sol.energy,dual_energy=sol.dual_energy,
                         min_slack=sol.min_slack,dual_pg=sol.dual_projected_grad,comp=sol.complementarity,
                         energy_rel_gap=sol.energy_rel_gap,projection_updates=sol.projection_updates,
                         min_density=aud['min_density'],lambda_star=aud['lambda_star'],s_star=aud['s_star'],
                         lambda_boundary=aud['lambda_boundary'],s_boundary=aud['s_boundary'],S=aud['S'],
                         lambda_cap=aud['lambda_cap'],feature_min_eig=sol.system.min_eigenvalue,
                         feature_diag_error=sol.system.max_diag_error,feature_corr_excess=sol.system.max_corr_excess,
                         cross_precision_error=sol.cross_precision_error,dps_final=sol.dps_final))
        last=(sol,aud,list(W))
        # Extend numerical domain before claiming success or boundary failure.
        expanded=False
        if aud['s_boundary'] and si<len(S_levels)-1: si+=1; expanded=True
        if aud['lambda_boundary'] and ci<len(cap_levels)-1: ci+=1; expanded=True
        w=(aud['lambda_star'],aud['s_star'])
        if aud['min_density'] < -density_tol and not any(abs(w[0]-a)<2e-8 and abs(w[1]-b)<2e-7 for a,b in W): W.append(w)
        if len(W)>90: W=W[-90:]
        if expanded: continue
        if aud['lambda_boundary'] or aud['s_boundary']:
            return sol,aud,hist,W,'DOMAIN_BOUNDARY_UNRESOLVED'
        if aud['min_density']>=-density_tol:
            ok=sol.min_slack>=-1e-9 and sol.energy_rel_gap<=1e-6 and sol.feature_valid and aud['mp_error']<=1e-8
            return sol,aud,hist,W,('PRIMAL_UPPER_BOUND_VALIDATED' if ok else 'PRIMAL_NUMERIC_AUDIT_FAILED')
        if any(abs(w[0]-a)<2e-8 and abs(w[1]-b)<2e-7 for a,b in W[:-1]):
            return sol,aud,hist,W,'PRIMAL_STALLED'
    sol,aud,W0=last
    return sol,aud,hist,W,'PRIMAL_OUTER_LIMIT'
