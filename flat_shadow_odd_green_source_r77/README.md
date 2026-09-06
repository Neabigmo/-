# R77 — Local Gram-to-source factorial estimate

R77 supplies the missing source estimate from R76, but in a deliberately
explicit local domain. The browser connector again reported an account
connection error and did not read the local R76 files; the formulas below were
therefore extracted from the finished response and checked against the local
R76 baseline.

## 1. Local theorem

For degree `k`, set `rho_k=4 sqrt(k)` and use the degree-local Hermite–Wiener
ball

    ||h||_(rho_k) = sum_(m=3)^(2k) |eta_m| rho_k^m/sqrt(m!),
    h=E+Y,
    ||E||_(rho_k)+||Y||_(rho_k) <= delta_* = 1/40.

Assume the exact finite Gram/Jacobi map is evaluated in this ball and the
degree-local multiplication and derivative bounds stated below hold. Then,
for every fixed `mu>3`, there is `C_mu`, independent of `k,n`, such that

    k! |S_k(E,Y)|
      <= C_mu mu^k
         (||E||_(rho_k)||Y||_(rho_k)+||Y||_(rho_k)^3),  k>=3.

After restoring the finite head `alpha_1=a`, `alpha_2=-a` and subtracting
`a S^(1)`, this becomes

    k! |S_tilde_k(a,E,Y)| <= C_mu mu^k Xi_k,

    Xi_k = |a|(||E||_(rho_k)+||Y||_(rho_k)^2)
           + ||E||_(rho_k)||Y||_(rho_k)
           + ||Y||_(rho_k)^3.

Thus `FS_(3+epsilon)` holds on this local ball for every `epsilon>0`.
The endpoint `FS_3` is not proved.

This is a local conditional theorem, not a claim that mere positivity or
invertibility of every finite Gram matrix implies a uniform factorial bound.
The uniform constants use the displayed weighted small-ball hypothesis.

## 2. Why the Gram inverse is harmless locally

The degree-local multiplication estimate is

    ||P_(V_k) M_(e_m) P_(V_k)||
       <= 2^m (3k)^(m/2)/sqrt(m!).

The weighted moment bound gives
`|eta_m| <= ||h||_(rho_k) sqrt(m!)/rho_k^m`, so the perturbation series is
bounded by

    ||G_(k-1)-I||
      <= C_G ||h||_(rho_k),
    C_G=(sqrt(3)/2)^3/(1-sqrt(3)/2)<5.

At `delta_*=1/40`, this is below `1/8`; hence
`||G_(k-1)^(-1)|| <= 8/7`. The resolvent derivative identity gives, for
`r<=3`,

    ||D^r G^(-1)||
      <= r! (8/7)^(r+1) C_G^r,

so no degree-dependent factorial catastrophe is introduced at these orders.
The derivative bounds for `phi_k=e_k-G_(k-1)^(-1)g_k` are part of the
degree-local hypothesis and are required explicitly; they are not inferred
from positivity alone.

## 3. Hermite product and the base `mu>3`

For degree-`k` polynomials `psi,chi`, choose

    q_mu=mu+1,
    p_mu=2(mu+1)/(mu-3),
    1/2=1/p_mu+2/q_mu.

Gaussian hypercontractivity and Holder give

    ||x psi chi||_2
       <= ||x||_(p_mu) mu^k ||psi||_2 ||chi||_2.

Applying this to the Gram-orthogonalized `phi_k` and its first three
degree-local derivatives bounds the exact triangular numerator

    B_k = alpha_k gamma_k
          - L_underbar[ Pi_(<=2k)(x phi_k^2) ]

by `C_(mu,r) mu^k`, for `r<=3`. Since `T_k=B_k/k!`, the factorial denominator
is exactly the one required by `FS_mu`.

The parity identity from R76 makes `B_k(E,Y)` odd in `Y` for `k>=3`. Its
Gaussian linear term is precisely removed by
`S_k=T_k+sum_(j<k)q_(k,j)Z_j`. Taylor's formula then gives the
`E Y+Y^3` remainder; the finite head contributes only
`a(E+Y^2)` after subtracting the tangent.

The threshold `mu>3` comes from the finite `p_mu` moment of `x`. As
`mu` decreases to `3`, `p_mu` tends to infinity and `x` is not in
`L_infinity` under the Gaussian law. This proves a limitation of the present
Holder–hypercontractive argument, not optimality of the number `3`.

## 4. Uniform-in-`n` form and consequence for odd control

For `k<=n`, `rho_k<=rho_n`, so the local estimate implies the simultaneous
bound with the top norm `rho_n`. Combining with the R76 signed Green transfer
and taking `mu=3+epsilon` gives `lambda_mu=4+epsilon` and the conditional
common-radius estimate

    ||Z_tilde||_(sigma_n)
      <= C_epsilon n^(-1/2)
         exp((256+64 epsilon)n) Xi,
    sigma_n=8 sqrt(n).

Using the previously audited tangent majorant
`||U||_(sigma_n)<=32 sqrt(n) exp(160n)`, the conservative bootstrap algebra
gives

    |a| <= c_epsilon n^(-1/4)
          exp(-(288+32 epsilon)n),
    t=a^2 <= c_epsilon^2 n^(-1/2)
          exp(-(576+64 epsilon)n).

This is conditional on the even response/domain closure used in the preceding
R74/R76 chain. It is a genuine improvement over the earlier `e^(-1088n)`
scale, but it is still exponentially smaller than
`A_(2n) ~ 3 exp(-0.405465 n)/sqrt(pi n)`.

## 5. Boundary and next problem

R77 closes the R76 source gap only on the explicit local ball and leaves
`FS_3`, a global Gram-connected formulation without the small-ball bound, D.1,
the positive backward tower, and backward OU divisibility OPEN.

The next bottleneck is now factorial-type even bootstrap: close the same-factor
even angular equation in a sequence norm compatible with `k!|S_k| <= C mu^k`
without converting every coefficient to `sigma_n=8 sqrt(n)` and paying the
`exp(64 lambda_mu n)` and `4^n` losses.

