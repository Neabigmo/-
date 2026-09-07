# R114 — Primitive cubic shear limit and the four-point no-go

Date: 2026-09-07.

R114 is the first scale audit after the R113 uniform phase budget. It separates
fixed physical frequencies from the primitive frequency rescaling and removes
an attractive but invalid route to `c_N -> 0`.

## 1. Fixed-frequency expansion

Let `tau=q^N -> 0`, `h_N=g_N^(N)`, `mu_(tau,N)=P_tau h_N`, and
`c_N=kappa_3(h_N)`. For fixed real `r`, OU transport and the exact d=3
fingerprint give

`log phi_mu(r) = -r^2/2 - i*tau^(3/2)c_N*r^3/6`
`                 + tau^3*c_N^2*r^6/240 + O(tau^(5/2)r^5)+O(tau^4)`.

After exponentiation, the relevant real invariant sees

`phi_mu(r)=exp(-r^2/2)[1-i*tau^(3/2)c_N*r^3/6`
`                    -7*tau^3*c_N^2*r^6/720]+o(tau^3)`.

For R109's four points `x=(0,s,s+t,2s+t)`, write `G` for the Gaussian
four-point Gram matrix. The Schur residual is related to the full determinant by

`S_mu := Delta0*Delta1-|N|^2 = (1-|phi_mu(s)|^2) det(G4(mu))`.

Perturbing `G` by the cubic matrix `A` and real sixth-order matrix `B` yields

`S_mu = S_G + tau^3*c_N^2*F4(s,t)+O(tau^4)`,

where

`F4=S_G*(tr(G^(-1)B)-1/2 tr((G^(-1)A)^2))`
`    - exp(-s^2)*s^6*det(G)/120`.

This is the fixed-frequency formula; no `r~tau^(-1/2)` substitution has been
made.

## 2. Gaussian neighborhood and the sign trap

Let
`Pi=s^6*t^2*(s+t)^4*(2s+t)^2` and
`H3=[m_(i+j)]_(i,j=0)^3`. The Vandermonde leading law is

`S_mu = det(H3)/144 * Pi + O(y^16)`,
`y^2=s^2+(s+t)^2+(2s+t)^2`.

For the exact d=3 jet,

`m3=tau^(3/2)c_N`,
`m4=3`,
`m5=10*tau^(3/2)c_N+tau^(5/2)d_N`,
`m6=15+7*tau^3*c_N^2`,

where `d_N=kappa_5(h_N)`. Exact determinant algebra gives

`det(H3)=12-30*tau^3*c_N^2-12*tau^4*c_N*d_N`
`        -tau^5*d_N^2-6*tau^6*c_N^4`.

Thus, in a generic sufficiently small parallelogram,

`S_mu-S_G = -(5/24)*tau^3*c_N^2*Pi + O(tau^4*Pi)+O(y^16)`.

The sign is negative, but this does not violate Bochner positivity: `S_G` is
strictly positive. Positivity acts on `S_mu`, not on `S_mu-S_G`. Therefore the
normalized correction has no positivity sign and cannot force `c_N=0`.

## 3. Exact angular `tau^3` limit

For the normalized angular exactness functional

`Z_(tau,N)(y)=exp(y^2/2)*< product_j phi_mu(a_j(theta)y) >_theta`,

the audited angular constants are
`<p6>=5/18` and `<p3^2>=1/12`. The first primitive term is

`Z_(tau,N)(y)=1-tau^3*y^6*(kappa_6(h_N)+3*c_N^2)/2592+O(tau^4)`.

Full exactness sets `kappa_6(h_N)=-3*c_N^2`, so the normalized angular limit is
identically zero for every bounded `c_N`. It supplies the sixth-cumulant
fingerprint, not cubic-charge annihilation.

## 4. Rescaling distinction and finite-jet obstruction

For fixed `s,t`, the legitimate primitive phase normalization is

`tau^(-3/2)*eta_(tau,N)(s,t) -> -c_N*s^2*(s+t)`

along any subsequence where `c_N` converges. If instead
`s=tau^(-1/2)*sigma`, `t=tau^(-1/2)*xi`, then off-diagonal Gaussian factors are
exponentially small and the Gram matrix tends to the identity; there is no
polynomial `tau^3` expansion to combine with the fixed-frequency formula.

The web derivation also gives a genuine probability finite-jet construction with
`m1=0`, `m2=1`, `m3=c`, `m4=3`, `m6=15+7c^2` for small nonzero `c`. Its Bochner
positivity, positive OU chain, and degree-six exact fingerprint coexist with
nonzero cubic charge. It is not an all-degree exact counterexample, but it proves
that no argument using only degree-six data and four-point PSD can close the
primitive sector.

## 5. Evidence boundary and next target

- **PROVED / LOCAL-AUDITED:** cumulant-to-moment substitutions, the exact
  `H3` determinant, Gaussian leading coefficient, angular `tau^3` cancellation,
  OU/frequency scaling identities, and the cubic shear polynomial in
  `audit_r114.py`.
- **ANALYTICALLY PROVED by the web derivation, with algebraic ingredients
  replayed locally:** the full fixed-frequency trace formula for `F4` and the
  finite-jet bump realization argument.
- **CONDITIONAL:** bare scalar `RK=1` to genuine full-exact identification.
- **OPEN:** `c_N -> 0` under all-degree exact positive backward divisibility.

R115 should attack only a Gaussian-relative slack saturation lemma: prove for one
fixed generic parallelogram that `S_(g_N^(0)) >= S_G-o(q^(3N))`, or replace it by
an all-degree positive/backward functional with primitive coefficient `-C*c_N^2`.
Without such a relative comparison, more local determinant coefficients cannot
close the theorem.

