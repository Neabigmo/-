# R120 — Conditional Radial-Score Sign / Angular-Mixture Coherence

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（结构分解，待本机 audit）；CONDITIONAL；
OBSTRUCTION；核心 OPEN。

## 1. 判决

R120 不能从 standard TP/MLR/log-concavity 直接推出
`Cov(Xbar,Sigma_R | Q=q)` 的 reflection-stable 固定符号。更精确地：

- shell-kernel TP2/RR2 分别只给 orientation-dependent 的 `h'(q)>=0` 或
  `h'(q)<=0`；
- reflection 精确交换 TP2 与 RR2，因此方向会随 skew 反转；
- anglewise TP 即使逐角成立，也不在 angular mixture 下保持；
- strict log-concavity、score monotonicity、analyticity、same-factor 与
  degree-six fingerprint 仍不足以产生反射不变方向。

本轮真正的新结构是把 shell derivative 分解为 within-angle MLR 与
between-angle coherence 两项，并将缺口压缩到后者。

## 2. Shell kernel 与 exact MLR 表示（PROVED）

定义

`a_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`，则

`sum_j a_j=0`,  `sum_j a_j^2=1`。

对 `q>0,m in R` 定义

`F_theta(q,m)=prod_j f(m+sqrt(q)a_j(theta))`,

`K_f(q,m)=(1/(2*pi)) int_0^(2*pi) F_theta(q,m)dtheta`。

除去固定的 polar Jacobian，`K_f` 是 `(Q,Xbar)` 的联合 shell density。令

`A(q)=int K_f(q,m)dm`,  `pi_q(m)=K_f(q,m)/A(q)`。

full exactness 只固定 row mass：

`A(q)=C_0 exp(-q/2)`。

因此任何正 row factor `A(q)^(-1)` 都不改变 TP2 minor 的符号；Gaussian radial
marginal 本身没有直接指定 `q-m` 的 TP orientation。

记 `rho=(log f)'`、
`Sigma_R=sum_j (X_j-Xbar)rho(X_j)`。逐角微分给

`partial_q log F_theta=Sigma_R/(2q)`，

平均后：

`partial_q log pi_q(m)=E[Sigma_R | q,m]/(2q)+1/2`。

故 `h(q)=E[Xbar|Q=q]` 满足

`boxed{h'(q)=Cov_pi_q(m,partial_q log pi_q(m))`
`=(1/(2q))Cov(Xbar,Sigma_R|Q=q).}`

这重新得到 R119 的 score-shell identity，但现在把它识别为 shell kernel 的
universal MLR orientation 问题。

## 3. TP2/RR2 与 reflection 的精确关系（PROVED / CONDITIONAL）

若 `K_f(q,m)` 在 `(q,m)` 上 TP2，则 `pi_(q2)/pi_(q1)` 随 `m` 单调增加，
所以

`K_f TP2 => h'(q)>=0 => Cov(Xbar,Sigma_R|Q=q)>=0`。

若 `K_f` 为 RR2，方向相反：

`K_f RR2 => h'(q)<=0`。

反射 `check f(x)=f(-x)` 满足

`K_check f(q,m)=K_f(q,-m)`,
`h_check f=-h_f`,
`C_check f(q)=-C_f(q)`,

其中 `C_f(q)=Cov_f(Xbar,Sigma_R|Q=q)`，且

`boxed{K_f TP2 iff K_check f RR2}`。

所以“每个 f 都有单调 h，但方向依赖 f”最多是 skew-orientation detector，
不能 annihilate skew。

若额外假设整个 genuine exact class 的 shell kernel 都具有统一方向 TP2（或
统一方向 RR2），则同一假设应用于 `f` 与 `check f`，使 `K_f` 同时 TP2 与 RR2。
所有 `2x2` minors 于是为零；严格正性给

`K_f(q,m)=A(q)B(m)`，即 `Xbar` 与 `Q` 独立。centeredness 使 `h=0`，从而
`kappa_3=0`。这是一个完整但尚未由 exactness 推出的
**Reflection-TP Rigidity** 条件性定理。

## 4. strict log-concavity 与 anglewise TP 的边界（PROVED OBSTRUCTION）

逐角交叉曲率为

`partial_m partial_q log F_theta`
`=(1/(2sqrt(q))) sum_j a_j(theta) rho'(m+sqrt(q)a_j(theta))`。

strict log-concavity 只给 `rho'(x)<0`，并不能固定上述和的符号；还需要
`rho'` 自身单调，即对 `rho'` 的二阶 shape 约束。若额外 `rho'` 非减，Chebyshev
给 anglewise TP2；若 `rho'` 非增，则 anglewise RR2。但 reflection 会交换这
两种方向，所以仍不是 reflection-stable 结论。

更强地，即使每个 `F_theta(q,m)` 都同方向 TP2，正的 angular mixture
`K_f=int F_theta dtheta` 也不自动 TP2。抽象的 `2x2` 反例是

`A=[[1,10],[10,100]]`,  `B=[[10,1000],[1,100]]`。

两者都是正 rank-one、determinant 为零的 TP2 矩阵，但

`det(A+B)=det([[11,1010],[11,200]])=-8910<0`。

所以 anglewise TP 还缺少跨角的 joint angular coherence / MTP 结构。

## 5. within-angle + between-angle 精确分解（PROVED / ANALYTICALLY PROVED）

令

`A_theta(q)=int F_theta(q,m)dm`，
`dw_q(theta)=A_theta(q)/(int A_alpha(q)dalpha) * dtheta/(2*pi)`，

`m_theta(q)=E[Xbar|q,theta]`，
`r_theta(q)=E[Sigma_R|q,theta]`。

则

`h(q)=E_(w_q)[m_theta(q)]`。

逐角微分与 angular mixture 微分分别给

`2q m_theta'(q)=Cov(Xbar,Sigma_R|q,theta)`,

`2q partial_q log A_theta(q)=r_theta(q)`，以及

`boxed{2q h'(q)`
`=E_(w_q)[Cov(Xbar,Sigma_R|q,theta)]`
`+Cov_(w_q)(m_theta(q),r_theta(q)).}`

第一项是 ordinary anglewise MLR 可触及的 within-angle term；第二项是
between-angle reweighting/coherence term，也是 standard TP 路线一直缺少的部分。

exact radial marginal 只给

`E_(w_q) r_theta(q)=-q`，

并不决定 `Cov_(w_q)(m_theta,r_theta)`。因此即使第一项有符号，第二项仍可改变
总符号。

## 6. analytic strict-log-concave same-factor obstruction（OBSTRUCTION）

取标准 Gaussian `gamma` 与 bounded real-analytic functions `psi_3,psi_4,psi_6`
（二阶导数有界），使其在 Gaussian 下对 Hermite modes `H_3,H_4,H_6` 形成对偶
矩阵。对小参数考虑

`p_theta(x) proportional exp(-x^2/2+theta_3 psi_3(x)+theta_4 psi_4(x)+theta_6 psi_6(x))`。

小参数下可保持严格正、real-analytic、严格 log-concave；affine standardize
后仍是 centered variance-one。Gaussian 点的 cumulant map 对
`(kappa_3,kappa_4,kappa_6)` 可取满秩，因此 inverse-function theorem 给出小
非零 `c` 的 genuine one-body density `f_c`，满足

`kappa_3(f_c)=c`,  `kappa_4(f_c)=0`,  `kappa_6(f_c)=-3c^2`。

每个 one-body law 自动是 genuine iid same-factor；利用 parity 可安排
`f_(-c)=check f_c`。但其 conditional covariance 的平均分别为 `c` 与 `-c`，
所以仅凭

`analyticity + strict log-concavity + same-factor + degree-six exact fingerprints`

不可能推出 reflection-stable universal `C(q)>=0` 或 `C(q)<=0`。该构造不是
full-exact project counterexample；它的用途是严格排除“正则性/有限 fingerprint
已经暗含符号定理”的误解。

## 7. score monotonicity 只控制错误层级

若 `f` log-concave，`rho` decreasing。对固定 residual vector `z_j` 且
`sum z_j=0`，反向排序给

`Sigma_R=sum_j z_j rho(m+z_j)<=0`。

但 exact shell identity 也给 `E[Sigma_R|Q=q]=-q<0`；这只控制 radial score
本身，不控制需要的
`Cov(Xbar,Sigma_R|Q=q)`，后者在 reflection 下翻号。故 score monotonicity
仍不能给固定 covariance 方向。

## 8. R120 判决与 R121

### 已确立

- shell kernel 的 exact MLR 表示；
- TP2/RR2 到 covariance sign 的方向映射；
- reflection 精确交换 TP2 与 RR2；
- universal fixed-orientation shell TP 的 rank-one rigidity（CONDITIONAL）；
- strict log-concavity 不足以固定 anglewise 交叉曲率；
- anglewise TP 不在 angular mixture 下闭合；
- within-angle + between-angle coherence 的精确分解；
- analytic、strict-log-concave、same-factor、degree-six-compatible obstruction。

### 仍为 OPEN

`Cov(Xbar,Sigma_R|Q=q)` 的 reflection-stable 固定符号，或更强的恒零，仍未由
genuine full-exact radial structure推出；因此 `kappa_3(f)=0` 仍 OPEN。

### R121 最小命题

研究 **Angular-Mixture Coherence Lemma**：只攻

`C_ang(q)=Cov_(w_q)(m_theta(q),r_theta(q))`。

目标不是先要求整个 shell kernel TP2，而是判断 genuine all-degree angular
exactness / R101 Herglotz structure 能否给出 `C_ang(q)` 的明确 quadratic-form
表示，或至少给出它与 within-angle term 的强制相对符号/抵消关系。若不能，便可
正式关闭 TP/MLR 作为主路线，而转向 R119 的 conditional-mean diagonal transform。

## 9. 证据等级

`audit_r120.py` 只核验 `a_j` frame、reflection/TP algebra、anglewise mixture
counterexample、within/between 分解的代数接口与 sign logic。score integration
by parts、inverse-function obstruction 与 full exactness 边界仍按
ANALYTICALLY PROVED / OBSTRUCTION / CONDITIONAL / OPEN 记录。
