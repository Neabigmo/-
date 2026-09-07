# R105 — Genuine homometric phase obstruction and the Schur–Abel no-go

日期：2026-09-07

本轮承接 `infinite_schur_cumulant_r104`。目标是审计网页端提出的

`P_3K\\ne0 => J(r)>3r^2/2 or J''(r)>3`

是否能成为 genuine full-exact law 的排除路线，并寻找一个不依赖形式 jet
的边界障碍。

## 1. 结论摘要

### PROVED — Schur–Abel real-axis slack identities

令

`K_e(r)=(K(r)+K(-r))/2`

并沿用 R104 的 Abel inverse `J`，使

`K_e(r)=r^2/2-J(r)/3`.

对任意非退化、具有相应实 MGF 的概率律，

`J(r)=3r^2/2-(3/2)log(M(r)M(-r))`，

因此对 `r>0`

`J(r)<3r^2/2`, `J'(r)<3r`, `J''(r)<3`.

更精确地，写 `mu_r` 为 `e^{rX}` 倾斜后的概率律，则

`3r^2/2-J(r)=(3/2)log(M(r)M(-r))`,

`3-J''(r)=(3/2)(Var_{mu_r}X+Var_{mu_{-r}}X)`.

这里第一条来自 Cauchy–Schwarz，第二条来自 `K''(r)=Var_{mu_r}X`。
这些是 genuine probability constraints；它们说明 R104 的 convexity-breakdown
命题不能靠 real-axis convexity 单独推进。

### PROVED — explicit genuine homometric obstruction

定义两条 centered、variance-one 的有限支撑概率律：

`mu_sym: P(-3/2)=2/9, P(0)=5/9, P(3/2)=2/9`；

`mu_asym: P(-1)=4/9, P(1/2)=4/9, P(2)=1/9`.

它们分别满足

`E_sym X^3=0`, `E_asym X^3=1/2`,

且都有 `E X^4=9/4`。若

`m(s)=2/3+(1/3)e^s`,

则

`M_sym(r)=m(3r/2)m(-3r/2)`,

`M_asym(r)=e^{-r}m(3r/2)^2`,

从而

`M_sym(r)M_sym(-r)=M_asym(r)M_asym(-r)`.

所以它们有完全相同的差分律 `mu*check(mu)`、`K_e`、`J` 以及 characteristic
modulus `|phi|^2`，但一个对称、一个非对称。该 obstruction 是 genuine
probability pair，不是 formal jet；不过它不是项目 counterexample，因为
两者都违反 genuine full-exact class 的四阶必要条件 `m_4=3`。

### PROVED — exactness 的四阶排除

在 genuine full-exact characteristic identity

`Z(z)=<exp(mathscr K(z,theta))>_theta=1`

下，三方向几何权满足 `<p_4>=1/2`，而三阶项的平方从六阶才开始。因此四阶
系数强制 `kappa_4=0`，即 centered variance-one 情形的 `m_4=3`。故上面的
同自相关 pair 只能作为 real-axis/phase-retrieval obstruction，不能冒充 exact
law。

## 2. 对原路线的判决

R104 的实轴目标

`P_3K\\ne0 => J>3r^2/2 or J''>3`

在 genuine law 上与“排除所有非对称 exact law”处于同一逻辑层级：一旦存在
非对称 exact law，它会同时满足严格的 real-axis slack，并直接反驳该
breakdown lemma；如果不存在非对称 exact law，该 lemma 只是在排除结论成立后
随之成立。它不是获得独立增益的中间命题。

因此，网页端的真正推进是把剩余问题精确转成：

> Schur–Abel cascade 已经恢复 one-body autocorrelation；剩余 Gaussian rigidity
> 是 same-factor cubic constraint 下的 Bochner characteristic phase-rigidity。

注意：`RK=1` 是否等价于这里的 full-exact law 仍为 **CONDITIONAL**，不能从
本轮 genuine 结论反推 bare scalar 版本。

## 3. 可执行的下一轮

### Exact-Constrained Bochner Phase-Lift Rigidity — OPEN

设 `D` 是 R104/R105 重构出的 difference law，`psi=widehat D`。寻找满足

`|phi(y)|^2=psi(y)`, `phi(0)=1`, `EX=0`, `EX^2=1`

以及 same-factor identity

`<prod_{j=1}^3 phi(a_j(theta)y)>_theta=e^{-y^2/2}`

的 characteristic phase lift，并证明其 phase 必为平凡 phase，即
`phi(y)=phi(-y) in R`。

一个尖锐但尚未证明的子引理是

`<prod_j |phi(a_j y)|> <= e^{-y^2/2}`.

exact identity 目前只给出三角不等式的相反方向

`e^{-y^2/2} <= <prod_j |phi(a_j y)|>`.

若能证明反向不等式，则处处取三角等号，随后才可研究 phase alignment 与
odd-cumulant 消失。不能把该子引理或 phase rigidity 写成已证定理。

## 4. 证据边界

- **PROVED / LOCAL-AUDITED**：上面的 slack 恒等式、两条有限支撑 MGF 计算、
  四阶 exactness obstruction。
- **CONDITIONAL**：将项目的 `RK=1` 识别为 genuine full-exact law。
- **OPEN**：非对称 genuine full-exact law 的排除、same-factor Bochner phase
  rigidity、symmetric even sector，以及原始 positive backward-tower 命题。
- **NOT A COUNTEREXAMPLE**：`mu_sym, mu_asym` 只反驳“实轴自相关数据足以识别
  对称性”，不反驳 full-exact 命题。

禁止用数值 sweep、SDP、optimizer、remote computation 或额外孤立低阶展开替代
上述 phase-lift 问题。
