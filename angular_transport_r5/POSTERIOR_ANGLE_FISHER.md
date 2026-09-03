# Posterior-angle Fisher field

Since the un-tilted mixture is `phi(x)`,
`pi_x(theta)=q_theta(x)/(2*pi*phi(x))` is a probability density. Exponential
tilting multiplies all components by the same factor in `x`, so `Theta|L=x`
remains `pi_x` for every tilt. Define
`H(x)=E_pi[(partial_x log pi_x)^2]`; it is nonnegative and is the posterior
angle Fisher information.
