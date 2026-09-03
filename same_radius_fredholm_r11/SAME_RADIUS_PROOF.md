# Same-radius compact-perturbation theorem

The actual Stage-7 source and its normalization are audited in
`NORMALIZED_DOMAIN_CONJUGACY.md`.  In particular, the operator is understood
on the normalized tangent domain
`X_rho={h in W_rho^even:h_0=h_2=0}`, not on an unconstrained even space.

Under `w=z^2`, this domain is exactly `w^2 A^+_(rho^2)`.  The map
`C(g)=w^2g` is a bounded Banach-space isomorphism with norm factors `rho^4`
and `rho^-4`, so removing the fixed degree-0 and degree-2 coordinates does
not create a Fredholm defect.  The even multiplier and the compact remainder
are both preserved and conjugated by `C`.

Assume the all-degree normalized Stage-7 linearization has coefficients
`A_ijk/A_n00` from `ALL_DEGREE_ANGULAR_PROOF.md`, and let `R` be entire with
ordinary Wiener coefficients `r_j`.  Differentiating

```text
T(R)=<R(z*a_1) R(z*a_2) R(z*a_3)>
```

gives `D T_R[h]=3<h(z*a_1)R(z*a_2)R(z*a_3)>`; division by `3*A_n00`
cancels this factor.  The fixed-shift endpoint is

```text
d_m = (-1/2)^m sum_(j+k=m) r_j r_k,
sum_m d_m z^m = (R(z/2)^2+R(-z/2)^2)/2 = D_R(z).
```

For `m=j+k` and `i=n-m`, split the sum into `i>=m` and `i<m`.

* In the dominant part, each fixed `(j,k)` difference is a bounded weighted
  shift followed by a diagonal tending to zero, hence compact.  The uniform
  ratio bound makes the `m>M` tail bounded by a constant times
  `sum_(j+k>M)|r_j|rho^j|r_k|rho^k`, which tends to zero in `W_rho`.
* In the nondominant part, `i<m` implies `n<2m`.  The global ratio bound is
  `O(sqrt(m))`.  Since `R` is entire, choose `sigma>rho`; the coefficient
  conversion gives `q^m`, `q=rho/sigma<1`, and the tail norm is bounded by
  `C sup_(m>M)(sqrt(m)+1)q^m ||R||_(W_sigma)^2`.  For fixed `m`, only
  finitely many `i` occur, so the part is finite rank.

Therefore, after the source/domain identification audited above, under the
all-degree kernel formula,

```text
L_R - M_(D_R): W_rho^even -> W_rho^even
```

is compact.  This uses no strict radius loss in the final operator statement.
The remaining research question is not domain identification: it is whether
probability/OU coherence can rule out the resulting negative index.  This
theorem does not claim Gaussian rigidity.
