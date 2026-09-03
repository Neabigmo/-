# R12 — parity Fredholm / OU audit

This package performs only exact symbolic and regression replays.  It does not
run numerical optimization, zero searches, SDP/NNQP, or remote computation.

The decision is deliberately conservative:

```text
PARITY_SYMBOL_CERTIFIED_EXACT_DEFECT_MAP_REMAINS
```

The odd-to-even principal symbol compensates the principal jet cokernel of
the even block away from common symmetric zeros, but compact perturbations
deform the exact cokernel.  The finite-dimensional exact defect map therefore
remains the single open question.  This package makes no Gaussian-rigidity
claim.

Run:

```text
python replay_parity_symbols.py
python audit_r12.py
python -m pytest -q
```

