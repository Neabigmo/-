# R27 proof-level audit

This audit checks the new residual Gram reduction and the first-order
covariance-completion no-go while keeping the full-exact theorem open.

## Checked

1. For `F_i=(X_i-bar X)P_M(X_i)` and the flat null relations,
   `L^3(F_i F_j)=(4q_M/9) delta_ij`.
2. The matrix heat product identity gives
   `A=E+(4q_M/9)I_3`, where `A` is the forward-probability Gram matrix and
   `E` is the derivative/noise Gram matrix.  The audit also checks the
   antisymmetric vector `c=(1,-1,0)/sqrt(2)`.
3. The explicit residual factorization
   `F_1-F_2=(X_1-X_2)H_P` is verified symbolically.
4. If an independent residual source has covariance
   `C_perp=t diag(r_1,r_2)` with `0<=r_i<=1`, then the flat-jet coefficient is
   `q_M t(r_1+r_2-2)/2<=0`; the maximal completion `r_1=r_2=1` gives exactly
   zero, never the required positive coefficient.

The seed moments are the previously recorded finite-prefix algebraic seed.
They are used only to test identities; no finite-prefix object is treated as a
genuine full-exact counterexample.

## Logical status

The matrix identity yields the narrower conditional target
`A_->=E_-` for one antisymmetric residual mode, which would imply `q_M>=0`.
The covariance-budget calculation rules out adding more independent positive
real residual noise as the missing mechanism.  A successful proof must instead
construct a genuine same-factor conditional residual-jet contraction handling
the common coordinate `U`; R18 sectorwise PSD and R21 pure-residual rotation do
not yet provide that contraction.  `P_3K` and Gaussian rigidity remain
logically disconnected/open.

Run:

```powershell
& 'F:\anaconda3\python.exe' flat_null_square_r27/audit_r27.py
```

Expected marker: `R27_AUDIT_COMPLETED`.
