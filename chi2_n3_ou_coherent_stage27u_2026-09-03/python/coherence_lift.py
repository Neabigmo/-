from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

from reduced_core import ReducedProblem


def odd_indices(N: int, d: int = 3):
    return list(range(d + 2, int(N) + 1, 2))


def coherence_factor(n: int, q_from: float, q_to: float, d: int = 3) -> float:
    q_from=float(q_from); q_to=float(q_to)
    if q_from <= 0 or q_to <= 0:
        raise ValueError("q must be positive")
    return (q_to/q_from)**((int(n)-d)/2.0)


def rescale_u(u, q_from: float, q_to: float, d: int = 3):
    u=np.asarray(u,float)
    out=np.zeros_like(u)
    for n in range(len(u)):
        if n < d:
            out[n]=u[n]
        else:
            out[n]=u[n]*coherence_factor(n,q_from,q_to,d=d)
    return out


def high_odd_to_low_x(y_high, N: int, q_low: float, q_high: float, d: int = 3):
    y=np.asarray(y_high,float)
    idx=odd_indices(N,d)
    if len(y) != len(idx):
        raise ValueError(f"expected {len(idx)} odd variables, got {len(y)}")
    return np.asarray([y[j]*coherence_factor(n,q_high,q_low,d=d) for j,n in enumerate(idx)],float)


def low_x_to_high_odd(x_low, N: int, q_low: float, q_high: float, d: int = 3):
    x=np.asarray(x_low,float)
    idx=odd_indices(N,d)
    if len(x) != len(idx):
        raise ValueError(f"expected {len(idx)} odd variables, got {len(x)}")
    return np.asarray([x[j]*coherence_factor(n,q_low,q_high,d=d) for j,n in enumerate(idx)],float)


@dataclass
class CoherentCompletion:
    N: int
    q_low: float
    q_high: float
    y_high: np.ndarray
    x_low: np.ndarray
    u_low: np.ndarray
    u_high: np.ndarray
    b_low: np.ndarray
    fock_residual_low: float
    prefix_energy_high: float


def complete_low_lift_high(y_high, N: int, q_low: float=.05, q_high: float=.10,
                           d: int=3, scale: float=.30) -> CoherentCompletion:
    N=int(N); y=np.asarray(y_high,float)
    prob=ReducedProblem(N,d,N*float(q_low),scale=scale)
    x=high_odd_to_low_x(y,N,q_low,q_high,d=d)
    _,_,b,u_low,maxres,_=prob.state(x,need_jac=False)
    u_low=np.asarray(u_low,float)
    u_high=rescale_u(u_low,q_low,q_high,d=d)
    E=float(np.dot(u_high[d:N+1],u_high[d:N+1]))
    return CoherentCompletion(N,float(q_low),float(q_high),y,x,u_low,u_high,np.asarray(b,float),float(maxres),E)


def complete_low_lift_high_with_jac(y_high, N: int, q_low: float=.05, q_high: float=.10,
                                    d: int=3, scale: float=.30):
    """Return coherent completion and du_high/dy_high.

    The low-q triangular Fock Jacobian is lifted exactly by OU coherence.
    """
    N=int(N); y=np.asarray(y_high,float); idx=odd_indices(N,d)
    prob=ReducedProblem(N,d,N*float(q_low),scale=scale)
    x=high_odd_to_low_x(y,N,q_low,q_high,d=d)
    _,_,b,u_low,maxres,aux=prob.state(x,need_jac=True)
    u_low=np.asarray(u_low,float);u_high=rescale_u(u_low,q_low,q_high,d=d)
    Jlow=np.zeros((N+1,len(idx)),float)
    for j,n in enumerate(idx):Jlow[n,j]=1.0
    for i,n in enumerate(aux['evens']):Jlow[n,:]=np.asarray(aux['dE_dO'][i,:],float)
    down=np.asarray([coherence_factor(n,q_high,q_low,d=d) for n in idx],float)
    lift=np.asarray([coherence_factor(n,q_low,q_high,d=d) if n>=d else 1.0 for n in range(N+1)],float)
    Jhigh=(lift[:,None]*Jlow)*down[None,:]
    E=float(np.dot(u_high[d:N+1],u_high[d:N+1]))
    cc=CoherentCompletion(N,float(q_low),float(q_high),y,x,u_low,u_high,np.asarray(b,float),float(maxres),E)
    return cc,Jhigh


def complete_direct_high(y_high, N: int, q_high: float=.10, d: int=3, scale: float=.30):
    N=int(N); y=np.asarray(y_high,float)
    prob=ReducedProblem(N,d,N*float(q_high),scale=scale)
    _,_,b,u,maxres,_=prob.state(y,need_jac=False)
    return np.asarray(u,float), np.asarray(b,float), float(maxres)


def lift_direct_relative_error(y_high, N: int, q_low: float=.05, q_high: float=.10,
                               d: int=3, scale: float=.30):
    cc=complete_low_lift_high(y_high,N,q_low,q_high,d=d,scale=scale)
    uh,_,rh=complete_direct_high(y_high,N,q_high,d=d,scale=scale)
    den=1.0+np.max(np.abs(uh[d:N+1]))
    err=float(np.max(np.abs(cc.u_high[d:N+1]-uh[d:N+1]))/den)
    return err,cc,uh,rh
