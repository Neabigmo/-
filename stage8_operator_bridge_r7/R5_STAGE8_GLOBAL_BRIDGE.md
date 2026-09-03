# Global R5–Stage-8 bridge

Let `q_theta` be the density of `L_theta` and `r_theta=q_theta/phi`, under the
regularity needed for the Hermite expansion.  Since the random-angle
projection is standard Gaussian,

`r_theta(x)=1+sum_{n>=1} S_n(theta) h_n(x)` in `L^2(dgamma)`,
`2 pi pi_x(theta)=r_theta(x)`.

The R5 missing-information integrand has the exact algebraic rewrite

`r_theta (partial_x log r_theta)^2 = (partial_x r_theta)^2/r_theta`.

The random-angle projection, positivity and differentiability of `r_theta`,
and the `L^2(dgamma)` expansion are analytic/probabilistic inputs, not claims
proved by this replay.  The algebraic rewrite is checked exactly.  It does
not by itself convert diagonal Gram positivity into a pointwise parity sign;
the Fock/product equations must enter any such coercivity argument.
