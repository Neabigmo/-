from __future__ import annotations
import math
from dataclasses import dataclass
import numpy as np
import mpmath as mp
from scipy.optimize import minimize

from joint_tail_core import scaled_hermites_mp, full_cross_kernel_mp

LD=np.longdouble

@dataclass
class NNQPResult:
    alpha: np.ndarray
    slack: np.ndarray
    m2_dual: float
    m2_primal: float
    objective: float
    projected_kkt_inf: float
    complementarity_inf: float
    dual_primal_abs: float
    dual_primal_rel: float
    active_count: int
    iterations: int
    max_subproblem_condition: float
    success: bool
    message: str


def _solve_spd(A,b):
    A=(A+A.T)/2
    vals,V=np.linalg.eigh(A)
    if len(vals)==0:
        return np.zeros(0),1.0
    vmax=max(float(vals[-1]),1e-300)
    vmin=float(vals[0])
    if vmin <= 0:
        raise np.linalg.LinAlgError(f"nonpositive active Hessian eigenvalue {vmin}")
    cond=vmax/vmin
    x=V@((V.T@b)/vals)
    return np.asarray(x,float),float(cond)


def solve_normalized_qp(c,C,eps,tol=1e-10,max_iter=500):
    """Solve min_{alpha>=0} alpha^T C alpha + 2 c^T alpha.

    KKT: alpha>=0, slack=c+C alpha>=0, alpha*slack=0.
    Tail energy is the dual quantity divided by eps^2.
    """
    c=np.asarray(c,float); C=np.asarray(C,float)
    J=len(c)
    alpha=np.zeros(J,float)
    passive=[]
    maxcond=1.0
    msg="optimal"

    for it in range(max_iter):
        slack=c+C@alpha
        inactive=[i for i in range(J) if i not in passive]
        worst=min(inactive,key=lambda i: slack[i]) if inactive else None
        active_stationarity=max([abs(slack[i]) for i in passive],default=0.0)
        if (worst is None or slack[worst] >= -tol) and active_stationarity <= 20*tol:
            break
        if worst is not None and slack[worst] < -tol and worst not in passive:
            passive.append(worst)

        inner_guard=0
        while True:
            inner_guard+=1
            if inner_guard>J+10:
                raise RuntimeError("NNQP inner active-set loop did not settle")
            if not passive:
                alpha[:]=0.0
                break
            P=np.array(sorted(passive),dtype=int)
            z=np.zeros(J,float)
            sol,cond=_solve_spd(C[np.ix_(P,P)],-c[P])
            maxcond=max(maxcond,cond)
            z[P]=sol
            if np.all(sol>tol*0.1):
                alpha=z
                break
            bad=P[sol<=tol*0.1]
            theta=1.0
            found=False
            for idx in bad:
                den=alpha[idx]-z[idx]
                if alpha[idx]>0 and den>0:
                    theta=min(theta,alpha[idx]/den); found=True
            if not found:
                for idx in bad:
                    if idx in passive: passive.remove(int(idx))
                alpha[bad]=0.0
                continue
            alpha=alpha+theta*(z-alpha)
            alpha[np.abs(alpha)<tol*0.1]=0.0
            for idx in list(passive):
                if alpha[idx] <= tol*0.1:
                    passive.remove(idx); alpha[idx]=0.0
    else:
        msg="max_iter"

    slack=c+C@alpha
    apos=alpha>10*tol
    pinf=max(
        float(np.max(np.abs(slack[apos]))) if np.any(apos) else 0.0,
        float(np.max(np.maximum(-slack[~apos],0.0))) if np.any(~apos) else 0.0,
    )
    comp=float(np.max(np.abs(alpha*slack))) if J else 0.0
    quad=float(alpha@C@alpha)
    lin=float(c@alpha)
    m2_dual=float((-2*lin-quad)/(eps*eps))
    m2_primal=float(quad/(eps*eps))
    dpabs=abs(m2_dual-m2_primal)
    dprel=dpabs/(1.0+abs(m2_dual)+abs(m2_primal))
    obj=float(quad+2*lin)
    success=(msg=="optimal" and pinf<=max(1e-8,100*tol) and comp<=max(1e-8,100*tol)*(1+np.linalg.norm(alpha)))
    return NNQPResult(alpha,slack,m2_dual,m2_primal,obj,pinf,comp,dpabs,dprel,int(np.sum(apos)),it+1,maxcond,success,msg)


def scaled_hermites_ld(q0,lam,s,N):
    q0=LD(q0); lam=LD(lam); s=LD(s)
    g=np.zeros(N+1,dtype=LD); g[0]=1
    if N==0:return g
    a=s/np.sqrt(q0); g[1]=a
    for n in range(1,N):
        g[n+1]=(a/np.sqrt(LD(n+1)))*g[n]-lam*np.sqrt(LD(n)/LD(n+1))*g[n-1]
    return g


def full_cross_kernel_ld(q0,l1,s1,l2,s2):
    q0=LD(q0); l1=LD(l1); l2=LD(l2); s1=LD(s1); s2=LD(s2)
    if l1==0 and l2==0:
        return np.exp(s1*s2/q0)
    if l1==0:
        return np.exp(s1*s2/q0-l2*s1*s1/(2*q0))
    if l2==0:
        return np.exp(s1*s2/q0-l1*s2*s2/(2*q0))
    rho=np.sqrt(l1*l2)
    x=s1/np.sqrt(l1*q0); y=s2/np.sqrt(l2*q0)
    den=1-rho*rho
    return np.exp((2*rho*x*y-rho*rho*(x*x+y*y))/(2*den))/np.sqrt(den)


def _tail_cross_fast(q0,N,w1,w2,g1=None,g2=None,cancel_tol=2e-12):
    if g1 is None:g1=scaled_hermites_ld(q0,w1[0],w1[1],N)
    if g2 is None:g2=scaled_hermites_ld(q0,w2[0],w2[1],N)
    full=full_cross_kernel_ld(q0,w1[0],w1[1],w2[0],w2[1])
    low=np.sum(g1*g2,dtype=LD)
    tail=full-low
    scale=abs(full)+abs(low)+LD(1e-300)
    risky=(not np.isfinite(tail)) or abs(tail) <= LD(cancel_tol)*scale
    return tail,risky


def _tail_cross_mp_float(q0,N,w1,w2,dps=70):
    old=mp.mp.dps; mp.mp.dps=dps
    try:
        g1=scaled_hermites_mp(q0,w1[0],w1[1],N)
        g2=scaled_hermites_mp(q0,w2[0],w2[1],N)
        z=full_cross_kernel_mp(q0,w1[0],w1[1],w2[0],w2[1])-mp.fsum(g1[n]*g2[n] for n in range(N+1))
        return float(z)
    finally:
        mp.mp.dps=old


def reduced_cost_fast(prob,u,alpha,joint,w,mp_fallback_dps=70):
    q0=prob.q; N=prob.N; eps=prob.eps
    w=(float(w[0]),float(w[1]))
    gw=scaled_hermites_ld(q0,w[0],w[1],N)
    t2,risky=_tail_cross_fast(q0,N,w,w,gw,gw)
    if risky or t2<=0:
        t2=LD(_tail_cross_mp_float(q0,N,w,w,dps=mp_fallback_dps))
    if not np.isfinite(t2) or t2<=LD('1e-70'):
        return dict(eta=math.inf,raw_density=math.inf,tail_norm=0.0,c=math.inf,cross=None,used_mp=True)
    d=float(np.sqrt(t2))
    prefix=1.0+eps*float(np.sum(np.asarray(u[3:N+1],LD)*gw[3:N+1],dtype=LD))
    c=prefix/d
    cross=np.zeros(len(joint['witnesses']),float)
    used_mp=bool(risky)
    for j,wj in enumerate(joint['witnesses']):
        gj=np.asarray(joint['gprefix'][j],dtype=LD)
        tc,rr=_tail_cross_fast(q0,N,w,wj,gw,gj)
        if rr or not np.isfinite(tc):
            tc=LD(_tail_cross_mp_float(q0,N,w,wj,dps=mp_fallback_dps)); used_mp=True
        cross[j]=float(tc)/(d*joint['dnorm'][j])
    eta=float(c+cross@alpha)
    return dict(eta=eta,raw_density=d*eta,tail_norm=d,c=c,cross=cross,used_mp=used_mp)


def reduced_cost_mp(prob,u,alpha,joint,w,dps=140):
    old=mp.mp.dps; mp.mp.dps=dps
    try:
        q0=mp.mpf(str(prob.q)); eps=mp.mpf(str(prob.eps)); N=prob.N
        l=mp.mpf(str(w[0])); s=mp.mpf(str(w[1]))
        gw=scaled_hermites_mp(q0,l,s,N)
        t2=full_cross_kernel_mp(q0,l,s,l,s)-mp.fsum(gw[n]*gw[n] for n in range(N+1))
        if t2<=mp.mpf('1e-80'):
            return dict(eta=math.inf,raw_density=math.inf,tail_norm=0.0,c=math.inf)
        d=mp.sqrt(t2)
        prefix=mp.mpf(1)+eps*mp.fsum(mp.mpf(str(float(u[n])))*gw[n] for n in range(3,N+1))
        eta=prefix/d
        for a,wj in zip(alpha,joint['witnesses']):
            if a==0:continue
            gj=scaled_hermites_mp(q0,wj[0],wj[1],N)
            tj=full_cross_kernel_mp(q0,l,s,wj[0],wj[1])-mp.fsum(gw[n]*gj[n] for n in range(N+1))
            dj2=full_cross_kernel_mp(q0,wj[0],wj[1],wj[0],wj[1])-mp.fsum(gj[n]*gj[n] for n in range(N+1))
            eta += mp.mpf(str(float(a)))*tj/(d*mp.sqrt(dj2))
        return dict(eta=float(eta),raw_density=float(d*eta),tail_norm=float(d),c=float(prefix/d))
    finally:
        mp.mp.dps=old


def find_min_reduced_cost(prob,u,alpha,joint,S=4.5,lambda_max=.82,s_grid=161,refine_k=8,dps=140,seed=20260901):
    existing=list(joint['witnesses'])
    def duplicate(w):
        return any(abs(w[0]-a)<2e-6 and abs(w[1]-b)<2e-5 for a,b in existing)
    lams=np.unique(np.r_[0.0,np.geomspace(2e-4,lambda_max,19),[.01,.03,.06,.1,.125,.18,.25,.35,.5,.65,.78]])
    lams=lams[(lams>=0)&(lams<=lambda_max)]
    vals=[]
    for lam in lams:
        for s in np.linspace(-S,S,s_grid):
            w=(float(lam),float(s))
            if duplicate(w):continue
            z=reduced_cost_fast(prob,u,alpha,joint,w)
            if np.isfinite(z['eta']): vals.append((z['eta'],w,z))
    if not vals:
        raise RuntimeError('reduced-cost oracle found no finite candidate')
    vals.sort(key=lambda x:x[0])
    seeds=[]
    for _,w,z in vals:
        if all(abs(w[0]-v[0])>2e-3 or abs(w[1]-v[1])>2e-2 for v in seeds):
            seeds.append(w)
        if len(seeds)>=refine_k:break
    refined=[]
    for w0 in seeds:
        try:
            opt=minimize(lambda y: reduced_cost_fast(prob,u,alpha,joint,(float(y[0]),float(y[1])))['eta'],
                         np.array([max(w0[0],1e-10),w0[1]]),method='Powell',
                         bounds=[(0.0,lambda_max),(-S,S)],
                         options=dict(maxiter=180,xtol=2e-7,ftol=1e-10,disp=False))
            w=(float(opt.x[0]),float(opt.x[1]))
            if not duplicate(w):
                z=reduced_cost_fast(prob,u,alpha,joint,w)
                if np.isfinite(z['eta']):refined.append((z['eta'],w,z))
        except Exception:
            pass
    candidates=vals[:max(12,refine_k)]+refined
    candidates.sort(key=lambda x:x[0])
    hp=[]
    seen=[]
    for _,w,_ in candidates:
        if any(abs(w[0]-a)<2e-7 and abs(w[1]-b)<2e-6 for a,b in seen):continue
        seen.append(w)
        z1=reduced_cost_mp(prob,u,alpha,joint,w,dps=dps)
        z2=reduced_cost_mp(prob,u,alpha,joint,w,dps=dps+30)
        err=abs(z2['eta']-z1['eta'])
        hp.append((z2['eta'],w,z2,err))
        if len(hp)>=5:break
    hp.sort(key=lambda x:x[0])
    eta,w,z,err=hp[0]
    return dict(eta_min=float(eta),lambda_star=w[0],s_star=w[1],raw_density=float(z['raw_density']),
                tail_norm=float(z['tail_norm']),c=float(z['c']),mp_validation_error=float(err),
                grid_best_eta=float(vals[0][0]),tested_grid_points=len(vals),refined_count=len(refined))
