# 2026-09-04 — R18 Laguerre–Abel endpoint audit

- Branch: `chi2-laguerre-abel-endpoint-r18-2026-09-04`.
- Scope: theory-only exact Abel transform and finite symbolic checks.
- Certified: Abel/Poisson formula, positive quadratic kernel, operator form,
  and endpoint non-coercivity witness `c=(1,-1)`.
- Limitation: only `d0`–`d3` are present in the R17 source; no all-orders
  Fock-determined `D(r)` formula was available. No Gaussian rigidity claim.
- Decision: B; the missing full `D(r)` kernel/coercivity is now explicit.

# 2026-09-05 — Theory route framework and R8 cross-parameter correction

- Added `THEORY_ROUTE_FRAMEWORK.md` as the durable theory outline for the
  Positive Backward-Tower Exact Zero-Set Rigidity program.
- The framework records the target theorem, the exact-defect/Fock, positivity,
  backward-OU, and spatial-escort layers, plus the stop conditions for routes
  that only produce finite-jet or operator-only evidence.
- R8 web review audited the transport identities and corrected the status of
  the former integrated-compensation target: `∫_0^q S = -Var_{nu_q}(K'_q)`
  under the Gaussian endpoint condition, so it is equivalent to rigidity and
  is not an intermediate lemma.
- The current concrete gap is the anisotropic same-factor posterior-variance
  coherence behind `Var(Y|X=x) <= tau`; this is recorded as the next minimal
  OPEN problem. No finite computation was needed.
- From this round onward, each C2C theory prompt must ask ChatGPT to read the
  framework and this append log through the connector before proposing work.

# 2026-09-05 — R9 posterior bridge and anisotropic ordering reduction

- Web review confirmed the posterior identities
  `W-τ=τ²K''_q`, `E_{ν_q}W=τ`, and that pointwise `W≤τ` would already force
  `K''_q=0`; it is therefore not a useful intermediate estimate.
- Audited new bridge identity: for `H_q=P_{s-q}H_s`, with `μ_{q,s}` the `Y`
  marginal of the cubic-escort three-copy bridge and
  `𝒟=E_{ν_q}Var_{π_{q,s}}(K'_s(Y))`,
  `E_{μ_{q,s}}K''_s=-𝒟≤0`, while `E_{ν_s}K''_s=0`.
- Audited escort–MMSE identity: if `λ_q=p_q dx`, `ν_q∝p_q^3dx`, and
  `ω_q=p_q^2/∫p_q^3`, then
  `E_{λ_q}W=τ-τ²E_{λ_q}(K'_q)^2`, `E_{ν_q}W=τ`, and
  `Cov_{λ_q}(W,ω_q)=τ²E_{λ_q}(K'_q)^2≥0`.
- Exact obstruction is now a missing ordering/coherence statement comparing the
  anisotropic marginal `μ_{q,s}` with the scalar escort `ν_s`; ordinary positivity,
  total positivity, finite nested horizons, and arbitrary tangents do not provide it.
- Minimal R10 OPEN: whether genuine positive same-factor all-degree exactness yields
  some `q<s` with `E_{μ_{q,s}}K''_s≥E_{ν_s}K''_s=0`, or a rigorous no-go. No Codex
  finite computation is needed.
