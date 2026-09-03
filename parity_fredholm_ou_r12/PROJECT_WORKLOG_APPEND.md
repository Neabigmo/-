# 2026-09-04 — R12 parity Fredholm / OU audit

- Read ChatGPT's R12 plan and created isolated branch/package `parity_fredholm_ou_r12`; no remote computation, optimization, numerical zero search, SDP, or NNQP.
- Proved and documented the exact odd-to-even principal symbol `C_R=(R(-z/2)^2-R(z/2)^2)/2`, the common symmetric zero criterion, and principal jet compensation by finite Hermite interpolation.
- Added normalized `X_rho=z^4 A^+_(rho^2)` and `Y_rho=z^3 A^+_(rho^2)` replays plus exact OU dilation covariance.
- Conservative outcome: `PARITY_SYMBOL_CERTIFIED_EXACT_DEFECT_MAP_REMAINS`; the compact-perturbed finite-dimensional defect map `Delta_rho` is the single remaining gap, and OU coherence gives no certified contradiction.
