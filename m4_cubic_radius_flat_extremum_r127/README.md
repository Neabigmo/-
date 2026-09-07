# R127 — `M=4` cubic radius and flat extremum

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（`M=4` 的 relaxed/genuine cubic radius 及其
flat extremizer）；全阶 `Gamma_M -> 0` 仍 OPEN。

## 1. 结论

令 `T_4` 是 R125 的 truncated Hamburger relaxation，令 `GammaHat_4` 是其中
`|y_3|` 的最大值；令 `Gamma_4` 是满足前四个 exact rows 的 genuine law 的 cubic
半径。则

`boxed{GammaHat_4=Gamma_4=c_4}`，

其中 `c_4=sqrt(u_4)`，`u_4` 是区间 `(1,2)` 中唯一的根

`P(u)=216u^5-1919u^4+4072u^3+4704u^2-8000u+64`，

数值为

`u_4=1.11004779030454...`,qquad `c_4=1.053588055315997...`.

与 R126 的 `M=3` ghost 端点 `sqrt(2)` 不同，`M=4` 的 extremizer 是 flat，因而
由一元 truncated Hamburger theorem 给出至多三原子的 genuine representing law。
这说明下一行 exact constraint 确实能消除 R126 的 singular non-flat ghost，并给出
第一个严格的有限阶 cubic-radius 数值。

## 2. `R_4` 的消元

前三行给出 `y_4=3`、`y_6=15+7c^2`。第四行的完整多项式为

`R_4=-(16/27)(16y_3^2+32y_3y_5-19y_4^2-24y_4-20y_6-y_8+648)`.

所以令 `a=y_5` 后，`R_4=0` 等价于

`y_8=105-124c^2+32ca`.

相关的 `H_3`、`H_4` 为

`H_3=[[1,0,1,c],[0,1,c,3],[1,c,3,a],[c,3,a,15+7c^2]]`,

`H_4=[[1,0,1,c,3],[0,1,c,3,a],[1,c,3,a,15+7c^2],
      [c,3,a,15+7c^2,b],[3,a,15+7c^2,b,y_8]]`.

## 3. 上界的 Schur-complement 证明

对 `0<=c<sqrt(2)`，固定 leading block

`H_2=[[1,0,1],[0,1,c],[1,c,3]]`

是 positive definite。对 `H_4` 关于 `H_2` 取 Schur complement，PSD 给出两个必要
条件：

`D(c,a):=-a^2+8ac-6c^4-10c^2+12 >=0`,

`N(c,a):=2a^2+18ac^3-88ac-75c^4+512c^2-48 <=0`.

第一条等价于

`a<=a_+(c):=4c+sqrt(6(2-c^2)(1+c^2))`.

在 `1<=c<sqrt(2)` 上，令
`s=sqrt(6(2-c^2)(1+c^2))`、`a_+=4c+s`。对 `a<=a_+` 有
`partial_a N<=18c^3-72c+4s<0`（例如
`18c(4-c^2)>36` 且 `4s<=4sqrt(12)<14`），故 `N(c,a)` 关于 `a`
严格递减，所以

`0>=N(c,a)>=N(c,a_+(c))=:F(c^2)`.

令 `u=c^2`，则

`F(u)=-15u^2+204u-24
      -18(4-u)sqrt(6u(2-u)(1+u))`.

有 `F(1)<0`、`F(2)=324>0`。对 `F(u)=0` 消去平方根，得到 `P(u)=0`；Sturm
计数给出 `P` 在 `(1,2)` 中恰有一个根 `u_4`。因此 `F` 在该区间只过零一次，
任何 `T_4` 可行点都满足 `c<=c_4`；`c<1` 的情形显然也不超过 `c_4`。

## 4. 极值点是 flat genuine extremizer

取 `c=c_4`、`a=a_+(c_4)`，再令

`b=(a^2c-8ac^2-18a+31c^3+42c)/(c^2-2)`.

由 `a=a_+` 得 `D(c,a)=0`，由 `F(u_4)=0` 得 `N(c,a)=0`；上述 Schur complement
的两个对角项和非对角项同时为零。因此 `H_4>=0` 且

`rank H_2=rank H_3=rank H_4=3`。

这是一条 flat truncated Hamburger sequence，一元 flat extension theorem 给出
至多三原子的 representing measure。它满足 `R_1=R_2=R_3=R_4=0`，所以
`Gamma_4>=c_4`；结合上界即得
`GammaHat_4=Gamma_4=c_4`，且 genuine supremum 在本层取得。

## 5. 路线意义

R126 的 `M=3` 端点是 non-flat ghost，不能代表概率律；R127 说明加入下一行后，
该端点不但被排除，而且新的极值落在 flat locus，ghost gap 在 `M=4` 这一层消失。
这为高阶问题提供了可检验模板：研究 `H_{M-1}` 的 Schur defect 与下一 exact row
的兼容性，而不是泛泛地要求所有 finite PSD truncations representable。

这仍不证明 `Gamma_M->0`；下一步应把这里的 `D=0/N=0` 机制推广到一般 `M`，或
证明高阶 singular kernel 的兼容性必然给出递减的 radius bound。

## 6. 本机审计

```powershell
& 'F:\anaconda3\python.exe' m4_cubic_radius_flat_extremum_r127/audit_r127.py
```

预期 marker：

```text
R127_M4_ROW_ELIMINATION_PASSED
R127_M4_SCHUR_COMPLEMENT_PASSED
R127_M4_UNIQUE_ROOT_ISOLATION_PASSED
R127_M4_FLAT_EXTREMIZER_INTERFACE_PASSED
R127_M4_CUBIC_RADIUS_CANDIDATE_CHECKED
R127_M4_CUBIC_RADIUS_AUDIT_COMPLETED
```
