# R102 — log-cumulant charge symmetry audit

Date: 2026-09-07.

This package audits the definition-level result recovered by the webpage
round.  It keeps the original log-MGF charge separate from the R101
probability/Herglotz charge.

For a centered, variance-one law `mu`, write

`M_mu(z)=E_mu exp(zX)`, `K_mu(z)=log M_mu(z)`

and

`a_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`.

The audited charge convention is the complex Fourier coefficient

`P_3K(mu;z)=(1/(2*pi))*int exp(-3*i*theta)*mathscr K_mu(z,theta) dtheta`,

where

`mathscr K_mu(z,theta)=sum_j K_mu(z*a_j(theta))-z^2/2`.

The exact cumulant formula is

`P_3K(mu;z)=sum_{m>=3, m odd} Lambda_m*kappa_m*z^m/m!`,

with

`Lambda_m=3*(sqrt(2/3)/2)^m*binomial(m,(m-3)/2)>0`.

The package verifies the finite symbolic truncations of this formula, the
reflection law `P_3K(check(mu))=-P_3K(mu)`, and the OU covariance
`P_3K(P_t mu)(z)=P_3K(mu)(sqrt(t)*z)`.  It also verifies the first-nonzero
odd-sector coefficient against the R101 cubic charge map:

`[z^d]P_3K=beta_(d,1)/sqrt(d!)`.

The factor-two convention is explicit: a full cosine coefficient is `2*P_3K`.

## Evidence boundary

- **PROVED / locally audited:** the displayed finite exact algebra and all
  constants under the stated angular log-MGF definition; reflection and OU
  covariance at the analytic-germ level; the first-nonzero odd-sector
  comparison with `beta_(d,1)`.
- **PROVED under local-MGF uniqueness:** `P_3K==0` as an analytic germ iff all
  odd cumulants vanish iff the law is symmetric.
- **PROVED under R101 genuine full-exact, moment-determinate hypotheses:**
  `P_3K==0` iff `chi_1==0`; this is a zero-set equivalence, not an identity of
  observables.
- **OPEN:** exclusion of asymmetric genuine full-exact laws; uniform primitive
  lower bounds after OU normalization; the final positive backward-tower
  rigidity theorem; and any transfer from bare scalar `RK=1` without a separate
  identification theorem.

Run:

`python log_cumulant_charge_r102/audit_r102.py`

Expected terminal marker:

`R102_LOG_CUMULANT_CHARGE_AUDIT_COMPLETED`
