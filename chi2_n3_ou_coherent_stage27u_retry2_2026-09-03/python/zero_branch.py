from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

from reduced_core import ReducedProblem
from normalized_kkt_stage26 import scaled_hermites_ld


@dataclass
class ZeroBranchState:
    q: float
    N: int
    kappa: float
    eps: float
    prob: ReducedProblem
    x: np.ndarray
    u: np.ndarray
    b: np.ndarray
    energy: float
    fock_residual: float


def zero_branch_state(q: float, N: int, d: int = 3, scale: float = 0.30) -> ZeroBranchState:
    """Return the canonical odd-zero Fock branch at fixed q,N.

    The distinguished coefficient u_d is fixed to 1 by ReducedProblem's
    normalization; every free odd coordinate is set to zero and the even
    coordinates are completed from the exact finite Fock recurrence.
    """
    q=float(q);N=int(N)
    if not (q>0 and N>=d):
        raise ValueError('require q>0 and N>=d')
    prob=ReducedProblem(N,d,N*q,scale=scale)
    x=np.zeros(len(prob.free_odds),float)
    r,JR,b,u,maxres,aux=prob.state(x,need_jac=False)
    E=float(np.dot(u[d:N+1],u[d:N+1]))
    return ZeroBranchState(q,N,N*q,prob.eps,prob,x,np.asarray(u,float),np.asarray(b,float),E,float(maxres))


def prefix_density(state: ZeroBranchState, lam: float, s: float) -> float:
    g=scaled_hermites_ld(state.q,float(lam),float(s),state.N)
    return float(1.0+state.eps*np.sum(np.asarray(state.u[3:state.N+1],np.longdouble)*g[3:state.N+1],dtype=np.longdouble))


def semiclassical_tau(kappa: float, lam: float, s: float) -> float:
    lam=float(lam);kappa=float(kappa);s=float(s)
    if lam<=0 or kappa<=0:
        return math.copysign(math.inf,s) if s else 0.0
    return s/(2.0*math.sqrt(lam*kappa))
