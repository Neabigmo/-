# R82 — exact degree-local mixed kernel and the first actual obstruction

Date: 2026-09-07.

The webpage completed R82 but reported that the bridge again returned an
account-connection error and did not actually read the R81 local files or
independently verify HEAD `1a3839f`.  The result below is recorded as a formal
same-factor/Jacobi hierarchy result and locally checked at fixed exact
degrees; it is not promoted to an infinite positive-tower theorem.

## 1. Complete finite-degree kernel

Write

`c_j=(j!)^2/(2j+1)!`,
`o_(2j+1)^pow=c_j Z_j`,
`U(z)=sum_(r>=1) upsilon_r z^(2r+1)`,

`upsilon_r=(-1)^(r-1) r(r+1)!/[2(2r+1)!]`.

For

`C_(p,q)=average_theta sum_(i<j) r_i^p r_j^q`,

the first map `o -> A_e^(-1)Q(U,o)` has exact coefficient

`W_(2m)=sum_j M_(m,j)Z_j`,

`M_(m,j)=c_j upsilon_(m-j-1)
 [C_(2m-2j-1,2j+1)+C_(2j+1,2m-2j-1)]/[2A_(2m)]`,

for `m>=j+2`, and zero otherwise.

For an even direction `M`, the Gaussian diagonal variation is

`D_M alpha_l=[M[xH_l^2]-2l M[H_lH_(l-1)]]/l!`.

Along the canonical tangent, the relevant cancellation is

`D_(L_1)D_M alpha_l=2M[P_l]/l!`,
`P_l=H_(l+1)q_l-lH_lq_(l-1)`,

where `q_0=q_1=0`, `q_2=-H_1`, `q_3=-H_0`, and
`q_(l+1)=xq_l-lq_(l-1)`.  If
`P_l=sum_(m<l)p_(l,m)H_(2m)`, then the source kernel is

`R_(l,m)=-2(2m)! p_(l,m)/(l!)^2`.

The corrected signed Green matrix is defined by

`sum_(k>=l)G_(k,l)x^k=e^(-x)x^l
 -2e^(-2x) integral_0^x e^t t^l dt`.

In particular `G_(l,l)=1` and
`G_(l+1,l)=-(1+2/(l+1))`.  The complete finite-degree composite kernel is

`K_(k,j)^(n)=sum_(l=j+3)^k G_(k,l)
 sum_(m=j+2)^(l-1) R_(l,m)M_(m,j)`,

for `k<=n`; the right side itself is independent of `n`, which only truncates
the output.

These formulas preserve every degree index and sign in the chain
`o -> A_e^(-1)Q(U,o) -> D_E S -> signed Green`.

## 2. First channel: gap d=3 survives

The first allowed output is

`K_(j+3,j)=2(j+6)/[3(j+1)(j+2)(j+3)^2]`

and hence

`K_(j+3,j)=2/(3j^3)+O(j^(-4))`.

For `j/n -> theta in (0,1)`,
`n^3 K_(j+3,j) ->2/(3theta^3)`.  Thus the first allowed fixed gap is
compatible with the R81 weighted criterion.

## 3. Actual canonical obstruction: gap d=4

At the next gap, the two source paths and the one-step Green return combine
to

`K_(j+4,j)=-(3j^3+146j^2+1001j+1560)
 /[15(j+1)(j+2)(j+3)^2(j+4)^2]`.

Therefore

`K_(j+4,j)=-1/(5j^3)+O(j^(-4))`.

This is an actual canonical channel, not the arbitrary-matrix triangular
counterexample from R81.  If `j/n -> theta>0`, then

`n^4K_(j+4,j)=-n/(5theta^3)+O(1) ->-infinity`.

For the R81 weights

`omega_(n,j)=((j!)^2/(2j+1)!) (4sqrt(n))^(2j+1)`,

the fixed-gap ratio is asymptotic to `(4n)^d`.  Consequently the single
`d=4` channel contributes

`|K_(j+4,j)| omega_(n,j+4)/omega_(n,j)
 ~256n/(5theta^3)`.

Taking `j=floor(n/2)`, the weighted operator norm is at least
`(2048/5+o(1))n`.  Thus the R81 hypothesis `MGK(C_K)` with an `n`-independent
constant is false for the actual canonical kernel.

## 4. Stronger incompatibility of a single power radius

For a common coefficient-Wiener radius `R_n=c n^alpha`, the actual gap-four
channel scales as

`|K_(j+4,j)| omega_(n,j+4)/omega_(n,j)
 asymp n^(8alpha-3)`.

Uniform mixed-kernel control requires `alpha<=3/8`.  On the other hand, the
fixed degree-four Hermite multiplication identity

`H_4 H_n=...+6n(n-1)H_n+...`

forces a Gram compression lower bound of order `n^2` for a normalized degree-4
multiplier.  A single Wiener estimate would therefore need
`n^2R_n^(-4)=O(1)`, i.e. `alpha>=1/2`.  No single power-radius Wiener norm can
simultaneously provide both dimension-free Gram control and uniform actual
mixed-kernel control.

This is stronger than the R81 arbitrary triangular-projection no-go because
the incompatible exponents come from the canonical `d=4` channel itself.

## 5. What remains possible

R82 does not determine the full all-gap growth.  The `d=4` channel proves only
the lower bound `||K_n||_(omega_n)>=c n`; higher or growing gaps might still
produce polynomial growth, or could reintroduce exponential growth.  If one
can prove `||K_n||=O(n^p)` for a fixed `p`, the mixed linear feedback is still
harmless at the already exponentially shrinking R80 window, even though the
stronger `O(1)` cancellation is false.

Accordingly the next target is not scalar optimization but the all-gap kernel:
derive a gap generating function or a summable polynomial envelope for
`K_(j+d,j)`, retaining signs and factorial ratios.  If a growing-gap family
has an exponential lower bound, the current coefficient norm must be replaced
by a hybrid Gram/triangular operator space.

## 6. Status boundary

Verified locally: the finite kernel construction at fixed degrees, the `d=3`
and `d=4` rational channels, the one-step Green coefficient, the weighted
fixed-gap asymptotic, and the radius-exponent arithmetic.  The all-degree
closed forms are conditional on the formal same-factor/Jacobi hierarchy and
are not a proof of positive realizability.

Strictly disproved: `MGK(C_K)` with `C_K` independent of `n` in the
`R_n=4sqrt(n)` Wiener norm, and more generally simultaneous single-radius
dimension-free Gram plus uniform actual mixed-kernel control.

Still OPEN: the full all-gap growth class (`O(n^p)` versus exponential), a
hybrid norm that handles both Gram and triangular transport, quartic centering,
D.1, positive infinite exact backward tower, backward OU divisibility, global
positivity, and endpoint `FS_3`.

Audit command:

`python flat_shadow_exact_mixed_kernel_r82/audit_r82.py`

The audit uses exact symbolic arithmetic and a few fixed exact degree checks;
it uses no determinants, optimizers, SDP, sweeps, relaxed measure LP, or
remote computation.
