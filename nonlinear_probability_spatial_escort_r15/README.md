# R15 — nonlinear probability / spatial escort audit

This branch audits the probability-side bridge from the exact Fock identity
to a nonlinear spatial-escort hierarchy. It is a small exact/symbolic audit:
no optimizer, Gram campaign, remote computation, or higher-order expansion.

The result is conservative: the common-shift and order 2/4/6 identities are
exact, but the order-six positive square is accompanied by signed terms.
Therefore Gaussian rigidity is not claimed.

Run:

    python audit_r15.py
    pytest -q

