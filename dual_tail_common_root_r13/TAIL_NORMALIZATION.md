# Tail normalization selection

For a nonzero bounded dual sequence `phi`, define

```text
b_i=sup_{n>=i}|phi_n|.
```

Whenever `b_i>0`, an approximate maximizer gives an index `n>=i` with
`|phi_n|>=b_i/2`.  Resetting the base beyond the selected index recursively
produces `i_k -> infinity` and

```text
psi^(k)_m=phi_{i_k+m}/b_{i_k},
||psi^(k)||_infinity<=1,
|psi^(k)_0|>=1/2.
```

Diagonal compactness then gives a nonzero pointwise limit.  This elementary
selection lemma is replayed exactly on a finite sequence.  Passing the
operator equations to that limit still requires `TAIL_LOCAL_REMAINDER.md`.

