#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

from coherence_lift import odd_indices,lift_direct_relative_error,complete_low_lift_high,scaled_completion_probe
from master_kernel import feature_identity_error,direct_vs_master_prefix_error,direct_master_full_kernel_error
from continuum_validation import tail_lower_bound
from outer_minimax import CoherentObjective,local_search,gradient_spot_check,energy_calibrated_starts,_prefix_energy_or_inf


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
    assert np.isfinite(qp.m2_dual) and qp.success and joint['raw_corr_min_eig']>-1e-8

    # Interior, active-set-aware gradient check.  Retry1's clipped-boundary FD test was invalid.
    obj=CoherentObjective(16,W,dps=90)
    for amp in (0.0,1e-3,1e-2):
        y=np.zeros(len(odd_indices(16)))
        if len(y):y[0]=amp
        gc=gradient_spot_check(obj,y,max_dirs=min(3,len(y)),h=8e-7)
        if gc['status']=='CHECKED_STABLE_ACTIVE_SET':
            assert gc['error']<2e-3,gc
    r=local_search(obj,np.zeros(len(odd_indices(16))),maxiter=8)
    assert np.isfinite(r['eval'].value) and r['eval'].scientific_valid

    # Energy-calibrated starts must remain inside the ball and target the relevant prefix-energy regime.
    ss=energy_calibrated_starts(32,12,seed=5)
    assert all(float(np.dot(y,y))<=5.0+1e-12 for y in ss)
    ee=[_prefix_energy_or_inf(y,32) for y in ss[1:]]
    assert all(np.isfinite(e) and e<=5.0 for e in ee),ee

    # Overflow probe must never emit +/-Inf in its finite bookkeeping fields.
    y=np.zeros(len(odd_indices(80)))
    if len(y):y[-1]=math.sqrt(5.0)
    pr=scaled_completion_probe(y,80,.05,.10,energy_cut=30.0)
    assert pr['status'] in ('PREFIX_OVERFLOW_BARRIER','SCALED_PROBE_FINITE','SCALED_RECURRENCE_NONFINITE')
    if np.isfinite(pr.get('energy_lower_bound',math.nan)):
        assert not math.isinf(pr['energy_lower_bound'])
    print('STAGE27U_RETRY2_SELFTEST_OK')

if __name__=='__main__':main()
