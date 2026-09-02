from __future__ import annotations
import math
import numpy as np
import mpmath as mp


def scaled_hermites_mp(q0,lam,s,N):
    q0=mp.mpf(str(q0)); lam=mp.mpf(str(lam)); s=mp.mpf(str(s))
    a=s/mp.sqrt(q0)
    g=[mp.mpf('0')]*(N+1)
    g[0]=mp.mpf(1)
    if N>=1:g[1]=a
    for n in range(1,N):
        g[n+1]=(a/mp.sqrt(n+1))*g[n]-lam*mp.sqrt(mp.mpf(n)/(n+1))*g[n-1]
    return g


def full_cross_kernel_mp(q0,l1,s1,l2,s2):
    q0=mp.mpf(str(q0)); l1=mp.mpf(str(l1));l2=mp.mpf(str(l2))
    s1=mp.mpf(str(s1));s2=mp.mpf(str(s2))
    if l1==0 and l2==0:
        return mp.e**(s1*s2/q0)
    if l1==0:
        return mp.e**(s1*s2/q0-l2*s1*s1/(2*q0))
    if l2==0:
        return mp.e**(s1*s2/q0-l1*s2*s2/(2*q0))
    rho=mp.sqrt(l1*l2)
    x=s1/mp.sqrt(l1*q0);y=s2/mp.sqrt(l2*q0)
    den=1-rho*rho
    return mp.e**((2*rho*x*y-rho*rho*(x*x+y*y))/(2*den))/mp.sqrt(den)


def tail_cross_mp(q0,N,w1,w2,dps=120):
    old=mp.mp.dps; mp.mp.dps=dps
    try:
        l1,s1=w1; l2,s2=w2
        g1=scaled_hermites_mp(q0,l1,s1,N)
        g2=scaled_hermites_mp(q0,l2,s2,N)
        return full_cross_kernel_mp(q0,l1,s1,l2,s2)-mp.fsum(g1[n]*g2[n] for n in range(N+1))
    finally:
        mp.mp.dps=old


def build_joint_tail(q0,N,witnesses,dps=140,ridge=1e-11,min_tail2='1e-70'):
    """Build normalized infinite-tail Gram plus a fixed diagonal ridge.

    The exact Gram is PSD.  A fixed ridge makes the float QP well conditioned
    without changing off-diagonal cross correlations.  It is conservative for
    proving obstruction: the larger quadratic penalty can only LOWER the dual
    tail-energy lower bound.
    """
    old=mp.mp.dps; mp.mp.dps=dps
    try:
        gs=[scaled_hermites_mp(q0,l,s,N) for l,s in witnesses]
        J=len(witnesses)
        Gmp=[[mp.mpf(0) for _ in range(J)] for __ in range(J)]
        for i,(li,si) in enumerate(witnesses):
            for j in range(i,J):
                lj,sj=witnesses[j]
                full=full_cross_kernel_mp(q0,li,si,lj,sj)
                low=mp.fsum(gs[i][n]*gs[j][n] for n in range(N+1))
                tail=full-low
                Gmp[i][j]=Gmp[j][i]=tail
        keep=[]; diag=[]
        floor=mp.mpf(str(min_tail2))
        for i in range(J):
            if Gmp[i][i] > floor:
                keep.append(i); diag.append(mp.sqrt(Gmp[i][i]))
        witnesses=[witnesses[i] for i in keep]
        gs=[gs[i] for i in keep]
        J=len(keep)
        Craw=np.empty((J,J),float)
        for a,i in enumerate(keep):
            for b,j in enumerate(keep):
                Craw[a,b]=float(Gmp[i][j]/mp.sqrt(Gmp[i][i]*Gmp[j][j]))
        Craw=(Craw+Craw.T)/2
        raw_eigs=np.linalg.eigvalsh(Craw) if J else np.array([1.0])
        raw_min=float(raw_eigs[0]) if J else 1.0
        C=Craw+float(ridge)*np.eye(J)
        eigs=np.linalg.eigvalsh(C) if J else np.array([1.0])
        if J and eigs[0] <= 0:
            raise FloatingPointError(f"regularized tail Gram not SPD: raw_min={raw_min}, ridge={ridge}")
        dnorm=np.array([float(x) for x in diag],float)
        gfloat=np.array([[float(z) for z in g] for g in gs],float)
        return dict(
            witnesses=witnesses,C=C,Craw=Craw,dnorm=dnorm,gprefix=gfloat,
            raw_corr_min_eig=raw_min,ridge=float(ridge),
            corr_cond=float(eigs[-1]/eigs[0]) if J else 1.0,
        )
    finally:
        mp.mp.dps=old


def prefix_scaled(prob,u,joint):
    eps=prob.eps
    vals=[]
    for g,d in zip(joint['gprefix'],joint['dnorm']):
        raw=1.0+eps*float(np.dot(u[3:prob.N+1],g[3:prob.N+1]))
        vals.append(raw/d)
    return np.asarray(vals,float)
