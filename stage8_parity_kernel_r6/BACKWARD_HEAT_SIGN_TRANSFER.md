# Backward-heat sign transfer audit

For a standard Gaussian, the exact Hermite/Mehler relation is

`E[H_m(X) | Y=y] = rho^m H_m(y)`.

Equivalently, the generating function transforms as

`sum rho^m H_m(y) t^m/m! = exp(rho*y*t-(rho*t)^2/2)`.

Thus positivity of a backward-heat amplitude at paired points implies an
`E_q >= |O_q|` inequality for those amplitudes.  What is *not* established by
the available R5 data is an exact identification of the Stage-8 local parity
profiles with these paired backward-heat amplitudes, uniformly in the double
scaling `n q -> tau`, including the normalization and the sign/location map.

Therefore this audit deliberately records the conservative outcome:
`BACKWARD_HEAT_SIGN_TRANSFER_FAILS` as a proof implication at the current
interface, not as a counterexample to the original theorem.  A valid transfer
would need an explicit uniform identification lemma (including tail
tightness), after which the Hadamard lemma could be applied.
