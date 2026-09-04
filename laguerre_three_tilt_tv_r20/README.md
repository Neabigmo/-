# R20 — theory-only three-tilt audit

This package contains no optimizer, numerical campaign, remote computation,
or high-order search.  It checks the proposed variance gate symbolically and
records the precise limitation.

Run:

```text
F:\anaconda3\python.exe replay_r20.py
F:\anaconda3\python.exe audit_r20.py
```

Expected markers:

```text
R20_FORCED_H4 0
R20_COMPATIBLE_H6 -3*h3**2/20
R20_LAPLACIAN_AVERAGED_LEADING ...
R20_RADEMACHER_TV_GAP ...
R20_CIRCLE_IDENTITY_JET_AUDIT_COMPLETED
R20_TV_NOT_CERTIFIED
```

The result is intentionally conservative: the formal jet is not an actual
probability-law counterexample.  It only blocks the proposed proof from using
the circle-average identity alone.
