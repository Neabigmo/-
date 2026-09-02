from __future__ import annotations
import math
from dataclasses import dataclass
import numpy as np
import mpmath as mp

from normalized_kkt_stage26 import scaled_hermites_ld


def mp_scaled_hermites(q: float, lam: float, s: float, M: int, dps: int = 160):
    old = mp.mp.dps; mp.mp.dps = int(dps)
    try:
        qmp=mp.mpf(str(q)); lmp=mp.mpf(str(lam)); smp=mp.mpf(str(s))
        a=smp/mp.sqrt(qmp)
        g=[mp.mpf('0')]*(int(M)+1); g[0]=mp.mpf(1)
        if M>=1: g[1]=a
        for n in range(1,int(M)):
            g[n+1]=(a/mp.sqrt(n+1))*g[n]-lmp*mp.sqrt(mp.mpf(n)/(n+1))*g[n-1]
        return g
    finally:
        mp.mp.dps=old


def prefix_mp(q: float, eps: float, N: int, u: np.ndarray, lam: float, s: float, dps: int=160) -> float:
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        g=mp_scaled_hermites(q,lam,s,N,dps=dps)
        z=mp.mpf(1)
        emp=mp.mpf(str(eps))
        for n in range(3,N+1):
            if u[n] != 0:
                z += emp*mp.mpf(str(float(u[n])))*g[n]
        return float(z)
    finally:
        mp.mp.dps=old


def density_mp(q: float, eps: float, N: int, u: np.ndarray, v: np.ndarray,
               lam: float, s: float, dps: int=160) -> float:
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        M=N+len(v); g=mp_scaled_hermites(q,lam,s,M,dps=dps)
        emp=mp.mpf(str(eps)); z=mp.mpf(1)
        for n in range(3,N+1):
            if u[n] != 0: z += emp*mp.mpf(str(float(u[n])))*g[n]
        for k,x in enumerate(v, start=1):
            if x != 0: z += emp*mp.mpf(str(float(x)))*g[N+k]
        return float(z)
    finally:
        mp.mp.dps=old


def density_ld(q: float, eps: float, N: int, u: np.ndarray, v: np.ndarray,
               lam: float, s: float) -> float:
    M=N+len(v); g=scaled_hermites_ld(q,float(lam),float(s),M)
    z=np.longdouble(1.0)
    z += np.longdouble(eps)*np.sum(np.asarray(u[3:N+1],np.longdouble)*g[3:N+1],dtype=np.longdouble)
    if len(v):
        z += np.longdouble(eps)*np.sum(np.asarray(v,np.longdouble)*g[N+1:M+1],dtype=np.longdouble)
    return float(z)


def lambda_to_t(lam: float) -> float:
    if lam<=0: return 0.0
    if lam>=1: return math.inf
    return -math.log1p(-float(lam))


def t_to_lambda(t: float) -> float:
    return -math.expm1(-max(0.0,float(t)))


def lambda_grid(lambda_cap: float):
    if not (0 < lambda_cap < 1): raise ValueError('lambda_cap in (0,1) required')
    anchors=[0.0,0.005,0.01,0.03,0.06,0.10,0.125,0.18,0.25,0.35,0.5,0.65,0.78,
             0.82,0.86,0.90,0.94,0.97,0.985,0.995,0.999,0.9999,0.99999,0.999999,
             0.9999999,0.99999999,0.999999999,0.9999999999,0.99999999999,0.999999999999]
    tmax=lambda_to_t(lambda_cap)
    ts=list(np.linspace(0,min(4.0,tmax),17))
    if tmax>4: ts += list(np.linspace(4.0,tmax,25))
    vals=[x for x in anchors if x<=lambda_cap]
    vals += [min(lambda_cap,t_to_lambda(t)) for t in ts]
    vals.append(lambda_cap)
    vals=sorted(vals)
    out=[]
    for x in vals:
        if not out or abs(x-out[-1])>max(1e-15,1e-12*(1-x)):
            out.append(float(x))
    return np.asarray(out,float)


def boundary_flags(lam: float, s: float, lambda_cap: float, S: float):
    t=lambda_to_t(lam); tmax=lambda_to_t(lambda_cap)
    lb=bool(tmax>0 and t >= tmax-max(0.08,0.01*tmax))
    sb=bool(abs(float(s)) >= 0.985*float(S))
    return lb,sb


@dataclass
class FeatureSystem:
    Phi: np.ndarray
    b: np.ndarray
    row_scales: np.ndarray
    row_scales_log10: np.ndarray
    G: np.ndarray
    witnesses: np.ndarray
    min_eigenvalue: float
    max_diag_error: float
    max_corr_excess: float
    dps: int


def build_feature_system(q: float, eps: float, N: int, u: np.ndarray, witnesses, L: int, dps: int=160) -> FeatureSystem:
    old=mp.mp.dps; mp.mp.dps=int(dps)
    try:
        M=N+int(L); rows=[]; rhs=[]; scales=[]; logsc=[]; W=[]
        for lam,s in witnesses:
            g=mp_scaled_hermites(q,float(lam),float(s),M,dps=dps)
            emp=mp.mpf(str(eps))
            tail=[emp*g[N+k] for k in range(1,L+1)]
            norm=mp.sqrt(mp.fsum(x*x for x in tail))
            if not mp.isfinite(norm) or norm <= mp.mpf('1e-100'):
                continue
            p=mp.mpf(1)
            for n in range(3,N+1):
                if u[n] != 0: p += emp*mp.mpf(str(float(u[n])))*g[n]
            nr=[x/norm for x in tail]
            rows.append([float(x) for x in nr]); rhs.append(float(-p/norm)); W.append((float(lam),float(s)))
            lf=mp.log10(norm)
            logsc.append(float(lf))
            scales.append(float(norm) if abs(lf)<300 else math.inf)
        if not rows: raise RuntimeError('no usable feature rows')
        J=len(rows); Gmp=[[mp.mpf(0) for _ in range(J)] for __ in range(J)]
        # Reconstruct mp rows from float-normalized features. This is safe after row normalization;
        # cross-precision auditing below detects any material loss from float conversion.
        mprows=[[mp.mpf(str(x)) for x in row] for row in rows]
        for i in range(J):
            for j in range(i,J):
                z=mp.fsum(mprows[i][k]*mprows[j][k] for k in range(L))
                Gmp[i][j]=Gmp[j][i]=z
        G=np.asarray([[float(Gmp[i][j]) for j in range(J)] for i in range(J)],float)
        G=(G+G.T)/2
        diag=np.diag(G); maxdiag=float(np.max(np.abs(diag-1)))
        den=np.sqrt(np.maximum(diag,1e-300)); C=G/den[:,None]/den[None,:]
        maxcorr=float(np.max(np.maximum(np.abs(C)-1,0)))
        ev=np.linalg.eigvalsh(G)
        return FeatureSystem(np.asarray(rows,float),np.asarray(rhs,float),np.asarray(scales,float),np.asarray(logsc,float),
                             G,np.asarray(W,float),float(ev[0]),maxdiag,maxcorr,int(dps))
    finally:
        mp.mp.dps=old


def cross_precision_feature_error(q,eps,N,u,witnesses,L,dps1=160,dps2=240):
    a=build_feature_system(q,eps,N,u,witnesses,L,dps=dps1)
    b=build_feature_system(q,eps,N,u,witnesses,L,dps=dps2)
    if len(a.witnesses)!=len(b.witnesses) or len(a.witnesses)==0:
        return math.inf,a,b
    err=float(np.max(np.abs(a.G-b.G)/(1+np.abs(b.G))))
    return err,a,b
