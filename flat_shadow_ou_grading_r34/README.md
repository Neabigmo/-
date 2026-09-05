# R34 — OU-graded total-shadow high-pass obstruction

This folder records the finite proof-level audit requested after the R34 web
round.  It uses exact symbolic algebra only; it does not run an SOS solver,
optimizer, numerical degree search, or parameter sweep.

Run with:

```text
F:\anaconda3\python.exe -u flat_shadow_ou_grading_r34\audit_r34.py
```

Expected output:

```text
R34_FLAT_OU_COVARIANCE PASSED
R34_TOTAL_SHADOW_HIGH_PASS NO_GO
R34_SIGNED_OU_FILTER_NORM_BLOWUP RECORDED
R34_NONLINEAR_GRADED_TRANSGRESSION REMAINS OPEN
R34_AUDIT_COMPLETED
```

## Exact covariance identities

Write `X_t=sqrt(t)X+sqrt(1-t)Z` and `a_t=1-t+ta`.  The MGF calculation gives

`L_(a_t)^(P_t mu)=S_(sqrt(t))L_a^mu`.

If `P_M` is monic and `P_(M,t)(x)=t^(M/2)P_M(x/sqrt(t))`, then the flat-null
relations scale homogeneously and the first-defect functional obeys

`q_(M,t)=t^(M+1)q_M`.

For an atomic shadow `nu_M` and `rho_M=P_a nu_M`, setting
`nu_(M,t)=S_(sqrt(t))nu_M` gives `rho_(M,t)=P_t rho_M`.  These identities are
checked by formal MGF and polynomial substitution.

## Gauge-invariant total shadow response

For a finite value certificate

`gamma+q_M=P_K+E_(Q,K)+E_(flat,K)`,

evaluation on the genuine feasible law kills the ideal terms.  Evaluation on
the positive flat shadow kills `q_M` and the flat ideal, so the total response

`Theta_K(t)=P_K(rho_(M,t))+E_(Q,K)(rho_(M,t))`

is exactly `gamma`, independent of the equality gauge and of `t`.  The script
checks this abstract evaluation identity.

## Strict OU-grading no-go

Along the OU orbit, normalized Hermite coefficient `a_ell` scales as
`t^(ell/2)a_ell`; with `u=sqrt(t)`, a remote-only OU-regular expansion has no
constant term in `u`.  It therefore cannot equal the constant `Theta_K=gamma`
on an interval unless `gamma=0`.  The same argument applies to any regular
nonlinear monomial grading when all monomials have strictly positive total OU
grade.

Positive OU mixtures are inherently low-pass.  Their grade multiplier is
`m_ell=integral u^ell d nu(u)`, so `m_ell>=m_(ell+1)>=0`.  If `m_N=1` for a
probability mixture on `[0,1]`, then `u=1` almost surely and no filtering occurs.

Signed filters can annihilate low grades, but their norm is not uniform.  A
signed measure with moments `integral u^j d sigma=0` for `j<N` and
`integral u^N d sigma=1` satisfies

`||sigma||_TV >= 1 / inf_(deg p<N)||u^N-p||_infty`.

The monic Chebyshev minimax theorem on `[0,1]` gives
`inf = 2^(1-2N)`, hence `||sigma||_TV >= 2^(2N-1)`.  The audit checks the monic
polynomial and normalization algebra; the minimax equality is recorded as the
standard proof theorem, not obtained by numerical optimization.

Thus the entire class of direct linear OU/heat-semigroup grading of the total
shadow scalar is a strict proof-mechanism no-go.  The remaining target is
**Nonlinear Shadow-Compatible Graded Value Transgression**: a same-factor
cubic/Fock construction performed before summing to the gauge-invariant total,
with only a separately controlled grade-zero defect tending to zero.  Gaussian
rigidity and the `P_3K` bridge remain OPEN.
