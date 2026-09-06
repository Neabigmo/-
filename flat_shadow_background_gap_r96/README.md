# R96 — actual background gap obstruction and endpoint-safe quadratic bound

Date: 2026-09-07.

R96 audits the first concrete backgrounds rather than the class of arbitrary
bounded multipliers.  The outcome changes the use of the R95 gap-Wiener norm:
the canonical tangent `g1` is not uniformly gap-Wiener summable.  Its exact
finite-head cancellation removes gap one, but the remaining odd gaps have a
harmonic tail.  The quadratic background `g2` has an endpoint-safe uniform
bound for each individual gap; its absolute gap sum is still open.

All statements below are relative to the formal same-factor/Jacobi formulas
already recorded in R71/R79/R80/R82/R83.  They are not a construction of a
positive infinite backward tower.

## 1. Common exact gap formula

Let `e_k=H_k/sqrt(k!)`, `V_n=span(e_0,...,e_n)`, and
`Hcal_n(h)=P_n M_h P_n`.  If `eta_m=L_h[e_m]`, then

`Hcal_n(h)_(ij)=sum_r r! binom(i,r)binom(j,r)
sqrt((i+j-2r)!/(i!j!)) eta_(i+j-2r)`.

For `d>=0`, the one-gap coefficient of `R^m psi_q` is

`c_(j,d)^(m)(q)=sqrt((j+d)!j!)
 [z^(j+d)w^j] exp(zw)(z+w)^m exp(-q(z+w)^2)`.

Expanding both exponentials gives the fully finite coefficient formula

`c_(j,d)^(m)(q)=sqrt((j+d)!j!)
 sum_r (-q)^r/[r!(j+(d-m)/2-r)!]
 binom(m+2r,(d+m)/2+r)`,

where the sum contains only indices with integral, nonnegative factorials;
it is zero if `d` and `m` have different parity.  This is coefficient
extraction from the exact bivariate identity, not an entrywise-to-operator
shortcut.

## 2. `g1`: exact formula and the actual `Theta(log n)` obstruction

R71 gives

`g1=int_0^1 (q R^3-q^2 R^5/2) psi_q ds`,
`q=s(1-s)`, `T psi_q=exp(-qz^2)`, and `T(R^m psi_q)=z^m exp(-qz^2)`.

Therefore, with `K_(d,n)^(m)(q)=Delta_d Hcal_n(R^m psi_q)`,

`Delta_d Hcal_n(g1)=int_0^1 [q K_(d,n)^(3)(q)
 -q^2 K_(d,n)^(5)(q)/2] ds`.

The normalized moments are

`eta_(2r)^(1)=0`,
`eta_(2r+1)^(1)=(-1)^(r-1)r(r+1)!/[2 sqrt((2r+1)!)]`.

The canonical Jacobi tangent recurrence in R82/R83 gives the same matrix
entries directly.  Apart from the finite head,

`A_(k+2a+3,k)=(-1)^a (a+1)(a+2)/2
 [a(a+1)-2k] (k+a-1)!/k!
 sqrt(k!/(k+2a+3)!)`,  `a>=1`,

where `A_n=Hcal_n(g1)`.  The gap-three line is

`A_(k+3,k)=-2 sqrt(k!/(k+3)!)`, `k>=1`,

with the exceptional finite-head value `A_(3,0)=1/sqrt(6)`.  Gap one is
zero except for `A_(2,1)=1/sqrt(2)`.  All even gaps vanish by parity.

For a fixed `d`, `Delta_d A_n` is a weighted shift, hence its operator norm
is the maximum absolute entry on that diagonal.  Put

`R_(k,a)^2=prod_(r=1)^(a-1)(k+r) /
            prod_(r=a)^(2a+3)(k+r)`.

Then the displayed entry has magnitude
`(a+1)(a+2)|a(a+1)-2k| R_(k,a)/2`.
At `k=a(a+1)`,

`R_(k,a)>=exp(-7/2)[a(a+1)]^(-5/2)`  for `a>=2`,

so whenever `a^2+3a+3<=n`,

`||Delta_(2a+3) A_n|| >= exp(-7/2)/[2(a+1)]`.

Consequently the positive-gap sum is at least a constant times `log n`;
Hermitian symmetry gives the same conclusion for the negative gaps.

For the matching upper bound, pair the first `a-1` numerator factors in
`R_(k,a)^2` with the first `a-1` denominator factors.  This gives

`R_(k,a)<=exp(-(a-1)^2/[2(k+2a-2)])/(k+2a-1)^(5/2)`.

With `x=(k+2a-2)/(a-1)^2`, the remaining polynomial factor is bounded by
`3a^4(1+x)` and
`(1+x)x^(-5/2)exp(-1/(2x))<6`.  A uniform safe consequence is

`||Delta_(2a+3) A_n|| <=864/(a+1)`, `a>=2`,

with the finite head absorbed separately.  Thus

`||Hcal_n(g1)||_(W_n)=Theta(log(n+2))`.

In particular,

`B1^triangle=sup_n ||Hcal_n(g1)||_(W_n)=infinity`.

This is an actual project multiplier obstruction.  It is not the R95
`sgn(x)` example: it uses the R71 Gaussian mixture and the exact
canonical tangent/Jacobi cancellation.

## 3. `g2`: exact gap operator and endpoint-safe partial theorem

Write `q_t=t(1-t)`, and for an angular pair let `A=r_i^2`, `B=r_j^2`,
`xi=6q_tau q_s A`, `eta=6q_tau q_u B`, `alpha=xi+eta`.  R80's explicit
representer is the four-term combination

`g_(alpha,xi,eta)=7R^6 psi_alpha-(13/2)alpha R^8 psi_alpha`
` +(alpha^2+11xi eta/4)R^10 psi_alpha
 -(alpha xi eta/2)R^12 psi_alpha`.

The exact signed prefactor is

`w_(ij)=(6q_tau)^3 q_s q_u r_i^3 r_j^3`,

and, with the angular average,

`g2=-(1/3)<sum_(i<j) int_[0,1]^3 w_(ij)g_(alpha,xi,eta)
 d tau ds du>_theta`.

Consequently

`Delta_d Hcal_n(g2)=-(1/3)<sum_(i<j) int w_(ij)[
 7 K_(d,n)^(6)(alpha) -(13/2)alpha K_(d,n)^(8)(alpha)
 +(alpha^2+11xi eta/4)K_(d,n)^(10)(alpha)
 -(alpha xi eta/2)K_(d,n)^(12)(alpha)]>`,

where the same exact coefficient extractor from Section 1 is used with
`q=alpha`.  Since all degrees are even, `Delta_d Hcal_n(g2)=0` for odd `d`.

The endpoint estimate must be applied to the four-term combination as a
whole.  R80 gives `||g_(alpha,xi,eta)||_infty<=C_R80 alpha^(-3)` and

`|w_(ij)| alpha^(-3)
 =q_s q_u A^(3/2)B^(3/2)/(Aq_s+Bq_u)^3`.

The `q_tau^3` factor cancels exactly, so `tau` endpoints are harmless.  The
remaining two-parameter integral is at most `4` by the R80 endpoint lemma,
including `A=0` or `B=0` by continuity.  Therefore the rigorously available
partial theorem is

`sup_(n,d)||Delta_d Hcal_n(g2)||_op <= M2:=4 C_R80`.

This does not imply a summable gap bound.  The only immediate finite-section
conclusion is `||Hcal_n(g2)||_(W_n)<=M2(n+1)`.  The status of
`sup_n||Hcal_n(g2)||_(W_n)` remains OPEN; the missing lemma must retain the
four-term cancellation and the endpoint geometry while summing in `d`.

## 4. Consequence for the global route

The uncentered background cannot enter the R95 `W_n` small ball.  Indeed
`A_n` has only odd gaps and `B_n^(2)` only even gaps, so

`||aA_n+a^2B_n^(2)||_(W_n)
 =|a| ||A_n||_(W_n)+a^2||B_n^(2)||_(W_n)`.

The first term grows like `|a| log n` for every fixed nonzero `a`.  This is
not a failure of operator positivity: R80 still gives
`||A_n||_op<=M1`, `||B_n^(2)||_op<=M2`, so

`|a|M1+a^2M2+sup_n||Hcal_n(Ehat(a)+o(a))||_op<1`

is a valid **CONDITIONAL** fixed-`a` all-degree positivity criterion.

The correct structured equation must first absorb
`G_(0,n)=I+aA_n+a^2B_n^(2)` by a background factor `C_(0,n)`:

`C_(0,n)G_(0,n)C_(0,n)^*=D_(0,n)`.

For `G_n=G_(0,n)+H_(n)^res`, `C_n=(I+L_n)C_(0,n)`, and
`E_n=C_(0,n)H_(n)^res C_(0,n)^*`, the exact lower equation is

`L_nD_(0,n)=-L_- [E_n+L_nE_n+E_nL_n^*
                  +L_nD_(0,n)L_n^*+L_nE_nL_n^*]`.

Thus the next project-specific target is the background-centered estimate

`||C_(0,n) Hcal_n(h) C_(0,n)^*||_(W_n)
 <=C_bg ||Hcal_n(h)||_(W_n)`,

with uniform `0<c_-<=D_(0,n)<=c_+`.  This is **OPEN** and is the proper
replacement for the false uncentered bound on `A_n`.

## 5. Exact hybrid mismatch

For an odd residual written in R92 coordinates,
`o(z)=sum_j c_j Z_j z^(2j+1)`, `c_j=(j!)^2/(2j+1)!`, one has exactly

`||o||_(rho_n)=4sqrt(n) sum_j n^j w_j|Z_j|`,
`w_j=16^j c_j`.

Hence `ell^1(w)` does not embed uniformly into the R95 growing-radius ball.
For the unit `Z_j` mode define
`gamma_(n,j)=||Hcal_n(o^(j))||_(W_n)`.  The degree-local estimate yields

`gamma_(n,j)<=c_j(2j+2)2^(2j+1)(3n)^(j+1/2)`.

A concrete sufficient hybrid criterion is to set
`v_(n,j)=w_j+gamma_(n,j)` and require

`sup_(n,j) v_(n,j)^(-1) sum_k v_(n,k)|K_(k,j)^(n)| < infinity`.

The `w`-only part is the R92/R93 theorem; the `gamma`-feedback part remains
OPEN.  This is a criterion, not an assumed embedding.

## 6. Status boundary

**PROVED / locally auditable:** the exact `g1` gap formula; its finite-head
cancellation and factorial-ratio lower/upper bounds yielding
`Theta(log n)`; the exact `g2` four-term gap formula; the cancellation-safe
`alpha->0` endpoint reduction; and the uniform per-gap `g2` bound.

**CONDITIONAL:** fixed-`a` positivity from the operator-norm inequality above;
restarting nonlinear Gram contraction after a valid background conjugation;
and the hybrid small-ball implication if the displayed `v_(n,j)` column bound
holds.

**OPEN:** the absolute gap sum for `g2`; the background conjugation estimate;
the full nonlinear hybrid invariant ball; actual fixed-parameter global branch
construction; positive infinite backward towers; backward OU divisibility; and
the `FS_3` endpoint.

Audit command:

`F:/anaconda3/python.exe flat_shadow_background_gap_r96/audit_r96.py`
