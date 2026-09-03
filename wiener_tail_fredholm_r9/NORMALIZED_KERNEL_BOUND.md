# Normalized kernel bounds

The audit separates two ingredients: a normalized multinomial benchmark,
where `multinomial(n;i,j,k)<=3^n` gives an explicit `a_*^n` bound after the
per-index factor is `a_*/3`, and the central-binomial estimate
`C(2m,m)/4^m >= 1/sqrt(4m)`. With `a_*=sqrt(2/3)`, the benchmark central
coefficient is at least `(1/sqrt(2))a_*^n/sqrt(n+1)`. Importing this into
the actual Stage-7 `A_{ijk}` still requires its exact coefficient formula.

