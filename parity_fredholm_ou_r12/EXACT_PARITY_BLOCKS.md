# Exact parity blocks

For

```text
T(R)(z)=<R(z a_1) R(z a_2) R(z a_3)>,
D T_R[h]=3<h(z a_1)R(z a_2)R(z a_3)>,
```

write `h=h_e+h_o` and `R=E+O`.  The exact coefficient equation is

```text
sum_{i+j+k=n} A_ijk r_i r_j r_k=0,
A_ijk=<a_1^i a_2^j a_3^k>.
```

For an even output degree `n`, the parity of `i` equals the parity of the
pair degree `j+k`.  Consequently the derivative splits into an even-to-even
block and an odd-to-even block.  With Stage7 normalization `r_0=1,
r_1=r_2=0`, the normalized tangent domains are

```text
X_rho={even h:h_0=h_2=0}=z^4 A^+_(rho^2),
Y_rho={odd h:h_1=0}=z^3 A^+_(rho^2).
```

The degree-0 row is fixed and omitted.  The degree-2 output of a tangent in
`X_rho` is zero because `h_0=h_2=0` and `r_1=r_2=0`; thus the even block maps
`X_rho` to itself.  The small exact coefficient replay checks the parity
classification and the nonzero even divisor `3 A_n00` through total degree 8.

