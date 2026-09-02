from __future__ import annotations
import math
import numpy as np
from scipy.optimize import minimize

from normalized_kkt_stage25 import (
    NNQPResult,
    solve_normalized_qp,
    reduced_cost_mp,
    scaled_hermites_ld,
    _tail_cross_fast,
    _tail_cross_mp_float,
    LD,
)



def reduced_cost_active_fast(prob,u,alpha,joint,w,active_tol=1e-24,mp_fallback_dps=70):
    """Fast eta evaluation using only nonzero alpha support.

    The Stage25 generic routine formed correlations against every stored
    witness.  eta=c+C alpha only needs active alpha entries; this matters once
    the pooled library has O(100) witnesses and the active set has O(10).
    """
    q0=prob.q;N=prob.N;eps=prob.eps
    w=(float(w[0]),float(w[1]))
    gw=scaled_hermites_ld(q0,w[0],w[1],N)
    t2,risky=_tail_cross_fast(q0,N,w,w,gw,gw)
    if risky or t2<=0:
        t2=LD(_tail_cross_mp_float(q0,N,w,w,dps=mp_fallback_dps))
    if not np.isfinite(t2) or t2<=LD('1e-70'):
        return dict(eta=math.inf,raw_density=math.inf,tail_norm=0.0,c=math.inf,used_mp=True)
    d=float(np.sqrt(t2))
    prefix=1.0+eps*float(np.sum(np.asarray(u[3:N+1],LD)*gw[3:N+1],dtype=LD))
    c=prefix/d
    eta=c;used_mp=bool(risky)
    active=np.where(np.abs(np.asarray(alpha,float))>active_tol)[0]
    for j in active:
        wj=joint['witnesses'][int(j)]
        gj=np.asarray(joint['gprefix'][int(j)],dtype=LD)
        tc,rr=_tail_cross_fast(q0,N,w,wj,gw,gj)
        if rr or not np.isfinite(tc):
            tc=LD(_tail_cross_mp_float(q0,N,w,wj,dps=mp_fallback_dps));used_mp=True
        corr=float(tc)/(d*joint['dnorm'][int(j)])
        eta += corr*float(alpha[int(j)])
    return dict(eta=float(eta),raw_density=float(d*eta),tail_norm=d,c=float(c),used_mp=used_mp,active_cross_count=int(len(active)))

def lambda_to_t(lam: float) -> float:
    lam=float(lam)
    if lam <= 0.0:
        return 0.0
    if lam >= 1.0:
        return math.inf
    return -math.log1p(-lam)


def t_to_lambda(t: float) -> float:
    t=max(float(t),0.0)
    if t > 745:
        return 1.0
    return -math.expm1(-t)


def boundary_lambda_grid(lambda_cap=1-1e-9):
    if not (0.0 < lambda_cap < 1.0):
        raise ValueError('lambda_cap must be in (0,1)')
    anchors=[0.0,0.005,0.01,0.03,0.06,0.1,0.125,0.18,0.25,0.35,0.5,0.65,0.78,0.82,
             0.86,0.90,0.94,0.97,0.985,0.995,0.999,0.9999,0.99999,0.999999]
    tmax=lambda_to_t(lambda_cap)
    ts=np.r_[np.linspace(0.0,min(tmax,4.0),17),
             np.linspace(min(tmax,4.0),tmax,17) if tmax>4 else []]
    vals=[x for x in anchors if x<=lambda_cap]
    vals += [t_to_lambda(float(t)) for t in ts]
    vals=np.asarray(sorted(set(round(float(x),14) for x in vals)),float)
    return vals[(vals>=0)&(vals<=lambda_cap)]


def _is_duplicate(w,existing,ltol=2e-7,stol=2e-6):
    return any(abs(float(w[0])-float(a))<ltol and abs(float(w[1])-float(b))<stol for a,b in existing)


def _diverse_take(records,k,t_sep=0.035,s_sep=0.035):
    out=[]
    for rec in records:
        t=lambda_to_t(rec['lambda'])
        s=rec['s']
        if all(abs(t-lambda_to_t(z['lambda']))>t_sep or abs(s-z['s'])>s_sep for z in out):
            out.append(rec)
        if len(out)>=k:
            break
    return out


def batch_reduced_cost_oracle(prob,u,alpha,joint,S=5.5,lambda_cap=1-1e-9,
                              s_grid=151,refine_k=12,batch_size=10,dps=180,
                              eta_add_tol=1e-20,existing_tol=(2e-7,2e-6)):
    """Boundary-complete discovery oracle on a compact numerical window.

    lambda is optimized in t=-log(1-lambda), which resolves the lambda->1
    boundary much better than a direct lambda grid.  The adding rule is the
    normalized KKT reduced cost eta=c+C alpha.  We return a *batch* of
    high-precision verified negative reduced-cost witnesses.

    This is numerical reconnaissance on lambda<=lambda_cap and |s|<=S; it is
    not a proof for the open endpoint lambda=1 or the unbounded s-axis.
    """
    existing=list(joint['witnesses'])
    lams=boundary_lambda_grid(lambda_cap)
    vals=[]
    svals=np.linspace(-float(S),float(S),int(s_grid))
    for lam in lams:
        for s in svals:
            w=(float(lam),float(s))
            if _is_duplicate(w,existing,*existing_tol):
                continue
            try:
                z=reduced_cost_active_fast(prob,u,alpha,joint,w,mp_fallback_dps=max(70,dps//2))
            except Exception:
                continue
            if np.isfinite(z['eta']):
                vals.append((float(z['eta']),w,z))
    if not vals:
        raise RuntimeError('batch reduced-cost oracle found no finite grid point')
    vals.sort(key=lambda x:x[0])

    seed_records=[]
    for eta,w,z in vals:
        rec={'eta':eta,'lambda':w[0],'s':w[1]}
        if all(abs(lambda_to_t(rec['lambda'])-lambda_to_t(v['lambda']))>0.05 or abs(rec['s']-v['s'])>0.05 for v in seed_records):
            seed_records.append(rec)
        if len(seed_records)>=refine_k:
            break

    tmax=lambda_to_t(lambda_cap)
    refined=[]
    for rec in seed_records:
        t0=lambda_to_t(rec['lambda'])
        y0=np.array([t0,rec['s']],float)
        try:
            def obj(y):
                lam=t_to_lambda(float(y[0]))
                return reduced_cost_active_fast(prob,u,alpha,joint,(lam,float(y[1])),mp_fallback_dps=max(70,dps//2))['eta']
            opt=minimize(obj,y0,method='Powell',bounds=[(0.0,tmax),(-S,S)],
                         options=dict(maxiter=220,xtol=2e-7,ftol=1e-11,disp=False))
            w=(t_to_lambda(float(opt.x[0])),float(opt.x[1]))
            if not _is_duplicate(w,existing,*existing_tol):
                z=reduced_cost_active_fast(prob,u,alpha,joint,w,mp_fallback_dps=max(80,dps//2))
                if np.isfinite(z['eta']):
                    refined.append((float(z['eta']),w,z))
        except Exception:
            pass

    candidates=vals[:max(4*batch_size,24)]+refined
    candidates.sort(key=lambda x:x[0])
    hp=[];seen=[]
    for _,w,_ in candidates:
        if _is_duplicate(w,seen,2e-8,2e-7):
            continue
        seen.append(w)
        try:
            z1=reduced_cost_mp(prob,u,alpha,joint,w,dps=dps)
            z2=reduced_cost_mp(prob,u,alpha,joint,w,dps=dps+30)
        except Exception:
            continue
        if not np.isfinite(z2['eta']):
            continue
        rec={'eta':float(z2['eta']),'lambda':float(w[0]),'s':float(w[1]),
             'raw_density':float(z2['raw_density']),'tail_norm':float(z2['tail_norm']),
             'c':float(z2['c']),'mp_error':float(abs(z2['eta']-z1['eta']))}
        hp.append(rec)
        if len(hp)>=max(6*batch_size,40):
            break
    if not hp:
        raise RuntimeError('high-precision reduced-cost validation produced no point')
    hp.sort(key=lambda r:r['eta'])
    best=hp[0]
    verified_tol=max(float(eta_add_tol),100*max(r['mp_error'] for r in hp[:min(10,len(hp))]))
    negative=[r for r in hp if r['eta'] < -verified_tol and not _is_duplicate((r['lambda'],r['s']),existing,*existing_tol)]
    additions=_diverse_take(negative,batch_size)
    lam_boundary=bool(best['lambda'] >= lambda_cap-(1-lambda_cap)*10)
    s_boundary=bool(abs(best['s']) >= 0.985*S)
    single_gain=max(-best['eta'],0.0)**2/((1.0+float(joint.get('ridge',0.0)))*prob.eps*prob.eps)
    return dict(best=best,additions=additions,eta_verified_tol=verified_tol,
                lambda_boundary=lam_boundary,s_boundary=s_boundary,
                single_atom_energy_gain=float(single_gain),
                grid_best_eta=float(vals[0][0]),grid_points=len(vals),
                hp_checked=len(hp),refined_count=len(refined),lambda_cap=float(lambda_cap),S=float(S))
