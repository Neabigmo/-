# R36 exact audit — one-body Laguerre–Hoeffding carrier obstruction

This folder audits the R36 web-side result with exact finite SymPy identities.
It does not run an optimizer, SDP, numerical sweep, remote computation, or a
relaxed-law search.

The audited route is the genuine full-exact iid class.  For
`Phi_n(X1,X2,X3)=L_n((X1^2+X2^2+X3^2)/2)`, the full-exact law makes
`T=(X1^2+X2^2+X3^2)/2` exponential.  The Laguerre basis is therefore
orthonormal, and the iid Hoeffding decomposition gives

`1 = 3||h_1||^2 + 3||h_2||^2 + ||h_3||^2`.

At the Gaussian anchor, the angular Hermite–Laguerre identity and Gaussian
conditional contraction give

`k_n^gamma = kappa_n h_(2n)`,
`kappa_n=(-1)^n sqrt((2n)!)/(2^n n!) (2/3)^n`,
`||k_n^gamma||^2=binom(2n,n)/9^n`.

The five-copy shared-coordinate identity differentiates as

`dot A_(n,N)=3(S_(n,N)+4L_(n,N))`.

The exact Hermite triple coefficient and Cauchy bound on the leaf term imply,
for fixed `N`, a bound of the form
`C_N(1+n^(N/2))(2/3)^n`, which collapses as `n→∞`.  Consequently an ordinary
`l2`-bounded remote one-body Laguerre carrier cannot transport a nonzero fixed
head mismatch.  This is a proof-mechanism no-go, not a counterexample in the
full-exact positive class.

The audit intentionally leaves the two-body degenerate Hoeffding projection
open: pair conditioning sees the residual direction `(X1-X2)/sqrt(2)` and may
avoid the one-body `(2/3)^n` loss.  The next local target is therefore the
Gaussian two-body Laguerre projection and its fixed-head sensitivity.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_hoeffding_transgression_r36\audit_r36.py
```

Expected markers:

```text
R36_HOEFFDING_VALUE_IDENTITY PASSED
R36_GAUSSIAN_ONE_BODY_PROJECTION PASSED
R36_FIXED_HEAD_SENSITIVITY_COLLAPSE PASSED
R36_REMOTE_ONE_BODY_CARRIER NO_GO
R36_TWO_BODY CARRIER REMAINS OPEN
R36_AUDIT_COMPLETED
```
