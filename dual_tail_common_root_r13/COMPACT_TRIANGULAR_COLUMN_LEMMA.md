# Compact lower-triangular column lemma

Let (X=ell^1(mathbb N_0)), with basis (e_i), and let (K:X	o X) be
compact.  Assume the matrix is lower triangular in the support sense

```text
supp(K e_i) subset {n >= i}.
```

Then

```text
||K e_i||_1 -> 0.
```

Indeed, if a subsequence had norm at least epsilon, compactness would give a
further norm-convergent subsequence `K e_{i_j} -> y`.  For every fixed finite
coordinate range, the lower-triangular support is eventually zero, so the
limit has every coordinate zero.  Thus `y=0`, contradicting the lower norm
bound.  This is the point at which lower triangularity is essential: the
rank-one compact map `x -> (sum_i x_i)e_0` has all column norms equal to one
and is not lower triangular.

For every bounded dual sequence (phiinell^infty), put

```text
b_i = sup_{n >= i} |phi_n|.
```

The support condition gives the exact estimate

```text
|(K^* phi)_i| <= ||K e_i||_1 b_i = eta_i b_i,
eta_i -> 0.
```

This applies separately to `K_e` and `K_o`.  It is an abstract lemma, not a
numerical tail experiment.

## Scope

In the present project, R11's same-radius theorem supplies compactness of
the remainders under its audited all-degree kernel hypothesis.  The direct
coefficient formula supplies `n=i+j+k >= i`, hence lower-triangular support;
restriction to parity blocks preserves the support.  The conclusion below is
therefore conditional only on those already-documented R11 hypotheses.

