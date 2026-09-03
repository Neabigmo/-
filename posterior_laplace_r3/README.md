# Posterior Laplace R3

This bounded symbolic package follows the C2C plan for the full posterior
Laplace-transform route.  It does not run Stage28, NNQP, Groebner/resultant
jobs, or a parameter campaign.

Run `python run_posterior_laplace.py`, then `python -m pytest -q tests`.
The pipeline verifies the Gaussian product identity, the full chi-square
Laplace identity, conditional Q moments through order four, the formal
moment-relaxation countermodel, and the posterior semigroup bridge.

The only kernel mechanism tested is the natural Gaussian-equality lower bound
`K >= K_Gaussian`.  A single exact heat-smoothed symmetric two-point prior
violates that bound: direct expansion gives
`K=1/2+(3/2)exp(-2/3)<3/2`.  The mechanism is stopped immediately.  This is
not a counterexample to the original characterization.
