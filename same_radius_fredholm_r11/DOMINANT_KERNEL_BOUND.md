# Dominant and nondominant bounds

The pointwise bound `|A_ijk| <= a_*^n`, `a_*=sqrt(2/3)`, follows immediately
from the angular integral.  For the endpoint normalization,
`A_n00 = a_*^n c_n` with `c_q = E|cos(theta)|^q`.  If `i=2a`, `m=2b`, and
`a >= b`, then

```text
c_i/c_(i+m) = product[t=0..b-1] 2(a+t+1)/(2(a+t)+1)
             <= exp(b/(2a+1)) < exp(1/2) < 2.
```

The logarithmic inequality is termwise `log(1+x) <= x`.  The script checks
this exact product and the resulting numerical inequality over a finite
benchmark range, while the proof statement is the displayed product argument.

For fixed shifts, the diagonal remainder has coefficient `1/(n+1)`, whose
tail supremum is exactly `1/(N+1)`.  For the nondominant region, the replay
uses `sqrt(n+1)*eta^n` with `eta=1/2`; its tail is geometrically decreasing.

