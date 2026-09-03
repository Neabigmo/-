# R5 low-mode consistency

For an odd first nonzero mode `d`, the squared leading Hellinger/OU
coefficient is

`rho^(2d) * kappa_d^2 * mean[p_d^2] / ((d-1)!)^2`.

The R6 replay evaluates the positive coefficient for `d=3,5,7,9` and checks
the symbolic general odd-d expression.  This is consistency with the R5
normalization, not an independent lower bound for the infinite-dimensional
problem.
