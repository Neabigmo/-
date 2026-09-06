# R94 — finite-horizon nonlinear Gram stability

Date: 2026-09-07

This record audits the R94 continuation of the hybrid route.  It keeps the
weighted coefficient Volterra theorem and the Gram--Schmidt problem separate.

## 1. Abstract coefficient theorem, with the explicit finite-section constant

Let `X=ell^1(w)`, `w_j>0`, and let

`(Kx)_k=sum_(j<k)K_(k,j)x_j`,

with `C_K=sup_j w_j^(-1) sum_(k>j)w_k|K_(k,j)| < infinity` and
`kappa_j -> 0`.  For `P_J` onto the first `J` coordinates, set
`epsilon_J=sup_(j>=J)kappa_j`.  Then

`||KQ_J||=epsilon_J`, `Q_J=I-P_J`,

and strict degree raising gives

`K=[[K_H,0],[C,K_T]]`,

with `K_H^J=0`, `||K_T||<=epsilon_J`, and `||C||<=C_K`.  If
`|lambda|epsilon_J<=1/2`, define

`S_J(lambda,C_K)=sum_(q=0)^(J-1)(|lambda|C_K)^q`.

The block inverse and the weighted direct-sum norm give the explicit bound

`sup_n ||(I-lambda P_n K P_n)^(-1)||`

`<= max(2,(1+2|lambda|C_K)S_J(lambda,C_K))`.

This applies to the formal R81 mixed linearized coefficient loop only.  It does
not apply to the nonlinear Gram map or to positivity.

## 2. Nonlinear Gram--Schmidt contraction theorem

Fix `N>=2`, let `Lambda_N=1+log N`, and let `H=H^*` be an `N` by `N` Hermitian
Gram perturbation.  On strict lower-triangular matrices with the operator norm,
define

`Phi_H(L)=-L_-[H+LH+HL^*+LL^*+LHL^*]`.

If

`h=||H|| <= 1/(64 Lambda_N^2)`

and `r=2 Lambda_N h`, then `Phi_H` maps the closed ball `||L||<=r` into itself
and is a contraction there.  The exact estimates are

`||Phi_H(L)|| <= Lambda_N[h(1+r)^2+r^2]`,

and, for `||L||,||M||<=r`,

`||Phi_H(L)-Phi_H(M)||`
`<=2 Lambda_N[h+r(1+h)]||L-M||`
`<= (97/1024)||L-M||`.

Indeed `r<=1/32`, `r^2/h<=1/16`, and
`(1+r)^2+r^2/h <=1153/1024<2`.  Banach's theorem therefore gives a unique
strict lower solution

`L=Phi_H(L)`, `||L||<=2(1+log N)||H||`.

Because `H=H^*` and `h<1`, `G=I+H` is positive.  With `C=I+L`, the fixed-point
equation is exactly `L_-(CGC^*)=0`.  Since `CGC^*` is Hermitian, it is diagonal;
since `C` is invertible, the diagonal is positive.  Moreover

`(1-r)^2(1-h)I <= CGC^* <= (1+r)^2(1+h)I`.

Thus this is a genuine finite-horizon nonlinear Gram factorization theorem, not
only a linearized resolvent statement.  The Hermitian hypothesis is necessary for
the positivity/diagonalization conclusion and is made explicit here.

## 3. Sharp dimension-free obstruction

The theorem is not uniform in `N` under a generic operator norm.  Let
`A_(jk)=1/(j-k)` for `j!=k`, and `H=iA`.  Then `H=H^*` and the finite discrete
Hilbert transform keeps `||H||` bounded, while the strict lower part applied to
a normalized constant vector has norm at least `c log N`.  Hence the derivative
of the Cholesky solution map at zero satisfies

`D Psi_N(0)[H]=-L_-H`, `||D Psi_N(0)|| >= c log N`.

There cannot be an `N`-independent local Lipschitz constant on a fixed operator
norm ball.  The `Lambda_N^(-2)` hypothesis is therefore a rigorous sufficient
finite-horizon scale, not an asserted optimal scale.  Positivity of `LL^*` alone
cannot remove the logarithm.

The next meaningful target is a structured estimate for actual Hermite Gram
compressions, for example

`||L_- H_n(h)||_op <= C[||H_n(h)||_op+||h||_(ell^1(w))]`,

with `C` independent of `n`.  This is **CONDITIONAL/OPEN**; it cannot be inferred
from arbitrary-matrix operator theory.

## 4. Overall route status

**PROVED and locally audited:** R92 all-gap rescaled coefficient column;
`kappa_j->0`; compact/quasinilpotent formal mixed kernel and fixed-parameter
finite-section resolvent; the generic `1+log N` triangular upper; and the
finite-horizon nonlinear Gram theorem above.

**OPEN:** a dimension-free structured Hermite triangular bound; a full nonlinear
hybrid implicit-function theorem at fixed nonzero parameter; global positivity;
positive infinite backward towers; backward OU divisibility; and `FS_3`.

Audit:

```text
node flat_shadow_nonlinear_gram_r94/audit_r94.js
```
