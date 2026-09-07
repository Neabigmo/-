# R98 — growing-radius hybrid transfer obstruction at the Gaussian endpoint

Date: 2026-09-07.

This note audits the proposed R97 hybrid cost
`Gamma_(a,n,j)=P_(a,n)(h^(j))`.  It proves that the corresponding weighted
column criterion cannot be uniformly finite down to the Gaussian endpoint
`a=0`.  The obstruction is an actual canonical mixed-kernel channel, not a
generic matrix example.

## 1. Exact Gaussian-endpoint cost

Use the R92/R93 unit-mode normalization

`c_j=(j!)^2/(2j+1)!`, `h^(j)=c_j e_(2j+1)`,

where `e_m=H_m/sqrt(m!)`.  At `a=0`, `mu_a=gamma`, the relative projection is
exactly `p_(0,n)[h^(j)]=h^(j)` whenever `n>=j+1`.  The R97 polynomial cost is

`Gamma_(0,n,j)=c_j A_(2j+1)(R_n)`,
`R_n=6 sqrt(3n+1)`,

where the positive monomial coefficient sum is

`A_m(R)=1/sqrt(m!) * sum_(ell=0)^[floor(m/2)]
         m! R^(m-2ell)/(2^ell ell! (m-2ell)!)`.

For every fixed `j` and `D>=1`, the top monomial is the leading term as
`R->infinity`, so with `k=j+D`,

`Gamma_(0,n,k)/Gamma_(0,n,j)`
`~ (c_k/c_j) sqrt((2j+1)!/(2k+1)!) R_n^(2D)`.

This is an exact finite-polynomial asymptotic, not a numerical scan.

## 2. Actual canonical channel forces divergence

R82 gives the exact finite-degree mixed kernel, independent of the truncation
once the output degree is present.  Its gap-four channel is

`K_(j+4,j)=-(3j^3+146j^2+1001j+1560)`
`/[15(j+1)(j+2)(j+3)^2(j+4)^2]`.

At `j=1`,

`K_(5,1)=-271/3600 != 0`.

Therefore for every `n>=5`, the proposed R97 Gram-transfer constant at
`a=0` obeys

`C_Gamma(0) >= |K_(5,1)| Gamma_(0,n,5)/Gamma_(0,n,1)`.

Since the right side is a positive constant times `R_n^8(1+O(R_n^(-2)))`,

`C_Gamma(0)=infinity`.

More generally, for every fixed `j` with a nonzero canonical channel
`K_(j+D,j)`, the same argument gives divergence like `R_n^(2D)`.

## 3. Meaning for the route

This does not contradict the R92/R93 theorem: their `ell^1(w)` norm uses the
rescaled coefficient radius `n^(-j) omega_(n,j)`, while `P_(a,n)` uses the
growing polynomial radius `R_n`.  Adding the two costs as
`v_(a,n,j)=w_j+Gamma_(a,n,j)` therefore does not repair the mismatch.

The strict conclusion is:

- **PROVED:** `C_Gamma(0)=infinity` for the R97 growing-radius polynomial cost;
  consequently no bound uniform on a parameter neighborhood containing `a=0`
  can use this `C_Gamma` unchanged.
- **OPEN:** whether `C_Gamma(a)` is finite for one fixed nonzero `a` after the
  background projection has generated higher degrees.  Continuity in `a` alone
  cannot settle it because the endpoint is singular in the proposed norm.
- **REPLACEMENT TARGET:** a renormalized mode cost, for example
  `GammaHat_(a,n,j)=R_n^(-(2j+1)) Gamma_(a,n,j)` at the Gaussian endpoint, or an
  intrinsically degree-local background/Jacobi cost whose fixed channel ratios
  do not carry `R_n^(2D)`.  Any replacement must be checked against both the
  R92/R93 `w` columns and the exact centered Gram equation.

This is a small publishable obstruction: it rules out the most immediate
relative-hybrid transfer formulation and sharply identifies the required
renormalization before attempting a nonlinear all-degree closure.

Audit command:

`F:/anaconda3/python.exe flat_shadow_hybrid_transfer_obstruction_r98/audit_r98.py`

