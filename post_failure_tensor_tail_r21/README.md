# R21 post-failure tensor-tail audit

This small audit checks the new R21 proof-level algebra only:

- the two-dimensional residual projection geometry;
- the rotational polynomial lift on a representative polynomial;
- the first-failure capture factor and the ridge multiplier;
- the exact triple-pivot coefficient and its Stirling-scale sanity check.

It does not construct a full-exact iid counterexample and does not prove Gaussian
rigidity. The unresolved issue remains domination of the post-failure Jacobi/tensor
tail through degree `3M`.

Run with:

```text
F:/anaconda3/python.exe post_failure_tensor_tail_r21/audit_r21.py
```
