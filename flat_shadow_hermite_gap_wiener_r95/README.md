# R95 — Hermite gap-Wiener algebra and the actual triangular obstruction

Date: 2026-09-07.

R95 attacks the structural gap left by R94: the strict lower-triangular
projection is logarithmically large on arbitrary operator-norm matrices, but
the matrices arising from Gaussian Hermite multiplication have an exact
degree-gap decomposition.  The result is a dimension-free theorem on a
precisely stated growing-radius coefficient class, together with an actual
Hermite-multiplier counterexample showing that boundedness alone is not
enough.

## 1. Exact normalized Hermite matrix

Use probabilists' Hermites

`e_k=H_k/sqrt(k!)`, `V_n=span(e_0,...,e_n)`, and
`Hcal_n(h)=P_(V_n) M_h P_(V_n)`.  If
`eta_m=L_h[e_m]` (or `eta_m=<h,e_m>_gamma` for a multiplier representer),
then

`Hcal_n(h)_(ij)=sum_(r=0)^(min(i,j))
 r! binom(i,r)binom(j,r)
 sqrt((i+j-2r)!/(i!j!)) eta_(i+j-2r)`.

Equivalently, with `m=i+j-2r`,

`Hcal_n(h)_(ij)=sum eta_m sqrt(i!j!m!)
 /[r!(i-r)!(j-r)!]`,

where the sum is over
`|i-j|<=m<=i+j` and `m=i+j (mod 2)`.  Thus a degree-`m` Hermite
mode only occupies the gaps
`-m,-m+2,...,m-2,m` (at most `m+1` diagonals; all occur when `n>=m`).

The bivariate generating identity is exact:

`sum_(i,j>=0) Hcal(h)_(ij) z^i/sqrt(i!) w^j/sqrt(j!)
 = exp(zw) F_h(z+w)`,

where
`F_h(z)=sum_m eta_m z^m/sqrt(m!)`.

For the tangent, `F_(g1)=U` and the already audited R71/R79 formula gives

`eta_(2r)^(1)=0`,
`eta_(2r+1)^(1)=(-1)^(r-1) r(r+1)!/[2 sqrt((2r+1)!)]` for `r>=1`.

The R80 multiplier `g2` is even and bounded, so `Hcal_n(g2)` occupies only
even gaps.  The centered decomposition remains

`G_n=I+a Hcal_n(g1)+a^2 Hcal_n(g2)+Hcal_n(Ehat+o)`.

## 2. The gap-Wiener algebra

For a finite matrix define the exact gap extraction

`Delta_d A=(2pi)^(-1) integral exp(-id theta)
 D_theta A D_theta^* dtheta`,

with `D_theta=diag(1,e^(itheta),...,e^(intheta))`.  It keeps exactly the
entries with `i-j=d`.  Define

`||A||_(W_n)=sum_(d=-n)^n ||Delta_d A||_op`.

Fourier extraction and gap bookkeeping give

`Delta_d(AB)=sum_r Delta_r(A)Delta_(d-r)(B)`,
`||AB||_(W_n)<=||A||_(W_n)||B||_(W_n)`,
`||A^*||_(W_n)=||A||_(W_n)`,
and
`||L_- A||_(W_n)<=||A||_(W_n)`.

Therefore `||L_-A||_op<=||A||_(W_n)` with no logarithmic loss.  This is an
algebraic identity, not an arbitrary-matrix operator-norm estimate.

## 3. Dimension-free structured theorem

Let `T_(m,n)=Hcal_n(e_m)`.  The R77 degree-local estimate, already audited
locally, is

`||T_(m,n)||_op <= 2^m(3n)^(m/2)/sqrt(m!)`.

For `rho_n=4 sqrt(n)` and

`||h||_(rho_n)=sum_(m=0)^(2n) |eta_m| rho_n^m/sqrt(m!)`,

`q=sqrt(3)/2` gives

`||Hcal_n(h)||_(W_n)
 <= sum_m |eta_m| rho_n^m/sqrt(m!) (m+1)q^m
 <= (189/64)||h||_(rho_n)`.

The last constant is sharp for this scalar majorant: the maximum of
`(m+1)(sqrt(3)/2)^m` is attained at `m=6` and equals `189/64`.

Keeping only positive gaps gives the sharper triangular estimate

`||L_- Hcal_n(h)||_op <= (27 sqrt(3)/32)||h||_(rho_n)
 < (3/2)||h||_(rho_n)`.

Both constants are independent of `n`.  This is **PROVED relative to the
already audited R77 degree-local multiplication estimate** and the exact
finite gap algebra above; it is not a claim about every bounded multiplier.

## 4. Uniform nonlinear Gram theorem in the structured norm

For Hermitian `H`, put `h_W=||H||_(W_n)` and define the R94 map

`Phi_H(L)=-L_-[H+LH+HL^*+LL^*+LHL^*]`.

If `h_W<=1/64`, take `r=2h_W`.  Submultiplicativity and the contractivity of
`L_-` give

`||Phi_H(L)||_W <= h_W(1+r)^2+r^2`,

and on the radius-`r` ball

`||Phi_H(L)-Phi_H(M)||_W
 <=2[h_W+r(1+h_W)]||L-M||_W
 <=97/1024 ||L-M||_W`.

Thus Banach's theorem gives a unique strict-lower `L` with
`||L||_W<=2||H||_W`.  Since `||H||_op<=h_W<1` and `||L||_op<=1/32`,

`(I+L)(I+H)(I+L)^*`

is a positive diagonal matrix.  This is a genuine horizon-uniform nonlinear
Gram factorization on the gap-Wiener small ball.

In particular, the R77 coefficient condition
`||h||_(rho_n)<=1/189` implies `||Hcal_n(h)||_(W_n)<=1/64` and hence gives
the uniform structured factorization for that residual block.

## 5. Actual obstruction: bounded multiplier is not enough

Take the actual bounded odd multiplier `h(x)=sgn(x)`.  Then
`||Hcal_n(h)||_op<=1`, but a half-line Green identity for the OU generator
gives, for `i=2p+1`, `j=2q`,

`Hcal_n(sgn)_(2p+1,2q)
 =2 gamma(0) sqrt(2p+1)e_(2p)(0)e_(2q)(0)
 /[2(p-q)+1]`,

where
`e_(2r)(0)=(-1)^r sqrt((2r)!)/(2^r r!)`.

Using the central-binomial lower bound gives, for `p>=q>=1`,

`|Hcal_n(sgn)_(2p+1,2q)|
 >=1/[sqrt(pi)(2(p-q)+1)]`.

Choosing a normalized input supported on even indices `2q`, `Q<=q<=2Q`,
with signs `(-1)^q`, and taking `3Q/2<=p<=2Q`, makes all contributing terms
have the same sign.  For `4Q+1<=n`, the output norm is bounded below by a
constant times `log Q`.  The generic R94 Fourier upper gives the matching
`O(log n)`, so

`||L_- Hcal_n(sgn)||_op=Theta(log n)`.

This is an actual Hermite multiplication matrix, not the earlier abstract
Hilbert witness.  Odd parity alone therefore does not remove the obstruction.

## 6. Route status and the exact remaining bridge

**PROVED:** exact Hermite matrix formula; exact bivariate identity; gap-Wiener
algebra; dimension-free structured residual estimate; dimension-free nonlinear
Gram factorization on the stated `rho_n` ball; and the `sgn(x)` bounded-class
`Theta(log n)` obstruction.

**CONDITIONAL:** applying the structured theorem to the full branch if the
background matrices satisfy
`sup_n||Hcal_n(g1)||_(W_n)<infinity` and
`sup_n||Hcal_n(g2)||_(W_n)<infinity`.

**OPEN:** those two concrete gap-Wiener bounds; uniform invariance of the
combined coefficient-plus-Gram hybrid norm; fixed nonzero-parameter global
positivity; a positive infinite backward tower; backward OU divisibility; and
`FS_3`.

The key global update is now precise: coefficient propagation is out of the
linear mixed-kernel bottleneck, and generic Gram logarithms can be removed on
a real structured algebra.  The remaining project-specific task is not “prove
a generic triangular bound”, but prove or refute the two Gaussian-mixture
background bounds for `g1` and `g2`.

Audit command:

`node flat_shadow_hermite_gap_wiener_r95/audit_r95.js`
