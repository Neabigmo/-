# R23 adjacent heat-Hankel / flat-leakage audit

This small audit checks only proof-level local algebra:

- the Laurent asymptotics forced by a corank-one flat leakage block,
  `h_(M+1) ~ -ell_M^2/h_M` and
  `beta_(M+1) ~ -ell_M^2/h_M^2`;
- monotonicity of truncated PSD admissible radii from leading principal-block
  inclusion;
- the adjacent Jacobi-ratio formula in Hankel determinants;
- the exact adjacent-sector threshold used in the R22 obstruction.

It does not prove real zero interlacing, a small-value transversality bound, a
uniform flat-leakage horizon, post-failure tensor-tail domination, or Gaussian
rigidity.  In particular, `inf_n g_n` may be identified with a full backward
heat radius only after the required moment-determinacy/full-cone passage is
established.

Run with:

```text
F:/anaconda3/python.exe adjacent_heat_hankel_r23/audit_r23.py
```
