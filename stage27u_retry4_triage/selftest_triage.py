#!/usr/bin/env python3
from __future__ import annotations
import mpmath as mp

mp.mp.dps=80
# Synthetic normalized 2x2 QP: c=(-2,-1), C=[[1,.2],[.2,1]].
a=mp.mpf(1); d=mp.mpf(1); b=mp.mpf('.2'); ci=mp.mpf(-2); cj=mp.mpf(-1)
det=a*d-b*b
assert det>0
ai=(-d*ci+b*cj)/det
aj=(b*ci-a*cj)/det
assert ai>0 and aj>0
f=a*ai*ai+2*b*ai*aj+d*aj*aj+2*ci*ai+2*cj*aj
lb=-f
assert lb > mp.mpf(4)
print('STAGE27U_RETRY4_TRIAGE_SELFTEST_OK')
