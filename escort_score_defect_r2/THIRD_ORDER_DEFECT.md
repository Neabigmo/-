# Third-order defect audit

Set `R=sqrt(tau) rho`, `G=tau(c+1/tau)`, `U=tau^(3/2) rho_xx`, and
`delta=E_nu[G^2]`.  Formal heat differentiation plus the escort IBP rule
produces the first candidate exactly:

`tau delta' = -E[U^2] + 4E[G^3] + 3E[R^2G^2] - 3delta`.

The proposed alternative expression involving `(9/5)E[R^6]` is not used
unless an independent certificate is found.  The script records the exact
polynomial residual and searches for a bounded total-derivative certificate
using the target third-derivative relation.  Failure of that certificate is
an algebraic warning, not a density counterexample.
