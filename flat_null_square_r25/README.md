# R25 proof-level audit

This audit checks the new reductions from the web-side R25 analysis while
preserving the distinction between local algebra and the unresolved
full-exact theorem.

## Checked

1. If `D_(M+1)=D_M h_(M+1)` on the quasi-definite side and
   `D_M(a_*)=0`, `h_(M+1)(a_*)=q_M`, then
   `D_(M+1)'(a_*)=q_M D_M'(a_*)`.  Since `D_M'(a_*)<0`, this is equivalent to
   `q_M>=0` iff `D_(M+1)'(a_*)<=0`.
2. From `L(P_M^2)=L(xP_M^2)=0`, every constant shift satisfies
   `L((x-c)^2P_M^2)=q_M`.  Independence then gives
   `q_M=(3/4)L^3(sum_i (X_i-bar X)^2P_M(X_i)^2)`.
3. Integrating the two heat-Hankel derivative inequalities gives
   `-q_M >= M^2(M+1)^2 h_(M-1)(a_*) (g_M-g_(M+1))^2/2`.
4. The monotonicity `Omega_(K+1)<=Omega_K` follows from nested
   finite-prefix classes.

## Conditional compactness note

Fix a parameter window for `a_*` and a positive lower-block margin.  If the
finite-prefix classes share the genuine exact-law square-exponential bound,
then a sequence with `Omega_K` bounded below has a tight subsequence with
uniform integrability of every fixed polynomial.  The limit preserves all
`Q`-moment equations, the inverse finite Hankel data, `ell_M=0`, and the
negative `q_M` margin.  Moment determinacy of `chi^2_2` then produces a
genuine full-exact bad boundary.  Conversely, a genuine bad boundary belongs
to every finite-prefix class.

Thus, under those uniformity and nondegeneracy assumptions, `Omega_K -> 0`
is equivalent to exclusion of a full-exact bad boundary in that local window.
The audit does not prove `Omega_K -> 0`; establishing that modulus is the
remaining infinite-tail problem.  Finite-prefix overshoot constructions do
not contradict this conditional compactness formulation.

Run:

```powershell
python flat_null_square_r25/audit_r25.py
```

Expected marker: `R25_AUDIT_COMPLETED`.
