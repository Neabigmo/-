# R152 — Semiclassical Hermite-Gram Bulk Limit / Toeplitz Positivity

Date: 2026-09-08  
Status: the fixed-offset bulk limit is identified for finite-support critical
shapes; it is positive for every real shape.  This is an obstruction to the
proposed bulk-negative-gap route, not a counterexample to the original law.

## 0. Scope and publication boundary

This is an independent local continuation of the R151 target.  It does not
replace the required webpage audit and it does not prove the original
positive backward-tower problem.  The global publication verdict remains:

`无（目前没有足够独立、完整、可审稿的发表性结果）`

The statement below is an operator-level bulk limit for a finite-support
critical coefficient shape.  It does not imply that a finite Hankel matrix is
positive, nor that the limiting operator lifts to a genuine iid probability
law satisfying the exact zero condition.

## 1. Exact scaled coefficient extraction

Let

`C_lambda(z)=sum_(k in K) U_k lambda^(k/2) z^k`,

where `K` is finite and the real coefficients `U_k` are fixed.  Put
`E(z)=exp(sum_(k in K)U_k z^k)`, so exactly

`exp(C_lambda(z))=E(sqrt(lambda) z)`.

For the Hermite Gram matrix defined by

`sum Gamma_mn u^m/sqrt(m!) v^n/sqrt(n!)`
`=exp(uv+C_lambda(u+v))`,

write `e_K=[z^K]E(z)`.  Direct coefficient extraction gives, whenever the
parities and ranges are admissible,

`Gamma_mn = sum_K e_K lambda^(K/2)
             sqrt(m!n!)/( (m+n-K)/2 )!
             binom(K,(K+m-n)/2)`.

Take `m=M_lambda+p`, `n=M_lambda+q`, with fixed integers `p,q`,
`M_lambda=floor(tau/lambda)`, and `tau>0`.  For each fixed `K`,

`lambda^(K/2) sqrt(m!n!)/( (m+n-K)/2 )! -> tau^(K/2)`.

Therefore the fixed-offset bulk limit is

`Gamma_(M+p,M+q) -> G_(p-q)(tau,U)`,

where

`G_l(tau,U)=sum_K e_K tau^(K/2) binom(K,(K+l)/2)`.

The finite-support exponential bound on `e_K` and `binom(K,.)<=2^K`
justifies passage from fixed `K` to the convergent full series.  This is an
entrywise/local-quadratic-form statement; vectors whose support grows with
`lambda^(-1)` require a separate uniform argument.

## 2. Toeplitz symbol and positivity

The preceding coefficients are exactly the Laurent coefficients of

`F_(tau,U)(x)=E(sqrt(tau)(x+x^(-1)))`

`=exp(sum_(k in K) U_k tau^(k/2)(x+x^(-1))^k)`.

On the unit circle `x=exp(i theta)`, this is

`F_(tau,U)(exp(i theta))`
`=exp(sum_(k in K) U_k tau^(k/2)(2 cos(theta))^k)>0`.

Consequently the limiting bi-infinite Toeplitz matrix satisfies, for every
finite vector `z`,

`sum_(p,q) conjugate(z_p) G_(p-q) z_q`
`=(1/(2 pi)) int_0^(2 pi) F_(tau,U)(exp(i theta))
  |sum_p z_p exp(i p theta)|^2 d theta >=0`.

For finite real `U` the symbol is strictly positive, so the limiting bulk
operator has no negative direction.  In particular, the R152 hoped-for
negative sparse limit cannot occur in this fixed-offset bulk scaling for any
finite-support real critical shape.

## 3. Consequence for the rigidity route

R137 still proves that, for fixed odd `d` and nonzero sparse amplitude, some
finite Hankel minor eventually fails.  R152 shows that such a failure cannot be
detected by a fixed-offset local limit at the first scale
`M~|a|^(-2/d)` alone.  The first failing vectors must use at least one of:

1. support growing with `lambda^(-1)`;
2. a boundary/edge regime rather than a bulk window near `M`;
3. coefficient shapes with no finite-support limit;
4. a genuinely global Hankel/zero-free constraint not visible in this Toeplitz
   symbol.

Thus the correct R152 conclusion is a rigorous route obstruction:
“critical bulk Toeplitz positivity” replaces the earlier unverified hope for a
bulk negative margin.  It does not provide a positive iid realization and does
not contradict R137's eventual finite-rank collapse.

## 4. Evidence grading

`PROVED at the formal/operator coefficient level`: the scaled coefficient
formula, the fixed-offset limit for finite-support shapes, and the Toeplitz
symbol identity/positivity under the stated convergence bound.

`NUMERICALLY AUDITED`: finite truncations of the coefficient series and entrywise
convergence for several `lambda`, `tau`, and real shapes (see `audit_r152.py`).

`OPEN`: uniform convergence for growing-support vectors, edge asymptotics,
first-failing-minor scale, all-order positive iid liftability, the
`RK=1 => full-SF` bridge, and the original backward-tower rigidity.

The next webpage task should not blindly seek a negative bulk operator.  It
should verify this Toeplitz obstruction, then target the edge/growing-support
semiclassical regime and state exactly which additional uniform estimate would
turn it into fixed-degree or moving-degree rigidity.
