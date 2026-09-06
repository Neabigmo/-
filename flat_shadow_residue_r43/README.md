# R43 local audit — the `m=5` first residue variation

This audit pushes the exact R42 generators through the next smallest open
case, `m=5`. It checks the bivariate block generator against finite Hermite
contractions, checks the raw `dot p_3` generator against direct Gaussian
marginalization, and performs the fixed-order algebraic singular assembly at
the `u=1` singularity. The `u=9` factor and the `(3-z)^(-3)` factor are
exponentially small for fixed `m` and are kept separate from the algebraic
coefficients.

The exact cancelled-chaos coefficients are

```text
q_(5,2) = 33/16
q_(5,4) = 23*sqrt(11)/8
q_(5,6) = 47*sqrt(33)/16
```

The exact-generator singular assembly gives

```text
W_(n,5) + chi_5 D_(n,14)
  = 55*sqrt(231)/(224*sqrt(pi)) n^(11/2)
    -11343*sqrt(231)/(7168*sqrt(pi)) n^(9/2)
    +2266031*sqrt(231)/(2293760*sqrt(pi)) n^(7/2)
    + O(n^(5/2))

D_(n,12)
  = sqrt(462)/(240*sqrt(pi)) n^(11/2)
    -sqrt(462)/(2560*sqrt(pi)) n^(9/2)
    -14917*sqrt(462)/(163840*sqrt(pi)) n^(7/2)
    + O(n^(5/2))

C_(n,5)
  = -57*sqrt(231)/(3584*sqrt(pi)) n^(9/2)
    +6871*sqrt(231)/(114688*sqrt(pi)) n^(7/2)
    + O(n^(5/2))

D_(n,10)
  = 3*sqrt(14)/(40*sqrt(pi)) n^(9/2)
    -9*sqrt(14)/(1280*sqrt(pi)) n^(7/2)
    + O(n^(5/2))
```

With `rho_5=825*sqrt(2)/28`, the `n^(11/2)` term cancels and

```text
R_(n,5)
  = -5703*sqrt(231)/(3584*sqrt(pi)) n^(9/2)
    +3711849*sqrt(231)/(573440*sqrt(pi)) n^(7/2)
    + O(n^(5/2))
```

Dividing by `D_(n,10)` gives

```text
sigma_5 = -9505*sqrt(66)/896
kappa_5 = 18887*sqrt(66)/448 > 0
r_5 = 1
```

This is a fixed-`m` algebraic consequence of exact generators, not a
numerical fit. It remains a residue statement only: it does not prove the
general `m>=6` formula, arbitrary-depth conditioning, positivity of a full
remote construction, or Gaussian rigidity.

An independent genuine finite regression at `(n,m)=(5,5)` is

```text
K_(5,5) = -219200*sqrt(462)/6561
D_(5,10) = 91916*sqrt(7)/2187
D_(5,12) = 46160*sqrt(231)/6561
D_(5,14) = 15400*sqrt(858)/6561
S_(5,5) = -687675*sqrt(66)/160853
```

Expected markers:

```text
R43_BLOCK_GENERATOR_AND_HEAD_FINITE_CHECK PASSED
R43_M5_EXACT_FINITE_REGRESSIONS PASSED
R43_M5_Q_COEFFICIENTS PASSED
R43_M5_BLOCK_AND_C_SECTORS PASSED
R43_M5_RESIDUE_ASYMPTOTIC_ASSEMBLY PASSED
R43_M5_SIGMA_AND_KAPPA PASSED
R43_M5_WEIGHTED_CONDITIONING r5=1 PASSED
R43_GENERAL_M_KAPPA REMAINS OPEN (m>=6)
R43_SINGULAR_EXPANSION_SCOPE: u=1 algebraic terms audited; u=9 terms exponentially small
R43_AUDIT_COMPLETED
```

No optimizer, SDP, numerical sweep, relaxed measure-LP, or remote computation
is used.
