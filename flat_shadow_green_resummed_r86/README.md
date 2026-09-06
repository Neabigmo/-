# R86 — exact Green-resummed generating identity and endpoint correction

Date: 2026-09-07.

R86's first step is now locally closed at the exact finite level.  The
`(s,g)` convolution in the mixed kernel can be folded into one source
generating series and the exact signed-Green operator:

`R_m(z) = sum_(s>=1) R_(m+s,m) z^s`,

`S_j(z) = sum_(r>=1) M_(j+r+1,j) z^(r+1) R_(j+r+1)(z)`,

and, as a formal series (finite after taking any fixed coefficient),

`K_j(z) = e^(-z) S_j(z)
 - 2 z e^(-2z) integral_0^1 e^(zu) u^j S_j(zu) du`.

Consequently `[z^d]K_j(z)=K_(j+d,j)`.  The local audit verifies this
identity against the exact finite kernel for several exact rational finite
blocks.  This is the correct starting point for any contour argument: the
signed `s/g` convolution is no longer represented as two independently
approximated sums.

## Corrected saddle bookkeeping

For `r/j -> alpha`, `s/j -> beta`, `d/j -> delta`, write `z=j*zeta` and
`gamma=delta-alpha-beta`.  The first Green term has the formal action

`Phi_1 = Phi_A(alpha) + alpha + beta
 - alpha log(alpha) - beta log(beta)
 + (alpha+beta-delta) Log(zeta) - zeta`.

Its stationary equations are

`beta=zeta`,
`zeta=alpha+beta-delta`,

so they force `alpha=delta` and `gamma=-beta`.  The angular action must
include the external root-filter phase `2 alpha Log(omega)` when a full
complex branch is used; omitting it changes the phase and is not harmless
for a lower bound.

For the second Green term, with `L=1+alpha+beta`, the action is

`Phi_2 = Phi_A(alpha) + alpha + beta
 - alpha log(alpha) - beta log(beta)
 + (alpha+beta-delta) Log(zeta)
 + L Log(u) - 2 zeta + zeta*u`.

The joint stationary equations give

`zeta=-gamma/(2-u)=-L/u`,
`u_* = 2L/(L+gamma)`.

The endpoint `u=1` meets the interior saddle at `gamma=L`, exactly the
Green transition already visible in R85.

## Endpoint factor correction

When the `u=1` endpoint is the valid branch, endpoint Laplace expansion of
the exact integral gives

`integral_0^1 e^(zu) u^(Lj) du
 ~ e^z/[j(zeta+L)]`.

Therefore the two Green pieces have combined prefactor

`P_G = 1 - 2 zeta/(L+zeta) = (L-zeta)/(L+zeta)`.

At the formal PSC saddle `alpha=delta`, `beta=zeta`, so
`L=1+delta+zeta` and

`P_G^PSC = (1+delta)/(1+delta+2 zeta)`.

The inverse factor would be an algebraic error.  The audit records this
correction explicitly; it does not claim that the endpoint contour is
legally dominant for the complex PSC saddle.

## What R86 does and does not prove

The exact generating identity and the corrected stationary equations are
unconditional finite/formal identities.  The contour deformation, complex
source endpoint continuation, Green endpoint dominance, and conjugate
angular phase control remain unproved.  Hence the candidate rate

`delta*(1-log(delta)) + Phi_A(delta)`

remains conditional.  A safe fallback is a uniform all-gap upper bound for
the rescaled coefficient kernel, but that requires uniform factorial-ratio
estimates beyond this exact identity.

The exact checks are in `audit_r86.py`; no determinant, optimizer, scan, or
numerical surrogate is used.
