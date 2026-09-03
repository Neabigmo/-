# Stage 8 parity kernel — R6

This package records a bounded, exact audit of the next proof layer after R5.
It does not claim a global Gaussian-rigidity theorem.  It checks four smaller
facts:

1. the exact parity Hadamard factorisation;
2. the interior square-root multinomial local-limit normalization (the
   uniform Stirling remainder remains a stated analytic lemma);
3. the exact Hermite/Mehler transform and the missing hypothesis needed to
   transfer backward-heat positivity to arbitrary Stage-8 parity profiles;
4. agreement of the low-mode odd-cumulant coefficient with the R5 formula.

Run from this directory with Python 3 and SymPy:

```text
python derive_parity_algebra.py
python derive_interior_lclt.py
python derive_backward_heat_matching.py
python audit_results.py
python -m pytest -q
```

The scripts write only small JSON reports under `results/`.  The package is a
proof-audit artifact: exact identities are marked certified, while asymptotic
claims state their domain and the remaining tightness/identification gap.
