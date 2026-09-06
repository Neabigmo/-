# R76 — Corrected signed source and factorial-transfer interface

R76 records the first nonlinear source object after the R75 sign correction.
The browser response was audited from its raw math sources; the connector did
not provide a read of the local R75 files, so the statements below are kept
separate from that unavailable read.

## 1. Exact source residual

Use the audited normalization

    e_m=H_m/sqrt(m!),       eta_m=L[e_m],
    phi_k=pi_k/sqrt(k!),   gamma_k=L[phi_k^2],

and the exact finite expansion

    x phi_k^2 = sqrt((2k+1)!)/k! e_(2k+1)
                 + sum_(m=0)^(2k) c_(k,m)(E,Y)e_m.

The triangular Jacobi equation is

    Z_k=T_k(a,E,Y)
       =1/k! [ alpha_k(a) gamma_k(E,Y)
               - sum_(m=0)^(2k)c_(k,m)(E,Y) eta_m ],

    Z_k=eta_(2k+1) sqrt((2k+1)!)/(k!)^2.

The Gaussian linearization is

    D_Y T_k(0)[Z] = -sum_(j<k) q_(k,j) Z_j,
    q_(k,j)=(1+2(k-j)/(j+1))/(k-j)!.

Consequently the signed nonlinear source is defined exactly by

    S_k := T_k + sum_(j<k)q_(k,j)Z_j,
    Z_k = S_k - sum_(j<k)q_(k,j)Z_j.

The minus sign is essential. It is the sign checked in R75 and is not the
positive majorant recursion.

## 2. Unconditional formal/algebraic cancellation

Reflection gives

    phi_k(E,-Y;x)=(-1)^k phi_k(E,Y;-x),
    gamma_k(E,-Y)=gamma_k(E,Y).

With alpha_1=a, alpha_2=-a, and alpha_k=0 for k>=3, the involution
`(a,Y)->(-a,-Y)`, `E->E`, makes the source odd. After subtracting the
Gaussian tangent source

    S^(1)(x)=x+x^2/2,
    S_tilde=S-a S^(1),

the formal/analytic Gram-neighborhood source ideal is

    S_tilde in a(E,Y^2) + E Y + Y^3.

For k>=3 there is no explicit alpha_k term, hence `S_k in E Y+Y^3`.
This means that under the canonical scaling `Y=O(a)`, `E=O(a^2)`, the
nonlinear odd source starts at cubic order. The exact ideal statement is the
algebraic milestone; uniform analytic bounds on its coefficients are not
being silently inferred.

## 3. Signed Green function and tangent check

For `Z(x)=sum Z_k x^k`, `S(x)=sum S_k x^k`, and
`F(x)=integral_0^x Z(t)dt`, the exact recurrence gives

    Z+2F=e^(-x)S,
    F=e^(-2x) integral_0^x e^t S(t)dt,
    Z=e^(-x)S-2e^(-2x) integral_0^x e^t S(t)dt.

Thus an entire source produces an entire signed solution. There is no signed
Green pole at `log(2)`; that pole belongs only to the absolute-value
majorant. With `S^(1)=x+x^2/2`,

    Z^(1)(x)=e^(-x)(x-x^2/2),
    [x^k]Z^(1)=(-1)^(k-1)(k+1)/(2(k-1)!),  k>=1,

which reproduces the audited R64 alternating tangent coefficients.

## 4. Factorial transfer theorem (proved conditional only on the source bound)

If a source obeys

    |S_k| <= M mu^k/k!,   mu>=0,

then the signed Green equation implies

    |Z_k| <= C_mu M lambda_mu^k/k!,
    lambda_mu=max(2,mu+1),

with the critical case `mu=1` carrying only an additional factor `k+1`.
The proof uses `Z'+2Z=e^(-x)(S'-S)` and the scalar recurrence

    b_(k+1) <= M(mu+1)^(k+1)+2 b_k,
    b_k=k!|Z_k|.

## 5. The remaining analytic interface

The smallest useful missing input is the n-uniform factorial source estimate

    |S_tilde_k| <= C mu^k/k! Xi,
    Xi=|a|(||E||+||Y||^2)+||E||||Y||+||Y||^3,

with fixed `C,mu` on the Gram-connected domain. Call this `FS_mu`. If it
holds, the preceding theorem yields factorial/exponential signed odd control.
On `sigma_n=8 sqrt(n)`, the elementary bound

    (2k+1)!/k! >= (k+1)!

gives the conditional conversion

    ||o||_(sigma_n)
      <= C C_mu [8 sqrt(n)/(64 lambda_mu n)]
         (exp(64 lambda_mu n)-1) Xi.

`FS_mu` remains OPEN. R76 proves the exact residual, the parity ideal, and the
signed transfer mechanism; it does not prove a positive backward tower, D.1,
or backward OU divisibility.

## 6. Next target

R77 should attack only the Gram-to-source factorial estimate: prove `FS_mu`
from the exact finite Gram/Jacobi map and Hermite product, or isolate the
smallest degree-local obstruction. A bound that first collapses all degrees
to the top level `n` does not answer this target.

