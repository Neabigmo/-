# R89 — source factorization, moving-saddle obstruction, and conditional absolute majorant

Date: 2026-09-07.

R89 tested whether the R88 fixed-saddle endpoint lemma can be applied to the
fully resummed source.  The useful outcome is a clean factorization and a
structural diagnostic: a fixed endpoint normalization is not uniformly mild
over the entire real `u` interval even in the leading `z*exp(z)` model.  This
does not disprove PSC; it says that any successful PSC proof must localize the
source saddle or use an absolute majorant.

## 1. Exact source factorization

For `ell=m+s`, define the non-divisive normalized band factor

`Xi_(m,s) := p_(m+s,m) / T_(m,s)`,

where

`T_(m,s)=2*(s-1)!*binom(m+s+1,s-1)*binom(m+s-3,s-1)`.

Then direct factorial simplification of the exact source formula gives

`R_(m+s,m) = -4 * (2m)!/((m+2)!(m-2)!)`
`                * (m+s+1)/((m+s)(m+s-1)(m+s-2))`
`                * Xi_(m,s)/(s-1)!`.

This is an exact finite identity for `m>=2`, `s>=1`.  On the real
proportional source band, R85's endpoint calculation says
`Xi_(m,s)->(1-lambda)/(1+lambda)^3`, `lambda=s/(m+s)`.

If one instead names `Theta=T/Xi`, then the same identity contains
`1/Theta`; this convention is the source of the inverse-looking forms in
some R89 displays.  The audit uses `Xi` so no division by a possibly zero
finite coefficient is needed.

## 2. Poisson-type generating identity

Let

`C_m=4*(2m)!/((m+2)!(m-2)!)`,

`D_(m,s)=(m+s+1)/((m+s)(m+s-1)(m+s-2))`, and
`R_m(z)=sum_(s>=1)R_(m+s,m)z^s`.  Formally,

`R_m(z)=-C_m*z*exp(z)*E[D_(m,N+1)*Xi_(m,N+1)]`,

where `N` is Poisson with parameter `z`; equivalently this is just the
coefficient identity
`z*exp(z)*E[f(N+1)]=z*sum_(n>=0)f(n+1)z^n/n!`.

This is a formal/finite coefficient identity, not a claim that the complex
Poisson representation already supplies a uniform asymptotic.

## 3. Corrected angular reality check

Set `y=omega*x` and `q=exp(-i*pi/6)`, `y=q*v`.  The angular saddle equation
becomes

`v^2 - sqrt(3)*(2*rho-1)*v + 1=0`, `rho=alpha/(1+alpha)`.

For real `alpha>=0`, `|sqrt(3)*(2*rho-1)|<=sqrt(3)<2`, so the two roots are
on the unit circle.  The branch through `x(0)=1` has
`arg(y)` in `[0,2*pi/3]` and never meets `y=-1`.

The substitution into the already audited PSC formula must be done carefully:

`zeta=4*alpha*x/(omega^2*(1+omega*x)^2)`
`     =4*alpha*y/(1+y)^2`
`     =alpha/cos(arg(y)/2)^2 > 0` for `alpha>0`.

The reciprocal `4*alpha*(1+y)^2/y` appearing in one R89 passage is an
algebraic inversion and is rejected.  Positivity survives the correction, but
the quantitative range and later estimates must use the displayed formula.

## 4. Fixed-saddle leading-model no-go

The natural fixed normalization for a source factor at `z=j*zeta` is

`A_src(u)=u^(-(alpha+zeta)j)*R_m(j*zeta*u)/R_m(j*zeta)`.

In the leading model `R_m(z) proportional to z*exp(z)`,

`A_src^(0)(u)=u^(1-(alpha+zeta)j)*exp(j*zeta*(u-1))`.

For real `zeta>0` and fixed `0<u<1`,

`log|A_src^(0)(u)|
 =j*[zeta*(u-1-log(u))-alpha*log(u)]+log(u)`.

The bracket is strictly positive.  Thus the global `C^1`/sup bound required
by R88 cannot hold for this frozen normalization even in the leading model.
This is a no-go for the proposed global fixed-amplitude application, not a
no-go for PSC.  A viable contour proof must use a moving source saddle or a
boundary-layer/remote-region decomposition.

## 5. Conditional absolute source and kernel majorants

Suppose the actual band factor satisfies, for `1<=s<=epsilon*m`,

`|Xi_(m,s)| <= C_Xi*exp(C_Xi*s^2/m)`.

Since `D_(m,s)<=9/m^2` for `m>=2`, the exact factorization gives the
conditional source estimate

`|R_(m+s,m)| <= C_epsilon*4^m*m^(-5/2)*(1+s)/s!`
`                       *exp(C_Xi*s^2/m)`.

Combining this with the R87 angular target

`|M_(j+r+1,j)| <= C*4^(-j-r)*j^(-1/2)*(1+r)^2/r!`

and the Green majorant `|G|<=C_epsilon/g!`, for `D=r+s+g`, yields the
conditional mesoscopic bound

`|K_(j+D+1,j)| <= C_epsilon*j^(-3)*(1+D)^3*3^D/D!`
`                            *exp(C_epsilon*D^2/j)`.

The three powers of `(1+D)` are explicit: two from angular and one from
`1/(s-1)!=s/s!`.  This is a target conditional on the source, angular, and
Green inequalities; it is not yet an actual all-gap theorem.

## 6. Rescaled weight ratio

For `c_j=(j!)^2/(2j+1)!` and `tilde omega_(n,j)=n^(-j)omega_(n,j)`, the exact
ratio is

`tilde omega_(n,j+D)/tilde omega_(n,j)
 =16^D*c_(j+D)/c_j`
` =16^D*prod_(h=1)^D(j+h)^2 / prod_(h=1)^(2D)(2j+h)`.

Hence

`tilde omega_(n,j+D)/tilde omega_(n,j)
 <=4^D*exp(D*(D+1)/j)`.

The weighted conditional kernel target is therefore

`|K_(j+D+1,j)|*tilde omega_(n,j+D+1)/tilde omega_(n,j)`
` <= C*j^(-3)*(1+D)^3*12^D/D!*exp(C*D^2/j)`

up to the harmless one-gap indexing convention.  Factorial absorption starts
at `D` of logarithmic order, but the hard source/angle estimates remain.

## Status boundary

Closed in this round:

- exact source factorization using `Xi=p/T`;
- formal Poisson coefficient identity;
- corrected real-branch positivity of `zeta`;
- leading-model obstruction to a global frozen-saddle amplitude bound;
- exact weight-ratio product and the conditional `(1+D)^3` convolution arithmetic.

Still open:

- a uniform bound on the actual `Xi_(m,s)` in the mesoscopic range;
- the R87 angular bound and uniform Green bound in the same range;
- moving-saddle/endpoint-layer PSC analysis and `z`-contour legality;
- actual proportional lower/equality and all hybrid Gram/triangular, positivity,
  backward-tower, OU-divisibility, and `FS_3` conclusions.

The audit is exact symbolic or finite rational algebra.  It uses no scan,
determinant, optimizer, or remote computation.
