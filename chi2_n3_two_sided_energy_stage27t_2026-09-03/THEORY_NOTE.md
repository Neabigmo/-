# Stage27T theory note

Let the zero-branch prefix at fixed `(q,N)` be `P_N(lambda,s)`, with `eps=q^(3/2)`. A finite tail of length `L` has coefficients

    v = (v_{N+1},...,v_{N+L})

and must satisfy, at witness points `w_i=(lambda_i,s_i)`,

    P_N(w_i) + eps * sum_{k=1}^L v_{N+k} g_{N+k}(w_i) >= 0.

Write a feature row

    Phi_i,k = eps * g_{N+k}(w_i)

and `b_i=-P_N(w_i)`. The finite least-energy repair is

    minimize  1/2 ||v||_2^2
    subject to Phi v >= b.

Each row may be divided by an arbitrary positive norm `r_i`; this preserves the feasible set. Stage27T normalizes every row to remove the enormous scale variation that destroyed the earlier coefficient-space calculation.

The dual is

    minimize_{y>=0} 1/2 y^T (Phi Phi^T) y - b^T y.

After solving the nonnegative Gram QP, the explicit primal coefficients are recovered by

    v = Phi^T y.

A small half-space projection correction is allowed only to enforce numerical feasibility. The final reported upper bound is `||v||^2` after this correction, and is accepted only if:

1. stored witness slacks are nonnegative to tolerance;
2. the explicit density passes an independent continuum MP audit on the expanded numerical domain;
3. no final domain boundary is unresolved;
4. feature Gram PSD/cross-precision checks pass;
5. recovered dual/primal energy discrepancy is small.

The Stage27S finite-witness NNQP gives lower bounds for the full repair problem because adding continuum constraints can only increase the minimum required energy. Hence a validated explicit upper repair gives a meaningful numerical bracket.

The decisive test is fixed `kappa=Nq=6.4`. Stage27S already has C1 `(q,N)=(0.10,64)` with a robust finite-witness lower bound about 0.525. If C3, C4 or C5 yields a validated explicit upper bound <=1e-3 on the expanded domain, the hypothesis that repair energy is controlled only by `Nq` is numerically rejected. This is not a theorem-level statement.

If that happens, the next theoretical direction should be OU-coherent simultaneous-q tails: a genuine probability distribution supplies one Hermite coefficient sequence whose smoothed tails at different q are coupled, whereas all previous pointwise-q repairs optimize these tails independently. Stage27T records this as a recommendation only and never launches it automatically.
