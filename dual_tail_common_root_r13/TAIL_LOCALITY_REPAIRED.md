# Repaired dual-tail locality

The R13 gap was the estimate needed after division by the tail envelope
`b_i`.  It is now supplied by the preceding lemma, not by a stronger claim
about compactness alone.

Write

```text
L_e = M_D + K_e,   B_o = M_C + K_o
```

on the same-radius (ell^1) Wiener coefficient space.  R11 gives compact
`K_e` and `K_o`; its coefficient formula has output index `n=i+j+k`, so the
column `i` is supported at `n >= i`.  The compact lower-triangular column
lemma consequently gives

```text
|(K_e^* phi)_i| <= eta_e,i b_i,
|(K_o^* phi)_i| <= eta_o,i b_i,
eta_e,i, eta_o,i -> 0.
```

For a sequence of approximate tail maximizers `i_k`, normalize
`psi^(k)_m = phi_(i_k+m)/b_(i_k)`.  The repaired estimate makes both compact
remainders vanish in the normalized limit.  The two principal equations
therefore pass simultaneously to the forward recurrences with symbols
`D_s` and `C_s`.

This closes the single R13 tail-locality gap **under the audited R11
same-radius operator theorem**.  It does not prove that a genuine probability
solution exists, nor does it rule out a symmetric common zero of the two
symbols.

