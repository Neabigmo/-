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
