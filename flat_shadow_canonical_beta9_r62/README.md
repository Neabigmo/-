# R62 — corrected beta9 cutoff

R62 continues the one-parameter canonical family after the corrected R61
window `0<t<tau8`, where `tau8` is the unique zero of `P8` in `(0,1/25)`.
The calculation below is local and exact; it does not identify the Jacobi law
with the original OU density.

## Degree-18 continuation

Let `a=m3`, `t=a^2`, `alpha1=a`, `alpha2=-a`, and `alpha_n=0` for `n>=3`.
Using `alpha8=0` and the degree-18 same-factor row gives

```text
m17 = 2*a*(5799325*t^5 - 17049855*t^4 + 3925920*t^3
           + 13603108*t^2 + 3127296*t - 4435200)/(2-t)^3,

m18 = (2948477*t^6 + 1914655626*t^5 - 11976383460*t^4
        + 24318362039*t^3 - 15915490026*t^2
        - 432574380*t + 275675400)/(2-t)^3.
```

The degree-18 Fock row reduces to

```text
b18 = (42240*sqrt(221)*b11*b7 + 30030*sqrt(238)*b13*b5
       + 37180*sqrt(51)*b15*b3 + 244*sqrt(255255)*b3*b6*b9
       + 120*sqrt(102102)*b5*b6*b7 - 280*sqrt(2431)*b6^3
       + 3139*sqrt(12155)*b9^2)/24310.
```

## Norm and beta9 factorization

Define

```text
Q9(t) = 3165494381056*t^16 + 30325981442862714*t^15
        - 374454388483999229*t^14 + 1980117276228617592*t^13
        - 5948703596679826184*t^12 + 11525374336730958528*t^11
        - 15614218470552621360*t^10 + 14603518104424932288*t^9
        - 6281195243972625024*t^8 - 4538141298321788672*t^7
        + 7271911315244371968*t^6 - 2538108384598913024*t^5
        - 76181770793263104*t^4 - 23999642267549696*t^3
        - 2927350178119680*t^2 + 45013480243200*t
        + 4161798144000.
```

The corrected norm identities are

```text
h8 = -3*P8(t)/(2*(2-t)^3*P6(t)),
h9 =  3*Q9(t)/((2-t)^4*P7(t)),
beta9 = h9/h8 = -2*P6(t)*Q9(t)/((2-t)*P7(t)*P8(t)).
```

At `t=0`, these give `h8=40320`, `h9=362880`, and `beta9=9`, fixing the
orientation `beta9=h9/h8`.

## Exact sign certificate

The Bernstein coefficients of `Q9` on `[0,1/100]` are all strictly positive.
The Bernstein coefficients of `Q9'` on `[1/100,1/25]` are all strictly
negative.  Moreover,

```text
Q9(1/100) > 0,
Q9(19/500) < 0,
P8(19/500) > 0,
P8(1/25) < 0.
```

The R61 Bernstein certificate gives `P8'<0` on `[0,1/25]`.  Hence there are
unique roots

```text
tau9 in (1/100,19/500),    Q9(tau9)=0,
tau8 in (19/500,1/25),     P8(tau8)=0,
```

and therefore `tau9<tau8`.  Numerically only for orientation,
`tau9 ~= 0.0379679226232613`; the exact result is the rational interval and
the monotonicity certificate.

On `0<t<tau8`, the earlier certificates give `P6<0`, `P7>0`, and `P8>0`.
Thus

```text
beta9(t)>0  iff  0<t<tau9,
beta9(t)<0  for tau9<t<tau8.
```

This is the second corrected even-stage contraction after R61: beta7 stays
positive, beta8 cuts to `tau8`, and beta9 cuts again to `tau9`.  It remains a
finite-stage canonical statement, not a proof of the full infinite tail.

## Global status

The partial pattern is now `tau6 > tau8 > tau9 > 0`, with beta7 positive
between the first two cutoffs.  The key open step is an all-even-stage theorem
such as `tau_(2k+2)<tau_(2k)` with limit zero, or another uniform tail
mechanism.  D.1, infinite positive viability, eventual skew annihilation,
Gaussian rigidity, and the `P_3 K` bridge remain distinct open problems.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation was used.
