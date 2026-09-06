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

## 7. R12：exact 概率类的紧性、OU 闭包与真正的剩余逃逸

### 7.1 先固定 exact law 的逻辑层级

本节的无条件陈述针对 genuine full exact probability class `𝓔`：若
`X_1,X_2,X_3` iid、centered、variance-one，且

`Q=∑_{i=1}^3(X_i-X̄)^2∼χ²_2`，

则称其为 exact law。若项目中的 `RK=1` 只是一个标量记号而尚未证明与
这个 full `Q`-law 等价，则以下 tail/OU 结论必须标为“在 genuine exact law
假设下”，不能直接从单个标量等式推出。`P_3K≠0` 的 charge sector 也必须单独
保留，不能由“非 Gaussian”自动补上。

### 7.2 无条件的 physical-tail no-go

由

`Q≥(X_1-X_2)^2/2`

和 `E exp(2ηQ)=(1-4η)^{-1}`，再对 `X_2` 使用条件 Jensen，得到

`E exp(ηX^2)≤e^{-η}/(1-4η)`,  `0<η<1/4`.

常数与 exact law、tower depth 和 tower index 无关。因此 exact 类具有
`N`-uniform tightness、任意固定阶矩的 uniform integrability，以及局部复 MGF
控制；Case B 不可能靠概率质量向 `|X|→∞` 的 physical tail escape 存活。

同一估计给 normalized Hermite coefficients 一个统一指数包络。若
`a_n(μ)=E_μ[H_n(X)/√(n!)]`，则存在与 `μ` 无关的 `M,B` 使
`|a_n(μ)|≤MB^n`。对深度 `N` 的顶层 `h_N`，OU 缩放给出

`a_n(P_{ρ^N}h_N)=ρ^{Nn/2}a_n(h_N)`，

于是 centered/variance-one 条件消去 `n=1,2` 后

`||P_{ρ^N}h_N-1||_2=O(ρ^{3N/2})`

一致成立（当 `N` 足够大）。这解释了为何 `g_N^(0)→1` 本身不是稀有额外
假设，但也不等于有限 `N` 的 exact rigidity。

### 7.3 exact 类对前向 OU 的无条件闭包

在 residual plane 取 `R=A(X_1,X_2,X_3)`，其中
`AA^T=I_2`、`A^TA=I_3-(1/3)11^T`，则 `|R|²=Q`。独立 OU 后

`R_t=√t R+√(1-t)G`,  `G∼N(0,I_2)`.

给定 `R` 时，`|R_t|` 的条件分布只依赖 `|R|`；而 `|R|` 与二维标准 Gaussian
半径同分布，所以 `|R_t|` 仍与二维标准 Gaussian 半径同分布。故

`g∈𝓔  ⇒  P_tg∈𝓔`,  `0<t<1`.

这是真实概率律层面的 OU closure，不是 tangent 或有限 Fock 结论。

### 7.4 Case B 与单个 counterexample 的关系

若存在一个 genuine positive、centered、variance-one、`L²` 的 exact law `h`，
则可定义

`g_N^(j)=P_{ρ^{N-j}}h`,  `j=0,…,N`.

它满足固定因子递推、每层 exact/positive，且 `g_N^(0)→1`。因此在不附加
`P_3K` sector 限定时，Case B 与“存在一个非 Gaussian exact law”本质等价。
对于本项目要求的 `P_3K≠0` sector，尚需显式证明该 charge 沿 OU 轨道不消失；
不能把这一步隐藏在“非 Gaussian”表述中。反方向则直接成立，因为 Case B
的任一有限层本身就是 exact law。

### 7.5 绝对局部 isolation 不是较弱的桥梁

在 exact 类 `𝓔` 对 OU 闭包且 `P_{ρ^m}h→1` 于 `L²` 的条件下，

`1 在 𝓔 中局部绝对孤立  ⇔  𝓔={1}`.

证明是直接的：局部孤立性作用于充分小的 `P_{ρ^m}h`，再用 OU 在
`L²(γ)` 上 Hermite 乘子全非零的 injectivity 得 `h=1`。所以寻找
`D_N=O(ρ^N)` 后直接推出 `D_N=0` 的 absolute depth-independent isolation，
本身已接近完整 Gaussian uniqueness，不能继续包装成非循环中间 lemma。

### 7.6 真正剩余的逃逸与最小 OPEN

R11 的深度界只给 `D_N→0`，而连续 coercivity 只能给“更小”，不能给有限
`N` 的 exact zero。physical tail escape 已被排除；剩下的是 amplitude escape
和 spectral/high-chaos escape，且现有统一 MGF/Hermite 包络尚未给出 uniform
`L²`-tail tightness 或非 Gaussian normalization。

因此当前最小 OPEN 改为：

### OU-Invariant Shape Rigidity — OPEN

能否构造一个 `𝓙(g)≥0`，满足 `𝓙(g)=0` 当且仅当 `g` Gaussian，并且在前向
OU 下具有可控的齐次缩放、不会随非 Gaussian 振幅一起塌缩；再将这个
amplitude-normalized same-factor tensor invariant 与 R11 的 depth decay 结合？

若不能，则需要严格刻画：在统一 sub-Gaussian compact class 中，任何自然的
OU-homogeneous normalization 是否都会发生 spectral noncompactness，以及究竟
是哪一类 all-degree angular/Fock tail 逃逸。不得以 absolute isolation、普通
小量 coercivity、tangent、形式 jet 或 operator-only 样例替代这个问题。

本轮 Codex 暂不执行；没有需要有限系数核验的地方。

## 8. R13：primitive shape、反向半径与 Bochner 尾障碍

### 8.1 反向 exactness 与最大反向半径

以下仍只对 genuine full exact law class `𝓔` 无条件成立：若 residual plane
中 `R=A(X_1,X_2,X_3)`，则独立 OU 后

`R_t=√t R+√(1-t)G`,  `G∼N(0,I_2)`.

若 `P_tμ` 的 residual radius 仍为 `χ²_2`，条件 Laplace 变换给出

`E exp(-zQ_{P_tμ}/2)
 = (1+(1-t)z)^{-1}
   E exp[-tzQ_μ/(2(1+(1-t)z))]`.

右端与 `1/(1+z)` 相等时，令
`θ=tz/(1+(1-t)z)`，在 `θ` 的一个非空区间上得到
`E exp(-θQ_μ/2)=1/(1+θ)`；Laplace 唯一性遂推出 `Q_μ∼χ²_2`。
所以 genuine exact law 的实际正 OU 原像也 exact；这不是由单个 `RK=1`
标量等式推出的结论。

对 exact probability law 定义

`r(μ)=sup{r≥1: μ=P_{r^{-2}}ν 对某个 probability law ν}`.

反向特征函数候选为

`φ_ν(u)=φ_μ(ru) exp((r²-1)|u|²/2)`.

R12 的 uniform sub-Gaussian bound 使所有 exact 原像 tight。若 `r_k→∞`，
则 `κ_m(ν_k)=r_k^mκ_m(μ)` 与统一矩界冲突，除非 `κ_m(μ)=0` 对所有
`m≥3`；矩确定性再给出 Gaussian。因此非 Gaussian exact law 的 `r(μ)` 有限。
取 `r_k↑r(μ)` 时，原像 subsequence 的弱极限仍 exact（uniform
integrability 保留均值和方差），并实现上述候选，故 primitive endpoint 可在
概率律层面取到。该 endpoint 未必属于原先要求的 `L²` 密度或 K-tensor
正则类；在 endpoint 上使用 `D` 或 K 恒等式必须另加正则性。

若 `μ` exact，则

`r(P_tμ)=r(μ)/√t`,  `Π(P_tμ)=Π(μ)`,

其中 `Π(μ)` 是最大反向半径处的 primitive representative。第一式的反向
方向来自特征函数消去：若 `P_tμ=P_{R^{-2}}ν`，先用
`R≥t^{-1/2}`，再得 `μ=P_{1/(tR²)}ν`（即反向半径为 `√t R`）。

### 8.2 可行的 OU-invariant shape 与其局限

令 `a_n(μ)=E_μ[H_n(X)/√(n!)]`。对非 Gaussian exact law，令 `d≥3`
为第一个非零 Hermite moment；矩确定性保证这样的 `d` 存在。OU 缩放为
`a_d(P_tμ)=t^{d/2}a_d(μ)`，因而

`Θ(μ)=r(μ)|a_d(μ)|^{1/d}=|a_d(Π(μ))|^{1/d}>0`

是 primitive shape 上的 OU-invariant。它说明“振幅坐标”和“primitive 形状”
可以分离，但并不说明 primitive shape 必须 Gaussian。

对 R13 的 residual-Fisher anchor `F_μ(a)=𝒟^μ_{ρa,a}`，在 score 展开
和相应可积性成立的条件下，若首个非零阶为 `d`，则

`F_μ(a)=C_{d,ρ}a^{d-1}|a_d(μ)|²+o(a^{d-1})`,

`C_{d,ρ}=d E_{Ξ∼N(0,ρ/3)} Var_Z[ψ_{d-1}(Ξ+√(1-ρ)Z)]>0`.

特别地，直接计算得 `C_{3,ρ}=(1-ρ)(3-ρ)`。并且 profile scaling 为
`F_{P_tμ}(a)=tF_μ(ta)`，所以这个小 `a` anchor 只测得 primitive
shape 的局部系数，不能直接被 R11 的 fixed-`s` 深度界控制：对
`μ_t=P_tΠ(μ)`，它按 `t^d` 衰减，而 primitive invariant 不变。

### 8.3 严格 obstruction：深度只改变 orbit coordinate

任意 depth-`N` Case B 首层 `μ_N` 都有
`r(μ_N)≥ρ^{-N/2}`，故可写成

`μ_N=P_{t_N}π_N`,  `t_N≤ρ^N`,  `r(π_N)=1`.

于是 R11 的 `O(ρ^N)` 只约束 orbit coordinate `t_N`；任何真正 OU-invariant
的 `Θ` 或 primitive anchor 只看 `π_N`。两者合并仍不能排除一列 primitive
shapes，除非先证明 primitive exact shape 的全局唯一性。这避免把
“amplitude decays”误写成“shape rigidity”。

R12 的概率紧性还把剩余缺口精确化为 Bochner/Fourier 尾障碍：若 primitive
`π_N` 弱收敛到 Gaussian，则每个固定阶 Hermite coefficient 都消失；但对
固定 `r>1`，逆 OU 候选

`Φ_{N,r}(u)=exp((r²-1)|u|²/2) φ_{π_N}(ru)`

对每个 `N` 仍不是 characteristic function。任何负的 positive-definiteness
witness 若不能在有界频率、固定 Gram 大小、非退化点配置中取得统一 margin，
就只能向频率无穷、Gram 尺寸无穷、点配置退化或 margin→0 逃逸。这是
global inverse-OU spectral tail escape，而不是 physical `X`-tail escape。

`P₃K≠0` 仍是独立 sector：若 primitive 的首个非零密度 Hermite mode 为
`d=3`，则小 `t` 时 `P_tπ=1+t^{3/2}a_3ψ_3+O(t²)`，局部可保留该 charge；
`d>3` 或一般非线性 `P₃K` 沿 primitive normalization 的存活仍 OPEN。

因此新的最小 OPEN 是：

### Primitive Exact Shape Rigidity / Bochner-Tail Closure — OPEN

是否存在 genuine full-exact primitive laws `π_N`，满足 `r(π_N)=1`、
`π_N⇒γ`，且对每个 `r>1` 其 inverse-OU 正定性失败只能发生在无界频率、
无界 Gram 尺寸、退化点配置或消失 margin？若 same-factor product 与
all-degree exactness 能排除这种 Bochner-tail escape，才可能得到真正的
primitive shape rigidity。该问题与 `P₃K` charge survival 分开处理。

R13 没有给出 Gaussian rigidity 的无条件证明，也没有真实概率律反例；它把
R11 的 depth decay 与 primitive shape 的逻辑分工固定下来。

## 9. R14：有限复杂度 Bochner 闭合与两种剩余逃逸

### 9.1 逆 OU 候选仍满足完整 exact tensor identity

对 full exact law 的 characteristic function `φ`，取

`a_j(θ)=√(2/3) cos(θ+2π(j-1)/3)`,  `∑_j a_j(θ)^2=1`.

residual radius 的 exactness 等价于 same-factor identity

`⟨∏_{j=1}^3 φ(a_j(θ)u)⟩_θ=e^{-u²/2}`.

对任意 `r>1` 的 inverse-OU candidate
`Φ_r(u)=exp((r²-1)u²/2)φ(ru)`，因为 `∑a_j²=1`，仍有

`⟨∏_j Φ_r(a_j(θ)u)⟩_θ=e^{-u²/2}`.

因此即使 `Φ_r` 已不是 characteristic function，它仍落在完整的
same-factor、all-degree exact equality manifold 上；把 identity 做成任意有限
Gram 点集的 Hadamard tensor lift 也仍成立。结论是：

`same-factor tensor equality ≠ Bochner positivity`.

这排除了“再多写一些 exact 系数/角向恒等式就能检测 primitive boundary”的
路线；真正缺失的结构是 probability cone 的全局正定性。

### 9.2 无条件的 confluent finite-complexity Bochner closure

设 primitive exact laws `π_N⇒γ`，固定 `r>1`，并令

`K_N(u)=exp((r²-1)u²/2) φ_{π_N}(ru)`.

R12 的 uniform square-exponential moment bound 使 `φ_{π_N}` 及每个固定阶导数
在紧区间上一致收敛到 Gaussian；故 `K_N→K_0=e^{-u²/2}` 于每个固定紧区间的
任意固定 `C^k` 拓扑。

对固定 Gram size `m`，令

`D_m[K](x)=det[K(x_i-x_j)]`,
`\widetilde D_m[K](x)=D_m[K](x)/∏_{i<j}(x_i-x_j)^2`.

在 `C^{2m-2}` 收敛下，divided-difference/confluent extension 使
`\widetilde D_m` 连续延拓到碰撞配置。Gaussian kernel 满足

`D_m[K_0](x)=e^{-∑x_i²} det[e^{x_i x_j}]`

以及 Cauchy–Binet 下界：若 `|x_i|≤L`，

`\widetilde D_m[K_0](x)≥e^{-mL²}/∏_{j=0}^{m-1}j!>0`.

所以对每个固定 `r>1、m≤M、L<∞`，充分大的 `N` 使 `K_N` 在所有
`m` 点、`|x_i|≤L` 的 Gram 测试上 PSD；不需要点间 separation。primitive
要求 `K_N` 对每个 `N` 都非 PD，于是任何负 Gram witness 必须满足

`m_N→∞` 或 `diam{x_{N,i}}→∞`

（经过子列）。R13 原先列出的碰撞、Gaussian 小特征值和 negativity margin
消失不再是独立逃逸通道。

### 9.3 为什么有限闭合仍不能推出全局正定

固定频率窗口内让 `m→∞` 时，Gaussian translation kernel 对紧区间对应的
positive integral operator 是 compact，非零特征值趋向零；因此没有
infinite-rank spectral gap。需要的真正条件不是普通 `C^∞_{loc}` 收敛，而是
Gaussian-relative form estimate，例如

`|⟨c,(K_N-K_0)c⟩|≤ε_N⟨c,K_0c⟩`,  `ε_N→0`,

对所有有限点集和系数一致成立。

另外，角向系数满足 `|a_j(θ)|≤√(2/3)<1`，exact identity 只读取更小的
frequency；它没有 inward-to-outward 的正定性传播，故不能把有限频率闭合
自动推到高频。

### 9.4 R14 的 conditional closure 与最小 OPEN

若 same-factor positivity 能证明以下任一项，则 primitive-to-Gaussian 聚集
不可能：

1. 固定 `r_0>1` 下，所有 primitive inverse-PD failure 都有统一有限
   Gram size 和统一有界频率的 negative witness；或
2. 先把任意 PD failure 约化到统一有限频率，再证明上面的 Gaussian-relative
   form estimate。

这两个目标比“Gaussian 局部孤立”更小且可证伪。反之，若二者均失败，则剩余
障碍已精确压缩为 `frequency escape` 或 `spectral-rank/Gram escape`，而不是
物理质量尾部、点碰撞或普通小 margin。

`P₃K` charge survival 仍须单独处理。`d=3` 首模给出强 OU 下的局部存活；
一般 primitive endpoint 的 `K`/score 正则性和 charge 的非恒零性尚未由
full exactness 推出。

R14 没有完成 Gaussian rigidity；它把 primitive 正定性缺口从模糊的
“Bochner tail”压缩成两个无限维通道，并证明完整 exact equality hierarchy
本身不能消灭它们。

## 10. R15：从 Bochner 局部化到 Uniform Inverse-Hankel Rank Closure

### 10.1 无条件局部化 lemma：非正定性在任意小窗口内出现

固定 `r>1`，对 genuine full-exact primitive law `π` 定义逆 OU 候选

`K_r(z)=exp((r^2-1)z^2/2) φ_π(rz)`.

R12 的 square-exponential moment bound 使 `K_r` 成为整个函数，并满足某个
order-2 增长估计；于是其形式逆矩

`m_k^(r)=i^(-k) K_r^(k)(0)`

满足 `|m_k^(r)|≤C_r(B_r√k)^k`。若存在 `L>0` 使核
`K_r(x-y)` 在所有 `x_i∈(-L,L)` 的有限 Gram 测试上都 PSD，则把点配置
通过有限差分压向 `0`，并使用 confluent limit，可得全部逆 Hamburger 矩阵

`H_M^(r)=[m_(j+k)^(r)]_(j,k=0)^M ⪰ 0`.

这里有限差分产生的相位只对应一个对角酉共轭，不改变 PSD。Hamburger 矩
定理给出具有这些矩的概率律；上述 order-2 增长又给出某个 `δ>0` 的
`E exp(δX^2)<∞`，从而矩确定性/整函数恒等定理迫使其 characteristic
function 就是 `K_r`。这意味着 `π` 有半径 `r` 的正 OU 原像，与
`r(π)=1` 矛盾。

因此得到无条件结论：

`primitive + r>1 ⇒ 对每个 L>0，K_r 在 (-L,L) 内都有有限负 Gram witness`.

等价地，逆候选的第一个 Hamburger-positivity failure 阶数

`M_r(π)=min{M:H_M^(r) 不为 PSD}`

必有限；所谓 frequency escape 被排除，剩余的唯一无限维逃逸是
`M_r→∞` 的 Gram/Hamburger rank escape。

### 10.2 Gaussian 聚集时，失败阶数必逃向无穷

若 genuine full-exact primitive laws `π_N⇒γ`，R12 的一致可积性给出每个
固定阶逆矩收敛到 Gaussian 逆矩。因此 Gaussian 的每个固定有限 Hankel
矩阵严格正定，故对固定 `r>1` 有

`M_r(π_N)→∞`.

这不是新的反例，而是对可能反例结构的精确刻画：forward law 保持正、
所有 exact algebraic identities 仍成立，但 inverse formal moment sequence
只在越来越高的 Hamburger 阶数才暴露非正性。

### 10.3 对 Gaussian-relative form estimate 的严格 no-go

在固定窗口 `[-L,L]` 上定义

`R_L(K)=sup |Q_K(c,x)-Q_γ(c,x)|/Q_γ(c,x)`，

其中 supremum 遍历任意有限点集与非零系数。上面的任意小窗口负 Gram
witness 给出 `Q_K<0`，而 Gaussian kernel 对非零指数多项式严格正，故
`R_L(K_r)>1`（可能为无穷）。所以要求 `R_L(K_{N,r})→0` 的 relative
form bound 并非较弱的紧性中间引理；它逐项排除了 primitive law，实质上
已经是 closure theorem。R15 因此把原来的两个候选压缩为一个纯 rank 命题。

### 10.4 正概率 Hermite 模型说明一般紧性不足

为审计“positivity + MGF + near-Gaussian”是否足以统一控制阶数，固定
`r>1`、`t=r^(-2)`，取奇数 `n`、`ψ_(2n)=H_(2n)/√((2n)!)`，令
`b_n=min ψ_(2n)<0`、`A_n=2/|b_n|`，并设

`q_n=1+A_nψ_(2n)`,  `g_n=P_tq_n=1+A_nt^nψ_(2n)`.

`q_n` 是归一化的 signed Gaussian density，`g_n` 对充分大 `n` 为正，且
centered、variance-one、`g_n→1` 于 `L^2`。由 Cauchy–Schwarz 与
`||ψ_(2n)||_2=1`，对每个 `η<1/4` 有一致 square-exponential moment bound。
同时，`q_n` 与 Gaussian 的所有阶 `<2n` 的矩相同，而 q_n 的某个更高阶
Hankel 矩阵必失败；所以 positivity、概率紧性、MGF 和固定阶 Hermite
收敛本身不能给出 uniform inverse-Hankel rank bound。

该模型不是 full exact `Q`-law，不能作为本项目反例；它只严格排除了不含
same-factor full-exact hierarchy 的一般性闭合论证。

### 10.5 R15 的最小 OPEN 与独立的 `P₃K` 缺口

当前最小可证伪命题改为：

### Uniform Inverse-Hankel Rank Closure — OPEN

固定 `r>1`，是否存在 `M(r)<∞`，使每个 genuine full-exact primitive law
的逆 formal moment sequence 都在不超过 `M(r)` 阶暴露 Hamburger 非正性？
即，full same-factor all-degree exact hierarchy 加 forward positivity，
能否阻止 inverse failure order `M_r(π)` 无界？若能，则 primitive-to-Gaussian
聚集立即矛盾；若不能，则需要构造/刻画同时满足 full exactness 的高阶 rank
escape，而不是再追逐频率尾。

`P₃K` 仍单独处理。首个非零 density Hermite mode 为 `d=3` 时有局部 charge
survival；一般仍没有从 nonGaussian 或 inverse-Hankel failure 推出
`P₃K≠0` 的 uniform charge-to-Hankel lemma。

R15 的本机审计结论：逆候选的 order-2 矩增长、局部 Gram PSD 到全部
Hamburger PSD 的有限差分链、Hermite signed-preimage 的正性/MGF 障碍均已
核对；不需要长数值扫描或远程计算。

## 11. R16：Primitive Closedness / Tail-to-Head Viability

### 11.1 逆 Hankel failure 的 Jacobi exit-time 重写

固定 `r>1`，把逆候选的形式矩记为 `m_k^(r)`。在逆 Hankel 前缀仍严格
正定时，形式正交多项式给出 Jacobi 系数 `α_j,β_j`，并令
`S_j=∑_{ℓ=0}^j α_ℓ`。已有的 full-exact Jacobi factorization 可写成

`G_n=(2^n/3^(n-1))(∏_{j=1}^{n-1}β_j)(β_n+S_(n-1)^2-B_n)`.

因此 exactness 在尚未退出的前缀上等价于
`β_n=B_n-S_(n-1)^2`。写
`u_n=S_(n-1)/√B_n`，则 Hankel viability 是
`β_n=B_n(1-u_n^2)≥0`，即 `|u_n|≤1`。

同时，`Q^n` 中最高新偶矩的系数为 `3(2/3)^n`，所以第 `n` 个 full-
`Q` 方程只决定 `m_(2n)`，而 `m_(2n-1)` 不进入该方程：若某变量出现
次数 `2n-1`，其余总次数为 1，中心化给出的 `m_1=0` 使该项消失。由此
得到精确的 triangularity：higher exact equations 不会代数地回头修改已经
选择的低阶 odd controls。`M_r(π)` 可理解为 inverse exact Jacobi control
trajectory 首次离开 `|u_n|≤1` 的 exit-time。

### 11.2 严格 no-go：有限阶 exact/Hankel/forward 检验无法给统一界

任取有限 `M`，把矩设为 Gaussian 矩直到 `2M-2`，取一个足够小的
`m_(2M-1)=ε≠0`，并保持 `m_(2M)` 为 Gaussian 值。Gaussian 的截断
Hankel 矩阵严格正定，故小 `ε` 下仍落在 truncated Hamburger cone 内；一维
截断矩定理给出真实正概率律。它 centered、variance-one、非 Gaussian，且前
`M` 个 `Q`-moments 仍精确等于 `χ²_2`。再作一步正 OU 平滑，仍能通过这些
有限 exact/Hankel/forward-OU 检验。

所以任何只依赖有限多个 `Q`-moments、有限 Hankel block 或有限阶 forward
positivity 的证明，都不能得到 uniform `M(r)`。这不是 full-exact 反例，
只说明若统一阶界成立，其来源必须是 infinite-tail positivity/growth 向
finite-prefix viability 的非局部反馈，而非 finite algebraic elimination。

### 11.3 无条件等价：rank closure 就是 primitive stratum 闭合

令 `E` 为 genuine full-exact probability class，令
`A_M(r)={μ∈E:H_M^(r)(μ)⪰0}`。在 R12 的一致 square-exponential bound
下，`E` 的弱极限保留固定阶矩；R15 的 local-Hamburger lemma 给出

`∩_M A_M(r)=E_r={μ∈E:r(μ)≥r}`.

因此固定 `r>1` 的 Uniform Inverse-Hankel Rank Closure 等价于 primitive
stratum `P={r(π)=1}` 不向 `E_r` 聚集；对所有 `r>1` 合起来，等价于
`P` 在 `E` 中弱闭。换句话说，R16 的核心已经从“找一个神奇的有限
determinant”改写为：full-exact probability cone 中 backward divisibility
depth 是否在弱极限下稳定。普通概率紧性只给出 backward radius 的
upper-semicontinuity，允许极限中 radius 向上跳，尚不足以关闭该缺口。

### 11.4 `P₃K` 必须继续断开

本轮没有得到 `P₃K≠0⇒m_3≠0` 或
`P₃K≠0⇒M_r(π)≤M_0(r)`。即使在首个 density Hermite mode 为 `d=3`
时有 strong-OU 下的局部 charge survival，其振幅仍可任意小，而每个固定
Gaussian Hankel block 都是严格内点；qualitative charge survival 不能推出
uniform rank bound。primitive endpoint 还可能只存在于 probability-law 层面，
不属于 `L²/K` 正则类。因此 charge-to-Hankel bridge 仍是独立 OPEN。

### 11.5 R16 的最小 OPEN

### Primitive Closedness / Tail-to-Head Viability — OPEN

对 genuine full-exact class，证明或否定
`π_N` primitive 且 `π_N⇒π` 是否必推出 `π` primitive；等价地，固定
`r>1` 时，`full same-factor all-degree exactness + forward positivity +
uniform exact-law growth` 是否迫使逆 Jacobi trajectory 在一个
`N`-independent finite order 前离开 `|u_n|≤1`。若不能，可能的结构性
rank escape 必须表现为每个固定前缀趋于 Gaussian，但 exit index
`M_r(π_N)→∞`；这仍只是精确化的可能形态，不是已构造的 full-exact 反例。

R16 的本机审计结论：已核对 triangularity、有限截断 no-go、
`∩_M A_M(r)=E_r` 的适用范围及 `P₃K` 的逻辑断开；未声称 uniform rank
closure 或 Gaussian rigidity 已完成，不需要长数值计算。

## 12. R17：OU–Laguerre 对角化与 All-Degree Spectral-Tail Tightness

### 12.1 genuine full-exact 类的弱闭性与 backward radius

令 `E` 为 genuine full-exact probability class，即 centered、variance-one
且 `Q=∑_{i=1}^3(X_i-X̄)^2∼χ²_2` 的一体分布类，并保留 R12 的一致
square-exponential bound。若 `μ_j⇒μ`，则 `μ_j^{⊗3}⇒μ^{⊗3}`，连续映射
把 `Q` 的分布传到极限；一致可积性保留均值和方差。因此 `E` 弱闭且紧。

固定 `r>1`，逆 OU 可除性类
`E_r={μ∈E:𝔯(μ)≥r}` 满足 `E_r=P_{r^{-2}}(E)`：正向 OU 连续，且 R13
的 reverse-exactness 保证任意实际正原像仍是 full-exact。因此 `E_r` 紧闭，
`𝔯` 在 `E` 上只有上半连续性，允许 primitive 序列的极限出现 backward
radius 向上跳。primitive closedness 需要额外的反向稳定性。

### 12.2 OU–Laguerre 系数的精确对角化

在三个 iid 坐标的 common/residual 正交分解中令

`U=(X_1+X_2+X_3)/√3=√3 X̄`,  `T=Q/2`.

full exactness 给 `T∼Exp(1)`。以 normalized Hermite
`ψ_ℓ(U)=H_ℓ(U)/√(ℓ!)` 和普通 Laguerre `L_n(T)` 定义

`C_{ℓn}(μ)=E_μ[ψ_ℓ(U)L_n(T)]`.

对三个坐标同时施加 `P_s` 后，common 坐标和二维 residual 坐标分别仍是
OU 变换；`ψ_ℓ` 的特征值为 `s^{ℓ/2}`，`L_n(|R|²/2)` 的特征值为 `s^n`。
因此有精确的概率级恒等式

`C_{ℓn}(P_s μ)=s^{n+ℓ/2}C_{ℓn}(μ)`.

这不是 Gaussian tangent 近似，而是 OU 在 common/residual chaos 上的严格
对角化；本地 `conditional_laguerre_odd_r17` 资产同时核对了 Laguerre 正交、
odd 系数的三角最高矩项和有限条件矩公式。

### 12.3 全阶 inverse-OU spectral viability inequality

对 positive full-exact law `ν`，条件函数
`m_ℓ(t)=E[ψ_ℓ(U)|T=t]` 属于 `L²(e^{-t}dt)`。Bessel/Parseval 给出

`∑_{n≥0}C_{ℓn}(ν)^2≤E_ν[ψ_ℓ(U)^2]≤A_ℓ`,

其中固定 `ℓ` 时 `A_ℓ` 由 R12 growth 一致控制。若 `μ=P_{r^{-2}}ν`，则

`∑_{n≥0} r^{4n+2ℓ} C_{ℓn}(μ)^2≤A_ℓ`.

这是此前缺少的全阶 inverse-OU 加权 viability 约束。特别地，令
`c_n=E[ X̄ L_n(T)]`，则 `C_{1n}=√3c_n` 且 `E U²=1`，从而

`3∑_{n≥0}r^{4n+2}c_n²≤1`.

任一非零 `c_n` 都给出 `𝔯(μ)≤(3c_n²)^(-1/(4n+2))`。但这只控制每个
固定 odd/Laguerre sector 的加权总量，并没有自动给出跨 `n,ℓ` 的 uniform
weighted-tail tightness。

### 12.4 严格 no-go：普通 growth 与任意长 finite prefix 仍不足

固定奇数 `n`，令 `ψ_{2n}=H_{2n}/√((2n)!)`，`b_n=min ψ_{2n}<0`，
`a_n=-1/b_n`，并设相对于 Gaussian 的密度

`g_n(x)=1+a_nψ_{2n}(x)`.

它非负且在最小点触零，centered、variance-one，并因
`a_n=O(n^{1/4})` 而弱收敛到 Gaussian。逆向任何非平凡 OU 原像的候选为
`1+a_nt^{-n}ψ_{2n}`，在最小点为 `1-t^{-n}<0`，所以每个 `g_n` 都 primitive。
生成函数还给出对每个 `η<1/4` 的一致 `E exp(ηX²)` bound。由于
`ψ_{2n}` 与所有次数 `<2n` 的多项式正交，`g_n` 通过
`E Q^j=2^j j!`（`j≤n-1`）的越来越长前缀，但在第 `n` 阶因最高矩已改变
而退出 exactness。

该序列是 ordinary positive/growth 类中的严格 primitive non-closed no-go，
不是 genuine full-exact 反例；它证明有限 exact prefix、普通概率紧性和
固定阶 Hermite 收敛都不能替代“所有阶在同一个概率律上同时 exact”。
特别要保留 `||g_n-1||_2=a_n` 并不趋于零这一点：该例展示的是 weak/MGF
紧性与谱尾紧性的差异，而非 `L²` 近 Gaussian。

### 12.5 当前唯一的全阶闭合目标

如果 primitive closedness 成立，必须存在一种跨所有 conditional/angular
sectors 的 moving-scale 控制，例如对任意弱紧 full-exact 序列和某个固定
`r>1`，逆 OU 权重下的总 chaos/Laguerre/Jacobi 尾满足

`lim_{M→∞} sup_j ∑_{2n+ℓ>M} r^{4n+2ℓ}|C_{ℓn}(μ_j)|²=0`

（或等强的完整 conditional-moment-matrix 版本）。这会把逐项系数收敛
升级为逆 OU 正性的强谱收敛，阻止 backward radius 在极限中向上跳。当前
只得到 sector-wise viability，不得到该 uniform tail theorem。

`P₃K` 仍与此逻辑断开：没有已审计的
`P₃K≠0⇒m_3≠0`、charge-to-Laguerre 下界或 uniform inverse-Hankel bound。
即使 `d=3` 首模在强 OU 下局部存活，其振幅仍可趋零，不能单独关闭谱尾
逃逸。

### 12.6 R17 的最小 OPEN

### All-Degree Spectral-Tail Tightness — OPEN

genuine full-exact same-factor product structure 加 forward positivity，是否
能阻止 OU eigenmode/Laguerre/Jacobi control mass 迁移到总 chaos degree
`∞`，从而把 backward radius 的上半连续性升级为 primitive 序列所需的
下半连续性/闭性？若不能，必须构造真正同时满足 all-degree exactness 的
rank/spectral-tail escape；有限前缀或形式候选不算反例。

R17 的本机审计结论：full-exact 类弱闭/紧、`E_r` 闭、OU–Laguerre 对角化、
`ℓ=1` 加权 Parseval 常数和 boundary Hermite primitive no-go 均已核对；
没有宣称 primitive closedness 或 Gaussian rigidity 已完成，不需要长数值计算。

## 13. R18：Same-Factor Matrix Hardy Gain / Relative Tail-to-Head Coercivity

R18 只攻击 R17 的 `All-Degree Spectral-Tail Tightness`，并先通过连接重新读取
本文件与 `PROJECT_WORKLOG_APPEND.md`。结论不是 primitive closedness 已证明，
而是把缺口进一步定位为“可除层内部已有谱尾控制，但该控制是否对邻域稳定”。

### 13.1 完整 conditional generating function 与矩阵正性

仍令 `U=(X_1+X_2+X_3)/√3`、`T=Q/2∼Exp(1)`，并令 `C_{ℓn}=E[ψ_ℓ(U)L_n(T)]`。
对 `0≤q<1`、`d=1-q`，定义 tilted triple law

`dP_q=d^(-1) exp(-qT/d)d(μ^⊗3)`.

Laguerre 与 Hermite 生成公式给出同时包含所有扇区的二维生成函数

`M_μ(q,z)=E_{P_q} exp(zU-z²/2)=∑_{ℓ,n≥0}C_{ℓn}q^n z^ℓ/√(ℓ!)`.

因此不是若干彼此独立的 scalar sector；对任意复数 `z,w`，

`K_q(z,w)=exp(z\bar w)M_μ(q,z+\bar w)⪰0`,

因为它是 `E_{P_q}[f_z(U)\overline{f_w(U)}]` 的 Gram kernel。利用
`Q=∑X_i²-U²` 的 Hubbard–Stratonovich 表示，还可写成同因子的 cubic form：

`M_μ(q,z)=d^(-1)e^(-z²/2)E_G[A_q((z+√(q/d)G)/√3)^3]`,

其中 `A_q(y)=E_μ exp(yX-qX²/(2d))`。在 `z=0`，full exact law 只给出该表达式的
归一化；尚未给出所需的相对 Hardy 增益。

### 13.2 无条件的完整谱尾结论

令 `a_m(μ)=E_μψ_m(X)`。Mehler 展开及 `2xy≤x²+y²` 给出，对任意 `0<ρ<1`：

`∑_mρ^m a_m(μ)^2≤(1-ρ²)^(-1/2)E exp(η_ρ(X²+Y²))`,

其中 `η_ρ=ρ/(2(1+ρ))<1/4`。结合 R12 的统一 square-exponential bound，
得到在整个 genuine full-exact 类 `E` 上统一的 subcritical Fock 预算。
三重张量在总 chaos degree 上的系数为 `a_i a_j a_k`；common/residual 正交变换
在每个总 degree 内是 unitary，所以对完整 conditional/angular basis 系数
`B_{D,α}` 有

`sup_{μ∈E}∑_{D,α}ρ^D|B_{D,α}(μ)|²≤K(ρ)^3`,  `ρ<1`.

更强地，若 `μ∈E_r`、`r>1`，写 `μ=P_{r^(-2)}ν`、`ν∈E`。OU 对角化给
`B_D(ν)=r^D B_D(μ)`，故对 `1<λ<r²`：

`sup_{μ∈E_r}∑_{D,α}λ^D|B_{D,α}(μ)|²≤K(λ/r²)^3`.

若 `1<λ_0<λ<r²`，还得到指数尾界

`sup_{μ∈E_r}∑_{D>M,α}λ_0^D|B_{D,α}(μ)|²
 ≤K(λ/r²)^3(λ_0/λ)^M`.

这是 R18 的实质推进：跨 conditional/angular sector 的 supercritical moving-scale
tail tightness 在真正的 deeper backward-divisible stratum `E_r` 内已经成立。
但它没有说明 `μ_N∉E_r`、`μ_N⇒μ∈E_R` 时该界能否从极限层传播到邻域。

### 13.3 可除极限提供的矩阵 margin 与 conditional closure

若 `π∈E_R` 且 `1<r<R`，写 `π=P_{R^(-2)}ξ`，则它的 `r`-原像为
`ν_r=P_sξ`，`s=r²/R²<1`。由 centered/variance-one 的 Chebyshev 下界，
`ξ([-2,2])≥3/4`；OU 核因此给出：对任意 `0<τ<1-s`，存在 `c>0` 使

`ν_r(dx)≥cγ_τ(dx)`,  从而  `L_{ν_r}(p²)≥cE_{γ_τ}p²`.

所以若 `π_N⇒π∈E_R` 且固定 `r<R` 的 inverse formal moment functionals 满足

`sup_{p≠0}|(L_{N,r}-L_{ν_r})(p²)|/E_{γ_τ}p²→0`,

则最终所有 polynomial square 上 `L_{N,r}≥0`。结合 R15 的 inverse moment growth、
Hamburger determinacy 和 same-factor exact identities，可恢复真实正的 `r`-原像，
从而排除 primitive 序列收敛到 `E_R`。这说明真正足够的假设是相对于 smoothed
preimage form 的 operator/Loewner 尾控制，而不是普通的 scalar Parseval 界。

### 13.4 严格 no-go 与 P₃K 边界

完整 conditional/angular moment-matrix 正性、精确径向律和统一 growth 单独仍不够。
可取 `T∼Exp(1)`、均匀角变量和独立 Gaussian，令
`U_ω=σ_ωZ+ε(cos(ωT)-(1+ω²)^(-1))`，再以 common/residual 正交变换还原三坐标。
这给出真实、交换对称、centered/variance-one、`Q∼χ²_2` 且 growth 一致的三元律，
其 Laguerre 生成函数含因子

`1/(1+ω²(1-q)²)-1/(1+ω²)`,

复奇点趋近 `q=1`，因此谱质量可向无限 Laguerre degree 逃逸。该例不是 iid
`μ^⊗3`，故绝不是项目的 genuine full-exact 反例；它严格说明必须真正使用
same-factor iid cube，不能只依赖条件/角向 PSD。

`P₃K` 仍逻辑断开。没有已审计的 charge-to-Laguerre 或 charge-to-Loewner 下界，
`P₃K≠0` 仍允许固定 charge 落在 `n→∞` 的径向尾上；不能据此推出 uniform
backward-Hankel 阶界或 primitive closedness。

### 13.5 R18 结论与 R19 最小 OPEN

无条件保留：完整二维生成函数的矩阵正性、same-factor cubic representation、
整个 `E` 上的 subcritical 全谱紧性，以及 `E_r` 内的 supercritical moving-scale
尾界。严格 no-go 保留为非 iid exchangeable 模型，不能升级为项目反例。

当前最小 OPEN 改为：

### Same-Factor Matrix Hardy Gain / Relative Tail-to-Head Coercivity — OPEN

对 `π_N⇒π∈E_R`、`r<R`，能否从 genuine iid same-factor cube 与 all-degree exactness
推出相对于 `L_{ν_r}` 的矩阵型估计，使 `E_R` 内的 supercritical 尾界对邻域稳定，
进而阻止 backward radius 的 upward jump？Gaussian rigidity 仍未完成；目前没有
真正的 full-exact rank/spectral-tail escape 反例。

R18 的本机动作只需 proof-level audit：既有 `conditional_laguerre_odd_r17` 与
`laguerre_abel_endpoint_r18` 重放均通过；不启动优化、数值扫参、Gram campaign 或
远程计算。

## 14. R19：Same-Factor Uniform Witness Alignment / Reverse-Schur Coercivity

R19 在读取 R18 的本机提交 `8d38b82` 后，继续只研究 genuine full-exact iid 类
中的 relative matrix/Loewner closure，不声称 Gaussian rigidity 已完成。它把
R18 的尾到头问题进一步改写成 posterior Gaussian deconvolution 的高秩见证人
对齐问题。

### 14.1 Gaussian-component 共轭

定义 centered variance-one 概率律的最大 Gaussian component 方差

`g(mu)=sup{a in [0,1]: mu=rho*gamma_a}`。

在 R13 的 backward-radius 记号下，网页端给出并使用
`g(mu)=1-r(mu)^(-2)`。对二次/Esscher posterior

`A_t^mu(y)=E_mu exp(yX-tX^2/2)`,

`d mu_(t,y)(x)=exp(yx-tx^2/2) dmu(x)/A_t^mu(y)`,

Gaussian convolution 的 complete-the-square 计算给出精确共轭

`g(mu_(t,y))=g(mu)/(1+t*g(mu))`。

因此 posteriorization 不会把 primitive boundary 变成内部点，而是精确保留它；
同时若 `pi in E_R`，每个固定 slice 都保留显式的 Gaussian component。

### 14.2 固定半径的 posterior Wick–Hankel cone

固定 `r>1`，令 `d_r=1-r^(-2)`，并设

`sigma_(r,t)^2=d_r/(1+d_r*t)`,

`B_(r;t,y)^mu(z)=exp(-sigma_(r,t)^2 z^2/2) A_t^mu(y+z)/A_t^mu(y)`。

在已有 moment-growth/determinacy 条件下，`mu in E_r` 等价于一个（事实上任一）
固定 `(t,y)` 的 `B_(r;t,y)^mu` 是概率律的 MGF，等价地其完整
exponential-convex/Wick–Hankel cone 成立。对应的多项式二次型为

`W_(r,t,y)^mu[p] = E_(mu_(t,y))[(exp(-sigma_(r,t)^2 partial_x^2/2) p^2)(X)]`。

其 rank-2 条件恰为
`Var_(mu_(t,y))(X) >= sigma_(r,t)^2`；但 rank-2 通过仍不等价于 Gaussian
可除性，全部 Wick–Hankel ranks 仍不可省略。

### 14.3 只需一个固定 slice 的 conditional closure

对 `pi_N=>pi in E_R`、`1<r<R`，若能对某个固定 `t>0`（甚至 `y=0`）证明

`sup_(p ne 0) |W_(r,t,0)^(pi_N)[p]-W_(r,t,0)^pi[p]| /
 E_(gamma_tau) p^2 -> 0`,

其中 `tau` 小于极限 posterior 的严格 Gaussian 余量，则该余量会使充分大的
`N` 满足完整 Wick–Hankel 正性；结合已有 Hamburger determinacy，得到
`pi_N in E_r`，从而排除 primitive 序列收敛到 `E_R`。这把 R18 的 relative
matrix target 缩成了一个固定 slice 的 relative Wick–Hankel convergence 问题。

### 14.4 same-factor cube 的精确重写与量词障碍

令
`d eta_t(y)=(1+t) A_t^mu(y)^3 d gamma_(t/3)(y)`。

对 residual unit vector `alpha(theta)` 满足 `sum_j alpha_j=0`、`sum_j alpha_j^2=1`，
R19 将 genuine iid same-factor all-degree exactness 重写为

`E_(eta_t) <prod_(j=1)^3 B_(r;t,Y)^mu(z alpha_j(theta))>_theta
 = exp(delta_(r,t) z^2/2)`,

其中
`delta_(r,t)=r^(-2)/((1+t)(1+d_r*t))`。

二阶项只给出 posterior variance deficit 的正平均值，不能直接给出每个 slice
的 pointwise Loewner floor。于是 primitive `pi_N` 只能推出

`for every y, there exists a high-rank p_(N,y) with W_(r,t,y)^[pi_N][p_(N,y)]<0`,

而 cubic escort 平均要检测的是一个在一批 `y` 上同时有效的共同见证人。R19
因此把精确缺口定位为
`uniform high-rank witness alignment / inverse-Schur localization`：
`(for all y exists witness_y)` 并不自动推出
`(there exists one coherent witness detectable by the iid cubic average)`。

这是相对于 R18 的新定位；不是普通 Parseval 尾界、局部 entire 收敛或低阶
log-convexity 能补上的量词转换。

### 14.5 严格边界、P₃K 与本机审计

- 普通 log-convexity 只控制 rank 2；固定 damping/posteriorization 与原 Gaussian
  divisibility 问题精确共轭，不会自行改善闭合性。
- Hubbard–Stratonovich cube 是正向的 escort-averaged Hadamard/cubic identity；
  当前没有可用的 reverse-Schur theorem 将其反推为逐 slice 的矩阵正性。
- 平移只把 escort 参数重命名，不能把平均局部化到坏 slice；指数 tilt 又不一般
  保留精确 `Q`-law。
- `P₃K` 仍与 closure 逻辑断开。没有定量 charge-to-Laguerre、charge-to-Loewner
  或固定秩负下界，`P₃K != 0` 仍可能沿径向 `n -> infinity` 逃逸。
- 本机新增 `posterior_witness_alignment_r20/audit_r20.py`，通过 Gaussian-component
  共轭、posterior 逆卷积矩、严格 gap、Gaussian escort identity/normalization 和
  translation covariance 六项检查，输出 `R20_AUDIT_COMPLETED`。其中 Gaussian
  检查只是一致性核验，不是一般性证明。

### 14.6 R19 结论与 R20 最小 OPEN

无条件保留：posterior Gaussian-component 共轭、固定 slice 的 Wick–Hankel
criterion、`E_R` 对 `r<R` 的严格 Gaussian margin，以及 same-factor cubic identity
的 posterior 重写。严格 no-go 是量词/见证人对齐障碍；没有构造 genuine full-exact
iid 非闭合序列。

当前最小 OPEN 改为：

### Same-Factor Uniform Witness Alignment / Reverse-Schur Coercivity — OPEN

对 genuine full-exact iid law，same-factor cubic identity 是否迫使所有 posterior
Wick–Hankel failure 共享一个可控的 degree/Loewner complexity，或等价地推出一个
固定 slice 的 relative operator estimate？若能，primitive closedness 随即闭合；
否则需要在 iid 约束下给出最小无条件 no-go。Gaussian rigidity 与 `P₃K` bridge
仍然分别 OPEN。

## 15. R20：Affine-Hankel Diagonal-Capture / Multiscale Reverse-Schur

R20 在读取 R19 的本机提交 `7ec40ac` 后，继续严格限制于 genuine full-exact iid 类。
本轮证明了 posterior 参数 `y` 的见证人对齐并非真正缺口；剩余问题是同一 Hankel
负方向在三个 residual affine scales 上的共同可见性，以及它在 same-factor
Hadamard cubic 的 diagonal tensor channel 中是否具有维数无关的捕获量。Gaussian
rigidity 仍未完成。

### 15.1 posterior slices 的精确 Esscher–affine 共轭

固定 `r>1,t>0`，写
`sigma^2=(1-r^(-2))/(1+t(1-r^(-2)))`，并令
`C(z)=B_(r;t,0)^mu(z)`。直接从 R19 的定义得到

`B_(r;t,y)^mu(z)=exp(sigma^2*y*z) C(y+z)/C(y)`。

因此对 Hankel Gram `H_y(s)_(ij)=B_(r;t,y)(s_i+s_j)`，置
`w_i=s_i+y/2`、`D_y=diag(exp(sigma^2*y*w_i))`，有

`H_y(s)=exp(-sigma^2*y^2)/C(y) * D_y [C(w_i+w_j)] D_y`。

前面的标量严格为正、`D_y` 可逆，且 `w_i` 在实轴上可任意取值。因此每个
posterior slice 与同一个 base kernel 只差平移节点、正对角 congruence 和正标量；
最小负 Gram 尺寸完全不依赖 `y`。负 witness 还能按
`s_i(y)=w_i-y/2`、`c_i(y)=exp(-sigma^2*y*w_i)v_i` 显式搬运到所有 slices。
非零 residual dilation 也不改变这一复杂度。

这给出一个无条件修正：R19 的 `for every y exists witness_y` 量词障碍在单因子层面
已经解决；真正剩下的是三重 affine/multiscale 对齐，而不是 posterior-`y` 对齐。

### 15.2 same-factor cubic 是 diagonal tensor compression

对任意同阶矩阵 `A_1,A_2,A_3`，令
`J e_i=e_i tensor e_i tensor e_i`，则精确有

`A_1 o A_2 o A_3 = J^*(A_1 tensor A_2 tensor A_3)J`。

所以 same-factor cubic 只观察 full tensor product 在
`Ran(J)=span{e_i tensor e_i tensor e_i}` 上的压缩。对单位负方向
`v_1,v_2,v_3`，其 diagonal capture 量是

`C(v_1,v_2,v_3)=sum_i |v_(1,i)v_(2,i)v_(3,i)|^2`。

在 residual coefficients `alpha_j(theta)` 下，三个 factor 实际来自同一个 `C`
在 `y/2+alpha_j(theta)s` 上的三个 affine copies。因而所需结构不是普通 reverse-Schur，
而是同时控制 multiscale affine alignment 与 diagonal-tensor capture。

### 15.3 严格的 generic reverse-Schur no-go

取 `m>=5`、`a=3/5` 的三对角 Toeplitz 矩阵
`A_m=I+a(S+S^*)`。其特征值为
`1+(6/5)cos(k*pi/(m+1))`，所以 `lambda_min(A_m)<0`；但

`A_m^(o3)=I+(27/125)(S+S^*)`

的最小特征值为
`1-(54/125)cos(pi/(m+1))>71/125>0`。

因此 `A_m` indefinite 而 entrywise cube 严格正定。其最低特征向量是 spread-out
sine mode；归一化后
`sum_i |v_i|^6 <= 8m/(m+1)^3 <= 8/m^2`，故负方向在 diagonal channel 中
可随维数消失。这个例子不是概率律、不是 exact iid 反例，但严格排除了仅凭 generic
Loewner indefiniteness 反推 Hadamard cubic negativity 的维数无关策略。

### 15.4 conditional closure

对 `pi_N=>pi in E_R`、`1<r<R`，若每个负 inverse-Hankel direction 都能在三个
residual affine copies 上选择匹配的方向，使负 spectral margin 有统一 relative
下界，并且

`integral sum_i |v_(N,1,i)v_(N,2,i)v_(N,3,i)|^2 d(eta_t x theta) >= kappa>0`,

同时非负 spectral remainder 具有 dimension-independent domination，则 diagonal
compression 不能抹掉负性；它会给出与 exact Gaussian cubic RHS 的 PSD 矛盾，继而在
固定 posterior slice 得到 Wick–Hankel 正性并排除 primitive rank escape。这里必须同时
要求 remainder domination；单独的 overlap 下界不足以保证压缩后的 Rayleigh quotient
为负。

### 15.5 P₃K 与 R20 缺口仍断开

本轮没有得到 `P₃K` 到 diagonal capture、Laguerre rank 或 relative Loewner norm 的
定量桥。`P₃K != 0` 仍不能推出
`C(v_1,v_2,v_3)>=kappa`，也不能阻止 Hankel/radial rank 趋于无穷；因此 P₃K
继续与 R20 closure 逻辑断开。

### 15.6 R20 结论与 R21 最小 OPEN

无条件保留：posterior slices 的 Esscher–affine congruence、slice-wise witness
complexity 不变、Hadamard cubic 的 diagonal compression 公式，以及 Toeplitz
矩阵给出的 generic reverse-Schur no-go。没有构造 genuine full-exact iid 非闭合序列。

当前最小 OPEN 改为：

### Affine-Hankel Diagonal-Capture / Multiscale Reverse-Schur — OPEN

genuine full-exact iid same-factor Hankel kernels 是否能排除这样的 rank escape：负
eigendirections 的 rank 趋于无穷，同时在三个 residual affine contractions 下的
coordinatewise tensor overlap 趋于零，使 negativity 对 Hadamard diagonal compression
渐近不可见？若能建立 Hankel-specific、维数无关的 diagonal-capture/coercivity，R18
的 relative matrix closure 才能完成；否则还需寻找真正的 full-exact iid 实现或更小的
不可避免障碍。

本轮本机新增的 proof-level audit 核验了 Esscher–affine congruence、Hadamard diagonal
compression、Toeplitz eigenvalue no-go 及 `O(m^(-2))` capture bound；输出
`R20_AUDIT_COMPLETED`。这些是代数/一致性核验，不是 Gaussian rigidity 证明。

## 16. R21：Post-Failure Tensor-Tail Domination

R21 在读取 R20 的本机提交 `8075da1` 后，继续严格限定 genuine full-exact iid
inverse formal hierarchy。它把 R20 的 generic diagonal-capture 问题推进到
Hankel-specific 的 first-failure 分解：一级负 pivot 的可见度确实指数衰减，因而
任何只依赖 first failing block 的维数无关 reverse-Schur 结论都不可能成立；但
degree `3M` 的 triple-pivot 项又有组合学放大，所以不能把一级 no-go 误读成
whole-cubic no-go。

### 16.1 完整二维 residual rotational lift

取 `A:R^3 -> R^2` 满足
`A A^T=I_2`、`A^T A=I_3-11^T/3`，则 `|A X|^2=Q`。在已有固定半径
inverse formal functional `Lambda_r` 与 all-degree exactness 下，对任意二维实多项式
`F` 有

`integral_SO(2) Lambda_r^(tensor 3)[F(O A X)^2] dO
 = E_(gamma_2) F(G)^2`。

理由是 SO(2) 平均后的 `F^2` 是 `|A X|^2=Q` 的多项式，因而只调用 exact
`Q~chi^2_2` 的全部矩。这里的“无条件”仅指在已有 genuine exact formal hierarchy
内的代数 lift；`Lambda_r` 本身未必正，因此这不是概率律反例或 positivity 结论。

### 16.2 first-failure 的精确负通道

假设 first inverse-Hankel failure 在 `M`，先取非退化情形
`H_(M-1)(Lambda_r) ≻ 0`、`H_M(Lambda_r) not >= 0`。令 `P_k` 为 monic formal
orthogonal polynomials，`Lambda_r(P_j P_k)=h_k delta_jk`，于是
`h_0,...,h_(M-1)>0`、`h_M<0`。对 degree-`M` 二维多项式 `F`，最高齐次部为
`H_M`，将 `F(O A X)` 展开到 `P_(k_1)(X_1)P_(k_2)(X_2)P_(k_3)(X_3)`，则

`Lambda_r^(tensor 3)[F(O A X)^2]
 = h_M sum_j |H_M(O v_j)|^2 + R_F(O)`,

其中 `v_j` 是 `A` 的列，`|v_j|^2=2/3`，且 `R_F(O)>=0`，因为其余项只含
`h_0,...,h_(M-1)`。这是精确的 triangular decomposition，不是切向近似。

旋转平均给出

`integral sum_j |H_M(O v_j)|^2 dO
 = 3(2/3)^M ||H_M||_(L^2(S^1))^2`。

所以 first pivot 在完整二维 residual polynomial test space 中仍只以
`3(2/3)^M` 的几何系数进入可见通道。更强地，若
`alpha_j(theta)` 是三列的 residual coordinates，则
`sum_j |alpha_j(theta)|^(2M) <= (2/3)^(M-1)`；局部化 angular variable 也不能消除
这一级指数损失。

### 16.3 iid-compatible 的一级 reverse-Schur no-go

对 ridge `H_M(u,v)=u^M`，有
`||H_M||_(L^2(S^1))^2=binom(2M,M)/4^M`，故 capture multiplier 正好是

`lambda_(2M)=3(2/3)^M binom(2M,M)/4^M
 ~ 3/(sqrt(pi M)) (2/3)^M`。

它与早期 uniform-Fock 路线的偶模 multiplier 一致，说明 inverse-Hankel diagonal
invisibility 与 residual angular inverse 的 exponential loss 是同一个内禀谱。
因此严格可以排除：任何只使用 first failing Hankel block `H_M` 的 dimension-free
reverse-Schur/coercivity theorem。这个 no-go 发生在 genuine iid residual geometry
内部，但不是 genuine full-exact primitive sequence 的构造。

### 16.4 cubic 的 triple-pivot amplifier

不能停在一级 no-go，因为 degree `3M` 的 ridge `S_theta^(3M)` 在 tensor orthogonal
expansion 中含有 `(M,M,M)` 项，其系数平方的 angular average 为

`Gamma_M = ((3M)!/(M!^3))^2 * (1/54^M) * binom(2M,M)/4^M`

并且 Stirling 给出
`Gamma_M ~ 3/(4 pi^(5/2)) * (27/2)^M / M^(5/2)`。

它对应 `h_M^3<0` 的真正 triple-negative channel，呈指数放大而非衰减。因此
same-factor cubic 不能被 R21 的一级 no-go 判死刑。

### 16.5 当前闭合仍缺 post-failure tail domination

degree `3M` 的一般测试满足
`Lambda_r^(tensor 3)[F(O A X)^2]=sum_k |c_k(O)|^2 h_(k_1)h_(k_2)h_(k_3)`。
我们只知道 `h_k>0`（`k<M`）和 `h_M<0`；`h_(M+1),...,h_(3M)` 的 signs/sizes
以及所有其它 partitions 尚无统一控制。故 amplified `(M,M,M)` 项可能仍被
post-failure Jacobi/tensor tail 抵消。

一个足够的 conditional closure 是：若 forward positivity、exact-law growth 与
Jacobi dynamics 能对某个 degree-`3M` test 给出

`R_M <= (1-epsilon) Gamma_M |h_M|^3`,

其中 `R_M` 汇总所有非 `(M,M,M)` partitions，则 exact Gaussian radial identity
与 `h_M^3<0` 矛盾，primitive rank escape 被排除。这里的关键不是再寻找一级
diagonal capture，而是控制 `M<k<=3M` 的 post-failure Jacobi tail。

### 16.6 P₃K 仍然独立

三列 residual coefficient 的乘积出现 `cos(3 theta)`，只是 residual cubic angular
harmony，不是 nonlinear log-density charge `P_3K`。本轮没有得到
`P_3K != 0` 到 `|h_M|`、`Gamma_M|h_M|^3` 或 `h_(M<k<=3M)` 的定量桥；因此
`P_3K` 继续与 R21 closure 断开。

### 16.7 R21 结论与 R22 最小 OPEN

无条件保留：二维 rotational lift、first-failure 的精确负通道分解、一级
`3(2/3)^M` capture loss、与旧 Fock multiplier 的一致性，以及 triple-pivot
系数 `Gamma_M` 的组合学放大。严格 no-go 仅针对“只用 first failing block 的
dimension-free reverse-Schur”；没有构造 genuine full-exact iid 非闭合序列。

当前最小 OPEN 改为：

### Post-Failure Tensor-Tail Domination — OPEN

对 genuine full-exact iid inverse formal trajectory，若 `M` 是第一个负 Hankel/Jacobi
pivot，能否由 forward positivity、simultaneous all-degree exactness 和 growth
控制 `M<k<=3M` 的 Jacobi/tensor tail，使 degree-`3M` 的 amplified
`Gamma_M h_M^3` 不被其它 partitions 抵消？这决定 cubic 是否必然暴露第一个
negative Hankel pivot，并决定 primitive closedness 能否完成。

本轮新增 `post_failure_tensor_tail_r21/audit_r21.py` 与 README，核验 residual
projection geometry、rotational polynomial lift、first-failure capture/ridge
multiplier、`Gamma_M` 精确式和 Stirling 尺度；运行输出 `R21_AUDIT_COMPLETED`。
这些是 proof-level 代数/尺度核验，不是 Gaussian rigidity 证明。

## 17. R22：Adjacent Heat-Hankel Transversality / Flat-Leakage Control

R22 在读取 R21 的本机提交 `13f36d2` 后，继续严格限定 genuine full-exact iid
inverse formal hierarchy。它没有证明 `Post-Failure Tensor-Tail Domination`，但把
缺口再压缩到相邻 Hankel determinants 的跨 rank 小值/零点几何：forward positivity
给每个 rank 一个全阶正系数 heat expansion，却尚未给出不同 rank 之间的相对控制。

### 17.1 forward positivity 的 heat-Hankel alternating 展开

固定 `r>1`，令 `b=r^2-1`，把真实 positive exact law 缩放为
`tilde(mu)=D_r mu`。固定半径的 inverse formal functional 满足
`M_(Lambda_r)(z)=exp(-b z^2/2) M_(tilde(mu))(z)`。令

`D_n(L)=det[L(x^(i+j))]_(i,j=0)^n`,
`V_n=prod_(i<j)(x_j-x_i)`, `N_n=n(n+1)/2`。

Vandermonde 是 harmonic polynomial，且

`D_n(L)=1/(n+1)! L^(tensor(n+1))[V_n^2]`,

`exp(a Delta/2)V^2=sum_alpha a^|alpha|/alpha! (partial^alpha V)^2`。

代入负 heat time `a=-b` 得到

`D_n(Lambda_r)=sum_(k=0)^(N_n) (-b)^k C_(n,k)(tilde(mu))`,

其中每个 `C_(n,k)>=0`，最高系数为
`C_(n,N_n)=prod_(j=0)^n j!`。这是 genuine forward positivity 给出的全阶
约束，不是 formal positivity；但负 heat time 使其表现为 alternating cancellation。

### 17.2 仍没有 cross-rank tail control

即使已知 `D_j(-b)>0`（`j<M`）而 `D_M(-b)<0`，上述展开对每个 `n` 使用的仍是
不同的正系数数组 `(C_(n,k))`。它没有推出
`D_(M+1),...,D_(3M)` 的 zero interlacing、small-value transversality、相对
determinant bound 或 flat-leakage horizon。R12 的 moment growth 最多提供绝对尺度
上界，不能防止 `|D_M|` 接近零，因此不能直接支持 cubic amplifier 所需的
relative Jacobi ratio estimate。

### 17.3 flat-Hankel crossing 与 leakage

在 flat 点若 `H_(M-1) ≻ 0`、`H_M >= 0` 且 `D_M=0`，则新增的 monic null
polynomial `P_M` 只给出 corank-one flat block。沿 forward heat parameter `a`，
`h_M` 的导数满足

`d h_M/da = L_a[(partial_x P_M)^2]`,

并在 flat 点有
`h'_M >= M^2 h_(M-1)>0`。所以非退化 flat crossing 是横截的，`D_M` 沿
backward 方向线性穿过零点。

令 `ell_M=L_*(P_M x^(M+1))`。换到
`P_0,...,P_(M-1),P_M,Q_(M+1)` 的基后，flat 尾块给出精确公式

`D_(M+1)(b_*)=-D_(M-1)(b_*) ell_M^2 <=0`。

若 `ell_M != 0`，越过 crossing 进入 `h_M<0` 后通常有 `h_(M+1)>0`；最近的
`(M-1,M,M+1)` tensor sector 因而会帮助负的 `h_M^3`，而不是自动抵消它。真正
困难的是 `ell_M=0` 的 coherent leakage delay。若 leakage 无限延迟，会落入有限
原子 flat extension，与完整连续 `chi_2^2` 径向律冲突；但现有 triangularity
没有给出 uniform leakage horizon，有限 flat branch 也能通过许多后续 `Q`-moment
方程。

对固定可数序列，`D_n(r)` 关于 `r` 为 real analytic 且 `D_n(1)>0`，因此可以在
`(1,R)` 选 generic `r` 避开全部 determinant zeros，使每个单独轨迹 quasi-definite。
这只解决固定序列的坐标合法性，不提供 near-flat 的 uniform coercivity。

### 17.4 degree `3M` 的结构性污染与相邻系数障碍

任何非零 degree-`3M` residual top part `H_(3M)` 在旋转平均中都带来非零的
`h_(3M)` channel，系数为
`3(2/3)^(3M)||H_(3M)||_(L2(S1))^2`。所以想利用
`P_M(X_1)P_M(X_2)P_M(X_3)` 的 triple pivot，不能通过选择测试多项式彻底绕开
post-failure horizon。

若最高齐次 residual polynomial 的 central coefficient 为 `c_(M,M,M)=c`，
translation invariance `partial_1+partial_2+partial_3=0` 强制相邻六个系数满足

`sum_six |c_(a,b,c)|^2 >= 3M^2/(2(M+1)^2) |c|^2`。

这些 sector 都带 `h_(M-1)h_M h_(M+1)`。当 `h_M<0`、`h_(M+1)<0` 时它们是正
贡献；若
`beta_(M+1)/|beta_M| >= 2(M+1)^2/(3M^2)`，则相邻正项已足以压过 central
`h_M^3` 项本身。故 R21 的 `Gamma_M h_M^3` 不能脱离 one-step post-failure
ratio 单独统治 remainder。

### 17.5 exact triangularity 与绝对 growth 不足以控制 ratio

Jacobi recursion 中 `beta_(M+1)=B_(M+1)-S_M^2`，而
`alpha_M=L(xP_M^2)/h_M` 的分母在 near-flat 时爆炸。`L(xP_M^2)` 对新奇矩
`m_(2M+1)` 的系数为 1，且第 `M+1` 个 `Q`-exact 方程不含该新奇矩；因此
triangularity 仍允许调节它来延迟 leakage。由

`|beta_(M+1)/beta_M|=|D_(M+1)|D_(M-1)^3/(|D_M|^3 D_(M-2))`,

可以看出绝对 moment growth 并不给所需的 relative bound。R22 因而排除了两条
策略：只用 first failure block 的 cubic 证明，以及只用 exact triangularity 加
绝对 growth 推出 post-failure ratio 控制。

### 17.6 P₃K 与 R22 仍断开

`cos(3 theta)` 只来自 residual cubic harmonic，不是 nonlinear log-density charge
`P_3K`。本轮没有得到 `P_3K != 0` 到 `|ell_M|`、Jacobi ratio、determinant
zero geometry 或 tail domination 的定量桥。因此 P₃K 继续与 R22/R23 closure
逻辑断开。

### 17.7 R22 结论与 R23 最小 OPEN

无条件保留：forward positivity 的 heat-Hankel 正系数展开、flat crossing 横截性、
flat leakage 行列式、degree `3M` 对 `h_(3M)` 的结构性污染，以及相邻系数/ratio
障碍。没有证明 post-failure tensor-tail domination，也没有构造 genuine full-exact
iid 非闭合序列。

当前最小 OPEN 改为：

### Adjacent Heat-Hankel Transversality / Flat-Leakage Control — OPEN

对 genuine full-exact iid inverse heat-Hankel trajectory，若 `M` 是第一个 negative
rank，forward positivity 与 same-factor all-degree exactness 是否迫使 flat null
relation 在可控 horizon 内 leakage，或在 `h_M,h_(M+1)<0` 的情形给出足够的
`beta_(M+1)/|beta_M|` uniform bound？若连这一阶都无法控制，R21 的 triple-pivot
amplifier 不能启动；若能，再向 `M+2,...,3M` 迭代。

本轮新增 `post_failure_tensor_tail_r22/audit_r22.py` 与 README，核验 Vandermonde
harmonic heat identity、flat crossing、flat leakage、adjacent coefficient bound 和
degree-`3M` 的 `h_(3M)` 通道；运行输出 `R22_AUDIT_COMPLETED`。这些是 proof-level
代数/尺度核验，不是 Gaussian rigidity 证明。

## 18. R23：Adjacent Heat-Hankel Transversality / Flat-Leakage Control

R23 在读取 R22 的本机提交 `90ca19e` 后，继续严格限定 genuine full-exact iid
inverse heat-Hankel trajectory；ordinary positive measures、有限矩前缀、非 iid
exchangeable 构造和 formal candidate 都不计为反例。

### 18.1 near-flat Laurent law：相邻比值不是 uniform upper bound

在 corank-one flat crossing 且 `ell_M != 0` 时，令横截参数为 `s`，并写
`h_M=c s+O(s^2)`、`c != 0`。由 R22 的
`D_(M+1)=-D_(M-1) ell_M^2+O(s)` 与 `D_n=D_(n-1)h_n` 得到

`h_(M+1)=-ell_M^2/(c s)+O(1)=-ell_M^2/h_M+O(1)`,

`beta_(M+1)=h_(M+1)/h_M=-ell_M^2/(c^2 s^2)+O(1/s)`。

因此在 `h_M<0` 的一侧，首个相邻 Jacobi norm 的主项为正，而相邻
`beta_(M+1)` 的绝对值会近 flat 发散。这个事实只能说明 adjacent mixed sectors
可能帮助 cubic negativity，不能转化成所需的 uniform
`beta_(M+1)/|beta_M|` 上界；near-flat Jacobi coordinates 本身是奇异坐标。

### 18.2 截断 Gaussian 可除半径与正确的 first-zero transversality

对 heat 参数 `a` 定义

`L_a=exp(-a partial_x^2/2)mu`,

`g_n(mu)=sup{a>=0: H_n(L_a) is PSD}`。

若 `a_1<a_2` 且 `L_(a_2)` 在第 `n` 阶可行，则
`L_(a_1)=E_Z L_(a_2)[p(x+sqrt(a_2-a_1)Z)^2]` 对所有
`deg p<=n` 非负。因此每一级可行集是区间 `[0,g_n]`；leading-principal-block
包含关系再给出无条件的
`g_(n+1)<=g_n`。结合 R15 的 Hamburger determinacy/full-cone passage，
`g_n downarrow mathfrak g`，其中 `mathfrak g` 是完整 Gaussian divisibility
radius；primitive law 等价于 `g_n downarrow0`。

在 `g_n<a<g_(n-1)` 的 quasi-definite 区间，monic orthogonal norm 满足

`h_n'(a)=-L_a[(P_n')^2] <= -n^2 h_(n-1)(a)`,

从而
`|beta_n(a)|=|h_n(a)|/h_(n-1)(a) >= n^2(a-g_n)`。
这给出 law-independent 的 first-zero small-value transversality。它不是
`D_n(a)` 全部复/实零点的 classical interlacing；ordinary positive iid law
仍可能有 higher-rank complex roots。

若 `ell_M=0`，coherent leakage 可以延迟到更高 rank。无限延迟会导向有限原子
flat branch，与连续 `chi_2^2` radial law 不相容；但这还不等于 cubic 可见尺度内的
uniform finite horizon。

### 18.3 quasi-definite crossing：正确的 cancellation quantity

在 `a_*=g_M<g_(M-1)` 且 `ell_M!=0` 时，令 `s=a-a_*>0`、
`c_M=L_(a_*)[(P_M')^2]>0`，则

`h_M(a)=-c_M s+O(s^2)`,

`h_(M+1)(a)=ell_M^2/(c_M s)+O(1)>0`,

`beta_(M+1)=-ell_M^2/(c_M^2s^2)+O(s^(-1))<0`。

因此 `|beta_(M+1)|/|beta_M|` 近 flat 发散，但这只是奇异坐标效应；
`h_M h_(M+1) -> -ell_M^2`，最近邻 tensor sector 反而是有利的负贡献。
R22 所需控制的不是绝对 ratio，而是 cancellation-relevant quantity
`(beta_(M+1))_+/|beta_M|`；generic leakage 分支中它在 crossing 后局部为零。

### 18.4 flat boundary 的三分支与 atomic-shadow overshoot

对 `H_(M+1)` 在 lower positive block 上做 Schur reduction，尾块为
`[[0,ell_M],[ell_M,q_M]]`：

- `ell_M!=0`：尾块 indefinite，但越过 boundary 后 `h_(M+1)>0`；
- `ell_M=0,q_M<0`：真正危险的 strict-drop branch，立即有
  `h_M,h_(M+1)<0`，且 cancellation ratio 可发散；
- `ell_M=0,q_M>=0`：进入 genuine plateau，`g_(M+1)=g_M`。

在 `ell_M=0` 时，`H_M` 的唯一 flat null relation 给出 M-atomic quadrature
shadow `nu_M`，并将 moment agreement 延伸到下一阶。若 `v_*=1-a_*`，则

`q_M=[v_*^(M+1)2^(M+1)(M+1)! - E_(nu_M^3) Q^(M+1)] /
      [3(2/3)^(M+1)]`。

因此坏分支完全等价于 atomic shadow 的 next-Q-moment overshoot。R23 尚未证明
该 overshoot 不会发生；这取代了不正确的 universal absolute beta-ratio 目标。

### 18.5 plateau 的无条件终止界与尺度缺口

若 flat plateau 从 `M` 持续到 `N`，PSD kernel propagation 给出
`x^jP_M in ker H_N`（`0<=j<=N-M-1`），所以 `L_(a_*)` 与 `nu_M` 的 moments
一致到 degree `2N-1`。而 `Q` 在 `nu_M^3` 下至多有

`K_M <= 1+C(M,2)+C(M,3)=1+(M^3-M)/6`

个 support values。其 `(K_M+1)`-阶 Q-Hankel 必奇异，而连续 scaled
`chi_2^2` 的对应块严格正定；故
`N<=2K_M<=2+(M^3-M)/3`。

这确实排除了 infinite plateau，但只有 `O(M^3)`，而 cubic amplifier 需要约
`O(M)`、至少推进到 `3M`，尚未闭合尺度。

### 18.6 ordinary zero-interlacing no-go 与 conditional closure

Bernoulli `X=+-1` 加任意正 Gaussian smoothing 的 ordinary positive iid stress
test 有
`D_3(t)=4t^2(t+2)(3t^3+12t^2+9t+2)`，cubic factor discriminant 为 `-216`。
所以 forward positivity/smooth iid law 本身不推出所有 heat-Hankel zeros
real-rooted 或 classical interlacing；这不是 full-exact `Q~chi_2^2` 反例。

R21 cubic 路线若要继续，只需集中证明两条 genuine full-exact iid bridge：
`ell_M=0 => q_M>=0`（排除 atomic-shadow overshoot），以及 plateau horizon
`g_N=g_M => N<=cM`（最好 `c<=3`）。generic leakage 已有有利 sign，坏
strict-drop branch 由第一条排除，plateau 再由第二条压到 cubic 可见范围；然后
才有意义把 tensor amplifier 迭代到 `M+2,...,3M`。

Exact triangularity 加 absolute moment growth 仍不能给 determinant-ratio control，
任何 degree `3M` test 也仍带 `h_(3M)` channel；`P_3K` 继续与上述桥断开。

要启动 R21 的 cubic amplifier，至少需要一个 genuine iid-compatible 的
cross-rank heat-Hankel 结论，例如排除 near-flat 后的 determinant-ratio 控制，或
在 `ell_M=0` 分支中的 uniform leakage horizon，并能把控制迭代到
`M+2,...,3M`。R23 没有证明这些条件，也没有构造 genuine full-exact iid
non-closed sequence。

`P_3K` 仍与 heat-Hankel leakage 断开：没有 charge-to-Jacobi、charge-to-determinant
或 charge-to-Loewner 的 quantitative bridge。主命题继续 OPEN。

本轮新增 `adjacent_heat_hankel_r23/audit_r23.py` 与 README，运行输出
`R23_AUDIT_COMPLETED`；只核验 near-flat Laurent 代数、截断 PSD 半径的主子块单调性、
相邻 determinant ratio 公式和 adjacent-sector threshold，不把这些局部核验写成
rigidity 证明。

当前最小 OPEN 改为：

### Flat-Shadow One-Step Overshoot Exclusion — OPEN

在 genuine full-exact inverse heat boundary
`H_(M-1)≻0, H_M⪰0, ker H_M=<P_M>, ell_M=0` 时，是否必有 `q_M>=0`？
等价地，匹配前 `M` 个 exact Q-moments 的 M-atomic iid quadrature shadow，
是否必满足
`E_(nu_M^3)Q^(M+1) <= v_*^(M+1)2^(M+1)(M+1)!`？
若成立，R23 的 one-step cancellation obstacle 消失；下一关是把目前
`O(M^3)` 的 plateau horizon 改进到 cubic 需要的 `O(M)`。

## 19. R24：Infinite-Tail Flat-Shadow Orientation

R24 在读取 R23 最终修订提交 `a006184` 后，继续严格限定 genuine full-exact iid
law；finite-prefix、ordinary iid stress test、exchangeable/non-iid 与 formal
extension 只用于证明策略的 no-go，不计为 Gaussian rigidity 反例。

### 19.1 无条件 reduction：`q_M` 是 null direction 的下一平方

在 flat boundary `a_*=g_M` 上，若
`H_(M-1)≻0, H_M⪰0, ker H_M=<P_M>` 且 `ell_M=0`，则 `P_M` 的正交关系从
`deg<=M` 延长到 `deg<=M+1`。因此可把下一 monic Schur direction 取为
`R_(M+1)=xP_M`，并得到

`q_M=L_(a_*)(x^2 P_M^2)`。

所以 R23 的 one-step overshoot exclusion 精确等价于

`L(P_M^2)=L(xP_M^2)=0  =>  L(x^2P_M^2)>=0`。

若令 `v_*=1-a_*`、`T=Q/(2v_*)`，则前 `M` 个 radial moments 为 `E T^j=j!`，并有

`q_M=3^M v_*^(M+1)[(M+1)!-E T^(M+1)]`

`=(-1)^M 3^M v_*^(M+1)(M+1)! E L_(M+1)(T)`。

因此剩余命题不是一般的 atomic quadrature extremality，而是首个未定 radial
Laguerre coefficient 的方向性：

`(-1)^M E_(nu_M^3)L_(M+1)(Q/(2v_*)) >= 0`。

### 19.2 严格 finite-prefix no-go：任意有限 exact horizon 都不足

R24 给出一个显式的 `M=3` 正 3-原子 Jacobi seed，其 one-body moments 为
`(1,0,1,1,3,4-2√3,22,3-36√3,274+44√3)`。三个 iid copies 满足

`E Q=2, E Q^2=8, E Q^3=48`,

但
`E Q^4=4336/9+64√3>384`。

其 `P_3` 在 support 上消失，故 `ell_3=0`；把 `m_8` 改为满足 `Q^4` exact 的
formal value `109-64√3` 后，仍有

`q_3=-(165+108√3)<0`。

这严格说明 positivity、iid、same-factor、flatness 与任意固定有限段 exactness
本身都不能推出 `q_M>=0`。进一步，利用 exact recurrence 的新 odd moment 自由度，
固定任意有限 `K` 后可把该坏 prefix 延长至 `Q^K`，再施加足够大的 forward
Gaussian smoothing，使有限 Hankel block 恢复严格正定。该构造仍然只是有限前缀
no-go；它不构造 genuine full-exact non-Gaussian law。

### 19.3 一个新的局部 plateau refinement

在 `ell_M=0` 分支，若 `q_M>0`，则 `H_(M+1)` 在 boundary 仍为 PSD，但若
`H_(M+2)` 也 PSD，kernel property 会强迫 `P_M` 与所有 degree `<=M+2` 多项式
正交，特别给出 `L(x^2P_M^2)=0`，与 `q_M>0` 矛盾。因此

`q_M>0 => g_M=g_(M+1)>g_(M+2)`。

长 plateau 只能发生在更退化的 `q_M=0` 分支。此时可把 plateau 改写成纯
atomic-Laguerre zero-multiplicity 问题：若 `nu` 为 M-atomic one-body shadow，
`A_n=E_(nu^3)L_n(Q/(2v))`，则 plateau 到 `N` 意味着
`A_1=...=A_(N-1)=0`。下一步应证明
`min{n>=1:A_n!=0}<3M`（最好给出 universal `c<=3`），以把 R23 的
`O(M^3)` support-count 界压到 cubic amplifier 所需的线性尺度。

### 19.4 R24 的逻辑等级与最小 OPEN

R24 已证明/保留：`q_M=L(x^2P_M^2)` 的 null-square reduction、Laguerre sign
identity、显式 `M=3` finite-prefix overshoot，以及 finite-horizon no-go 的构造
机制。尚未证明 `q_M>=0`，也没有 genuine full-exact iid non-closed sequence。

因此当前最小 OPEN 精确改名为：

### Infinite-Tail Flat-Shadow Orientation — OPEN

对 genuine full-exact iid law，在
`H_(M-1)≻0, H_M⪰0, ker H_M=<P_M>, ell_M=0` 时，simultaneous all-degree
exactness、genuine forward positivity 与 uniform exact-law growth 是否强迫
`L(x^2P_M^2)>=0`？等价地，是否强迫首个未定 Laguerre 系数满足上面的定向不等式？

若该命题成立，下一关是 `M`-atomic residual Laguerre zero-multiplicity `<3M`，
再之后才继续 R21 的 post-failure tensor-tail domination。`P_3K` 仍完全断开：
没有 charge-to-Jacobi/determinant/Loewner 的 quantitative bridge，不能把
`P_3K≠0` 接入 R24 closure。

本轮新增 `infinite_tail_flat_shadow_r24/audit_r24.py` 与 README，运行输出
`R24_AUDIT_COMPLETED`。本机只核验上述局部代数、显式 seed、Laguerre 恒等式和
Gaussian-smoothed finite-prefix 正定性，不把 finite-prefix no-go 写成 full-exact
反例，也不把 R24 写成 Gaussian rigidity 证明。

## 20. R25：Flat Null-Square Tail-to-Head Positivity

R25 先重新读取本文件与工作日志至提交 `02f4bca`，继续严格限定 genuine
full-exact iid law。R25 没有证明 `q_M>=0`，也没有构造 genuine full-exact
non-Gaussian 反例；它把剩余命题进一步压缩成共同根导数、same-factor 残差平方
以及一个需要 uniformity 假设的紧性模量。

### 20.1 共同根导数的无条件重写

在
`D_M(a_*)=D_(M+1)(a_*)=0`、`D_M'(a_*)<0`、`ell_M=0` 的分支，沿
quasi-definite 一侧有
`D_(M+1)(a)=D_M(a)h_(M+1)(a)`，且 `h_(M+1)(a)->q_M`。因此

`D_(M+1)'(a_*)=q_M D_M'(a_*)`，

从而

`q_M>=0  <=>  D_(M+1)'(a_*)<=0`。

这不是完整 determinant-zero interlacing，只是 first boundary 的 adjacent
common-root orientation，目标比 classical interlacing 窄得多。

### 20.2 same-factor 残差平方恒等式

R24 的 null relations 给出
`L(P_M^2)=L(xP_M^2)=0`。故任意常数 `c` 都满足
`L((x-c)^2P_M(x)^2)=q_M`。在三个 iid 坐标中取
`c=(X_2+X_3)/2`，并令 `bar X=(X_1+X_2+X_3)/3`，得到

`q_M=(3/4)L^3(Psi_M)`,

其中
`Psi_M=sum_i (X_i-bar X)^2 P_M(X_i)^2 >= 0` 点态成立。

这是第一次把 one-step sign 写成 same-factor residual-weighted null-square。
但 inverse `L^3` 本身尚未证明对该特殊平方保持正性；因此该恒等式不是
`q_M>=0` 的证明，只准确指出了所需的窄 cone bridge。

### 20.3 坏符号必导致 adjacent-radius gap

若 `q_M<0`，令 `a_1=g_(M+1)`、`Delta_M=g_M-g_(M+1)>0`。在
`a_1<a<a_*` 上两次 heat-Hankel 导数不等式积分得到

`-q_M >= (M^2(M+1)^2/2) h_(M-1)(a_*) Delta_M^2`。

所以坏 sign 具有真实的几何后果：在 lower-block margin 不退化的局部类内，
`q_M` 若趋于零，adjacent truncated Gaussian radius gap 也必须趋于零。这个
估计不能排除坏分支，但排除了“坏 sign 有固定余量而完全不改变半径结构”的想象。

### 20.4 `Omega_K` 紧性模量：准确的 conditional closure

固定 `M`、`a_*` 的紧参数窗口和 `H_(M-1)>=delta I`，在满足 genuine exact
class 统一 square-exponential bound 的 `K`-prefix 类上定义

`Omega_K=sup (-q_M)_+`。

由于 prefix 类嵌套，`Omega_(K+1)<=Omega_K`。在统一增长界、参数窗口和
lower-block margin 同时成立时，若 `lim Omega_K>0`，tightness、uniform
integrability、子列极限、所有 `Q`-矩 exactness 及 `chi^2_2` moment determinacy
会产生一个 genuine full-exact `q_M<0` boundary；反向若已有 full-exact 坏边界，
它属于所有 prefix 类。因此在这些明确的 uniformity 假设下，

`Omega_K -> 0  <=>` 该局部窗口内不存在 genuine full-exact 坏边界。

这只是把 R25 的无限尾内容精确写成 uniform finite-prefix overshoot-decay
modulus；它没有证明 `Omega_K->0`。R24 的“任意有限 horizon 都能 overshoot”与
该模量并不矛盾，因为其坏余量、半径 gap、lower-block margin 或统一增长控制
至少必须有一项退化。

### 20.5 R25 的逻辑等级与当前最小 OPEN

本轮无条件核验了共同根导数恒等式、residual null-square 恒等式和 radius-gap
下界；没有得到 full-exact orientation，也没有得到 `P_3K` 的 quantitative
bridge。R24 的 finite-prefix no-go 仍然有效，因此不存在只用固定有限个 exact
`Q` 方程、有限 Hankel positivity 和有限 same-factor algebra 就推出 `q_M>=0`
的证明模板。

当前最小 OPEN 更精确地改名为：

### Flat Null-Square Tail-to-Head Positivity — OPEN

在 genuine full-exact inverse flat boundary，是否有以下等价/紧密对应的任一证明：

1. `D_(M+1)'(a_*)<=0`；
2. `L(x^2P_M^2)>=0`；
3. `L^3(sum_i (X_i-bar X)^2P_M(X_i)^2)>=0`；
4. 在明确 uniformity 假设下建立 `Omega_K->0`。

下一轮 R26 应优先沿第三种 common/residual coherence 研究 R18 的 conditional
matrix positivity 或 Hubbard–Stratonovich 表示能否覆盖这个特殊平方；若不能，
则给出严格的最小缺失条件或 full-exact no-go。不要把 `M`-atomic residual
Laguerre `<3M` 提前升级，也不要重新展开已被排除的普通 zero-interlacing。
`P_3K` 继续断开，Gaussian rigidity 仍 OPEN。

本轮新增 `flat_null_square_r25/audit_r25.py` 与 README。使用带 SymPy 的本机
Python 3.12 运行，输出 `R25_AUDIT_COMPLETED`；并复跑 R24 审计通过。脚本只核验
局部代数和条件模量的单调性，不把 conditional compactness 或 R25 orientation
写成已完成定理。

## 21. R26：Residual-Corrected Flat Null-Square Hardy Gain

R26 先重新读取本文件、工作日志和 R25 审计资产至提交 `fb8c7e4`。本轮仍严格
限定 genuine full-exact iid law；没有把 ordinary iid、finite-prefix、形式逆热
候选或非 iid law 当作反例。R26 没有证明 `q_M>=0`，但给出了一个无条件的
reverse-heat 分解、一个严格的 common-only 错符号 obstruction，以及两个很窄的
conditional bridge。

### 21.1 reverse-heat square decomposition

令 `F_i=(X_i-bar X)P_M(X_i)`、`G_i=P_(-a)F_i`，并令 `L` 是 flat boundary
处的 inverse functional。多元 heat product identity 为

`P_a((P_(-a)F)^2)=sum_alpha a^|alpha|/alpha! (partial^alpha F)^2`。

结合 R25 的 `L^3(sum_i F_i^2)=4q_M/3`，得到精确分解

`A_M=4q_M/3+E_M`,

其中

`A_M=L^3(P_a(sum_i G_i^2))`

是 forward heat image 下的真实 square expectation，而

`E_M=sum_{i,|alpha|>=1} a^|alpha|/alpha! L^3((partial^alpha F_i)^2)`。

对 `F_i` 的每个非零导数，每个 one-body degree 都不超过 `M`；所以在
`H_M(L)>=0` 的条件下 `E_M>=0`。但这只给出“forward square energy 减去
lower-rank Gaussian-noise energy”的表示，不给出所需的 `A_M>=E_M`。
显式 pullback 也经过核验：若 `P_hat=P_(-a)P_M`，则

`P_(-a)[(X_i-bar X)P_M(X_i)] =
(X_i-bar X)P_hat(X_i)-(2a/3)P_hat'(X_i)`。

### 21.2 posterior pullback 与严格错符号

对 `A_t^mu(y)=E_mu exp(yX-tX^2/2)`，令 `D=1+at`、`s=y/D`、`u=t/D`，
complete-the-square 给出

`A_t^mu(y)=D^(-1/2) exp(ay^2/(2D))
 L(exp(sX-uX^2/2))`。

在 flat null `L(P_M^2)=L(XP_M^2)=0`、`L(X^2P_M^2)=q_M` 下，

`L(exp(sX-uX^2/2)P_M^2)=q_M(s^2-u)/2
 +O(|s|^3+|s|u+u^2)`。

自然的三副本 HS escort 满足 `E[Y^2]=t/3+O(t^2)`，故其 common-shift 平均的
首项为

`E_eta[W_a,t,Y[p_t,Y]]=-(q_M/3)t+o(t)`。

因此 ordinary raw conditional PSD、点态 `Psi_M>=0`、以及 common-only scalar
HS averaging 都不能证明 `q_M>=0`；后者在 leading order 读取的还是 `-q_M`。
任何成功的 HS/matrix 方案至少需要同阶 residual correction/common--residual
coherence，不能把 pure-residual rotational positivity 直接套到
`(X_i-bar X)P_M(X_i)` 上。

### 21.3 两个最窄的 conditional bridge

以下两条均为 conditional theorem schema，不是当前假设下已证命题：

1. 若 flat rank-`M` deconvolved Hankel positivity 在一列 infinitesimal Esscher
   slice 上保持，则 `q_M>=0`，因为该 slice 的二阶项是 `q_M y^2/2`。
2. 若能证明 reverse-heat latent-energy domination `A_M>=E_M`，则由上述分解
   得 `q_M>=0`。这只要求一个特殊 flat-null vector 的能量控制，远弱于整个
   inverse `L` 在所有 squares 上正性。

R26 还严格排除了三种模板：点态非负不等于 inverse `L^3` 正性；R18 raw
conditional kernel 的 PSD 位于 Gaussian stripping 之前；自然 common-only HS
平均的首阶方向相反。故本 special-cone bridge 仍服务原 Gaussian rigidity 路线，
但必须先找到 residual-corrected inequality；`P_3K` 仍没有任何 quantitative
bridge，继续与 R26 closure 断开。

### 21.4 R26 逻辑等级与下一步

本轮无条件审计的是 heat pullback、flat parabolic jet、wrong-sign leading
coefficient、reverse-heat square identity 和显式 `P_(-a)F_i` 公式。当前最小
OPEN 改名为：

### Residual-Corrected Flat Null-Square Hardy Gain — OPEN

在 genuine full-exact inverse flat boundary，证明或否定 `A_M>=E_M`，或找到
等价的 residual-corrected common/residual coherence；第一阶符号必须为所需的
`+c q_M t`（`c>0`），不能再次得到 common-only 的 `-q_M/3`。若这条桥关闭，
才返回 residual Laguerre `<3M` 与 R21 cubic amplifier；Gaussian rigidity 仍
OPEN。

本轮新增 `flat_null_square_r26/audit_r26.py` 与 README。使用带 SymPy 的本机
Python 3.12 运行，输出 `R26_AUDIT_COMPLETED`；并复跑 R24、R25 审计与
`git diff --check`。脚本只核验局部恒等式和 degree schema，不把 conditional
domination、full-exact orientation 或 Gaussian rigidity 写成已完成结论。

## 22. R27：Same-Factor Conditional Residual-Jet Contraction

R27 先重新读取本文件、工作日志和 R26 审计资产至提交 `7268c1f`。本轮仍严格
限定 genuine full-exact iid law；没有把 finite-prefix seed、ordinary iid、独立
residual source、formal inverse candidate 或 sectorwise PSD 当作 full-exact 反例。
R27 没有证明 `q_M>=0`，但把 R26 的 trace bridge 压成了一个单一 antisymmetric
residual mode，并严格排除了一整类看似自然的 covariance completion。

### 22.1 `3x3` residual Gram identity

在 flat inverse boundary 令
`F_i=(X_i-bar X)P_M(X_i)`。由 `L(P_M x^k)=0`、`0<=k<=M+1` 以及
`L(x^2P_M^2)=q_M`，得到无条件的矩阵恒等式

`B_ij=L^3(F_iF_j)=(4q_M/9) delta_ij`。

这比 R25 的 trace identity 更强：坏 sign 在三个 residual-coordinate test
方向上是同一个 scalar gap，而不是只存在于一个未指定的组合方向。

### 22.2 矩阵 reverse-heat 分解

令 `G_i=P_(-a)F_i`，并定义

`A_ij=E_(mu^3)[G_iG_j]`,

`E_ij=sum_(|alpha|>=1) a^|alpha|/alpha!
L^3[(partial^alpha F_i)(partial^alpha F_j)]`。

heat product identity 给出

`A=E+(4q_M/9)I_3`。

这里 `A>=0` 只来自 genuine forward probability positivity；`E>=0` 只在
`H_M(L)>=0` 下由每个 derivative 的 one-body degree 不超过 `M` 得到。两者
分别半正定仍不推出 `A>=E`；本轮所需的等价目标是

`q_M>=0  <=>  A-E>=0`。

取 `c=(1,-1,0)/sqrt(2)`，即可把它进一步压成单一 antisymmetric residual mode

`F_-=(F_1-F_2)/sqrt(2)`,  `A_--E_-=4q_M/9`。

并且

`F_1-F_2=(X_1-X_2)H_P`,

`H_P=(P(X_1)+P(X_2))/2
 +(X_1+X_2-2X_3)(P(X_1)-P(X_2))/(6(X_1-X_2))`。

所以这个 mode 确实含有 residual factor，但 quotient 仍依赖 common coordinate。

### 22.3 独立正实 residual-source completion 的严格 no-go

自然 common HS source 的 covariance trace 是 `t`。若再加入独立 centered
residual source，且剩余 quadratic damping 保持 PSD，则

`0<=C_perp<=tP_perp`,  `tr(C_perp)<=2t`。

flat jet 的 `q_M` 首阶系数因此为

`(q_M/2)(tr(C_perp)-2t)<=0`。

最大 completion `C_perp=tP_perp` 只能把错误首阶抵消为 `0`，不能产生所需的
`+c q_M t`。同样的首阶 no-go 也适用于与 common field 仅作外部正随机化、大小为
`O(sqrt(t))` 且满足同一 damping budget 的一般 centered real source；高阶
cumulants 只影响 `o(t)`。因此继续调 residual Gaussian covariance 已经没有
意义，成功路线必须使用真正的 `U-R` 条件相关、cross-factor Schur term，或
R18 matrix sectors 的非平凡 contraction。

### 22.4 最强 conditional bridge 与当前 OPEN

R27 把当前桥压成

`E_(mu^3)G_-^2 >=
sum_(|alpha|>=1) a^|alpha|/alpha! L^3[(partial^alpha F_-)^2]`。

更结构化地，若 genuine full-exact conditional/common--residual Hilbert space
能构造 contraction `C_M`，使

`E_-=||C_M G_-||_2^2`,  `||C_M||<=1`,

则 Bessel 不等式立即给出 `E_-<=A_-`，从而 `q_M>=0`。这不是把结论换名：它
精确指出 R18 尚缺的 operator structure 是“所有 inverse derivative sectors
共同来自同一个 forward residual vector 的 contractive conditional projection”。

因此当前最小 OPEN 改名为：

### Same-Factor Conditional Residual-Jet Contraction — OPEN

在 genuine full-exact iid law 内证明或否定上述 `A_--> = E_-`，并显式处理
antisymmetric mode 的 common-coordinate dependence。若新候选仍只是独立正实
residual source、radial/pure-residual positivity 或 sectorwise PSD，按 R27.3
直接淘汰。该 bridge 仍服务原 Gaussian rigidity 的非循环局部路线；但
`P_3K` 没有 charge-to-residual-jet contraction 或 angular Hardy constant，仍
与 closure 逻辑断开。若 contraction 也无法构造，则应回到 R25 的 `Omega_K`
infinite-tail compactness modulus，而不再堆 HS 展开。

本轮无条件审计了 flat Gram、矩阵 heat 分解、antisymmetric factorization 和
residual covariance budget；新增 `flat_null_square_r27/audit_r27.py` 与 README，
运行输出 `R27_AUDIT_COMPLETED`。这些局部恒等式和 no-go 不构成 full-exact
反例，也没有关闭 Gaussian rigidity。

## 23. R28：Flat-Shadow One-Body Tail-to-Head Collapse

R28 先重新读取本文件、工作日志和 R27 审计资产至提交 `cb3e70a`。本轮仍严格
限定 genuine full-exact iid law；atomic shadow 只作为由 flat boundary 导出的
正概率辅助对象，formal moment vector 和 toy law 只用于审计恒等式，均不作为
full-exact 反例。

### 23.1 正 shadow realization

在 `ell_M=0` 的 flat boundary，令 `nu_M` 为 `P_M` 零点上的正 `M`-atomic
shadow，并令 `rho_M=P_a nu_M`。对
`F_-=(F_1-F_2)/sqrt(2)`、`G_-=P_(-a)F_-`，heat intertwining 给出
`E[G_-(Y+sqrt(a)Z)|Y]=F_-(Y)=0`，因为 `P_M(Y_i)=0`。因此

`E_-=E_(rho_M^3) G_-^2`

确实是一个正 iid Gaussian-mixture law 下的条件方差，而不是把 inverse
functional 直接误当成正量。于是 R27 的目标等价于两个正 iid law 对同一
antisymmetric mode 的 `L^2` 范数比较：

`A_--E_- >= 0  <=>  ||G_-||_(L^2(mu^3))^2 >= ||G_-||_(L^2(rho_M^3))^2`。

### 23.2 pair fiber 与 exact Q 的真实信息量

令 `D=X_1-X_2`、`S=X_1+X_2`、`Y=X_3`，则

`Q=D^2/2+(S-2Y)^2/6`。

因此 exact `Q~chi^2_2` 只直接给出 pair-difference conditional Laplace
transform 的一个加权 scalar average；它不提供 `D|S` 的 pointwise variance/
Loewner order，也不提供 full-exact law 与 `rho_M` 之间的 conditional Schur
order。iid permutation symmetry虽给出 `E[R|U,T]=0`、
`E[RR^T|U,T]=T I_2`，但只控制 rank-one residual harmonic，不能实现完整
derivative-jet contraction。

### 23.3 Hoeffding decomposition：residual sector 精确抵消

令 `R=P_(-a)P_M`、`W=P_(-a)(xP_M)=xR-aR'`。same-factor heat algebra 给出

`G_i=(2/3)W_i-(1/3)(X_j+X_k)R_i`。

在 centered unit-variance product law、`E R=E W=0` 下，antisymmetric
Hoeffding sectors 正交，并有

`E G_-^2=(4/9)E W^2+(2/9)E R^2-(1/9)(E[XR])^2`。

由于 `mu` 与 `rho_M` 在 flat boundary 上匹配到至少 `2M+1` 阶，`R^2`、
`XR` 以及 `W^2` 的 derivative/noise remainder 全部匹配；唯一剩余的是
one-body first-order mode：

`A_--E_-=(4/9)(E_mu W^2-E_rho_M W^2)`，

而 one-body heat product identity 又给

`q_M=E_mu[P_(-a)(xP_M)]^2-E_rho_M[P_(-a)(xP_M)]^2`。

所以所有 residual two-body/conditional Schur sector 对符号逐项抵消。只从
该 sector 提取新 contraction gain 的路线不能关闭 `q_M`；这是一条
full-exact-compatible 的 proof-route no-go，而不是 counterexample。

### 23.4 当前最小 OPEN 与后续方向

R28 将最小 OPEN 从 residual-jet contraction 进一步收缩为：

### Uniform Flat-Shadow One-Body Tail-to-Head Gain — OPEN

要求在 genuine exact-law uniform growth 和 nondegenerate flat window 下，证明

`||P_(-a)(xP_M)||_(L^2(mu)) >= ||P_(-a)(xP_M)||_(L^2(rho_M))`，

或等价地证明 `Omega_K -> 0`。R28 的 conditional theorem 是：若上述
one-body norm monotonicity 成立，则 `q_M>=0`，随后可继续接回 plateau、残余
Laguerre `<3M` 和 R21 cubic amplifier。未来候选必须直接触及 `W` 或
infinite-tail feedback；common-only HS、独立正实 residual source、纯 residual
rotation、sectorwise PSD，以及只处理 residual degenerate sector 的 Schur
contraction 均按 R24–R28 的审计停止条件淘汰。`P_3K` 仍无 quantitative bridge，
Gaussian rigidity 仍 OPEN。

本轮新增 `flat_null_square_r28/audit_r28.py` 与 README，运行输出
`R28_AUDIT_COMPLETED`；审计覆盖正 shadow 条件方差实现、same-factor heat 分解、
Hoeffding 正交与范数公式、低阶矩匹配下的 residual cancellation，以及 pair-sum
恒等式。没有 optimizer、数值 sweep 或远程计算。

## 24. R29：Flat-Shadow One-Body Tail-to-Head 的算子包装与障碍

R29 先读取本文件、工作日志和 R28 审计资产至提交 `ea59523`。本轮仍只讨论
genuine full-exact iid law；原子 shadow、Gaussian prefix、形式矩和有限谱只作
恒等式审计，不构成 full-exact 反例。

### 24.1 下一 Jacobi 范数差

令 `rho_M=P_a nu_M`，`W=P_(-a)(xP_M)`。在 flat-boundary 的 null/正交前提下，
`W` 是两侧共享的 monic degree-`M+1` orthogonal direction，而 `mu` 与
`rho_M` 至少匹配到 `2M+1` 阶。因此

`q_M=||W||_(L^2(mu))^2-||W||_(L^2(rho_M))^2`

可重写为下一 Jacobi norm 的差

`q_M=h_(M+1)(mu)-h_(M+1)(rho_M)`

以及

`q_M=h_M (beta_(M+1)^mu-beta_(M+1)^rho_M)`。

这是对 R28 one-body 缺口的精确 forward-Jacobi 包装；它本身没有给出符号。
同一 heat algebra 仍是
`R=P_(-a)P_M`、`W=P_(-a)(xP_M)=xR-aR'`，且 `W` 保持 monic。

### 24.2 Gaussian pair kernel 的全阶标量信息

定义

`k_tau(x,y)=exp(-tau(x-y)^2/6)`，
`T_tau f(x)=integral k_tau(x,y)f(y)dmu(y)`。

因
`k_tau(x,y)=exp(-tau x^2/6) exp(-tau y^2/6) exp(tau xy/3)`，
其幂级数是正 feature expansion，故 `T_tau` 为正算子；并且
`Tr(T_tau)=1`。三角迹的指数使用

`sum_(i<j)(X_i-X_j)^2=3Q`

得到

`Tr(T_tau^3)=E exp(-tau Q/2)=1/(1+tau)`

（最后一个等号只在 genuine exact `Q~chi^2_2` 层面使用）。若特征值为
`lambda_j>=0`，则 `sum lambda_j=1`、`sum lambda_j^3=1/(1+tau)`，从而

`1/(1+tau) <= Tr(T_tau^2) <= 1/sqrt(1+tau)`,
`||T_tau||_op <= (1+tau)^(-1/3)`。

这些是 scalar/radial 的 Schatten 信息；它们没有把指定的 `W` 与 shadow
范数联系起来。紧算子在无限维空间没有 uniform reverse coercivity，因此不能
从 `T_tau` 的 smoothing/contraction 自动反推出 `q_M` 的方向。

### 24.3 有限 Q 矩与真正的 tail 目标

令 `Z_mu(z)=E exp(-zQ/2)`。若前 `K` 个 `Q` 矩匹配 exact 值
`E Q^n=2^n n!`，则 `Z_mu(z)-(1+z)^(-1)` 在零点至少有 `K+1` 阶；在统一
square-exponential growth 下，网页端给出的 Cauchy remainder 还产生一个局部
指数尾估计。这说明 scalar radial channel 有真实的 tail decay，但仍不控制
directional one-body Rayleigh defect。

R29 的最强 conditional 证书是：若能对固定 nondegenerate flat window 证明

`(-q_M)_+ <= C_(M,W) sum_(n>N_K) r0^n a_n(mu)^2`,
`0<r0<r1<1`,

并由统一 square-exponential growth 控制右侧，则得到 `Omega_K->0`，进而
`q_M>=0`，再接回 plateau、Laguerre 和 R21 cubic amplifier。等价的理想形式是
把 `q_M=P_K+R_K` 分解为 finite Hankel/Jacobi 非负 slack 与可由远端 Hermite
尾控制的 remainder。该 relative tail-to-head estimate 尚未证明。

### 24.4 当前最小 OPEN

### Uniform Flat-Shadow One-Body Tail-to-Head Gain — OPEN

真正缺失的含义是：negative flat-shadow head defect 必须强迫 uniformly visible
remote spectral/Hermite tail。普通 Christoffel/Markov/Stieltjes、scalar radial
exactness、Schatten contraction，以及纯 triangular Jacobi elimination 都只看
有限前缀或 unitary-invariant 量，不能提供这个方向性的 reverse estimate。
因此 R29 下一步应直接尝试 adjoint/telescoping certificate；若只能得到
operator-only、common-only 或已在 R28 精确抵消的 residual sector 结论，应记录
no-go 而停止。`P_3K` 仍没有 charge-to-one-body quantitative bridge，Gaussian
rigidity 仍 OPEN。

本轮新增 `flat_shadow_tail_gain_r29/audit_r29.py` 与 README，运行输出
`R29_TAIL_EJECTION_CERTIFICATE REMAINS OPEN` 和 `R29_AUDIT_COMPLETED`。审计
覆盖 forward-Jacobi norm/beta 包装、Gaussian triangle kernel、Schatten 代数及
径向矩消零阶数；没有 optimizer、数值 sweep 或远程计算。

## 25. R30：Flat-shadow Sign-Compatible Augmented Adjoint Locality

网页端在开始本轮前读取了本框架、工作日志、R29 审计资产和 Git 提交
`e08d8e6cef8b6c9b313b39241b791b99d0fdfe7c`。本轮仍只讨论 genuine full-exact
iid law；formal moment vector、Gaussian shadow、有限 multiplier 和 odd-control
方向只作为恒等式/障碍审计对象，不构成反例。

令 `N=2M+2`，`m_j=E_mu X^j`，`r_j=E_rho X^j`，且
`d_0=...=d_(N-1)=0`、`d_N=q_M`。定义

`G_n(v)=E_(v^tensor3) Q^n-2^n n!`,

并沿 `v_s=r+s(m-r)` 定义路径平均 Jacobian

`bar J_(n,j)=integral_0^1 partial_(v_j)G_n(v_s) ds`。

则有全阶精确恒等式

`G_n(m)-G_n(r)=sum_(j=0)^(2n) bar J_(n,j)d_j`。

在 genuine exact law 的 `G_n(m)=0` 下，这就是 R30 的路径平均伴随起点。其
结构性支点为

`bar J_(n,2n)=3(2/3)^n>0`, `bar J_(n,2n-1)=0`，

因此第一行 `n=M+1` 给出

`q_M=-G_(M+1)(r)/(3(2/3)^(M+1))`。

这仍然没有符号：任意有限 multipliers `lambda_n` 只产生精确的

`q_M=-sum_(n=M+1)^K lambda_n G_n(r)-sum_(j=N+1)^(2K)c_j d_j`,

其中 `c_j=sum_n lambda_n bar J_(n,j)` 且归一化 `c_N=1`。等式伴随本身没有
正性，并且每个新 Q 等式配一个新的最高偶矩支点，同时留下后续奇矩的
odd-control 方向；所以它只能给出“头部 = shadow defect + odd remainder”，不能
给出“正的 Jacobi/Hamburger slack + 远端谱尾”。

R30 的真正收窄是 augmented certificate：

`q_M=sum_j eta_j S_j(mu)+sum_n lambda_n G_n(mu)+R_K`,

其中 `eta_j>=0`、`S_j>=0` 是 Hamburger/Jacobi 正性余量，且 `R_K` 的 dual
vector 只落在 `l>N_K`、`N_K->infinity`，并满足一个 law-independent weighted
`ell^2` 界。若存在这样的证书，则由统一 square-exponential Hermite growth 得
`R_K->0`，从而 `q_M>=0`；但本轮没有构造出 `lambda,eta`，因此这只是条件定理。

当前最小 OPEN 改名为 **Sign-Compatible Augmented Adjoint Locality**：同时实现
等式伴随、非负 Jacobi multipliers、固定/中间 one-body mode cancellation、纯远端
残差和统一 weighted dual locality。`P_3K` 仍没有 charge-to-augmented-adjoint
桥；Gaussian rigidity 仍 OPEN。

本轮新增 `flat_shadow_augmented_adjoint_r30/audit_r30.py` 与 README。审计运行
`R30_AUGMENTED_ADJOINT_IDENTITY PASSED`、`R30_SIGN_COMPATIBLE_LOCALITY REMAINS
OPEN`、`R30_AUDIT_COMPLETED`；没有 optimizer、SDP、大规模扫参或远程计算。

## 26. R31：Jacobi-Slack Adjoint Completion

网页端在开始本轮前读取了本框架、工作日志、R30 审计资产和 Git 提交
`7198c91b18b1e76874a453af2e946047b5111363`。本轮仍严格限定 genuine full-exact
iid law；formal Jacobi prefix、odd-control 坐标和有理数 sign test 只用于结构审计，
不构成 full-exact 反例。

R31 没有构造完整的 `q_M=P_K+R_K`、`P_K>=0` 且 `R_K` 具有统一远端尾界的证书，
但把 Jacobi-slack completion 的失败位置精确拆成三层：同级 slack 对新 odd
direction 的 pivot 可为零；固定延迟一级的 slack 没有普遍固定正号；即使 differential
cancellation 成功，路径增强仍留下非远端的 shadow-slack debt。rank 数量本身已经
匹配，因此不能再把障碍归因于“约束数量不够”。

### 26.1 无条件 odd-block 结构

在 forward Jacobi budget

`beta_n=B_n-S_(n-1)^2`, `h_n=beta_n h_(n-1)`

中，新 odd moment 的最高项给出

`partial_(m_(2n-1)) S_(n-1)=1/h_(n-1)`,
`partial_(m_(2n-1)) beta_n=-2S_(n-1)/h_(n-1)`。

因此以 odd controls 为列、以 `beta_(M+2), beta_(M+3),...` 为行为下标的
Jacobi-slack block 是 lower triangular，但其 diagonal 可能退化。canonical control
`u_n=S_(n-1)/sqrt(B_n)` 下，`beta_n=B_n(1-u_n^2)`，且

`partial_(u_n) beta_n=-2B_nu_n`,
`partial_(u_k) beta_n=(1-u_n^2)partial_(u_k)B_n`。

`u_n=0` 和 `|u_n|->1` 分别给出 pivot 消失及 off-diagonal leverage 被压低的两种
退化面，故 positivity 本身不提供显然的 uniform conic right inverse。

### 26.2 all-degree odd pressure 与首个 sign obstruction

对 centered `m_1=0`，same-factor cubic equation 满足全阶公式

`partial_(m_(2n-1))G_(n+1)
=-n(n+1)(n+5)(2/3)^(n+1)m_3`。

它说明新 odd moment 第一次进入下一条 exact row 时，压力方向由 `m_3` 决定；若尝试
只用同级 `beta_n` 消除，则必要 multiplier 的符号要求为

`eta_n>=0 iff m_3 S_(n-1)<=0`。

在 `S_(n-1)=0` 且 `m_3!=0` 时同级 slack 没有一阶 pivot；在相反符号时 multiplier
必须为负。因此“一个 odd slot 配自己的 `beta_n`”不是普遍可行规则。

固定延迟一级也失败。取 Jacobi 坐标

`s=m_3=1/20`, `p=2-s^2=799/400`, `c=S_2=-1`,

则

`beta_2>0`, `beta_3=1607/799>0`, `B_4=51765601/12839930>0`,

但固定 `S_3` 时

`partial_c beta_4=-5809029/5164898<0`,
`partial_c G_4=-6392/3375<0`。

故只用下一 slack 解 `partial_cG_4+eta_4 partial_c beta_4=0` 强迫
`eta_4<0`。这是 natural positive prefix cone 上的 sign obstruction，不是
genuine full-exact counterexample。

### 26.3 path augmentation 的 shadow debt

若沿 `v_s=r+s(m-r)` 对 Jacobi slack 定义

`bar H_(j,k)=integral_0^1 partial_(v_k)beta_j(v_s) ds`,

则

`beta_j(mu)-beta_j(rho_M)=sum_k bar H_(j,k)d_k`。

把这条零恒等式加入 R30 的 equality adjoint 后，正项确实出现为
`sum_j eta_j beta_j(mu)`，但同时必然留下

`D_K^sh=-sum_n lambda_n G_n(rho_M)-sum_j eta_j beta_j(rho_M)`。

由于正 Gaussian-smoothed shadow 满足有限阶 `beta_j(rho_M)>0`，gradient-level
completion 不等于 value-level certificate；除非 `D_K^sh=o_K(1)` 或它本身能被
远端 Hermite tail 控制，否则仍不能得到 `q_M=P_K+R_tail`。

因此真正需要的不是更多 slack，而是 simultaneous positive cone inf-sup、path sign
coherence、moving-rank conditioning 和 shadow balance。rank 已匹配，但 sign、
conditioning、shadow debt 及 law-independent weighted dual norm 仍未解决。

### 26.4 conditional closure 与当前最小 OPEN

令 finite odd block 为 `H_K=[bar H^(odd)_(j,n)]`。若对 worst-case viable prefixes
能够证明

`-c^(K) in H_K^T R_+^(J_K)`,
`||eta^(K)||_(ell^2(w))<=C`（`C` 与 law、`K` 无关），

并且 `D_K^sh=o_K(1)` 或具有同样的 remote-tail 表示，则
`q_M=sum_j eta_j beta_j(mu)+R_K`、`R_K->0`，从而 `q_M>=0`。这是一条条件定理，
没有假设 norm monotonicity，也没有偷用 Gaussian rigidity。

R31 后当前最小 OPEN 改为 **Uniform Positive Jacobi Normal-Cone Locality**：
对 `Omega_K` 的 worst-case viable prefixes，能否让 active forward Jacobi ranks
逃向无穷，同时构造非负 normal-cone multipliers，使 weighted Hermite-dual norm
统一有界并消除 shadow debt。固定 active rank 会导致有限支持并与
`Q~chi^2_2` 矛盾，但这只说明 rank escape，不给 multiplier bound。

本轮新增 `flat_shadow_jacobi_slack_r31/audit_r31.py` 与 README。审计运行
`R31_JACOBI_SLACK_STRUCTURE PASSED`、`R31_POSITIVE_ADJOINT_INF_SUP REMAINS
OPEN`、`R31_AUDIT_COMPLETED`；没有 optimizer、SDP、大规模扫参或远程计算。
`P_3K` 仍与该 normal-cone locality 逻辑断开，Gaussian rigidity 仍 OPEN。

## 27. R32：Global Value-Level Remote Adjoint Locality

网页端在开始本轮前读取了本框架、工作日志、R31 审计资产和 Git 提交
`78ce2eacffcf2e216b1ba52b394f96cafa2f9415`。本轮仍严格限定 genuine full-exact
iid law；有限 viable prefix、terminal flattening 和 KKT 只用于证明结构与障碍，
不构成反例。

R32 把 `Omega_K` 的 finite worst-case 问题写成显式的 moment/Jacobi feasible set：
exact `G_1=...=G_K=0`、forward `H_K(m)>=0`、记录的 even-moment bounds，以及
固定 nondegenerate inverse-flat window。`q_M` 在该集合上连续，因此有限 `K` 的
坏极值确实存在。这一步不需要 KKT 或数值 optimizer。

### 27.1 active-rank escape

在 `K>=M+2` 且前一阶 Hankel block 正定时，`G_K` 不含新 odd moment
`m_(2K-1)`；固定其它量，把 Jacobi control `S_(K-1)` 推到
`|S_(K-1)|=sqrt(B_K)`，不改变 exact rows、固定 head `q_M`、inverse-flat 条件或
even growth bounds，得到 terminal flattening `beta_K=0`。所以每个有限坏极值都可
选成 terminally flat。

若 `Omega_K` 沿子列保持 `>=epsilon>0`，而某个固定 forward Hankel rank 一直奇异，
则 even-moment bound 给出 diagonal extraction；PSD、所有固定 `G_n=0` 和 Carleman
唯一性产生 genuine full-exact limit law。固定 Hankel 奇异又迫使一体 law 有限支持，
从而 iid triple 的 `Q` 有限支持，与连续 `chi^2_2` 矛盾。因此

`r_K:=min{j:H_j(m^(K)) singular} -> infinity`。

同一紧性论证还给出：每个固定 rank `J` 在足够深的 viable prefix 上有统一正的
`lambda_min H_J>=c_J`。所以固定 rank 的 conditioning 不是缺口，缺口发生在 moving
rank。

### 27.2 finite-dimensional normal cone 的边界

在有限维变量 `z=(m_3,...,m_(2K),a)` 上，Fritz--John 分离可写成

`alpha nabla f_K + DE_K^T lambda - D H_K^*[Z] + N_other=0`,

其中 `f_K=-q_M`、`Z>=0`，并有 PSD complementarity
`<Z,H_K>=0`。exact Q rows 的最高偶矩导数为正且三角独立，但完整 flat/equality
流形是否有 uniform constraint qualification 尚未证明；因此无条件只能使用
Fritz--John，不能把 `alpha=1` 或 uniform KKT normalization 当成已证事实。

active-rank escape 只控制 singularity 出现的 degree，不控制 active-face 的 conic
inf-sup `sigma_K`，故

`r_K->infinity` 不推出 `sigma_K>=c>0`。

更致命的是标准 local KKT value completion 的互补性：

`eta_j>=0`, `beta_j(mu_K)>=0`, `eta_j beta_j(mu_K)=0`,
以及矩阵形式 `<Z,H_K>=0`。

因此 normal cone 只能消梯度，不能产生 R30 所需的正 value budget
`P_K=sum eta_j beta_j(mu_K)`；该量在 KKT 点恒为零。人为 terminal flattening 的 active
约束甚至满足 `theta_K=0`，所以 active rank escape 不保证存在 nonzero escaping
multiplier；inactive slack 的 multiplier 则被互补性强制为零。

这严格排除了 **Local Jacobi KKT/Normal-Cone Value Completion**：不能从“坏极值
存在 + active ranks 逃远 + local KKT”自动推出 `q_M=P_K+R_K` 且 `R_K->0`。
增加更多同类型 Jacobi constraints 也不修复这一机制，因为 inactive constraints
没有 dual mass，active constraints 的 value slack 为零，新增非零 multiplier 只会
增加 shadow debt。

### 27.3 shadow debt 的条件压制与真正缺口

在固定 compact flat window 内，positive Gaussian shadow `rho_M=Y+sqrt(a)Z` 的
Jacobi coefficients 满足

`beta_j(rho_M)/(j+1)<=C_W`,

并且 normalized exact-Q defects `Gtilde_j(rho_M)` 有统一有界 normalization。若
remote multiplier 支持从 `r_K->infinity` 开始，且存在 `0<theta<1` 使

`sum_j theta^(-j)|etatilte_j^(K)|^2 <= C`,

则 weighted Cauchy--Schwarz 给出 shadow debt `O(theta^(r_K/2))->0`。所以 shadow
debt 不是独立终极障碍；它可以在真正的 remote weighted locality 已成立时被压掉。

但 active-rank escape 只把 Jacobi normal support 推远，不把 equality multipliers
`lambda_(M+1),lambda_(M+2),...` 推远。也没有 audited identity 把固定低阶 equality
costate 转移到高阶。因此真正缺的是

**low equality costate -> remote bounded costate**。

这不是 rank 数量问题，而是 global value-level separation、conic inf-sup、shadow
balance 和 law-independent Hermite-dual conditioning 的联合问题。

### 27.4 conditional closure 与当前最小 OPEN

若坏极值存在 normalized global adjoint，使 `alpha=1`，所有 fixed/intermediate
Hermite modes 消失，并有 `N_K->infinity`、

`sum_(ell>N_K) theta^(-ell)|Gamma_ell^(K)|^2<=C`,

且 Jacobi 与 exact-Q shadow debt 同样被该 remote weighted bound 压到零，则 R12
uniform Hermite tail 给出 `Omega_K->0`，进而 `q_M>=0`。随后旧链条仍接回
strict-drop 排除、短 plateau、Laguerre first-defect `<3M` 与 R21 cubic amplifier。
这是一条 conditional theorem，不是 local KKT 已证结论。

R32 后当前最小 OPEN 改为 **Global Value-Level Remote Adjoint Locality**：构造真正
的 global polynomial/SOS、same-factor adjoint telescoping 或其它 value-level
separation，把固定 head functional `q_M` 的 equality costate 逐级推到 remote
Hermite degrees，并保持 law-independent weighted norm。若没有新的 value identity，
R25--R32 的 local one-body normal-cone 支线应停止，不再堆更多局部 Jacobi 代数。

本轮新增 `flat_shadow_normal_cone_r32/audit_r32.py` 与 README。审计运行
`R32_ACTIVE_RANK_ESCAPE PASSED`、`R32_LOCAL_NORMAL_CONE_VALUE_COMPLETION NO_GO`、
`R32_REMOTE_EQUALITY_COSTATE LOCALITY REMAINS OPEN`、`R32_AUDIT_COMPLETED`；没有
optimizer、SDP、大规模扫参或远程计算。`P_3K` 继续与该 value-level locality
逻辑断开，Gaussian rigidity 仍 OPEN。

## 28. 已探索路线与停止条件

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

## 29. 每轮协作协议

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

## 30. 当前 checkpoint

- C2C task：`c2c_7b4e`。
- 已完成：R12、R13、R14、R15、R16、R17、R18、R19、R20、R21、R22、R23、R24、R25、R26、R27、R28、R29、R30、R31、R32。R14 证明 primitive-to-Gaussian 序列在任意
  固定 frequency/Gram complexity 内最终通过 confluent Bochner tests；R15
  又证明 genuine full-exact primitive 的逆候选若在任意一个非空小窗口内
  对所有 Gram size 都 PSD，就会由 order-2 矩增长升级为全局正定，故频率
  escape 被无条件排除。剩余唯一 Bochner 缺口是 `M_r→∞` 的
  inverse-Hankel rank escape；R16 又把它等价重写为 primitive stratum 的弱
  闭合/尾到头 viability 问题；R17 提取了 OU–Laguerre 全阶加权 viability
  不等式；R18 又证明完整 subcritical 全谱紧性和 `E_r` 内 supercritical moving-scale
  尾界；R19 又把 relative matrix closure 改写为 posterior Wick–Hankel 的固定 slice
  严格余量与 uniform witness alignment 问题；R20 又证明 posterior-`y` 对齐可由
  Esscher–affine congruence 精确解决，并把缺口压成 multiscale affine alignment
  与 diagonal-tensor capture；R21 又在 genuine iid residual 几何内排除了只使用
  first failure block 的 dimension-free reverse-Schur，并发现 degree `3M` 的
  triple-pivot amplifier；R22 又把 post-failure 控制压成 heat-Hankel 跨 rank 小值、
  flat leakage horizon 与 one-step Jacobi ratio；R23 又证明截断 Gaussian 可除半径
  `g_(n+1)<=g_n`、first-zero transversality
  `|beta_n|>=n^2(a-g_n)`，并把 generic leakage、degenerate overshoot 与 plateau
  三分支分开；plateau 只得到 `O(M^3)` 终止界，且 ordinary iid 的完整 zero
  interlacing 被 discriminant `-216` 严格排除；R24 又把 one-step 问题化为
  `q_M=L(x^2P_M^2)` 的 infinite-tail Laguerre orientation，并核验显式 finite-prefix
  overshoot no-go，运行 `R24_AUDIT_COMPLETED`；R25 又把它重写为 adjacent
  common-root derivative、same-factor residual-weighted null-square 与
  `Omega_K` conditional compactness modulus，运行 `R25_AUDIT_COMPLETED`；另保留
  `P_3K` sector 限定；R26 又得到 reverse-heat square decomposition、
  common-only HS wrong-sign obstruction 和两个 conditional bridges，运行
  `R26_AUDIT_COMPLETED`；R27 又将其压成 `3x3` residual Gram、单一
  antisymmetric residual mode，并排除独立正实 residual-source completion，运行
  `R27_AUDIT_COMPLETED`；R28 又把该 residual contraction 路线搬到正 shadow
  概率律并以 Hoeffding 分解证明 residual sector 精确抵消，剩余符号完全退回
  one-body `W=P_(-a)(xP_M)` 范数差，运行 `R28_AUDIT_COMPLETED`；R29 又把 one-body
  差包装为下一 Jacobi norm/beta gap，并以正 Gaussian pair kernel 的
  `Tr(T_tau^3)=1/(1+tau)`、Schatten sandwich 和有限 `Q` 矩的径向变换消零阶数
  明确 scalar/radial channel 的信息边界，运行 `R29_AUDIT_COMPLETED`。真正的
  tail-ejection certificate 仍未证明。
  `P_3K` 仍没有 quantitative bridge。
- 当前方向：R32 已完成，local Jacobi KKT/normal-cone value completion 已严格
  排除；active-rank escape 与 fixed-rank margin 已建立，但不能控制 equality costate
  的 moving-rank conditioning。唯一 OPEN 收窄为 `Global Value-Level Remote Adjoint
  Locality`：构造 global value certificate，把 fixed head 的 equality costate 推到
  remote Hermite tail，并保持 law-independent weighted bound，同时处理 shadow debt。
  若没有新的 value-level identity，应将 R25--R32 的 local one-body normal-cone
  route 记录为严格 no-go，不再做代数换名；只有关闭 one-step sign 后，才回到
  residual Laguerre `<3M` 与 R21 cubic amplifier。
- 结论状态：主命题仍 OPEN；没有 Gaussian rigidity 的无条件证明，也没有真实概率
  律反例。

## 31. R33：global value duality 与 positive-shadow quotient obstruction

网页端在开始 R33 前应先读取本框架、`PROJECT_WORKLOG_APPEND.md`、R32 审计
资产以及当前 Git 提交 `d1af16e3b98a0fbb2f86bd46b444826da1c47201`。本轮仍只
讨论 genuine full-exact iid law；global SOS、quotient 和 shadow 只作证明结构，
不构成反例。R33 的本机 proof-level 审计位于
`flat_shadow_global_value_r33/`，没有运行 SOS solver、optimizer、degree search
或远程计算。

### 31.1 有限 `K` 的 global value duality 不是首要障碍

在固定有限 `K` 的 compact Archimedean feasible set 上，若 `Omega_K` 是坏 head
defect 的 worst-case value，则对任意严格上界 `gamma>Omega_K`，标准
Positivstellensatz/Archimedean duality 给出

`gamma+q_M = P_K+E_K`,  `P_K in M_K`, `E_K in I_K`。

这只说明有限 `K` 有近似值证书，并不说明 `Omega_K->0`。等价地，对每个
`epsilon>0` 存在有限 `K(epsilon)` 使

`epsilon+q_M in M_(K(epsilon)) + I_(K(epsilon))`

当且仅当 `Omega_K->0`。因此“存在越来越好的 generic SOS certificate”本身
与待证明的 orientation 等价，不是新的 closure mechanism。

### 31.2 exact-`Q` ideal 的 triangular quotient

在 `m_0=1,m_1=0,m_2=1` 下，same-factor cubic rows 满足

`G_n = c_n m_(2n)-F_n(m_3,...,m_(2n-2))`,

其中 `c_n=3(2/3)^n>0`，且 `partial_(m_(2n-1))G_n=0`。所以有限截断的 exact
ideal 可递归消去所有 even moments，形式上给出

`R[m_3,m_4,...,m_(2K)]/<G_2,...,G_K> ~= R[m_3,m_5,...,m_(2K-1)]`。

对任意 `SOS=sum s_r^2`，逐项作递归 substitution 仍是
`sum (R_K s_r)^2`，故 quotient 不破坏 SOS 形式。R33 本机审计对 `G_2,G_3,G_4`
核验了 triangular pivot、odd-control 保留和 SOS substitution。

### 31.3 equality gauge 与 positive shadow 的冲突

global redundant-coordinate certificate 的 equality multipliers 没有 canonical
含义。例如

`P+s^2G^2+(h-s^2G)G=P+hG`。

因此不能逐项追踪 arbitrary `h_n` 的“shadow debt”。更基本地，正 flat shadow
`rho_M` 与 exact law 的 moments 匹配至 `2M+1`，但

`G_(M+1)(rho_M)=-c_(M+1)q_M`。

把 shadow 的 odd moments继续代入 exact quotient 所得到的 formal even continuation
满足

`rhat_(2M+2)-r_(2M+2)=q_M`。

只要 `q_M!=0`，这个 quotient point 就不在实际 positive shadow 的 exact-`Q`
variety 上。故 canonical exact quotient 消去了 equality costate，却丢失了正
shadow anchor；保留 redundant coordinates 则保留 shadow，却留下 gauge/costate
问题。这是 proof architecture obstruction，不是 counterexample。

若写成 `gamma+q=P+E_Q+E_flat`，在 genuine feasible law 上有
`gamma+q(mu)=P(mu)`；在 flat shadow 上有
`gamma=P(rho_M)+E_Q(rho_M)`，因为 `q(rho_M)=0` 且 flat ideal 在 shadow 上消失。
真正规范不变的是整个 shadow evaluation，而不是其 positive/equality 两个分块。

### 31.4 当前真正需要的 graded theorem

所需的不是任意 global certificate，而是一族 shadow-compatible、gauge-invariant
的 value certificates，其 canonical shadow normal form 满足：存在 `N_K->infinity`
使所有 Hermite degrees `ell<=N_K` 消失，且 remote coefficients 有 law-independent
weighted bound，例如

`sum_(ell>N_K) r_0^(-ell)|Gamma_(ell,K)|^2 <= C`，

并且

`gamma_K=sum_(ell>N_K) Gamma_(ell,K)a_ell(rho_M)`。

固定 Gaussian smoothing 的统一 Hermite tail 随即给 `gamma_K->0`，再由
`q_M=P_K(mu)-gamma_K` 得到 `Omega_K->0`。这是 conditional closure，尚未构造。

高 constraint rank 不等于高 Hermite degree：每个 `G_n` 仍依赖整个 moment prefix；
同样，简单 measure-LP relaxation 会丢掉 `Pi=mu^(tensor 3)` 的 same-factor/rank-one
结构。因此更多 local Jacobi minors 或无结构的 generic SOS 不能单独修复缺口。

### 31.5 R33 后的最小 OPEN 与逻辑边界

当前最小 OPEN 收窄为 **Shadow-Compatible Graded Global Positivstellensatz**，
也可称 **gauge-invariant Global Value-Level Remote Adjoint Locality**：能否构造
上述证书，使全部 fixed/intermediate shadow Hermite content 真正消失，并保持
对 `K`、law 和 moving rank 的统一 analytic/weighted norm。

Gaussian rigidity 仍 OPEN；`P_3K` 仍没有到该 graded certificate 的 audited bridge，
所以 `P_3K!=0` 与 R33 closure 继续逻辑断开。若下一轮没有新的 value-level identity，
R25--R32 的 local one-body normal-cone 支线不再堆叠更多同类约束；网页端必须先
阅读本框架与工作日志，再提出下一轮唯一可证伪的 global 子命题。

本轮新增 `flat_shadow_global_value_r33/audit_r33.py` 与 README。审计输出为
`R33_FINITE_GLOBAL_VALUE_DUALITY RECORDED`、`R33_Q_IDEAL_GAUGE_AND_SHADOW_OBSTRUCTION
PASSED`、`R33_GRADED_REMOTE_LOCALITY REMAINS OPEN`、`R33_AUDIT_COMPLETED`。

## 32. R34：OU-covariant total-shadow high-pass no-go

网页端在开始 R34 前已先通过连接读取本框架、工作日志、R33 README/审计脚本，
并核对真实 HEAD `c6fdf1844d4ed73a73e5b248985b0d97642220d0`。本轮将 R33 的
“总 shadow evaluation”目标进一步做成一个可证伪子命题：能否直接用 OU/heat
grading 把它变成 uniform remote-only object。结论是这整类直接线性机制严格失败，
但求和前的 nonlinear same-factor/Fock value transgression 尚未被排除。

### 32.1 OU 协变的无条件恒等式

令 `X_t=sqrt(t)X+sqrt(1-t)Z`，`a_t=1-t+ta`。MGF/heat 代数给出

`L_(a_t)^(P_t mu)=S_(sqrt(t))L_a^mu`。

若 `P_M` 为 monic flat-null polynomial，令
`P_(M,t)(x)=t^(M/2)P_M(x/sqrt(t))`，则 flat-null relations 保持，并且

`q_(M,t)=t^(M+1)q_M`。

对 `rho_M=P_a nu_M` 与 `nu_(M,t)=S_(sqrt(t))nu_M`，还有
`rho_(M,t)=P_t rho_M`，故 shadow 的 Hermite coefficient 按
`a_ell(rho_(M,t))=t^(ell/2)a_ell(rho_M)` 缩放。R34 本机脚本精确核验这些
MGF、polynomial 和 semigroup identities。

### 32.2 总 shadow evaluation 沿 OU 轨道是纯 grade 0

对任意有限值证书

`gamma+q_M=P_K+E_(Q,K)+E_(flat,K)`，

在 genuine exact law 上 ideal terms 消失；在 positive flat shadow 上 `q_M=0` 且
flat ideal 消失。因此规范不变的总响应

`Theta_K(t)=P_K(rho_(M,t))+E_(Q,K)(rho_(M,t))`

恒等于 `gamma`，与 equality gauge 和 `t` 都无关。若要求它在 OU-stable interval
上由 law-independent、OU-regular 的 strictly positive grade remote series 表示，
令 `u=sqrt(t)` 后右侧在 `u=0` 没有常数项，而左侧恒为 `gamma`；解析唯一性强迫
`gamma=0`。同样，任何所有 monomial 总 grade 都严格为正的 regular nonlinear
normal form也会在 `u=0` 消失，不能表示非零 finite-`K` 误差。

因此不能把整个 gauge-invariant total evaluation 本身 exact high-pass；成功方案
必须在“求和成 total evaluation”之前产生非平凡的 transgression/cancellation。

### 32.3 正 OU averaging 与 signed high-pass 的双重障碍

正性保持的 OU mixture
`A_nu=int_0^1 P_(u^2)dnu(u)` 的 grade multiplier 为
`m_ell=int_0^1 u^ell dnu(u)`。因为 `0<=u<=1`，有
`m_0>=m_1>=m_2>=...>=0`；若归一化 `m_N=1`，则 `u=1` 几乎处处成立，滤波
退化为恒等。因此所有 positive OU/heat averaging 都是 low-pass。

允许 signed filter 后，若其前 `N` 个 moments 被 annihilate 且第 `N` 个 moment
归一为 1，则对任意 `deg(p)<N` 有

`1 <= ||sigma||_TV ||u^N-p||_(infinity,[0,1])`。

monic Chebyshev minimax theorem 给最优误差 `2^(1-2N)`，从而
`||sigma||_TV>=2^(2N-1)`。所以 signed linear high-pass 的自然 norm 至少指数
爆炸，不能给出 R33 所需的 `K`-uniform weighted bound。R34 audit 核验了 Chebyshev
monic normalization 与该精确下界的代数 schema；minimax 结论作为标准证明定理
记录，不通过数值优化取得。

### 32.4 R34 后的最小 OPEN

R34 严格停止 **OU/heat-semigroup linear grading of the total shadow evaluation**，
包括 positive OU mixtures 和 signed finite-difference high-pass。新的最小 OPEN 为
**Nonlinear Shadow-Compatible Graded Value Transgression**：能否利用 same-factor
cubic/Fock homogeneous algebra，在求和成 gauge-invariant total evaluation 之前，
构造 positivity-compatible 的非线性 transgression，使唯一允许的 grade-zero defect
`delta_K->0`，其余项逃向高 OU grade 且 norm 统一有界。

相应 conditional closure 是：若存在
`gamma_K+q_M=mathcal P_K+mathcal T_K`，其中 `mathcal P_K(mu)>=0`，且
`mathcal T_K(rho_M)=delta_K+remote_K`，有 `delta_K->0`、远端 Hermite/OU norm
统一受控并由 Gaussian smoothing 统一尾估计压到 0，则 `gamma_K->0`、
`Omega_K->0`、`q_M>=0`，随后接回既有 plateau/Laguerre/cubic amplifier 链。
该 transgression 尚未构造。Gaussian rigidity 与 `P_3K` bridge 仍 OPEN 且断开。

本轮新增 `flat_shadow_ou_grading_r34/audit_r34.py` 与 README。修正两处审计实现
问题后，精确运行输出为 `R34_FLAT_OU_COVARIANCE PASSED`、
`R34_TOTAL_SHADOW_HIGH_PASS NO_GO`、`R34_SIGNED_OU_FILTER_NORM_BLOWUP RECORDED`、
`R34_NONLINEAR_GRADED_TRANSGRESSION REMAINS OPEN`、`R34_AUDIT_COMPLETED`。

## 33. R35：Fock first-grade linearity 与 SOS anchor tax

网页端在开始 R35 前已先读取本框架、工作日志、R34 README/审计脚本，并核对
真实 HEAD `88fd022c6e52d27a02139261b88c527cf1247284`。本轮只测试一个新的
value-level 子命题：same-factor cubic/Fock homogeneous polarization 能否在求和
成 total evaluation 之前提供正性兼容的非线性 grade transport。结论是自然的
有限、uniform、Fock-SOS 类被严格排除；constraint-coupled non-SOS 仍开放。

### 33.1 首个 shadow mismatch 与 cubic 的首级纯线性

令 `N=2M+2`，用 normalized Hermite/Fock 坐标 `b_j` 表示 full exact law `mu`
与 positive flat shadow `rho`。已有匹配关系给出

`b_j(mu)=b_j(rho)` (`j<N`)，`Delta_N=b_N(mu)-b_N(rho)=q_M/sqrt(N!)`。

same-factor homogeneous cubic

`F_n(b)=sum_(i+j+k=n) sqrt(n!/(i!j!k!)) A_(ijk)b_i b_j b_k`

的精确 polarization 是

`F(S+H)-F(S)=3B(H,S,S)+3B(H,H,S)+B(H,H,H)`。

若 `ord_OU(H)=N`，三项最低 grades 分别为 `N,2N,3N`；所以所有真正 nonlinear
cubic correction 在首 mismatch grade `N` 完全缺席。首个 defect 只能来自 linear
polarization。对 symmetric same-factor coefficient，首级为

`F_N(b(mu))-F_N(b(rho))=3A_(N00)Delta_N`，

而 `A_(N00)=(2/3)^d binom(2d,d)/4^d>0` (`N=2d`)，故首个 cubic shadow defect
与 `q_M` 同义，不能藏入同级 nonlinear cancellation。

### 33.2 exact ideal 的最低非零 grade 是规范不变量

考虑 regular（不含负 OU grade）ideal transgression
`J_K=sum_d H_(d,K)F_d`。shadow 上 `F_d(rho)=0` 对 `d<N` 成立，`d>N` 的
generator 只从更高 grade 开始，因此

`[u^N]J_K(rho_u)=H_(N,K)(g)F_N(rho)`。

这一个最低非零 shadow-grade coefficient 不受 equality multiplier 的 syzygy
gauge 影响，因为其它 generators 无法贡献 grade `N`。若要求 shadow remainder
从 `N` 之后才开始，而 `q_M!=0`，就必须有 `H_(N,K)(g)=0`，于是 exact-ideal
部分不能承担首个 head defect。

### 33.3 Fock-SOS anchor tax

若 positivity part 是有限平方和 `P_K=sum_r f_(r,K)^2`，记 Gaussian Fock anchor
处的

`c_r=f_(r,K)(g,xi_0)`, `d_r=partial_(b_N)f_(r,K)(g,xi_0)`。

full law 与 shadow 在首级相减，且 ideal 部分已被要求 remote 后，得到

`q_M=2Delta_N sum_r c_r d_r`。

在 `q_M!=0` 时因此
`sum_r c_r d_r=sqrt(N!)/2`，Cauchy--Schwarz 给出

`P_K(g,xi_0) D_(N,K)^2 >= N!/4`,

其中 `D_(N,K)^2=sum_r|d_r|^2`。任何固定 grade 的 analytic/weighted factor norm
都会控制 `D_(N,K)`；若 factors 的总 norm law-independent 且 `K`-uniform，
`P_K(g,xi_0)` 就必须保留一个 `K`-independent 的正预算，不能与允许的
`delta_K->0` 同时成立。等价的一维 sharp model 是

`x=(c+x)^2/(2c)-c/2-x^2/(2c)`，`c>0`：令 grade-zero `c/2` 消失会使 remote
coefficient `1/(2c)` 发散。

这也说明 cubic 的高阶项没有隐藏的 first-grade positivity gain：它们本来就从
`2N,3N` 才开始，真正的 sign-indefinite linear head 仍必须由正平方承担。

### 33.4 R35 的严格 no-go 与剩余 OPEN

本轮严格停止 **Uniformly Bounded Finite Fock--SOS Graded Transgression**：有限
cubic factors、有限 same-factor homogeneous products、正平方/二次模块、
`delta_K->0`、exact-ideal shadow remote 和 law-independent `K`-uniform analytic
factor norm 不能在 `q_M!=0` 分支同时成立。这是 proof-mechanism no-go，不是
full-exact probability counterexample。

仍未排除的唯一有意义方向是 **Constraint-Coupled Non-SOS Graded Value
Transgression**：signed homogeneous pieces 不能各自依赖 ambient SOS 正性，而
必须在 genuine same-factor exact manifold 与 probability cone 联合后才出现总的
非负性，同时保持 grade-zero defect 趋零和 remote norm 统一受控。Gaussian rigidity
与 `P_3K` bridge 仍 OPEN 且逻辑断开。

本轮新增 `flat_shadow_fock_transgression_r35/audit_r35.py` 与 README。修正一处
SymPy 符号元组可变性问题和零多项式的 grade 约定后，审计输出为
`R35_CUBIC_FIRST_GRADE_LINEARITY PASSED`、`R35_FIRST_IDEAL_GRADE_CANONICAL PASSED`、
`R35_FOCK_SOS_ANCHOR_TAX PASSED`、`R35_BOUNDED_FOCK_SOS_TRANSGRESSION NO_GO`、
`R35_CONSTRAINT_COUPLED_TRANSGRESSION REMAINS OPEN`、`R35_AUDIT_COMPLETED`。

## 34. R36：一体 Laguerre--Hoeffding 载体的固定头敏感性塌缩

网页端在开始 R36 前先读取了本框架、工作日志、R35 README/审计，并核对真实
HEAD `3e537e8`。本轮只推进一个新的可证伪子命题：能否用高 Laguerre 阶的一体
Hoeffding 投影承载首个固定 Hermite/Fock 头部 mismatch，同时保持 Gaussian
anchor 消失、固定头敏感性不塌缩和远端系数范数统一有界。

### 34.1 full-exact iid 下的 Laguerre--Hoeffding 恒等式

取 `Phi_n(X_1,X_2,X_3)=L_n(T)`，`T=(X_1^2+X_2^2+X_3^2)/2`。在 genuine
full-exact iid law 下，`T~Exp(1)`，所以 `E Phi_n=0`、`E Phi_n^2=1` (`n>=1`)。
令 `k_n^mu(x)=E_mu[Phi_n|X_1=x]`，并作三阶 Hoeffding 分解。正交性给出

`1=3||k_n^mu||^2+3||h_(2,n)^mu||^2+||h_(3,n)^mu||^2`。

一体投影的五副本 shared-coordinate 公式为

`||k_n^mu||^2=E_{mu^5}[Phi_n(X_1,X_2,X_3)Phi_n(X_1,X_4,X_5)]`。

这一步使用的是同一坐标共享后的 iid Fubini 分解，不是任意 exchangeable law
上的形式类比。

### 34.2 Gaussian anchor 的精确衰减

在 Gaussian residual plane 上，令 `T=(R_1^2+R_2^2)/2`，`h_m=H_m/sqrt(m!)`。
角向平均满足

`E_theta h_(2n)(R dot e_theta)=(-1)^n c_n L_n(T)`，
`c_n=sqrt((2n)!)/(2^n n!)`。

Gaussian 条件收缩再给出

`k_n^gamma(x)=kappa_n h_(2n)(x)`,
`kappa_n=(-1)^n c_n(2/3)^n`,
`||k_n^gamma||^2=binom(2n,n)/9^n`。

故一体 energy `A_n(gamma)=3 binom(2n,n)/9^n` 指数趋于零；一体高阶载体
天然丢失 `(2/3)^n` 量级的信息。

### 34.3 固定 head 的敏感性同样塌缩

取首个 mismatch `N=2M+2`，`Delta_N=q_M/sqrt(N!)`。沿形式 tangent
`dmu_epsilon=(1+epsilon h_N)d gamma` 做导数审计（这只是导数测试，不是概率候选），
五副本恒等式给出

`dot A_(n,N)=3(S_(n,N)+4L_(n,N))`，

其中 shared term `S_(n,N)=kappa_n^2 E[h_N h_(2n)^2]`，leaf term 满足
`|L_(n,N)|<=|kappa_n|`。当 `N` 为偶数且 `N<=4n` 时，精确 Hermite triple
coefficient 为

`E[h_N h_(2n)^2]=sqrt(N!)(2n)!/((2n-N/2)!(N/2)!^2)`。

因此对每个固定 `N`，
`|dot A_(n,N)| <= C_N(1+n^(N/2))(2/3)^n ->0`。

### 34.4 一体远端 carrier 的严格 no-go 与新的 OPEN

若 `J_K(mu)=sum_{n>=R_K} lambda_(n,K)A_n(mu)` 且
`sum|lambda_(n,K)|^2<=C^2`，Cauchy--Schwarz 与上面的敏感性塌缩共同推出：
Gaussian value 和固定 head sensitivity 都趋于零。要传递
`[u^N](J_K(mu_u)-J_K(rho_u))=q_M`，就必须让一体系数范数至少按
`R_K^{-N/2}(3/2)^{R_K}` 爆炸。具有统一 `l2` outer gradient 的有界非线性
重组也由 chain rule 同样排除。

所以 R36 严格停止 **Uniform Remote One-Body Laguerre--Hoeffding
Transgression**。这仍是 proof-mechanism no-go，不是 full-exact positive class
中的反例；它不排除二体 degenerate Hoeffding 投影或跨阶 pair/tensor carrier。
二体条件化能看到残余方向 `(X_1-X_2)/sqrt(2)`，可能绕过一体的 `(2/3)^n`
衰减。故当前最小 OPEN 收缩为 **Two-Body Laguerre--Hoeffding Head
Sensitivity**：计算 Gaussian 下 `E[L_n(T)|X_1,X_2]`、二体退化投影范数和
`partial_(b_N)||h_(2,n)||^2|_gamma`，再判断 constraint-coupled non-SOS
transgression 是否仍有可行窗口。Gaussian rigidity 与 `P_3K` bridge 仍 OPEN
且逻辑断开。

本轮新增 `flat_shadow_hoeffding_transgression_r36/audit_r36.py` 与 README。精确
运行输出为 `R36_HOEFFDING_VALUE_IDENTITY PASSED`、
`R36_GAUSSIAN_ONE_BODY_PROJECTION PASSED`、
`R36_FIXED_HEAD_SENSITIVITY_COLLAPSE PASSED`、
`R36_REMOTE_ONE_BODY_CARRIER NO_GO`、
`R36_TWO_BODY CARRIER REMAINS OPEN`、`R36_AUDIT_COMPLETED`。未使用 optimizer、
SDP、数值 sweep 或 remote computation。

## 35. R37：二体 Laguerre--Hoeffding 投影确实绕过一体指数损失

由于右侧网页标签的控制层暂时连续超时，本轮先完成 R36 已明确指向的二体
Gaussian anchor 子问题本机精确审计；没有把未经过网页复核的固定头导数当作
结论。新增审计前提仍是 genuine full-exact iid Gaussian anchor 的 common/
residual 坐标分解。

### 35.1 二体条件投影的精确生成函数

令 `S=(X_1+X_2)/sqrt(2)`、`D=(X_1-X_2)/sqrt(2)`。条件在 `(X_1,X_2)` 后，
残余 radial variable `T=(Y^2+Z^2)/2` 仍留下一个 variance `2/3` 的 Gaussian
方向。直接完成条件 Gaussian 积分得到

`sum_n E[L_n(T)|X_1,X_2]z^n`
`=(1-z)^(-1/2)(1-z/3)^(-1/2)`
`  * exp(-zD^2/(2(1-z))-zS^2/(6(1-z/3)))`。

等价地，写 `c_j=sqrt((2j)!)/(2^j j!)`、
`L_j^(-1/2)(x^2/2)=(-1)^j c_j h_(2j)(x)`，则

`p_n(X_1,X_2)=sum_(a+b=n)3^(-b)
 L_a^(-1/2)(D^2/2)L_b^(-1/2)(S^2/2)`。

本机 SymPy 审计对 `n=0,...,4` 将该式与直接对第三个 Gaussian 坐标积分的
`E[L_n(T)|X_1,X_2]` 逐项相等核验，并同时复核一体投影
`k_n^gamma=(-1)^n c_n(2/3)^n h_(2n)`。

### 35.2 退化二体范数与 anchor 的真实量级

令 `w_j=binom(2j,j)/4^j`。由于 `S,D` 独立标准 Gaussian，二体条件投影的
精确范数为

`||p_n||^2=sum_(b=0)^n9^(-b)w_(n-b)w_b`。

从 `p_n=k_n(X_1)+k_n(X_2)+h_(2,n)` 的 Hoeffding 正交分解，以及
`||k_n^gamma||^2=binom(2n,n)/9^n=(4/9)^nw_n`，得到

`B_n^gamma=||h_(2,n)||^2`
`=sum_(b=0)^n9^(-b)w_(n-b)w_b-2(4/9)^nw_n`。

其生成函数是
`sum_n||p_n||^2z^n=((1-z)(1-z/9))^(-1/2)`。`z=1` 的主奇点给出

`B_n^gamma~(3/(2sqrt(2)))w_n~3/(2sqrt(2pi n))`。

这与 R36 一体载体的指数衰减有本质区别：二体 anchor 仍趋零，但只按
`n^(-1/2)` 衰减，不能用 R36 的 `(2/3)^n` 塌缩机制排除。因而二体退化
Hoeffding sector 是真实的 carrier window，而不是把一体路线换个记号。

### 35.3 当前最小 OPEN 不变

本轮严格只关闭了 **Two-Body Gaussian Conditional Projection and Anchor
Scale**。尚未计算或宣称
`partial_(b_N)B_n^gamma` 的固定头敏感性，也尚未证明该 sector 能与 genuine
probability cone、same-factor exact ideal 和非 SOS 正性拼成 uniform
transgression。下一轮网页端必须先读取本框架、工作日志、R36 审计和本 R37
README/脚本，然后审查二体固定头导数：计算
`partial_(b_N)||h_(2,n)||^2|_gamma` 的精确五/六副本表达式及其 `n`-量级，
并判断它是否足以承载 `q_M`。Gaussian rigidity 与 `P_3K` bridge 仍 OPEN
且逻辑断开。

本轮新增 `flat_shadow_hoeffding_transgression_r37/audit_r37.py` 与 README，
精确运行输出为 `R37_TWO_BODY_CONDITIONAL_PROJECTION PASSED`、
`R37_TWO_BODY_DEGENERATE_NORM PASSED`、
`R37_TWO_BODY_ANCHOR_POLYNOMIAL_DECAY PASSED`、
`R37_TWO_BODY_HEAD_SENSITIVITY REQUIRES WEB_REVIEW`、
`R37_CONSTRAINT_COUPLED_TRANSGRESSION REMAINS OPEN`、
`R37_AUDIT_COMPLETED`。未使用 optimizer、SDP、数值 sweep 或 remote computation。

### 35.4 R37 网页复核：固定 head 敏感性通过筛选

同一项目网页端在开始工作前读取了本框架、工作日志、R36/R37 README 与审计脚本，
并核对真实 HEAD `370dd03bf289f7f73b2624c2d4936018b446649d`。网页复核给出
normalized `S,D` 展开

`p_n=(-1)^n sum_b 3^(-b)c_(n-b)c_b h_(2(n-b))(D)h_(2b)(S)`，

以及退化二体系数

`eta_(n,b)=(-1)^n[3^(-b)c_(n-b)c_b
 - 2c_n3^(-n)sqrt(binomial(2n,2b))]`。

对真实 law-functional `B_n(mu)=||h_(2,n)^mu||^2`，完整一阶导数先保留
底层 `mu^(tensor 2)` 权重、条件投影、一体 subtraction 与均值修正；Gaussian
退化性与 chaos-order 正交性随后给出精确简化

`partial_(b_N)B_n|_gamma = 2 E_gamma[h_N(X1)(h_(2,n)^gamma)^2]`。

对于 `N=2m`，网页端进一步给出有限 triple-Hermite 和

`D_(n,2m)=2 sum_(j=0)^m 2^(-m)sqrt(binomial(2m,2j))
 sum_(b,b'=0)^n eta_(n,b)eta_(n,b')
 tau(n-b,n-b';m-j)tau(b,b';j)`，

并得到固定 `m` 的渐近量级

`D_(n,2m) ~ 3sqrt((2m)!)/(sqrt(2pi)(m!)^2) n^(m-1/2)`。

这与本机预审计值一致：`D_(1,2)=2sqrt(2)/9`、
`D_(2,2)=28sqrt(2)/27`、`D_(2,4)=2sqrt(6)/3`。结合
`B_n^gamma~3/(2sqrt(2pi n))`，归一化 `lambda_(n,2m)=sqrt((2m)!)/D_(n,2m)`
后，固定 head 保持为常数而 Gaussian anchor 按 `n^(-m)` 趋零。因此二体
sector 通过了 R36 的 carrier-window screening；这仍不等于完整 graded
transgression，因为多级 fixed-grade cancellation、uniform condition number
和 remote tail 尚未证明。

R37 后全局最小 OPEN 收缩为 **Uniform Multi-Grade Cancellation for Two-Body
Hoeffding Carriers**，其上位路线仍是 **Constraint-Coupled Non-SOS Graded
Value Transgression — OPEN**。Gaussian rigidity 与 `P_3K` bridge 仍 OPEN 且
逻辑断开，本轮没有建立 charge-to-transgression bridge。

### 35.5 R38 本机 proof-level follow-up

新增 `flat_shadow_hoeffding_transgression_r38/audit_r38.py` 与 README。它只对
R37 网页复核产生的新有限恒等式做精确小阶核验：normalized pair expansion、
完整 Gateaux derivative 的各项分解、subtraction/mean/internal kernel 导数的
正交消失、finite Hermite sum 以及 `n=1,...,4` 的 exact regression。运行输出为

`R38_TWO_BODY_NORMALIZED_EXPANSION PASSED`、
`R38_TWO_BODY_FULL_DERIVATIVE PASSED`、
`R38_INTERNAL_HOEFFDING_DERIVATIVES_CANCEL PASSED`、
`R38_FIXED_HEAD_FINITE_SUM PASSED`、
`R38_TWO_BODY_CARRIER_WINDOW WEB_REVIEWED_LOCAL_FINITE_CHECK PASSED`、
`R38_MULTI_GRADE_CONDITIONING REMAINS OPEN`、`R38_AUDIT_COMPLETED`。

该审计确认二体 carrier window 的有限代数基础，但不从有限表推出渐近定理，
也没有使用 optimizer、SDP、数值 sweep、relaxed measure-LP 或 remote computation。

## 36. R39：二体 multi-grade 的第一道消项可行，但瓶颈移到 mixed Hessian

R39 网页复核在开始工作前读取了最新框架、工作日志、R36/R37/R38 审计记录，
并核对 HEAD `4184d3fd884ac6cbe5106e35cfcb05a77a6368ed`。固定首个 mismatch
`N=2m`，记 `D_(n,d)=DB_n(gamma)[h_d]`、
`lambda_(n,N)=sqrt(N!)/D_(n,N)`，则真实 full/shadow OU 路径的第一项为

`[u^N](B_n(mu_u)-B_n(rho_u))=D_(n,N)Delta_N`。

由于 `B_n` 在 reflection 下为偶函数且 centered variance-one 给出
`b_1=b_2=b_4=0`，下一非零 fixed grade 没有 nonlinear contamination：

`[u^(N+2)](B_n(mu_u)-B_n(rho_u))=D_(n,N+2)Delta_(N+2)`。

R38 的渐近量级给出

`D_(n,2r)~alpha_r n^(r-1/2)`，
`alpha_r=3sqrt((2r)!)/(sqrt(2pi)(r!)^2)`，

所以 `r_n=D_(n,N+2)/D_(n,N)=c_m n+O(1)`。取两个足够大的不同阶数，
`w_1=r_(n2)/(r_(n2)-r_(n1))`、
`w_2=-r_(n1)/(r_(n2)-r_(n1))` 精确满足
`w_1+w_2=1` 与 `w_1r_(n1)+w_2r_(n2)=0`。例如层级分离
`n_1=R,n_2=R^2` 时，`w_1=1+O(R^(-1))`、`w_2=-R^(-1)+O(R^(-2))`，
第一步没有类似 R34 signed-filter 的 multiplier blow-up。

在 genuine full-exact iid law 上，Hoeffding 正交分解给出

`1/3-B_n=A_n+C_n^(3)/3>=0`。

由于上述两级权重对应的实际 carrier coefficients 满足 `a_1>0>a_2`，可将
signed combination 写为

`a_1B_(n1)+a_2B_(n2)=P_R-delta_R`，

其中 `P_R=a_1B_(n1)+|a_2|(1/3-B_(n2))>=0` 只在 genuine full-exact
probability/Hoeffding 结构上成立，且 `delta_R=|a_2|/3 ->0`。Gaussian
anchor 上 `P_R->0`，而 grade `N` 保持为 `q_M`、grade `N+2` 精确消失，
奇数 grade 由 reflection parity 消失。这是一个真实的 finite-grade
constraint-coupled cancellation lemma，不是 tangent 反例，也不是 ambient SOS。

但 grade `N+4` 首次出现第二个 response channel。完整二阶 law-functional
导数必须同时包括 base-measure weight、conditional projection、one-body
subtraction、mean correction 和 mixed internal derivative：

`H_(n;a,b)=E[(g_1r_2+r_1g_2)h^2]`
`+2E[(g_1+g_2)h dot(h_r)]`
`+2E[(r_1+r_2)h dot(h_g)]`
`+2E[dot(h_g)dot(h_r)]+2E[h ddot(h_(g,r))]`。

当 `N>=6` 时，`b_4=0`，因此

`[u^(N+4)]F_n=D_(n,N+4)Delta_(N+4)
 +H_(n;N+1,3)b_3Delta_(N+1)`。

特殊 `N=4` 还多出 `-H_(n;4,4)Delta_4^2/2`。所以只根据
`D_(n,N),D_(n,N+2),D_(n,N+4)` 做 3×3 Vandermonde 不能控制整个
`N+4` grade；真正的最小 OPEN 进一步缩成 **Mixed-Hessian Two-Body
Response Lemma**，即研究 `H_(n;2m+1,3)` 与已有 linear response rows 的
渐近 span、符号和条件数。

新增 `flat_shadow_multigrade_r39/audit_r39.py` 与 README。本机精确运行输出为

`R39_TWO_GRADE_EXACT_CANCELLATION PASSED`、
`R39_CONSTRAINT_COUPLED_POSITIVITY PASSED`、
`R39_SECOND_DERIVATIVE_DECOMPOSITION PASSED`、
`R39_GRADE_NPLUS4_CHANNEL_DECOMPOSITION PASSED`、
`R39_LINEAR_VANDERMONDE_NOT_THE_OBSTRUCTION RECORDED`、
`R39_MIXED_HESSIAN_RESPONSE REMAINS OPEN`、`R39_AUDIT_COMPLETED`。

因此上位路线仍是 **Constraint-Coupled Non-SOS Graded Value Transgression —
OPEN**；Gaussian rigidity 仍 OPEN，`P_3K` bridge 仍完全断开。本轮没有使用
optimizer、SDP、大规模 sweep、relaxed measure-LP 或 remote computation。

## 37. R40：mixed-Hessian 的渐近共线性与 residue OPEN

为配合 R39 指出的最小 OPEN `K_(n,m)=D^2B_n(gamma)[h_(2m+1),h_3]`，网页端
给出了完整有限 Hermite 表示，并进一步把五项 Hessian 在 `a=2m+1>=7,b=3`
时精确缩成 `K=W+2C`：`⟨dot h_a,dot h_3⟩=0`、
`⟨h,ddot h_(a,3)⟩=0`，以及 `h_3`-外部交叉项均由 chaos order 消失。
网页端的渐近候选为，令 `chi_m=sqrt(binomial(2m+4,3))`、
`rho_m=sqrt(3(m+1))(2m+1)(4m+5)/(4(m+2))`，则

`K_(n,m)+chi_m D_(n,2m+4)-rho_m D_(n,2m+2)=O_m(n^(m-1/2))`。

等价地，`K/D_(n,2m)` 的最高 `n^2` 与 `n` 两层被已有 linear rows 吸收；
当前尚未决定的是

`S_(n,m)=(K_(n,m)+chi_m D_(n,2m+4)-rho_m D_(n,2m+2))/D_(n,2m)`

的极限 `sigma_m` 及首个非恒定 `1/n` 阶。该渐近结论目前作为网页端推导候选
记录，不能由有限表单独推出。

本机 `flat_shadow_mixed_hessian_r40/audit_r40.py` 对 affine density
`(1+epsilon h_a+delta h_b)d gamma` 直接提取 `epsilon delta` 系数，并与包含
base-measure、conditional projection、one-body subtraction、mean correction
及 mixed internal derivative 的完整五项公式逐项相等核验；同时核验了上述
三个 chaos cancellation 和 `S,D` 基底的 leading-component 系数。

在目标 `m=3`（`N=6`）下，精确回归为

`K_(1,3)=0`、`K_(2,3)=0`、
`K_(3,3)=-100sqrt(210)/81`、
`K_(4,3)=-25264sqrt(210)/2187`、
`K_(5,3)=-320648sqrt(210)/6561`，并额外核验
`K_(4,4)=-25808sqrt(105)/2187`。

网页端给出的 `g_(m,0)` leading coefficient、
`q_(m,2)=2^(-m)sqrt(3)(2m+1)sqrt(2m+2)` 也通过了本机精确投影核验。
审计输出为

`R40_MIXED_HESSIAN_COMPLETE_DECOMPOSITION PASSED`、
`R40_CHAOS_CROSS_TERMS_CANCEL PASSED`、
`R40_LEADING_COMPONENT_COEFFICIENTS PASSED`、
`R40_MIXED_HESSIAN_FINITE_REGRESSION PASSED`、
`R40_ASYMPTOTIC_RESPONSE WEB_CANDIDATE_RECORDED_UNAUDITED`、
`R40_AUDIT_COMPLETED`。

这只是有限 exact regression，不能单独推出 `n` 的主阶、与
`D_(n,2m+4)` 的相关性或 response-rank 结论；网页端的 `S_(n,m)` residue
仍需继续求出。当前上位 OPEN、Gaussian rigidity 与 `P_3K` bridge 的状态不变，
二体子路线的最小 OPEN 已从 mixed-Hessian row 缩为
**Renormalized Mixed-Hessian Residue / Weighted Conditioning — OPEN**。

本轮起，理论路线的整体框架、阶段大纲、每轮网页结论与本机 exact audit
均以本文件和 `PROJECT_WORKLOG_APPEND.md` 为本机记录，并随研究提交 Git。
每次向同一项目网页端继续推进前，必须先在提示中要求其阅读这两份最新记录及
相关 R-folder README/audit，再开始新的推导；网页端返回后再把可核验的新结论
补入本机记录。该记录协议只约束研究衔接，不改变当前 OPEN 命题、证据边界或
其余工作方式。

## 38. R41：residue 极限已显式化，m=3 的 N+4 条件数关口通过

网页端在开始本轮前读取了 R36–R40 的本机记录，并核对了 R40 时点的
`e9cd026`。本轮把 R40 的二体条件投影进一步压成固定 `S,D`-grade blocks：

`T_(r,j)(n)=E[h_(2j)(S)h_(2(r-j))(D)p_n^2]`

具有新的精确有限和

`T_(r,j)=sum_(s=-j)^j sum_b 3^(-2b-s)c_b c_(b+s)c_(n-b)c_(n-b-s)`
`times tau(2j,2b,2b+2s)tau(2r-2j,2n-2b,2n-2b-2s)`，

其中只保留 factorial 合法项，`tau` 是 normalized triple-Hermite 系数。
这给出了一个可直接审计的有限 block formula，而不是“类似可算”的声明。

网页端进一步给出 residue

`R_(n,m)=K_(n,m)+chi_m D_(n,2m+4)-rho_m D_(n,2m+2)`

的渐近候选：

`R_(n,m)=sigma_m alpha_m n^(m-1/2)+O_m(n^(m-3/2))`，其中

`sigma_m=-sqrt(6(2m+1))(160m^3+312m^2+140m+15)/(64(m+1)(m+2))<0`

对 `m>=3`。这意味着一般 `sigma_m` 不为零，但它本身不是 weighted
conditioning 的 no-go；真正需要看 residue 去掉常数后的首个变化阶。

最低情形 `m=3` 的网页渐近候选为

`S_(n,3)=-7563sqrt(42)/1280+(6327sqrt(42)/512)n^(-1)+O(n^(-2))`，

所以 `r_3=1<=m-1=2`。在该最低情形，N+4 mixed condition 的实际 carrier
系数仍趋零，网页端给出有限级 conditional continuation；但这仍不包括
`N+6,N+8,...`、任意深度 uniform conditioning 或 positive flat shadow 的
remote analytic tail。

本机新增 `flat_shadow_residue_r41/audit_r41.py` 与 README。它独立核验了
R41.1 的有限 block 和、`q_(m,2)`/`q_(m,4)` 的 exact `S,D` 投影、`sigma_m`
的精确特例与严格负号、`m=3` 商展开的 `1/n` 系数、三个 exact residue
回归点及 `1,n,n^2,n^(-1)` 的 4×4 行列式恒等式。输出为

`R41_BLOCK_FORMULA_FINITE_CHECK PASSED`、
`R41_Q_COEFFICIENTS_FINITE_CHECK PASSED`、
`R41_SIGMA_SPECIALIZATION_AND_SIGN PASSED`、
`R41_M3_FIRST_VARIATION_ALGEBRA PASSED`、
`R41_EXACT_RESIDUE_REGRESSION PASSED`、
`R41_4X4_DETERMINANT_IDENTITY PASSED`、
`R41_GENERAL_M_FIRST_VARIATION REMAINS OPEN`、
`R41_ASYMPTOTIC_CLAIMS REMAIN_WEB_DERIVED_UNAUDITED`、
`R41_AUDIT_COMPLETED`。

因此 R41 的严格结论是：一般 `sigma_m` 的网页闭式已有明确候选且有限代数
组件通过核验；`m=3` 的首个变化阶为 `1`，没有产生 N+4 family-specific
weighted no-go；一般 `m>=4` 的 `kappa_m` 非零性仍是当前最小 OPEN。上位
Constraint-Coupled Non-SOS Graded Value Transgression、Gaussian rigidity
仍 OPEN，`P_3K` bridge 仍完全断开。

## 39. R42：m=4 的首个 residue 变化阶通过，OPEN 收缩到一般 m>=5

网页端在开始本轮前读取了 R36–R41 的本机记录，并核对嵌套仓库 HEAD
`1b5d2ac`。本轮没有发现 R41 的渐近装配漏项：固定-chaos one-body
subtraction 以及 `dot p_3` 中的 one-body correction 只给出
`poly(n)(2/3)^n` 级的指数小项，不进入任何固定 `m` 的代数 `1/n` 展开。
`C` 项中 `j=1` 的首个修正与 `j=3` 的首项进入 `n^(m-3/2)`，而 `j>=5`
只从更低阶开始；对应地，`q_(m,2)` 需要二阶修正、`q_(m,4)` 需要一阶
修正、`q_(m,6)` 需要首项，且 `D_(n,2m+2)` 需要二阶修正。

网页端给出了两个新的 exact generating identity。若
`A(x;z)=(1-z)^(-1/2) exp(-zx^2/(2(1-z)))`，则

`P(z;S,D)=sum_n p_n(S,D)z^n=A(D;z)A(S;z/3)`，并且

`E[h_(2q)(G)A(G;z)A(G;w)]`
`=(-1)^q c_q (z+w-2zw)^q/(1-zw)^(q+1/2)`。

因此 `T_(r,j)` 具有精确二元生成函数

`sum_(k,l) E[h_(2j)(S)h_(2r-2j)(D)p_kp_l] z^k w^l`
`=(-1)^r 3^(-j)c_jc_(r-j)`
`*(z+w-(2/3)zw)^j(z+w-2zw)^(r-j)`
`/((1-zw/9)^(j+1/2)(1-zw)^(r-j+1/2))`。

插入 `h_3(X_3)` 的 odd conditional derivative 也有精确生成式：

`sum_n dot p_(3,n)z^n`
`=P(z;S,D)[2sqrt(3)z^2(2z-3)/(3-z)^3 h_1(S)`
`+2sqrt(2)z^3/(3-z)^3 h_3(S)]`。

在 `m=4`、`N=8` 下，网页端由这些生成式给出完整的 residue assembly：

`sigma_4=-15807sqrt(6)/640`，
`kappa_4=38325sqrt(6)/512>0`，因此 `r_4=1`。这与 R41 的 `sigma_m`
候选在 `m=4` 的特化一致。相应的 N+4 response row 为 `n^(-1)`，实际
carrier coefficient 的额外尺度为 `R^(1-4+1/2)=R^(-5/2)->0`，所以这一
层没有 family-specific weighted-conditioning no-go；这仍只是 finite-grade
conditional continuation，不是完整 transgression。

本机新增 `flat_shadow_residue_r42/audit_r42.py` 与 README。审计严格区分
exact 与网页渐近：二元 block generator、`dot p_3` generator、`m=4`
`q_2,q_4,q_6` 投影、residue quotient algebra、`S_(4,4)` exact regression
及 weighted exponent arithmetic 均通过；网页给出的 singular expansions
仍明确标为未审计。输出为

`R42_BLOCK_BIVARIATE_GENERATOR PASSED`、
`R42_DOTP3_GENERATOR PASSED`、
`R42_M4_Q_COEFFICIENTS PASSED`、
`R42_M4_RESIDUE_QUOTIENT_ALGEBRA PASSED`、
`R42_M4_EXACT_RESIDUE_REGRESSION PASSED`、
`R42_M4_WEIGHTED_CONDITIONING PASSED`、
`R42_M4_SINGULAR_EXPANSIONS REMAIN_WEB_DERIVED_UNAUDITED`、
`R42_GENERAL_M_KAPPA REMAINS OPEN`、`R42_AUDIT_COMPLETED`。

`S_(4,4)` 的新 exact 回归为 `-11639sqrt(6)/1179`。因此当前最小 OPEN
收窄为 **General-m>=5 First Residue Variation Lemma**，仍不能从 `m=3,4`
两例外推一般闭式或宣布所有 `kappa_m` 非零。上位 Constraint-Coupled
Non-SOS Graded Value Transgression、Gaussian rigidity 仍 OPEN，`P_3K`
bridge 仍完全断开。下一轮网页端开始工作前必须先读取本框架、工作日志及
R36–R42 的 README/audit；只有新的可精确核验有限恒等式才继续新增本机审计。

## 40. R43：m=5 的首个 residue 变化阶通过，OPEN 收缩到一般 m>=6

本轮本机沿用 R42 的精确二元 block generator 与 `dot p_3` generator，直接
推进下一未决情形 `m=5`。这里严格区分了三层证据：生成函数和有限回归是
exact；`u=1` 的系数提取是固定 `m` 的代数渐近装配；由 residue 推出
N+4 条件数行为仍只是 conditional continuation。

对 `m=5`，取消 pure-D component 后的相关系数为
`q_(5,2)=33/16`、`q_(5,4)=23sqrt(11)/8`、`q_(5,6)=47sqrt(33)/16`。

本机从 R42.3/R42.5 的 exact generator 得到目标阶的装配：

`W+chi_5D_(n,14)` 的 `n^(11/2), n^(9/2), n^(7/2)` 系数分别为
`55sqrt(231)/(224sqrt(pi))`、`-11343sqrt(231)/(7168sqrt(pi))`、
`2266031sqrt(231)/(2293760sqrt(pi))`；

`D_(n,12)` 的相应三阶系数为
`sqrt(462)/(240sqrt(pi))`、`-sqrt(462)/(2560sqrt(pi))`、
`-14917sqrt(462)/(163840sqrt(pi))`；

`C_(n,5)` 的 `n^(9/2), n^(7/2)` 系数为
`-57sqrt(231)/(3584sqrt(pi))`、`6871sqrt(231)/(114688sqrt(pi))`；

`D_(n,10)` 的前两阶为
`3sqrt(14)/(40sqrt(pi))`、`-9sqrt(14)/(1280sqrt(pi))`。

因此，使用 `rho_5=825sqrt(2)/28`，residue numerator 为
`-5703sqrt(231)/(3584sqrt(pi)) n^(9/2)`
`+3711849sqrt(231)/(573440sqrt(pi)) n^(7/2)+O(n^(5/2))`，
从而本机得到
`sigma_5=-9505sqrt(66)/896`、
`kappa_5=18887sqrt(66)/448>0`、`r_5=1`。

这与 `m=3,4` 的行为一致，但仍不能从三个值外推一般 `kappa_m` 闭式或
非零性。由于 `r_5=1<=m-1`，N+4 mixed row 的额外实际 carrier 尺度仍为
`R^(1-5+1/2)=R^(-7/2)->0`，所以这一层没有 two-body family-specific
weighted-conditioning no-go；仍缺 N+6 以上 channel、任意深度 uniform
conditioning，以及 positive flat-shadow remote tail。

本机新增 `flat_shadow_residue_r43/audit_r43.py` 与 README。它核验：R42.3
block generator 的有限 Hermite 对照、m=5 的 exact finite regression、
R42.5 raw `dot p_3` generator 的直接 Gaussian 对照、`q_2/q_4/q_6`、
`C^(1)+C^(3)` 的目标阶装配、D denominator、residue quotient 及
weighted exponent arithmetic。关键有限回归是
`K_(5,5)=-219200sqrt(462)/6561`、`D_(5,10)=91916sqrt(7)/2187`、
`D_(5,12)=46160sqrt(231)/6561`、`D_(5,14)=15400sqrt(858)/6561`、
`S_(5,5)=-687675sqrt(66)/160853`。

当前最小 OPEN 已收窄为 **General-m>=6 First Residue Variation Lemma** 的
一般非零性（以及更理想的一般显式 `kappa_m`）；`m=5` 已完成但不能外推。上位
Constraint-Coupled Non-SOS Graded Value Transgression、Gaussian rigidity
仍 OPEN，`P_3K` bridge 仍完全断开。下一轮网页端开始工作前必须先读取本框架、
工作日志及 R36–R43 的 README/audit；只有新的精确有限恒等式才继续新增
本机审计。

## 41. R44：一般 first-residue variation lemma 关闭，OPEN 前移至 N+6 多响应

本轮网页端先通过连接读取本框架、工作日志与 R36–R43 的本机记录，并核对
嵌套仓库真实 HEAD `5855acd94a5d4312d456af68bc3a26829a3cefa8`。网页端随后
将 R42.3/R42.5 的五类目标阶贡献一般化；本机 R44 audit 已对新增有限代数
与 `m=3,4,5` 的整套 fixed-`m` residue quotient 重装配完成核验。

### 41.1 无条件 exact / fixed-`m` 结论

对 `H_(alpha,beta)(u)=(1-u/9)^(-alpha)(1-u)^(-beta)`，固定 `m` 和固定
shift 时，主奇点 `u=1` 的 Darboux 展开由 `A_1,A_2` 给出，`u=9` 只贡献
`O(9^(-n) poly(n))` 的指数小项。本机核验了该系数规则及其 Gamma-ratio
实现。

R42.3 的 diagonal central-binomial moments `M_0,M_1,M_2` 在 `j=1,2,3`
的通式、本轮需要的 cancelled-chaos 系数通式均通过 exact polynomial
核验。其中

`q_(m,2)=2^(-m)sqrt(3)(2m+1)sqrt(2m+2)`，

`q_(m,4)=2^(1-m)sqrt(2m+1)(2m^2-m+1)`，

`q_(m,6)=2^(1-m)(6m^2-15m+19)
sqrt((2m-1)(2m)(2m+1)/120)`。

R42.5 的 `C` sectors 出现新的 exact pole-cancellation：`C^(1)` 和 `C^(3)`
中原本的 `(3-z)^(-3)` 因子分别精确约去，剩下统一的 `u=zw=1` 代数
奇点与 `u=9` 指数尾。相应的 `C^(1)` 两个 constant-term moments、
`C^(3)` leading constant-term identity 也通过本机核验。

将网页端的一般五项装配在固定 `m` 的 exact generator 上重装配，`m=3,4,5`
均严格复现既有本机结果；其中新的统一候选为

`kappa_m = sqrt(6(2m+1))
(608m^4+672m^3-386m^2-207m-27)/(256(m+1)(m+2))`。

因此 `P(m)=608m^4+672m^3-386m^2-207m-27`。对 `m>=1`，
`608m^4-386m^2>=222` 且 `672m^3-207m>=465`，所以
`P(m)>=660>0`；在 admissible `m>=3` 上 `kappa_m>0`，从而
`r_m=1`。这不是由 `m=3,4,5` 插值，而是由 exact finite moments、Darboux
规则和五项装配组成的固定-`m` 公式。

### 41.2 Conditional theorem 与证据边界

在假设 R39/R40 的 full-exact positivity conversion 和固定-`m` remainder
控制可沿用时，N+4 normalized response rows 仍为
`1,n,n^2,S_(n,m)-sigma_m`，其 leading span 是 `1,n,n^2,n^(-1)`。
由于 `lambda_(R,2m)=O(R^(-(m-1/2)))`，消去该 row 的额外 `O(R)` 放大后为
`O(R^(-m+3/2))->0`（`m>=3`），故整个 N+4 two-body mixed-Hessian level
不产生 family-specific weighted-conditioning no-go。

本机 R44 标记为：

`R44_GENERAL_DARBOUX_COEFFICIENT_ALGEBRA PASSED`、
`R44_GENERAL_BLOCK_MOMENTS PASSED`、
`R44_C_SECTOR_POLE_CANCELLATION PASSED`、
`R44_GENERAL_Q_FORMULAS PASSED`、
`R44_C_CONSTANT_TERM_IDENTITIES PASSED`、
`R44_GENERAL_KAPPA_SPECIALIZATIONS PASSED`、
`R44_GENERAL_KAPPA_POSITIVITY PASSED`、
`R44_FIXED_M_ASSEMBLY m=3,4,5 PASSED`、
`R44_NPLUS4_WEIGHTED_CONDITIONING PASSED`、
`R44_AUDIT_COMPLETED`。

这些标记不把固定-`m` 代数误写成 `m`-uniform remainder theorem，也不把
N+4 continuation写成完整 transgression。`N+6` 多响应、任意深度 uniform
conditioning、负系数补偿的 grade-zero debt 总控、positive flat-shadow
remote analytic tail、Gaussian rigidity 和 `P_3K` bridge 仍未解决。

### 41.3 当前最小 OPEN

`General-m>=6 First Residue Variation Lemma` 现已关闭；当前最小可证伪
子问题前移为：

**Grade-(N+6) Multi-Response Conditioning Lemma — OPEN**。

下一轮网页端开始前必须先读取本框架、工作日志及 R36–R44 的 README/audit。
只有产生新的可精确核验有限恒等式才新增本机 audit；不使用 optimizer、SDP、
大规模 sweep、relaxed measure-LP 或 remote computation。

## 42. R45：N=6 second-residue resonance 的有限核验，quotient rank 仍 OPEN

本轮网页端先读取本框架、追加工作日志及 R36–R44 的 README/audit，并核对
嵌套仓库 HEAD `73f063031a0362d9deb49b3e50305c3339252398`。网页端随后完成了
Grade-(N+6) Multi-Response Conditioning 的第一轮结构分析。本机只审计其中
可有限精确核验的最低危险情形 `N=6`、`m=3`，不把网页推导直接升级为一般定理。

### 42.1 新的 exact finite 结论

对 genuine full-exact law，degree-6 same-factor Fock 方程在 `b_1=b_2=b_4=0`
下只有 `(6,0,0)` 与 `(3,3,0)` 两类，精确给出

`b_6 = (7sqrt(5)/10) b_3^2`。

因此当 `N>6` 时，网页端的 `H_(n;N,6)b_6 Delta_N` 可以与
`(1/2)D^3B_n[h_N,h_3,h_3]b_3^2 Delta_N` 合并为一个 effective channel；
但在最低 `N=6` 时，`b_6` 已经是 mismatch grade，不能这样直接代入，额外
出现

`- (1/2) H_(n;6,6) Delta_6^2`。

所以网页端的 channel bookkeeping 修正为：`N>6` 有四个 law-monomial
channels，而 `N=6` 有五个，其中第五个是这个 quadratic resonance。

本机 R45 audit 用完整 law-functional 恒等式

`B_n(zeta)=E[K_4]-2E[K_5]+E[K_6]`

计算 `eps*delta^2` 系数；这等于
`(1/2)D^3B_n[h_6,h_3,h_3]`。在 `(n,m)=(3,3)` 得到

`K_4=376sqrt(5)/729`、`K_5=196sqrt(5)/729`、
`K_6=-28sqrt(5)/81`，

从而

`(1/2)D^3B_3[h_6,h_3,h_3]=-268sqrt(5)/729`。

完整 law-dependent Hoeffding kernel 的另外三个 finite regressions 为

`H_(3;9,3)=-32sqrt(105)/81`、
`H_(3;7,5)=-800sqrt(42)/729`、
`H_(3;6,6)=5560/729`。

因此

`J_(3,3)=(7sqrt(5)/10)H_(3;6,6)
          +(1/2)D^3B_3[h_6,h_3,h_3]
        =1208sqrt(5)/243`。

这里的 `K_4,K_5,K_6` 来自 exact multi-copy representation，包含底层 law
weight、conditional projection、one-body subtraction 和 mean correction；
它们不是只微分固定 kernel 的近似。

本机新增 `flat_shadow_residue_r45/audit_r45.py` 与 README，输出

`R45_DEGREE6_FOCK_RELATION PASSED`、
`R45_FULL_LAW_THIRD_VARIATION PASSED`、
`R45_M3_HESSIAN_REGRESSIONS PASSED`、
`R45_N6_RESONANCE_COMBINATION PASSED`、
`R45_NPLUS6_QUOTIENT_RANK REMAINS OPEN`、
`R45_AUDIT_COMPLETED`。

### 42.2 Conditional continuation 与当前最小 OPEN

网页端进一步指出：对固定 `m`，N+6 新 response 在旧
`{D_(N+6),D_(N+4),D_(N+2),1,S_(n,m)-sigma_m}` span 商空间中的渐近从
`n^(-2)` 开始。于是一般 `m>=4` 应计算三行
`H_(N+3,3), H_(N+1,5), J` 的 `n^(-2),n^(-3),n^(-4)` 系数矩阵；`m=3`
还要加入 `H_(6,6)` resonance row，并检查四阶 quotient matrix。

这只是 conditional rank diagnosis：本轮尚未计算 `C_m` 或 `C_3^res` 的
determinant，也没有 uniform-in-`m` remainder、uniform inverse bound、
positive-shadow remote tail 或完整 transgression。因此当前最小 OPEN 更新为

**N=6 Second-Residue Rank Lemma**：先精确计算 `C_3^res` 的 rank，至少判断
它是 `1` 还是已经 `>=2`。Gaussian rigidity、Constraint-Coupled Non-SOS
Graded Value Transgression 与 `P_3K` bridge 继续 OPEN。

下一轮网页端开始前必须先读取本框架、工作日志及 R36–R45 的 README/audit。
本轮没有使用 optimizer、SDP、大规模 sweep、relaxed measure-LP 或 remote
computation。

## 43. R46：N=6 second-residue quotient 已证明 rank 至少为 2，但完整矩阵仍 OPEN

网页端 R46 在右侧前端出现了工具调用未收尾的不同步状态；本轮不把未同步的
网页中间态当作定理。基于 R45 已确认的 exact generators，本机独立完成了
`flat_shadow_residue_r46/audit_r46.py` 的 proof-level algebra audit，目标只收窄
`N=6 Second-Residue Rank Lemma`，不回做 R29–R45。

### 43.1 本机 exact / Darboux 计算

对 `q=5` 的 conditional-score generator，先用 R45 的生成公式构造
`C^(5)`，再在 `(n,m)=(3,3)` 与直接 Gaussian marginalization 对照；这一有限
恒等式通过。`H_(n;7,5)` 的 `W` 部分则由 exact bivariate block generator 的
total-grade-12 `S,D` 分解得到。为取 second-residue，不能把 R43 只到二阶的
analytic Taylor truncation 继续外推；R46 audit 对
`(1-u/9)^(-alpha)` 在 `u=1` 的 Taylor 尾按所需阶数完整保留，并以 Laurent
级数逐行消去旧 span

`{D_(n,12)/D_(n,6), D_(n,10)/D_(n,6), D_(n,8)/D_(n,6), 1,
  S_(n,3)-sigma_3}`。

得到两条新 quotient rows 的前两列：

`H_(n;9,3)/D_(n,6)`：

`c_(3,2)=-3970123318809sqrt(21)/294859571200`，
`c_(3,3)=59155049844691sqrt(21)/8491955650560`；

`H_(n;7,5)/D_(n,6)`：

`c_(5,2)=1176526610081sqrt(210)/294859571200`，
`c_(5,3)=-2147390944445sqrt(210)/566130376704`。

这两个数构成的 `2 x 2` minor 为

`72543614649557486062397sqrt(10)/148407681470693376000 != 0`。

因此本机已经无条件地得到当前有限 Darboux 层面的 rank lower bound

`rank(C_3^res) >= 2`。

### 43.2 结论边界与下一刀

这不是 `rank(C_3^res)` 的完整计算：`J_(n,3)` 与额外 resonance row
`H_(n;6,6)` 的前两列尚未纳入同一审计，四行矩阵的完整 determinant 仍 OPEN。
所以当前只能说“旧 span 后至少出现两个独立 second-residue directions”，
不能把它升级为 weighted conditioning no-go；仍需具体 carrier-node scheme、
weighted norm、positive complement debt 以及 uniform tail 控制。

在现有 sequential/inverse bookkeeping 下，`rank >= 2` 使 `N=6` 的
conditioning danger 成为真实的 conditional possibility；它尚未证明
`R^(5/2)` blow-up 必然发生。形式 Hermite 方向仍只是 genuine OU Taylor
coefficient extractor，positive flat shadow 仍不能偷用 full-exact positivity。

本机新增 `flat_shadow_residue_r46/README.md` 与 `audit_r46.py`，输出：

`R46_H75_GENERATOR_FINITE_CHECK PASSED`、
`R46_H93_QUOTIENT_SECOND_RESIDUE`、
`R46_H75_QUOTIENT_SECOND_RESIDUE`、
`R46_C3RES_FIRST_TWO_ROWS_RANK_GE2`、
`R46_C3RES_FULL_MATRIX REMAINS OPEN`、
`R46_AUDIT_COMPLETED`。

下一轮网页端开始前必须先读取本框架、工作日志及 R36–R46 的 README/audit。
全局 `Constraint-Coupled Non-SOS Graded Value Transgression`、Gaussian
rigidity 与 `P_3K` bridge 继续 OPEN。

## 44. R46 correction：网页终稿已读，秩结论确认，n^-3 系数暂不强行合并

随后读取了右侧网页端已经完成的 R46 终稿。网页端直接给出
`rank C_{3,{n^-2,n^-3}}^{res}=2`，并因此确认完整 `C_3^{res}` 的 rank
至少为 2；这与本机的非零 `2 x 2` minor 结论一致。网页终稿同时把下一刀
收窄为 `N=6 Second-Residue Constraint-Coupling / Weighted-Inverse Lemma`：
需要判断 genuine full-exact same-factor manifold 中 `b_3 Delta_9` 与
`b_5 Delta_7` 是否能够独立激活，不能把 response rank >= 2 直接升级为
weighted no-go。

本机重新实现了完整的半整数 Gamma-ratio 形式展开，补足中心二项式的
`n^-3` 及更高阶项，并通过中心项
`1-1/(8n)+1/(128n^2)+5/(1024n^3)-21/(32768n^4)` 校验；随后重新运行
`flat_shadow_residue_r46/audit_r46.py`。当前本机可复核输出为：

`c_(3,2)=-3967045866009sqrt(21)/294859571200`，
`c_(3,3)=350225725881sqrt(21)/49660559360`；

`c_(5,2)=1178920184481sqrt(210)/294859571200`，
`c_(5,3)=-184569690489sqrt(210)/49660559360`；其 minor 为
`4530725172882348802803sqrt(10)/9893845431379558400 != 0`。

其中本机的 `c_(3,2)`、`c_(5,2)` 与网页显示一致，网页显示的两个
`n^-3` 系数则不同。故当前严谨状态是：`rank >= 2` 已确认，网页与本机
的二阶 residue 列尚需逐项对账；不把两套 `n^-3` 数字混成一个“已核验”
矩阵。完整四行 `C_3^{res}`、weighted inverse、positive complement debt、
uniform tail 与 global transgression 仍 OPEN。

下一轮网页端开始前必须先读取本框架、工作日志及 R36–R46 的 README/audit，
并区分 genuine full-exact、formal Gateaux coefficient extractor 与 positive
flat shadow 三种层次。本轮仍未使用 optimizer、SDP、大规模 sweep、relaxed
measure-LP 或 remote computation。

## 45. R47：有限 Fock/Hermite 约束不降掉 N=6 的两个方向，但 all-degree 积分仍 OPEN

网页端已完成本轮 constraint-coupling 推导。它把 `N=6` 的 rank-2 flat
shadow 写成二原子结构：令 `U=Y/sqrt(v)`，则 `EU=0`、`EU^2=1`，并且
支撑为两点等价于 `U^2=tU+1`。`b_4^rho=0` 给出 `t^2=2`，因此矩满足
`m_(k+2)=t m_(k+1)+m_k`，并有
`EH_5(U)=-6t`、`EH_6(U)=-4`、`EH_7(U)=36t`、
`EH_9(U)=-232t`、`EH_10(U)=-432`、`EH_12(U)=2848`。

配合 Hermite-heat covariance，网页端得到 `b_3,b_5 != 0`，以及
`b_5=-(3v/sqrt(5))b_3`、`Delta_6=(9sqrt(5)/10)b_3^2`。这些是
rank-2 flat shadow 的 exact head identities，不是 formal tangent 结论。

### 45.1 degree-10/12 same-factor identities

本机新增 `flat_shadow_constraint_coupling_r47/audit_r47.py`，独立用三方向
angular constant-term 计算 same-factor cubic 系数，并核验网页给出的
degree-6、degree-10、degree-12 方程。genuine full-exact 层的两个新式子为

`b_10 = sqrt(30)b_3 b_7 + (17sqrt(7)/14)b_5^2`，

以及在 `b_6=(7sqrt(5)/10)b_3^2` 后

`b_12 = (10sqrt(55)/11)b_3 b_9
       + (21sqrt(22)/11)b_5 b_7
       - (369sqrt(231)/440)b_3^4`。

把它们与二原子 shadow 的 `b_7,b_9,b_10,b_12` 相减，得到 exact
mismatch-coordinate 变换：

`b_5 Delta_7 = b_5/(sqrt(30)b_3) Delta_10
               + (13sqrt(42)/35) Delta_6^2`，

`b_3 Delta_9 = (sqrt(55)/50) Delta_12
               - (7sqrt(3)/50)(b_5/b_3) Delta_10
               - (1073sqrt(105)/31500) Delta_6^2`。

其线性部分对 `(Delta_10,Delta_12)` 的 Jacobian（自由坐标取
`(b_7^mu,b_9^mu)`）为 `(10sqrt(1650)/11)b_3^2 != 0`。

所以有限 degree-10/12 Fock 方程并没有把 `b_3 Delta_9` 与
`b_5 Delta_7` 压成一维；它们只是被可逆地改写成两个 even-mismatch
坐标，另加固定的 `Delta_6^2` 项。

### 45.2 证据边界与新的最小 OPEN

本机 R47 审计通过：

`R47_SHADOW_TWO_ATOM_RECURRENCE PASSED`、
`R47_DEGREE10_FOCK_IDENTITY PASSED`、
`R47_DEGREE12_FOCK_IDENTITY PASSED`、
`R47_MISMATCH_COORDINATE_IDENTITIES PASSED`、
`R47_LOCAL_JACOBIAN_RANK2 PASSED`。

这关闭了“有限 Fock/Hermite/Hankel 关系会自动把 rank-2 response 降秩”
这一局部猜想，但没有构造 genuine all-degree positive full-exact law。
网页端明确保留的真正 OPEN 是：两个有限前缀方向能否同时积分为满足
all-degree same-factor exactness、正性、OU backward divisibility 与
uniform weighted-tail 要求的真实 laws。有限 positive prefix 不是
all-degree realization，不能用它直接宣布 global obstruction 或 no-go。

因此当前路线应从“有限约束是否降秩”转向“全阶正性/相干性是否阻止二维
odd-control cone 的积分”。formal Gateaux 仍只是 OU Taylor coefficient
extractor，positive flat shadow 仍不能使用 full-exact Fock positivity；
Gaussian rigidity、`P_3K` bridge 与完整 Constraint-Coupled Non-SOS
Graded Value Transgression 继续 OPEN。

下一轮网页端开始前必须先读取本框架、工作日志及 R36–R47 README/audit；
只有出现新的 all-degree exact identity、正性递推或可证伪的全阶 cone
obstruction，才进入下一次本机 proof-level audit。本轮没有使用 optimizer、
SDP、大规模 sweep、relaxed measure-LP 或 remote computation。

## 46. R48：heat-lift null hierarchy 给出固定阶不定性与 moving-rank OPEN

网页端 R48 已在读取本机 R47 记录后选择 all-degree obstruction 路线。它没有
宣称 Gaussian rigidity 或 two-body no-go，而是把 rank-2 shadow 的二原子关系
只作为一个 test polynomial，构造了可逐项审计的 inverse-heat Gram hierarchy。

### 46.1 本机 proof-level audit

本机新增 `flat_shadow_heatlift_rankescape_r48/audit_r48.py` 与 README，并用
精确 SymPy 代数核验网页本轮的新有限/结构性内容。为避免一个隐蔽的归一化
错误，`x^p` 使用方差 `v` 的 generalized Hermite 展开；这正是网页公式中
`28v`、`36v` 等项的来源，而不是标准方差一的展开。

在 `v=1-a`、`c^2=2v`、
`P(x)=x^2-cx-v`、`r_k=L_a^mu(x^kP(x)^2)` 下，本机核验：

`r_2=sqrt(6!) Delta_6`，

`r_3=sqrt(7!) Delta_7-2c sqrt(6!) Delta_6`，

`r_4=sqrt(8!) Delta_8-2c sqrt(7!) Delta_7
     +28v sqrt(6!) Delta_6`，

`r_5=sqrt(9!) Delta_9-2c sqrt(8!) Delta_8
     +36v sqrt(7!) Delta_7-54cv sqrt(6!) Delta_6`。

本机还独立核验 genuine full-exact 的 degree-8 same-factor identity

`b_8=(8sqrt(14)/7)b_3b_5`，

并结合 rank-2 shadow 得到

`Delta_8=-(9sqrt(70)/35)v^4`、`r_2=18v^3`、
`r_4=-72v^4-2cr_3`。

因此最小 shifted inverse-null block 的 determinant 精确为

`det [[r_2,r_3],[r_3,r_4]]
 =-(r_3+18cv^3)^2-648v^7<0`。

这关闭的只是“把 `L_a(P^2R^2)` 当作正 Christoffel/Hankel 形式”的直接
证明路线；它不是 Gaussian-rigidity no-go，也没有把 shadow 的 `P=0`
施加到 genuine full law。

进一步，本机从 `L_s=L_a exp((a-s)partial_x^2/2)` 的三条 polynomial
heat-lift 公式实际重建并核验了 completed-square determinant：令
`x=(a-s)/v`、`R=r_3/v^(7/2)`，则

`det(N_1(s))/v^7
 =-(R-(t/2)A(x))^2+9(x+3)(5x^2+2)f(x)`，

其中

`A(x)=30x^3-132x^2-24x-36`，

`f(x)=35x^4+110x^3+129x^2+186x-12`。

本机核验 `f'(x)>0`（`x>=0`）、`f(3/50)<0<f(1/16)`，并记录网页给出的
唯一非负根阈值 `xi_*`。同时核验 forward-OU 缩放

`r_k(tau)=tau^(k/2+2)r_k`。

本机输出：

`R48_NULL_DEFECT_HIERARCHY PASSED`、
`R48_DEGREE8_BRANCH_IDENTITY PASSED`、
`R48_SHIFTED_NULL_HANKEL_STRICTLY_INDEFINITE PASSED`、
`R48_INTERIOR_HEAT_LIFT_FORMULAS PASSED`、
`R48_COMPLETED_SQUARE_THRESHOLD_BRACKET PASSED`、
`R48_XI1_SCALAR_THRESHOLD RECORDED`、
`R48_OU_NULL_DEFECT_SCALING PASSED`、
`R48_LIFTED_NULL_THRESHOLD_DIVERGENCE REMAINS OPEN`、
`R48_AUDIT_COMPLETED`。

### 46.2 证据边界与新的最小 OPEN

对每个固定 `K`，ordinary/lifted Gram block 仍可能有严格正 margin；因此
固定阶 positive prefix 不能推出 all-degree realization。网页端将真正的全阶
问题压缩为 moving-rank feasibility threshold `Xi_K`：若定义为满足 rank-2
lower heads、所需 same-factor exact rows 与 `Gamma_K>=0` 的最小 `x=a/v`，
则 `Xi_{K+1}>=Xi_K`，每个固定 `K` 的有限阈值可存在，而是否

`Xi_K -> infinity`

仍完全 OPEN。`K=2` 才首次同时看到 `r_3` 与 `r_5`，即同时看到 `b_7` 与
`b_9` 的两条 defect slots；这解释了 fixed-`K` 论证为何不足。

本轮已关闭：最小 shifted inverse-null positivity 路线，以及 near-flat
Gaussian-divisibility collar 内的“阶数逃逸”解释。仍开放：ordinary
Hamburger/Jacobi tail 的 moving-rank compatibility、`Xi_K` 发散与真实
all-degree positive full-exact law 的存在性。全局 Constraint-Coupled
Non-SOS Graded Value Transgression、Gaussian rigidity、`P_3K` bridge 继续
OPEN；R46 rank>=2 仍不是 no-go。下一轮网页端开始前必须先读取本框架、日志
与 R36–R48 README/audit，并优先证明或反驳 `Xi_K` 的递增发散，而不是重复
固定低阶展开。本轮没有使用 optimizer、SDP、大规模 sweep、relaxed
measure-LP 或 remote computation。

## 47. R49：Christoffel 压缩揭示 lifted-null hierarchy 没有独立正性增益

网页端在读取本机 R48 记录后选择 obstruction 路线，得到一组新的全阶
Christoffel/Schur 恒等式。本机新增
`flat_shadow_christoffel_rankescape_r49/audit_r49.py` 与 README，并以嵌套
仓库真实 HEAD `23abb45b3671693c7fc408caaea7d777b2dcb1c9` 为记录基准。

令 `q(x)=x P(x)=x(x^2-cx-v)`，其中 `c^2=2v`，并令 `Q_K` 是乘以 `q`
在单项式系数上的矩阵。对任意有限 `K`，本机用一般矩符号核验

`Gamma_K = Q_K^T H_(K+3) Q_K`。

因此 lifted-null Gram 是 ordinary Hamburger Gram 的压缩：
`H_(K+3)>=0` 自动推出 `Gamma_K>=0`，不能单独提供更强的正性压力。

设 `pi_n,h_n` 是原矩泛函的 monic orthogonal polynomials/norms，三根为
`zeta=(0,(c+sqrt(c^2+4v))/2,(c-sqrt(c^2+4v))/2)`，并明确采用

`K_n(zeta_i,zeta_j)=sum_(j=0)^n pi_j(zeta_i)pi_j(zeta_j)/h_j`，
`D_n=det K_n(zeta_i,zeta_j)`。

在 `N=K+3` 且原 Hankel 前缀严格正定时，网页给出的 Schur complement
恒等式为

`det(Gamma_K)/det(Gamma_(K-1))
 = h_N + p_N^T K_(N-1)^(-1) p_N`，

其中 `p_N=(pi_N(zeta_i))`。本机用标准高斯和一个精确的归一化五点正
测度逐项核验。进一步核验三根 Vandermonde square 为 `6v^3`，并得到

`det(Gamma_K)=det(H_(K+3))*D_(K+3)/(6v^3)`，

以及 transformed Jacobi quotient

`beta_tilde_K=beta_(K+3)*D_(K+3)*D_(K+1)/D_(K+2)^2`。

这些公式中的新增项是非负的 three-root interpolation leverage，而不是
负反馈；`K=1` 的 `xi_*` 仍只是 ordinary-Hankel 必要下界，`K=2` 虽首次
看到 `r_5/Delta_9`，也不会在原始 Hankel block 正定时自动产生新的
`b_9` obstruction。

本机输出：

`R49_CHRISTOFFEL_COMPRESSION_IDENTITY PASSED`、
`R49_THREE_ROOT_SCHUR_FORMULA GAUSSIAN PASSED`、
`R49_HANKEL_KERNEL_DETERMINANT_FACTORIZATION GAUSSIAN PASSED`、
`R49_TRANSFORMED_JACOBI_RECURSION GAUSSIAN PASSED`、
`R49_THREE_ROOT_SCHUR_FORMULA FIVE_POINT PASSED`、
`R49_HANKEL_KERNEL_DETERMINANT_FACTORIZATION FIVE_POINT PASSED`、
`R49_TRANSFORMED_JACOBI_RECURSION FIVE_POINT PASSED`、
`R49_LIFTED_GRAM_NO_INDEPENDENT_SIGN_PRESSURE RECORDED`、
`R49_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN`、
`R49_AUDIT_COMPLETED`；`py_compile` 亦通过。

证据边界保持严格：即使所有 `Gamma_K` 都正，也至多首先得到
`q^2 L_0` 的正矩测度；要恢复 genuine positive `L_0`，仍需
inverse-Christoffel/Geronimus 可积性、根处无原子及完整 same-factor exact
相干性。故本轮不宣布 `Xi_K->infinity`、ordinary Jacobi exit、Gaussian
rigidity 或 global transgression。

当前最小 OPEN 改写为：对固定有限 `X`，能否对所有 R47-compatible exact
prefix 证明某个有限阶的 ordinary Jacobi exit `S_(n-1)^2>B_n`，或者更强地
证明 root-leverage-dominated exit
`S_(n-1)^2-B_n>=Lambda_n+epsilon(X)`；其中
`Lambda_n=p_n^T K_(n-1)^(-1)p_n/h_(n-1)`。R48 没有给出 moving-`n`
的 leverage 上界、Jacobi drift 或 uniform exit，因此
`Xi_K->infinity` 继续 OPEN。下一轮网页端开始前必须读取本框架、日志和
R36–R49 的 README/audit，并只攻这个 quantitative tail lemma；不得把
fixed-K prefix、`Gamma`-only positivity 或 formal Gateaux coefficient
extractor 当作 genuine full-exact law。

## 48. R50：ordinary-Jacobi 两步中心分离与 tail-budget 形式化

网页端在核对本机 R49 记录后，将当前最小 OPEN 从 lifted-Christoffel
方向收缩为 ordinary Jacobi 的两步延拓问题。本轮网页端读取并核验的嵌套
仓库基准是 `3775204505b223767c71fb13a4b930be5e145875`；本机新增
`flat_shadow_jacobi_center_separation_r50/audit_r50.py` 与 README，审计脚本
对一般矩符号在 `n=3` 做两步 Schur 核验，并对 same-factor pressure 的
`n=2,...,6` 做精确核验。

令当前 odd coordinate `y=m_(2n-1)`，exact row 给出
`m_(2n)=E_n(y)`，并令
`S_(n-1)=(y-y_n^0)/h_(n-1)`。在 `H_(n-1)>0` 时，一步可行性是
`h_n(y)=h_(n-1)B_n-(y-y_n^0)^2`，等价于
`|S_(n-1)|<sqrt(B_n)`。

下一 exact row 中定义
`w_n(y)=(m_(n+1),...,m_(2n-2),y,m_(2n))^T`，
`D_n(y)=E_(n+1)(y)-w_n(y)^T H_(n-1)^(-1)w_n(y)`。自由的
`m_(2n+1)` 可以令两步 Schur off-diagonal 为零；于是穿过下一块的充要
条件是 `h_n(y)>0` 且 `D_n(y)>0`。本轮精确核验了新的凹度恒等式

`D_n''(y)=-2(H_(n-1)^(-1))_(n-2,n-2)
        =-2B_(n-1)/h_(n-1)<0`。

其中第二个等号来自 inverse Gram / orthogonal-polynomial decomposition。
若以 `s=S_(n-1)` 重写，则存在 `M_n` 与 `sigma_n` 使

`D_n(s)=M_n-B_(n-1)h_(n-1)(s-sigma_n)^2`，

故当前一步区间与下一步延拓区间的交叠成为两个显式区间的 overlap
问题。same-factor cubic pressure 的精确导数和 even pivot 为

`partial_(m_(2n-1))G_(n+1)
 =-n(n+1)(n+5)(2/3)^(n+1)m_3`，
`partial_(m_(2n+2))G_(n+1)=3(2/3)^(n+1)`，

所以沿 exact manifold 的中心平移为

`Delta sigma_n^sf
 =n(n+1)(n+5)m_3/(6B_(n-1))`。

这给出可直接攻击的 sufficient tail estimate：若对固定 `X`，所有 viable
prefix 在某个 `n<=N(X)` 满足

`sqrt(2)*n(n+1)(n+5)
 /(6(1+X)^(3/2)B_(n-1))
 >|sigma_n^geom|+sqrt(B_n)+R_n^+`，

其中 `R_n^+=sqrt(M_n/(B_(n-1)h_(n-1)))`，则两区间分离并得到 uniform
finite ordinary-Jacobi exit。该条件本身尚未证明；R50 只把它精确化为
一个 tail-budget lemma，未把 pressure shift 误报成 exit。

固定 `X` 的 rank-2 head 给出 `v>=1/(1+X)`、`m_3^2=2v^3`，故
`|m_3|>=sqrt(2)/(1+X)^(3/2)`；因此最简单的 amplitude-to-zero rank
escape 已排除。但 `R12` 型 raw-moment bounds 不控制 moving inverse-Hankel
spectrum、`h_(n-1)^(-1)`、`B_n` 或 root leverage，仍不足以推出上述统一估计。
固定 `X` 的有限前缀紧性可以沿 R25 的 finite-intersection 逻辑给出
“若每阶 prefix 都存在，则存在 compatible moment sequence”的条件性结论，
但这不是新的 coercivity，也不自动给出 genuine positive inverse-
Christoffel law 或 OU backward preimage。

本机输出：

`R50_SAME_FACTOR_PRESSURE_AND_EVEN_PIVOT PASSED`、
`R50_ONE_STEP_VIABILITY_INTERVAL n=3 PASSED`、
`R50_TWO_STEP_CURVATURE n=3 PASSED`、
`R50_TWO_STEP_EXTENSION_CRITERION n=3 PASSED`、
`R50_SAME_FACTOR_CENTER_SHIFT PASSED`、
`R50_INTERVAL_OVERLAP_COMPLETION PASSED`、
`R50_FIXED_X_HEAD_NONZERO PASSED`、
`R50_FIXED_HEAD_TWO_STEP_EXIT REMAINS OPEN`、
`R50_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN`、
`R50_FIXED_X_COMPACTNESS REMAINS CONDITIONAL`、
`R50_AUDIT_COMPLETED`；并通过 `py_compile` 与 `git diff --check`。

证据边界：本轮没有证明 ordinary Jacobi exit、`Xi_K->infinity`、Gaussian
rigidity、`P_3K` bridge 或 global transgression；R46 rank>=2、R48 collar
与 R49 Christoffel compression 的边界全部保留。下一轮网页端必须先读取本
框架、日志与 R36–R50 README/audit，然后只推进
`Fixed-Head Two-Step Jacobi Center-Separation / Tail-Budget Lemma`：要么
给出 `B_n`、`sigma_n^geom`、`R_n^+` / inverse-Hankel spectrum 的全阶
控制并证明 uniform exit，要么构造严格 compatible 的 bounded-`x` all-degree
chain。不得用 fixed-K compactness、`Gamma`-only positivity 或 formal
系数提取冒充 genuine full-exact law，也不得使用 optimizer、SDP、sweep、
relaxed measure-LP 或 remote computation。

## 49. R51：优化后的 two-step Jacobi budget 与 cubic-trace tracking（2026-09-06）

网页端在开始本轮前通过已连接 Codex 读取了本机总纲、工作日志和 R36–R50
审计，并核对嵌套仓库真实 HEAD 为 `c04f58c4ec34138f6a1bec25b8e4983e775dd269`。
本机新增 `flat_shadow_two_step_budget_r51/audit_r51.py` 与 README；本轮只
核验网页端新出现的 exact all-degree algebra，不把 conditional theorem 当成
已完成的 obstruction。

R51 首先把自由的下一 odd moment 选择解释为消去两步 Schur off-diagonal：在
当前 viable prefix 上，这等价于 formal Jacobi 坐标 `S_n=0`。令
`\hat B_(n+1)` 表示当前 `S_(n-1)=0` 且下一步 `S_n=0` 的
doubly-centered formal extension 的 next Jacobi budget。则新的 transfer law 为

`D_n(0)/h_(n-1)=B_n*\hat B_(n+1)`,

`D_n(s)/h_(n-1)=B_n*\hat B_(n+1)
  +2*B_(n-1)*sigma_n*s-B_(n-1)*s^2`。

因此 completed square 给出

`(R_n^+)^2=sigma_n^2+B_n*\hat B_(n+1)/B_(n-1)`。

在当前区间 `|s|<sqrt(B_n)` 上优化后，严格两步延拓的充要条件可以压成

`V_n=B_n*\hat B_(n+1)+B_(n-1)*Psi_(sqrt(B_n))(sigma_n)>0`,

其中 `Psi_r(sigma)=sigma^2`（`|sigma|<=r`），否则为
`2*r*|sigma|-r^2`。故 ordinary two-step exit 等价于 `V_n<=0`，而 rescue
项始终非负。特别是 `\hat B_(n+1)>=0` 时，same-factor center pressure
把中心推远并不会自动造成区间分离；R50.21 的 pressure-vs-radius sufficient
路线若要成功，必须先有一个负的 centered next budget。

R51 还把 R50 的 geometric center 识别为 doubly-centered Jacobi truncation
`J_n^circ` 的 cubic trace：

`B_(n-1)*sigma_n
 =n*(n+1)*(n+5)*m_3/6-tr((J_n^circ)^3)/3`,

并给出尾部当前 `S_(n-1)=s`、下一步 `S_n=0` 下的 affine law

`tr(J_n(s)^3)=tr((J_n^circ)^3)+3*B_(n-1)*s`。

写 `A_n=B_(n-1)*sigma_n` 后，优化 rescue 项的两支为

`R_n=A_n^2/B_(n-1)`，当 `|A_n|<=B_(n-1)*sqrt(B_n)`；

`R_n=2*|A_n|*sqrt(B_n)-B_(n-1)*B_n`，否则。

由此得到的可审计 conditional theorem 是：固定有限 `X`，若每个 compatible
prefix 在某个 `4<=n<=N(X)` 同时满足
`|A_n|<=kappa_X*B_(n-1)*sqrt(B_n)`、
`\hat B_(n+1)<=-theta_X*B_(n-1)` 且 `theta_X>kappa_X^2`，则
`V_n<0`，ordinary Jacobi exit 在 `N(X)+1` 之前发生。R51 只核验了这个
蕴含的代数；没有证明两个 tail hypotheses。当前真正缺的 one-lemma 因而
从 R50 的三量 tail bound 收缩成 `cubic-trace tracking` 加
`centered-budget negativity`，而 root-leverage-dominated exit 仍然更强、
更靠后。

本机输出：

`R51_DOUBLY_CENTERED_TRANSFER_IDENTITY PASSED`、
`R51_RADIUS_AND_OPTIMIZED_FUNCTIONAL PASSED`、
`R51_CENTERED_BUDGET_EXIT_ALGEBRA PASSED`、
`R51_CUBIC_JACOBI_TRACE_AFFINE_LAW PASSED`、
`R51_CUBIC_TRACE_CENTER_REDUCTION PASSED`、
`R51_FIXED_HEAD_TWO_STEP_EXIT REMAINS OPEN`、
`R51_ROOT_LEVERAGE_DOMINATED_EXIT REMAINS OPEN`、
`R51_XI_DIVERGENCE REMAINS OPEN`、
`R51_AUDIT_COMPLETED`；并通过 `py_compile` 与 `git diff --check`。

证据边界：R51 没有证明 ordinary Jacobi exit、`Ξ_K->infinity`、Gaussian
rigidity、`P_3K` bridge 或 global transgression；fixed-K formal prefix、
genuine all-degree full-exact law 与 formal Gateaux/Hermite extractor 仍严格
区分。下一轮网页端必须先读取本框架、日志和 R36–R51 README/audit，再攻
`Uniform Cubic-Trace Tracking + Centered-Budget Negativity Lemma`，或构造
真正兼容的 bounded-`x` all-degree chain；不得重复巨大 determinant，也不得
使用 optimizer、SDP、sweep、relaxed measure-LP 或 remote computation。

## 50. R52：全局路线审计与 trace–budget obstruction（2026-09-06）

网页端本轮首先通过已连接 Codex 读取 `THEORY_ROUTE_FRAMEWORK.md`、
`PROJECT_WORKLOG_APPEND.md` 及 R36–R51 README/audit，并核对嵌套仓库真实
HEAD 为 `f7025279f3d625d5257e26319ed079a74e2bcb53`。本轮先做整体路线审计，
再推进 R51 的 ordinary-Jacobi target；没有回到固定阶 determinant。

### 50.1 全局进度与路线边界

R36–R51 已完成三次机制级压缩：

1. R36–R38 排除一体远端 carrier，并识别出二体 degenerate
   Laguerre–Hoeffding carrier 的 `n^(-1/2)` 级 anchor 损失和固定头响应；
2. R39–R47 把 constraint-coupled positivity、mixed-Hessian residue 与
   N+6 quotient rank 分开，corrected R46/R47 表明有限 same-factor
   Fock/Hermite 关系不能把两个响应方向压成一个；
3. R48–R51 把 inverse-heat / lifted-Christoffel 层压回 ordinary
   Hankel/Jacobi tail，并得到 exact two-step budget 与 cubic-trace 坐标。

因此，继续增加固定 `m` 的低阶 determinant 会真正进入局部重复；当前关口
是 global coherence barrier：必须证明 all-degree exactness 产生的 centered
deficit 超过 odd-center/cubic-trace rescue，或者构造 genuine bounded-`x`
all-degree positive chain。R49 的 Christoffel compression 没有额外负号资源，
R50–R51 的 center pressure 也不是自动 exit。

目前最成熟、可以独立整理为 theorem package 的方向是：R11–R13 的
exact-class tail/OU closure/projectively-compatible tower rigidity；R36–R44
的 two-body Laguerre–Hoeffding generator、fixed-head asymptotics 与
finite-grade transgression；R48–R51 的 inverse-heat/Christoffel 到
ordinary-Jacobi reduction 与 optimized two-step budget。这里记录的是数学
自包含程度，不把文献新颖性当作已核验事实。Gaussian rigidity 尚未完成；
`P_3K != 0`、固定 `m_3`、rank-two head 与 Jacobi exit 也仍逻辑独立，当前
没有 `P_3K` charge-to-exit bridge。

### 50.2 R52 无条件 Jacobi identities

对 monic Jacobi recurrence

`x*pi_k=pi_(k+1)+alpha_k*pi_k+beta_k*pi_(k-1)`、`beta_k>0`，定义
`S_k=sum_(j=0)^k alpha_j`、`S_(-1)=0`、`B_k=beta_k+S_(k-1)^2`，并令
`T_k=tr(J_k^3)`。逐闭路计数给出

`T_k-T_(k-1)=alpha_k^3+3*beta_k*(alpha_(k-1)+alpha_k)`,

以及

`T_k-T_(k-1)=(S_k-S_(k-1))^3
  +3*(B_k-S_(k-1)^2)*(S_k-S_(k-2))`.  (A.3)

固定旧 prefix `S=S_(n-2)`，取 `s=S_(n-1)`、`t=S_n`，two-control law 为

`tr(J_n(s,t)^3)-tr((J_n^circ)^3)
  =3*B_(n-1)*s+t^3-3*s*t^2+3*B_n*t`.  (A.4)

特别地，`t=0` 时

`A_n=B_(n-1)*sigma_n
  =n*(n+1)*(n+5)*m_3/6-tr((J_n^circ)^3)/3`.  (A.5)

这些是 genuine full-exact Jacobi identities，不使用 Gateaux 提取，也不能
把 fixed-K prefix 变成概率律。

### 50.3 centered budget 与 sharp rescue cone

R51 的位移变量 `s` 满足

`(B_n-s^2)*B_(n+1)(s)
  =B_n*B_(n+1)+2*A_n*s-B_(n-1)*s^2`.  (A.7)

位移变量的完成平方为

`B_n*B_(n+1)-B_(n-1)*(s-A_n/B_(n-1))^2
  +A_n^2/B_(n-1)`。

实际 compatible chain 的坐标 `S_(n-1)` 另满足

`B_n*B_(n+1)=beta_n*beta_(n+1)+beta_n*S_n^2
  +B_(n-1)*S_(n-1)^2-2*A_n*S_(n-1)`,  (A.8)

其完成平方为

`beta_n*beta_(n+1)+beta_n*S_n^2
 +B_(n-1)*(S_(n-1)-A_n/B_(n-1))^2-A_n^2/B_(n-1)`.  (A.9)

两式的变量和符号不同，不能混合。由实际链式式可得
`B_(n+1)>-A_n^2/(B_(n-1)*B_n)`，且 `B_(n+1)<0` 必须有
`A_n*S_(n-1)>0`。令

`a_n=|A_n|/(B_(n-1)*sqrt(B_n))`,

`Phi(a)=a^2`（`0<=a<=1`），`Phi(a)=2*a-1`（`a>=1`）。在
`|S_(n-1)|<sqrt(B_n)` 上优化 rescue 后，strict compatibility 的必要条件为

`B_(n+1)/B_(n-1)+Phi(a_n)>0`.  (A.13)

于是，若固定有限 `X` 下存在 `4<=n<=N(X)` 使
`|A_n|<=kappa_X*B_(n-1)*sqrt(B_n)`、
`B_(n+1)<=-theta_X*B_(n-1)`，且 `theta_X>Phi(kappa_X)`，则 two-step
viability value 为负，ordinary Jacobi exit 发生。对 `kappa_X>1`，新阈值
`2*kappa_X-1` 优于旧的 `kappa_X^2`。

### 50.4 当前 OPEN 与较弱里程碑

R52 没有证明 `Uniform Cubic-Trace Tracking + Centered-Budget Negativity`。
障碍是具体的：cubic trace 控制 linear/center channel，而 centered budget
是独立 constant channel；R46–R47 的 rank-two survival 正是同一结构在
有限 Fock 坐标中的表现。R12 的 square-exponential tail 也不足以控制
moving inverse-Hankel spectrum、`B_n`、`h_(n-1)^(-1)` 或 Jacobi spikes。

更值得优先的弱命题是 `Canonical Centered-Tail Rigidity`：固定一个
R47-compatible bounded-`X` head，之后每个新 odd slot 取 `S_k=0`，并由
exact `G_(k+1)=0` 决定 even moment；目标为

`forall X<infinity, canonical centered branch 在有限阶出现 B_k<=0`. (D.1)

若 D.1 失败且所有 `B_k>0`，则 Jacobi norms 保持正，Hamburger 定理给出
positive representing law；exact `G_k=0` 给出 `E[Q^k]=2^k*k!`，且
`S_k=S_(k-1)=0` 后 `alpha_k=0`，形成具有 eventually-zero Jacobi diagonal
的 genuine infinite-chain candidate。它仍需 positive backward OU preimage，
但比形式 prefix 强得多，因而是清晰的可证/可反证二分法。

本机新增 `flat_shadow_trace_budget_r52/audit_r52.py` 与 README。exact
symbolic audit 通过：

`R52_FULL_EXACT_JACOBI_TRACE_INCREMENT PASSED`、
`R52_S_COORDINATE_TRACE_INCREMENT PASSED`、
`R52_TWO_CONTROL_CUBIC_TRACE_LAW PASSED`、
`R52_CENTERED_BUDGET_COMPLETE_SQUARE PASSED`、
`R52_SHARP_RESCUE_CONE_AND_CONDITIONAL_EXIT PASSED`、
`R52_UNIFORM_TRACE_BUDGET_LEMMA REMAINS OPEN`、
`R52_CANONICAL_CENTERED_BRANCH_EXIT REMAINS OPEN`、
`R52_GAUSSIAN_RIGIDITY REMAINS OPEN`、
`R52_P3K_BRIDGE REMAINS OPEN`、`R52_AUDIT_COMPLETED`；并通过 `py_compile`。

证据边界：本轮只审计 exact algebra 与 conditional implication，没有声称
ordinary Jacobi exit、D.1、`Xi_K->infinity`、Gaussian rigidity、`P_3K`
bridge 或 global transgression 已完成。下一轮网页端开始前必须读取本框架、
工作日志及 R36–R52 README/audit；优先攻 D.1 的 canonical centered branch，
不得重复 determinant，也不得使用 optimizer、SDP、sweep、relaxed measure-LP
或 remote computation。
