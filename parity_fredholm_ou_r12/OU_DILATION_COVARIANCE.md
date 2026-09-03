# Exact OU/scaling covariance

For `R_lambda(z)=R(lambda z)`, exact dilation equivariance gives

```text
T(R_lambda)(z)=T(R)(lambda z),
D_(R_lambda)(z)=D_R(lambda z),
C_(R_lambda)(z)=C_R(lambda z).
```

Thus `T(R)=1` implies `T(R_lambda)=1`.  With `N=z d/dz`, differentiation
along the logarithmic dilation orbit gives

```text
D T_(R_lambda)[N R_lambda] = N T(R_lambda) = 0.
```

The tangent splits as `N E_lambda + N O_lambda`, respecting parity.  The
ordinary parameter derivative is the same identity multiplied by the
harmless factor `lambda^(-1)`.  The replay checks the chain rule and the
`D/C` scaling identities exactly; it does not assert that this tangent makes
the exact defect map surjective.

