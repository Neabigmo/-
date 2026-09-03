# R17 — Conditional-Q Laguerre odd bridge

This branch audits the exact bridge between the odd Fock freedom and the conditional mean

\[
m(T)=\mathbb E[\bar X\mid T],\qquad T=Q/2\sim\operatorname{Exp}(1).
\]

The work is theory-first and intentionally small.  It contains exact SymPy replays for the
Laguerre convention, the tilted-mean coefficients, the first conditional second-moment
coefficients, the triangular leading-moment relation, and the R16 Fisher dictionary.

The audit is not a Gaussian-rigidity proof.  Its honest outcome is that pointwise conditional
variance positivity plus the checked finite coefficient identities does not yet force all odd
Laguerre coefficients to vanish.  The remaining task is an infinite conditional-variance
positivity theorem using cross-`x` coherence of the posterior exponential family.

Run from the repository root:

```powershell
F:\anaconda3\python.exe -m py_compile conditional_laguerre_odd_r17\replay_r17.py conditional_laguerre_odd_r17\audit_r17.py
F:\anaconda3\Scripts\pytest.exe -q conditional_laguerre_odd_r17\tests
F:\anaconda3\python.exe conditional_laguerre_odd_r17\audit_r17.py
```

No optimizer, numerical tail search, Gram campaign, remote computation, or order-8 escalation
is part of this branch.

