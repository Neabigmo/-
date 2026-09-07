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

## 4. A positive endpoint theorem after renormalization

At `a=0`, define the renormalized mode cost (for `n>=j+1`)

`GammaHat_(0,n,j)=R_n^(-(2j+1)) Gamma_(0,n,j)`.

The positive-coefficient Hermite recurrence

`A_(m+1)(R)=(R A_m(R)+sqrt(m) A_(m-1)(R))/sqrt(m+1)`

and `A_(m-1)/A_m<=sqrt(m)/R` imply, for `k=j+D`, `n>=k+1`,

`A_(2k+1)(R_n)/A_(2j+1)(R_n)`
`<=R_n^(2D)(55/54)^(2D)/sqrt((2j+2)_(2D))`.

Indeed every intermediate degree is at most `2n`, while
`(2n)/R_n^2<1/54`.  Also

`c_(j+D)/c_j=product_(t=1)^D (j+t)^2/[(2j+2t-1)(2j+2t)] <=2^(-D)`.

Consequently, with the explicit constant

`rho_*=(55/54)^2/2=3025/5832<1`,

`GammaHat_(0,n,j+D)/GammaHat_(0,n,j) <=rho_*^D`.

This removes the false `R_n^(2D)` growth from the mode ratio.  Combining it
with the already proved R91 mesoscopic weighted column estimate and the R92
factorial all-gap majorant gives the following interior-column theorem:

`sup_(n>=1,j>=1) sum_(k=j+3)^(n-1)
 |K_(k,j)^(n)| GammaHat_(0,n,k)/GammaHat_(0,n,j) < infinity`.

For `2<=D<=j/8`, use `w_(j+D+1)/w_j>=1` and `rho_*^(D+1)<=1` to dominate by
the R91 bound.  For `D>=j/8`, use `j<=8D`, the R92 terms with bases `3^D/D!`
and `4^D/D!`, and multiply by `rho_*^(D+1)`; the resulting polynomial-times-
factorial series converges by the ratio test.  The first finite head is
handled by the exact R82 channels.  The statement is deliberately restricted
to `n>=k+1`, where the odd mode is present in the `2n` moment projection.

Thus the corrected endpoint picture is two-sided:

- the unrenormalized R97 `Gamma` criterion is **PROVED false** at `a=0`;
- the explicit degree-renormalized `GammaHat` column criterion is **PROVED for
  the interior Gaussian endpoint**, conditional only on the formal R91/R92
  kernel identities already audited;
- transporting this renormalization to fixed nonzero `a`, controlling the
  residual nonlinear map, and treating the horizon boundary remain **OPEN**.

The renormalized cost is not yet a positivity theorem: it repairs the linear
mixed feedback scale, while the centered Gram small-ball estimate and the
positive backward tower still require separate arguments.

## 5. Finite-order commutator barrier for the `g2` mesoscopic gap

There is also a clean limitation on the tempting next step.  Suppose, for a
fixed integer `r>=2`, one can prove the finite-horizon estimate

`||P_n ad_N^r(M_(g2)) P_n||op <= C_r (n+1)^(r/2)`.

The exact number-operator grading then gives

`||Delta_d B_n^(2)||op <= min{M_2, C_r (n+1)^(r/2)/|d|^r}`.

Let `D_*` be the first integer with
`D_*^r >= C_r(n+1)^(r/2)/M_2`.  Since
`sum_(d>D_*)d^(-r)<=D_*^(1-r)/(r-1)`,

`sum_(d>=1) min{M_2,C_r(n+1)^(r/2)/d^r}`
`<= M_2(D_*+1)+C_r(n+1)^(r/2)D_*^(1-r)/(r-1)`.

The two terms have the same scale
`M_2^(1-1/r) C_r^(1/r) (n+1)^(1/2)`.  Thus every fixed-order commutator
route has the same `sqrt(n)` crossover, regardless of `r`.  In particular,
higher commutator decay alone cannot improve R97's `O(sqrt(n))` theorem.

This is a **method barrier**, not a claim that `g2` itself grows like
`sqrt(n)`.  For the R80 endpoint geometry, the constants `C_r` for higher
orders also require fresh endpoint checks and may not be finite.  Either way,
the missing `g2` lemma must exploit a cancellation which is invisible to any
fixed-order `d^(-r)` bound—such as a low-gap subtraction, a finite-difference
identity retaining the four-term block, or a genuinely summable two-parameter
kernel envelope.

Audit command:

`F:/anaconda3/python.exe flat_shadow_hybrid_transfer_obstruction_r98/audit_r98.py`

## 6. An exact nonzero gap-6 anchor for the actual `g2`

The preceding barrier does not determine whether the full `g2` gap-Wiener
norm is bounded, logarithmic, or larger.  There is nevertheless an exact
finite-degree anchor which is useful for checking every proposed cancellation.
From the R71 tangent representation,

`U(z)=z^3 integral_0^1 q_s exp(-q_s z^2)(1-q_s z^2/2) ds`
`=z^3/6+O(z^5)`.

Hence the quadratic source in the R80 equation `A V=-B`,
`B=average_theta sum_(i<j)U(r_i z)U(r_j z)`, has

`[z^6]B=C_(3,3)/36`,
`C_(3,3)=average_theta sum_(i<j)r_i^3r_j^3`.

For `r_j=sqrt(2/3) cos(theta+2 pi(j-1)/3)`, the identities
`sum_j r_j=0`, `sum_j r_j^2=1`, and
`r_1r_2r_3=(2/3)^(3/2) cos(3 theta)/4` give
`C_(3,3)=-7/72`.  Since `A_(6)=5/18`, the first quadratic coefficient is

`[z^6]V=-(C_(3,3)/36)/A_(6)=7/720`.

Because `T g2=V`, its normalized Hermite moment is therefore
`eta_6=sqrt(6!)[z^6]V=7 sqrt(5)/60`.  The exact product identity
`e_6 e_0=e_6` then gives, for every `n>=6`,

`(B_n^(2))_(6,0)=eta_6`,
`||Delta_6 B_n^(2)||op >=7 sqrt(5)/60`.

Hermitian symmetry supplies the opposite gap, so

`||B_n^(2)||_(W_n) >=7 sqrt(5)/30` for `n>=6`.

This is a strict lower anchor for the actual R80 multiplier, not a claim of
growth.  It rules out any proposed argument which annihilates all even gaps;
the unresolved issue remains the summation over the mesoscopic gaps.

More precisely, the entire degree-six boundary corner is explicit.  For
`i+j=6` and `0<=i,j<=6`, degree locality and `eta_0=eta_2=eta_4=0` give

`(B_n^(2))_(i,6-i)=eta_6 sqrt(6!/(i!(6-i)!))
                 =eta_6 sqrt(binomial(6,i))`.

Thus the first boundary entries of gaps `6,4,2,0` have sizes
`eta_6`, `sqrt(6)eta_6`, `sqrt(15)eta_6`, and `sqrt(20)eta_6`, respectively.
This is an exact degree-six corner certificate for the actual multiplier;
it is still only a finite-degree lower bound and leaves the mesoscopic tail
completely open.
