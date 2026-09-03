# Exact Hermite identification

Use normalized probabilists' Hermites `h_m=H_m/sqrt(m!)`.  If
`L_theta=sum_j a_j(theta) X_j` and `sum_j a_j(theta)^2=1`, the generating
function gives the exact addition formula

`h_n(L_theta) = sum_{i+j+k=n} sqrt(n!/(i!j!k!))`
`                 a_1^i a_2^j a_3^k h_i(X_1)h_j(X_2)h_k(X_3)`.

Taking expectation gives precisely the Stage-8 signed Hellinger multinomial
integrand with `b_m=E[h_m(X)]`.  No local limit or asymptotic argument is used
for this identification.
