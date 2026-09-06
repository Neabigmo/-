# R87 — small-proportional algebraic safety window and correction audit

Date: 2026-09-07.

R87 returned a two-track plan: either close a small-proportional signed
phase-cancellation theorem, or prove a mesoscopic factorial majorant for the
`n^(-j)`-rescaled coefficient component.  This local round audits the
algebraic part of the first track and the finite combinatorics of the second.
It deliberately does **not** promote the proposed contour, source endpoint,
or angular phase lemmas to theorems.

## 1. Correct angular branch and the small-`delta` scale

Let `omega=exp(2*pi*i/3)`, `rho=alpha/(1+alpha)`, and let `x(alpha)` be the
branch through `x(0)=1` of

`P(alpha,x)=1+(1-omega)*(2*rho-1)*x-omega*x^2=0`.

At `(alpha,x)=(0,1)`,

`P_x=-(1+omega) != 0`,

so the implicit-function theorem supplies a nonzero complex neighborhood in
which this branch is analytic and nondegenerate.  With the complete
root-filter phase, the angular action can be written in expanded form as

`Phi_A(alpha,x)=2*alpha*Log(omega*(1+omega*x))
                 +2*Log(1+x)-(1+alpha)*Log(x)
                 -2*(1+alpha)*log(2)`.

On the saddle branch the envelope derivative is

`Phi_A'(alpha)=2*Log(omega*(1+omega*x))-Log(x)-2*log(2)`.

Therefore the PSC stationary value is

`zeta(alpha)=alpha*exp(-Phi_A'(alpha))
            =4*alpha*x/(omega^2*(1+omega*x)^2)`.

Since `omega^2*(1+omega)^2=1`, this gives

`zeta(alpha)=4*alpha+O(alpha^2)`.

With

`L=1+alpha+zeta`, `Delta=L+zeta=1+alpha+2*zeta`,

one obtains `Delta=1+9*alpha+O(alpha^2)`.

## 2. Endpoint algebra: two corrections that must be preserved

The source endpoint variable is the proportional ratio

`lambda = zeta/L`,

not `L/zeta`.  Consequently

`P_H(lambda)=(1+lambda)^3/(1-lambda)
             =Delta^3/((1+alpha)*L^2)`.

The exact Green endpoint calculation from R86 gives

`P_G=1-2*zeta/(L+zeta)=(L-zeta)/(L+zeta)`.

At the PSC point this is

`P_G^PSC=(1+alpha)/Delta`.

Thus the correct product is

`P_H*P_G=Delta^2/L^2`,

not `Delta^4/((1+alpha)^2*L^2)`, which is the product obtained by using the
inverse Green factor.  The apparent inverse in parts of the webpage R87
response is an internal inconsistency; the audit below rejects it.

For small positive `alpha`, the formal branch therefore has
`lambda=4*alpha+O(alpha^2)` and `Delta=1+9*alpha+O(alpha^2)`, so the algebraic
danger set is absent in a sufficiently small complex neighborhood.  This is
only an algebraic safety-window statement; it does not establish a uniform
complex source estimate.

## 3. Green endpoint separation and the remaining analytic gap

After the source saddle is frozen, the real `u`-integral has local exponent

`phi(u)=zeta*u+L*Log(u)`.

If `Re(Delta)>=eta>0`, then `Re(L)>0` because
`L=(1+alpha+Delta)/2`, and for `0<u<=1`,

`Re(phi'(u))=Re(zeta)+Re(L)/u
              =Re(Delta)+(1/u-1)*Re(L)>=eta`.

Hence `u=1` is the unique maximum on the original real segment.  Under an
additional uniform `C^2` bound on the source amplitude, ordinary endpoint
Laplace expansion would have denominator `j*Delta`.  The amplitude bound and
the complex source continuation are still open, so this does not yet prove
PSC.

## 4. Correct form of the conjugate-phase lemma

The webpage target

`C*exp(i*j*Theta)+conj(C)*exp(-i*j*Theta)`

does imply a positive limsup after normalization only with a nondegeneracy
condition.  `C != 0` alone is insufficient: `Theta=0` and purely imaginary
`C` make the displayed leading combination identically zero.  A valid
minimal condition is

`Theta not in pi*Z` or `Re(C) != 0`.

Under that condition the Cesaro mean of the squared leading combination is
positive (with the elementary separate treatment of `Theta in pi*Z`), so a
subsequence has modulus bounded below by a fixed positive constant.  This
supports a limsup statement, but the required two-saddle asymptotic itself is
still unproved.

## 5. Fallback arithmetic boundary

The proposed path bounds combine as

`j^(-1/2)*(1+r)^2*j^q/(r!*s!*g!)`

before summing `r+s+g=D`.  The exact multinomial identity is

`sum 1/(r!*s!*g!)=3^D/D!`.

With the `(1+r)^2` angular prefactor one instead gets an explicit polynomial
factor of order `(1+D)^2`; it cannot simply disappear while keeping the same
unspecified `q`.  Thus R87's target `(R87.16)` may still be viable after
recalibrating the polynomial prefactor, but the three displayed finite
inequalities are not by themselves a proof of it.  In particular, if the
source exponent is called `q_s`, a direct absolute convolution gives the
safe schematic form

`C*j^(q_s-1/2)*(1+D)^2*3^D/D!*exp(C*D^2/j)`.

This is the exact point to improve if the fallback route is selected.

## Status boundary

Locally audited and retained:

- the analytic angular branch anchor at `alpha=0`;
- the corrected `zeta=4*alpha+O(alpha^2)` and `Delta=1+9*alpha+O(alpha^2)`;
- the corrected definitions `lambda=zeta/L`, `P_G=(L-zeta)/(L+zeta)`;
- the correct endpoint product `P_H*P_G=Delta^2/L^2`;
- the real-segment derivative inequality for endpoint dominance;
- the exact multinomial arithmetic and the polynomial-factor warning.

Still open:

- uniform complex source endpoint continuation;
- amplitude bounds needed for endpoint Laplace expansion;
- the nondegenerate two-saddle asymptotic and PSC limsup theorem;
- a uniform mesoscopic factorial upper bound;
- all hybrid Gram/triangular, positivity, backward-tower, OU-divisibility,
  and `FS_3` conclusions.

The audit is exact symbolic/algebraic and finite.  It uses no scans,
determinants, optimizers, or remote computation.
