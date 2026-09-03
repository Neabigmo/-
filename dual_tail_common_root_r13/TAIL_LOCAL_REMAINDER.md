# Tail-local remainder requirement

After the R11 radius conjugacy, write

```text
L_e=M_D+K_e,   B_o=M_C+K_o.
```

The dual common-root argument needs more than compactness.  For
`b_i=sup_{n>=i}|phi_n|`, it needs a relative estimate of the form

```text
|(K_e^* phi)_i| + |(K_o^* phi)_i| <= eta_i b_i,
eta_i -> 0,
```

or an equivalent high-column estimate strong enough to survive division by
`b_i`.  R11 proves same-radius compactness by fixed-band approximation and
radius-gap tails, but that statement does not imply this relative estimate:
compact operators can have adjoint coordinate rows that are not controlled by
the tail envelope of an arbitrary bounded dual vector.  The finite model in
`replay_tail_locality.py` illustrates the sufficient estimate only; it is not
evidence that the Stage7 remainder has it.

