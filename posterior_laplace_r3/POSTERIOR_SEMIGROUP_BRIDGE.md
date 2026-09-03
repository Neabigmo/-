# Posterior semigroup bridge

Set `u=1/(2s)`, `v=tu/(t+u)`, and `r=t-v`.  Exact Gaussian product and
change-of-variable algebra give.  The implementation independently checks
the complete Gaussian product integrals for all eight signed triples at each
of three exact `(v,r,y)` points, and checks the bridge ratio at three exact
`(t,u,s,y)` points; it does not certify the target law itself.

`L_{t,y}(s)=(v/t) P_{r/3}(p_v^3)(y)/p_t(y)^3`.

For a Gaussian heat-smoothed density, the critical ratio is independent of
`y` and equals `(1+v+r)/(1+v)`.  The naive Holder argument is critical: the
conjugate Gaussian weights cancel, leaving a non-integrable constant factor.

The bridge is exact, but it does not itself supply the missing rigidity
inequality.
