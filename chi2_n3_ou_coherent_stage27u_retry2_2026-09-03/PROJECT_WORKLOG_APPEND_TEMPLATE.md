## 2026-09-03 — Stage27U retry2 numerical repair

- Work: reran OU-coherent lifted minimax after retry1 numerical-audit failure.
- Retry1 issues addressed: clipped-boundary gradient FD audit removed; active-set-stable interior gradient audit added; nonfinite-b regions converted only to non-scientific scaled-r overflow barriers; random starts calibrated by coherent high-q prefix energy; +/-Inf scientific CSV entries prohibited.
- Reliable result: fill from `stage27u_summary.json` and independent audit only after `STAGE27U_RETRY2_NUMERIC_AUDIT_OK`.
- Limitations: numerical campaign only; no global theorem, no Stage28.
- Next step: return results to ChatGPT for independent scientific review before any new stage.
