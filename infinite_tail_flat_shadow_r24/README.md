# R24 infinite-tail flat-shadow orientation audit

This small audit records the proof-level algebra behind the R24 reduction and
the explicit finite-prefix obstruction.  It checks:

- when `ell_M = 0`, the next Schur direction is `x P_M` and its norm is
  `q_M = L(x^2 P_M^2)`;
- the Laguerre identity turning the sign of `q_M` into the first unfixed
  radial Laguerre coefficient;
- the explicit positive 3-atomic Jacobi seed with exact `Q`, `Q^2`, `Q^3`
  but strict `Q^4` overshoot, including its negative formal `q_3`;
- one Gaussian-smoothed finite prefix whose order-4 Hankel block is strictly
  positive while the same-factor `Q` moments remain exact through order 4.

The finite-prefix construction is an iid-compatible strategy no-go only.  It
is not a genuine full-exact counterexample and does not refute Gaussian
rigidity.  The general statement that every prescribed finite horizon can be
preserved by triangular extension and sufficiently large smoothing is recorded
in the worklog as a lemma target, but is not silently promoted to a theorem by
this short script.  No full infinite-tail orientation theorem, plateau
`O(M)` bound, or `P_3K` bridge is proved here.

Run with:

```text
F:/anaconda3/python.exe infinite_tail_flat_shadow_r24/audit_r24.py
```
