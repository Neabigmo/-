# R140 — Gap–separation shell-to-energy audit

日期：2026-09-08

本目录审计同一网页端“数学定理证明 — 理论推进审计”对话中的 R140。网页端
按公开仓库提交 `5569c32c41e2ff078cb4d7e7d25479e170d7d028` 读取 R139 基线，
然后推进“最小非配对零点壳到 real-axis angular/Bochner 正能量”的接口。

对象始终是 centered、variance-one、square-exponential 的 genuine probability law；
需要 full same-factor identity 时明确加入 genuine full-SF/all-row 假设。`RK=1`、
空间的 `K_sp=log g`、normalized Bargmann 的 `C_g=log B_g`、ordinary
`K=log E exp(tX)`、formal moments/cumulants、真实 moments 和
`phi(t)=M(it)` 不互换。R140 仍没有构造 genuine non-Gaussian full-SF law。

## 1. R139 更正与量词

R139 的 signed-divisor、Cesàro mean-square、subsequential lower bound 保留。
若 `R_Delta<infty`，Pringsheim 无限变号论证必须显式使用 odd Taylor 半径
`R_Delta` 有限；不能把它应用到可能 entire 的 formal odd series。R139 的
angular `H^1` 结论和 Tonelli 版本也是 upper majorization，不能反向推出
zero-shell mass。

一个重要的 Bochner 记号修正：对第一 hidden odd degree `d=2s+1`，
`(d+3)/2` 是第一处 Hankel-leading coefficient 被 hidden `d` 改变的矩阵
尺寸，不是更小 Bochner 矩阵“完全看不见” odd phase。任意非退化 `3x3`
triangle 的 direct odd phase 在 determinant 中可在 `h^(2d)` 阶出现；其
Gaussian lower-order positive terms 仍使固定小矩阵不能给 uniform rigidity。

R139 even-cumulant cone 的量词保留为
`kappa_(2m)>=0` 对每一个 `m>=2`。仅 eventual nonnegativity 不足以逐项
杀掉 Jensen slack。

## 2. 条件性的 shell-to-energy 定理

按 `zeta -> -zeta` 轨道选代表。设第一非配对壳为

`zeta_j=R exp(i theta_j)`, `delta_j != 0`, `j=1,...,J`,

并置

`V=sum_j delta_j^2`, `L=sum_j |delta_j|`.

假设第一壳的 reciprocal angular frequencies
`lambda_j=exp(-2 i theta_j)` 满足

`sigma=min_(j != ell)|lambda_j-lambda_ell|>0`,

下一非配对 signed shell 满足 `|zeta|>=Gamma R`（`Gamma>1`），并有显式
weighted outer-tail bound

`B_3=sum_(|zeta|>R)|delta(zeta)|(R/|zeta|)^3 < infinity`.

令

`N=ceil(max{1,4L^2/(sigma V)})`,

`m_0` 为最小奇数 `>=3` 且
`B_3 Gamma^(-(m_0-3)) <= sqrt(V/8)`，并令
`M=m_0+2(N-1)`。则存在 odd `m`，`m_0<=m<=M`，使

`|kappa_m|/(m-1)! >= sqrt(V/8) R^(-m)`.

理由是，对 `m=2k+1` 的第一壳 exponential sum

`A_k=sum_j delta_j exp(-i(2k+1)theta_j)`

任意长度 `N` 的 shifted block 都满足

`N^(-1) sum_{k=K}^{K+N-1}|A_k|^2
 >= V-2L^2/(N sigma) >= V/2`.

outer shell 的归一化误差至多
`B_3 Gamma^(-(m_0-3))`，故不可能在整个这个有限 odd block 上抵消第一壳。
注意：这是 bounded-degree subsequence lower bound，不是逐阶 lower bound。

### 可审计的能量下界

令 `rho=sqrt(2/3)`，

`ell_n=(3/2^n) binom(n,(n-3)/2)`,
`a=sqrt(V/8) min_(3<=n<=M,n odd)(ell_n/n)`,
`B=L+B_3`,

以及 odd index 集合 `D_M={3,5,...,M}` 的 Gram 矩阵最小特征值

`h_M=lambda_min[1/(d_i+d_j+1)]_(d_i,d_j in D_M)>0`.

利用 odd tail 的步长为 2，可以直接核验网页端的常数 8：

`tau=min{1/2,
 sqrt(a sqrt(h_M)(M+2)sqrt(2M+5)/(8B))}`, `T=R tau/rho`.

把 `f(x)=Q_1((R/rho)x)=sum_(n odd>=3)b_n x^n` 分成 degree `<=M` 和尾项。
零点重求和及 `ell_n<=3` 给出

`|b_n| <= 3B/n`,

而上面的 shell lower bound 给出某个 `m<=M` 有 `|b_m|>=a`。由于 `M` 是 odd，
尾项从 `n=M+2` 开始；有限 monomial Gram lower bound 和 `0<tau<=1/2`
给出

`||sum_(n>M,n odd)b_n x^n||_(L^2(0,tau))
 <= 4B tau^(M+5/2)/((M+2)sqrt(2M+5))`.

这与上面的 `tau` 选择共同推出

`||f||_(L^2(0,tau)) >= (1/2)a sqrt(h_M) tau^(M+1/2)`.

因为 `Q_1(t)=f(rho t/R)`，R139 的 weighted energy 包含
`9 t^(-2)|Q_1(t)|^2`，所以得到条件性 shell-to-energy theorem：

`E(T):=sum_(r odd) int_0^T (|Q_r'|^2+9r^2|Q_r|^2/t^2)dt`

`>= Psi := (9rho/(4R)) a^2 h_M tau^(2M-1) > 0`.

这是真正的 lower bound，但依赖 `sigma`、`Gamma`、`B_3` 和有限第一壳
数据；不是只依赖 `(R_Delta,V_Delta)`。在 genuine full-SF/all-row 下，R139
upper majorization 还给

`E(T)<=U(T):=int_0^T exp(t^2/2)dt`.

因此 `Psi>U(T)` 排除该明确 geometry class。若 `J<=J_0`、
`sigma>=sigma_0`、`Gamma>=Gamma_0>1`、`B_3<=b sqrt(V)`，并使用 signed
multiplicity 的 `L<=sqrt(J_0 V)`，`M`、`tau` 可从 normalized geometry
选择，且 `Psi` 为正的 `V/R` 常数倍；从而得到该 regular-shell class 的
显式 multiplicity upper bound。由于 genuine real MGF 的非配对壳按共轭对
出现，`V` 为偶数且 `V>=2`；若得到 `V_max<2`，该 geometry class 即被排除。

证据等级：`PROVED under the displayed analytic hypotheses`; 本目录脚本只
验证有限代数和数值接口，不替代 entire-function、Fisher 或 zero-divisor
分析证明。

## 3. 为什么 `(R_Delta,V_Delta)` 仍没有 universal gap

outer shells 确实不能在上述 gap/separation/tail 假设下抹掉一个 bounded-degree
subsequence，但 `R_Delta,V_Delta` 本身不控制角向合并或径向贴近。

### Angular coalescence：genuine Bochner obstruction

令 `p+q=1`，令 centered variance-one Bernoulli law

`B_p=sqrt(q/p)` with probability `p`, and `-sqrt(p/q)` with probability `q`.

其 MGF zeros 是

`zeta_k=sqrt(pq)(log(q/p)+i(2k+1)pi)`.

当 `p->1/2` 时，最近非配对共轭壳的 angular frequencies 合并，而
`V_Delta=2`。再取独立 Gaussian `G_v` 并令

`s_p=R_0/R_p`, `v_p=s_p^2-1`, `X_p=(B_p+G_{v_p})/s_p`

（固定 `R_0>pi/2`，取 p 足够接近 `1/2`），则每个 `X_p` 是 genuine
centered variance-one law，`R_Delta=R_0`、`V_Delta=2`，square-exponential
和 Bochner positivity 一致，outer weighted tails 可统一控制，但 odd part
在每个 bounded real interval 的 `C^1` 中趋于零。因此固定 real-axis
weighted energy 可趋于零。这不是 full-SF counterexample；例如其 fourth
cumulant 不满足 full-SF 的首个 even row。

### Radial coalescence：另一 genuine Bochner obstruction

固定一个非对称 `B_p`，取独立 copy `B_p'`，固定 `S>sqrt(2)`，令 `c->1`：

`X_c=(B_p-cB_p'+G_(S^2-1-c^2))/S`.

第一壳保持 `R_Delta=S R_p`、`V_Delta=2`，但 reflected second factor 的壳
在 `R_Delta/c`，故 `Gamma=1/c->1`，而 `sigma` 可保持固定。奇累积量满足

`kappa_m(X_c)=S^(-m)(1-c^m)kappa_m(B_p)`, `m odd`,

所以 bounded-window angular energy 趋于零。该族同样只是 genuine
probability/Bochner obstruction，不是 full-SF law。

R139 的 finite-degree witness `Q_r(t_0)=Q_r'(t_0)=0` 仍说明有限测试可精确
相消；上面两族进一步说明即使要求 genuine probability 与 Bochner positivity，
没有 uniform angular/radial gap 时，bounded-window energy 仍可任意小。

## 4. Bochner：成功的全阶不等式与最低敏感阶

对 `s_j=t r_j(theta)`，`s_1+s_2+s_3=0`，三角形节点
`0,s_1,s_1+s_2=-s_3` 的 `3x3` Bochner PSD 给出

`1-sum_j|phi(s_j)|^2+2 Re(prod_j phi(s_j))>=0`.

若 genuine full-SF，则
`<prod_j phi(t r_j)>=exp(-t^2/2)`，因而

`3<|phi(rho t cos(theta))|^2> <= 1+2 exp(-t^2/2)`.

这是 genuine full-SF + Bochner 的 `PROVED` cross-degree majorization；它只
控制 modulus/even sector，不能给非配对零点 phase 的反向 gap。其 exact phase
slack 也可能由 the modulus weight 变小。

固定三角形的 direct odd phase 对 `3x3` determinant 可在 `h^(2d)` 级出现，
而第一处 Hankel-leading coefficient 改变的矩阵尺寸仍是 `(d+3)/2`。二者
不能混写。允许每个 `d` 只选有限节点和有限 SF rows 时，有限维光滑插值仍可
隐身；对一个固定 genuine all-degree law 让尺寸与节点族一起趋于无穷，仍是
合法但未解决的 global Bochner 方向。

## 5. 证据分层与 Positive Backward Tower

`PROVED`（在明确假设下）：R139 的 zero-divisor/root-limsup、有限 odd radius
下的无限变号、angular `H^1` upper bound、以及本节 gap/separation/tail 下的
shell-to-energy lower bound；full-SF triangle majorization；even-cumulant cone
Gaussian lemma；uniform compactness interface；projectively compatible genuine
backward-tower Gaussian rigidity。

`OBSTRUCTION`：没有 angular separation 或 radial gap 时，genuine Bochner
probability bounded-window energy 可以趋零；同一 `Q_r` 内跨 degree cancellation；
任意有限 Bochner 测试族的局部隐身。上述 witness 都不是 full-SF counterexample。

`CONDITIONAL`：bare scalar `RK=1 -> genuine full-SF/all-row`；ordinary
MGF/Bargmann 结论到 spatial `P_3 K_sp`；以及把有限/移动截断的 formal
对象升级为 single genuine all-degree law。

`OPEN`：full-SF + Bochner 是否自动排除 angular/radial shell coalescence；
特别是 `R_Delta->infty` 时 characteristic-scale 的 scale-invariant positive
phase gap；以及 incompatible moving-top positive backward tower。

projectively compatible single tower 的结论不变：genuine full-SF/all-row 的
统一 zero-free disk 与 OU normalized Bargmann scaling 把 bottom 的所有零点
压入共同 zero-free disk，故 bottom Gaussian。incompatible moving-top tower
仍可通过 `d_N->infty`、`a_N->0` 和 zero escape 逃逸；从 bare scalar `RK=1`
进入 genuine class 仍是 `CONDITIONAL`。

下一轮唯一任务：**R141 — Renormalized Zero-Shell Bochner Phase Compactness**。
只研究 `t=R_Delta s` 的 characteristic scale，用 `|phi|<=1` 与三角 Bochner
phase/modulus inequality，判断当 asymmetric zeros 向无穷远逃逸时，归一化的
first-shell phase 是否仍能保持统一正 gap；若不能，给出 normalized analytic
cancellation model。不得宣称已构造 genuine non-Gaussian full-SF law。
