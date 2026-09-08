# R153 — Full-Section Gauss–Hermite Coercivity Audit

Date: 2026-09-08  
Status: the webpage's coercivity mechanism survives an independent finite
normalisation audit under its stated uniform analytic and real-gap hypotheses;
it is not an unconditional theorem for the original sparse/full-SF branch.

## 0. What is being audited

For a family of ordinary Taylor series

`E_lambda(y)=sum_(k>=0)e_(k,lambda)y^k`,

consider the Hermite-Gram kernel

`K_lambda(u,v)=exp(uv)E_lambda(sqrt(lambda)(u+v))`.

With probabilists' Hermite polynomials `He_k`, normalized basis
`psi_k=He_k/sqrt(k!)`, and standard Gaussian measure `gamma`, define

`g_(lambda,M)(x)=sum_(k=0)^(2M)e_(k,lambda)lambda^(k/2)He_k(x)`.

The key finite identity is

`Gamma_mn = int g_(lambda,M)(x)psi_m(x)psi_n(x)d gamma(x)`

for `0<=m,n<=M`.  The truncation is exact because a term of Hermite degree
`k` contributes only total `u,v` degree at least `k`, while `m+n<=2M`.

For `N=2M+1` Gaussian quadrature nodes and positive weights, the product
`g_(lambda,M)p^2` has degree at most `4M`, below the quadrature exactness degree
`2N-1=4M+1`.  Hence

`z^*Gamma z=sum_j w_j g_(lambda,M)(x_j)|p(x_j)|^2`,

and positivity of the truncated density at all quadrature nodes implies
`Gamma>=0`.  The node bound `|x_j|<2sqrt(N)` gives
`|sqrt(lambda)x_j|<=2sqrt(2tau+1)` when `M=floor(tau/lambda)` and
`lambda<=1`.

## 1. Independent checks

`audit_r153.py` checks:

1. the coefficient normalisation in the exact kernel/density identity by
   comparing coefficient extraction with positive Gauss–Hermite quadrature;
2. the degree count needed for full-section quadrature;
3. the standard Hermite-node envelope `max_j |x_j|<2sqrt(N)` over finite orders;
4. the explicit expansion and recurrence for
   `H_k^(lambda)(y)=lambda^(k/2)He_k(y/sqrt(lambda))`;
5. the compact error estimate used in the webpage's (B.7) and (B.9);
6. the predicted positive-node margin for a concrete entire function positive
   on the real axis; and
7. the algebra behind `R_tau^2/2=4tau+2`, used in the R132 lower bound.

The audit is deliberately finite and numerical/algebraic.  It does not prove
uniform Cauchy bounds for an arbitrary completed sparse branch, does not prove
that `RK=1` implies the all-row class, and does not produce a genuine iid
counterexample or solve the backward-tower rigidity problem.

## 2. Correct theorem level after audit

The defensible R153 statement is conditional:

> If there is a uniform complex-circle bound for `E_lambda` on a circle
> `|z|=S>D_tau`, and a uniform real compact gap
> `inf_lambda inf_|y|<=R_tau E_lambda(y)>=m_tau>0`, then for sufficiently small
> `lambda`, the finite Gram section with `M=floor(tau/lambda)` is coercive;
> in particular, its smallest eigenvalue is at least `m_tau/2`.

For a fixed entire `E` satisfying `E(y)>0` on the relevant compact interval,
this gives a valid model-family corollary.  It does not automatically apply
to the original completed full-SF/sparse branch: the needed uniform complex
bound, positive gap, and existence of a fixed entire shape subsequence remain
to be established there.

## 3. Publication boundary and next target

The global publication verdict remains:

`无（目前没有足够独立、完整、可审稿的发表性结果）`

R153 is a useful conditional coercivity package and closes one proposed
edge/growing-support escape mechanism inside its hypotheses.  The remaining
research target is R154: the genuinely supercritical regime
`tau_lambda=lambda M_lambda -> infinity`, comparing negative generalized-
Hermite tail depth with the Christoffel localisation cost of a degree-`M`
polynomial.  A pointwise negative value of a truncation is not by itself a
negative Gram direction.
