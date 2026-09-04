# R18 — theory-only Laguerre–Abel endpoint audit

This branch implements the next focused theory task from ChatGPT. It proves
the exact `Exp(1)` Laguerre Abel transform, its positive quadratic form, and a
finite exact endpoint non-coercivity witness. It also records that the current
R17 materials contain only `d0`–`d3`, so a full Fock formula for `D(r)` is not
available to derive honestly.

Run:

```text
F:/anaconda3/python.exe laguerre_abel_endpoint_r18/audit_r18.py
```

No optimizer, numerical search, Gram campaign, order-8 campaign, remote
compute, or long-running task is used.

The machine-readable report is `results/r18_audit.json`.
