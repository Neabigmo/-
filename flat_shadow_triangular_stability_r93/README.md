# R93 — weighted Volterra stability and Gram triangular loss

Date: 2026-09-07

This record audits the webpage R93 proposal against the already audited R91/R92
coefficient bounds.  It treats two different triangular operators separately:

1. the mixed coefficient kernel `K`, which raises degree; and
2. the Gram--Schmidt projection `L_-`, which is a truncation on matrix entries.

They must not be identified.

## 1. Rescaled coefficient space and column tails

Set

`w_j = 16^j (j!)^2/(2j+1)!`.

The common factor in `n^(-j) omega_(n,j)` is irrelevant, so the rescaled
weighted space is `ell^1(w)`.  For the formal infinite kernel

`(Kx)_k = sum_(j<k) K_(k,j) x_j`,

write

`kappa_j = w_j^(-1) sum_(k>j) w_k |K_(k,j)|`.

R91 proves, for the mesoscopic interval, the bound

`sum_(2<=D<=j/8) |K_(j+D+1,j)| w_(j+D+1)/w_j <= C91 j^(-3)`,

with `C91 = 2405376 exp(12)`.  R92 proves the all-gap absolute majorant.  For
`D >= j/8`, `j>=1`, use `j+D+1 <= 10D`,
`D^2+6D+2 <= 9D^2`, and (for `D>=2`)
`D^2+7D-2 <= 4D^2`.  After the already audited ratio

`w_(j+D+1)/w_j < 4^(D+1)`,

both R92 terms are bounded by

`C92 D^7 16^D/D!`,

where the safe explicit choice is `C92 = 31,008,000`.  Consequently

`kappa_j <= C91 j^(-3) + C92 sum_(D>=j/8) D^7 16^D/D! -> 0`.

The limit is elementary: for `D>=64`, the ratio of consecutive terms is at
most `16/(D+1) * (1+1/D)^7 < 1/2`, so the factorial tail tends to zero.
Finite small `j` do not affect the limit.

## 2. Audited operator theorem

The exact column formula for the weighted `ell^1` operator norm gives

`||K - K P_J|| = sup_(j>=J) kappa_j =: epsilon_J -> 0`,

where `P_J` keeps the first `J` input coordinates.  Since `K P_J` has finite
rank, this proves

`K : ell^1(w) -> ell^1(w)` is compact.

More strongly, degree raising gives the block form for
`X = P_J X + (I-P_J)X`:

```
K = [ K_H   0 ]
    [ C    K_T ],
```

where `K_H` is a `J`-dimensional strict triangular matrix,
`||K_T|| <= epsilon_J`, and `||C|| <= C_K`.  Hence `K_H^J=0`.  For every fixed
`lambda`, choose `J` with `|lambda| epsilon_J <= 1/2`.  Then

`R_T=(I-lambda K_T)^(-1)` exists with `||R_T||<=2`, and

```
(I-lambda K)^(-1)
 = [ R_H                    0 ]
   [ lambda R_T C R_H       R_T ],

R_H = sum_(q=0)^(J-1) lambda^q K_H^q.
```

Thus, for every fixed `lambda`, the resolvents of all finite sections
`K^(n)=P_n K P_n` are uniformly bounded in `n`; the finitely many `n<J` are
absorbed into the constant.  The same block argument shows that
`I-lambda K` is invertible for every finite `lambda`.  Therefore

`sigma(K) = {0}`.

This is a compact, quasinilpotent, Volterra-type conclusion for the mixed
coefficient kernel.  It is not a nonlinear Gram--Schmidt theorem.

## 3. Minimal no-go for the weaker inference

Column boundedness and finite triangularity alone do not give uniform inverse
bounds.  On `ell^1_N`, let `S_N e_j=e_(j+1)`.  Then `||S_N||=1`, `S_N^N=0`,
but

`(I-S_N)^(-1)=I+S_N+...+S_N^(N-1)` and `||(I-S_N)^(-1)||=N`.

The audited extra input in the actual kernel is the vanishing tail
`kappa_j -> 0`, not triangularity by itself.

## 4. Separate Gram--Schmidt statement

For matrices indexed by `0,...,N-1`,

`(L_- H)_(jk) = 1_(j>k) H_(jk)`.

With `D_theta=diag(1,e^(i theta),...,e^((N-1)i theta))` and
`p_N(theta)=sum_(d=1)^(N-1)e^(-id theta)`, coefficient extraction gives the
exact Fourier identity

`L_- H = (2 pi)^(-1) integral p_N(theta) D_theta H D_theta^* dtheta`.

Since conjugation preserves operator norm and
`|p_N(theta)| <= min(N, pi/|theta|)` on `[-pi,pi]`,

`||L_- H||_op <= (1+log N) ||H||_op`.

The matching lower obstruction `||L_-|| >= c log N` is inherited from the R81
discrete Hilbert-matrix witness; the lower calculation uses harmonic sums on a
constant vector.  Hence the generic Gram triangular loss is `Theta(log N)`, not
dimension-free.  If `||H_N||_op <= epsilon_N` and
`(1+log N)epsilon_N < 1`, the linearized inverse satisfies

`||(I+L_- H_N)^(-1)|| <= [1-(1+log N)epsilon_N]^(-1)`.

For exact Cholesky/Gram--Schmidt, with `G=I+H`, `C=I+L`, the strict lower part
of `C G C^*` gives the exact nonlinear identity

`L = -L_-[H+LH+HL^*+LL^*+LHL^*]`.

The audit verifies the signs by direct finite matrix expansion, but does not
claim a nonlinear contraction.

## 5. Overall status

**PROVED and locally audited:** rescaled column vanishing, compactness and
quasinilpotent/resolvent stability of the formal mixed coefficient kernel;
Fourier upper bound for `L_-`; exact nonlinear off-diagonal identity.

**Sharp but inherited:** the `c log N` lower witness for `L_-` from R81.

**Still OPEN:** a uniform nonlinear Gram--Schmidt theorem, global positivity,
positive infinite backward towers, backward OU divisibility, and `FS_3`.

Audit:

```text
node flat_shadow_triangular_stability_r93/audit_r93.js
```
