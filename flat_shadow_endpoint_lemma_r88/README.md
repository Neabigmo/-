# R88 — explicit real-`u` endpoint lemma under a uniform amplitude hypothesis

Date: 2026-09-07.

R88 chose the first branch of the R87 decision tree: isolate the real Green
integral and prove its endpoint expansion with an explicit remainder.  The
result below is an unconditional analytic lemma for a prescribed amplitude;
it is not yet an estimate for the actual source series.

## Endpoint lemma

Let `I` be a compact parameter set.  Assume that for every parameter in `I`

`phi(u)=zeta*u+L*Log(u)`, `0<u<=1`,

has `Re(Delta)>=eta>0`, `Re(L)>=ell_0>0`, where `Delta=L+zeta`.  Let
`A_j` be `C^1([0,1])` and suppose

`sup_{j,parameter,u} (|A_j(u)|+|A_j'(u)|)<=M`.

Then

`integral_0^1 exp(j*phi(u)) A_j(u)du`

`= exp(j*zeta) A_j(1)/(j*Delta) + R_j`,

with

`|R_j| <= [M/eta]*(1/c+L_max/c^2) * exp(j*Re(zeta))/j^2`,

where `c=min(eta,ell_0)` and `L_max=sup_I |L|`.

### Proof

Set `B_j(u)=A_j(u)/phi'(u)=A_j(u)u/(zeta*u+L)`.  The denominator obeys

`Re(zeta*u+L)=u*Re(Delta)+(1-u)*Re(L)>=c`,

so

`B_j'(u)=A_j'(u)u/(zeta*u+L)+A_j(u)L/(zeta*u+L)^2`

and

`|B_j'(u)|<=M*(1/c+L_max/c^2)`.

Moreover,

`Re(phi'(u))=Re(Delta)+(1/u-1)Re(L)>=eta`,

so `u=1` is the unique endpoint maximum and

`integral_0^1 exp(j*Re(phi(u)))du <= exp(j*Re(zeta))/(j*eta)`.

Integration by parts gives

`I_j=exp(j*zeta)A_j(1)/(j*Delta)
     -(1/j) integral_0^1 exp(j*phi(u))B_j'(u)du`.

The lower boundary is zero because `Re(L)>0` and `B_j(u)=O(u)` as `u` tends
to zero.  The displayed remainder follows immediately.

## Consequence for the corrected Green factor

If additionally `|A_j(1)|>=m>0`, the additive expansion is relative with
`1+O_I(j^(-1))`.  Substitution into the exact R86 Green operator gives

`e^(-j*zeta)S_j(j*zeta)-2j*zeta*e^(-2j*zeta)I_j`

`=e^(-j*zeta)S_j(j*zeta)
  [1-2*zeta/Delta+O_I(j^(-1))]`,

provided the normalization identifies `A_j(1)` with the corresponding source
amplitude.  Therefore the factor is

`P_G=1-2*zeta/Delta=(L-zeta)/(L+zeta)`.

At the PSC algebraic point `L=1+alpha+zeta`, this becomes
`P_G=(1+alpha)/Delta`.  Combining with the separately conditional source
endpoint factor `P_H=Delta^3/((1+alpha)L^2)` gives the corrected product
`P_H P_G=Delta^2/L^2`.

## Exact status boundary

Closed here:

- the abstract endpoint lemma and its explicit `j^(-2)` remainder;
- real-segment endpoint monotonicity under `Re(Delta),Re(L)>0`;
- the corrected Green prefactor algebra.

Not closed here:

- the actual complex source series has not been shown to produce uniformly
  bounded `A_j` and `A_j'`;
- the lower bound `|A_j(1)|>=m` is not established for that source;
- the `z`-Cauchy contour deformation and angular conjugate phase remain open;
- consequently no proportional lower/equality or full PSC theorem is claimed.

The audit is symbolic and finite; it uses no scan, determinant, optimizer, or
remote computation.
