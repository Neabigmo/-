# Principal cokernel compensation

Suppose `Dtilde` has an interior zero `w_alpha` of multiplicity `m_alpha`.
The cokernel of multiplication by `Dtilde` on the positive Wiener algebra is
represented by the jets modulo `(w-w_alpha)^m_alpha`.  If
`Ctilde(w_alpha) != 0`, then `Ctilde` is a unit in that local quotient.

For any target jet `p`, choose

```text
q = Ctilde^(-1) p mod (w-w_alpha)^m_alpha.
```

Then `Ctilde q` has the prescribed jet.  The replay verifies this explicitly
for simple and double zeros.  For distinct zero powers, the same construction
combines by the Chinese remainder theorem, so all principal defect jets are
surjective simultaneously.  Therefore, away from common symmetric zeros,
the odd principal block fills the entire principal cokernel of the even
principal block.

This is a theorem about the principal symbols.  It does not identify the
cokernel of `M_D+K` with evaluation jets, because a compact perturbation may
deform the finite-dimensional exact cokernel.

