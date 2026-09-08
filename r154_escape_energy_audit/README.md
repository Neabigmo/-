# R154 — Supercritical Escape-Energy / Christoffel Localisation Audit

Date: 2026-09-09  
Status: an exact finite negative-direction criterion has been isolated.  It
reduces the supercritical question to a quantitative polynomial-concentration
problem, but does not by itself prove a negative direction for the original
full-SF completion.

## 1. Exact criterion

Let `Gamma_M` have the R153 density representation

`z^*Gamma_M z=int g_(lambda,M)(x)|p_z(x)|^2 d gamma(x)`,

where `deg p_z<=M` and `||p_z||_(L^2(gamma))=||z||_2`.  For a measurable interval
`I`, define the degree-`M` concentration matrix and its top eigenvalue

`A_M(I)=[int_I psi_m(x)psi_n(x)d gamma(x)]_(m,n=0)^M`,

`Theta_M(I)=lambda_max(A_M(I))`.

Suppose, for some `a,b>0`,

`g_(lambda,M)<=-a` on `I`,   `g_(lambda,M)<=b` on `I^c`.

Then the exact Loewner estimate is

`Gamma_M <= b I_(M+1) -(a+b)A_M(I)`,

and therefore

`lambda_min(Gamma_M)<=b-(a+b)Theta_M(I)`.

Consequently a true negative Gram direction follows if and only if the
available lower bound on `Theta_M(I)` exceeds `b/(a+b)`.  Equivalently, the
localisation leakage `1-Theta_M(I)` must be smaller than `a/(a+b)`.

This is the correct finite statement behind “negative-tail depth versus
Christoffel localisation cost.”  A pointwise negative value of `g` is
insufficient: if `I` is too small, every degree-`M` polynomial can leak too much
mass into the positive complement.

## 2. Local audit

`audit_r154.py` computes `A_M(I)` by Gaussian integration and checks the
criterion in two piecewise-constant signed-density models.  It also checks a
small negative interval for which `g=-1` on `I` and `g=1` elsewhere but the
whole Gram matrix remains positive, explicitly falsifying the pointwise-only
shortcut.

The audit is finite and model-level.  It does not identify a negative interval
for the R137 completed sparse branch, does not establish an asymptotic bound on
`Theta_M(I)` in the moving scaled tail, and does not construct a genuine iid
law.

## 3. R154 research boundary

For a supercritical sequence `M_lambda` with
`tau_lambda=lambda M_lambda -> infinity`, the remaining analytic task is to
find a scaled interval `I_lambda` on which the R153 truncated density has a
negative depth `a_lambda` and a usable complement bound `b_lambda`, then prove

`Theta_(M_lambda)(I_lambda)>b_lambda/(a_lambda+b_lambda)`.

Any theorem must quantify the interval's location and width in the Gaussian
variable, the tail depth, and the Christoffel leakage together.  If only a
pointwise sign or a finite formal jet is obtained, the result remains
`FORMAL/FINITE-ONLY`.

The global publication verdict remains:

`无（目前没有足够独立、完整、可审稿的发表性结果）`

