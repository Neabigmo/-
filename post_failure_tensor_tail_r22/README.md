# R22 heat-Hankel / flat-tail audit

This small audit checks the new proof-level algebra only:

- Vandermonde harmonic heat expansion and its top coefficient;
- transversality of a flat Hankel crossing;
- the flat leakage determinant;
- the translation-invariant adjacent-coefficient bound;
- the simultaneous appearance of the degree-`3M` coordinate channel in a
  representative triple-pivot test.

It does not prove cross-rank tail domination, construct a full-exact iid
counterexample, or prove Gaussian rigidity. The unresolved issue is still the
quantitative cross-rank heat-Hankel/flat-leakage geometry.

Run with:

```text
F:/anaconda3/python.exe post_failure_tensor_tail_r22/audit_r22.py
```
