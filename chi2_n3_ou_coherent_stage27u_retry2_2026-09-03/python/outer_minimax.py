from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from scipy.optimize import minimize

from coherence_lift import (complete_low_lift_high,complete_low_lift_high_with_jac,odd_indices,scaled_completion_probe)
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
    scientific_valid: bool = True
    status: str = 'FINITE_TAIL'


def _active_signature(qp):
    if qp is None or len(qp.alpha)==0:
        return ()
    a=np.asarray(qp.alpha,float)
    th=max(1e-11,1e-8*max(float(np.max(np.abs(a))),1e-300))
    return tuple(int(i) for i in np.where(a>th)[0])


class CoherentObjective:
    def __init__(self,N,W,q_low=.05,q_high=.10,A=5.0,ridge=1e-11,dps=180):
        self.N=int(N);self.W=list(W);self.q_low=float(q_low);self.q_high=float(q_high)
        self.A=float(A);self.ridge=float(ridge);self.dps=int(dps);self.calls=0
        self.prepared=prepare_tail(self.q_high,self.N,self.W,ridge=self.ridge,dps=self.dps)
        self._last_y=None;self._last=None;self.barrier_evaluations=0

    def _barrier(self,y,exc):
        probe=scaled_completion_probe(y,self.N,self.q_low,self.q_high,energy_cut=self.A+25.0)
        if not probe.get('definitely_over_cut',False):
            # This is an unexpected numerical failure rather than a certified-over-cut region.
            raise exc
        self.barrier_evaluations+=1
        # Smooth finite algorithmic barrier.  It is deliberately far above every scientific
        # candidate and is NEVER serialized as a lower bound or certificate.
        yy=float(np.dot(y,y)); value=1.0e6+100.0*yy
        grad=200.0*np.asarray(y,float)
        return EvalResult(value,value+self.A,self.A+25.0,0.0,
                          np.zeros(self.N+1,float),float(probe.get('fock_residual',0.0)),None,grad,
                          False,'PREFIX_OVERFLOW_BARRIER')

    def evaluate(self,y):
        y=np.asarray(y,float)
        if self._last_y is not None and np.array_equal(y,self._last_y):return self._last
        self.calls+=1
        try:
            cc,J=complete_low_lift_high_with_jac(y,self.N,self.q_low,self.q_high)
        except FloatingPointError as exc:
            r=self._barrier(y,exc)
            self._last_y=y.copy();self._last=r;return r
        E=cc.prefix_energy_high
        gradE=J[3:self.N+1,:].T@(2.0*cc.u_high[3:self.N+1])
        if not np.isfinite(E) or not np.all(np.isfinite(gradE)):
            r=self._barrier(y,FloatingPointError('nonfinite coherent prefix energy/Jacobian'))
        elif E>self.A+25:
            r=EvalResult(E-self.A,E,E,0.0,cc.u_high,cc.fock_residual_low,None,np.asarray(gradE,float),True,'PREFIX_ONLY')
        else:
            qp,joint,c=tail_lower_bound_prepared(self.prepared,cc.u_high)
            if not qp.success or not np.isfinite(qp.m2_dual):
                raise FloatingPointError(f'NNQP invalid success={qp.success} m2={qp.m2_dual}')
            T=max(0.0,float(qp.m2_dual));tot=E+T
            if T>0 and len(qp.alpha):
                eps=float(self.prepared['prob'].eps)
                weighted=np.zeros(self.N+1,float)
                for a,g,dn in zip(qp.alpha,joint['gprefix'],joint['dnorm']):
                    if a!=0:weighted += float(a)*np.asarray(g,float)/float(dn)
                # Envelope theorem for m2=-min(alpha^T C alpha+2c^T alpha)/eps^2,
                # with dc/du=eps*g/dnorm gives dm2/du=-(2/eps) sum alpha*g/dnorm.
                dmdu=(-2.0/eps)*weighted
                grad=np.asarray(gradE + J[3:self.N+1,:].T@dmdu[3:self.N+1],float)
            else:grad=np.asarray(gradE,float)
            if not np.all(np.isfinite(grad)):
                raise FloatingPointError('nonfinite coherent envelope gradient')
            r=EvalResult(tot-self.A,tot,E,T,cc.u_high,cc.fock_residual_low,qp,grad,True,'FINITE_TAIL')
        self._last_y=y.copy();self._last=r;return r

    def fun(self,y):return float(self.evaluate(y).value)
    def jac(self,y):return np.asarray(self.evaluate(y).grad,float)



def _prefix_energy_or_inf(y,N,q_low=.05,q_high=.10):
    try:
        cc=complete_low_lift_high(y,N,q_low,q_high)
        e=float(cc.prefix_energy_high)
        return e if np.isfinite(e) else math.inf
    except FloatingPointError:
        pr=scaled_completion_probe(y,N,q_low,q_high,energy_cut=30.0)
        if pr.get('definitely_over_cut',False):
            return max(30.0,float(pr.get('energy_lower_bound',30.0)))
        return math.inf


def energy_calibrated_starts(N,count,q_low=.05,q_high=.10,seed=20260903,radius=math.sqrt(5.0)):
    """Random directions scaled to scientifically relevant high-q prefix-energy levels.

    Uniform-in-volume starts are pathological here: in high dimension almost every point sits
    near the odd-energy sphere and coherent even completion can explode.  We instead solve a
    one-dimensional radial calibration along each random direction.
    """
    dim=len(odd_indices(N));rng=np.random.default_rng(seed);out=[np.zeros(dim,float)]
    targets=(1.05,1.15,1.30,1.60,2.20,3.00,4.20,4.75)
    for k in range(max(0,count-1)):
        z=rng.normal(size=dim);z/=max(np.linalg.norm(z),1e-300)
        target=float(targets[k%len(targets)])
        lo=0.0;hi=min(radius,1e-6);ehi=_prefix_energy_or_inf(z*hi,N,q_low,q_high)
        while hi<radius and np.isfinite(ehi) and ehi<target:
            lo=hi;hi=min(radius,hi*3.0);ehi=_prefix_energy_or_inf(z*hi,N,q_low,q_high)
        if hi>=radius and np.isfinite(ehi) and ehi<target:
            rr=radius
        else:
            # Bisection on the first crossing.  Monotonicity is not assumed globally; we only
            # use the local first-crossing bracket generated above.
            for _ in range(18):
                mid=0.5*(lo+hi);em=_prefix_energy_or_inf(z*mid,N,q_low,q_high)
                if np.isfinite(em) and em<=target:lo=mid
                else:hi=mid
            rr=lo
        out.append(z*rr)
    return out

def random_ball_starts(dim,count,radius=math.sqrt(5.0),seed=20260903):
    """Stratified starts instead of uniform-in-volume starts (which concentrate at the boundary)."""
    rng=np.random.default_rng(seed);out=[np.zeros(dim,float)]
    radial_fracs=np.asarray([.06,.12,.22,.35,.50,.68,.82,.94],float)
    for k in range(max(0,count-1)):
        z=rng.normal(size=dim);z/=max(np.linalg.norm(z),1e-300)
        frac=float(radial_fracs[k%len(radial_fracs)])
        # Small jitter preserves broad coverage without pushing almost every high-dim point to ||y||=sqrt(5).
        frac=min(.98,max(.02,frac*(.9+.2*rng.random())))
        out.append(z*(radius*frac))
    return out


def _clip_ball(y,radius=math.sqrt(5.0)):
    y=np.asarray(y,float);n=np.linalg.norm(y)
    return y if n<=radius else y*(radius/n)


def gradient_spot_check(obj,y,max_dirs=4,h=1e-6):
    """Check the unconstrained envelope gradient only at interior, active-set-stable points.

    Retry1 incorrectly clipped y+/-h e_j back to the ball and compared that constrained
    directional derivative to the raw coordinate gradient.  This routine never does that.
    """
    y=np.asarray(y,float);base=obj.evaluate(y)
    if not base.scientific_valid or base.grad is None or not np.all(np.isfinite(base.grad)):
        return dict(status='INVALID_BASE',error=math.nan,count=0,active_stable=False)
    slack=5.0-float(y@y)
    if slack <= max(1e-5,20*h*(1+np.linalg.norm(y))):
        return dict(status='BOUNDARY_SKIPPED',error=math.nan,count=0,active_stable=False)
    sig0=_active_signature(base.qp);errs=[];used=0
    for j in range(min(len(y),max_dirs)):
        step=h*(1+abs(float(y[j])))
        yp=y.copy();ym=y.copy();yp[j]+=step;ym[j]-=step
        ep=obj.evaluate(yp);em=obj.evaluate(ym)
        if not (ep.scientific_valid and em.scientific_valid):
            continue
        if ep.status!=base.status or em.status!=base.status:
            continue
        if base.qp is not None:
            if _active_signature(ep.qp)!=sig0 or _active_signature(em.qp)!=sig0:
                continue
        fd=(ep.value-em.value)/(2*step)
        an=float(base.grad[j])
        errs.append(abs(fd-an)/(1+abs(fd)+abs(an)));used+=1
    obj.evaluate(y)  # restore cache
    if not used:
        return dict(status='ACTIVE_SET_OR_BRANCH_SWITCH',error=math.nan,count=0,active_stable=False)
    return dict(status='CHECKED_STABLE_ACTIVE_SET',error=float(max(errs)),count=used,active_stable=True)


def local_search(obj,start,maxiter=220):
    start=_clip_ball(start);B=5.0
    cons={'type':'ineq','fun':lambda y:B-float(np.dot(y,y)),'jac':lambda y:-2*np.asarray(y,float)}
    op=minimize(obj.fun,start,jac=obj.jac,method='SLSQP',constraints=[cons],
                options=dict(maxiter=maxiter,ftol=1e-10,disp=False))
    y=_clip_ball(op.x);ev=obj.evaluate(y)
    # If the optimizer ended in an algorithmic barrier, prefer the original start when it is valid.
    if not ev.scientific_valid:
        es=obj.evaluate(start)
        if es.scientific_valid:
            y=start.copy();ev=es
    gc=gradient_spot_check(obj,y,max_dirs=3,h=2e-6)
    best=(ev.value,y,ev)
    step=0.02/max(1,math.sqrt(len(y)))
    for j in range(min(len(y),12)):
        for sg in (-1,1):
            yy=_clip_ball(y+sg*step*np.eye(1,len(y),j).ravel());ee=obj.evaluate(yy)
            if ee.scientific_valid and (not best[2].scientific_valid or ee.value<best[0]):best=(ee.value,yy,ee)
    return dict(y=best[1],eval=best[2],success=bool(op.success),message=str(op.message),nit=int(getattr(op,'nit',0)),
                grad_fd_error=float(gc['error']) if np.isfinite(gc['error']) else math.nan,
                grad_check_status=gc['status'],grad_check_count=int(gc['count']))


def multistart_search(N,W,starts,q_low=.05,q_high=.10,A=5.0,ridge=1e-11,dps=180,maxiter=220):
    obj=CoherentObjective(N,W,q_low=q_low,q_high=q_high,A=A,ridge=ridge,dps=dps)
    rows=[]
    for i,s in enumerate(starts):
        try:
            r=local_search(obj,s,maxiter=maxiter);ev=r['eval']
            rows.append(dict(start_id=i,y=r['y'],margin=(float(ev.value) if ev.scientific_valid else math.nan),
                             total_lb=(float(ev.total_lb) if ev.scientific_valid else math.nan),
                             prefix_energy=(float(ev.prefix_energy) if ev.scientific_valid else math.nan),
                             tail_lb=(float(ev.tail_lb) if ev.scientific_valid else math.nan),
                             fock_residual=(float(ev.fock_residual) if ev.scientific_valid else math.nan),
                             scientific_valid=bool(ev.scientific_valid),eval_status=ev.status,
                             success=r['success'],message=r['message'],nit=r['nit'],
                             grad_fd_error=r.get('grad_fd_error',math.nan),grad_check_status=r.get('grad_check_status'),
                             grad_check_count=r.get('grad_check_count',0)))
        except Exception as e:
            rows.append(dict(start_id=i,error=repr(e),margin=math.nan,scientific_valid=False,
                             eval_status='UNEXPECTED_START_EXCEPTION',success=False,message=repr(e),
                             grad_fd_error=math.nan,grad_check_status='NOT_RUN',grad_check_count=0))
    rows.sort(key=lambda r:(0 if r.get('scientific_valid') else 1,
                            r.get('margin') if np.isfinite(r.get('margin',math.nan)) else math.inf))
    return rows,obj.calls,obj.barrier_evaluations
