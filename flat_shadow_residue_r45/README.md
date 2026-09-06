# R45 — finite N+6 multi-response audit

This audit records the exact finite part of the web-side R45 review.  It
targets the lowest resonance case `N=6` (`m=3`) and does not claim the
general Grade-(N+6) conditioning lemma.

## Exact scope

The script checks:

1. the degree-six same-factor Fock relation
   `b_6 = 7*sqrt(5)*b_3**2/10` for a genuine full-exact law;
2. the complete law-functional third-variation coefficient using the exact
   multi-copy identity
   `B = E[K_4] - 2 E[K_5] + E[K_6]`;
3. the `m=3,n=3` finite values of `H_(n;9,3)`, `H_(n;7,5)`, and
   `H_(n;6,6)` from the complete law-dependent Hoeffding kernel;
4. the combined effective degree-six response
   `J_(3,3) = (7*sqrt(5)/10) H_(3;6,6)
              + (1/2) D^3 B_3[h_6,h_3,h_3]`.

The third derivative is evaluated from the full law-functional multi-copy
formula, so base-measure weights, conditional projections, one-body
subtraction, and mean correction are included.  The `K_6` term is evaluated
by its two independent three-variable blocks; this is an exact factorization,
not a numerical approximation.

## Evidence boundary

The finite checks support the web-side correction that `N=6` has an extra
`-1/2 H_(6,6) Delta_6**2` resonance.  They do not establish the general
channel-exhaustion formula, the quotient coefficient matrices
`C_m`/`C_3^res`, their determinants, uniform conditioning, or the global
transgression.  Those remain open.

No optimizer, SDP, sweep, relaxed measure-LP, or remote computation is used.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_residue_r45\audit_r45.py
```

