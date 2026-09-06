# R75 — Moving-radius conjugation, with sign-corrected Volterra Green function

R75's moving-radius factorization is a useful structural lemma, but its first
Volterra equation had the wrong sign. The exact Jacobi recursion from R73 is

    eta_(2k+1)=factor_k [alpha_k gamma_k-sum_(m<=2k)c_(k,m)eta_m],

and the Gaussian lower-degree coefficients `c_(k,2j+1)` are positive. Thus the
signed conjugated variable satisfies a *minus* Volterra recursion. The plus
recursion and its `log(2)` pole are valid only for an absolute-value majorant;
they are not the actual Gaussian odd Green spectrum.

## 1. Moving-radius factorization that survives the correction

For arbitrary positive radii `sigma_k`, define

    v_k=(k!)^2 sigma_k^(2k+1)/(2k+1)!,
    Z_k=eta_(2k+1) sqrt((2k+1)!)/(k!)^2.

The weighted transfer from level `j` to level `k` factors exactly as

    K_(k,j)^mov=(v_k/v_j) q_(k,j),
    q_(k,j)=1/(k-j)! * (1+2(k-j)/(j+1)).

The radii disappear from `Z_k`. This remains valid for `sigma_k=8sqrt(k)` or
any other positive moving-radius choice.

## 2. Correct signed Volterra equation

Let `S_k` denote the signed source after the current odd coordinate is removed.
For the Gaussian linearized recurrence, `q_(k,j)>0` but the exact equation is

    Z_k=S_k-sum_(j<k)q_(k,j)Z_j.

Writing `Z(x)=sum Z_k x^k`, `S(x)=sum S_k x^k`, and
`F(x)=integral_0^x Z(t)dt`, the exact equation is

    Z=S-(exp(x)-1)Z-2 exp(x) F,

or equivalently

    Z+2F=exp(-x)S,
    F'(x)+2F(x)=exp(-x)S(x).

Therefore the signed Green function is explicitly

    F(x)=exp(-2x) integral_0^x exp(t)S(t)dt,
    Z(x)=exp(-x)S(x)
          -2 exp(-2x) integral_0^x exp(t)S(t)dt.

It is entire whenever `S` is entire. There is no denominator `2-exp(x)` and no
universal `log(2)` singularity in the exact signed Gaussian Green function.

For the absolute-value sequence, one may replace the minus sign by a plus sign
to obtain a worst-case majorant. That majorant does have the formal denominator
`2-exp(x)` and threshold `1/log(2)`, but this is a loss caused by discarding the
alternating signs. It cannot be used as a lower bound or as a genuine resonance
obstruction for the canonical branch.

## 3. Low-order sign audit and tangent consistency

For the canonical head, the Gaussian tangent has

    z_m=(-1)^(m-1) m(m+1)/(2 m!),   m>=1,

where `z_m` is the signed conjugated odd coefficient. Its finite head source is
`S(x)=x+x^2/2`, and the sign-corrected Volterra equation reproduces
`z_1=1`, `z_2=-3/2`, `z_3=1`, `z_4=-5/12`, ... . This agrees with the audited
R64 tangent signs. The plus equation would contradict these coefficients.

## 4. What R75 actually proves

The unconditional algebraic milestone is the exact moving-radius conjugation
and the sign-corrected entire signed Green formula. The original claim that the
actual Gaussian Green problem has sharp spectral base `(log 2)^(-1)` is rejected
as a sign error; `(log 2)^(-1)` is only the absolute-majorant threshold.

This correction does not yet prove a nonlinear odd tame estimate. The nonlinear
source contains Gram-inverse and even-feedback terms, and one must preserve its
sign/structure rather than apply the positive majorant. The common-radius even
conversion also still costs `4^n`, so no angular-comparable `t_n` follows yet.

D.1, a positive infinite exact backward tower, and backward OU divisibility remain
OPEN. The next target is the sign-preserving canonical nonlinear source identity:
derive the source in the corrected Green equation and determine whether its
contribution is controlled by exact cancellation, a finite-rank identity, or a
quantitative remainder.

