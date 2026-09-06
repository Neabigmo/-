# R72 — Analytic-norm angular tameness and conditional odd-solver closure

R72 sharpens the R71 Hermite--Gram barrier. It does not prove the missing
canonical odd-solver estimate, so it does not yet give an unconditional
all-`n` no-reversal scale or a boundary-layer reversal. It proves two useful
conditional facts: the even angular inverse is tame after any fixed analytic
radius loss, and an explicit odd-solver tame hypothesis closes the nonlinear
Hermite source majorant.

## 1. Exact even source equation

Let

    q=sqrt(2/3),
    F_a(z)=sum_(m>=0) L_a[e_m] z^m/sqrt(m!)=1+f_a(z),
    e_m=H_m/sqrt(m!).

The full same-factor identity is

    average_theta product_(j=1)^3 (1+f_a(r_j z))=1,
    r_j=sqrt(2/3) cos(theta+2 pi j/3).

Writing the linear, quadratic, and cubic terms as `A`, `Q`, and `C`, the even
part satisfies the exact coefficientwise equation

    f_e=-A_e^(-1)[Q(f,f)+C(f,f,f)].

The angular eigenvalues are

    A_(2k)=3 binom(2k,k)/6^k,
    A_(2k+1)=0.

For the truncated analytic Wiener norm
`||g||_R=sum_m |g_m|R^m`, one has

    ||Q(f,f)||_R <= 3||f||_(qR)^2,
    ||C(f,f,f)||_R <= ||f||_(qR)^3.

Wallis' bound `binom(2k,k)>=4^k/(2 sqrt(k))` gives

    A_(2k)>=3 q^(2k)/(2 sqrt(k)).

Consequently, for `0<theta<1`,

    ||A_e^(-1)g||_(theta qR)
      <= C_A(theta)||g||_R,
    C_A(theta)=(2/3) sup_(k>=1) sqrt(k) theta^(2k)<infinity.

At `theta=1/2`, `C_A(1/2)=1/6`. Thus

    ||f_e||_(qR/2)
      <= (1/6)[3||f||_(qR)^2+||f||_(qR)^3].

This proves that the angular inverse itself has no exponential operator growth
in this norm. The coefficient inverse `A_(2n)^(-1)` grows exponentially only
when the compensating radius loss is omitted.

## 2. Conditional odd-solver hypothesis

Write `f_o=aU+o`, where `U` is the audited R64 tangent and `o` is the odd
nonlinear remainder. Put

    rho_n=4 sqrt(n), sigma_n=8 sqrt(n),
    o=O_n(a,e), e=f_e.

The only new unproved input is the tame estimate

    ||O_n(a,e)||_(sigma_n)
      <= Omega_n( |a|^3 + |a| ||e||_(rho_n) ),

on the connected branch with `||e||_(rho_n)<=1`. This is compatible with odd
reflection parity, but no `n`-uniform bound on `Omega_n` is currently known.

## 3. Conditional closure of the nonlinear source

Set `U_n=||U||_(sigma_n)`. If `U_n>1` and

    |a| Ubar_n <= 4^(-(n+1)),
    |a| <= 1/(4 Omega_n),

where the explicit tangent bound

    U_n <= Ubar_n=(256/3)n^(3/2)(1+8n)e^(16n)

is available, a bootstrap using the even source equation gives

    ||e||_(rho_n)<=3 |a|^2 U_n^2,
    ||o||_(sigma_n)<=|a|^2 U_n^2,
    ||e+o||_(rho_n)<=4 |a|^2 U_n^2.

The change from `sigma_n` to `rho_n` uses only the finite-degree estimate
`||e||_(sigma_n)<=4^n||e||_(rho_n)` for degree at most `2n`; the even estimate
is applied with an intermediate radius chosen so that the input norm is
`sigma_n` and the output norm is `rho_n`.

## 4. R71 majorant and a conditional explicit scale

Write

    w=e+o=sum_(m<=2n) r_m(a) z^m/sqrt(m!).

The Cauchy estimate in the `rho_n` Wiener norm gives
`|r_m(a)|<=sqrt(m!) rho_n^(-m)||w||_(rho_n)`. Therefore R71's Gram majorant

    Mcal_n(a)=3^(n/2)sum_(m<=2n)3^(m/2)|r_m(a)|

satisfies

    Mcal_n(a)<=4 C_B 3^(n/2)|a|^2 U_n^2,
    C_B=1/(1-sqrt(6)/4).

Define

    a_n#=min{ 1/n,
              1/(4M_*),
              1/(4^(n+1) Ubar_n),
              1/(4 Omega_n),
              1/(2 Ubar_n sqrt(n C_B 3^(n/2))) }.

Under the odd-solver tame hypothesis, for `|a|<=a_n#`,

    Mcal_n(a)<=1/n,
    ||G_n(a)-I||_op<=1/4+1/n<1

for all sufficiently large `n`. Hence every leading Gram block through degree
`n` stays positive and

    beta_k(a^2)>0,  0<=k<=n,
    0<=t<=(a_n#)^2.

This is a genuine conditional all-order no-reversal window. Its scale is not
unconditional because `Omega_n` and its analytic domain are not yet bounded.

## 5. Actual status and next target

R72 rules out attributing an order-one nonlinear Gram profile to the even
angular inverse alone. A profile can still arise from the odd solver, source
accumulation, or loss of analytic radius. R72 does not construct a negative
profile, prove D.1, construct a positive exact backward tower, or establish
backward OU divisibility.

The unique next target is to prove the canonical odd-solver tame estimate with
an explicit `n`-growth bound for `Omega_n`, or to prove that such a bound fails
at a specific scale. The local exact audit is `audit_r72.py`.
