# Posterior cumulant chain

With `d=1-q`, posterior exponential-family differentiation gives

`m' = V/d`, `V' = mu3/d`, `V'' = kappa4/d^2`, `V''' = kappa5/d^3`, and `V'''' = kappa6/d^4`.

The centered cumulants used here are

`kappa4 = mu4-3V^2`,
`kappa5 = mu5-10Vmu3`,
`kappa6 = mu6-15Vmu4-10mu3^2+30V^3`.

The powers of `d` are audited exactly; no numerical derivative normalization is used.
