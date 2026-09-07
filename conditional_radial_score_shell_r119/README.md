# R119 — Universal Sign-Flip Identity 与 Conditional Radial-Score Shell

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（待本机 audit）；CONDITIONAL；FORMAL；核心 OPEN。

## 1. 目标与判决

在 R118 中，令 `X_1,X_2,X_3` iid centered，

`Q=sum_j(X_j-Xbar)^2`,

并令 `Y=(X_1,X_2,-X_3)`、
`Qsharp=sum_j(Y_j-Ybar)^2`。

R119 检查是否能用 mixed-reflection 的三阶矩反向比较关闭 cubic sector。结论是：
这个反向比较本身就是原目标的等价重写，不是独立的较弱桥梁；真正新增的是
same-factor score-shell identity。

## 2. Universal sign-flip moment identity（PROVED）

直接有

`Qsharp=Q+(4/3)X_3(X_1+X_2)`。

对任意 centered iid law（只需六阶矩有限，不需 exactness、`kappa_4` 或 degree-six
fingerprint）进行纯矩代数：

`E Qsharp=E Q`,

`E(Qsharp)^2=E Q^2`,

`boxed{E(Qsharp)^3-EQ^3=(224/27)(E X^3)^2}`。

所以在 genuine full-exact class 中 `EQ^3=48` 时，

`boxed{E(Qsharp)^3<=48 iff kappa_3(f)=0}`。

这解释了为什么 R118 的自然方向 `E(Qsharp)^3>=48` 不是技术误差，而是任何
skewed centered iid law 都满足的 universal sign-flip 事实。

## 3. Laplace saturation 同样等价（PROVED）

令 `L(lambda)=E exp(-lambda Q)`、
`Lsharp(lambda)=E exp(-lambda Qsharp)`。因前两矩相同：

`L-Lsharp=(E(Qsharp)^3-EQ^3)lambda^3/6+O(lambda^4)`

`=(112/81)kappa_3(f)^2lambda^3+O(lambda^4)`。

因此在当前 subGaussian/exponential-moment class 中：

`boxed{Lsharp(lambda)=L(lambda)-o(lambda^3) iff kappa_3(f)=0}`。

故 `E(Qsharp)^3<=48` 和 Laplace `o(lambda^3)` 都已经等价于 cubic exclusion，
不能作为独立中间命题继续追。

## 4. modulus-only 路线的严格障碍（OBSTRUCTION）

mixed-sign residual characteristic transform 为

`Hsharp(r)=avg_theta phi(r a_1)phi(r a_2)phi(-r a_3)`。

由于 `phi(-u)=conjugate(phi(u))`，其逐点 modulus 与 ordinary product 完全相同：

`|phi(r a_1)phi(r a_2)phi(-r a_3)|`
`=|phi(r a_1)phi(r a_2)phi(r a_3)|`。

所以任何只使用 `|phi|`、difference law、Schur–Abel modulus 或 radial product
magnitude 的 global comparison 都看不到 `Q` 与 `Qsharp` 所需的 cubic sign；
差异完全在 angular phase。反向比较若成立，必须真正使用 all-degree exact radial
identity，而不能来自 ordinary same-factor positivity、Hölder 或 modulus。

## 5. Conditional mean profile（PROVED）

在 full exact 下，令

`h(q)=E[Xbar|Q=q]`,  `nu(dq)=(1/2)e^{-q/2}dq`。

centeredness 给 `int h dnu=0`，而

`kappa_3=(3/2)int qh(q)dnu`。

因此 reverse comparison 的真正内容只是要求 `h` 对 `q` 再正交：

`int qh dnu=0`。

centeredness 只给 `h` 对常数 `1` 正交；这明确显示了尚缺的一个 scalar
orthogonality。

profile-level variation-diminishing 也不足：`h_0(q)=q-2` 满足
`int h_0 dnu=0`，严格单调且只变号一次，但
`int qh_0 dnu=Var(Q)=4`。这不是 genuine exact one-body counterexample，
只是说明“单调/一次变号”本身不能关闭 cubic。

## 6. 新的 same-factor conditional score-shell identities（PROVED / ANALYTICALLY PROVED）

若存在 nonzero-charge counterexample，可先做任意小 forward OU smoothing，因此可
无损假设 `f` 严格正、analytic 且 score integration 合法。记

`rho(x)=(log f)'(x)`,

`Sigma_0=sum_j rho(X_j)`,
`Sigma_R=sum_j(X_j-Xbar)rho(X_j)`。

在 mean-residual orthogonal coordinates
`M=sqrt(3)Xbar`、`|Z|^2=Q` 中，mean-direction integration by parts 给

`E[psi(Q)Sigma_0]=0`,  所以 `E[Sigma_0|Q]=0`；

`boxed{E[Xbar Sigma_0|Q]=-1}`。

residual-plane radial divergence 给

`E[psi(Q)Sigma_R]=-E[2psi(Q)+2Qpsi'(Q)]`。

利用 `Q~chi^2_2` 的 exponential Stein identity：

`boxed{E[Sigma_R|Q=q]=-q}`。

再对 `Xbar psi(Q)` 做同样的 residual integration by parts，并作一维积分分部，
得到

`E[Xbar Sigma_R|Q=q]=2q h'(q)-q h(q)`，

从而得到本轮的核心新接口

`boxed{2q h'(q)=Cov(Xbar,Sigma_R|Q=q).}`

这是 genuinely same-factor、score-sensitive、conditional、global-in-q 的结构，
不是 finite moment identity。

并且

`E[Xbar Q]=E[ Cov(Xbar,Sigma_R|Q) ]`,

所以

`boxed{kappa_3=(3/2)E[Cov(Xbar,Sigma_R|Q)]}`。

## 7. 可发表的条件性接口与精确缺口

若能证明对整个 genuine exact class 都有 reflection-stable 固定方向

`Cov(Xbar,Sigma_R|Q=q)>=0` a.e. `q`

或 universally `<=0`，则将同一 theorem 应用于 reflected law `check f(x)=f(-x)`：
`Q` 不变、`h_check=-h`、`h'_check=-h'`，两侧符号同时成立，故 `h'=0`；centered
再给 `h=0`，最终 `kappa_3=0`。

这形成一个精确的 **Reflection-Stable Radial-Score Sign Lemma**；它是当前最合适
的 total-positivity / conditional MLR 目标。重要的是，若只能得到
`sign h'=sign kappa_3` 这类 orientation-dependent 单调性，reflection 后完全
相容，不能产生矛盾。

## 8. R119 判决与 R120

### 已确立

- universal sign-flip 的前三阶矩恒等式；
- reverse third-moment 与 Laplace `o(lambda^3)` saturation 都等价于
  `kappa_3=0`；
- modulus-only 与 ordinary same-factor comparison 不可能产生 reverse；
- exact radial-score shell identity；
- `kappa_3` 与 conditional radial-score covariance 的精确表示。

### 仍为 OPEN

`kappa_3(f)=0`，或等价地 `B(t)=o(t^(-2))`。R119 没有制造 genuine probability
counterexample；R104 的 nonzero odd all-degree completion 仍只是 FORMAL。

### R120 最小命题

研究 **Conditional Radial-Score Sign / Total-Positivity Lemma**：在 strict
positive analytic genuine exact three-line class 中，能否由 same-factor product、
Gaussian radial marginal 与 TP/rearrangement/conditional MLR 推出

`Cov(Xbar, sum_j(X_j-Xbar)(log f)'(X_j) | Q=q)`

对所有 `q` 具有 reflection-stable 的固定符号？若能，立即关闭 cubic；若不能，
构造 genuine same-factor、最好 strict log-concave/TP2 的有限 exact obstruction，
证明标准 TP2 只给 orientation-dependent monotonicity。

## 9. 证据等级

`audit_r119.py` 只核验 sign-flip 多项式与前三阶矩、Laplace coefficient、profile
正交例子、score-shell 的代数接口与 reflection sign。积分分部的 analytic
正则性和 conditional disintegration 仍标为 ANALYTICALLY PROVED；固定符号引理
以及 cubic exclusion 仍 OPEN。
