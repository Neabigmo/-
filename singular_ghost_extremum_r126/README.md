# R126 — Singular Ghost at the Cubic Extremum (the exact `M=3` layer)

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（`M=3` 的 relaxed radius、ghost 极值、genuine
supremum 的 non-attainment）；核心全阶问题仍 OPEN。

## 1. 结论

令 `y_k=E[X^k]`，并令 `E_3` 是 centered、variance-one probability laws，满足前三
个 circular exact rows。令 `T_3` 是 R125 的 truncated Hamburger relaxation，并写

`Gamma_3 = sup_{mu in E_3} |y_3|`,

`GammaHat_3 = max_{y in T_3} |y_3|`.

则

`boxed{GammaHat_3 = Gamma_3 = sqrt(2)}`.

但是两者的 attainment 完全不同：`GammaHat_3` 的端点 maximizer 是 singular
non-flat ghost；`Gamma_3` 的值只是一个不取得的 genuine supremum。

这给出了 R125 所说 finite ghost gap 的明确 `M=3` 实例，并且说明不能把
finite-level relaxed maximizer 自动当作 genuine extremizer。

## 2. 前三行的精确消元

对

`Q=(2/3)(sum_i X_i^2-sum_{i<j}X_iX_j)`

和 iid centered variance-one copies，有

`R_1=0`,

`R_2=(4/3)(y_4-3)`,

`R_3=(8/9)(y_6-7y_3^2+12y_4-51)`.

故 exact rows `R_2=R_3=0` 等价于

`y_4=3`,qquad `y_6=15+7c^2`,

其中 `c=y_3`。取 `y_5=4c`，相应的三阶 Hankel 矩阵为

`H_3(c)=[[1,0,1,c],[0,1,c,3],[1,c,3,4c],[c,3,4c,15+7c^2]]`.

其 leading `H_2` 的行列式是

`det H_2=2-c^2`.

所以任何 PSD truncation 都满足 `|c|<=sqrt(2)`。

## 3. 端点是 singular non-flat ghost

在 `c=sqrt(2)`，取

`y=(1,0,1,sqrt(2),3,4sqrt(2),29)`.

此时 `H_3` PSD，`rank(H_2)=2`，`rank(H_3)=3`，即

`H_3` singular 且 `rank(H_3)>rank(H_2)`。

`H_2` 的 kernel 含向量 `(-1,-sqrt(2),1)`。若该 truncation 有 representing law，
则

`X^2-sqrt(2)X-1=0` almost surely.

递推 `X^2=sqrt(2)X+1` 给出 `y_6=4c^2+3=11`，而 exact `R_3=0` 要求
`y_6=29`，矛盾。因此端点不是 genuine law，而是一个 singular non-flat ghost。

端点的 PSD 由 principal minors 直接核验；例如非零三阶 minor 包含
`det H_{\{0,1,3\}}=18`，而 `det H_3=0`。

## 4. genuine 半径的逼近但不取得

对任意 `|c|<sqrt(2)`，仍取 `y_5=4c`、`y_6=15+7c^2`。令 `u=c^2`，`H_3(c)` 的
关键 principal minors 为

`2-u`, `6(1+u)`, `30+3u`, `18+14u-7u^2`,
`6(2-u)(1+u)`,

其余一阶、二阶 minors 也严格为正；因而 `H_3(c)` positive definite。

一元 truncated Hamburger theorem 将这个正定截断提升为 representing probability
measure。该 measure 的 moments `0,...,6` 正好满足 centered/variance-one、`R_2=R_3=0`
以及所有 `T_3` 的 even caps。因此 `Gamma_3>=|c|` 对所有 `|c|<sqrt(2)`；结合
`H_2>=0` 的上界，得到 `Gamma_3=sqrt(2)`，但端点的 ghost 论证说明 genuine
supremum 不取得。

## 5. 对全局路线的意义

这是一个局部但严格的 R126 结论：

1. finite relaxed maximizer 的 singular non-flat 分支确实会出现，不是技术性空警告；
2. 在这个例子中 ghost gap 的数值并不来自 relaxed radius 大于 genuine radius，
   而来自 genuine supremum 不 attainment；
3. 因而 R125 的渐近 squeeze 必须使用 `M->infty` 的 compactness，而不能在单个
   finite layer 直接调用 finite atomic representation；
4. 下一步不是重复 `M=3`，而是研究高阶 maximizer 的 singular kernel 是否能被下一行
   exact constraint 强制破坏，以及这种破坏能否给出 `GammaHat_M` 的定量衰减。

本包没有声称 `Gamma_M->0`，也没有把这个有限层例子误报为主 cubic exclusion。

## 6. 本机审计

使用：

```powershell
& 'F:\anaconda3\python.exe' singular_ghost_extremum_r126/audit_r126.py
```

预期 marker：

```text
R126_M3_ROW_ELIMINATION_PASSED
R126_M3_RELAXED_RADIUS_SQRT2_PASSED
R126_M3_PD_APPROACHING_FAMILY_PASSED
R126_M3_GHOST_NONFLAT_PASSED
R126_M3_ENDPOINT_NONREPRESENTABLE_PASSED
R126_M3_GENUINE_SUPREMUM_NOT_ATTAINED
R126_SINGULAR_GHOST_EXTREMUM_AUDIT_COMPLETED
```
