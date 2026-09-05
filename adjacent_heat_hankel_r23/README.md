# R23 adjacent heat-Hankel / flat-leakage audit

This small audit checks only proof-level local algebra:

- the Laurent asymptotics forced by a corank-one flat leakage block,
  `h_(M+1) ~ -ell_M^2/h_M` and
  `beta_(M+1) ~ -ell_M^2/h_M^2`;
- the interval/nesting logic for truncated PSD admissible radii and the
  derivative lower bound `|beta_n| >= n^2(a-g_n)`;
- the Schur-complement trichotomy `(ell_M,q_M)` and the sign convention for
  the atomic-shadow next-moment overshoot;
- the `O(M^3)` support-count arithmetic behind the finite plateau horizon;
- the ordinary Bernoulli-plus-Gaussian determinant example whose cubic factor
  has discriminant `-216`;
- the adjacent Jacobi-ratio formula in Hankel determinants;
- the exact adjacent-sector threshold used in the R22 obstruction.

It does not prove real zero interlacing, a small-value transversality bound, a
uniform flat-leakage horizon, post-failure tensor-tail domination, or Gaussian
rigidity.  In particular, `inf_n g_n` may be identified with a full backward
heat radius only after the required moment-determinacy/full-cone passage is
established; likewise the atomic-shadow identity is recorded as a sign
check, not independently re-derived from the full residual projection in this
small script.

Run with:

```text
F:/anaconda3/python.exe adjacent_heat_hankel_r23/audit_r23.py
```
