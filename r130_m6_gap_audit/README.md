# R130 — Explicit M=6 relaxed-radius gap certificate

日期：2026-09-08

状态：`ANALYTICALLY PROVED` by the exact rational-box certificate in
`audit_r130.py`.  The result is a finite relaxed bound; it is not an explicit
value of `GammaHat_6` and it does not by itself address the positive
backward-OU tower.

## 1. New finite-level result

With the project normalization and the R125 truncated-Hamburger feasible set,
the exact R2--R6 rows and `H_6>=0` imply

`|c|<=1.0535`, hence

`GammaHat_6<=1.0535`.

R127's exact-root interval gives `1.05358<c_4<1.05359`, so the explicit gap is

`c_4-GammaHat_6>0.00008`.

The decimal is only a convenient rational endpoint: the proof uses the exact
inequality `c_4>105358/100000` and the rational upper bound
`GammaHat_6<=10535/10000`.

## 2. Exact proof chain

It is enough to treat `c>=0`, by reflection.  R127 already gives the global
upper bound `c<=c_4`; the Sturm/root-count certificate in this round refines
it to the window

`10535/10000 <= c <= 105359/100000`.

Write `a=y_5`, `b=y_7`.  The R127 H4 Schur inequalities are

`D=-a^2+8ac-6c^4-10c^2+12>=0`,

`N=2a^2+18ac^3-88ac-75c^4+512c^2-48<=0`.

Exact rational interval arithmetic proves throughout this window that

`75698/10000<a<7571/1000`,

and that the corresponding H4 Schur entries satisfy

`0<=S_00=D/(2-c^2)<1/100`,

`0<=S_11=-N/(2-c^2)<1/16`.

The off-diagonal H4 Schur entry is exactly `S_01=b-b_*(c,a)`, where

`b_*=(a^2c-8ac^2-18a+31c^3+42c)/(c^2-2)`.

The same rational interval certificate gives

`70.29<b_*<70.4`.

Since H4 PSD implies `S_01^2<=S_00 S_11`, one obtains

`70.2<b<70.5`.

Now take the H6 Schur complement relative to the positive-definite H2.  Its
entry coupling the old `xp` kernel direction to the new column is the R129
residual

`r_1=S_13`

and exact interval arithmetic on the above box gives `r_1>800`.  PSD of the
corresponding 2x2 principal submatrix forces

`r_1^2<=S_11 S_33`.

But the bottom Schur entry satisfies `S_33<=y_12`, while the T6 moment cap gives

`0<=y_12<=4^6 6!=2,949,120`.

Therefore

`r_1^2>800^2=640,000`,

whereas

`S_11 S_33 < (1/16)(2,949,120)=184,320`,

a contradiction.  Thus no H6-feasible point lies in the stated c-window.

## 3. Evidence and limits

The script uses exact rational polynomial interval arithmetic and exact
Sturm root counts/sign evaluations.  It emits:

`R130_C4_ROOT_INTERVAL_PASSED`

`R130_H4_PARAMETER_BOX_PASSED`

`R130_BSTAR_INTERVAL_CERTIFICATE_PASSED`

`R130_R1_LOWER_BOUND_CERTIFICATE_PASSED`

`R130_M6_SCHUR_IDENTITIES_PASSED`

`R130_M6_SCHUR_2X2_CONTRADICTION_PASSED`

`R130_M6_EXPLICIT_GAP_CERTIFICATE_PASSED`

The result is `ANALYTICALLY PROVED` for the relaxed finite radius.  The exact
value of `GammaHat_6`, the genuine `Gamma_6`, all-order decay, and the
positive/backward-OU exact-zero-set rigidity remain `OPEN`.

Audit command:

`F:\\anaconda3\\python.exe r130_m6_gap_audit\\audit_r130.py`
