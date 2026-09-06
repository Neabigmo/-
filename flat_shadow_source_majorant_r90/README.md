# R90 — corrected source-band majorant and audit boundary

Date: 2026-09-07.

The webpage R90 proposed the useful target

`|Xi_(m,s)| < 28`, for `m>=8` and `1<=s<=m/8`,

where `Xi_(m,s)=p_(m+s,m)/T_(m,s)`.  The target is valid after correcting
the displayed factorial orientation.  This round records the correction,
proves the majorant by finite-product inequalities, and keeps the angular and
Green legs explicitly conditional.

## 1. Exact normalization and the correction

Write `ell=m+s` and

`T_(m,s)=2*(s-1)!*C(ell+1,s-1)*C(ell-3,s-1)`.

The exact R83 band formula gives

`Xi_(m,s)=sum_(a=0)^(s-1) A_(m,s,a)-sum_(a=0)^(s-2) B_(m,s,a)`,

with omitted terms understood as zero.  The correctly normalized terms are

`A_(m,s,a) = (-1)^(a+1)*(a+1)*(a+2)/4`
`  * [a^2+5a-2(m+s)+6]`
`  * (m+s-a-4)!/(m+s-3)!`
`  * (s-1)!/(s-a-1)!`
`  * (m+2)!/(m+a+2)!`
`  * (m-2)!/(m-a-2)!`,

and

`B_(m,s,a) = (-1)^(a+1)*(a+1)*(a+2)/4`
`  * [a^2+5a-2(m+s)+8] * (m+s)/(m+s+1)`
`  * (m+s-a-5)!/(m+s-3)!`
`  * (s-1)!/(s-a-2)!`
`  * (m+2)!/(m+a+2)!`
`  * (m-2)!/(m-a-2)!`.

In particular `A_(m,s,0)=1`.  The webpage display had the first two
factorial ratios and both `m`-ratios inverted.  Taken literally, that display gives
`A_(m,s,0)=(m+s-3)^2`, so it cannot be used as a proof.  The local audit
rejects that literal version and verifies the corrected one against the
original finite band formula.

## 2. Uniform source theorem

Assume `m>=8` and `1<=s<=m/8`, and set `q=s/(m-2)`.  Then `q<=1/6`.

For every nonzero `A` term, finite-product comparison gives

`(ell-a-4)!/(ell-3)! <= (m-2)^(-(a+1))`,
`(s-1)!/(s-a-1)! <= s^a`,

and

`(m+2)!/(m+a+2)! * (m-2)!/(m-a-2)! <= 1`.

For the last inequality, write both ratios as products of `a` factors:
each numerator factor is at most `m-2`, while each denominator factor is at
least `m+3`, so every paired ratio is less than one.  Therefore

`|A_(m,s,a)| <= q^a/(m-2) * (a+1)(a+2)/4`
`  * [2*ell + (a+2)(a+3)]`.

Using `2ell/(m-2)<=3`, `m-2>=6`, and
`(a+1)(a+2)<=(a+3)^2`, this yields the explicit bound

`|A_(m,s,a)| <= (a+3)^4*q^a/8`.

Similarly, for every nonzero `B` term,

`(ell-a-5)!/(ell-3)! <= (m-2)^(-(a+2))`,
`(s-1)!/(s-a-2)! <= s^(a+1)`,

while

`(m+2)!/(m+a+2)! * (m-2)!/(m-a-2)! <= 1`.

Together with `|a^2+5a+8|<=(a+4)^2` after the `2ell` part is separated,
the same comparison gives

`|B_(m,s,a)| <= (a+4)^4*q^(a+1)/8`.

The two coefficient inequalities used here are elementary: for `x>=3`,

`x^2/4*(3+x^2/6) <= x^4/8`.

Hence

`|Xi_(m,s)| <= (1/8)*sum_(a>=0)(a+3)^4*q^a`
`             +(1/8)*sum_(a>=0)(a+4)^4*q^(a+1)`
`          <= 681843/25000 < 28`.

This is an actual source-band theorem, not a conditional `exp(C*s^2/m)`
target.  It uses only the exact R83 finite band formula and positive
finite-product comparisons.

## 3. Consequence for the source coefficient

The exact R89 factorization is

`R_(m+s,m)=-4*(2m)!/((m+2)!(m-2)!)`
`  * (m+s+1)/((m+s)(m+s-1)(m+s-2))`
`  * Xi_(m,s)/(s-1)!`.

The middle factor is at most `9/m^2`.  Also

`(2m)!/((m+2)!(m-2)!)`
` = C(2m,m)*m*(m-1)/((m+1)(m+2))`
` <= 4^m/sqrt(m)`.

One elementary proof of the last inequality is to write
`C(2m,m)/4^m=prod_(k=1)^m(2k-1)/(2k)` and use
`(2k-1)^2/(4k^2)<=k/(k+1)` before telescoping.  Thus, on the same band,

`|R_(m+s,m)| <= 1008*4^m*m^(-5/2)/(s-1)!`
`                     =1008*4^m*m^(-5/2)*s/s!`.

The webpage R90 wrote the central-binomial fraction in the opposite
orientation; the inequality above uses the reciprocal that occurs in the
exact R factorization.

## 4. Rescaled-weight correction

For `c_j=(j!)^2/(2j+1)!` and
`tilde omega_(n,j)=n^(-j)*omega_(n,j)`, the correct ratio is

`tilde omega_(n,j+D)/tilde omega_(n,j)=16^D*c_(j+D)/c_j`
` = prod_(h=1)^D 8*(j+h)/(2*(j+h)+1) < 4^D`.

The denominator comes from pairing `(2j+2h)(2j+2h+1)` in the exact
factorial product.  If the convolution variable is `D=r+s+g` but the
output is `K_(j+D+1,j)`, the applied ratio is instead the same formula with
`D+1`; this is the only remaining gap-index convention.

## 5. Status boundary after correction

Closed in this round:

- exact corrected `A/B` normalization against the R83 band formula;
- the source theorem `|Xi_(m,s)|<28` for `m>=8`, `s<=m/8`;
- the explicit source bound with constant `1008`;
- the global exact rescaled-weight bound `<4^D`;
- rejection of the webpage's literal inverted factorial display.

Still conditional/open:

- the R87 angular majorant;
- a uniform Green majorant in the same range;
- their convolution into a full `K` theorem;
- moving-saddle PSC, proportional lower/equality, hybrid stability,
  positivity, backward towers, OU divisibility, and `FS_3`.

The local audit is exact BigInt rational algebra plus the stated infinite
product inequalities.  It uses no determinant, optimizer, SDP, scan, or
remote computation.
