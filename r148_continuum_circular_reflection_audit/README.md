# R148 — Continuum Circular Boundary / Dual Regression / Reflection Deficit

Date: 2026-09-08  
Status: web-side continuum lemma package recorded; finite numerical/algebraic
audit completed separately.  The fixed-sample-size characterization and the
positive backward-tower theorem remain open.

## 0. Evidence boundary

The webpage completed R148 after reading the public R147 commit
`153ffabdadd885625d8fedb6999b9b9e1b945da8` in `Neabigmo/temp`.  Its strict
publication verdict was still:

`无（目前没有足够独立、完整、可审稿的发表性结果）`。

R148 does contain a stronger, coherent analytic/probability lemma package;
the local script below checks only finite identities and numerical interfaces.
It does not certify the infinite-dimensional uniqueness step, the full-SF
characterization, positivity of a nonlinear solution branch, novelty, or the
`RK=1` and spatial `P_3 K_sp` bridges.

Throughout, `X_1,X_2,X_3` are iid centered variance-one variables,

`C=(X_1+X_2+X_3)/sqrt(3)`,

`Q=sum_j(X_j-Xbar)^2=U^2+V^2`.

Whenever `Q~chi^2_2` is used, it is a genuine full-SF/all-row consequence;
it is not derived here from the scalar condition `RK=1`.

## 1. Bessel–Laguerre dual completeness

Set `T=Q/2~Exp(1)` and

`a_m=E[C L_m(T)]`,

where `L_m` is the standard Laguerre basis.  Bessel and Laplace uniqueness,
followed by the Laguerre generating identity, give the equivalent chain

`E[C|Q]=0`
`<=> a_m=0 for every m`
`<=> E[C J_0(t sqrt(Q))]=0 for every t>=0`
`<=> E[C exp(-zQ)]=0 for every z>0`.

The exact transform is

`E[C J_0(t sqrt(Q))]`
`= exp(-t^2/2) sum_(m>=1) a_m (t^2/2)^m/m!`.

The only special-function input is

`int_0^infty exp(-x) L_m(x) J_0(2 sqrt(xy)) dx`
`= exp(-y)y^m/m!`.

This is a genuine continuum reformulation of the missing common-mode
regression, not a finite sampling statement.

## 2. Shifted circular transform

For the residual-plane unit vectors `r_j(theta)` used in the webpage,

`A(s,t)=(1/(2pi)) int product_j phi(s/sqrt(3)+t r_j(theta)) dtheta`

satisfies the exact identity

`A(s,t)=E[exp(i s C) J_0(t sqrt(Q))]`.

The residual law fixes only

`A(0,t)=exp(-t^2/2)`.

The missing dual regression is precisely the normal derivative

`partial_s A(0,t)=i E[C J_0(t sqrt(Q))]=0` for every `t`.

Thus the open step is a genuine Dirichlet-to-normal-derivative problem.  A
Fourier expansion of the circular integral identifies the missing data as a
cubic zero-mode derivative; it does not create that derivative from the
boundary trace.

## 3. Gaussian continuum linearization

For a Gaussian-relative density perturbation `g=1+epsilon f`, define

`F_g(z)=E_(g dgamma)^3 exp(-zQ)`.

The first variation is

`D F_1[f](z)=3 <f,A_z>_gamma`,

`A_z(x)=exp(-b_z x^2)/sqrt((1+2z)(1+2z/3))`,

`b_z=2z/(3+2z)`.

In the normalized Hermite basis `psi_n=He_n/sqrt(n!)`, with
`r=2z/(1+2z)`,

`D F_1[psi_(2m)](z)`
`=3/(1+2z) * sqrt((2m)!)/m! * (-r/3)^m`,

while `D F_1[psi_(2m+1)](z)=0`.

Consequently the full continuum boundary has odd tangent kernel, and the
even inverse has exponentially small multipliers

`3^(1-m) sqrt((2m)!)/m! ~ 3(2/3)^m (pi m)^(-1/4)`.

This is a precise functional-analytic obstruction to upgrading finite IFT
surjectivity to a uniformly controlled continuum right inverse.  It is not a
counterexample to the exact positive full-SF equation.

## 4. Reflection-symmetrization Laplace deficit

Let `check(mu)` be reflection, and write

`nu=(mu+check(mu))/2`, `sigma=(mu-check(mu))/2`.

For `F_z(alpha,beta,gamma)=int exp(-zQ) d alpha d beta d gamma`, parity gives

`F_z(mu,mu,mu)=F_z(nu,nu,nu)+3 F_z(nu,sigma,sigma)`.

For fixed `x_1=a`,

`exp(-zQ(a,x,y))`
`=exp(-2za^2/3) f_a(x)f_a(y) exp((2z/3)xy)`,

and expansion of the last exponential yields

`int int K_(z,a)(x,y) d sigma(x)d sigma(y)`
`=exp(-2za^2/3) sum_n (2z/3)^n/n!`
`* (int x^n f_a(x)d sigma(x))^2 >= 0`.

Under the displayed integrability assumptions, equality at one `z>0` forces
`sigma=0`.  Hence every asymmetric exact full-SF candidate would have to
satisfy the strict deficit

`F_z(nu,nu,nu) < 1/(1+2z)` for every `z>0`.

The reverse inequality is not a consequence of symmetry, scalar positivity,
or one-step positive backward divisibility: OU-smoothed Rademacher laws give
genuine iid scalar witnesses with the opposite local sign, although they do
not satisfy full-SF.

## 5. OU transport and tower interface

For `D_mu(t)=E[C J_0(t sqrt(Q))]` and
`hat(D)_mu(t)=exp(t^2/2)D_mu(t)`, the exact OU transport is

`hat(D)_(P_lambda mu)(t)=sqrt(lambda) hat(D)_mu(sqrt(lambda)t)`.

For `g_N=P_(q^N)h_N`,

`q^(-N/2) hat(D)_(g_N)(q^(-N/2)t)=hat(D)_(h_N)(t)`.

This renormalized continuum shape retains all dual Laguerre modes and is the
right interface for a moving-top escape.  Ordinary bottom `L^2` convergence
does not control this high characteristic scale.

## 6. Global status and exact publication answer

The article-shaped chain is now:

`n=3 chi-square sample variance`
`-> zero-divisor/OU shape`
`-> coherent cross-coherence`
`-> iid bispectrum`
`-> common/residual regression`
`-> tilted Laguerre`
`-> continuum dual transform`
`-> reflection deficit`.

R132, R138, R140–R148 contain genuine theorem/lemma packages under explicit
assumptions.  R133, R136, R141 and R142 retain formal/packet/form-level
boundaries in parts.  The unresolved logical bridges remain:

1. `RK=1 => genuine full-SF/all-row`;
2. `Q~chi^2_2 + iid => E[C|Q]=0`;
3. incompatible positive backward-tower uniform closure;
4. ordinary/Bargmann rigidity `=> P_3 K_sp=0`.

Therefore the honest answer to “do we already have a complete publishable
result?” remains **无**.  The project is no longer merely a collection of
low-order attempts, but the R148 package is not yet an independent,
novelty-checked, closed paper theorem.

The unique next theoretical target is R149: determine whether the exact
nonlinear equation

`F_z(nu)+3 Q_z^nu(sigma)=1/(1+2z)` for every `z>0`, `|sigma|<=nu`,

can prevent odd reflection data from being absorbed by an even positive
correction.  Any claimed closure must use genuine all-order scalar positivity
and backward-cone information, not another finite witness.

