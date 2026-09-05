# R26 proof-level audit

This audit records the new reductions from the R26 web-side analysis while
preserving the distinction between identities, conditional positivity, and
the unresolved full-exact theorem.

## Checked

1. Completing the square gives
   `A_t^mu(y)=(1+at)^(-1/2) exp(ay^2/[2(1+at)])
   L(exp(sX-uX^2/2))`, with `s=y/(1+at)` and `u=t/(1+at)`.  The transported
   polynomial `p_(t,y)(z)=P((1+at)z-ay)` pulls back to `P(X)` at the formal
   latent coordinate `z=(X+ay)/(1+at)`.
2. Under the flat relations `L(P^2)=L(XP^2)=0` and
   `L(X^2P^2)=q_M`, the parabolic jet is
   `L(exp(sX-uX^2/2)P^2)=q_M(s^2-u)/2
   +O(|s|^3+|s|u+u^2)`.
3. With the genuine three-copy escort variance
   `E[Y^2]=t/3+O(t^2)`, the displayed leading jet has coefficient
   `-q_M/3` after division by `t`.  Hence common-shift scalar HS averaging has
   the wrong first-order orientation for proving `q_M>=0`.
4. The polynomial heat identity
   `P_a((P_-a F)^2)=sum_alpha a^|alpha|/alpha! (partial^alpha F)^2`
   and the explicit formula
   `P_-a[(X_i-bar X)P(X_i)] =
   (X_i-bar X) P_hat(X_i)-(2a/3)P_hat'(X_i)`
   were checked symbolically.  Combining this with the R25 residual identity
   gives the algebraic decomposition
   `A_M=4q_M/3+E_M`.

## Logical status

The decomposition is not a sign proof.  `A_M>=0` is forward probability
positivity, while `E_M>=0` follows conditionally when the inverse moment block
`H_M(L)` is positive semidefinite, because every nonzero derivative has degree
at most `M` in each one-body coordinate.  Neither fact implies the required
domination `A_M>=E_M`.

The R26 obstruction is therefore proof-level and full-exact compatible:
ordinary raw conditional PSD, pointwise `Psi_M>=0`, and common-only HS averaging
do not supply the missing residual correction.  The remaining minimum OPEN is
`Residual-Corrected Flat Null-Square Hardy Gain`: prove/refute
`A_M>=E_M`, or equivalently establish the needed special-cone inverse positivity
with a genuinely common--residual coherence estimate.  `P_3K` remains
logically disconnected and Gaussian rigidity remains OPEN.

Run with the SymPy-enabled local interpreter:

```powershell
& 'F:\anaconda3\python.exe' flat_null_square_r26/audit_r26.py
```

Expected marker: `R26_AUDIT_COMPLETED`.
