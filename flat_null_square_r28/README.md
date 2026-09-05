# R28 proof-level audit

This audit records the new flat-shadow reduction while keeping the genuine
full-exact Gaussian-rigidity problem open.

## Checked

1. For an atomic shadow `nu` supported on the zeros of `P`, the forward image
   `rho=P_a nu` satisfies the exact operator identity
   `E[G_-(Y+sqrt(a)Z)|Y]=F_-(Y)=0`.  Consequently the inverse derivative
   energy is the conditional variance under a genuine positive shadow law.
2. The same-factor heat algebra is checked symbolically:
   `R=P_(-a)P`, `W=P_(-a)(xP)=xR-aR'`, and
   `G_i=(2/3)W_i-(1/3)(X_j+X_k)R_i`.
3. For a centered unit-variance product law with the relevant null means, the
   antisymmetric Hoeffding decomposition is checked:
   `E G_-^2=(4/9)E W^2+(2/9)E R^2-(1/9)(E[XR])^2`.
   The one-body and degenerate two-body sectors are symbolically orthogonal.
4. If the full law and its positive flat shadow match moments through
   `2M+1`, then `R^2`, `XR`, and all derivative/noise terms have matched
   expectations.  The only remaining difference is the one-body first-order
   norm, with `E_mu W^2-E_rho W^2=q_M` under the support/null-square premise.
5. The pair-sum coordinate identity
   `Q=D^2/2+(S-2Y)^2/6` is verified.  The exact radial law therefore supplies
   only a weighted scalar conditional Laplace average, not a conditional
   Loewner order.

The formal moment vector in item 4 and the toy atomic/normal laws in items 1–3
are algebraic audit devices only.  They are not full-exact counterexamples and
do not prove the remaining one-body inequality.

## Logical status

R28 gives a full-exact-compatible route no-go: any proof that extracts gain
only from the residual two-body/conditional Schur sector cannot change the
sign, because that sector cancels exactly between the full law and its positive
flat shadow.  The remaining open target is
`||P_(-a)(xP_M)||_{L^2(mu)} >= ||P_(-a)(xP_M)||_{L^2(rho_M)}`
or the equivalent uniform flat-shadow overshoot modulus decay `Omega_K -> 0`.
This still feeds the Gaussian-rigidity route, while `P_3K` remains logically
disconnected.

Run:

```powershell
& 'F:\anaconda3\python.exe' flat_null_square_r28/audit_r28.py
```

Expected marker: `R28_AUDIT_COMPLETED`.
