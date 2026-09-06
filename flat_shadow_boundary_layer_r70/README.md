# R70 — Finite-t boundary-layer necessity and no-reversal lemma

R70 moves beyond the now-closed Gaussian-local tangent sector. It gives a
general, auditable necessary condition for a shrinking zero of a normalized
finite-stage Jacobi/norm ratio. The statement is conditional on a finite-t
canonical branch being analytic (or twice continuously differentiable); it is
not an all-order construction of the positive backward tower.

## 1. Normalization

Write

    beta_hat_n(t)=beta_n(t)/n,
    ell_n=beta_hat_n'(0)=Lambda_n/n.

R69 gives, in the R64–R68 conditional full same-factor hierarchy,

    beta_hat_n(0)=1,
    ell_n~(33 sqrt(pi)/256)n^(-3/2)>0.

For an analytic finite-t branch, define

    beta_hat_n(t)=1+ell_n t+N_n(t),
    N_n(t)=sum_(r>=2) b_(n,r)t^r.

If `tau_n` is a zero in the analytic interval, then exactly

    N_n(tau_n)=-1-ell_n tau_n,
    sum_(r>=2)|b_(n,r)|tau_n^r >= 1+ell_n tau_n >= 1.

Consequently, if `tau_n->0`, then `N_n(tau_n)->-1`. A shrinking cutoff cannot
be caused by any finite-order Gaussian tangent approximation: the all-order
nonlinear tail must produce an order-one negative response at the shrinking
scale.

## 2. No-reversal alternatives

For a scale `s_n->0`, let

    Mcal_n(s_n)=sum_(r>=2)|b_(n,r)|s_n^r.

If `Mcal_n(s_n)<=1-delta` for a fixed `delta>0`, then for all
`0<=t<=s_n`,

    beta_hat_n(t)>=1+ell_n t-Mcal_n(s_n)>=delta,
    beta_n(t)>=delta n>0.

If `Mcal_n(s_n)=o(1)`, the stronger uniform statement is

    beta_hat_n(t)=1+ell_n t+o(1)=1+o(1),
    0<=t<=s_n.

There is also a C2 version. Put

    M_n(s)=sup_(0<=u<=s) (-beta_hat_n''(u))_+.

Taylor's integral identity gives

    beta_hat_n(t)>=1+ell_n t-(1/2)M_n(s)t^2.

Thus `M_n(s_n)s_n^2<=2(1-delta)` excludes a zero on `[0,s_n]`. Conversely,
if `tau_n` is a zero, then

    tau_n^2 M_n(tau_n)>=2(1+ell_n tau_n),

so `tau_n->0` forces

    M_n(tau_n)>=(2+o(1))/tau_n^2.

For the unnormalized coefficient this is

    sup_(0<=t<=tau_n)(-beta_n''(t))_+
      >=(2+o(1)) n/tau_n^2.

## 3. Analytic-radius corollary and scope

If `beta_hat_n` is analytic on `|t|<R_n` and uniformly bounded there by a
constant `M`, Cauchy's estimate yields

    Mcal_n(s_n)<=M (s_n/R_n)^2/(1-s_n/R_n).

Therefore `s_n/R_n->0` gives uniform no-reversal:
`beta_n(t)=n(1+o(1))` for `0<=t<=s_n`. Any genuine shrinking zero must therefore
occur at a scale not negligible relative to its complex analytic radius, or
the normalized branch must lose uniform boundedness.

R70 does not prove either a negative boundary-layer profile or an all-n
uniform no-reversal scale: R64–R69 do not provide an all-order bound on the
Taylor coefficients or a uniform complex radius. Its reportable contribution
is the exact conversion of the finite-stage cutoff question into an
all-order-tail/curvature requirement. The next target is an all-order nonlinear
tail scaling lemma, not another Gaussian-point derivative.

Audit command:

    python flat_shadow_boundary_layer_r70/audit_r70.py

