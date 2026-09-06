# R83 — all-gap mixed-kernel growth and fixed-gap generating function

Date: 2026-09-07.

The webpage's R83 response again reported that it could not read the local
R82 files through the bridge.  The result is therefore recorded as a formal
same-factor/Jacobi-hierarchy continuation.  The local audit independently
checks the finite coefficient identities and several fixed gaps with exact
rational arithmetic; it does not promote the formal hierarchy to a positive
backward tower.

## 1. Exact finite building blocks

Keep the R82 notation

`c_j=(j!)^2/(2j+1)!`,

`upsilon_r=(-1)^(r-1)r(r+1)!/[2(2r+1)!]`,

and let `B_(r,j)` be the mixed angular ratio for powers `2r+1` and `2j+1`.
The root-of-unity filter gives the exact finite expression

`B_(r,j)=(R_(r,j)-1)/2`,

where

`R_(r,j)=3 sum_{0<=a<=2r+1, 2r+1-2a=0 mod 3}
 binom(2r+1,a) binom(2j+1,j+r+1-a)
 / binom(2j+2r+2,j+r+1)`.

Thus the mixed angular coefficient is

`M_(j+r+1,j)=c_j upsilon_r B_(r,j)`.

The Gaussian tangent polynomial has an exact Hermite band

`q_l=sum_a Q_(l,a) H_(l-3-2a)`,

with

`Q_(l,a)=(-1)^(a+1)(a+1)(a+2)
 [a^2+5a-2(l-3)](l-a-4)!/[2(l-3-2a)!]`.

For `m=l-s`, the exact finite source band is

`p_(l,l-s)=sum_(a=0)^(s-1) Q_(l,a)(s-a-1)!
 binom(l+1,s-a-1)binom(l-3-2a,s-a-1)`

`- l sum_(a=0)^(s-2) Q_(l-1,a)(s-a-2)!
 binom(l,s-a-2)binom(l-4-2a,s-a-2)`.

Then `R_(l,m)=-2(2m)!p_(l,m)/(l!)^2` and the signed Green coefficient is

`G_(l+g,l)=(-1)^g/g!
 -2 sum_(u=0)^(g-1)(-2)^(g-1-u)/[(g-1-u)!u!(l+u+1)]`.

Together these reproduce the R82 finite kernel

`K_(k,j)=sum_(l=j+3)^k G_(k,l)sum_(m=j+2)^(l-1)R_(l,m)M_(m,j)`.

## 2. Fixed-gap cancellation

For every fixed `r`, the angular coefficient has

`B_(r,j)=-1/(2*4^r)+O_r(j^(-1))`.

For every fixed `s`, the top Hermite band has

`p_(l,l-s)=2l^(2s-2)/(s-1)!+O_s(l^(2s-3))`.

After multiplying the angular and source factors, all powers of `4^j` and
`j^(1/2)` cancel, leaving a common `j^(-3)` leading order.  The leading
source coefficient is

`sigma_(r,s)=2(-1)^(r+1)r(r+1)!/[(2r+1)!(s-1)!]`.

The Green leading kernel is `(-1)^g/g!`.  Its `exp(-z)` factor cancels the
`exp(z)` from summing the source band, giving the fixed-gap formal theorem

`K_(j+d,j)=kappa_d/j^3+O_d(j^(-4))`,

`kappa_d=2(-1)^(d-1)(d-2)(d-1)!/(2d-3)!`, for every fixed `d>=3`.

The gap generating function is

`sum_(d>=3) kappa_d z^d
 =2z^2 sum_(r>=1)(-1)^(r+1)r(r+1)!z^r/(2r+1)!`

`=4 z^(3/2) U(sqrt(z))`.

Equivalently, using the R64 integral representation,

`sum_(d>=3) kappa_d z^d
 =4z^3 integral_0^1 q_s exp(-q_s z)(1-q_s z/2) ds`,

where `q_s=s(1-s)`.  The coefficients are all nonzero and satisfy a
factorial gap decay; in particular `sum_d 4^d|kappa_d|<infinity`.

The audited values recover `kappa_3=2/3` and `kappa_4=-1/5`.

## 3. Consequence for the R82 Wiener weights

For

`omega_(n,j)=((j!)^2/(2j+1)!)(4sqrt(n))^(2j+1)`

and `j/n -> theta in (0,1)`, fixed `d` gives

`omega_(n,j+d)/omega_(n,j)=(4n)^d(1+O_d(n^(-1)))`.

Therefore every fixed gap has the asymptotic weighted channel

`|K_(j+d,j)| omega_(n,j+d)/omega_(n,j)
 =4^d|kappa_d|theta^(-3)n^(d-3)(1+o(1))`.

Since `kappa_d` is nonzero for every fixed `d>=3`, for any fixed polynomial
degree `p` one may choose a fixed `d>p+3` and then take `j=floor(n/2)`.
The resulting single channel grows like a nonzero constant times
`n^(d-3)`, so the current weighted mixed norm is faster than every fixed
polynomial.  This is stronger than the R82 linear lower bound.

This is not an exponential lower bound: the fixed-gap theorem cannot be used
with `d=d(n)` without a uniform remainder estimate.  The proportional-gap
regime `d/j -> delta>0` remains OPEN.

## 4. Norm diagnosis and next route

The current `4sqrt(n)` coefficient-Wiener norm cannot be polynomial-tame for
the mixed loop.  Rescaling the coefficient weights by `n^(-j)` removes the
fixed-gap factor and leaves the summable profile `4^d|kappa_d|`, but that
rescaling cannot by itself provide Gram stability.  The minimal candidate is
a hybrid norm combining Gram compression, strict triangular compression, and
the rescaled coefficient weights.  Uniform boundedness of the full hybrid
kernel is not proved.

The remaining decisive problem is a two-parameter asymptotic: either prove a
uniform moderate-gap estimate such as

`K_(j+d,j)=j^(-3)kappa_d exp(O(d^2/j))`

in a range like `d=o(sqrt(j))`, or obtain a genuine growing-gap saddle-point
lower bound.  Neither conclusion follows from the fixed-gap result alone.

## 5. Verification and boundary

The local audit checks:

- the root-of-unity angular filter against direct angular moments;
- the exact `q_l` Hermite band and the exact `p_(l,l-s)` formula;
- the signed Green coefficient by finite formal-series convolution;
- exact fixed-degree kernels through gaps `d=8` and the displayed `kappa_d`;
- the generating-function identity through its checked Taylor coefficients;
- the logical super-polynomial lower-bound implication.

Command:

`python flat_shadow_all_gap_r83/audit_r83.py`

All checks passed with exact symbolic/rational arithmetic.  The result is
conditional on the formal same-factor/Jacobi hierarchy.  D.1, global
positivity, positive infinite exact backward towers, backward OU divisibility,
endpoint `FS_3`, and the proportional-gap regime remain OPEN.
