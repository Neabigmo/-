# 2026-09-04 — R13 dual-tail common-root audit

- Read the ChatGPT R13 plan and created isolated package `dual_tail_common_root_r13`; no remote compute, determinant search, numerical zero search, optimization, SDP, or NNQP.
- Formalized the dual defect characterization and conditional chain from normalized tail extraction to simultaneous shift recurrences and a common `D/C` spectral root.
- Added and proved the compact lower-triangular column lemma: `||K e_i||_1 -> 0` for compact lower-triangular `K` on `ell_1`, yielding the relative adjoint tail estimate after division by `b_i`.
- Audited the documented Stage7/R11 index relation `n=i+j+k >= i`; parity restriction preserves lower-triangular support. Added finite replays and a nontriangular compact counterexample.
- Updated the exact dual-surjectivity conclusion to hold under the audited R11 same-radius operator theorem.
- No remote compute, numerical search, optimization, or Gaussian-rigidity claim.
- Conservative outcome: `TAIL_LOCALITY_GAP`; no Gaussian rigidity claim and no automatic R14.
