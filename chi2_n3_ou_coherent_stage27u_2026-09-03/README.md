# Stage27U — OU-coherent low-q completion / high-q obstruction

This package implements the Stage27U plan for the n=3 chi-square characterization project.
It does **not** run Stage28 and it does **not** launch a naive simultaneous-q or N*q^alpha campaign.

## Scientific pivot

Stage27T obtained no validated independent-q primal upper bounds. Stage27U therefore stops
trying to repair each q independently and instead enforces the exact OU coherence of one
master Hermite/Fock coefficient sequence.

For d=3 and master coefficients a_n,

    b_n(q) = q^(n/2) a_n,
    u_n(q) = b_n(q)/q^(3/2) = q^((n-3)/2) a_n.

Thus for qL=0.05, qH=0.10,

    u_n(qH) = 2^((n-3)/2) u_n(qL).

Stage27U uses qL only as a numerically stable triangular Fock-completion device, then lifts
the completed prefix exactly to qH=0.10 where prefix energy and robust infinite-tail
obstruction are evaluated.

The scaled Hermite recurrence also yields the exact master-feature identity

    q^(n/2) g_n(q,lambda,s) = g_n(1,q*lambda,s).

The package tests direct/high vs low-complete/lift overlap and direct/master kernel identity
before any outer campaign is allowed to proceed.

## Main files

- `python/coherence_lift.py` — downscale high-q odd variables, low-q completion, exact lift, Jacobian lift.
- `python/master_kernel.py` — master/direct Hermite and Mehler-kernel identities.
- `python/candidate_loader.py` — conservative loader for optional Stage15/16 normalized-u candidates.
- `python/nnqp_core.py` — NNQP wrapper/audit.
- `python/continuum_validation.py` — fixed-ridge robust high-q tail lower bound and continuum reduced-cost validation.
- `python/outer_minimax.py` — prepared-Gram coherent objective, analytic envelope gradient, multistart/local search.
- `python/run_stage27u.py` — production campaign at N=32,48,64,80.
- `python/audit_stage27u_results.py` — independent reload/recompute audit.
- `python/selftest_stage27u.py` — fast local unit tests.
- `MANIFEST.txt` — exact transfer and external-input accounting.

## Decision statuses

The production summary may report only one of:

- `COHERENT_HIGHQ_OBSTRUCTION_STRONG_NUMERIC_EVIDENCE`
- `COHERENT_SURVIVOR_FOUND` (requires a final fixed candidate with continuum-stationary validation)
- `COHERENT_OUTER_MINIMAX_UNRESOLVED`

No theorem certificate is produced by this package.
