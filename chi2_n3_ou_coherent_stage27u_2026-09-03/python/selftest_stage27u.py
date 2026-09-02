#!/usr/bin/env python3
from __future__ import annotations
import math,tempfile
from pathlib import Path
import numpy as np

from coherence_lift import odd_indices,lift_direct_relative_error,complete_low_lift_high
from master_kernel import feature_identity_error,direct_vs_master_prefix_error,direct_master_full_kernel_error
from joint_tail_core import build_joint_tail
from continuum_validation import tail_lower_bound
from outer_minimax import CoherentObjective,local_search


def main():
    for N in (16,24,32):
        dim=len(odd_indices(N));y=np.zeros(dim)
        err,cc,uh,rh=lift_direct_relative_error(y,N,.05,.10)
        assert err<1e-10,(N,err)
    rng=np.random.default_rng(17)
    for N in (24,48):
        for _ in range(4):
            q=float(rng.choice([.05,.08,.10]));l=float(rng.uniform(0,.8));s=float(rng.uniform(-2,2))
            assert feature_identity_error(q,l,s,N,120)<1e-40
            assert direct_vs_master_prefix_error(q,l,s,N,160)<1e-40
            assert direct_master_full_kernel_error(q,(l,s),.10,(.3,.7),160)<1e-40
    W=[(.2,-1.0),(.4,.5),(.7,1.2),(.85,-.3)]
    cc=complete_low_lift_high(np.zeros(len(odd_indices(24))),24,.05,.10)
    qp,joint,c=tail_lower_bound(.10,24,cc.u_high,W,dps=100)
    assert np.isfinite(qp.m2_dual) and joint['raw_corr_min_eig']>-1e-8
    obj=CoherentObjective(16,W,dps=90);r=local_search(obj,np.zeros(len(odd_indices(16))),maxiter=8)
    assert np.isfinite(r['eval'].value)
    print('STAGE27U_SELFTEST_OK')

if __name__=='__main__':main()
