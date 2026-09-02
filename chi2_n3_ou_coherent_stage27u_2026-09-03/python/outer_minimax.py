from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from scipy.optimize import minimize

from coherence_lift import complete_low_lift_high,complete_low_lift_high_with_jac,odd_indices
from continuum_validation import prepare_tail,tail_lower_bound_prepared


@dataclass
class EvalResult:
    value: float
    total_lb: float
    prefix_energy: float
    tail_lb: float
    u_high: np.ndarray
    fock_residual: float
    qp: object|None
    grad: np.ndarray|None = None


class CoherentObjective:
    def __init__(self,N,W,q_low=.05,q_high=.10,A=5.0,ridge=1e-11,dps=180):
        self.N=int(N);self.W=list(W);self.q_low=float(q_low);self.q_high=float(q_high)
        self.A=float(A);self.ridge=float(ridge);self.dps=int(dps);self.calls=0
        self.prepared=prepare_tail(self.q_high,self.N,self.W,ridge=self.ridge,dps=self.dps)
        self._last_y=None;self._last=None

    def evaluate(self,y):
        y=np.asarray(y,float)
        if self._last_y is not None and np.array_equal(y,self._last_y):return self._last
        self.calls+=1
        cc,J=complete_low_lift_high_with_jac(y,self.N,self.q_low,self.q_high)
        E=cc.prefix_energy_high
        gradE=J[3:self.N+1,:].T@(2.0*cc.u_high[3:self.N+1])
        if not np.isfinite(E):
            r=EvalResult(1e12,math.inf,E,math.inf,cc.u_high,cc.fock_residual_low,None,np.zeros_like(y))
        elif E>self.A+25:
            r=EvalResult(E-self.A,E,E,0.0,cc.u_high,cc.fock_residual_low,None,np.asarray(gradE,float))
        else:
            qp,joint,c=tail_lower_bound_prepared(self.prepared,cc.u_high)
            T=max(0.0,float(qp.m2_dual));tot=E+T
            if T>0 and len(qp.alpha):
                eps=float(self.prepared['prob'].eps)
                weighted=np.zeros(self.N+1,float)
                for a,g,dn in zip(qp.alpha,joint['gprefix'],joint['dnorm']):
                    if a!=0:weighted += float(a)*np.asarray(g,float)/float(dn)
                dmdu=(-2.0/eps)*weighted
                grad=np.asarray(gradE + J[3:self.N+1,:].T@dmdu[3:self.N+1],float)
            else:grad=np.asarray(gradE,float)
            r=EvalResult(tot-self.A,tot,E,T,cc.u_high,cc.fock_residual_low,qp,grad)
        self._last_y=y.copy();self._last=r;return r

    def fun(self,y):return float(self.evaluate(y).value)
    def jac(self,y):return np.asarray(self.evaluate(y).grad,float)


def random_ball_starts(dim,count,radius=math.sqrt(5.0),seed=20260903):
    rng=np.random.default_rng(seed);out=[np.zeros(dim,float)]
    for _ in range(max(0,count-1)):
        z=rng.normal(size=dim);z/=max(np.linalg.norm(z),1e-300)
        r=radius*(rng.random()**(1/max(dim,1)))
        out.append(z*r)
    return out


def _clip_ball(y,radius=math.sqrt(5.0)):
    y=np.asarray(y,float);n=np.linalg.norm(y)
    return y if n<=radius else y*(radius/n)


def local_search(obj,start,maxiter=220):
    start=_clip_ball(start);B=5.0
    cons={'type':'ineq','fun':lambda y:B-float(np.dot(y,y)),'jac':lambda y:-2*np.asarray(y,float)}
    op=minimize(obj.fun,start,jac=obj.jac,method='SLSQP',constraints=[cons],
                options=dict(maxiter=maxiter,ftol=1e-10,disp=False))
    y=_clip_ball(op.x);ev=obj.evaluate(y)
    fd_err=0.0;h=2e-6
    for j in range(min(len(y),3)):
        yp=y.copy();ym=y.copy();yp[j]+=h;ym[j]-=h;yp=_clip_ball(yp);ym=_clip_ball(ym)
        fd=(obj.fun(yp)-obj.fun(ym))/(2*h); fd_err=max(fd_err,abs(fd-ev.grad[j])/(1+abs(fd)+abs(ev.grad[j])))
    best=(ev.value,y,ev)
    step=0.02/max(1,math.sqrt(len(y)))
    for j in range(min(len(y),12)):
        for sg in (-1,1):
            yy=_clip_ball(y+sg*step*np.eye(1,len(y),j).ravel());ee=obj.evaluate(yy)
            if ee.value<best[0]:best=(ee.value,yy,ee)
    return dict(y=best[1],eval=best[2],success=bool(op.success),message=str(op.message),nit=int(getattr(op,'nit',0)),grad_fd_error=float(fd_err))


def multistart_search(N,W,starts,q_low=.05,q_high=.10,A=5.0,ridge=1e-11,dps=180,maxiter=220):
    obj=CoherentObjective(N,W,q_low=q_low,q_high=q_high,A=A,ridge=ridge,dps=dps)
    rows=[]
    for i,s in enumerate(starts):
        try:
            r=local_search(obj,s,maxiter=maxiter);ev=r['eval']
            rows.append(dict(start_id=i,y=r['y'],margin=ev.value,total_lb=ev.total_lb,
                             prefix_energy=ev.prefix_energy,tail_lb=ev.tail_lb,
                             fock_residual=ev.fock_residual,success=r['success'],message=r['message'],nit=r['nit'],grad_fd_error=r.get('grad_fd_error',math.nan)))
        except Exception as e:
            rows.append(dict(start_id=i,error=repr(e),margin=math.inf,success=False))
    rows.sort(key=lambda r:r.get('margin',math.inf))
    return rows,obj.calls
