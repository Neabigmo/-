# R92 — global source polynomial bound and all-gap rescaled closure

Date: 2026-09-07.

R91 closed the interval `D<=j/8`.  R92 found a simpler route for the
remaining sector: use the corrected R90 finite `A/B` formulas without a
mesoscopic geometric contraction, and use the exact Green coefficient in two
pieces.  This gives a coarse global source bound but enough factorial decay to
close the entire rescaled coefficient column.

## 1. Global source bound

For `ell=m+s`, the exact corrected R90 terms are

`A_a = (-1)^(a+1)*(a+1)*(a+2)/4`
`  * [a^2+5a-2ell+6] * (ell-a-4)!/(ell-3)!`
`  * (s-1)!/(s-a-1)! * (m+2)!/(m+a+2)! * (m-2)!/(m-a-2)!`,

and

`B_a = (-1)^(a+1)*(a+1)*(a+2)/4`
`  * [a^2+5a-2ell+8] * ell/(ell+1)`
`  * (ell-a-5)!/(ell-3)!`
`  * (s-1)!/(s-a-2)! * (m+2)!/(m+a+2)! * (m-2)!/(m-a-2)!`.

The exact binomial support in the R83 formula forces `a<=m-2` in both groups.
For `m>=3`, the `m`-factor product is at most one.  Pairing the remaining
factorials gives, for `s>=2`,

`(ell-a-4)!/(ell-3)! * (s-1)!/(s-a-1)! <=1/(s-1)`,

and, for `s>=3`,

`(ell-a-5)!/(ell-3)! * (s-1)!/(s-a-2)! <=1/(s-2)`.

Since `a<ell`, the polynomial prefactors are bounded by `ell^2/4` and
`4*ell^2`, respectively.  Thus each nonzero term is at most `ell^4/(s-1)`
or `ell^4/(s-2)`.  Counting at most `s` and `s-1` terms, and handling
`s=1,2` directly, yields the safe global theorem

`|Xi_(m,s)| <=16*(m+s)^4`, `m>=3`, `s>=1`.

The constant 16 is deliberately loose; no asymptotic or numerical scan is
needed.

Combining it with the exact R89 factorization,
`D_(m,s)<=9/m^2`, and
`(2m)!/((m+2)!(m-2)!)<=4^m/sqrt(m)`, gives

`|R_(m+s,m)| <=576*4^m*m^(-5/2)*(m+s)^4*s/s!`.

The reciprocal central-binomial orientation is essential here: the exact R
factorization contains `(2m)!/((m+2)!(m-2)!)`.

## 2. Global Green bound

The exact coefficient is, for `g>=1`,

`G_(ell+g,ell)=(-1)^g/g!`
`  *[1+2g*integral_0^1 t^ell*(2-t)^(g-1)dt]`.

Using only `2-t<=2` gives

`|G_(ell+g,ell)| <=1/g! + 2^g/((ell+1)*(g-1)!)`.

The case `g=0` is `G=1`.

## 3. All-gap kernel bound

Let `D=r+s+g`, `m=j+r+1`, `ell=m+s`, and use the exact R83 convolution.
The source, angular, and global Green bounds give, for `j>=1`, `D>=2`,

`|K_(j+D+1,j)| <= (256/3)*j^(-3)*(j+D+1)^4`
`  *D*(D^2+6D+2)*3^D/D!`
` +18*j^(-3)*(j+D+1)^3`
`  *D*(D-1)*(D^2+7D-2)*4^D/D!`.

The first term comes from the `1/g!` part of Green.  The second comes from
the `2^g/((ell+1)(g-1)!)` part.  The exact identities behind them are

`sum_(r+s+g=D)(r+1)^2*s/(r!*s!*g!)`
` =(3^D/D!)*D*(D^2+6D+2)/27`,

and

`sum_(r+s+g=D)(r+1)^2*s*2^g/(r!*s!*(g-1)!)`
` =(4^D/D!)*D*(D-1)*(D^2+7D-2)/128`.

The actual convolution only uses `r,s>=1`, so extending to all nonnegative
indices is a valid positive majorant.

## 4. All-gap rescaled coefficient propagation

R90 gives the global exact weight inequality
`tilde omega_(n,j+h)/tilde omega_(n,j)<4^h`.  With `h=D+1`, the two terms
above become bases `12^D/D!` and `16^D/D!`, with only polynomial factors in
`j+D+1` and `D`.

For the remaining tail `D>=j/8`, one has `j<=8D` and
`j+D+1<=10D`.  Since `sum_D D^7*16^D/D!` is finite, the weighted tail is
uniformly bounded in `j`.  The R91 interval theorem handles `2<=D<=j/8`
with a stronger `O(j^-3)` bound.  Hence the rescaled coefficient column is
globally bounded:

`sup_(n,j) sum_k |K_(k,j)^(n)|*tilde omega_(n,k)/tilde omega_(n,j) < infinity`,

within the exact mixed-kernel decomposition and its `K_(j+D+1,j)` indexing.

This is a coefficient-propagation theorem, not a PSC lower/equality theorem.

## 5. Status after R92

Now proved:

- a global coarse source bound `|Xi|<=16*(m+s)^4`;
- a global Green bound with `1/g!` and `2^g/((ell+1)(g-1)!)`;
- an all-gap absolute kernel upper with explicit `3^D` and `4^D` pieces;
- global boundedness of the `n^(-j)`-rescaled mixed coefficient column.

The main coefficient-propagation bottleneck is therefore closed.  Remaining
high-level problems are hybrid Gram/strict-triangular stability, the original
unrescaled norm obstruction, PSC lower/equality, global positivity, positive
backward towers, backward OU divisibility, and `FS_3`.

The local audit uses exact BigInt rational algebra and finite-product or
generating-function identities only; it uses no determinant, optimizer, SDP,
scan, or remote computation.
