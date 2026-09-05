# R37 exact audit — two-body Laguerre–Hoeffding Gaussian anchor

R36 ruled out an ordinary remote one-body Laguerre carrier because both its
Gaussian anchor and fixed-head sensitivity lose an exponential `(2/3)^n`
factor.  R37 tests the next genuinely different sector: the degenerate
two-body Hoeffding projection.

Use independent standard Gaussian coordinates `U,Y,Z` for the common and
residual directions.  For the two observed iid coordinates, set
`S=(X1+X2)/sqrt(2)` and `D=(X1-X2)/sqrt(2)`.  Conditioning the residual radial
variable `T=(Y^2+Z^2)/2` on `(X1,X2)` leaves one Gaussian residual direction
with variance `2/3`, and gives the exact generating function

`sum_n E[L_n(T)|X1,X2] z^n`
`= (1-z)^(-1/2)(1-z/3)^(-1/2)`
`  * exp(-z D^2/(2(1-z))-z S^2/(6(1-z/3)))`.

Equivalently,

`p_n(X1,X2)=sum_{a+b=n} 3^(-b)
  L_a^(-1/2)(D^2/2)L_b^(-1/2)(S^2/2)`.

With `w_j=binom(2j,j)/4^j`, the exact Gaussian pair-projection norm is

`||p_n||^2 = sum_{b=0}^n 9^(-b) w_(n-b)w_b`,

whose generating function is
`((1-z)(1-z/9))^(-1/2)`.  The one-body subtraction has norm
`||k_n||^2=binom(2n,n)/9^n`, so the degenerate two-body norm is

`B_n^gamma=||h_(2,n)^gamma||^2
          =sum_{b=0}^n 9^(-b)w_(n-b)w_b
           -2(4/9)^n w_n`.

The singularity at `z=1` gives
`B_n^gamma ~ (3/(2sqrt(2))) w_n ~ 3/(2sqrt(2 pi n))`.  Thus the pair
anchor still tends to zero, but only polynomially; the one-body exponential
loss is genuinely absent.  This makes the pair sector a real carrier window,
not a relabeling of the R36 no-go.

The derivative of `B_n` with respect to the first Hermite head and the
constraint-coupled sign mechanism are deliberately not claimed here.  They
are the web-side R37 target and must be reviewed before drawing a
transgression conclusion.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_hoeffding_transgression_r37\audit_r37.py
```

Expected markers:

```text
R37_TWO_BODY_CONDITIONAL_PROJECTION PASSED
R37_TWO_BODY_DEGENERATE_NORM PASSED
R37_TWO_BODY_ANCHOR_POLYNOMIAL_DECAY PASSED
R37_TWO_BODY_HEAD_SENSITIVITY REQUIRES WEB_REVIEW
R37_CONSTRAINT_COUPLED_TRANSGRESSION REMAINS OPEN
R37_AUDIT_COMPLETED
```
