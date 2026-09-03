#!/usr/bin/env python3
from __future__ import annotations
import numpy as np
from dual_prune_retry4 import coordinate_dual_lb, CertifiedSingleWitnessPrune, _consistent_pair

c=np.array([2.0,-3.0,-1.0])
diag=np.array([1.0,2.0,4.0])
eps=0.5
lb,j,lbs=coordinate_dual_lb(c,diag,eps)
assert j==1 and abs(lb-18.0)<1e-12
assert abs(lbs[2]-1.0)<1e-12
assert issubclass(CertifiedSingleWitnessPrune,FloatingPointError)
rep1={'lb':18.0}; rep2={'lb':18.0*(1+1e-13)}
cons,rel=_consistent_pair(rep1,rep2)
assert cons < 18.0 and rel < 1e-10
assert _consistent_pair({'lb':18.0},{'lb':19.0}) is None
print('STAGE27U_RETRY4_DUAL_PRUNE_SELFTEST_OK')
