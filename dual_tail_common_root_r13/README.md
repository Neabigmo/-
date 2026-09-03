# R13 — dual-tail common-root audit

This package follows the R12 finite-dimensional defect-map question without
starting a determinant search or numerical campaign.  It formalizes the dual
annihilator route and checks the exact algebraic pieces on small examples.

The result is deliberately conditional:

```text
TAIL_LOCALITY_GAP
```

R11 compactness is not, by itself, the relative tail estimate needed after
normalizing by a decreasing tail envelope `b_i`.  Until that stronger estimate
is proved for the actual kernel, the common-root conclusion remains
conditional.  No Gaussian rigidity claim is made.

Run:

```text
python replay_tail_locality.py
python audit_r13.py
python -m pytest -q
```

