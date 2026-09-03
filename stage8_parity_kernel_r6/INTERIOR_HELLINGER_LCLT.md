# Interior square-root multinomial local limit

Let `p_j>0`, `p_1+p_2+p_3=1`, and restrict to a compact interior
`min p_j >= delta`.  For raw deviations `y_j=N_j-n p_j`, `sum y_j=0`, the
interior Stirling expansion gives

`sqrt(P(N)) = (2 pi n)^(-1/2) (p_1 p_2 p_3)^(-1/4)
               exp(-sum(y_j^2/p_j)/(4 n)) (1+O_delta(n^(-1/4)))`

uniformly for raw deviations `|y_j| <= n^(1/2+1/12)=n^(7/12)`; equivalently
the standardized deviations satisfy `|y_j|/sqrt(n) <= n^(1/12)`.  The
displayed exponent is the quadratic part and the error exponent follows from
the cubic Stirling remainder.

In the coordinates `(y_1,y_2)`, the quadratic-form matrix has determinant
`1/(p_1 p_2 p_3)`.  Squaring the leading amplitude and integrating its
Gaussian over the constraint plane gives exactly one.  Each of the four
parity sublattices has asymptotic density one fourth in this two-dimensional
lattice.  The statement is local/interior; tails require a separate uniform
`l^2` tightness argument.  The R6 script certifies the determinant and Gaussian
normalization algebra; it does not by itself certify the uniform Stirling
remainder.
