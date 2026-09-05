# R29 proof-level audit

This audit records the R29 reduction of the flat-shadow problem to a one-body
next-norm defect.  It is intentionally limited to exact algebraic identities;
it does not run a numerical sweep and does not claim a genuine full-exact
counterexample.

## Checked

1. When two laws share moments through `2M+1`, the common monic degree `M+1`
   orthogonal direction has a norm difference equal to the difference of the
   next Jacobi norms, hence to the common `h_M` times the next `beta` gap.  The
   same-factor heat identity `W=P_(-a)(xP)=xR-aR'` and monicity of `W` are also
   checked.  In the flat-shadow application, the boundary hypotheses identify
   this direction with the `W` appearing in `q_M`.
2. For `k_tau(x,y)=exp(-tau(x-y)^2/6)`, the positive feature expansion is
   checked algebraically.  The triangle identity
   `sum_{i<j}(X_i-X_j)^2=3Q` gives the cubic trace integrand
   `exp(-tau Q/2)`, whose genuine exact-law average is `1/(1+tau)`.
3. For a positive trace-one spectrum, the Cauchy identity
   `(sum lambda)(sum lambda^3)-(sum lambda^2)^2
   =sum_{i<j}lambda_i lambda_j(lambda_i-lambda_j)^2`
   and `0<=lambda_i<=1` yield
   `1/(1+tau) <= Tr(T_tau^2) <= 1/sqrt(1+tau)` and
   `||T_tau||_op <= (1+tau)^(-1/3)` when `Tr(T_tau^3)=1/(1+tau)`.
4. Matching the first `K` exact `Q` moments makes the Taylor series of
   `Z_mu(z)` agree with `(1+z)^(-1)` through degree `K`, so the radial
   transform difference has a zero of order `K+1`.  The elementary identity
   `Q <= X_1^2+X_2^2+X_3^2` is also checked.

## Still open

All four checks are unitary-invariant or scalar/radial.  They do not compare
the directional Rayleigh defect
`q_M=||P_(-a)(xP_M)||_{L^2(mu)}^2-
||P_(-a)(xP_M)||_{L^2(rho_M)}^2`.

The missing result is the `Flat-Shadow Tail-Ejection Certificate`: a negative
one-body head defect must force a uniformly visible remote Hermite/Jacobi tail,
with a tail bound strong enough to imply `Omega_K -> 0`.  Ordinary
Christoffel/Markov/Stieltjes estimates, scalar radial exactness, Schatten
contraction, and purely triangular Jacobi elimination do not supply this
directional reverse estimate.  `P_3K` and Gaussian rigidity remain separate.

Run:

```powershell
& 'F:\anaconda3\python.exe' flat_shadow_tail_gain_r29/audit_r29.py
```

Expected markers: `R29_TAIL_EJECTION_CERTIFICATE REMAINS OPEN` and
`R29_AUDIT_COMPLETED`.
