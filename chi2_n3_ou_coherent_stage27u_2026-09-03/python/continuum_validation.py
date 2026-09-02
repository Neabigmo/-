from __future__ import annotations
import math
import numpy as np

from reduced_core import ReducedProblem
from joint_tail_core import build_joint_tail,prefix_scaled
from normalized_kkt_stage25 import solve_normalized_qp,find_min_reduced_cost


def dedupe(W,ltol=2e-7,stol=2e-6):
    out=[]
    for a,b in W:
        w=(float(a),float(b))
        if not (0<=w[0]<1 and np.isfinite(w[0]) and np.isfinite(w[1])):continue
        if not any(abs(w[0]-x)<ltol and abs(w[1]-y)<stol for x,y in out):out.append(w)
    return out


def prepare_tail(q,N,W,ridge=1e-11,dps=220):
    prob=ReducedProblem(int(N),3,int(N)*float(q),scale=.30)
    joint=build_joint_tail(q,N,dedupe(W),dps=dps,ridge=ridge)
    return dict(q=float(q),N=int(N),prob=prob,joint=joint,ridge=float(ridge),dps=int(dps))


def tail_lower_bound_prepared(prepared,u):
    prob=prepared['prob']; joint=prepared['joint']
    c=prefix_scaled(prob,np.asarray(u,float),joint)
    qp=solve_normalized_qp(c,joint['C'],prob.eps,tol=1e-12,max_iter=3000)
    return qp,joint,c


def tail_lower_bound(q,N,u,W,ridge=1e-11,dps=220):
    return tail_lower_bound_prepared(prepare_tail(q,N,W,ridge=ridge,dps=dps),u)


def validate_fixed_candidate(q,N,u,W,ridge=1e-11,dps=220,max_outer=8,
                             eta_stop=1e-12,S_levels=(6.0,8.0,10.0),
                             lambda_levels=(0.995,0.999,0.9999)):
    W=dedupe(W);hist=[]
    if not W:raise ValueError('empty witness pool')
    si=0;li=0
    for it in range(max_outer):
        qp,joint,c=tail_lower_bound(q,N,u,W,ridge=ridge,dps=dps)
        prob=ReducedProblem(int(N),3,int(N)*float(q),scale=.30)
        oracle=find_min_reduced_cost(prob,np.asarray(u,float),qp.alpha,joint,
                                     S=S_levels[si],lambda_max=lambda_levels[li],
                                     s_grid=161,refine_k=12,dps=dps)
        lb=oracle['lambda_star']>=lambda_levels[li]-1e-5
        sb=abs(oracle['s_star'])>=0.985*S_levels[si]
        hist.append(dict(iteration=it,witness_count=len(W),m2=qp.m2_dual,
                         eta_min=oracle['eta_min'],lambda_star=oracle['lambda_star'],
                         s_star=oracle['s_star'],lambda_boundary=lb,s_boundary=sb,
                         raw_min_eig=joint['raw_corr_min_eig'],kkt=qp.projected_kkt_inf,
                         complementarity=qp.complementarity_inf))
        if oracle['eta_min']>=-eta_stop and not lb and not sb:
            return dict(status='COHERENT_CONTINUUM_STATIONARY',m2=qp.m2_dual,qp=qp,joint=joint,
                        oracle=oracle,witnesses=W,history=hist)
        expanded=False
        if sb and si<len(S_levels)-1:si+=1;expanded=True
        if lb and li<len(lambda_levels)-1:li+=1;expanded=True
        w=(oracle['lambda_star'],oracle['s_star'])
        if not any(abs(w[0]-a)<2e-7 and abs(w[1]-b)<2e-6 for a,b in W):W.append(w)
        if len(W)>96:W=W[-96:]
        if (lb and li==len(lambda_levels)-1) or (sb and si==len(S_levels)-1):
            if not expanded:
                return dict(status='COHERENT_DOMAIN_BOUNDARY_UNRESOLVED',m2=qp.m2_dual,qp=qp,joint=joint,
                            oracle=oracle,witnesses=W,history=hist)
    qp,joint,c=tail_lower_bound(q,N,u,W,ridge=ridge,dps=dps)
    return dict(status='COHERENT_CONTINUUM_OUTER_LIMIT',m2=qp.m2_dual,qp=qp,joint=joint,
                oracle=hist[-1] if hist else {},witnesses=W,history=hist)
