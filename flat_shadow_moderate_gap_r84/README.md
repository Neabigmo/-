# R84 — uniform logarithmic moderate-gap extension

Date: 2026-09-07.

R84 extends the R83 fixed-gap profile to a genuinely growing gap.  The
webpage response was read from the same in-app conversation and its local
records were available through the bridge during this round.  The analytic
uniform constants below are recorded as the webpage's formal-hierarchy
theorem; the local audit checks the exact algebraic blocks, finite anchors,
and exponent arithmetic, not every analytic remainder estimate.

## 1. Uniform building blocks

For `p=2r+1`, `N=j+r+1`, the root-of-unity filter has the exact complex
coefficient representation

`B_(r,j)=Re[ omega^p / binom(2N,N)
 [x^N](1+omega*x)^p(1+x)^(2N-p)]`,

where `omega=exp(2*pi*i/3)`.  The central saddle gives, uniformly for
`r<=log(j)/16`,

`B_(r,j)=-1/(2*4^r)(1+epsilon_A)`,

with `|epsilon_A|<=C_A r^2/j` in the proposed formal estimate.

The exact Hermite band from R83 can be grouped into a top term and lower
terms.  For `s=O(log ell)`, the proposed uniform estimate is

`p_(ell,ell-s)=2 ell^(2s-2)/(s-1)!
 [1+epsilon_H]`,

with `|epsilon_H|<=C_H s^2/ell`.  The signed Green has the exact positive
integral form

`G_(ell+g,ell)=(-1)^g/g!
 [1+2g integral_0^1 t^ell(2-t)^(g-1)dt]`,

and, for `g<=ell/2`,

`G_(ell+g,ell)=(-1)^g/g!(1+epsilon_G)`,
`0<=epsilon_G<=2g/(ell-g+2)`.

There is no artificial `3^g` loss in this Green factor.

## 2. Uniform path and cancellation estimate

Writing `m=j+r+1`, `ell=m+s`, and `g=k-ell`, a single path has the formal
uniform form

`T_(r,s,g)(j)=j^(-3) sigma_(r,s)(-1)^g/g!
 [1+epsilon_(r,s,g;j)]`,

where

`sigma_(r,s)=2(-1)^(r+1)r(r+1)!/[(2r+1)!(s-1)!]`.

The signed source sum has an `exp(z)` factor and the Green sum has an
`exp(-z)` factor.  They cancel in the leading term, but the small remaining
errors must be compared against the small final coefficient `kappa_d`.
Taking the absolute condition number of this cancellation gives the proposed
uniform relative estimate

`|j^3 K_(j+d,j)/kappa_d - 1|
 <= C_1 (d^2/j) exp(8d)`.

This is deliberately weaker than the tempting `exp(O(d^2/j))` relative error;
the latter requires additional higher-order cancellation and is not claimed.

## 3. Logarithmic moderate-gap theorem

For

`3<=d<=log(j)/16`,

the preceding estimate implies the formal-hierarchy result

`K_(j+d,j)=kappa_d j^(-3)
 [1+O((log j)^2/sqrt(j))]`,

uniformly over the entire logarithmic range, with

`kappa_d=2(-1)^(d-1)(d-2)(d-1)!/(2d-3)!`.

This is the first actual growing-gap result, rather than an argument that
chooses a different fixed gap for each polynomial degree.

For `j=floor(n/2)` and `d_n=floor(c log n)+3`, `0<c<1/16`, the R82 weights
therefore have a single-channel lower bound of the form

`||K_n|| >= exp[c_* (log n)^2
 - c_* (log n)log log n - C_* log n]`.

It is `e^(o(n))`, so this still does not prove an exponential-in-`n` lower
bound.  It does prove a quantitative stretched-superpolynomial obstruction.

## 4. Rescaled hybrid coefficient weight

For `tilde_omega_(n,j)=n^(-j)omega_(n,j)`, the exact fixed-gap ratio obeys

`tilde_omega_(n,j+d)/tilde_omega_(n,j)
 =4^d exp(O(d^2/j))`.

Consequently, in the whole range `3<=d<=log(j)/16`, the channel sum is
uniformly bounded by a constant times

`j^(-3) sum_d 4^d|kappa_d|`,

and the latter converges.  This validates the hybrid idea on the logarithmic
moderate-gap sector.  It does not establish boundedness when `d/j` tends to a
positive constant, nor does it provide Gram or triangular stability by itself.

## 5. Proportional-gap saddle and a necessary correction

The angular complex saddle can be written with

`rho=r/(j+r)` and

`Psi_rho(x)=rho log(1+omega*x)+(1-rho)log(1+x)
 -1/2 log(x)-log(2)`.

Its stationary equation is

`1+(1-omega)(2rho-1)x-omega*x^2=0`.

If one instead defines `delta=j/r`, then `rho=1/(1+delta)`; if
`delta=r/j`, then `rho=delta/(1+delta)`.  The webpage's displayed
parameterization of `rho` was inconsistent with its own saddle equation; the
local record uses the corrected normalized fraction.  This correction does
not solve the proportional-gap problem: angular phase, Hermite/source saddle,
and signed Green cancellation still have to be combined.

## 6. Status boundary and audit

The local audit passed:

- exact root-filter complex coefficient versus direct angular moments;
- the corrected saddle equation and normalization;
- the exact signed-Green integral and its uniform decay bound;
- exact fixed-gap kernel anchors through `d=8`;
- the rescaled-weight arithmetic;
- the stretched-superpolynomial exponent arithmetic.

Command:

`python flat_shadow_moderate_gap_r84/audit_r84.py`

The uniform analytic estimates with unnamed constants remain conditional on
the formal hierarchy until fully expanded into a line-by-line proof.  The
proportional-gap regime `d/j->delta>0`, a true exponential lower bound, full
hybrid-norm boundedness, R80 safe-window improvement, D.1, global positivity,
positive infinite backward towers, backward OU divisibility, and `FS_3` remain
OPEN.
