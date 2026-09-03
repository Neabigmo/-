# Posterior-variance reformulation

For `Y_t=X+sqrt(t) Z`, Gaussian convolution and differentiation give

`rho_t(y)=(E[X|Y_t=y]-y)/t`,
`rho_t'(y)=Var(X|Y_t=y)/t^2-1/t`.

Under the escort measure associated with `p_t` and the target identity
`F=C/(1+t)`, `E_nu[rho_t']=-1/(1+t)`.  Hence

`E_nu Var(X|Y_t)=t/(1+t)` and
`Var_nu(Var(X|Y_t))=t^4 Var_nu(rho_t')`.

The first equality is an escort mean identity.  It is not an assertion that
ordinary MMSE is universally bounded by the escort mean.
