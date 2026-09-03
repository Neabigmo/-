# R8 — analytic-radius coercivity and Fredholm reduction

This is a bounded, exact audit package for the R8 plan.  It does not run a
parameter campaign, optimization, SDP, resultant, or zero hunt.  It records
what follows from a genuine positive-radius Hermite/OU hypothesis and keeps
the remaining Stage-7 operator-identification gap explicit.

Run:

```text
python derive_radius_gap_bound.py
python replay_endpoint_symbol.py
python audit_results.py
python -m pytest -q
```

The conservative decision is `RADIUS_GAP_COMPACTNESS_CERTIFIED_FREDHOLM_GAP_REMAINS`:
the radius-loss compactness mechanism and the candidate Fredholm defect
functionals are explicit, but the full Stage-7 infinite-dimensional operator
normalization/range theorem is not silently inferred from a finite replay.

