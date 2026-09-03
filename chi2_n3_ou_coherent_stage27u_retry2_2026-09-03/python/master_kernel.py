from __future__ import annotations
import math
import mpmath as mp
import numpy as np

from joint_tail_core import scaled_hermites_mp, full_cross_kernel_mp


def master_feature_mp(q, lam, s, N, dps=160):
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        g=scaled_hermites_mp(q,lam,s,N)
        qmp=mp.mpf(str(q))
        return [qmp**(mp.mpf(n)/2)*g[n] for n in range(N+1)]
    finally:
        mp.mp.dps=old


def effective_feature_mp(q, lam, s, N, dps=160):
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        return scaled_hermites_mp(mp.mpf(1),mp.mpf(str(q))*mp.mpf(str(lam)),s,N)
    finally:
        mp.mp.dps=old


def feature_identity_error(q,lam,s,N,dps=160):
    a=master_feature_mp(q,lam,s,N,dps=dps)
    b=effective_feature_mp(q,lam,s,N,dps=dps)
    errs=[]
    for x,y in zip(a,b):
        errs.append(abs(x-y)/(mp.mpf(1)+abs(y)))
    return float(max(errs) if errs else 0)


def direct_master_full_kernel_error(q1,w1,q2,w2,dps=180):
    """Cross-check the coherent master Mehler kernel by two MP paths.

    Path A uses the shared helper at q0=1. Path B evaluates the same effective
    (r_i=q_i lambda_i) closed form independently. No Python-float q*lambda
    product is used in either path.
    """
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        l1,s1=w1; l2,s2=w2
        q1m=mp.mpf(str(q1)); q2m=mp.mpf(str(q2))
        r1=q1m*mp.mpf(str(l1)); r2=q2m*mp.mpf(str(l2))
        s1m=mp.mpf(str(s1)); s2m=mp.mpf(str(s2))
        A=full_cross_kernel_mp(1,r1,s1m,r2,s2m)
        if r1==0 and r2==0:
            B=mp.e**(s1m*s2m)
        elif r1==0:
            B=mp.e**(s1m*s2m-r2*s1m*s1m/2)
        elif r2==0:
            B=mp.e**(s1m*s2m-r1*s2m*s2m/2)
        else:
            rho=mp.sqrt(r1*r2); x=s1m/mp.sqrt(r1); y=s2m/mp.sqrt(r2); den=1-rho*rho
            B=mp.e**((2*rho*x*y-rho*rho*(x*x+y*y))/(2*den))/mp.sqrt(den)
        return float(abs(A-B)/(1+abs(B)))
    finally:
        mp.mp.dps=old


def direct_vs_master_prefix_error(q,lam,s,N,dps=180):
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        g=scaled_hermites_mp(q,lam,s,N)
        gm=scaled_hermites_mp(1,mp.mpf(str(q))*mp.mpf(str(lam)),s,N)
        qmp=mp.mpf(str(q))
        return float(max(abs(qmp**(mp.mpf(n)/2)*g[n]-gm[n])/(1+abs(gm[n])) for n in range(N+1)))
    finally:
        mp.mp.dps=old
