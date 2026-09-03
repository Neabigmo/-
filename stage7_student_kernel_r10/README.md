# R10 — exact Student kernel and Wiener symbol audit

This is a bounded, theory-first audit.  It does not run remote jobs,
optimization, SDP, parameter grids, resultants, or numerical zero searches.

It corrects the Gaussian convention from R9: for the project's Fock
normalization `R(z)=E exp(zX-z^2/2)`, the standard Gaussian has `R=1` and
therefore `D_R=1`.

Run:

```text
python replay_normalization.py
python derive_angular_moment.py
python derive_student_kernel.py
python audit_symbol_theorem.py
python -m pytest -q
```

The conservative decision is
`STUDENT_KERNEL_CERTIFIED_OPERATOR_GAP_REMAINS`: the Student/Beta identities
and finite-band limits are replayed, but the complete Stage-7 uniform
operator-norm passage is not inferred without its original kernel file.

