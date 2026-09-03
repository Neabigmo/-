# Exact parity Hadamard lemma

For signs `sigma_j in {+1,-1}`, define

`Phi = E1 E2 E3 + sigma2 sigma3 E1 O2 O3`
`    + sigma1 sigma3 O1 E2 O3 + sigma1 sigma2 O1 O2 E3`.

Expanding the two products gives the exact identity

`Phi = 1/2 [ product_j(E_j+sigma_j O_j)
              + product_j(E_j-sigma_j O_j) ]`.

If `E_j >= |O_j|`, both factors in both products are nonnegative, hence
`Phi >= 0`.  If all three inequalities are strict, every factor is positive
and therefore `Phi > 0`.  This is an algebraic lemma; it does not assert that
an arbitrary continuum profile has the required pointwise inequalities.
