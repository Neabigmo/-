# R117 — Cubic Heat-Norm Equivalence 与 Heat-Escort Barycenter

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（全局等价与提取器，待本机 audit）；
OBSTRUCTION；核心 OPEN。

## 1. 目标

承接 R116 的 same-factor three-line convolution 问题。取 centered
variance-one density `f`，令 `u_t=P_t f=f*gamma_t`，其中 `gamma_t` 是方差
`t` 的一维 Gaussian。设 `X_1,X_2,X_3` iid、

`Q=sum_j (X_j-Xbar)^2`。

本轮不再直接追逐二维角相位，而是把 radial exactness 变成一条一维 heat-flow
恒等式，再寻找对 cubic skew 敏感的全局 observable。

## 2. 新的小里程碑：Cubic Heat-Norm Equivalence（PROVED）

Gaussian completion 给出

`int_R (P_t f)^3 dx`
`= (1/(2*pi*t*sqrt(3))) E exp(-Q/(2t)).`

因此

`Q~chi^2_2`

当且仅当对所有 `t>0`

`boxed{ int_R (P_t f)^3 dx = 1/(2*pi*sqrt(3)*(1+t)) }`

即

`boxed{ Q~chi^2_2 iff ||P_t f||_3^3=||gamma_(1+t)||_3^3 for every t>0. }`

反向使用正半轴 Laplace transform 的唯一性。这是 genuine global、非 finite-jet
的等价改写：径向 exactness 被压缩成整条正 heat curve。

## 3. Heat curvature identity 与其缺口（PROVED / OBSTRUCTION）

令

`A(t)=int u_t^3`,  `I(t)=int u_t(u_t')^2`,
`J(t)=int u_t(u_t'')^2`。

由 `partial_t u_t=(1/2)u_t''` 和积分分部：

`A'=-3I`,  `I'=-J`。

在 exact branch `A=C/(1+t)`、`C=1/(2*pi*sqrt(3))`，所以

`I=C/(3(1+t)^2)`,  `J=2C/(3(1+t)^3)`,

并得到

`boxed{ A J = 6 I^2 }`。

一般正密度只由 Cauchy–Schwarz 得

`I=-(1/2)int u^2u''`,  `A J >= 4 I^2`。

因此 exact value `6` 位于基础 positivity cone 的内部，而不是 equality boundary；
单靠 Cauchy、基础 Fisher positivity 或 zeroth-overlap rearrangement 不能给出
Gaussian equality-case rigidity。这与 R109–R116 的 strict-interior 障碍同源。

## 4. Cubic Heat-Escort Barycenter Extractor（PROVED）

定义 tilted cubic heat integral

`A_t(lambda)=int exp(lambda y)u_t(y)^3dy`。

三 Gaussian 的精确 completion 给

`A_t(lambda)=exp(lambda^2 t/6)/(2*pi*t*sqrt(3))`
` * E[ exp(lambda Xbar) exp(-Q/(2t)) ].`

令

`B(t)=int y(P_t f(y))^3dy`。

在 `lambda=0` 求导：

`B(t)=1/(2*pi*t*sqrt(3)) E[Xbar exp(-Q/(2t))].`

由于 centered 且

`E[Xbar Q]=(2/3)kappa_3(f)`,

当 `t -> infinity`：

`B(t)= -kappa_3(f)/(6*pi*sqrt(3))*t^(-2)+O(t^(-3)).`

若定义 cubic escort law

`d nu_t(y)=(P_t f(y))^3 / int(P_t f)^3 dy`,

则

`E_(nu_t)Y= -kappa_3(f)/(3t)+O(t^(-2))`,

从而得到精确提取器

`boxed{ kappa_3(f)=-3 lim_(t->infty) t E_(nu_t)Y }`。

这把 cubic annihilation 改写成一个完全一维的 heat-escort barycenter decay
问题：需要证明其比自然 `t^(-1)` 尺度多衰减一阶。

## 5. Conditional-characteristic 版本（PROVED）

令 normalized sample mean `M=(X_1+X_2+X_3)/sqrt(3)`，并对 residual radius
`R=sqrt(Q)` 定义

`G(xi,rho)=(1/(2*pi)) int prod_j phi(xi/sqrt(3)+rho a_j(theta))dtheta`

其中 `a_j(theta)` 是长度 `sqrt(2/3)` 的三向 tight-frame projections。则

`G(xi,rho)=E[exp(i xi M)J_0(rho R)]`。

径向 exactness 只给

`G(0,rho)=exp(-rho^2/2)`。

其 first diagonal derivative

`D(rho)=partial_xi G(0,rho)=iE[MJ_0(rho R)]`

满足

`D(rho)= -i*kappa_3(f)/(2*sqrt(3))*rho^2+O(rho^4)`。

所以

`boxed{ kappa_3(f)=0 iff D(rho)=O(rho^4) as rho->0 }`。

若更强地 `D identically 0`，Hankel injectivity 给出 `E[M|Q]=0`，当然推出
`kappa_3=0`。定义 signed conditional-mean measure
`eta(dq)=E[Xbar;Q in dq]`，则同一缺口的两种变换为

`B(t)=1/(2*pi*t*sqrt(3)) int exp(-q/(2t))eta(dq)`,

`D(rho)=i*sqrt(3) int J_0(rho sqrt(q))eta(dq)`。

目标只要求
`int q eta(dq)=E[Xbar Q]=2*kappa_3/3=0`；真正缺失的是 same-factor
three-line structure 对 `E[Xbar|Q=q]` 的 global coherence。

## 6. I3 / total positivity 路线的精确 no-go（OBSTRUCTION）

令

`p_epsilon(r,theta)=(1/(2*pi))exp(-r^2/2)`
` * [1+2 epsilon r^3 exp(-r^2) cos(3 theta)]`。

对足够小的非零 `epsilon`，这是严格正、real-analytic、`D_3` 对称的二维密度，
其 circular radialization 完全 Gaussian，但

`u_1(r)=epsilon r^3 exp(-r^2)`,

`int r^3u_1(r)r exp(-r^2/2)dr`
`=epsilon int r^7 exp(-3r^2/2)dr`
`=(16/27)epsilon !=0`。

甚至当 `epsilon>0` 时 `u_1(r)>0`，所以正核
`I_3(zr)>0` 的 modified-Bessel transform 也严格为正。故

`radial Gaussian + positivity + D_3 + I_3 positivity/total positivity`

仍不足以杀掉 first harmonic；必须使用 same-factor three-line convolution。
这个 `p_epsilon` 不是项目反例。

## 7. R117 判决与 R118

### 已确立

- `Q~chi^2_2` 与整条 cubic `L^3` Gaussian heat curve 的双向等价；
- exact branch 的 `A'=-3I`、`I'=-J`、`AJ=6I^2`；
- cubic escort barycenter 的 asymptotic extractor；
- `D(rho)`、`B(t)` 与同一个 conditional-mean measure `eta` 的 Fourier/Laplace
  双表示；
- `I_3` 正性路线的精确非因子化 obstruction。

### 仍为 OPEN

`p_f` 的 genuine same-factor three-line convolution + Gaussian circular
radialization，是否强制

`int x(P_t f(x))^3dx=o(t^(-2))`，等价于 `kappa_3(f)=0`。

基础 positivity 的 `AJ>=4I^2` 不够；`I_3` 的正性也不够。

### R118 最小命题

直接攻 **Heat-Escort Barycenter Annihilation**：在 R117 假设下证明或反驳

`int_R x(P_t f(x))^3dx=o(t^(-2))`。

等价的 conditional-characteristic 版本是

`partial_xi|_(xi=0) < prod_j phi(xi/sqrt(3)+rho a_j) > = O(rho^4)`

而无需证明整个 derivative 恒为零。优先寻找带线性 tilt 的 rearrangement、
three-line total positivity，或 `E[Xbar|Q]` 的 sign/variation-diminishing
定理；不回到 finite Gram/minor、tau 高阶或数值路线。

## 8. 证据等级

`audit_r117.py` 只核验 Gaussian completion、Laplace equivalence、heat derivative
代数、tilted completion、cubic coefficients、conditional-characteristic
leading term 与 obstruction integral。Laplace/Hankel injectivity、全局
regularity、以及 same-factor annihilation仍按 ANALYTICALLY PROVED / OPEN 记录。
