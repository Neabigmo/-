# R91 — angular, Green, and mesoscopic full-kernel closure

Date: 2026-09-07.

R90 closed the source leg on `m>=8`, `s<=m/8`.  R91 supplied two elementary
component estimates that fit the same window.  The webpage's central
binomial induction had its ratio written backwards; after correcting that
line, both component estimates are rigorous and the exact convolution gives a
mesoscopic full-kernel theorem.

## 1. Angular coefficient

Use the exact R83/R87 decomposition

`M_(j+r+1,j)=c_j*upsilon_r*B_(r,j)`,

where

`c_j=(j!)^2/(2j+1)!`,
`upsilon_r=(-1)^(r-1)*r*(r+1)!/[2*(2r+1)!]`,

and `B_(r,j)=(rho_(r,j)-1)/2`.  The root-filter expression has
`0<=rho_(r,j)<=3`, because its numerator is a nonnegative subset of the
full binomial convolution and the prefactor is 3.  Hence `|B_(r,j)|<=1`.

The elementary central-binomial estimate needed here is

`C(2k,k)>=4^k/(2*sqrt(k))`, `k>=1`.

For `a_k=4^(-k) C(2k,k)`, the correct ratio is
`a_(k+1)/a_k=(2k+1)/(2k+2)`, not its reciprocal.  The induction step follows
from
`(2k+1)^2-4k(k+1)=1`.

It follows that

`c_j<=4^(-j)*j^(-1/2)`.

Rewriting `upsilon_r` through `C(2r,r)` and using the same estimate gives

`|upsilon_r|<=4^(-r)*(r+1)^2/r!`.

Therefore the actual global angular majorant is

`|M_(j+r+1,j)|<=4^(-j-r)*j^(-1/2)*(r+1)^2/r!`, `j,r>=1`.

No proportional saddle or asymptotic lower bound is used.

## 2. Green coefficient

The exact R83/R86 Green coefficient is

`G_(ell+g,ell)=(-1)^g/g!`
`  * [1+2g*integral_0^1 t^ell*(2-t)^(g-1) dt]` for `g>=1`,

and `G_(ell,ell)=1`.  Since `t(2-t)<=1` on `[0,1]`,
`2-t<=t^(-1)`, so

`integral_0^1 t^ell*(2-t)^(g-1)dt <=1/(ell-g+2)`.

In the common convolution window
`D=r+s+g<=j/8`, with `ell=j+r+s+1`, one has
`ell>=j+3`, `g<=j/8`, and therefore

`2g/(ell-g+2)<2/7`.

Thus the uniform Green bound is

`|G_(ell+g,ell)|<=9/(7*g!)`.

This is a direct exact-coefficient theorem; it does not use the R88
endpoint-amplitude or PSC contour hypotheses.

## 3. Mesoscopic full-kernel theorem

Let `D=r+s+g` and use the exact R83 convolution for
`K_(j+D+1,j)`.  If `j>=16` and `2<=D<=j/8`, every nonempty path has
`m=j+r+1>=8` and `s<=D<=j/8<=m/8`, so the R90 source theorem applies.

The three proven factors give the single-path bound

`|GRM|<=5184*j^(-3)*(r+1)^2*s/(r!*s!*g!)`.

The exact convolution polynomial is obtained from

`sum_r (r+1)^2*x^r/r! = (x^2+3x+1)e^x`,
`sum_s s*x^s/s! = x e^x`.

Consequently

`sum_(r+s+g=D) (r+1)^2*s/(r!*s!*g!)`
` = (3^D/D!)*D*(D^2+6D+2)/27`.

Since the actual path set is a subset of this nonnegative majorant,

`|K_(j+D+1,j)| <= 192*j^(-3)*D*(D^2+6D+2)*3^D/D!`,

for `j>=16`, `2<=D<=j/8`.  This is now PROVED for the exact mixed-kernel
decomposition used in R83, not merely conditional on the earlier schematic
`(1+D)^3` convolution.

## 4. Rescaled weighted column

R90 proved globally that

`tilde omega_(n,j+h)/tilde omega_(n,j)<4^h`.

With `h=D+1`, the mesoscopic theorem gives

`|K_(j+D+1,j)|*tilde omega_(n,j+D+1)/tilde omega_(n,j)`
` <=768*j^(-3)*D*(D^2+6D+2)*12^D/D!`.

The full majorant sums exactly as

`sum_(D>=0) D*(D^2+6D+2)*12^D/D! =3132*e^12`.

Therefore the whole local/mesoscopic rescaled column satisfies

`sum_(2<=D<=j/8) |K_(j+D+1,j)|`
` *tilde omega_(n,j+D+1)/tilde omega_(n,j)`
` <=2405376*e^12*j^(-3)`.

This is the first complete interval-level coefficient-propagation result in
the rescaled norm.  It is not yet a global column theorem: the remaining
large-gap sector `D/j>=1/8` is open.

## 5. Status boundary

Now proved on the stated window:

- source `Xi` and `R` majorants from R90;
- global angular upper bound;
- `9/(7g!)` Green upper bound;
- full exact-kernel bound for `2<=D<=j/8`;
- the corresponding interval-level rescaled weighted column bound.

Still open:

- compact-uniform control for `D/j>=1/8`;
- any proportional lower/equality or PSC conclusion;
- hybrid Gram/strict-triangular stability;
- global positivity, positive backward towers, backward OU divisibility, and
  `FS_3`.

The local audit uses exact BigInt rational algebra and elementary inequalities;
it uses no determinant, optimizer, SDP, scan, or remote computation.
