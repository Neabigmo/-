# R11 normalized even domain and `w^2` conjugacy

## Source identification

The original Stage-7 implementation is retained outside this extraction
repository at

`G:\2026\8.22统计\_stage7_result_extract_20260831_v1\run\chi2_n3_characteristic_transfer_stage7_2026-08-31\python\direct_r_core.py`.

Its `DirectRCompleter` sets `r[0]=1`, fixes `r[n]=0` for `n<=2`, and solves
even orders using `mean_power_sum[n]`, which is the symmetric sum of the
three root powers.  The companion
`THEORY_NOTE.md` states the exact coefficient equation

```text
sum_{i+j+k=n} A_ijk r_i r_j r_k = 0,
A_ijk = <a_1^i a_2^j a_3^k>,
```

and the even linear divisor `3 A_n00`.  Differentiating the displayed cubic
map gives

```text
D T_R[h] = 3 <h(z a_1) R(z a_2) R(z a_3)>.
```

After division by `3 A_n00`, the normalized coefficient operator is therefore

```text
(L_R h)_n = sum_{i+j+k=n} (A_ijk/A_n00) h_i r_j r_k.
```

This is the actual Stage-7 kernel identification used by R11, not a
hypothetical replacement recurrence.  The all-degree formula for `A_ijk` is
proved in `ALL_DEGREE_ANGULAR_PROOF.md` and replayed separately.

## The normalized tangent domain

Let `W_rho^even` be the even Wiener space and impose the normalization tangent
conditions

```text
X_rho = {h in W_rho^even : h_0 = h_2 = 0}.
```

The source normalization is `r_0=1`, `r_1=r_2=0`.  In the coefficient formula,
the degree-0 row is a fixed normalization row and is excluded from the
tangent operator.  In degree 2, every term containing a nonzero tangent
coefficient would require either `h_0` or `h_2` (the remaining factors are
the normalized `r_1,r_2`), so the degree-2 row vanishes on `X_rho`.  Hence
`L_R(X_rho) subset X_rho` after the fixed rows are removed.

## Exact `w=z^2` ideal

The coefficient map

```text
W_rho^even  ~=  A^+_(rho^2),
h(z)=sum_{j>=0} h_{2j} z^(2j) <-> sum_{j>=0} h_{2j} w^j
```

identifies `X_rho` with the principal ideal `w^2 A^+_(rho^2)`.  Define
`C(g)=w^2 g`.  With the Wiener norms,

```text
||C g||_rho = rho^4 ||g||_(rho^2),
||C^(-1) h||_(rho^2) = rho^(-4) ||h||_rho.
```

Thus `C` is a bounded Banach-space isomorphism onto the true normalized
tangent domain; the two removed coefficients introduce no Fredholm defect.

## Principal multiplier and compact remainder

For the even symbol `D_R(z)`, write `D_R(z)=Dtilde_R(w)` with `w=z^2`.
Multiplication preserves `w^2 A^+` and

```text
C^(-1) (M_D|X_rho) C = M_Dtilde_R.
```

The same-radius theorem already proved in R11 gives
`L_R-M_D=K` compact on `W_rho^even`.  Since both `L_R` and `M_D` preserve
`X_rho`, its restriction and conjugate
`Ktilde=C^(-1)(K|X_rho)C` are compact, and therefore

```text
C^(-1) (L_R|X_rho) C = M_Dtilde_R + Ktilde.
```

This closes the domain-identification and compactness passage without losing
the working radius.

## Index statement and boundary

If `Dtilde_R` has `N_rho` zeros in the open disk, counted with multiplicity,
and no zeros on the boundary, then multiplication by the zero-free factor is
invertible and

```text
ind(L_R|X_rho) = -N_rho.
```

The Stage-7 zero-free lemma still implies only that a non-Gaussian entire
`R` produces a negative normalized-even index at a suitable radius.  It does
not prove Gaussian rigidity.  The next open question is whether a genuine
probability/OU-coherent Fock solution can realize such a negative index.
