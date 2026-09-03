# R7 decision

## R6_POINTWISE_SIGN_INTERFACE_INVALID

The exact operator bridge is:

`S_n(theta)=<Psi_n,theta, G^tensor3 e_0^tensor3>`,

with the automatic bound
`|S_n|^2 <= <Psi_n,G^tensor3 Psi_n>`.  A finite exact PSD example has a
negative mixed matrix element, so operator positivity alone cannot imply the
pointwise Stage-8 inequality `E_j >= |O_j|`.

This is not a counterexample to the original Gaussian characterization and it
does not satisfy the Fock equations.  Any future Stage-8 proof must combine
the Fock/product equations with positivity, rather than use positivity alone.
