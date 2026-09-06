# R78 — Same-radius factorial even bootstrap

R78 attacks the post-R77 bottleneck: close the same-factor even equation in a
single coefficient Wiener norm instead of converting from `rho_n` to
`sigma_n=2 rho_n`. The browser connector again reported an account-connection
error and did not read the local R77 files; the statement below was extracted
from the completed response and checked locally against R77.

## 1. Conditional same-factor coefficient lemma

Write the Gaussian-normalized Hermite series as

    f(z)=E(z)+Y(z)=sum_(m>=1) f_m z^m,
    f_m=L[e_m]/sqrt(m!).

Assume the exact same-factor angular identity has, at degree `2k`, the form

    A_(2k) E_(2k) + Q_(2k)(f,f) + C_(2k)(f,f,f) = 0,

where

    A_(2k)=3 binom(2k,k)/6^k,

and the angular quadratic/cubic coefficients obey the absolute moment bounds

    |C_(r,s)+C_(s,r)| <= 2 A_(2k),
    |D_(r,s,t)| <= A_(2k),

for `r+s=2k` and `r+s+t=2k`. These coefficient inequalities are the
explicit same-factor input; they are not consequences of arbitrary forcing.

Then, since the factor `A_(2k)` is present in the actual nonlinear source,

    |E_(2k)| <= sum_(r+s=2k)|f_r f_s|
                 + sum_(r+s+t=2k)|f_r f_s f_t|.

The inverse `A_(2k)^(-1)`, whose arbitrary-source size is
`asymp sqrt(k)(3/2)^k`, therefore does not enter this exact source majorant.

## 2. Same-radius Wiener closure

For fixed truncation `n`, set `R_n=4 sqrt(n)` and

    ||g||_n=sum_(m<=2n+1)|g_m| R_n^m.

This is a coefficient Wiener norm, so ordinary convolution is
submultiplicative. The coefficient lemma gives the conditional even estimate

    ||E||_n <= ||f||_n^2 + ||f||_n^3,
    f=E+Y.

Thus the same-factor angular solver has no separate `(3/2)^n` inverse loss and
no `rho_n -> sigma_n` factor `4^n`. The statement is local and finite; it does
not assert a bound for arbitrary even sources.

## 3. Combining with R77 and the signed odd transfer

R77 applies whenever the top norm satisfies
`||E||_n+||Y||_n<=1/40`, because `rho_k=4 sqrt(k)<=R_n` for `k<=n`.
For any fixed `mu>3`, put `lambda=mu+1` and use the R76 signed transfer:

    |Z_tilde_k| <= D_mu lambda^k/k! Xi,
    D_mu <= [2 mu/(mu-1)] C_mu.

The odd coefficient in the same Hermite coefficient norm is

    |o_(2k+1)| <= D_mu Xi k! lambda^k/(2k+1)!.

Summing directly at `R_n`, without a second radius, gives

    ||o||_n <= Gamma_(n,mu) Xi,
    Gamma_(n,mu)=K_mu n^(-1/2)[16 e(mu+1)]^n,
    K_mu=256 mu C_mu/[31(mu-1)].

The elementary bound uses
`k!/(2k+1)!<=1/(k+1)!` and the fact that the final term dominates the finite
sum when `lambda>4`.

## 4. Local bootstrap and explicit window

Let `H_n` be the same-norm size of the audited R64 tangent. The exact tangent
coefficient gives

    H_n <= (8/3) n^(3/2) 16^n.

With `x=|a|H_n`, the bootstrap

    ||Y||_n<=2x,  ||E||_n<=8x^2,  x<=1/100

is self-consistent for the even map. The R77 source factor satisfies
`Xi<=36x^3`; hence the odd improvement closes if
`36 Gamma_(n,mu) x^2<=1`.

A conservative local no-reversal scale is therefore

    a_(n,mu)# = H_n^(-1) min{1/100, [36 Gamma_(n,mu)]^(-1/2)},
    t_(n,mu)# = (a_(n,mu)#)^2.

For sufficiently large `n`, using the tangent and `Gamma` bounds yields the
explicit sufficient forms

    a_(n,mu)# >=
      [16 sqrt(K_mu)]^(-1) n^(-5/4)
      [64 sqrt(e(mu+1))]^(-n),

    t_(n,mu)# >=
      [256 K_mu]^(-1) n^(-5/2)
      [4096 e(mu+1)]^(-n).

These are conditional local finite-hierarchy scales. They are far below
`A_(2n)~3(2/3)^n/sqrt(pi n)`; the remaining loss comes from the size of the
Gaussian tangent in the growing `4 sqrt(n)` Gram norm (`H_n` carries `16^n`)
and the signed Green evaluation at that radius, not from an extra even
angular inverse or a common-radius conversion.

## 5. Precise boundary and next target

R78 does not prove D.1, an infinite positive backward tower, or backward OU
divisibility. It also does not prove that the local Gram ball can be centered
at the large background `aU`. The next target is the tangent-centered
Gram/source bootstrap: write the Gram matrix as

    G_n(a)=I+a A_n+R_n(a),

with `sup_n ||A_n||<infinity`, and impose the smallness condition only on
`(E,o)` while treating `aU` as an exact background. This is the route that may
remove the tangent `16^n` penalty; it remains OPEN.

