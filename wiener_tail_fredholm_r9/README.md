# R9 — Wiener tail and single-radius characteristic reduction

This package is a bounded exact audit.  It does not run remote jobs,
optimization, SDP, parameter grids, resultants, or numerical zero searches.

The purpose is to separate the Hermite coefficient normalization from the
ordinary Taylor/Wiener normalization.  It checks the factorial conjugation,
the radius-loss tail mechanism, a finite-band Stage-7 replay, and exact range
conditions for multiplication by a polynomial with a simple or multiple zero.

Run from this directory:

```text
python replay_normalization.py
python exact_kernel_bound.py
python replay_wiener_range.py
python audit_results.py
python -m pytest -q
```

The conservative decision is `NORMALIZATION_REPAIRED_BUT_SYMBOL_LIMIT_NOT_UNIFORM`.
The ordinary Wiener compact-tail estimate is supported, but the exact
Stage-7 one-high infinite-band passage to `D_R` still requires the genuine
Stage-7 kernel formula and a uniform tail proof.

