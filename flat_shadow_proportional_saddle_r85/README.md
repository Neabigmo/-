# R85 — proportional-gap joint saddle and the signed-cancellation boundary

Date: 2026-09-07.

R85 closes the next useful one-sided part of the growing-gap analysis.  In
the formal same-factor/Jacobi hierarchy, for `d/j -> delta > 0`, the exact
finite simplex decomposition and Stirling bookkeeping give

`limsup (1/j) log(j^d |K_(j+d,j)|)
 <= delta*(1 + log(3/delta))`.

Equivalently,

`|K_(j+d,j)| <= j^(-d)
 exp(j*delta*(1 + log(3/delta)) + o(j))`.

This is an upper bound for the full signed kernel, not a lower bound from a
single modulus-maximizing path.  It implies that every fixed proportional
gap is super-exponentially tame after the `n^(-j)` coefficient rescaling,
while the original `4*sqrt(n)` weighted channel is at most exponential.

## Exact blocks checked locally

1. The root-of-unity filter is the exact complex coefficient

   `B_(r,j) = Re[ omega^(2r+1) [x^(j+r+1)]
      (1+omega*x)^(2r+1)(1+x)^(2j+1) /
      binom(2j+2r+2,j+r+1) ]`,

   with `omega=exp(2*pi*i/3)`.  With
   `rho=r/(j+r)`, its saddle polynomial is

   `1 + (1-omega)*(2*rho-1)*x - omega*x^2 = 0`.

   This is the corrected normalization: if `delta=j/r`, then
   `rho=1/(1+delta)`; if `delta=r/j`, then
   `rho=delta/(1+delta)`.

2. The signed Green coefficient has the exact positive-integral form

   `G_(ell+g,ell) = (-1)^g/g! *
      [1 + 2g integral_0^1 t^ell(2-t)^(g-1) dt]`.

   For `L=ell/j` and `g/j -> gamma`, its exponential integral rate is

   `J_G(L,gamma) = 0`, when `gamma <= L`, and otherwise

   `L log(2L/(L+gamma)) + gamma log(2gamma/(L+gamma))`.

   On the interior branch, with `L=1+delta-gamma`,
   `d J_G/d gamma = log(gamma/L)`.

3. For the Hermite/source band with `s/ell -> lambda in (0,1)`, the
   endpoint summation has the nonzero prefactor

   `p_(ell,ell-s) / T_0 -> (1-lambda)/(1+lambda)^3`,

   where
   `T_0 = 2*(s-1)!*binom(ell+1,s-1)*binom(ell-3,s-1)`.

   The first two endpoint groups have term ratios
   `T_a/T_0 -> (-1)^a binom(a+2,2) lambda^a` and
   `U_a/T_0 -> lambda*(-1)^a binom(a+2,2) lambda^a` for fixed `a`.
   Thus the proportional source endpoint is not itself killed by an
   alternating Hermite-band cancellation.

4. Combining the exact source formula, mixed angular coefficient, and
   Stirling factors gives the exponential-level path action

   `F_abs = delta - alpha log(alpha) - beta log(beta)
      - gamma log(gamma) + Lambda_A_abs(alpha)
      + J_G(1+alpha+beta,gamma)`,

   with `alpha+beta+gamma=delta` and `Lambda_A_abs <= 0` from `|B_(r,j)|<=1`.
   Dropping angular decay and maximizing the remaining real expression gives

   `sup F_abs = delta*(1 + log(3/delta))`.

   The local audit checks the entropy maximization algebra, including the
   `gamma > L` Green branch; it does not claim to prove the webpage's full
   uniform asymptotic remainder estimates.

## The genuine obstruction

The full signed path carries phase `(-1)^(r+g)` in addition to the angular
complex phase.  On the real simplex, the gamma stationary equation is

`log(beta/gamma) + i*pi = 0` when `gamma < L`,

and becomes

`log(beta/L) + i*pi = 0` when `gamma > L`.

There is therefore no positive-real signed-Green saddle.  A modulus saddle
cannot be converted into an actual exponential lower bound without a
contour-deformation and phase-control argument.

The formal complex cancellation `gamma=-beta` forces `alpha=delta` and
suggests the candidate rate

`R_can(delta) = delta*(1-log(delta)) + Lambda_A(delta)`,

but this remains conditional.  The missing statement is the proportional
signed-cancellation lemma `PSC_delta`: legal contour deformation, no larger
Stokes contribution, no exponential cancellation between conjugate angular
saddles, and a nonzero prefactor.  R85 does not prove `PSC_delta`.

## Status

The proportional sector now has a rigorous one-sided bound within the
formal finite/Jacobi hierarchy, and the `n^(-j)` rescaled coefficient route
survives it.  The actual proportional lower/equality, the mesoscopic bridge
`log(j) << d << j`, full hybrid Gram/triangular stability, R80 safe-window
improvement, D.1, global positivity, positive infinite backward towers,
backward OU divisibility, and `FS_3` remain OPEN.

The exact checks are in `audit_r85.py`.  They are intentionally finite and
symbolic: they validate the algebraic blocks and rate optimization, without
turning unproved uniform saddle remainders or `PSC_delta` into a theorem.
