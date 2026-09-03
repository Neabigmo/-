# Global kernel bound

The replay checks the normalized multinomial benchmark
`multinomial(n;i,j,k)(a_*/3)^n <= a_*^n`, with `a_*=sqrt(2/3)`, and the
central-binomial lower bound
`a_*^n C(n,n/2)/2^n >= (1/sqrt(2))a_*^n/sqrt(n+1)` for even `n>=2`.

This is the exact finite audit of the requested algebraic bounds.  Applying
it to the real Stage-7 `A_ijk` requires importing that exact source formula;
the package does not silently substitute a benchmark for it.

