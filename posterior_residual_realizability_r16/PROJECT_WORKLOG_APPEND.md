# 2026-09-04 — R16 posterior residual realizability

- Created a theory-first R16 branch with exact SymPy replay of the posterior cumulant chain, order-4/order-6 rewrites, conditional `Q` moments, corrected negative residual tilt, Pearson/sixth projection inequalities, the low-order cone countermodel, Fisher deficit, and sample-mean tilt.
- Trusted result: all exact checks pass; the pointwise degree-six cone does not force constant posterior variance.
- Corrections: the joint triple residual exponent is negative; the projected sixth-order relation is an inequality. The cross-`x` coherence/realizability step remains open.
- No remote computation, order-8 expansion, optimizer, or Gram escalation was run.
