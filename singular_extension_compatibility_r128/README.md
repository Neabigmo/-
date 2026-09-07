# R128 — Singular extension compatibility and the next exact row

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED for the extension lemma, the `R_5`
elimination formula, and the strict finite-level drop `GammaHat_5<GammaHat_4`;
the global decay `Gamma_M -> 0` remains OPEN.

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

## 4. Strict drop at the next layer

The R127 equality conditions are rigid. If a feasible `M=5` point had
`c=c_4`, its `M=4` projection would attain the R127 maximum, hence necessarily

`a=a_+(c_4)`,

`b=(a^2c-8ac^2-18a+31c^3+42c)/(c^2-2)`.

Substituting these values into the R5 elimination gives

`y_10 = N(u)/(u-2)`, `u=c_4^2`,

where, with `s=sqrt(6(2-u)(1+u))`,

`N(u)=-666u^3+1044u^2-6307u+13766
      -216 sqrt(u) s (2u+1)`.

The R127 root is uniquely isolated by `1.11<u<1.12`. On this interval the first
four terms are strictly larger than `7000`, while the final positive magnitude
is strictly smaller than `2500`; hence `N(u)>4500`. Since `u-2<0`, this proves
`y_10<0`. But `H_5>=0` requires its last diagonal entry `y_10>=0`, a contradiction.

Using the finite-row moment caps from R124/R125 for compactness, equality
`GammaHat_5=GammaHat_4` would have a maximizer and the preceding contradiction
applies. Therefore

`boxed{GammaHat_5 < GammaHat_4 = c_4}`,

and consequently `Gamma_5<=GammaHat_5<c_4`. This is a rigorous finite-level
strict-decrease theorem, not a numerical estimate of `GammaHat_5`; the exact
M=5 value and an asymptotic rate remain OPEN.

## 5. Consequence for the R128 program

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

## 6. Labels and next webpage task

- **PROVED:** singular PSD extension compatibility; generalized Schur defect;
  exact `R_5` polynomial and triangular elimination; strict drop
  `GammaHat_5<GammaHat_4=c_4`.
- **AUDITED INTERVAL STEP:** the R127 extremizer forces `y_10<0` under `R_5`.
- **OPEN:** an explicit `Gamma_5`, a monotone decay estimate, and the all-order
  implication `Gamma_M -> 0`.

The next theoretical target is therefore a genuine `M=5` singular/flat split,
with every compatibility equation audited before any numerical optimization.
