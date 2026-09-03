# Escort-score defect R2

This package executes one bounded symbolic task from the C2C plan.  It does not start Stage28, NNQP, a large resultant, or a parameter campaign.

The primary objects are a positive smooth heat-flow density `p_t`,
`F=integral p^3`, the escort measure `dnu=p^3 dx/F`, `rho=(log p)_x`, and
`c=rho_x`.  Under `F(t)=C/(1+t)`, the package verifies the escort IBP
identities, the exact Gaussian equality case, posterior-variance
reformulations, and the first candidate defect evolution.

The package is deliberately conservative.  A candidate identity is recorded
as a theorem only when a symbolic total-derivative certificate is produced.
The second proposed defect formula is tested and reported separately; no
numerical optimizer is used to promote it to a result.

Run:

```text
python run_escort_defect.py
```

Then run the tests:

```text
python -m pytest -q tests
```
