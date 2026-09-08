# R147 — Dual Laguerre Regression / Positive-Backward Finite-Boundary Blindness

Date: 2026-09-08  
Status: an exact dual-regression theorem, an analytic finite-information
no-go, and an OU reflection-filter interface are recorded.  The genuine
fixed-sample-size chi-square characterization and the full positive backward
tower remain open.

## 0. Scope and evidence boundary

The web-side round read the public R146 commit and performed a global audit of
the project from R132 through R146.  Its strict publication verdict was:

`无（目前没有足够独立、完整、可审稿的发表性结果）`。

This is not a claim that the project contains no proved mathematics.  It means
that the principal implication has not been closed and that the current lemma
packages have not yet been assembled into an independent, novelty-verified
paper theorem.  In particular, the finite-boundary construction below is not a
counterexample to the full-SF law: it matches only finitely many boundary
constraints.

Throughout, let `X_1,X_2,X_3` be iid centered variance-one variables, and put

`C=(X_1+X_2+X_3)/sqrt(3)`,

`U=(X_1-X_2)/sqrt(2)`, `V=(X_1+X_2-2X_3)/sqrt(6)`, and

`Q=U^2+V^2=sum_j X_j^2-(sum_j X_j)^2/3`.

Whenever the exact residual boundary is used, it is explicitly the genuine
full-SF consequence `Q~chi^2_2`, not an assertion derived from the scalar
condition `RK=1`.

## 1. Dual Laguerre regression theorem

Set `T=Q/2` and let `L_m` be the standard Laguerre polynomials for the
`Exp(1)` law.  Under `Q~chi^2_2`, define the common-tilt coefficients

`ell_m(a)=E[exp(aC)L_m(T)]/E exp(aC)`.

Their derivative at the untilted point is

`ell_m'(0)=E[C L_m(T)]`.

Since the Laguerre system is complete in `L^2(Exp(1))`, conditional
expectation gives the exact Parseval identity

`E[E[C|Q]^2]=sum_(m>=1) ell_m'(0)^2`.

Suppose the first non-Gaussian cumulant of the scalar law has odd degree
`d=2s+1`.  The full-SF first-row recursion makes this the relevant first
nonzero degree, and the top coefficient of `L_s(Q/2)` yields

`ell_s'(0)=(-1)^s sqrt(3)/(3^s s!) kappa_(2s+1)`.

Consequently,

`E[E[C|Q]^2] >= 3^(2-d) kappa_d^2/(s!)^2 > 0`.

Thus the following is a rigorous closure theorem under a neighborhood-MGF
and moment-determinacy hypothesis:

`E[C|Q]=0 a.s.  +  Q~chi^2_2  =>  mu=N(0,1)`.

The proof can also be read in two stages.  The identity `E[C|Q]=0` gives
`E[CQ^s]=0` for every `s`; triangular moment expansion then kills all odd
moments, hence the scalar law is symmetric.  The full-SF even recursion then
kills all higher even cumulants.  This dualizes the earlier sufficient
condition `E[Q|C]=2`: the missing full-SF-to-regression implication is now
isolated as `Q~chi^2_2 => E[C|Q]=0`.

## 2. The all-Laguerre reflection cross-spectrum

Let `W_a=exp(aC)/E exp(aC)` and

`r_a(Q)=E[W_a|Q]=1+sum_(m>=1) ell_m(a)L_m(Q/2)`.

Define the reflection cross-spectrum

`J(a)=sum_(m>=1) ell_m(a)ell_m(-a)`

`=E[(r_a(Q)-1)(r_(-a)(Q)-1)]`.

Because `W_a W_(-a)` is constant, conditional Cauchy gives

`r_a(Q)r_(-a)(Q)>=1/(E exp(aC) E exp(-aC))`,

and therefore

`J(a)>=exp(-3[K(a/sqrt(3))+K(-a/sqrt(3))])-1`.

The lower bound is allowed to be negative, so it does not imply reflection
positivity.  Near zero, if `G(Q)=E[C|Q]`, then

`r_a(Q)=1+aG(Q)+O_(L^2)(a^2)`,

and hence

`J(a)=-a^2 E[G(Q)^2]+O(a^4)`.

Every hypothetical non-Gaussian exact full-SF law therefore has a negative
small-`a` dip in `J`.  A proof of `J(a)>=0` would itself be a Gaussian
rigidity certificate, but ordinary conditional Cauchy is too weak to supply
it.  This identifies reflection positivity as a rigidity statement rather
than a generic consequence of positivity.

## 3. Genuine iid positive backward finite-boundary blindness

Fix `q in (0,1)`, finitely many distinct positive values
`z_1,...,z_m`, and `epsilon_0>0`.  The web-side analytic construction gives
strictly positive centered variance-one densities `h` and `g=P_q h` such
that

`||g-1||_(L^2(gamma))<epsilon_0`,

`E exp(-z_j Q)=1/(1+2z_j)` for every `j`, while simultaneously

`kappa_3(g)!=0`,

`ell_1^g(a)ell_1^g(-a)<0` for small nonzero `a`, and

`<log g, psi_3>_gamma !=0`.

Here the three variables are genuinely iid with law `g dgamma`, and the
backward preimage is positive.  Consequently, no finite collection of
global Laplace boundary samples, even with strict positivity, one-step
backward divisibility, arbitrary near-Gaussian closeness, and a nonzero
spatial cubic charge, can force the reflection sign or the spatial charge to
vanish.

This is a finite-information no-go theorem, not a full-SF counterexample:
the construction does not impose the continuum identity for all `z>=0`.
Its precise conclusion is that continuum/all-row information is
indispensable; finite Taylor, Fock, Laguerre, or finite boundary audits cannot
be promoted to the desired global rigidity statement.

## 4. Analytic construction behind the finite-boundary theorem

For

`F_z(g)=E_(g dgamma)^3 exp(-zQ)`,

the Gaussian first variation is

`D F_z(1)[v]=3 int v(x) A_z(x) dgamma`,

where

`A_z(x)=exp(-b_z x^2)/sqrt((1+2z)(1+2z/3))`,

`b_z=2z/(3+2z)`.

At the bottom of the backward step, self-adjointness changes the response to
`P_q A_z`, another centered Gaussian profile whose exponent is strictly
increasing in `z`.  Thus `1`, `x^2`, and the finitely many `P_q A_(z_j)` are
linearly independent.  Choose even compactly supported correction functions
whose Jacobian against normalization, variance, and the finite boundary
constraints is invertible.  Choose an odd compactly supported `f` with
`<f,x>=0` but `<f,psi_3>!=0`; parity makes its first-order effect on all even
constraints vanish.  The implicit-function theorem supplies even corrections
`y(epsilon)=O(epsilon^2)` so that all finite constraints remain exact, while
positivity persists for small `epsilon`.

The odd perturbation leaves a nonzero third cumulant and produces the negative
reflection product and nonzero spatial cubic charge.  The argument is an
analytic local construction under the stated `C_c^infty`/domination
regularity.  It deliberately stops before claiming a continuum exact-SF
solution.

## 5. OU/tower reflection filter

For `g=P_lambda h`, the exact Laguerre transport law is

`ell_m^g(A)=lambda^m ell_m^h(sqrt(lambda)A)`.

At the common top-scale parameter `A=a/sqrt(lambda)`,

`lambda^(-2) J_g(a/sqrt(lambda))`
`=ell_1^h(a)ell_1^h(-a)+R_lambda(a)`,

with

`|R_lambda(a)|<=lambda^2 sqrt(Xi_h(a)Xi_h(-a))`,

`Xi_h(a)=sum_(m>=1) ell_m^h(a)^2`.

For a moving-top tower `g_N=P_(q^N)h_N`, this becomes

`q^(-2N)J_(g_N)(q^(-N/2)a)`
`=ell_1^(h_N)(a)ell_1^(h_N)(-a)+O_A(q^(2N))`,

under the genuine uniform square-exponential/data-processing bounds already
isolated in R132 and R146.  Therefore a plausible weaker local interface than
full tilted-energy control is

`J_(g_N)(q^(-N/2)a)>=-o(q^(2N))`.

This would exclude an order-`q^(2N)` negative common-mode defect, but it is a
candidate condition only; positivity has not been shown to imply it.

## 6. Relation to the local statement (33)

For the local one-step form `g=P_q h`, positivity, `RK(g)=1`, and
`||g-1||_2<delta_q`, the finite-boundary theorem shows that positivity plus
finite exact samples cannot force the desired reflection sign or
`P_3 K_sp(g)=0`.  A proof of (33) must therefore use one of the genuinely
continuum consequences of the exact scalar condition `RK=1`, the full
`z>=0` Laplace law, or global positive-backward coherence.  R147 does not
decide that implication.

The unique next target is the continuum circular-transform closure

`Q~chi^2_2 + iid scalar factorization  =>?  E[C|Q]=0`.

Equivalently, by Bessel/Laplace completeness, one wants

`E[C J_0(t sqrt(Q))]=0` for every `t>=0`.

Writing

`A(s,t)=(1/(2pi)) int product_j phi(s/sqrt(3)+t r_j(theta)) dtheta`,

the exact full-SF boundary gives only `A(0,t)=exp(-t^2/2)`.  The missing
identity is `partial_s A(0,t)=0` for all `t`.  This is the R148 problem.

## 7. Global audit R132–R147

The web-side classification is:

* R132: exact residual law, tail/OU smoothing, and weak spatial bridge.
* R133: first odd Jacobi packet and finite-row blindness.
* R136: formal even completion.
* R137: fixed sparse-branch Hankel feasibility radius tending to zero.
* R138: zero-divisor/root-limsup and compatible infinite-tower zero-free
  rigidity.
* R140: regular-shell positive angular-energy coercivity and witnesses.
* R141: normalized zero-shell OU invariance and raw phase erasure.
* R142: Gaussian-relative form, coherent recovery, and Hermite–Toeplitz
  structure.
* R143: coherent Bessel spectrum and purity.
* R144: iid ridge/bispectrum and balanced wrong-sign obstruction.
* R145: common/residual mixed cumulants and Schur/Appell regression.
* R146: tilted Laguerre/heat transform, positive source, and exact OU scaling.
* R147: dual regression closure, reflection cross-spectrum, and the
  finite-boundary positive-backward blindness theorem.

The strongest article-shaped chain is now

`exact Q law -> tilted Laguerre spectrum -> dual regression E[C|Q]`
`-> reflection sign / Gaussian`.

These are not merely failed numerical attempts: the individual theorem and
lemma packages above are exact under their assumptions.  Nevertheless, the
main characterization, the scalar `RK=1` to full-SF bridge, the continuum
full-SF to dual-regression step, the moving-top uniform tower closure, and the
ordinary-to-spatial `P_3 K_sp` bridge are still open.  The honest publication
answer therefore remains:

`无（目前没有足够独立、完整、可审稿的发表性结果）`。

That answer should be revisited only after R148 either proves the continuum
closure or produces a rigorously verified exact-class obstruction.

## 8. Reproducibility boundary

`audit_r147.py` checks finite polynomial coefficients, the dual Laguerre
normalization, the reflection-filter algebra, the parity/IFT linear interface,
and the OU scaling estimate.  It does not certify the infinite Laguerre
series, the analytic implicit-function construction in all function-space
details, the full-SF law, tower uniformity, or publication novelty.  Those
boundaries are part of the record rather than hidden assumptions.
