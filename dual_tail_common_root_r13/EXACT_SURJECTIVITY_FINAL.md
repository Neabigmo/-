# Exact defect-map conclusion

Assume the audited R11 same-radius theorem, the R12 parity block
decomposition, and the compact lower-triangular column lemma.  A failure of

```text
Delta_rho : Y_rho -> coker(L_e)
```

has a nonzero bounded dual annihilator.  Tail normalization and the repaired
relative estimate produce a nonzero limit sequence on which both forward
recurrences hold.  The closed shift-invariant span of that sequence has a
nonempty spectrum in the closed unit disk.  Analytic spectral mapping then
gives a common zero of the two scaled symbols in the interior.  Removing the
scale yields a nonzero common zero of `D_R` and `C_R`.

Hence, under the stated hypotheses,

```text
no common interior nonzero D_R/C_R zero
    => Delta_rho is surjective.
```

The R12 identities

```text
D_R(z)+C_R(z)=R(-z/2)^2,
D_R(z)-C_R(z)=R( z/2)^2
```

reduce the exceptional mechanism to

```text
R(a)=R(-a)=0,  a != 0.
```

This is an exact surjectivity theorem away from symmetric common zeros.  It
is not a Gaussian-rigidity theorem: the existence or impossibility of such a
pair for a genuine probability/Fock solution remains open.

