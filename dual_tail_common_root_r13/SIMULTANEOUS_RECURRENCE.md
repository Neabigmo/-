# Simultaneous tail recurrence

Under the tail-locality estimate, divide the two adjoint equations at indices
`i_k+p` by `b_{i_k}`.  Dominated convergence for the principal `ell^1`
coefficients, together with the normalized-tail limit, yields

```text
sum_{m>=0} d_m psi_{p+m}=0,
sum_{m>=0} c_m psi_{p+m}=0,
```

for all `p>=0`, where `d_m=[u^m]Dtilde_R` and
`c_m=[u^m]Ctilde_R`.  These are exact simultaneous constant-coefficient
forward recurrences.  In R13 this implication is recorded as conditional;
no finite experiment is used to claim it for the actual compact remainder.

