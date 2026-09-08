# R149 — Nonlinear Reflection Compensation / Odd-to-Even Continuum Audit

Date: 2026-09-08  
Status: local finite audit recorded; the exact positive-cone classification remains open.

## Evidence boundary

The webpage completed R149 after reading the public R148 commit
`5397c979702731107536227d82f773eddef4ee83`.  Its global publication verdict
remained:

`无（目前没有足够独立、完整、可审稿的发表性结果）`

This directory records only the claims that can be checked locally without
turning a formal jet into a probability law.  The script checks exact integer
profiles, Gaussian quadrature interfaces, finite signed-measure examples,
and asymptotic ratios.  It does **not** certify an all-order positive branch,
the classical characterization, moving-degree tower closure, novelty, or the
bridges `RK=1 => full-SF/all-row` and ordinary/Bargmann `=> P_3 K_sp`.

Throughout,

`Q(x_1,x_2,x_3) = ((x_1-x_2)^2+(x_2-x_3)^2+(x_3-x_1)^2)/3`.

## 1. Reflection quadratic form: exact function-space statement

Let `nu` be a nonzero finite positive measure and `sigma` a finite signed
measure.  Define

`Q_z^nu(sigma) = ∫∫∫ exp(-z Q(a,x,y)) dnu(a) dsigma(x) dsigma(y)`, `z>0`.

The kernel is bounded by one, so the integral is absolutely defined for
finite total variation; no bilateral exponential moment is required.

For `c=2z/3`,

`exp(-z Q(a,x,y))`
`= exp(-2 z a^2/3) exp(-2 z x^2/3+2 z a x/3)`
`  * exp(-2 z y^2/3+2 z a y/3) exp(c x y)`.

The Gaussian feature identity turns the fixed-`a` quadratic form into

`q_(z,a)(sigma)`
`= exp(-2 z a^2/3) E_G [ ∫ exp(-z x^2`
`  +(2 z a/3 + sqrt(2z/3) G)x) dsigma(x) ]^2 >= 0`.

If this square vanishes, the Gaussian-damped transform

`L_sigma(w)=∫ exp(-z x^2+w x) dsigma(x)`

is zero on the real line and is entire: on every compact set of `w`, the
Gaussian factor uniformly dominates all derivatives against finite total
variation.  At `w=i xi`, Fourier uniqueness gives
`exp(-z x^2) sigma=0`, hence `sigma=0`.  Therefore

`sigma != 0 => Q_z^nu(sigma)>0` for every `z>0`.

This is a genuine all-`z` measure theorem, but it is only a positive
quadratic source; it does not exclude exact nonlinear compensation.

If `nu=(mu+check(mu))/2` and `sigma=(mu-check(mu))/2`, then
`|sigma| <= nu` and `sigma(R)=0`.  Writing `h=dsigma/dnu`, `|h|<=1`, gives
the strict sandwich

`0 <= Q_z^nu(sigma) < F_z(nu)` when `sigma != 0`.

Consequently, an asymmetric exact candidate satisfying
`F_z(mu)=1/(1+2z)` would have to obey

`1/(4(1+2z)) < F_z(nu) < 1/(1+2z)` and
`0 < Q_z^nu(sigma) < 1/(4(1+2z))`.

The sandwich is a necessary constraint, not a contradiction.

## 2. Pure odd Hermite source and unique even quadratic jet

Let `gamma` be standard Gaussian measure and
`psi_n=He_n/sqrt(n!)`.  For odd `d>=3`, let
`sigma_d(dx)=psi_d(x) gamma(dx)`.  With

`r=2z/(1+2z)`,

the Gaussian-tilted covariance has
`Cov(X_2,X_3)=r/3` and `Var(X_2)=1-2r/3`.  The Hermite generating function
then yields the complete profile

`Q_z^gamma(sigma_d)`
`= (1/(1+2z)) (T_d/3^d) r^d`,

where

`T_d = sum_(j=0)^(floor(d/2)) d!/(j!^2 (d-2j)!)`

is the central trinomial coefficient.

The Gaussian continuum first variation satisfies

`D F_1[psi_(2m)](z)`
`= (3/(1+2z)) sqrt((2m)!)/m! (-r/3)^m`,

and vanishes on odd Hermite modes.  Thus the formal equation

`D F_1[h] + 3 Q_z^gamma(sigma_d)=0` for every `z>0`

has the unique even quadratic correction

`h=A_d psi_(2d)`,  `A_d=d! T_d/sqrt((2d)!)`.

The asymptotic is

`A_d ~ (sqrt(3)/2) (3/2)^d (pi d)^(-1/4)`.

This is an exact continuum-parameter second-order calculation.  It is not
an exact density construction.

For a general odd `f` with the necessary centering/variance constraints, if
`S_f(r)=Q_z^gamma(f gamma)/(1/(1+2z))=sum_(k>=2) q_k r^k`, then the only
possible even correction in `L^2(gamma)` has coefficients

`h_k=(-1)^(k+1) 3^k k!/sqrt((2k)!) q_k`,

and exists in `L^2` exactly when

`sum_(k>=2) 9^k (k!)^2/(2k)! |q_k|^2 < infinity`.

The inverse is therefore exponentially ill-conditioned, not a bounded
right inverse in the natural unweighted Hermite `L^2` topology.

## 3. What the quadratic tail calculation does and does not prove

At `|x|` of order `|epsilon|^(-1/d)`, the second-order truncation

`1+epsilon psi_d+epsilon^2 A_d psi_(2d)`

has leading rescaled profile `1+y+B_d y^2`, where

`B_d=T_d/binom(2d,d)`.

Pointwise nonnegativity of this quadratic profile would require
`4 T_d >= binom(2d,d)`.  The exact values give
`4T_3/binom(6,3)=7/5`, but
`4T_5/binom(10,5)=17/21<1`; the ratio decreases thereafter, so the
quadratic truncation is negative in a far tail for every odd `d>=5` and
nonzero sufficiently small `epsilon`.

This is only a finite-order no-go.  At the same tail scale,
`epsilon^k psi_(kd)(x)` is generally order one for every fixed `k`.  The
full resummed series, not the quadratic truncation, controls positivity.
In the OU high-spatial scale it resums to the real Bargmann/heat transform
`B_mu(y)`, whose strict positivity is automatic for a genuine positive law.
Thus the calculation cannot be promoted to a genuine all-order
counterexample.

The inherited fixed-degree Hankel cap from R137 is also insufficient by
itself: if `|epsilon|^2` is bounded by a constant times
`binom(d,(d-1)/2)^(-1)`, then
`A_d/binom(d,(d-1)/2)=O(d^(1/4)(3/4)^d)`.  The inverse growth is therefore
compatible with shrinking amplitudes.  A uniform moving-degree estimate is
still missing.

## 4. OU interface and remaining open bridge

For a density `h=dmu/dgamma`,

`(P_lambda h)(y/sqrt(lambda)) -> B_mu(y)`

under the square-exponential domination used in the project.  This is the
all-order resummation mechanism that can absorb the finite quadratic tail.
Ordinary real positivity yields only `B_mu(y)>0`; it does not yield the
stronger positive-definite/Hankel coherence needed for rigidity.

The exact nonlinear equation remains

`F_z(nu)+3 Q_z^nu(sigma)=1/(1+2z)` for every `z>0`, `|sigma|<=nu`.

The unique next target is a quantitative moving-degree statement: either a
tail-stable negative Hankel/Bochner minor with explicit cutoff and norm, or
a rigorous diagonal-resummation no-go showing why every such margin can be
evaded.  No genuine non-Gaussian full-SF law has been constructed here.

## 5. Local audit scope

`audit_r149.py` checks:

1. central-trinomial recurrence and exact Hermite source profiles;
2. the even inverse coefficient and its asymptotic scaling;
3. the quadratic-tail discriminant boundary and sample ratios;
4. the finite signed-measure quadratic form and OU Möbius profile on explicit
   finite measures;
5. Gaussian-quadrature agreement for the pure odd Hermite source.

The final status is therefore: R149 adds a concrete all-`z` nonlinear
compensation package and a sharp finite-order positivity obstruction, while
the all-order positive-cone classification and the publication claim remain
open.
