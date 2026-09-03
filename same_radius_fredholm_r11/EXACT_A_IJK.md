# Exact angular kernel

Let `a_l(theta) = sqrt(2/3) cos(theta+phi_l)` with
`phi=(0,2*pi/3,4*pi/3)` and `n=i+j+k`.  Fourier extraction gives

```text
A_ijk = (sqrt(2/3))^n 2^(-n)
        sum_{p,q,r; p+q+r=n/2}
        binom(i,p) binom(j,q) binom(k,r)
        omega^((j-2q)+2*(k-2r)),
```

where `omega = exp(2*pi*I/3)`.  The expression is real and is zero for odd
`n`.  The implementation also evaluates the same angular average by a
Laurent-Fourier constant term and by an exact roots-of-unity filter; all
triples of total degree at most 8 are compared.

The formula is an exact finite-degree angular-kernel derivation.  It is not by
itself a proof that this is the complete all-degree Stage-7 kernel in every
normalization; that import is recorded as the remaining gap in the result.

