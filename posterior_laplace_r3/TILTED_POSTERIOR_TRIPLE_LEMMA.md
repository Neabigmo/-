# Tilted posterior triple lemma

For `p_t=P_t mu`, `nu_t(dy)=p_t(y)^3 dy/F_t`, and three iid posterior
draws conditional on `Y=y`,

`integral product_i phi_t(y-x_i) dy = (2*pi*t*sqrt(3))^(-1) exp(-Q/(2t))`.

Therefore the escort average of any bounded nonnegative function of `Q` is
the `mu^3` expectation tilted by `exp(-Q/(2t))`.  If the original triple
statistic is `chi2_2`, its Laplace transform gives
`E_nu L_{t,Y}(s)=1/(1+2 a_t s)`, `a_t=t/(1+t)`.

The package certifies the quadratic decomposition and normalization
algebraically; it does not replace the assumed target law.
