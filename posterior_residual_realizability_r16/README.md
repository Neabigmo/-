# R16 — posterior residual realizability

This is a theory-first exact audit following R15. It records the posterior cumulant chain, raw order-four/order-six identities, conditional residual moments, the corrected joint tilted triple law, moment-cone inequalities, an abstract countermodel, the spatial Fisher deficit, and the sample-mean tilt.

Run:

```text
python audit_r16.py
pytest -q tests
```

The machine-readable report is `results/r16_audit.json`. The honest outcome is D (`FORMULA_CORRECTION_REQUIRED`): the two supplied formulas need correction and the cross-`x` realizability gap remains. No remote or long-running computation is performed.
