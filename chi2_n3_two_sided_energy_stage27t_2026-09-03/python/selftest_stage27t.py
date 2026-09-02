#!/usr/bin/env python3
from __future__ import annotations
import tempfile
from pathlib import Path
import numpy as np
from zero_branch import zero_branch_state
from normalized_kkt_stage26 import scaled_hermites_ld
from mp_features import mp_scaled_hermites,build_feature_system,density_ld,density_mp,lambda_grid
from stable_primal_tail import dual_coordinate_qp,feasibility_projection,solve_tail


def main():
    q=.1;N=16;st=zero_branch_state(q,N)
    g1=scaled_hermites_ld(q,.7,1.2,24);g2=mp_scaled_hermites(q,.7,1.2,24,dps=100)
    err=max(abs(float(g1[i])-float(g2[i]))/(1+abs(float(g2[i]))) for i in range(25))
    assert err<1e-12
    print('PASS MP Hermite recurrence vs longdouble')
    W=[(.5,-1.0),(.7,.5),(.9,1.2),(.95,-1.5)]
    fs=build_feature_system(q,st.eps,N,st.u,W,12,dps=100)
    assert fs.max_diag_error<1e-12 and fs.max_corr_excess<1e-12 and fs.min_eigenvalue>-1e-10
    print('PASS normalized feature Gram PSD/diag audit')
    G=np.eye(3);b=np.array([1.,.5,-.2]);y,pg,_=dual_coordinate_qp(G,b);assert np.max(abs(y-[1,.5,0]))<1e-8 and pg<1e-8
    v=np.array([0.,0.]);Phi=np.array([[1.,0.],[0.,1.]]);bb=np.array([1.,2.]);vv,sl,_=feasibility_projection(Phi,bb,v);assert np.min(sl)>-1e-10 and np.linalg.norm(vv-[1,2])<1e-8
    print('PASS dual Gram QP and halfspace feasibility projection')
    v=np.zeros(8);z1=density_ld(q,st.eps,N,st.u,v,.8,.7);z2=density_mp(q,st.eps,N,st.u,v,.8,.7,dps=120);assert abs(z1-z2)<1e-10*(1+abs(z2))
    print('PASS MP density vs longdouble moderate-point agreement')
    assert lambda_grid(1-1e-16)[-1] <= 1 and lambda_grid(1-1e-16)[-1] > 0.999999999999
    print('PASS near-one lambda grid')
    # A tiny tail solve smoke: success here only tests the numerical path, not continuum feasibility.
    sol=solve_tail(q,st.eps,N,st.u,W,16,dps1=80,dps2=110)
    assert sol.feature_valid and np.isfinite(sol.energy) and sol.min_slack>-1e-8
    print('PASS stable finite-tail dual solve/recovery smoke')
    print('STAGE27T_SELFTEST_OK')
if __name__=='__main__':main()
