# Positive Backward-Tower Exact Zero-Set Rigidity — Theory Route Framework

维护起点：2026-09-05  
工作区：`G:\2026\8.22统计`  
本文件是本项目的理论路线总纲；逐轮事实与审计摘要继续写入 `PROJECT_WORKLOG_APPEND.md`。

## 1. 总目标

当前主命题是 **Positive Backward-Tower Exact Zero-Set Rigidity**。

固定 `q∈(0,1)`，研究是否不存在一列非 Gaussian 的正 exact backward OU tower

`g^(j)=P_q g^(j+1)`, `j=0,…,N`, `N→∞`,

使每个 `g^(j)` 都是正的、centered、variance-one 的 `L²` 密度，并满足同一
`R K(g^(j))=1` exact-zero defect，而 `g^(0)→1` 但 `P_3 K(g^(0))≠0`。

最小局部版本：固定 `q`，若 `g=P_q h`，`g,h` 都是正的 centered
variance-one `L²` 密度且 `R K(g)=1`，是否存在 `δ_q>0` 使

`||g-1||₂<δ_q  ⇒  P_3 K(g)=0`？

必须同时使用的四个结构是：

1. exact zero defect；
2. same-factor cubic map；
3. positivity；
4. OU backward divisibility。

结论的逻辑等级必须始终标明为：无条件 lemma、conditional theorem、严格
no-go、或 OPEN；形式 jet、有限阶模型和 operator-only 反例不能冒充真实概率律。

## 2. 总体证明框架

### A. Exact defect / Fock reduction

- 用 exact-zero defect 把目标约束写成 Fock/Hermite 系数的三次 same-factor 方程。
- 利用 radial 与 charge 分解，识别 `P_3 K` 的零集与所有非零 Fock charge 的消失之间的关系。
- 现有精确三阶/低阶关系只能提供必要约束；除非有新的全阶 identity，不把有限阶消元升级为 rigidity。

### B. Gaussian anchor and local scale

- Gaussian 是 `R K=1`、`D=0`、所有非零 charge 消失的基准点。
- Near-Gaussian 论证必须说明拓扑、正则性、端点 `q↓0` 的收敛和 exact branch 的可实现性。
- Gaussian tangent 的符号测试只诊断弱假设是否足够，不能单独构成 genuine exact branch 反例。

### C. Positive backward divisibility

- 设 `H=e^K`。backward heat 方向为 `∂_q H=-(1/2)∂_x²H`。
- 真正的 backward preimage 要保持正性、可积性和同因子 exact Fock 结构；“存在一个固定 preimage”不能自动替代整座 tower。
- 任何从 positivity 得到的结论都必须区分点态约束、均值约束和跨 `x` 的相关性约束。

### D. Cross-parameter / spatial escort route

这是当前主线，目的是把 `q` 方向的 exact branch 变化与空间 `x` 的 posterior 结构接起来。

令

`ν_q(dx) ∝ exp(3K_q(x)) γ_{q/3}(dx)`,  
`u=K'_q`, `v=K''_q`, `r=x/q-u`, `U=u-E_{ν_q}u`。

在允许 Stein 积分分部的 classical exact branch 上，已审计得到：

`E f'=3E(fr)`,  `E(Ur)=0`,  `E(r²)=1/(3q)`,  `E(v)=0`,

以及 Fisher defect identity

`D(q)=3q Var_{ν_q}(u)=3 Var_{ν_q}(X)/q-1`。

严格的 transport identity 是

`(D(q)/q)' = -3 S(q)`,

其中

`S(q)=Cov_{ν_q}(U², 2v+3r²)-E_{ν_q}(v²)`。

这是目前唯一不可消去的 signed cross-`x` statistic。若 Gaussian 端点满足
`Var_{ν_q}(u)→0`，则

`∫_0^q S(s)ds = -Var_{ν_q}(u) = -D(q)/(3q) ≤ 0`。

因此“证明积分 `S≥0`”不是较弱的中间补偿 lemma，而是把主刚性结论换了一种写法；后续不得再把它当作独立目标。

## 3. Posterior bridge 与已审计障碍

若 `0<q<s`、`τ=s-q` 且 `H_q=P_τ H_s`，定义

`π_{q,s}(dy|x) ∝ H_s(y) exp(-(y-x)²/(2τ))dy`,

并令 `M(x)=E[Y|X=x]`、`W(x)=Var(Y|X=x)`。已得到

`u(x)=(M(x)-x)/τ`,  `v(x)=W(x)/τ²-1/τ`,  `E_{ν_q}W=τ`。

所以 positivity 只给出 `W≥0`（等价于 `K''_q≥-1/τ`），而 exact identity
给出 `E W=τ`；它没有给出 `W≤τ`，也没有给出 `K''_q≤0`。natural 三副本
coupling 的 Gaussian reference covariance 为
`τ I₃+(q/3)11ᵀ`，在 common/residual 坐标中是不各向同性的。这解释了为什么
原 scalar/all-degree Fock hierarchy 尚不能沿 `q` 自动 telescope。

当前缺口的结构名称是：

**anisotropic same-factor posterior-variance coherence**。

它不是普通的 Cauchy–Schwarz 界，也不是单个 radial 系数恒等式；必须说明
same-factor exactness 如何控制这族各向异性 posterior covariance。

## 4. R9：posterior bridge 的新精确恒等式

第 9 轮网页审查确认：点态 `W≤τ` 不是温和的中间估计，而是几乎直接
刚性，因为 `W-τ=τ²K''_q` 且 `E_{ν_q}K''_q=0`。本轮真正新增的是两个
可核验的跨参数恒等式。

### 4.1 三副本桥接的曲率输运

对 `0<q<s`、`τ=s-q`，若 `H_q=P_τH_s`，则后验 `π_{q,s}` 满足

`u_q(x)=E_{π_{q,s}}[u_s(Y)]`,
`v_q(x)=E_{π_{q,s}}[v_s(Y)] + Var_{π_{q,s}}(u_s(Y))`。

令 `μ_{q,s}` 为在 `ν_q(dx)π_{q,s}(dy|x)` 下的 `Y` 边缘，并令

`𝒟_{q,s}=E_{ν_q}[Var_{π_{q,s}}(u_s(Y))]≥0`。

则有经过局部正则性/可积性条件审计的恒等式

`E_{μ_{q,s}}v_s = -𝒟_{q,s}`,  `E_{ν_s}v_s=0`。

因此 `μ_{q,s}` 与 `ν_s` 之间确实存在一个各向异性曲率缺口；但现有假设
没有给出 `μ_{q,s}≽ν_s` 或任何足以控制 `v_s` 的随机序。注意这不是
有限 Fock 系数恒等式，也没有自动使用出 all-degree same-factor 的额外约束。

一个可证明但不适用于当前物理塔的边界事实是：若固定 `H_q` 存在任意深度
`T→∞` 的正 heat preimages，则 `K''_q≥-1/T` 强迫 `K''_q≥0`；再结合
`E_{ν_q}K''_q=0` 即为 Gaussian。OU-to-heat 共轭在物理区间的总 horizon
有限，所以这个 deep-horizon 结论不能解决原命题。

### 4.2 cubic escort 与 MMSE

写 `λ_q(dx)=p_q(x)dx=H_q(x)dγ_q(x)`，则 `ν_q` 是 `λ_q` 的 cubic escort：

`dν_q = p_q^3 dx / ∫p_q^3 dx`。

对同一后验的 `W=Var(Y|X)`，普通观测律 `λ_q` 给出

`E_{λ_q}W = τ-τ²E_{λ_q}u_q²`，

而 exact cubic escort identity 给出 `E_{ν_q}W=τ`。若
`ω_q=p_q²/∫p_q³`，则 `E_{λ_q}ω_q=1` 且

`Cov_{λ_q}(W,ω_q)=τ²E_{λ_q}u_q²
 =τ² I(λ_q||γ_q)≥0`。

这把缺口具体化为“如何比较 cubic escort 与 ordinary observation law 对后验
方差的加权”。它仍然没有给出所需的反向排序；其作用是提供一个独立的
rigidity certificate，而不是非 Gaussian exact law 的反例。

## 5. 当前最小开放命题

### Anisotropic Curvature Ordering — OPEN

对 sufficiently near-Gaussian 的 genuine positive、same-factor、all-degree exact
backward tower，是否存在某个 `q<s` 使

`E_{μ_{q,s}}K''_s ≥ E_{ν_s}K''_s=0`？

无条件桥接恒等式已经给出左边 `≤0`，所以若这个单一 scalar reverse-order
不等式成立，两边即同时为零，`𝒟_{q,s}=0`，后验中 `u_s` 为常数，并进入
Gaussian rigidity。它严格弱于点态 `W≤τ`，且直接瞄准唯一未控制的
anisotropic marginal。

一个平行的、同样足以关闭刚性的候选是
`Cov_{λ_q}(W,ω_q)≤0`；但精确 escort–MMSE 恒等式表明它等价于
`I(λ_q||γ_q)=0`，因此只能作为刚性证书，不能当作已知中间估计。

不得再把 `∫S≥0`、`D=0` 或等价的 rigidity 结论作为假设。log-concave
backward preimage 仍是已成立的充分条件：一维 Brascamp–Lieb 给出 `W≤τ`，
从而 Gaussian；当前原始假设尚未推出任何 preimage 的 log-concavity。

## 6. 已探索路线与停止条件

- Angular/Fourier、低阶 Fock、radial coefficient：已提供必要恒等式，但没有全阶
  positivity/coercivity；停止继续无约束展开。
- Analytic-radius、Fredholm、tail/common-root：已定位 compactness、相对尾估计和
  complex resonance 缺口；没有概率/OU coherence 时不再扩展该线。
- Posterior/Laguerre/spatial escort：已产生 exact bridge 和条件矩恒等式；scalar
  closure 的有限 `Q`-moment 版本不能代表真实概率反例，也不能代替 cross-`x` coherence。
- 任意 Gaussian tangent、Rademacher 或 operator-only PSD 样例：只用于严格 no-go
  诊断，不作为 genuine exact law 的反例。
- 任何新 Codex 计算必须先证明它会触及一个尚未解决的全阶/各向异性结构；若只是
  有限系数核验、数值扫参或重复低阶展开，明确记录“Codex 暂不执行”。

## 7. 每轮协作协议

1. 网页端开始新一轮理论工作前，先通过连接阅读本文件和
   `PROJECT_WORKLOG_APPEND.md`，再阅读当前 Git 状态与已有审计资产；不得要求粘贴
   文件内容。
2. 每轮只锁定一个可证伪的理论子命题，并输出：无条件 lemma、conditional theorem、
   已审计 obstruction、最小 OPEN、是否需要 Codex 计算。
3. Codex 负责本机执行、精确核验、结果记录和 Git；网页端负责理论规划与审查。
4. 新的本机事实先写入日志/本文件，再提交到实际 Git 子仓库；不改写历史证据，
   不提交凭据、令牌、原始连接日志或无关大文件。
5. 若需要计算，使用独立专用分支和明确输入/输出/验收标记；计算结果不能替代理论
   可实现性证明。

## 8. 当前 checkpoint

- C2C task：`c2c_7b4e`。
- 已完成：R9；建立三副本曲率输运和 escort–MMSE 恒等式，确认点态 domination
  过强，并将最小 OPEN 改为 Anisotropic Curvature Ordering。
- 当前方向：R10，直接审查 `μ_{q,s}` 与 `ν_s` 的可能排序，寻找 genuine
  same-factor/all-degree 约束能否提供该 scalar reverse inequality，或给出严格
  no-go。
- 结论状态：主命题仍 OPEN；没有 Gaussian rigidity 的无条件证明，也没有真实概率
  律反例。
