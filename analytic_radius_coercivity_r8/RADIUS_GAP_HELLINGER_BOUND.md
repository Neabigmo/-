# Hellinger Cauchy–Schwarz and radius loss

At fixed angle, the normalized Stage-8 coefficient is

`T_n^theta(u,v,w) = sum_{i+j+k=n} sqrt(P_n^theta(i,j,k))
 sigma_{ijk}(theta) u_i v_j w_k`,

where `sum P_n^theta = 1` and `|sigma|=1`.  Cauchy–Schwarz gives

`|T_n^theta|^2 <= sum_{i+j+k=n} |u_i|^2 |v_j|^2 |w_k|^2`.

After multiplication by `r^(2n)` and summing over `n`, this gives
`||T(u,v,w)||_r <= ||u||_r ||v||_r ||w||_r`, hence also the weaker
`H_R -> H_r` estimate for `r<R`.

If at least two indices are at least `N`, then with `q=r/R<1`,
`q^(i+j+k) <= q^(2N)`.  The same calculation gives

`||T_{2high,N}(u,v,w)||_r <= q^(2N)||u||_R||v||_R||w||_R`.

For three high indices the factor is `q^(3N)`.  The constants are uniform in
theta because only `sum P=1` is used; angle averaging cannot increase this
bound.  The replay checks the exponent and the exact zero residuals.

