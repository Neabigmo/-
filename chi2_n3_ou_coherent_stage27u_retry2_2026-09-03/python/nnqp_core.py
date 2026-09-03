from __future__ import annotations
import numpy as np
from normalized_kkt_stage25 import solve_normalized_qp


def solve_tail_nnqp(c,C,eps,tol=1e-12,max_iter=3000):
    qp=solve_normalized_qp(np.asarray(c,float),np.asarray(C,float),float(eps),tol=tol,max_iter=max_iter)
    return qp


def nnqp_audit(qp,kkt_tol=1e-8,comp_tol=1e-8,dp_tol=1e-7):
    return dict(
        kkt_ok=bool(qp.projected_kkt_inf <= kkt_tol),
        complementarity_ok=bool(qp.complementarity_inf <= comp_tol*(1+np.linalg.norm(qp.alpha))),
        dual_primal_ok=bool(qp.dual_primal_rel <= dp_tol),
        success=bool(qp.success),
    )
