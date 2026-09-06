# R49 — Christoffel compression and the moving-rank obstruction

This is a local exact audit of the webpage R49 theory round.  It does not
claim `Xi_K -> infinity`, ordinary Jacobi exit, or exclusion of a genuine
all-degree positive full-exact law.  The rank-two shadow supplies the cubic
test multiplier only; its null relation is never imposed on the full law.

## Audited identities

Let

```text
q(x) = x*P(x) = x*(x^2-c*x-v),   c^2=2*v,
Gamma_K = [L_0^mu(x^(i+j)*q(x)^2)]_(i,j=0)^K.
```

For the coefficient matrix `Q_K` of the map `p -> q*p`, the audit checks the
finite exact compression

```text
Gamma_K = Q_K^T H_(K+3) Q_K.
```

Writing `pi_n` and `h_n` for the monic orthogonal polynomials and norms of
the original moment functional, and letting

```text
zeta = (0, (c+sqrt(c^2+4*v))/2, (c-sqrt(c^2+4*v))/2),
K_n(zeta_i,zeta_j) = sum_(j=0)^n pi_j(zeta_i)*pi_j(zeta_j)/h_j,
D_n = det[K_n(zeta_i,zeta_j)],
```

the exact Schur formula checked is, for `N=K+3`,

```text
det(Gamma_K)/det(Gamma_(K-1))
  = h_N + p_N^T K_(N-1)^(-1) p_N,
```

where `p_N=(pi_N(zeta_i))`.  The determinant telescoping identity is

```text
det(Gamma_K) = det(H_(K+3))*D_(K+3)/(6*v^3),
```

because the root Vandermonde square is `6*v^3` under `c^2=2*v` and the
normalized lower moments have `h_0=h_1=1`.  The transformed Jacobi quotient is

```text
beta_tilde_K
  = beta_(K+3)*D_(K+3)*D_(K+1)/D_(K+2)^2.
```

The script checks these formulas exactly for the standard Gaussian moment
sequence and for a normalized positive five-point moment sequence.  The
compression identity is also checked symbolically for generic moments.

## Evidence boundary

The identities show that the lifted-null block is an ordinary Hamburger Gram
compression and its Schur complement is an ordinary Jacobi norm plus a
nonnegative three-root interpolation leverage.  Hence this route supplies no
automatic sign pressure stronger than ordinary Hankel positivity.  The
remaining statement

```text
Xi_K -> infinity
```

is still open.  Even all `Gamma_K >= 0` would only produce a positive measure
for `q^2*L_0`; inverse-Christoffel integrability and positivity of `L_0`
remain separate requirements.

Fixed-K formal positive prefixes, genuine all-degree positive full-exact laws,
and formal Gateaux/Hermite Taylor extractors remain distinct.  No optimizer,
SDP, numerical sweep, relaxed measure-LP, or remote computation is used.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_christoffel_rankescape_r49\audit_r49.py
```

Expected markers:

```text
R49_CHRISTOFFEL_COMPRESSION_IDENTITY PASSED
R49_THREE_ROOT_SCHUR_FORMULA GAUSSIAN PASSED
R49_HANKEL_KERNEL_DETERMINANT_FACTORIZATION GAUSSIAN PASSED
R49_TRANSFORMED_JACOBI_RECURSION GAUSSIAN PASSED
R49_THREE_ROOT_SCHUR_FORMULA FIVE_POINT PASSED
R49_HANKEL_KERNEL_DETERMINANT_FACTORIZATION FIVE_POINT PASSED
R49_TRANSFORMED_JACOBI_RECURSION FIVE_POINT PASSED
R49_LIFTED_GRAM_NO_INDEPENDENT_SIGN_PRESSURE RECORDED
R49_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN
R49_AUDIT_COMPLETED
```
