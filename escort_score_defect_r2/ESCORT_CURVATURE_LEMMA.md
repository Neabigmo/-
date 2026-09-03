# Escort curvature lemma

Assume `p>0` is smooth, the displayed boundary terms vanish, and
`F=int p^3=C/tau` with `tau=1+t`.  With `dnu=p^3 dx/F`,
`rho=(log p)_x`, and `c=rho_x`, exact escort integration by parts gives

`E_nu[f_x] = -3 E_nu[rho f]`,
`E_nu[rho]=0`, `E_nu[rho^2]=1/(3 tau)`, and `E_nu[c]=-1/tau`.

Writing `B=int p (p_xx)^2`, the pointwise identity
`p_xx/p=c+rho^2` and escort IBP give

`B/F = E_nu[c^2]-E_nu[rho^4]`.

The target second derivative `F''=2F/tau^2` and the heat-flow IBP identity
`F''=3B` then give the exact defect identity

`Var_nu(c) = E_nu[rho^4] - 3(E_nu[rho^2])^2`.

If the left side vanishes, `c` is constant under the positive escort
measure, hence everywhere on the connected support.  Therefore `log p` is
quadratic; integrability forces a Gaussian density.  This is an equality
lemma, not a claim that the defect is always zero.
