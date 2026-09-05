# R32 — Normal-cone locality audit

This folder records the R32 finite-dimensional normal-cone analysis.  The
script checks:

1. the terminal odd moment is absent from `G_K` after centering, so
   `m_(2K-1)` can be moved to the boundary `beta_K=0` without changing the
   fixed-head objective or the exact rows;
2. terminal KKT stationarity forces the artificial terminal multiplier to be
   zero;
3. scalar Jacobi and PSD complementarity cannot produce a positive value term;
4. the fixed-rank finite-support contradiction underlying active-rank escape;
5. the Gaussian-shadow Jacobi growth normalization and the geometric weighted
   Cauchy bound that would suppress remote shadow debt.

Run with:

```text
F:\anaconda3\python.exe -u flat_shadow_normal_cone_r32\audit_r32.py
```

Expected output:

```text
R32_ACTIVE_RANK_ESCAPE PASSED
R32_LOCAL_NORMAL_CONE_VALUE_COMPLETION NO_GO
R32_REMOTE_EQUALITY_COSTATE LOCALITY REMAINS OPEN
R32_AUDIT_COMPLETED
```

The finite `K` viable set is compact under the recorded even-moment bounds,
PSD moment constraints, and a fixed nondegenerate flat window; continuity of
`q_M` therefore gives a worst-case extremizer.  If a bad sequence had a fixed
singular forward Hankel rank, diagonal extraction plus the moment growth bound
would give a Carleman-determinate full-exact law with a finite-support one-body
law, hence finite-support `Q`, contradicting `Q~chi^2_2`.  Thus active forward
ranks escape to infinity, and in fact each fixed rank has a uniform positive
margin along sufficiently deep viable prefixes.

This does not bound the normal multipliers.  At a terminally forced active
face, stationarity gives multiplier zero; at any active Jacobi/PSD face,
complementarity gives `eta_j beta_j=0` or `<Z,H>=0`.  Hence local KKT/normal-cone
objects cancel gradients but cannot themselves supply the positive value budget
`P_K`.  Inactive constraints have zero multiplier.  A Gaussian-shadow estimate
and an exponentially weighted multiplier tail would suppress shadow debt, but
the missing bound is precisely the remote equality-costate locality.

The local mechanism is therefore a strict proof-route no-go, not a
full-exact counterexample.  The remaining OPEN target is a global value-level
identity that moves the low equality costate to remote Hermite degrees with a
law-independent weighted bound.  No optimizer, SDP, remote sweep, or `P_3K`
bridge is used; Gaussian rigidity remains OPEN.
