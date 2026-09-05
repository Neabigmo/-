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

## 13. 已探索路线与停止条件

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

## 14. 每轮协作协议

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

## 15. 当前 checkpoint

- C2C task：`c2c_7b4e`。
- 已完成：R12、R13、R14、R15、R16、R17。R14 证明 primitive-to-Gaussian 序列在任意
  固定 frequency/Gram complexity 内最终通过 confluent Bochner tests；R15
  又证明 genuine full-exact primitive 的逆候选若在任意一个非空小窗口内
  对所有 Gram size 都 PSD，就会由 order-2 矩增长升级为全局正定，故频率
  escape 被无条件排除。剩余唯一 Bochner 缺口是 `M_r→∞` 的
  inverse-Hankel rank escape；R16 又把它等价重写为 primitive stratum 的弱
  闭合/尾到头 viability 问题；R17 提取了 OU–Laguerre 全阶加权 viability
  不等式，但证明它不足以自动给出跨 sector 的谱尾紧性；另保留 `P_3K`
  sector 限定。
- 当前方向：R18，攻击 `All-Degree Spectral-Tail Tightness`：寻找 full-exact
  product structure 对 OU eigenmode/Laguerre/Jacobi moving-scale 尾的统一
  控制，或构造严格的 simultaneous-all-degree no-go；继续单独审计 `P_3K`
  survival。
- 结论状态：主命题仍 OPEN；没有 Gaussian rigidity 的无条件证明，也没有真实概率
  律反例。
