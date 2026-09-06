# R81 — mixed tangent–residual operator cancellation

Date: 2026-09-07.

The webpage completed R81 but again reported an account-connection error and
said it had not actually read the R80 local files or independently checked
HEAD `7c42885`.  This record keeps that provenance explicit and audits the
response against the locally committed R80 baseline.

## 1. Structural result

Use the quadratic-centered coordinates

`Y=aU+o`, `E=a^2V+Ehat`.

Let

`M_n o := A_e^(-1) Q(U,o)`

be the first-order even response to the odd residual, and let `L_n` denote
the corrected signed-Green derivative of the odd source with respect to
`Ehat`.  At `(Ehat,o)=(0,0)`, the formal same-factor equations give

`D_o Ehat[o] = -2a M_n o`,
`D_Ehat o[Ehat] = a L_n Ehat`.

Eliminating `Ehat` therefore extracts the exact mixed Jacobian

`D_o o_new = -2a^2 K_n`, `K_n=L_n M_n`.

This is an algebraic Schur-complement identity relative to the formal
same-factor/Jacobi hierarchy.  The R80 estimate had replaced the two factors
by separate coarse bounds `||L_n||<=Gamma_n` and `||M_n||<=H_n`; R81 shows
exactly where the product structure was lost.

## 2. Positive result before angular inversion

Suppose `U=T g_1`, `o=T h` with `g_1,h` bounded Gaussian multipliers.  For
`r^2+s^2<=1`, the Wick contraction has the conditional representation

`Gamma_r f diamond Gamma_s g
 = E[f(Y_1)g(Y_2)|X]`,

where `Y_1,Y_2` are standard Gaussian and unconditionally independent, while
their conditional means are `rX,sX`.  The conditional noise covariance is
`-rs`; its covariance matrix is positive exactly when `r^2+s^2<=1`.

Consequently

`||Gamma_r f diamond Gamma_s g||_infinity
 <=||f||_infinity||g||_infinity`.

The three-factor geometry has `r_i^2+r_j^2<=1`, hence every mixed pair is
dimension-free and

`||T^(-1) Q(U,o)||_infinity <=3||g_1||_infinity||h||_infinity`.

Thus the large R80 tangent Wiener norm `H_n` is not created by the `U` leg
itself.  It is created only after angular inversion and triangular source
transport.

## 3. First strict failure boundary: generic angular inversion

On the even Hermite transform mode

`W_k(z)=z^(2k)/sqrt((2k)!)`,

the angular inverse multiplies by

`A_(2k)^(-1)`, `A_(2k)=3*6^(-k)binomial(2k,k)`.

Therefore `||W_k||_(L^2)=1` but

`||A^(-1)W_k||_(L^2)=A_(2k)^(-1)
 ~sqrt(pi k)/3*(3/2)^k`.

So the dimension-free bounded multiplier estimate before inversion cannot be
promoted by abstract operator theory to a uniform bound for `M_n`.  A proof
of `M_n=O(1)` must use the special mixed same-factor image, including its
signs and degree localization.

## 4. Second strict failure boundary: triangular Gram derivative

If `H` is a Gram perturbation, the first variation of the normalized monic
orthogonal polynomial contains the strict lower triangular projection

`D phi_k[H] = -sum_(j<k) H_(jk)e_j`.

The map `L_-:B(l^2) -> B(l^2)` is not dimension-free in operator norm.  For

`H_(jk)=1/(j-k)` for `j!=k`, `H_(jj)=0`,

the full matrix is a finite discrete Hilbert-transform compression and is
uniformly bounded, while for
`v=N^(-1/2)(1,...,1)`,

`(L_-v)_j=H_(j-1)/sqrt(N)`.

Hence

`||L_-H||_op^2 >=N^(-1)sum_(j=2)^N H_(j-1)^2 >=c(log N)^2`.

This proves a genuine no-go: bounded Gram compression alone cannot give an
`n`-uniform derivative for `D_E S`.  The actual mixed image may be a smaller
structured class, but that is an additional theorem, not a consequence of
R80's two bounded background operators.

## 5. Exact weighted criterion

Write corrected odd coordinates as `Z_j`, with

`o_(2j+1)=((j!)^2/(2j+1)!) Z_j`.

In the R80 radius `R_n=4sqrt(n)`, define

`omega_(n,j)=((j!)^2/(2j+1)!) R_n^(2j+1)`.

If `(K_n Z)_k=sum_j K_(k,j)^(n) Z_j`, then the induced weighted `l^1`
operator norm is exactly

`||K_n||=sup_j omega_(n,j)^(-1)
 sum_k omega_(n,k)|K_(k,j)^(n)|`.

Thus the missing input is the explicit column condition

`sup_(n,j) sum_k |K_(k,j)^(n)| omega_(n,k)/omega_(n,j)<infinity`.

For a fixed degree gap `d`,

`omega_(n,j+d)/omega_(n,j)~(4n)^d`

when `j/n` stays in `(0,1]`.  Therefore any fixed-gap channel must satisfy

`K_(j+d,j)^(n)=O(n^(-d))`

unless there is cancellation across degrees.  This is the first decisive
local test for R82.

## 6. Conditional consequence and remaining scale

Define `MGK(C_K)` to be the weighted column condition above.  If it holds,
then `||K_n o||_(R_n)<=C_K||o||_(R_n)` and the mixed linear feedback is
controlled by `2C_K a^2<1`; the old `Gamma_n H_n` factor disappears from
that loop.

This still does not reach the angular natural scale.  The existing quartic
even remainder retains the condition

`Gamma_n a^4 H_n^4<<1`.

With `H_n<=4n^3(4e)^n` and
`Gamma_(n,mu)<=K_mu^(2)n^(-1/2)[16e(mu+1)]^n`, MGK would give the conditional
sufficient scale

`t_(n,mu)# >= c_mu n^(-23/4)
 [64e^2 sqrt(e(mu+1))]^(-n)`.

For fixed `mu downarrow3`, its denominator base tends to
`128e^2 sqrt(e)`, while the R80 base was `256e^2`.  This is a finite but real
improvement, still exponentially below
`A_(2n)~3(2/3)^n/sqrt(pi n)`.

## 7. Status boundary

Verified locally: Schur-complement algebra, the conditional Gaussian Wick
contraction mechanism, angular-inverse mode growth, the triangular-truncation
no-go, weighted norm identity, fixed-gap weight growth, and the conditional
quartic scale arithmetic.

Conditional: `MGK(C_K)`, the full mixed source transport, finite Jacobi branch,
positivity, and the resulting no-reversal window.

Still OPEN: whether the actual mixed kernel satisfies `MGK(C_K)`, whether the
quartic response can itself be centered at operator/factorial level, D.1,
positive infinite exact backward tower, backward OU divisibility, global
positivity, and endpoint `FS_3`.

Audit command:

`python flat_shadow_mixed_kernel_r81/audit_r81.py`

The audit uses exact symbolic identities and fixed checks only.  It uses no
determinants, optimizers, SDP, sweeps, relaxed measure LP, or remote
computation.
