# R65 — finite quadratic-response sums and corrected local-cutoff lemma

R65 turns the R64 conditional response mechanism into explicit finite sums and
checks them at targeted exact stages.  It also corrects a reciprocal error in
the webpage's proposed local-slope cutoff lemma.

## Exact finite sums

For odd `r,s>=3` with `r+s=2n`, define

`E_(r,s)=sum_p [0<=n-p<=s and 2p-r=0 mod 3]
          binom(r,p)binom(s,n-p)`.

The exact three-angle pair average is

`C_(r,s)=3(3E_(r,s)-binom(2n,n))/(2*6^n)`.

Equivalently, with `omega=exp(2*pi*i/3)`,

`E_(r,s)=(1/3) sum_(ell=0)^2 omega^(-ell*r)
          [x^n](1+omega^(2ell)x)^r(1+x)^s`.

The bound

`-1/2 <= C_(r,s)/A_(2n) <= 1`,

where `A_(2n)=3*binom(2n,n)/6^n`, is immediate from `0<=E_(r,s)<=binom(2n,n)`.

Let

`u_(2m+1)=(-1)^(m-1)m(m+1)!/2`,

and set `u_d=0` otherwise.  Under the full same-factor hierarchy, if
`v_(2n)=[a^2]L_a[H_(2n)]`, then

`v_(2n)/(2n)! = -(1/(2*binom(2n,n)))
  sum_(r+s=2n, r,s odd>=3)
  (u_r/r!)(u_s/s!)(3E_(r,s)-binom(2n,n))`.

For the norm curvature, define

`M_(n,k)=sum_(j=0)^(min(n,k)) j! binom(n,j)binom(k,j)u_(n+k-2j)`,

`D_n=sum_(j=0)^n j! binom(n,j)^2 v_(2n-2j)`,

`K_n=D_n-sum_(k=0)^(n-1) M_(n,k)^2/k!`,

and

`Lambda_n=(K_n-nK_(n-1))/(n-1)!`.

The audit checks the response sums and the exact values

`Lambda_10=-1481/21`, `Lambda_15=15335/858`,
`Lambda_20=-42799/19019`, and
`Lambda_30=1063856351/38818159380`,

as well as the exact signs `Lambda_100>0` and `Lambda_200>0`.  These targeted
values are evidence against a naive eventual-negative pattern, not a proof of
eventual positivity or of any asymptotic law.

## Corrected conditional local-slope cutoff lemma

Suppose, on `0<=t<=rho_n`,

`beta_n(t)=n+Lambda_n*t+R_n(t)`, with `Lambda_n<0`,

and for some `0<=eta_n<1`,

`|R_n(t)| <= eta_n*|Lambda_n|*t`.

Then

`n-(1+eta_n)|Lambda_n|t <= beta_n(t)
 <= n-(1-eta_n)|Lambda_n|t`.

If

`T_n=n/((1-eta_n)|Lambda_n|) <= rho_n`,

continuity yields a zero in `(0,T_n]`.  For the first positive zero
`tau_n`, whenever it is defined,

`n/((1+eta_n)|Lambda_n|) <= tau_n
 <= n/((1-eta_n)|Lambda_n|)`.

The webpage had the reciprocal scale `|Lambda_n|/n`; that is incorrect.  The
correct implication for a cutoff tending to zero is a subsequence with
`|Lambda_n|/n -> infinity`, together with a uniform remainder bound whose
radius covers `T_n`.  A derivative bound such as
`|beta_n'(t)-Lambda_n| <= eta|Lambda_n|` on the whole prior window supplies
the additional no-reentry condition.

This lemma is conditional and local.  It does not prove that the present
canonical `Lambda_n` has a favorable asymptotic sign or that the R59–R63
finite cutoffs shrink to zero.

Audit command:

`python flat_shadow_quadratic_response_r65/audit_r65.py`

The audit uses exact rational arithmetic and targeted stages only; no
determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote computation.
