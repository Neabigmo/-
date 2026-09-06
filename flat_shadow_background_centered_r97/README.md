# R97 — background-centered exact factorization and finite-horizon substitute

Date: 2026-09-07.

This record isolates the part of the background-centered route that is
unconditional at finite Hermite horizon. It does not claim a uniform
gap-Wiener conjugation theorem for the actual `g1`/`g2` background.

## 1. Exact finite LDL recursion

Let `G=G^*` be an `(n+1) x (n+1)` Hermitian matrix with

`G = I + H`, `||H||op <= h < 1`.

The unit lower-triangular `T` and positive diagonal `D` are obtained without
determinants by

`d_i = G_ii - sum_(k<i) T_ik d_k conjugate(T_ik)`,

`T_ij = [G_ij - sum_(k<j) T_ik d_k conjugate(T_jk)] / d_j`, `i>j`,

with `T_ii=1`. Induction gives `G=T D T^*`. Put `C=T^{-1}` by

`C_ii=1`,

`C_ij=-sum_(k=j)^(i-1) T_ik C_kj`, `i>j`.

Then the exact background factor is

`C G C^* = D`.

For the `i`-th leading principal block, `d_i` is its Schur complement, or
equivalently `d_i = min_x (x,1)^* G_[0:i] (x,1)`. The sandwich
`(1-h)I <= G <= (1+h)I` therefore gives

`1-h <= d_i <= 1+h`.

Moreover, directly from `C G C^*=D`,

`||C||op^2 <= kappa(h):=(1+h)/(1-h)`,

and the same bound holds for `||C^{-1}||op^2`.

For the formal background
`G_(0,n)(a)=I+a A_n+a^2 B_n^(2)`, the condition

`h_0:=|a|M_1+a^2M_2<1`

is sufficient whenever `||A_n||op<=M_1` and `||B_n^(2)||op<=M_2` uniformly.
It gives `D_(0,n)` and `C_(0,n)` for every finite `n`, with constants
independent of `n`. This is **PROVED** under the stated operator bounds.

## 2. Uniform replacement for the false gap-Wiener claim

Let `E=C_(0,n) H C_(0,n)^*` be the conjugated residual and let `||.||_1`
be the Schatten trace norm. Operator conditioning gives the dimension-free
estimate

`||E||_1 <= kappa(h_0) ||H||_1`.

If `D=D_(0,n)`, define `R=D^(-1/2) E D^(-1/2)`. Then

`||R||_1 <= [(1+h_0)/(1-h_0)^2] ||H||_1 =: beta(h_0)||H||_1`.

Thus a finite horizon `N=n+1` admits the R94 strict-lower contraction whenever

`beta(h_0)||H||_1 <= 1/[64(1+log N)^2]`.

The normalized equation is `(I+L)(I+R)(I+L)^*` diagonal, with
`||L||op <= 2(1+log N)||R||op` and contraction factor `97/1024`. The
original factor is `(I+L)D^(-1/2)C_(0,n)`.

This is a genuine finite-horizon corollary. It trades the unavailable uniform
gap-Wiener residual estimate for a trace-norm residual budget; it is not an
infinite-horizon theorem.

## 3. Strict obstruction at the linearized background level

For `G_n(a)=I+aA_n`, differentiating
`C_n(a)G_n(a)C_n(a)^*=D_n(a)` at `a=0` and taking strict lower entries gives

`C_n'(0)=-L_-A_n`.

R96 proves for the actual `g1` multiplier that
`||L_-A_n||_(W_n) >= c log(n+2)` along the factorial-ratio gap channels.
Hence `sup_n ||C_n'(0)||_(W_n)=infinity`.

Therefore a dimension-free gap-Wiener local Lipschitz estimate for the
background factor, or a proof of background conjugation based on such an
estimate, is impossible already at first order. This is a **PROVED
linearized no-go**, not a claim that every fixed nonzero `a` has unbounded
conjugation norm.

The comparison
`||C_(0,n) H C_(0,n)^*||_(W_n) <= C_bg ||H||_(W_n)` is consequently
**OPEN** for restricted actual residual classes and is not implied by
operator positivity. The exact usable alternatives are the trace-norm
finite-horizon statement above, or the background-relative norm
`||H||_(bg,n):=||C_(0,n)H C_(0,n)^*||_(W_n)`, whose uniform comparison with
the original `W_n` norm remains OPEN.

## 4. Stronger webpage result: relative background Jacobi norm

The correct centered variable can be made exact at each finite horizon. Define

`w_a(x)=1+a g_1(x)+a^2 g_2(x)`,

`S_(0,n)=D_(0,n)^(-1/2)C_(0,n)`, and let `psi_k` be the corresponding
background orthonormal polynomials. Then

`S_(0,n)G_(0,n)S_(0,n)^*=I`,

and for a residual multiplier `h`,

`(S_(0,n) Hcal_n(h) S_(0,n)^*)_(ij)
 = integral [h(x)/w_a(x)] psi_i(x)psi_j(x) d mu_a(x)`.

Only the Gaussian moments through degree `2n` enter this matrix. If
`h^[2n]=sum_(m<=2n) eta_m e_m` and
`r_(a,n)=h^[2n]/w_a`, let `p_(a,n)[h]` be the degree-`2n` orthogonal projection
of `r_(a,n)` in `L^2(mu_a)`. Since `deg(psi_i psi_j)<=2n`, this projection is
exact, not an approximation:

`bar E_n = ( integral p_(a,n)[h] psi_i psi_j d mu_a )_(i,j<=n)`.

Write `p_(a,n)[h](x)=sum_m b_m x^m`. If `J_a` is the background Jacobi
matrix, then it is tridiagonal and, with
`kappa_a=(1+delta_a)/(1-delta_a)`,

`||J_a^[N]||op <= 2 sqrt(kappa_a) sqrt(N+1)`,

because `||x f||_(mu_a)<=sqrt(1+delta_a)||x f||_gamma` and
`||f||_gamma<=(1-delta_a)^(-1/2)||f||_(mu_a)`. Using the degree-locality of
`p(J_a)` through degree `3n`, set

`R_(a,n)=6 sqrt(kappa_a) sqrt(3n+1)`,

`P_(a,n)(h)=sum_m |b_m| R_(a,n)^m`.

The gap algebra then gives the proved finite-horizon estimate

`||bar E_n||_(W_n)<=P_(a,n)(h)`,

and, returning to monic normalization,

`||E_n||_(W_n)<= (1+delta_a) P_(a,n)(h)`.

The centered equation is normalized exactly by
`tilde L_n=D_(0,n)^(-1/2)L_nD_(0,n)^(1/2)` and
`bar E_n=D_(0,n)^(-1/2)E_nD_(0,n)^(-1/2)`. It becomes the R95 equation with
identity background. Hence `P_(a,n)(h)<=1/64` gives the explicit contraction
factor `97/1024`, `||tilde L_n||_(W_n)<=2P_(a,n)(h)`, and
`||L_n||_(W_n)<=2 sqrt(kappa_a)P_(a,n)(h)`.

This yields the fixed-parameter conditional criterion

`delta_a<1` and `sup_n P_(a,n)(h(a))<=1/64`

for all-degree background-centered Gram positivity. It is stronger and more
structural than the trace-norm finite-horizon substitute above. The remaining
issue is proving this relative polynomial cost is uniformly invariant under
the actual same-factor map.

## 5. Stronger g2 growing-gap theorem

Let `N e_k=k e_k` be the Gaussian number operator. The exact commutators are

`[N,M_g]=M_(Ng)-2M_(g') partial`,

`ad_N^2(M_g)=M_(N^2g)-2M_((Ng)')partial-2M_(N(g'))partial
              +4M_(g'')partial^2+2M_(g')partial`.

Since the Hermite basis diagonalizes `N`,

`d^2 Delta_d Hcal_n(g)=Delta_d P_n ad_N^2(M_g)P_n`.

For `g=g_2`, the R80 four-term block and its endpoint geometry imply a finite
constant `C_(2,g2)` for the displayed differential combination; this uses the
same `alpha^(-3)` endpoint majorant and the exact cancellation of the
`q_tau^3` factor, not a fixed lower bound on `alpha`. Therefore

`||Delta_d B_n^(2)||op <= min{ M_2, C_(2,g2)(n+1)/d^2 }` for `d != 0`.

Summing the two signs of each gap and using
`sum_(d>=1) min(A,B/d^2)<=A+2 sqrt(A B)` gives

`||B_n^(2)||_(W_n) <= 3M_2+4 sqrt(M_2 C_(2,g2)(n+1))`

and hence `O(sqrt(n))`. For every fixed `delta>0`, the proportional-gap tail
is uniformly bounded:

`sum_(|d|>=delta(n+1)) ||Delta_d B_n^(2)||op <=4 C_(2,g2)/delta`.

The unresolved window is now precisely sublinear, especially
`1<<d<=O(sqrt(n))`. A bounded absolute gap sum would follow from a uniform
two-parameter envelope such as

`||Delta_d B_n^(2)||op <= F(d/sqrt(n),d)` with `sup_n sum_d F<infinity`,

or from `C(1+d)^(-1-epsilon)`. The endpoint estimate alone does not prove this.

## 6. Updated hybrid transfer

For the unit odd `Z_j` mode in the R92/R93 coordinates, let `h^(j)` be its
Gaussian polynomial representer and define the relative background Gram cost

`Gamma_(a,n,j)=P_(a,n)(h^(j))`,

`v_(a,n,j)=w_j+Gamma_(a,n,j)`.

The `w_j` column bound from R92/R93 is PROVED. The new mixed Gram condition is

`C_Gamma(a)=sup_(n,j) Gamma_(a,n,j)^(-1)
             sum_k Gamma_(a,n,k)|K_(k,j)^(n)| < infinity`.

If it holds, then the combined weighted column norm is bounded by
`max(C_w,C_Gamma(a))`; the `Gamma` feedback is the only new linear obstruction.
Full nonlinear hybrid invariance remains OPEN.

## 7. Status boundary

**PROVED:** determinant-free finite LDL recursion; uniform diagonal and
operator conditioning bounds; trace-norm conjugation inequality; exact
relative background polynomial/Jacobi reduction; explicit centered contraction
constant; the actual `g1` linearized gap-Wiener no-go via R96; and the `g2`
second-commutator growing-gap estimate with `O(sqrt(n))` total bound.

**CONDITIONAL:** applying the relative-background criterion to the full actual
same-factor branch requires uniform control of `P_(a,n)(h(a))`; applying the
trace-norm finite-horizon corollary requires a trace-norm residual bound.

**OPEN:** comparison of the relative polynomial norm with the original
gap-Wiener norm; the `g2` mesoscopic gap sum; hybrid `Gamma` feedback and full
nonlinear invariance; global positivity; positive backward towers; backward OU
divisibility; and `FS_3`.

Audit command:

```text
F:/anaconda3/python.exe flat_shadow_background_centered_r97/audit_r97.py
```
