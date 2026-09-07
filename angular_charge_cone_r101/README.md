# R101 — Angular Herglotz charge cone for genuine exact three-copy laws

Date: 2026-09-07.

This record audits the strongest new result obtained from the webpage round:
the same-factor cubic map can be placed inside a genuine positive angular
measure cone.  It is deliberately separate from `P_3 K`; the latter is still
not identified with the first angular charge.

## 1. Exact probability construction

Let `mu` be a centered, variance-one probability law satisfying the genuine
full exact three-copy identity.  Put

`r_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`

and let `mu_theta` be the law of

`Y_theta=sum_(j=1)^3 r_j(theta) X_j`, with iid `X_j~mu`.

The exact characteristic identity and uniqueness imply the genuine measure
barycenter

`(1/(2*pi)) int mu_theta dtheta = gamma`.

For an integer `r`, define the complex signed measure

`nu_r(B)=(1/(2*pi)) int exp(-3*i*r*theta) mu_theta(B) dtheta`.

The cyclic invariance of `mu_theta` makes `3*r` the natural angular grading,
and `nu_0=gamma`.  Total variation domination is unconditional:

`|nu_r| <= gamma`.

Thus `chi_r=d nu_r/d gamma` exists and `|chi_r|<=1` almost everywhere.

For every finite vector `c`, the positive measure

`sigma_c=sum_(p,q) c_p conjugate(c_q) nu_(p-q)`

has density `sum_(p,q)c_p conjugate(c_q) chi_(p-q)>=0`.  Hence the infinite
Toeplitz/Herglotz cone holds pointwise almost everywhere:

`[chi_(p-q)(x)]_(p,q=0)^M >= 0` for every `M`.

This proof uses measure positivity and does not use determinants, SDP, or an
optimizer.  The related Gaussian-relative Fourier Gram statement is recorded
only in its safe form: the full indexed block is positive, while an individual
complex `T_r` should not be written as an Loewner-ordered Hermitian matrix
without an additional reality convention.

## 2. Exact cubic map and all-degree cone

Write `e_m=He_m/sqrt(m!)` and `a_m=E_mu[e_m(X)]`.  Hermite addition gives

`E[e_m(Y_theta)] = sum_(k1+k2+k3=m)
 sqrt(m!/(k1! k2! k3!)) prod_j r_j(theta)^kj a_kj`.

If `beta_(m,r)=int e_m d nu_r`, then the exact same-factor charge map is

`beta_(m,r)=sum_(k1+k2+k3=m) sqrt(m!/(k1!k2!k3!))
 A_r(k1,k2,k3) prod_j a_kj`,

where `A_r` is the `3*r` Fourier coefficient of `prod_j r_j(theta)^kj`.
The selection rules are

`beta_(m,r)=0` if `m<3|r|` or `m not congruent r (mod 2)`.

Since `|chi_r|<=1`, Parseval gives the genuine nonlinear probability
inequality

`sum_(m>=3|r|, m congruent r (mod 2)) |beta_(m,r)|^2 <= 1`.

If `mu=P_t nu` and both laws are genuine exact, three independent OU copies
give `chi_r(mu)=P_t chi_r(nu)` and therefore

`beta_(m,r)(mu)=t^(m/2) beta_(m,r)(nu)`.

Consequently every positive `t`-preimage satisfies the full charge cone

`sum_(m>=3|r|, m congruent r (mod 2)) t^(-m)|beta_(m,r)(mu)|^2 <= 1`.

For `r=1`, the first explicit terms (under `a_1=a_2=a_4=0`) are

`beta_(3,1)=sqrt(6)/12*a_3`,

`beta_(5,1)=5*sqrt(6)/72*a_5`,

`beta_(7,1)=7*sqrt(6)/144*a_7`,

`beta_(9,1)=7*sqrt(6)/216*a_9 - 7*sqrt(14)/144*a_6*a_3
             + sqrt(70)/216*a_3^3`.

The last line is the first genuinely nonlinear charge mixing and is not an
identification of charge with the third Hermite coefficient.

## 3. Angular asymmetry theorem and its scope

Assume the exact law is moment-determinate (the project's square-exponential
envelope supplies this).  If its first nonzero odd Hermite coefficient is
`a_d`, then `d>=3` is odd and minimality leaves only the `(d,0,0)` permutations
in `beta_(d,1)`.  Therefore

`beta_(d,1)=Lambda_d*a_d`,

`Lambda_d=3*(sqrt(2/3)/2)^d*binomial(d,(d-3)/2)>0`.

It follows that

`chi_1=0  iff  mu is symmetric`.

Define

`S_3(t;mu)=sum_(m=3,5,7,...) t^(-m)|beta_(m,1)(mu)|^2` and
`tau_ang(mu)=inf{t in (0,1]: S_3(t;mu)<=1}`.

Every asymmetric genuine exact law has `tau_ang(mu)>0`, and any positive exact
preimage at parameter `t` satisfies `t>=tau_ang(mu)`.  Thus an asymmetric
fixed base has finite positive backward depth.  This strictly improves a
single `a_3` obstruction: asymmetry may first occur at any high odd degree.

This is a genuine weak theorem with independent reporting value.  It does not
solve the varying-bottom problem, because `tau_ang(mu_N)` may tend to zero.
It also does not prove `P_3K != 0 => chi_1 != 0`; the nonlinear log-density
charge and the angular charge remain distinct objects.

## Status

- **PROVED / locally audited:** D3 root-filter coefficients through degree 9,
  cubic Hermite-map coefficients, selection rules, the explicit all-degree
  Parseval cone, and the minimal-odd-mode asymmetry implication.
- **PROVED analytically under genuine full-exact identification:** barycenter,
  measure domination, pointwise Herglotz cone, and OU intertwining.
- **CONDITIONAL:** transferring the result from the genuine full-exact class to
  bare scalar `RK=1`, if that identification is not already independently
  established.
- **OPEN:** `P_3K` versus `chi_1` zero-set bridge; uniform primitive charge
  noncollapse for varying bottoms; symmetric even-sector rigidity; the full
  Positive Backward-Tower Exact Zero-Set Rigidity theorem.

Audit command:

`F:/anaconda3/python.exe angular_charge_cone_r101/audit_r101.py`

