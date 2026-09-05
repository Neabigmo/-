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

## 5. R10 审计：排序目标的严格 no-go 与必要修正

### 5.1 有效的新结论

在三副本桥上定义 `P_⊥=I-(1/3)11ᵀ`、
`𝓘_⊥(q,s)=E_{J_{q,s}}||P_⊥u_s(Y)||²`，则条件独立性给出

`𝓘_⊥(q,s)=2𝒟_{q,s}`，
`E_{μ_{q,s}}v_s=-𝒟_{q,s}=-(1/2)𝓘_⊥(q,s)`。

若 `H_s` 非 Gaussian，则 `u_s` 非常数；由于后验核在 `ℝ` 上处处为正，
`Var_{π_{q,s}}(u_s)>0`，所以

`E_{μ_{q,s}}v_s<0` 对每个 `q<s` 成立。

因此 `E_{μ_{q,s}}v_s≥E_{ν_s}v_s=0` 不是尚未证明的中间排序，而是一个
真实概率层面的严格 no-go：它本身等价于残差 Fisher 消失并立即导出 Gaussian。
同理，escort–MMSE 的反向协方差也只能作 rigidity certificate，不能作
非循环的中间 lemma。

嵌套后验还给出一个有效的精确分解。对 `q<r<s`，

`𝒟_{q,s}=𝒟_{q,r}+E_{μ_{q,r}}[Var_{π_{r,s}}(u_s)]`。

这明确显示了 telescoping 的缺口：第二项的权重是 `μ_{q,r}`，而自然的下一层
缺陷 `𝒟_{r,s}` 使用 `ν_r`，两者对同一个非负 production field 的比较未知。

在同一正则性下，小桥极限为

`lim_{τ↓0} 𝒟_{s-τ,s}/τ = E_{ν_s}[v_s²]`。

所以若某个 exact tower 能产生 `𝒟_{s-τ_j,s}/τ_j→0` 的小桥序列，便有
`v_s=0` 并进入 Gaussian；这是当前最弱的非循环 conditional closure。

### 5.2 对 shell/Laplace 说法的审计修正

三副本 Gaussian 密度比的代数分解仍然成立。令
`Q=∑(Y_i-Ȳ)²`、`T=Q/(2s)`、`r=s/τ`，则

`dJ_{q,s}=(s/τ)exp(-(q/(2sτ))Q)dλ_s^{⊗3}`。

但在一般非 Gaussian exact law 下，`Q/s∼χ²_2` 是错误的；它只在
`λ_s` 本身为 Gaussian 时成立。故由 `T∼Exp(1)` 推出的
`𝒟/r` completely monotone 结论不能保留。

一般只能写成（若 `ρ_s` 是 `T` 在 `λ_s^{⊗3}` 下的密度，
`Φ_s(t)=E[||P_⊥u_s||²|T=t]`）

`𝒟_{q,s}=(r/2)∫ exp(-(r-1)t) Φ_s(t)ρ_s(t)dt`。

这里 `ρ_s` 是未知的非 Gaussian shell law，不能替换为 `e^{-t}`；因此不能
从该分解推出完全单调性或自动的 production 消失。后续只使用已审计的
残差 Fisher 恒等式、嵌套分解和小桥渐近，不再使用错误的 chi-square shell
归一化。

## 6. R11：固定因子缩放与深度衰减

### 6.1 OU–heat 共轭的审计结论

为避免与 heat 时间混淆，将固定 OU 因子记为 `ρ∈(0,1)`。若
`𝔓_t f(x)=E[f(x+√t Z)]`、`S_c f(x)=f(cx)`，则

`P_ρ=S_{√ρ}𝔓_{1-ρ}`。

对 `H_a^{(j)}=𝔓_{1-a}g^{(j)}`，exact backward 关系给出

`H_a^{(j)}(x)=H_{ρa}^{(j+1)}(√ρ x)`.  (C)

所以固定 OU 因子在热坐标中制造的是 `a→ρa` 的移动参数和同步空间缩放，
不是固定顶层 `s` 上的 `τ_j↓0` 桥。虽然自然桥宽
`(1-ρ)ρ^j s→0`，但顶层函数与参数同时变化，不能直接套用 R10 的固定顶层
小桥极限。

### 6.2 经过审计的 production 缩放与 cap

令

`Δ_j(a)=𝒟^{(j+1)}_{ρa,a}`。

由 (C) 及 `u→√ρu`、`v→ρv` 的链式缩放，得到

`Δ_j(a)=ρ Δ_{j+1}(ρa)`,  即 `aΔ_j(a)=(ρa)Δ_{j+1}(ρa)`.

另一方面，若 `H_s=𝔓_{1-s}g` 且 `g≥0`，后验 Hessian 给出

`v_s≥-1/(1-s)`,  从而 `0≤𝒟_{q,s}≤1/(1-s)` 对 `0<q<s<1` 成立。

### 6.3 有限深度与相容无限塔

对深度 `N` 的 genuine positive same-factor all-degree exact tower，固定
`s∈(0,1)`，第一层 production
`Δ_0(s)=𝒟^{(1)}_{ρs,s}` 满足

`ρ^{-(N-1)}Δ_0(s)
 =𝒟^{(N)}_{ρ^Ns,ρ^{N-1}s}
 ≤𝒟^{(N)}_{ρ^Ns,s}
 ≤1/(1-s)`.

因此

`0≤𝒟^{(1)}_{ρs,s}≤ρ^{N-1}/(1-s)`.

这不是 `τ→0` 结论，而是“深度 `N` 越大，固定第一层 production 越小”的
深度衰减界。若同一第一层 pair 可相容地延拓到任意深度，则令 `N→∞` 得
`𝒟^{(1)}_{ρs,s}=0`；R10 的严格残差 Fisher no-go 随即给出 `u_s^{(1)}`
为常数，中心化与热半群 injectivity 进一步给出该层以及 `g^{(0)}` 为 Gaussian。

因此已排除的是：**projectively compatible 的非 Gaussian 正 exact 无限固定因子塔**。
原始命题还允许每个 `N` 取彼此不相容的新塔；对这类序列，上界只给出
`𝒟_N=O(ρ^N)`，不能把有限 `N` 的正量升级为 exact zero。

### 6.4 当前最小开放命题

### Depth-to-Zero Production Rigidity — OPEN

对彼此不相容的 genuine positive、same-factor、all-degree exact depth-`N` towers，
已知固定 `s` 上

`0≤𝒟^{(1,N)}_{ρs,s}≤ρ^{N-1}/(1-s)`。

剩余问题是：all-degree exact zero-set 与 positivity 是否能提供
depth-independent 的 zero-set isolation / tensor coercivity，把这个指数小量
提升为 exact Gaussian；或者能否构造/排除一列真实概率律，使非 Gaussian exact
one-step pair 的 production 沿任意深度仍可降到 `O(ρ^N)`。

必须特别区分 near-Gaussian 紧性与 tail escape：不能无证据假设
`N`-uniform coercivity，也不能用 tangent、形式 jet 或 operator-only 样例替代
真实正概率律。不得再把 `E_{μ}v_s≥0`、`∫S≥0` 或 `D=0` 当作中间假设。

log-concave backward preimage 仍是已成立的充分条件：一维 Brascamp–Lieb 给出
`W≤τ`，从而 Gaussian；当前原始假设尚未推出任何 preimage 的 log-concavity。

## 7. 已探索路线与停止条件

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

## 8. 每轮协作协议

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

## 9. 当前 checkpoint

- C2C task：`c2c_7b4e`。
- 已完成：R11；审计 OU–heat 共轭、production 缩放与外部 heat-horizon cap，得到
  固定第一层 production 的 `O(ρ^{N-1})` 深度衰减，并排除 projectively compatible
  的非 Gaussian 正 exact 无限固定因子塔；同时保留 R10 的 shell 修正。
- 当前方向：R12，攻击彼此不相容的有限深度塔：寻找 depth-independent
  zero-set isolation / tensor coercivity，或给出真实概率级的 tail-escape 障碍。
- 结论状态：主命题仍 OPEN；没有 Gaussian rigidity 的无条件证明，也没有真实概率
  律反例。
