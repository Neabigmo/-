# Analytic Hilbert scale

For a Hermite coefficient sequence `b=(b_n)`, define

`||b||_s^2 = sum_n s^(2n) |b_n|^2`.

The radius statement needed by R8 is: there is a positive `rho_0` for which
the OU-smoothed coefficient sequence belongs to a positive-radius scale.  If
`b` is already in `H_R`, OU smoothing `b_n -> rho^n b_n` gives
`||OU_rho b||_s = ||b||_{s rho}` (with the evident interpretation for finite
partial sums), so `s rho <= R` is sufficient.

This is not asserted for an arbitrary `ell^2` sequence.  The weakest useful
hypothesis is positive-radius membership of the genuine probability's
Hermite expansion after some positive OU time (or an equivalent analytic
growth estimate).  Stage-19/Mehler input may be used to establish that
hypothesis for the target probability, but this small package does not prove
that analytic input from the probability axioms alone.

For `0<r<R`, the inclusion `H_R -> H_r` is compact: its diagonal weights are
`(r/R)^n -> 0`.  This is the functional-analytic source of the radius-gap
compactness below.

