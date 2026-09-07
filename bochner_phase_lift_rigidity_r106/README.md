# R106 — Exact-constrained Bochner phase lift and the first modulus excess

日期：2026-09-07

本轮承接 `homometric_phase_obstruction_r105`，审查网页端提出的

`A(y)=<prod_j |phi(a_j(theta)y)|> <= exp(-y^2/2)`

是否能作为独立的 phase-rigidity 桥。这里
`a_j(theta)=sqrt(2/3) cos(theta+2*pi*j/3)`，所以
`a_1+a_2+a_3=0`、`sum_j a_j^2=1`。

## 1. 结论摘要

### PROVED — exact triangle/phase-defect identity

令

`F_y(theta)=prod_j phi(a_j(theta)y)=r_y(theta) exp(i V_y(theta))`,

`A(y)=<r_y>`，`g(y)=exp(-y^2/2)`。在 `A(y)>0` 时以
`d pi_y=r_y d theta/A(y)` 加权。full exactness 给出

`E_(pi_y) exp(i V_y)=g(y)/A(y)`.

因此

`A(y)-g(y)=2 A(y) E_(pi_y) sin^2(V_y/2) >= 0`.

这是真正的恒等式而非估计；模长超额正是同因子乘积的角向相位离散度。

### PROVED / LOCAL-AUDITED — local reverse-modulus equivalence

三角不等式已经给出 `A>=g`，所以在局部非零区间内

`A<=g` `iff` `A=g` `iff` `V_y=0` `pi_y`-a.e.

由于 characteristic function 在原点附近不为零，连续 logarithm branch 可用，
故 phase alignment 等价于 `V_y` 恒为零。结合 R102 已核验的 angular charge
识别（以及 MGF/analytic uniqueness），网页端得到局部等价链：

`P_3 K=0` `iff` `mu` 对称 `iff` local phase alignment
`iff` `A(y)=g(y)` `iff` `A(y)<=g(y)`。

这里“`P_3 K=0 iff mu symmetric`”依赖 R102 的 analytic input；本机 audit
只核验本轮有限恒等式，不把它伪装成独立的有限系数证明。

### CONDITIONAL — nonzero odd charge forces strict reverse direction

若 genuine full-exact law 存在且 `P_3 K != 0`，令 `d` 为首个非零 odd
cumulant degree，并令 R103 的 first-charge energy 为

`S_d=sum_(r: 3r<=d, r odd) |q_r|^2 > 0`.

R103/R104 的 Schur identity 与 exactness 给出

`A(y)/g(y)=1+S_d y^(2d)+O(y^(2d+2))`.

所以该 hypothetical asymmetric exact law 必满足 `A(y)>g(y)` 对所有充分小的
非零 `y` 成立。它是候选 upper bound 的 genuine full-exact counterexample，
但仍然是 CONDITIONAL：构造这个 law 本身等价于推进当前主 OPEN。

并且 `S_d=1/2 <V_d^2>`，故首个正系数就是首个非零 log-charge 的 phase
variance。

## 2. 新的 genuine Bochner necessary condition

三点 Bochner/Cauchy–Schwarz 对任意 characteristic function 给出

`|phi(x+v)-phi(x)phi(v)|^2 <= (1-|phi(x)|^2)(1-|phi(v)|^2)`.

取 `x=a_1 y`、`v=a_2 y`，并用 `a_1+a_2=-a_3`，得到

`1+2 r_1 r_2 r_3 cos(V_y)-(r_1^2+r_2^2+r_3^2)>=0`.

平均并使用 full exactness 后，令 `psi=|phi|^2`、`rho=sqrt(2/3)`，得到

`3 < psi(rho y cos(theta))>_theta <= 1+2 exp(-y^2/2)`.  (20)

这是 genuine probability/Bochner 的 phase-free necessary condition；它只依赖
差分律 `D=X-X'`，因而与 R105 的 Schur–Abel autocorrelation reconstruction
直接接口。

更精确地，Bochner allowance 给出

`0 <= A-g <= (1/2)[1+2A-3<psi(rho y cos(theta))>]`.

这条式子把需要的 phase defect 与 difference-law 能够承受的 budget 分开。

## 3. 战略判决与下一轮

R105 的反向模长上界不是独立的 phase-rigidity 工具：在局部它就是 phase
alignment 本身。R106 的实质性弱推进是把剩余问题压到 phase-free 的三点
Bochner inequality (20)。

下一轮最小 OPEN 是 `Difference–Bochner Breakdown Lemma`：若 `P_3K!=0`，是否
必存在有限 `y!=0` 使 (20) 严格反向？若能证明即可排除 asymmetric exact branch；
若不能，则应转向 higher-point Bochner constraints，而不是重开 R99–R105。

## 4. 证据边界

- **PROVED / LOCAL-AUDITED**：phase-defect algebra、三点 Bochner algebra、
  平均后的 phase-free bound、首个 excess 系数与 phase-variance 的关系。
- **ANALYTICALLY PROVED / LOCAL-AUDITED**：在 R102 的 analytic charge input、
  局部 log branch 与 exact MGF 假设下的等价链和 strict asymptotic。
- **CONDITIONAL**：存在 asymmetric genuine full-exact law时的 counterexample
  分支；它不是已构造的 law。
- **OPEN**：nonzero odd charge 的 Bochner breakdown、asymmetric genuine exact-law
  exclusion、full phase-lift rigidity，以及最终 positive backward-tower theorem。

禁止用 numerical sweep、SDP、optimizer、remote computation 或孤立低阶展开替代
上述 infinite-dimensional phase-lift/Bochner 问题。
