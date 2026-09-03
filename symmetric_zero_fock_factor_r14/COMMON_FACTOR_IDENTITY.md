# Symmetric common-factor identity

For any analytic `R` with a symmetric zero pair `R(a)=R(-a)=0`, the normalized
factorization used by the Fock calculation is

```text
P_a(z) = 1-z^2/a^2,
R(z) = P_a(z) H(z).
```

This differs from the unnormalized factor `(z^2-a^2)` by the nonzero scalar
`-a^2`; all resonance constants must use the normalized `P_a`.

For the Stage7 angular roots `alpha_1,alpha_2,alpha_3`, put `t=z^2/a^2`.
The exact elementary identities give

```text
product_j (1-t alpha_j^2)
  = 1-t+t^2/4-t^3 q(theta)^2
  = (1-t/2)^2-t^3 q(theta)^2.
```

If `A_H(z)=<product_j H(z alpha_j)>` and
`B_H(z)=<q(theta)^2 product_j H(z alpha_j)>`, the full Fock identity becomes

```text
(1-z^2/(2a^2))^2 A_H(z) - (z^6/a^6) B_H(z) = 1.
```
For a real-coefficient analytic function, conjugation adds the conjugate
pair.  The resulting quartet factor is recorded separately in
`CONJUGATE_QUARTET_FACTOR.md`.

The factorization is an algebraic consequence of the two zeros.  It does not
make (H) a probability MGF, preserve positive definiteness, or transfer a
real-axis positivity inequality to the complex resonance point.
