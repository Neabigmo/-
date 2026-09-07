# R104 — Infinite Schur–Cumulant Cascade and Schur–Abel realization test

This package records the completed webpage derivation for R104 and its finite-
grade exact symbolic audit.  It does not claim the asymmetric genuine exact-law
exclusion or the final positive backward-tower rigidity.

## Audited interfaces

For a fixed admissible real `z`, write

`w_z(theta)=exp(mathscr K(z,theta))`,

and use the `2*pi/3` periodicity to set `phi=3*theta` and
`d sigma_z(phi)=w_z(phi/3) dphi/(2*pi)`.  Then

`c_r(z)=int exp(-i*r*phi) d sigma_z(phi)`

is a real Toeplitz correlation sequence.  The monic OPUC/Gram–Schmidt
reflection parameters are

`alpha_n=-Phi_(n+1)(0)`,

with

`E_(n+1)=E_n(1-alpha_n^2)`, `E_0=1`.

The first two are

`alpha_0=c_1`,

`alpha_1=(c_2-c_1^2)/(1-c_1^2)`,

and the optimal two-step prediction error is

`E_2=1-c_1^2-(c_2-c_1^2)^2/(1-c_1^2)`.

For a strictly positive continuous weight, the infinite Szego identity is

`exp(R(z))=prod_(n>=0)(1-alpha_n(z)^2)`,

where `R(z)=<mathscr K(z,theta)>`.  Equivalently, with

`S(z)=sum_(n>=0)-log(1-alpha_n(z)^2)`,

`S(z)=-R(z)`.

The local exact audit checks this identity coefficientwise through grade 12;
the omitted reflection parameters start too late to contribute to those
coefficients.

## Same-factor grades and forced-even recursion

The D3 geometry gives

`Lambda_(m,r)=3*(sqrt(2/3)/2)^m*binom(m,(m-3r)/2)`

whenever `m>=3r` and `m-3r` is even, and zero otherwise.  The angular average is

`A_(2N)=<p_(2N)>=3*binom(2N,N)/6^N`.

The charge/reflection selection rule is

`alpha_(r-1)(z)=O(z^(3r))`,

with `alpha_(r-1)(-z)=(-1)^r alpha_(r-1)(z)`.  At the first nonzero odd
cumulant degree `d`, the whole admissible first Schur vector is activated:

`[z^d] alpha_(r-1)=Lambda_(d,r) kappa_d/d!`,

for odd `r` with `3r<=d`.

Since `S=-R`, the forced even cumulants obey the triangular finite-grade formula

`kappa_(2N)=-(2N)!/A_(2N) * [z^(2N)] S(z)`.

Only charges `r<=floor(N/3)` can contribute to this coefficient.  The exact
symbolic audit verifies the barycenter equation, the first forced values
`kappa_4=0`, `kappa_6=-3*kappa_3^2`, the Schur budget through grade 12, and the
coefficient recursion.

## Global Schur–Abel reconstruction

Let `K_e(r)=(K(r)+K(-r))/2` and

`(A f)(r)=(2/pi) int_0^r f(s)/sqrt(r^2-s^2) ds`.

The same-factor geometry gives the real-axis identity

`A K_e(r)=r^2/4-(1/3)S(r/rho)`, `rho=sqrt(2/3)`.

The explicit Abel inverse yields

`K_e(r)=r^2/2-(1/3) d/dr int_0^r s*S(s/rho)/sqrt(r^2-s^2) ds`.

If `K=log M` comes from a genuine probability law, then

`K_e(r)>=0`, `K_e''(r)>=0`,

and therefore, with the derivative term denoted by `J(r)`,

`J(r)<=3*r^2/2`, `J''(r)<=3`.

These are genuine one-body realization constraints on the entire Schur
cascade.  The local audit confirms their algebraic Abel multiplier but does not
attempt to prove that every nonzero odd charge violates one of these global
constraints.

## Status

- D3 harmonic weights, Schur first steps, OU grades, Abel multiplier, and the
  finite-grade forced-even recursion: **LOCAL-AUDITED**.
- Infinite Szego product and Schur–Abel reconstruction for strictly positive
  continuous angular weights: **ANALYTICALLY PROVED**, with finite-grade audit.
- Formal infinite Schur completion by itself excludes no odd branch:
  **FORMAL-PROVED / NOT A PROBABILITY REALIZATION**.
- Schur–Abel Convexity Breakdown Lemma, asymmetric genuine exact-law exclusion,
  and final positive backward-tower rigidity: **OPEN**.
- The identification of a bare scalar `RK=1` with the genuine full exact
  three-copy law remains **CONDITIONAL** unless established elsewhere.

Run the audit with the project Anaconda interpreter:

`F:/anaconda3/python.exe infinite_schur_cumulant_r104/audit_r104.py`
