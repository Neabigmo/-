# Laguerre–Parseval bridge

Use the ordinary Laguerre polynomials

\[
L_n(t)=\sum_{k=0}^n(-1)^k {n\choose k}\frac{t^k}{k!}.
\]

With the `Exp(1)` measure `e^{-t}dt`,

\[
\int_0^\infty e^{-t}L_n(t)L_m(t)\,dt=\delta_{nm}.
\]

Consequently, for square-integrable conditional quantities,

\[
m(t)=\mathbb E[\bar X\mid T=t]=\sum_{n\ge0}c_nL_n(t),
\quad c_n=\mathbb E[\bar X L_n(T)].
\]

Likewise write `b(t)=E[bar X^2|T=t]=sum d_n L_n(t)`.  The residual conditional variance

\[
h(t)=b(t)-m(t)^2\ge0
\]

is the exact realizability constraint.  Parseval gives `sum c_n^2 <= E[bar X^2]=1/3`, but
turning `h>=0` and the Fock-determined coefficients into `c_n=0` is an infinite-dimensional
problem.  The finite replay therefore records the bridge without claiming closure.

