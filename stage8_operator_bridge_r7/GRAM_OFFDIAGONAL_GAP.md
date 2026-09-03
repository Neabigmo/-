# Gram positivity and its exact limitation

For a nonnegative density ratio `f`, let
`G_mn=int f h_m h_n dgamma`.  Every finite principal block is PSD,
`G e_0=b`, and the Stage-8 coefficient is
`S_n=<Psi_n, G tensor G tensor G (e_0 tensor e_0 tensor e_0)>`.

The strongest automatic consequence is

`|S_n|^2 <= <Psi_n,G^tensor3 Psi_n>`

because `<e_0^tensor3,G^tensor3 e_0^tensor3>=1`.  The right-hand side is
`E[h_n(L_theta)^2]`.  This is diagonal energy control, not a sign condition.

The exact 2-by-2 PSD matrix `[[1,-1/2],[-1/2,1]]` gives a negative mixed
matrix element against `e_0` while remaining PSD.  Its three-fold tensor gives
the same countermodel for the Stage-8-shaped matrix element.  The model is
only an operator countermodel: it does not obey the Fock equation or target
law.
