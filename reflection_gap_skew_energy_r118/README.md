# R118 — Reflection-Gap Skew Energy 与 Mixed-Reflection Moment

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（待本机 audit）；CONDITIONAL；FORMAL；核心 OPEN。

## 1. 目标

承接 R117 的一维 heat-escort barycenter。令 `u_t=P_t f`，
`check u_t(x)=u_t(-x)`，并分解

`e_t=(u_t+check u_t)/2`,  `o_t=(u_t-check u_t)/2`。

`e_t` 为偶部、`o_t` 为奇部；在 `t>0` 且 `f` 为概率密度时二者满足
`e_t>0`、`|o_t|<e_t`。

## 2. Reflection polarization：一个非负全局 gap（PROVED）

定义

`C(t)=int u_t(x)^2 check u_t(x) dx`,
`D(t)=int u_t^3-C(t)`。

直接展开：

`boxed{D(t)=4 int e_t o_t^2`
`= (1/2) int (u_t+check u_t)(u_t-check u_t)^2 >=0.}`

Hölder 给 `C(t)<=int u_t^3`；等号对任意一个 `t>0` 当且仅当
`u_t=check u_t`。Gaussian convolution 的 Fourier multiplier 无零点，所以
这等价于 `f=check f`，从而 `kappa_3(f)=0`。因此

`D(t)=0 for one t>0 => f symmetric => kappa_3(f)=0`。

这是 genuine global equality mechanism；Gaussian/symmetric state 在这个 gap 上
确实位于 boundary，与 R109–R117 ordinary Gram/heat overlap 的 strict interior
现象不同。

## 3. Mixed-reflection Laplace order（PROVED）

取 `Y_1=X_1,Y_2=X_2,Y_3=-X_3`，令

`Qsharp=sum_j(Y_j-Ybar)^2`。

同一 Gaussian completion 应用于 `u_t^2 check u_t`，给出

`C(t)=1/(2*pi*t*sqrt(3)) E exp(-Qsharp/(2t))`。

R117 exactness 给
`int u_t^3=1/(2*pi*t*sqrt(3))*t/(1+t)`，所以

`boxed{D(t)=1/(2*pi*t*sqrt(3))`
`*[t/(1+t)-E exp(-Qsharp/(2t))].}`

结合 `D>=0`，得到对所有 `t>0` 的 global order

`boxed{E exp(-Qsharp/(2t)) <= t/(1+t)=E exp(-Q/(2t)).}`

这是首次在同因子/reflection structure 下得到没有 phase cancellation 的单边
sample-variance comparison。

## 4. Barycenter 被正 gap 控制（PROVED）

写 `h_t=o_t/e_t`，则 `|h_t|<1`，且 parity 给

`B(t)=int x u_t(x)^3 dx=int x e_t^3(3h_t+h_t^3)dx`。

用 `|3h+h^3|<=4|h|`、Cauchy 与 `int e_t^3h_t^2=D(t)/4`：

`boxed{B(t)^2 <=4D(t) int x^2e_t(x)^3dx.}`

因 `e_t<= (2*pi*t)^(-1/2)`、`int x^2e_t=1+t`，有

`int x^2e_t^3 <=(1+t)/(2*pi*t)`，从而

`boxed{B(t)^2 <=2(1+t)/(pi*t) D(t).}`

所以 sufficient condition 是

`D(t)=o(t^(-4)) => B(t)=o(t^(-2)) => kappa_3(f)=0`。

## 5. Positive skew-energy 的精确 cubic coefficient（PROVED / ANALYTICALLY PROVED）

在 R117 exact class 中
`m_4=3`、`m_6=15+7*kappa_3^2`。直接 iid moment algebra 对 `Qsharp` 给

`E Qsharp=2`,  `E(Qsharp)^2=8`,

`boxed{E(Qsharp)^3=48+(224/27)kappa_3^2.}`

而 `Q~chi^2_2` 有 `EQ=2`、`EQ^2=8`、`EQ^3=48`。令 `lambda=1/(2t)`，则

`E exp(-lambda Q)-E exp(-lambda Qsharp)`
`=(112/81)kappa_3^2 lambda^3+O(lambda^4)`。

代回 gap：

`boxed{D(t)=7/(81*pi*sqrt(3))*kappa_3^2*t^(-4)+O(t^(-5)).}`

因此

`boxed{lim_(t->infty) t^4D(t)=7/(81*pi*sqrt(3))*kappa_3^2}`，

即在 R117 class 中
`D(t)=o(t^(-4)) iff kappa_3=0`。

若 `kappa_3!=0`，它还与 R117 的 barycenter asymptotic 精确匹配：

`B(t)=-kappa_3/(6*pi*sqrt(3))*t^(-2)+O(t^(-3))`,

故

`boxed{D(t)/B(t)^2 ->28*pi/(3*sqrt(3)).}`

这使 `D` 成为 `B^2` 的正 global surrogate；但它没有自动比自然 `t^(-4)` 多
衰减一阶。

## 6. 为什么现有 total positivity / rearrangement 仍不够（OBSTRUCTION）

Heat kernel 的 strict total positivity 可以控制 odd sign changes；但 cubic odd
heat mode 允许

`u_t-check u_t=O(kappa_3*t^(-2))`,
`D(t) asymp kappa_3^2*t^(-4)`。

所以 variation-diminishing 的自然 rate 正好容纳非零 cubic skew，不能自动给
`o(t^(-4))`。

另一方面 exactness 固定的是 `A(t)=int u_t^3`，而

`A(t)=int e_t^3+3 int e_to_t^2`

只表达“symmetric deficit + odd positive energy = 0”；非零 odd component 可以
由降低 `int e_t^3` 来补偿。故 zeroth overlap rearrangement 仍碰不到 barycenter。

## 7. Reflection-mixture polarization（PROVED）

定义概率插值

`f_lambda=((1+lambda)/2)f+((1-lambda)/2)check f`,  `-1<=lambda<=1`。

则 `P_t f_lambda=e_t+lambda o_t`，且

`boxed{int(P_t f_lambda)^3`
`= A_G(t)-3/4(1-lambda^2)D(t).}`

其中 `A_G(t)=1/(2*pi*sqrt(3)*(1+t))` 在 exact branch。故两个 exact
asymmetric endpoints `lambda=+-1` 是这条 reflection-mixture path 的 overlap
最大值，symmetric midpoint `lambda=0` 低出恰好 `3D/4`。这是漂亮的 global
polarization identity，同时说明简单的“对称化改变 overlap”不能单独结束主问题。

## 8. Conditional lemma 与下一轮

若在 R117 genuine same-factor exact class 之外，再能证明

`t/(1+t)-E exp(-Qsharp/(2t))=o(t^(-3))`,

则 `D=o(t^(-4))`，从而 `kappa_3=0`。等价地，只需获得 opposite third-moment
comparison

`boxed{E(Qsharp)^3<=48}`。

但当前 reflection/Hölder 结构给出的自然方向正是
`E(Qsharp)^3>=48`，差额为 `(224/27)kappa_3^2`；这不是所需的反向比较。

因此 R118 判决仍为 OPEN：

`same-factor three-line convolution + Gaussian radial exactness`
`=> B(t)=o(t^(-2)) <=> kappa_3(f)=0`。

### R119 最小命题

研究 **Mixed-Reflection Third-Moment Reversal**：在 genuine full-exact class 中，
能否从除 reflection/Hölder 外的 global same-factor structure 得到

`E(Qsharp)^3<=48`

或至少使 Laplace gap 为 `o(lambda^3)`。若证明 standard rearrangement/total
positivity 不可能给出此 opposite comparison，则转向 R117 的 conditional-mean
diagonal transform `E[Xbar J_0(rho sqrt(Q))]`。

## 9. 证据等级

`audit_r118.py` 只核验 reflection polynomial identities、Gaussian completion
系数、barycenter bound 的常数、mixed-sign sample-variance 的前三阶矩、Laplace
与 `D/B^2` leading coefficient、以及 mixture polarization。total-positivity
decay、moment remainder 与 same-factor annihilation仍按 ANALYTICALLY PROVED /
CONDITIONAL / OPEN 记录。
