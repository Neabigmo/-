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

## 4. Status boundary

**PROVED:** determinant-free finite LDL recursion; uniform diagonal and
operator conditioning bounds; trace-norm conjugation inequality; explicit
finite-horizon R94 contraction threshold; and the actual `g1` linearized
gap-Wiener no-go via R96.

**CONDITIONAL:** applying the finite-horizon corollary to the full residual
requires a trace-norm bound on the actual residual after the background split.

**OPEN:** uniform background-centered gap-Wiener comparison; the absolute
`g2` gap sum; hybrid `gamma_(n,j)` feedback; global positivity; positive
backward towers; backward OU divisibility; and `FS_3`.

Audit command:

```text
F:/anaconda3/python.exe flat_shadow_background_centered_r97/audit_r97.py
```
