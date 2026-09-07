# R128 — Singular extension compatibility and the next exact row

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED for the extension lemma and the `R_5`
elimination formula; the global decay `Gamma_M -> 0` remains OPEN.

## 1. Why this is the correct next interface

R126 showed that the relaxed `M=3` cubic extremum can be a singular non-flat
Hamburger ghost. R127 showed that adding `R_4=0` forces a different extremum,
which is flat and genuine. The reusable mechanism is not a particular low-order
determinant: whenever a singular moment matrix is extended, every old kernel
polynomial must remain orthogonal to the new column. The next exact row then has
to be tested against this compatibility equation.

## 2. Singular extension lemma

Let

`H_M=(y_{i+j})_{0<=i,j<=M} >= 0`,

and let `p=(p_0,...,p_M)^T` belong to `ker H_M`. For an extension

`H_{M+1}=[[H_M,b],[b^T,y_{2M+2}]] >= 0`,

where `b=(y_{M+1},...,y_{2M+1})^T`, positivity gives

`H_{M+1}(p,0)^T=0`.

Consequently the exact compatibility condition is

`sum_{i=0}^M p_i y_{M+1+i}=0` for every `p in ker H_M`. Equivalently,
`b in Ran(H_M)`. In that case the generalized Schur defect is

`delta_{M+1}=y_{2M+2}-b^T H_M^+ b >= 0`.

`delta_{M+1}=0` is the flat extension case; `delta_{M+1}>0` is the only possible
one-step singular non-flat ghost direction. This statement is an unconditional
PSD lemma and does not invoke a representing measure.

## 3. Exact `R_5` row

For `Q=sum_{j=1}^3 (X_j-Xbar)^2`, independent centered variance-one copies, the
fifth radial exact row is

`E Q^5 - 2^5 5! = 0`,

with

`E Q^5 = 3 y_10 - 360 y_3 y_5 - 180 y_3 y_7
          + 225 y_4^2 + 270 y_4 y_6 - 153 y_5^2
          + 180 y_6 + 90 y_8`.

Thus

`y_10 = 120 y_3 y_5 + 60 y_3 y_7 - 75 y_4^2 - 90 y_4 y_6
        + 51 y_5^2 - 60 y_6 - 30 y_8 + 1280`.

This is the exact next-row input for an `M=5` audit. It is triangular in the new
top moment, but it does not by itself imply positivity or flatness.

## 4. Consequence for the R128 program

At a candidate singular maximizer of `T_M`, the next round must proceed in this
order:

1. compute `ker H_M` and impose `b in Ran(H_M)`;
2. substitute the exact row `R_{M+1}=0`;
3. analyze the remaining scalar/generalized-Schur defect;
4. distinguish a flat genuine extremizer from a positive singular ghost.

For `M=5`, the new row is the formula above. A high-precision diagnostic already
shows that the particular flat `M=4` extremizer from R127 does not automatically
survive `R_5`; this is recorded only as a diagnostic until an interval-certified
sign proof is added. The rigorous R128 result is the singular compatibility lemma
and the exact `R_5` interface, not a claimed value of `Gamma_5`.

## 5. Labels and next webpage task

- **PROVED:** singular PSD extension compatibility; generalized Schur defect;
  exact `R_5` polynomial and triangular elimination.
- **DIAGNOSTIC:** R127 flat extremizer tested against the `R_5` recurrence.
- **OPEN:** an explicit `Gamma_5`, a monotone decay estimate, and the all-order
  implication `Gamma_M -> 0`.

The next theoretical target is therefore a genuine `M=5` singular/flat split,
with every compatibility equation audited before any numerical optimization.
