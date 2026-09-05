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

## 22. 已探索路线与停止条件

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

## 23. 每轮协作协议

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

## 24. 当前 checkpoint

- C2C task：`c2c_7b4e`。
- 已完成：R12、R13、R14、R15、R16、R17、R18、R19、R20、R21、R22、R23、R24、R25、R26。R14 证明 primitive-to-Gaussian 序列在任意
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
  `R26_AUDIT_COMPLETED`。`P_3K` 仍没有 quantitative bridge。
- 当前方向：R26 已完成，最小 OPEN 改为 `Residual-Corrected Flat Null-Square
  Hardy Gain`：在严格 genuine full-exact iid 类内证明或否定 `A_M>=E_M`，或
  找到等价的 residual-corrected common/residual coherence。下一轮先做一阶符号
  测试与最小可审计的非标量 HS/matrix candidate；若仍无桥，则记录新的
  full-exact-compatible no-go，不重复 common-only scalar escort 展开。只有关闭
  one-step sign 后，才回到 residual Laguerre `<3M` 与 R21 cubic amplifier。
- 结论状态：主命题仍 OPEN；没有 Gaussian rigidity 的无条件证明，也没有真实概率
  律反例。
