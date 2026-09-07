# R115 — Gaussian-relative slack saturation is equivalent to cubic exclusion

Date: 2026-09-07.

R115 closes the proposed four-point saturation route as an independent lemma.
It does not produce the desired saturation; instead it proves that, once the
R114 expansion and R112 uniform envelope are available, saturation is already
the same problem as eliminating the primitive cubic charge.

## 1. Fixed generic parallelogram

Choose one sufficiently small generic `(s0,t0)` for which the R114 coefficient
`F4(s0,t0)<0`. Write

`tau_N=q^N`, `h_N=g_N^(N)`, `mu_N=P_(tau_N)h_N`,
`c_N=kappa_3(h_N)`, and `lambda_4=-F4(s0,t0)>0`.

The fixed-frequency expansion, with a uniform remainder supplied by the R112
analytic envelope, is

`S_muN(s0,t0)=S_G(s0,t0)-lambda_4*tau_N^3*c_N^2+R_N`,
`|R_N|<=C4*tau_N^4`.

## 2. Exact equivalence

Suppose the desired relative comparison holds:

`S_muN(s0,t0)>=S_G(s0,t0)-epsilon_N*tau_N^3`,
`epsilon_N -> 0`.

Combining the two displays gives

`lambda_4*c_N^2 <= epsilon_N+C4*tau_N`,

so `c_N->0`. Conversely, if `c_N->0`, the expansion gives
`S_muN-S_G=o(tau_N^3)`, hence the same relative comparison. Thus, for this
fixed generic parallelogram,

`Gaussian-relative saturation  <=>  kappa_3(h_N)->0`.

If a subsequence has `|c_N|>=c_*>0`, then eventually

`S_muN <= S_G-(lambda_4*c_*^2/2)*q^(3N)`.

The strict Gaussian baseline makes this compatible with absolute Bochner
positivity. The obstruction is structural, not a missing remainder estimate.

## 3. Why all-degree exactness and backward OU do not give a free comparison

For a varying-bottom tower, any genuine full-exact top law `h_N` generates
`g_N^(j)=P_(q^(N-j))h_N`. This automatically gives the fixed-factor chain,
probability, and exactness at every layer. But the definition allows `h_N` and
`h_(N+1)` to be unrelated, so backward OU supplies no cross-`N` coherence for
`c_N`.

Higher exact cumulant rows enter the bottom at higher OU grades. They cannot
repair an already present `tau^3*c_N^2*F4` term; if all-degree exactness forces
`c_N->0`, that is the sought global rigidity itself.

The formal all-degree odd-charge completion from the earlier Schur–Abel route
therefore violates relative saturation whenever `c!=0`. More strongly, for any
finite order `M`, a small smooth perturbation of the Gaussian can match that
formal branch through order `M`, remain a genuine probability law with a
nonzero cubic moment, and retain all Bochner positivity. It need not be
all-degree exact. Hence no finite list of exact rows or minors can prove R115.

## 4. Compactness reduction to a single law

R112 supplies `E exp(X^2/8)<=2` uniformly for the genuine exact class. Therefore
the class is tight and all fixed moments are uniformly integrable. If
`limsup|c_N|>0`, take a subsequence with `c_N->c!=0` and `h_N=>h`. Moment
convergence gives `kappa_3(h)=c`. The exact angular identity passes to the
limit by dominated convergence, so `h` is itself genuine full-exact. The
converse is immediate: a single nonzero-skew genuine exact law used as every
top `h_N` gives a varying-bottom tower with `c_N` constant.

Consequently,

`there is a varying-bottom nonvanishing cubic sequence`
`<=> `there is a genuine full-exact single law with kappa_3 != 0`.`

This is the principal progress of R115: the finite-depth tower complexity is
quotiented out of the cubic sector.

## 5. The required replacement for a finite Gram minor

Any successful global functional must be Gaussian-centered and have a genuine
one-body/global factorization source. At minimum it should satisfy

`F(Gaussian)=0`, `F(mu)>=0`,
`F(P_tau h)=-C*c^2*tau^3+o(tau^3)`, `C>0`.

An ordinary positive Gram minor fails the first condition because the Gaussian
is a strict interior point and has positive slack. The next round therefore
removes `tau`, `N`, and finite four-point saturation entirely and attacks the
single-law factorized Gaussian-radial cubic exclusion.

## 6. Evidence boundary

- **PROVED / LOCAL-AUDITED:** the exact `H3` determinant and its primitive
  expansion, the `-5/24` coefficient, the angular `tau^3` cancellation,
  scale identities, and the algebraic saturation implication in
  `audit_r115.py`.
- **ANALYTICALLY PROVED by the web derivation, with local algebraic replay:**
  the full fixed-frequency expansion, saturation equivalence with a uniform
  remainder, and the compactness/dominated-convergence reduction.
- **CONDITIONAL:** bare scalar `RK=1` to genuine full-exact identification;
  existence of a genuine all-degree nonzero-skew law is the exact unresolved
  alternative, not a constructed counterexample.
- **FORMAL / FINITE-ORDER OBSTRUCTION:** coefficientwise odd-charge completions
  and their genuine moment-matching truncations.
- **OPEN:** single-law genuine full-exact cubic exclusion, hence the original
  Positive Backward-Tower Exact Zero-Set Rigidity.

R116 should study only the single-law factorized Gaussian-radial problem: if
`R` is the two-dimensional residual vector of three iid factors and
`|R|^2~chi^2_2`, decide whether the factorization forces `kappa_3(X)=0`.

