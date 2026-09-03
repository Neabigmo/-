# Joint tilted triple law

Completing the square gives the corrected law

`dP_q(u1,u2,u3) = d^(-1) exp[-q Q(u)/(2d)] mu(du1)mu(du2)mu(du3)`.

The exponent is negative. For the Gaussian residual `Q~chi^2_2`, its Laplace transform is `d`, so the prefactor `d^(-1)` normalizes the law. A positive exponent would not normalize and is therefore a formula error.

Conditionally, `X | (u1,u2,u3) ~ N(q*(u1+u2+u3)/3, q*d/3)`.
