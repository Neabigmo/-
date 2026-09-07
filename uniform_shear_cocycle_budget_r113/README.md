# R113 — Uniform shear-cocycle budget and the remaining primitive obstruction

Date: 2026-09-07.

R113 is the next local record after `uniform_subgaussian_exact_r112`. The web
side continued from the self-contained R112 data even though the connector did
not expose the local files. The result is a useful theorem-level reduction,
not a solution of the positive backward-tower rigidity problem.

## 1. What R113 adds

Use the R109 four-frequency configuration

`a=phi(s)`, `b=phi(t)`, `c=phi(s+t)`, `d=phi(2s+t)`,

with

`V0=s*t*(s+t)`, `V1=s*(s+t)*(2s+t)`,
`y^2=s^2+(s+t)^2+(2s+t)^2`.

Near the Gaussian point, the common-edge Schur data have the provisional
expansions

`Delta0=((2-m3^2)/4)*V0^2+O(y^8)`,
`Delta1=((2-m3^2)/4)*V1^2+O(y^8)`,
`N=((2-m3^2)/4)*V0*V1+O(y^7)`.

The degree-12 terms in the disk slack cancel. The Gaussian leading slack
reported by the web side is

`S_G = det(H3)/144 * s^6*t^2*(s+t)^4*(2s+t)^2 + O(y^16)`,

where the Gaussian moment Gram determinant is `det(H3)=12`; hence the generic
leading coefficient is `1/12`. This says the Gaussian alignment point is
strictly inside the four-point disk. Consequently, the R109 pointwise disk
does not itself force the shear phase to vanish and supplies no `q,N` gain.

## 2. The phase budget that does follow

Writing `vartheta(u)=arg phi(u)` on the uniform zero-free branch, the local
phase expansion is

`vartheta(u)=-m3*u^3/6+O(u^5)`,

and the shear mismatch is

`eta=vartheta(t)-2*vartheta(s+t)+vartheta(2s+t)`
`   =-m3*s^2*(s+t)+O(y^5)`.

This is only a local diagnostic. The actual uniform estimate comes from R112's
uniform analytic logarithm and exact OU phase transport. If
`tau=q^(N-j)`, then

`vartheta_j(r)=vartheta_bottom(sqrt(tau)*r)`.

With `rho=sqrt(e/128)` and the R111/R112 Cauchy bound, one may take

`C_vartheta=2*log(2)/rho^3`,
`C_ph=2*(3+2*sqrt(2))*log(2)/rho^3`.

For `|y| <= r_* tau^(-1/2)`, `r_*=rho/2`, the exact ellipse geometry gives

`|eta_j(s,t)| <= C_ph*tau^(3/2)*|y|^3`,

and therefore

`|eta_j(s,t)|^2 <= C_ph^2*tau^3*|y|^6`.

At the base this is the explicit scale
`C_ph*q^(3*N/2)*|y|^3`. Importantly, this is not obtained by taking a square
root of the R109 modulus budget; it is a separate consequence of a uniformly
controlled analytic phase. This closes the rough phase-budget question while
leaving annihilation open.

## 3. Sharpness and obstruction boundary

The R107 exact-fourth asymmetric law `H` gives a positive finite tower but is
not full-exact: its sixth cumulant is `-6`, whereas the full-exact d=3
fingerprint requires `kappa6=-3*kappa3^2`. After OU smoothing,

`vartheta(u)=-q^(3N/2)*u^3/6+O(q^(5N/2)*u^5)`,

so generically `|eta|` is of order `q^(3N/2)*y^3`. Thus the exponent is sharp
for the available probability-plus-positive-backward analysis; full exactness
must provide the extra cancellation.

The formal perturbation
`phi_epsilon(u)=exp(-u^2/2)*exp(-i*epsilon*u^3/6)` has exactly Gaussian modulus
but nonzero leading shear. It is a local algebraic obstruction model only and
is not asserted to be a characteristic function.

## 4. Evidence boundary and R114 target

- **PROVED / LOCAL-AUDITED:** the cubic shear polynomial, ellipse geometry,
  explicit constants, OU sixth-power scaling, and Gaussian Gram determinant
  recorded in `audit_r113.py`.
- **ANALYTICALLY PROVED by the web derivation, pending only local replay of
  the stated asymptotic calculation:** the Gaussian-neighborhood disk
  expansions and the uniform phase budget.
- **CONDITIONAL:** identifying the original bare scalar `RK=1` class with the
  genuine full-exact angular realization.
- **OPEN:** primitive odd-phase annihilation and the resulting
  Positive Backward-Tower Exact Zero-Set Rigidity.

R114 should compute the normalized primitive limit

`tau^(-3)*(Delta0*Delta1-|N|^2-S_G)`

and the exact angular `tau^3` limit, with all Gaussian baseline terms removed.
The decisive fork is whether the normalized four-point cone still permits
`|c_N|<=sqrt(2)` or instead forces `c_N -> 0`. A surviving cone is a genuine
four-point no-go and tells us exactly what additional positive backward input
must be used.

