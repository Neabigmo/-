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

## 58. R61：corrected degree-16 cutoff（2026-09-06）

R61 的可靠结论仍是 degree 16 产生新的 finite sign cutoff，但网页端给出的
`m_16`、`P_8` 及 norm fractions 未通过本机 Gaussian sanity check 与
degree-16 relation 核验。故本机按 R60 的正确 `P_7`、`beta_7=h_7/h_6` 重新
生成 degree-16 continuation。

令 `a=m_3,t=a^2`。由 `alpha_7=0` 和 degree-16 same-factor row，在本机
exact rational family points 上核验的矩为

`m_15=a(42287t^5-330144t^4+228921t^3+556826t^2
       +306060t-531720)/(2-t)^3`,

`m_16=3(12981388t^3-26820320t^2-837195t+1351350)/(2-t)`。

校正后的 degree-12 sign polynomial 是

`P_8(t)=1204550144t^12-35494536455t^11-2967319034778t^10
       +24133342031328t^9-68513207463264t^8+75535499377824t^7
       -6513636214656t^6-32358682547712t^5+576720933888t^4
       +8343384129536t^3-662433824768t^2-28728360960t+1651507200`。

直接按正确 norm 方向得到

`h_7=3P_7/[(2-t)^3p_5]`,
`h_8=-3P_8/[2(2-t)^3P_6]`,

`beta_8=h_8/h_7=-p_5P_8/(2P_6P_7)`。

在 `0<t<tau_6` 上，`p_5>0,P_7>0,P_6<0`，所以 `sign(beta_8)=sign(P_8)`。
精确值 `P_8(0)=1651507200>0`、
`P_8(1/25)<0`；`P_8'` 在 `[0,1/25]` 的 Bernstein 系数全负，
而 `P_8` 在 `[1/25,9/100]` 的 Bernstein 系数全负。结合 R59 的
`P_6` 严格递增性和 `P_6(9/100)>0`（故 `tau_6<9/100`），得到唯一

`tau_8 in (0,1/25)`，`P_8(tau_8)=0`,

并且在 `0<t<tau_6` 上

`beta_8>0 <=> 0<t<tau_8`,
`beta_8<0` 于 `tau_8<t<tau_6`。

这比网页端未校正的约 `0.085` cutoff 更小；本机正确结果把窗口再次压缩
到 `tau_8<0.04`。它仍只是 finite-stage contraction：尚未证明所有固定
`t>0` 最终退出，也没有构成 full-exact non-Gaussian counterexample。

本机新增 `flat_shadow_canonical_beta8_r61/audit_r61.py` 与 README。审计通过
degree-16 row、`m_15/m_16`、Gaussian `h_7=5040,h_8=40320,beta_8=8` 的
exact rational checks，以及两个 Bernstein sign certificates；没有使用
determinant、optimizer、SDP、sweep、relaxed measure-LP 或 remote computation。
当前偶数 cutoff 的可靠部分是 `tau_6>tau_8>0`，中间 `beta_7` 全程正。
下一唯一 lemma 是 `beta_9` 在 `0<t<tau_8` 上的 corrected degree-18 sign
lemma。D.1、eventual skew annihilation、Gaussian rigidity 与 `P_3 K`
bridge 仍分别 OPEN。

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

## 51. R53：canonical centered tail 与 moving Gauss-quadrature deficit（2026-09-06）

网页端本轮在同一 Project 对话中完成 READ_FIRST，核对嵌套仓库 HEAD 为
`abee8f94007648df2d349f9e3e856ae6ca307a1e`，并重新读取总纲、工作日志及
R36–R52 README/audit。全局判断是：R11–R13、R36–R44、R48–R52 已足够整理为
三个层级不同的自包含 theorem package；R45–R47 更适合作为桥。这里仍不把
“自包含”写成已核验的文献新颖性。

R53 确认 D.1 是正确的下一层 model problem，但不是最终等价问题：固定
`S_k=0` 会移除 arbitrary-control chain 中可能提供 rescue 的 odd controls。
它的价值在于：一旦失败，得到的是 genuine all-degree positive law，而非
fixed-prefix 或 Gateaux extractor。

### 51.1 canonical Jacobi tail

对 monic recurrence

`x*pi_n=pi_(n+1)+alpha_n*pi_n+beta_n*pi_(n-1)`、
`h_n=||pi_n||^2`、`beta_n=h_n/h_(n-1)`、
`S_n=sum_(j=0)^n alpha_j`、`B_n=beta_n+S_(n-1)^2`，full-exact factorization

`G_n=c_n*h_(n-1)*(beta_n+S_(n-1)^2-B_n)`,
`c_n=3*(2/3)^n`

给出 canonical tail 上（连续两个新 centered slots 之后）

`alpha_n=0`, `B_n=beta_n`,
`pi_(n+1)=x*pi_n-B_n*pi_(n-1)`,
`h_n=B_n*h_(n-1)=h_K*product_(j=K+1)^n B_j`.

因此在前面 Jacobi block 正的前提下，canonical finite exit 精确等价于
某一步 `B_n<=0`。

### 51.2 moving Gauss-quadrature deficit

令 `nu_(n-1)` 为 n 点 Jacobi truncation 的 spectral measure，记
`q_r(n)=integral x^r d nu_(n-1)(x)`。它匹配现有矩到 `2n-1`，并满足

`m_(2n)-q_(2n)(n)=h_n`,
`m_(2n+1)-q_(2n+1)(n)=(S_n+S_(n-1))*h_n`.

第二式中的 `2*S_(n-1)` 来自 degree-`2n` error，不能误写成
`alpha_n*h_n`。所以 canonical choice `S_(n-1)=S_n=0` 恰好令
`m_(2n+1)=q_(2n+1)(n)`。

若 `delta_n` 表示目标 chi-square cubic-product moment 与 n 点 product
quadrature 的差，则 exact same-factor row 给出

`delta_n=c_n*h_n`,
`h_n=(3^(n-1)/2^n)*delta_n`,
`B_n=beta_n=(3/2)*(delta_n/delta_(n-1))`.

于是（在前级 norm 正时）
`B_n<=0 <=> delta_n<=0`。D.1 被压缩为一个 moving product
Gauss quadrature 是否必在有限阶对目标矩 overshoot 的问题。

### 51.3 条件性二分法与新的 OPEN

若所有 canonical `B_n>0`，Favard/Hamburger 给出 genuine positive representing
law；`G_n=0` 给出完整 `E[Q^n]=2^n*n!`，且 centered tail 的 Jacobi diagonal
eventually 为零。这是 genuine full-exact candidate，但仍需 positive backward
OU preimage，不能直接推出原 Gaussian rigidity，也不能自动给出 `P_3K != 0`。

若要证明 D.1，只需排除该 candidate class。一个更弱但可报告的充分目标是

`mu in E, alpha_n=0 eventually => m_3(mu)=0`。

Eventual zero Jacobi diagonal 本身不足以推出原 law 对称：有限 Jacobi head
可以保留 skewness。R12 raw-tail 也不控制 moving quadrature nodes、weights、
inverse-Hankel conditioning 或 deficit sign。故 canonical finite exit、eventual
skew annihilation、Gaussian rigidity、`P_3K` bridge 与 arbitrary-control exit
继续 OPEN。

本机新增 `flat_shadow_canonical_tail_r53/audit_r53.py` 与 README，审计
Jacobi tail、Gauss even/odd error、deficit/norm ratio、cubic stabilization 及
条件性 Favard positivity；没有 determinant、optimizer、SDP、sweep、relaxed
measure-LP 或 remote computation。证据边界严格保留：条件性 realization
不是 canonical positivity 的证明。

## 52. R55：finite skew head、eventual zero tail 与 factorial-escape target（2026-09-06）

R55 沿同一 Project 对话继续检查 canonical centered branch 失败时的全局
含义。它没有找到 genuine full-exact counterexample，但把一个容易混淆的
逻辑点钉死：eventual zero Jacobi diagonal 并不推出原始 law 对称。

### 52.1 finite head 保留 skew

在 centered variance-one 归一化 `alpha_0=0`、`beta_1=1` 下，取

`alpha_0=0, alpha_1=a, alpha_2=-a, alpha_n=0 (n>=3), beta_n=1`。

有限 Jacobi 代数给出

`m_1=0, m_2=1, m_3=a, m_4=2+a^2`。

所以 `a!=0` 时 finite head 保留非零 skew；`a=1/2` 给出 `m_4=9/4`，
不满足 target `m_4=3`，故这只是 control/obstruction example，不是 full-exact
反例。对应的无限 `beta_n=1` chain 是 bounded positive Favard example，
但它只说明“正性 + eventually symmetric tail”不足以推出原始对称性。

对 symmetric Jacobi resolvent，tail m-function 满足

`m_k(z)=1/(z-alpha_k-beta_(k+1)m_(k+1)(z))`。

任意 finite positive head 都是 tail m-function 的非恒定 Möbius 复合；
正 `beta` 使其对 tail 的导数不是恒等于零。因此要消掉 `m_3`，必须使用
整个 full-exact moment system 或额外的 tail-transfer 约束，不能只用
eventual diagonal zero。

### 52.2 factorial envelope 的逻辑修正

R55 中提出的

`limsup (1/n) log(n!/h_n)=+infinity`

不能等价替代 R12 的 `h_n<=C*A^n*n!` 包络失败。对 `h_n>0`，正确的
root-test 等价是

`exists finite C,A: h_n<=C*A^n*n!`
`<=> limsup (h_n/n!)^(1/n)<infinity`，

亦即包络失败要求

`limsup (1/n)log(h_n/n!)=+infinity`

或等价的 `liminf (1/n)log(n!/h_n)=-infinity`。原先 reversed-log 的正
limsup 甚至可与有效包络共存，不能作为 contradiction。故真正的
`Skew-Forced Factorial Escape Lemma` 仍需从 full-exact recurrence 推导额外
的 lower-growth/invariant，不能由 R12 upper envelope 单独推出。

### 52.3 全局二分与下一步

若 canonical branch 有限到达 `B_n<=0`，则得到 D.1；若所有 `B_n>0`，
Favard/Hamburger 给出 genuine positive full-exact candidate，并带有
eventually zero Jacobi diagonal，但 R55 证明其 tail shape 不足以让 `m_3=0`。
因此下一轮唯一值得推进的是

`R56 — Skew-Forced Factorial Escape Lemma`：

对 `mu in E`、full-exact、eventually `alpha_n=0` 且 `m_3!=0` 的链，或者
证明某个 `beta_n<=0`，或者证明校正后的 factorial root-growth escape；若
做不到，则给出成立该结论所需的最弱额外 tail-transfer condition，并说明
它是否可由 R12/R47 得到。D.1、Gaussian rigidity 与 `P_3 K` bridge 仍是
OPEN，三者不能互相冒充已证。

本机新增 `flat_shadow_skew_forced_escape_r55/audit_r55.py` 与 README。审计
通过 finite-head moments、非恒定 Möbius tail coupling、factorial-envelope
逻辑与条件 deficit sign，并显式保留 R56、D.1、Gaussian rigidity、`P_3 K`
bridge 的 OPEN 边界。下一轮网页端必须先读取本框架、工作日志及 R36–R55
相关 README/audit。

## 53. R56：factorial-escape gap 的严格边界（2026-09-06）

R56 要求证明或反驳 `Skew-Forced Factorial Escape Lemma`：full-exact、
positive Jacobi/Favard、`alpha_n=0 eventually` 且 `m_3!=0` 是否必然导致
有限 `beta_n<=0` 或违反 `h_n<=C A^n n!`。网页端没有完成证明或反例，
但把真正缺口定位为：exact recurrence 目前只有 moving deficit/norm 的
上界/递推信息，而 R12 只提供 `h_n` 的 upper envelope；尚未得到 lower
growth 或 sign mechanism。

### 53.1 必须保留的 root-test 修正

`limsup (1/n)log(n!/h_n)=+infinity` 不能与 envelope failure 等价。反例
`h_n=n!/2^(n^2)` 同时满足 `h_n<=n!` 与该 reversed-log limsup。正确的
等价式是

`exists finite C,A: h_n<=C A^n n!`
`<=> limsup (h_n/n!)^(1/n)<infinity`，

因此 envelope failure 等价于

`limsup (1/n)log(h_n/n!)=+infinity`

或 `liminf (1/n)log(n!/h_n)=-infinity`。这是逻辑修正，不是从
full-exact recurrence 得到的 escape 结论。

### 53.2 可保留的 exact identity 与证据边界

canonical centered tail 在此前级 norm 正时仍满足

`delta_n=c_n h_n`, `c_n=3(2/3)^n`,
`beta_n=(3/2)delta_n/delta_(n-1)`。

所以已知正链上 `delta_n>0`，而 `beta_n<=0` 是 finite canonical exit；
但这是 candidate chain 的条件传播，不能反过来证明下一步正性。R56 没有
产生 genuine full-exact positive non-Gaussian counterexample，也没有证明
eventual-diagonal skew annihilation。

若未来证明该桥，则可推出 R12 类上的 `alpha_n=0 eventually=>m_3=0`，
从而结合 R47 bounded-head 下界关闭 D.1；仍不能自动推出 Gaussian rigidity
或 `P_3 K` bridge。三者继续区分。

本机新增 `flat_shadow_skew_forced_escape_r56/audit_r56.py` 与 README，审计
通过两组 factorial-growth counterexample 与 canonical deficit constants，
并显式保留 R56、D.1、Gaussian rigidity、`P_3 K` 的 OPEN 边界。下一轮须
先读取框架、工作日志与 R36–R56 README/audit，直接寻找 all-degree invariant、
真正 full-exact counterexample，或可由 backward-OU positivity 提供的最弱
tail-transfer 条件。

## 54. R57：从 factorial escape 转向 canonical viability（2026-09-06）

R57 完成了本段最重要的路线修正。对 positive canonical exact branch，
moving product Gauss measure 上 `Q_n>=0`，所以

`0<delta_n<=2^n n!`，`delta_n=c_n h_n`、`c_n=3(2/3)^n` 给出

`0<h_n<=3^(n-1)n!`。

因此只要所有前级 `beta_n>0`，factorial-exponential envelope 自动成立，
甚至不需要 R12。`m_3!=0 => envelope failure` 不可能成为 D.1 的证明。
真正二分被压缩为

`finite sign exit: delta_n<=0 (equiv. beta_n<=0)`

或

`infinite positive exact viability: delta_n>0 for all n`。

第二项若成立，R53 的 Favard/Hamburger 机制才会产生 genuine full-exact
positive law；它不是 finite prefix，也仍不自动处理 backward-OU tower。

### 54.1 可审计的 finite-stage skew family

令 `a=m_3`、`t=a^2`，取 canonical `alpha_2=-a`、`alpha_n=0 (n>=3)`。
网页端给出的前几阶矩为

`m_4=3, m_5=4a, m_6=15+7a^2, m_7=15a,`
`m_8=105+4a^2,`
`m_9=a(96-112a^2-49a^4)/(2-a^2),`
`m_10=945-234a^2`。

monic recurrence 给出

`pi_2=x^2-a x-1, pi_3=x^3-3x-a,`
`h_2=2-a^2, h_3=6(1+a^2)`。

本机约定 `beta_n=h_n/h_(n-1)`，故

`beta_2=2-a^2, beta_3=6(1+a^2)/(2-a^2)`。

后续 `beta_4=h_4/h_3`、`beta_5=h_5/h_4` 由本机符号审计直接重算，避免
浏览器纯文本分式倒置。`a=1/10` 时 `beta_2,...,beta_5` 全正，说明
非零 skew 不会在前五级 exact/canonical rows 自动消失；这仍只是
finite-stage family，`beta_6,beta_7,...` 与 full-exact infinite viability
继续 OPEN。

### 54.2 backward-OU positivity 的真实贡献

若 `mu=P_lambda nu`、`0<lambda<1`，对任意 monic degree-`n` polynomial，
条件 Gaussian Hermite 分解给出

`h_n(mu)>= (1-lambda)^n n!`。

结合 `G_2=0` 的 `h_2=2-m_3^2`，得到严格的

`m_3^2<=2lambda(2-lambda)`。

所以若有 arbitrarily-deep positive OU divisibility `lambda_j->0`，则
`m_3=0`；固定因子的无限兼容 backward tower 满足此条件。这是一个干净
的 conditional skew-annihilation lemma，但不等同于 single eventual-zero
diagonal 的 D.1，也不关闭 Gaussian rigidity 或 `P_3 K` bridge。

本机新增 `flat_shadow_canonical_viability_r57/audit_r57.py` 与 README，审计
finite-stage moments、Jacobi beta orientation、`a=1/10` 的前五级正性、
positive-branch upper envelope 与 OU norm bound。R57 明确关闭的是
factorial-growth 路线，不是 D.1；下一轮唯一主攻应是 surviving
`0<a^2<32-12sqrt(7)` 中 moving `delta_n(a)` 的有限变号，或证明其存在
infinite positive exact chain。相关 theorem 仍需与 Gaussian rigidity、
`P_3 K` bridge 分开。

## 55. R58：OU tower 与 Favard/Jacobi realization 的桥接边界（2026-09-06）

R58 直接审计 R53–R57 最容易被偷换的一步：若 canonical branch 的所有
`beta_n>0`，Favard/Hamburger 给出的 `mu_*` 是否自动继承原始正 OU tower
`g^(j)=P_q g^(j+1)`。网页端本轮只完成了对象区分，未在生成长链中给出严格
operator/measure map，随后被安全停止；故不能把它记作 bridge 已证。

这里必须区分三层对象：原始假设中的正密度 `g^(j)` 及其 OU action；由
escort 或 cubic row 产生的 ordinary moment functional；以及 R53 用 Favard
重建的 Jacobi 变量 `x` 的谱测度。Favard 只从正 Hankel/Jacobi 数据重建最后一
个对象。除非另有定理同时证明 law identification（或显式 map）、归一化保持、
`x` 矩/monic norm 保持以及与 `P_lambda` 的 intertwining，否则
`mu_*=P_(q^N)nu_N` 不能从 `g^(j)=P_qg^(j+1)` 推出。

### 55.1 可保留的 conditional theorem

若上述 bridge 以后被严格建立，并且 R53 law 满足对所有 `N`

`mu_*=P_(q^N)nu_N`, `0<q<1`,

同时 exact second row 给出 `h_2(mu_*)=2-m_3(mu_*)^2`，则 Gaussian
conditional-Hermite bound 立即给出

`h_2(mu_*) >= 2(1-q^N)^2`,
`m_3(mu_*)^2 <= 2q^N(2-q^N)`。

令 `N->infinity` 得 `m_3(mu_*)=0`。这会关闭“eventually zero Jacobi
diagonal + arbitrarily deep positive OU divisibility 仍保留 finite-head skew”
这一候选分支；它只关闭 D.1 的一个 conditional/eventual-skew 层，不等于
原始 law 的 Gaussian rigidity，也不等于 `P_3 K` bridge。

### 55.2 R58 的证据边界与下一步

本机新增 `flat_shadow_ou_jacobi_bridge_r58/audit_r58.py` 与 README，审计
conditional OU degree-two algebra、`q^N->0` 的极限及桥接所需的四项数据，
但明确打印 Favard law 的 OU inheritance 仍 OPEN。R58 因网页端未完成而不是
数学结论；下一轮 R59 必须二选一：给出显式 OU–Favard transfer lemma 并逐项
验证，或明确指出当前假设不足并转入 canonical moving-deficit 的一条具体
`beta_6/beta_7` 递推。不得再把 auxiliary spectral law 当作原始 OU density。

R58 继续保留 D.1、infinite positive exact viability、Gaussian rigidity 与
`P_3 K` bridge 的独立 OPEN 状态；没有使用 determinant、optimizer、SDP、
sweep、relaxed measure-LP 或 remote computation。下一轮网页端开始前必须读取
本框架、工作日志及 R36–R58 相关 README/audit，但只需先处理本桥接边界与
R53/R57 的相关公式，避免重复扫描整套历史。

## 56. R59：canonical beta6 positivity contraction（2026-09-06）

R59 对 R58 的桥接问题给出明确选择 (II)：R53 的 Favard/Hamburger
`mu_*` 只是 canonical ordinary moment functional 在 Jacobi 变量 `x` 上的
谱测度。原始 `g^(j)` 相对 OU 不变 Gaussian 的密度所对应的 ordinary law
`lambda_j=g^(j)gamma` 确实满足 `lambda_j=P_q lambda_(j+1)`，但 escort 的
非线性重加权/归一化不与 `P_q` 交换；更没有证据说明 canonical odd controls
所选的 `m_k^*` 是原始 `lambda_0` 的全阶 moments。因此 `mu_*=P_(q^N)nu_N`
不能由 Favard 正性自动推出。

若要补足 bridge，至少需要：law identification 或显式 measure map、归一化
保持、`x`-moment/monic-norm 保持，以及与 `P_lambda` 的 intertwining；在全矩
层可写成对每个 `N` 存在正 probability `nu_N`、`lambda=q^N`，满足

`m_k^*=sum_(r=0)^[k/2] binom(k,2r)(1-lambda)^r(2r-1)!!
 lambda^((k-2r)/2) m_(k-2r)(nu_N)`。

这个缺口一旦补上，degree-two conditional Hermite bound 给出
`h_2(mu_*)>=2(1-q^N)^2`、`m_3(mu_*)^2<=2q^N(2-q^N)`，故 `N->infinity`
时 `m_3(mu_*)=0`。它只关闭具有深层正 OU 可除性的 canonical skew 分支，
不自动关闭 ordinary eventual-zero diagonal、Gaussian rigidity 或 `P_3 K`
bridge。

### 56.1 第六级 exact recurrence

R59 沿 R57 一参数 canonical family

`a=m_3`, `t=a^2`, `alpha_0=0`, `alpha_1=a`, `alpha_2=-a`,
`alpha_n=0 (n>=3)`

继续到 degree-12 row。记

`p_4(t)=t^2-64t+16`,
`p_5(t)=253t^3-1278t^2+816t+160`,

`P_6(t)=532t^6-45655t^5+351508t^4-625952t^3
         +110432t^2+83200t-7680`。

本机以 monic recurrence 直接重算并校正浏览器纯文本分式方向，得到

`m_11=a(140t^2-913t-30)/(2-t)`,
`m_12=(2849t^3-19102t^2-15987t+20790)/(2-t)`,

`h_5=3p_5/[2(2-t)(1+t)]`,
`h_6=-6P_6/[(2-t)^2p_4]`。

因此项目约定 `beta_n=h_n/h_(n-1)` 给出正确的新式

`beta_6(t)=-4(1+t)P_6(t)/[(2-t)p_4(t)p_5(t)]`。

网页端给出的 `delta_5,delta_6,beta_6` 文字分式再次发生倒置；本机审计
以 `h_6/h_5` 和 `beta_n=(3/2)delta_n/delta_(n-1)` 校正。倒置不改变
`beta_6` 的 sign，但不能把网页显示式当作已核验公式。

在 `0<t<r`, `r=32-12sqrt(7)` 上，`2-t,p_4,p_5` 都正。并且 `P_6'` 在
`[0,r]` 严格正（用 `r<13/50`、保留正的 `t^3,t^5`、并对负的 `t^2,t^4`
作上界即可得到正的显式下界）。精确值

`P_6(1/20)=-26559850671/8000000<0`,
`P_6(1/10)=576531391/500000>0`

给出唯一 `tau_6 in (1/20,1/10)` 满足 `P_6(tau_6)=0`，从而

`beta_2,...,beta_6>0  <=> 0<t<tau_6`

对这条 canonical finite-stage family 成立。此前五级窗口被严格压缩；但
`beta_7,beta_8,...` 仍未定，故没有 genuine full-exact counterexample 或
D.1 的无条件证明。

本机新增 `flat_shadow_canonical_beta6_r59/audit_r59.py` 与 README，审计
degree-12 same-factor relation、`h_6/h_5` 方向、`P_6` 单调性和精确变号
区间；没有使用 determinant、optimizer、SDP、sweep、relaxed measure-LP 或
remote computation。R59 的最小可报告结果是 canonical nonzero-skew
positivity window 在第六级收缩为显式唯一根以前的区间。下一唯一 lemma 是
`beta_7` positivity-interval contraction：在 `0<t<tau_6` 上找
`tau_7<tau_6` 或证明 `beta_7` 全程正。

## 57. R60：degree-14 不再收缩 canonical window（2026-09-06）

R60 继续唯一的 `beta_7` lemma。网页端的可靠结构结论是第二种情形：第七级
没有产生 `tau_7<tau_6`，而是在全部 `0<t<tau_6` 保持正。由于网页输出
再次把高阶 norm 分式和部分多项式写错，本机只采纳其目标与结构，所有具体式子
均按 degree-14 same-factor relation、`alpha_6=0` 及 monic recurrence 重新核验。

令 `p_4,p_5,P_6` 沿用 R59，并定义校正后的

`P_7(t)=2150400+19281920t-206264064t^2-424134656t^3
       +2523473440t^4-4074599496t^5+2790646820t^6
       -853051174t^7+100963863t^8-2264192t^9`。

`alpha_6=0` 给出

`m_13=3a(1145t^2-2284t-2280)/(2-t)`，

degree-14 exact row（结合 R59 的 `m_12`）经本机 degree-14 Fock relation
核对给出

`m_14=(839909t^3-1338415t^2-187437t+270270)/(2-t)`。

直接按正确方向 `beta_7=h_7/h_6` 的因子结构为

`h_6=-6P_6/[(2-t)^2p_4]`,
`h_7=3P_7/[(2-t)^3p_5]`,

`beta_7=-p_4P_7/[2(2-t)p_5P_6]`。

在 `0<t<tau_6<1/10` 上，R59 已给 `p_4,p_5,2-t>0,P_6<0`。为避免新的
大规模扫描，本机把 `P_7(u/10)` 写成 `[0,1]` 上的 degree-9 Bernstein
形式；十个 Bernstein 系数全部为正，因此 `P_7>0`，从而

`beta_7(t)>0` 对所有 `0<t<tau_6` 成立。

本机新增 `flat_shadow_canonical_beta7_r60/audit_r60.py` 与 README。审计以
degree-14 relation 的符号核对、exact rational family points 的
`h_7/h_6` 因子核验，以及 Bernstein 正性证书组成；高阶展开不再强行做耗时的
全局 factorization。R60 的可靠结论是：前七级均正的非零 skew 开区间存在，
但尚未说明 `beta_8` 以后，也不能升级为 genuine full-exact counterexample。

全局影响不变但更具体：D.1 若成立，canonical finite exit 首次进一步出现的
层级只能是 `n>=8`；eventual skew annihilation 不能靠前七级消元；Gaussian
rigidity 与 `P_3 K` bridge 仍独立 OPEN。下一唯一 lemma 改为 corrected
degree-16 `beta_8` sign lemma，继续区分 OU law 与 auxiliary Jacobi law，
禁止 determinant、optimizer、SDP、sweep、relaxed measure-LP 和 remote
computation。

## 59. R62：corrected degree-18 再次收缩 canonical window（2026-09-06）

R62 在校正后的 `0<t<tau_8` 上继续同一个 canonical family。这里仍然取
`a=m_3`、`t=a^2`、`alpha_1=a`、`alpha_2=-a`、`alpha_n=0 (n>=3)`，并且
严格使用项目约定 `beta_n=h_n/h_(n-1)`。网页端高阶分式存在反复倒置风险，
故本节只保留本机 exact recurrence 与 Bernstein 证书通过的表达式。

### 59.1 degree-18 exact rows

`alpha_8=0` 给出

`m_17=2a(5799325t^5-17049855t^4+3925920t^3+13603108t^2+
       3127296t-4435200)/(2-t)^3`。

degree-18 same-factor row `G_9=0` 的 reduced Fock relation 为

`b_18=(42240 sqrt(221)b_11b_7+30030 sqrt(238)b_13b_5+
       37180 sqrt(51)b_15b_3+244 sqrt(255255)b_3b_6b_9+
       120 sqrt(102102)b_5b_6b_7-280 sqrt(2431)b_6^3+
       3139 sqrt(12155)b_9^2)/24310`。

代回 Hermite moments 得

`m_18=(2948477t^6+1914655626t^5-11976383460t^4+24318362039t^3-
       15915490026t^2-432574380t+275675400)/(2-t)^3`。

本机在 `a=0,1/10,1/5` 三个 exact rational points 上同时核验 odd row、
degree-18 relation 与 `m_18`，没有把浏览器显示的未核验大式直接写入记录。

### 59.2 norm factor and sign polynomial

令

`Q_9(t)=3165494381056t^16+30325981442862714t^15-374454388483999229t^14
       +1980117276228617592t^13-5948703596679826184t^12
       +11525374336730958528t^11-15614218470552621360t^10
       +14603518104424932288t^9-6281195243972625024t^8
       -4538141298321788672t^7+7271911315244371968t^6
       -2538108384598913024t^5-76181770793263104t^4
       -23999642267549696t^3-2927350178119680t^2
       +45013480243200t+4161798144000`。

本机 recurrence 与 exact rational norm evaluation 给出

`h_8=-3P_8/[2(2-t)^3P_6]`,
`h_9=3Q_9/[(2-t)^4P_7]`,

从而正确的第九级系数是

`beta_9=h_9/h_8=-2P_6Q_9/[(2-t)P_7P_8]`。

Gaussian sanity check 为 `h_8(0)=40320`、`h_9(0)=362880`、
`beta_9(0)=9`。这同时确认了 norm ratio 的方向。

### 59.3 exact cutoff comparison

`Q_9` 在 `[0,1/100]` 的 degree-16 Bernstein coefficients 全部严格正，
所以 `Q_9>0`；`Q_9'` 在 `[1/100,1/25]` 的 degree-15 Bernstein
coefficients 全部严格负，所以 `Q_9` 在该区间严格递减。精确端点符号为

`Q_9(1/100)>0`, `Q_9(19/500)<0`, `Q_9(1/25)<0`。

因此存在唯一

`tau_9 in (1/100,19/500)`, `Q_9(tau_9)=0`。

R61 的 `P_8'<0` on `[0,1/25]` 证书与
`P_8(19/500)>0>P_8(1/25)` 又给出 `tau_8>19/500`，故
`tau_9<tau_8`。数值 `tau_9≈0.0379679226232613` 仅作定位，正式结论
是上述有理区间与严格 Bernstein 证书。

在 `0<t<tau_8` 上，前轮已有 `P_6<0`、`P_7>0`、`P_8>0`，于是

`beta_9>0  <=>  0<t<tau_9`,
`beta_9<0  for tau_9<t<tau_8`。

这给出目前可靠的局部里程碑：`tau_6>tau_8>tau_9>0`，且 beta7 在
`tau_8` 之前不产生额外截断。

### 59.4 全局解释与唯一下一步

R62 不是 full-exact counterexample，也没有证明任意固定非零 skew 最终
退出；它只说明 canonical branch 的 even-stage contraction 至少再次发生。
若要从“有限阶段可报道结果”走向 D.1，下一条真正需要的是 structural
all-even-stage lemma，例如证明 `tau_(2k+2)<tau_(2k)` 并控制其极限，或
给出不依赖逐阶大多项式的统一 tail sign/curvature mechanism。

因此 D.1、infinite positive viability、eventual skew annihilation、Gaussian
rigidity 与 `P_3 K` bridge 仍保持彼此独立的 OPEN 状态；R62 没有把
Favard 辅助谱测度偷换成原始 OU law。新增本机审计为
`flat_shadow_canonical_beta9_r62/audit_r62.py`，没有使用 determinant、
optimizer、SDP、sweep、relaxed measure-LP 或 remote computation。

### 59.5 网页端复核注记

R62 网页端最终正确识别了 `Q_9` 的新零点以及严格关系
`tau_9<tau_8`，但其显示的 `h_8`、`h_9` 闭式各自取了倒数，因而显示的
`beta_9` 分式也是项目约定 `h_9/h_8` 的倒数。这与它随后写出的
`h_8(0)=40320`、`h_9(0)=362880`、`beta_9(0)=9` 彼此矛盾。故本机 exact
audit 的 norm evaluation、Gaussian sanity 与有理点核验优先；网页端本轮
只保留其符号结构和 cutoff 结论，不采纳倒置的显示公式。

## 60. R63：degree-20 再次产生严格 cutoff（2026-09-06）

R63 继续同一 canonical family，并把网页端提出的 `beta_10` 目标先在本机
按 exact recurrence 重建。关键修正是：此前的 `m_20` 只有探索性截断来源，
不能直接使用；本轮从 degree-20 same-factor cubic row 对 `m_20` 做线性精确
求解，并在 `a=0,1/10,1/5` 三个有理点通过整行核验。

令 `A_10` 为 `flat_shadow_canonical_beta10_r63/README.md` 中记录的 exact
degree-20 polynomial，则本机得到

`h_10=A_10/[(t-2)^5P_8]`,

`beta_10=h_10/h_9=A_10P_7/[3(t-2)P_8Q_9]`。

Gaussian sanity 为 `m_20(0)=19!!`、`h_10(0)=10!`、`beta_10(0)=10`，并且
`beta_10'(0)=-1481/21`。这一次分式方向由 norm evaluation 和 Gaussian
值共同固定，不采纳网页端的未经核验高阶倒置式。

### 60.1 exact sign certificate

对 `A_10` 的 derivative，在 `[0,1/200]` 上的 Bernstein 系数全正；同时
`A_10(0)<0<A_10(1/200)`。将 `[1/200,19/500]` 分成五个固定有理子区间，
每段的 `A_10` Bernstein 系数全正；`(t-2)^5P_8` 在 `[0,19/500]` 的
Bernstein 系数全负。因此存在唯一

`tau_10 in (0,1/200)`, `A_10(tau_10)=0`。

R62 已给 `tau_9 in (1/100,19/500)` 且 `Q_9>0` 直到 `tau_9`；前轮还给出
`P_7,P_8>0`。故在整个既有窗口 `0<t<tau_9` 内，

`beta_10>0` 当且仅当 `0<t<tau_10`，

`beta_10<0` 对 `tau_10<t<tau_9` 成立。于是得到目前最强的 canonical
finite-stage chain：

`tau_6>tau_8>tau_9>tau_10>0`。

### 60.2 全局位置

R63 是一个可明确陈述的 finite-stage exact-positive obstruction：即使连续
前几级的 cubic/Favard 系数通过，degree 20 仍会把同一 canonical branch 切断。
它没有完成 D.1，也没有推出所有固定非零 skew 最终退出；Gaussian rigidity 与
`P_3 K` bridge 仍是独立 OPEN。下一步应从这四次 cutoff 的共同代数结构中抽取
uniform all-even-stage lemma，而不是继续无结构地堆叠大多项式。

新增本机审计为 `flat_shadow_canonical_beta10_r63/audit_r63.py`。

## 61. R64：从逐阶 cutoff 提炼 quadratic-response 结构（2026-09-06）

R64 不再继续计算 `beta_11` 的完整闭式，而是审计网页端提出的结构化压缩。
本节的全阶表述以“formal moment functional 满足 full same-factor hierarchy”为
条件；本机只把它核验到 degree 20，故不能把条件性全阶式误报成已经存在的
非 Gaussian full-exact tower。

### 61.1 finite-head Jacobi tangent

在 canonical head
`alpha_1=a`、`alpha_2=-a`、`alpha_n=0 (n>=3)`、`t=a^2` 下，已知
`beta_n(t)=n+O(a^2)`，于是 orthonormal Jacobi operator 的一阶变化只有有限
diagonal head：

`J_a=J_0+aD+O(a^2)`,

`D=|e_1><e_1|-|e_2><e_2|`。

令
`F_a(z)=L_a[exp(zX-z^2/2)]=1+aU(z)+a^2V(z)+O(a^3)`。Duhamel 公式与
Gaussian Jacobi kernel 给出

`U(z)=z^3 integral_0^1 s(1-s) exp(-s(1-s)z^2)
       (1-s(1-s)z^2/2) ds`。

故

`[a]L_a[H_(2m+1)]=(-1)^(m-1)m(m+1)!/2`。

这不是由 R59–R63 的有限模式猜出的经验式；它来自 finite-head perturbation。
本机 exact audit 对 `m=1,...,9`（Hermite degree `3,...,19`）全部通过。

### 61.2 full same-factor 的二阶 even convolution

取
`r_j(theta)=sqrt(2/3)cos(theta+2pi(j-1)/3)`，则 `sum_j r_j^2=1`。若 formal
full same-factor identity 为

`average_theta product_{j=1}^3 F_a(r_j z)=1`,

并定义
`A_(2n)=average sum_j r_j^(2n)=3*binomial(2n,n)/6^n`，
`C_(r,s)=average sum_{i<j}r_i^r r_j^s`，
则 `a^2 z^(2n)` 系数满足

`[a^2]L_a[H_(2n)]/(2n)!
 = -A_(2n)^(-1) sum_{r+s=2n, r,s odd, r,s>=3}
     u_r u_s C_(r,s)/(r!s!)`,

其中 `u_r=[a]L_a[H_r]`。`C_(r,s)` 是有限 root-of-unity exact sum。R64 本机
对 even degrees `4,...,20` 全部与 audited canonical moments 相符。

### 61.3 norm ratio 的统一局部曲率

写 `L_a=L_0+aL_1+a^2L_2+O(a^3)`，`pi_n=H_n+aq_n+O(a^2)`。一阶正交性给出

`q_n=-sum_{k<n}L_1[H_nH_k]H_k/k!`，

从而

`h_n=n!+K_n t+O(t^2)`,

`K_n=L_2[H_n^2]-sum_{k<n}L_1[H_nH_k]^2/k!`。

因此

`beta_n(t)=n+Lambda_n t+O(t^2)`,
`Lambda_n=beta_n'(0)=(K_n-nK_(n-1))/(n-1)!`。

本机 exact audit 核验到 `n=10`，并复现 R63 的 `Lambda_10=-1481/21`。

### 61.4 理论地位与剩余桥

R64 的正式地位是一个 conditional all-degree response lemma：finite skew head
唯一决定 odd tangent；full same-factor hierarchy 唯一决定 even quadratic
response；norm/beta 的 Gaussian-local slopes 由一个显式 finite quadratic form
决定。它比单列 `P_6,P_8,Q_9,A_10` 更接近可发表的机制性结果。

但 `Lambda_n<0` 只是在 Gaussian 点的局部方向，不能单独给出 cutoff，更不能
保证 cutoffs 全阶单调。离 D.1 的唯一桥仍是 uniform shrinking-cutoff certificate：
需要同时控制某个负 slope 的 `O(t^2)` remainder，或直接建立有限 `t` 的统一 tail
deficit，并且仍需另行处理原始 OU law 与 Favard 辅助谱测度的 bridge。

新增本机审计为 `flat_shadow_structural_response_r64/audit_r64.py`。

## 62. R65：quadratic-response 有限和与 cutoff 尺度校正（2026-09-06）

R65 将 R64 的 root-of-unity convolution 化为可直接审计的二项式有限和。对
`r+s=2n`、`r,s` 为奇数，令

`E_(r,s)=sum_p [0<=n-p<=s, 2p-r=0 mod 3] binom(r,p)binom(s,n-p)`。

则

`C_(r,s)=3(3E_(r,s)-binom(2n,n))/(2*6^n)`。

等价的 root-of-unity filter 与界
`-1/2<=C_(r,s)/A_(2n)<=1` 也随之成立。代入 R64 的 odd tangent，得到

`v_(2n)/(2n)! = -(1/(2 binom(2n,n)))
  sum_(r+s=2n, r,s odd>=3) (u_r/r!)(u_s/s!)
  (3E_(r,s)-binom(2n,n))`。

再用 Hermite product formula，`K_n` 与
`Lambda_n=beta_n'(0)=(K_n-nK_(n-1))/(n-1)!` 完全化为有限有理和。本机对
R63/R64 可用的 targeted stages exact 核验了 `Lambda_10=-1481/21`、
`Lambda_15=15335/858`、`Lambda_20=-42799/19019`、
`Lambda_30=1063856351/38818159380`，并核验 `Lambda_100>0`、
`Lambda_200>0`。因此不能把“偶数级局部斜率一直为负”当作结构定理；
eventual sign 与渐近尺度仍 OPEN。

### 62.1 local-slope cutoff lemma 的正确版本

网页端给出的局部 cutoff 引理在零点尺度上把分子分母倒置了。正确设定为

`beta_n(t)=n+Lambda_n t+R_n(t)`, `Lambda_n<0`,
`|R_n(t)|<=eta_n|Lambda_n|t`，其中 `0<=eta_n<1` 且 `0<=t<=rho_n`。

于是

`n-(1+eta_n)|Lambda_n|t <= beta_n(t)
 <= n-(1-eta_n)|Lambda_n|t`。

若
`T_n=n/((1-eta_n)|Lambda_n|)<=rho_n`，则连续性给出零点；第一正零点满足

`n/((1+eta_n)|Lambda_n|)<=tau_n
 <=n/((1-eta_n)|Lambda_n|)`。

所以要由局部斜率推出 `tau_n->0`，必要的尺度条件是
`|Lambda_n|/n->infinity`，还要有覆盖 `T_n` 的 uniform remainder radius；
若想控制整个 prior window，还需 no-reentry/导数符号。网页端原先写的
`|Lambda_n|/n` cutoff scale 已被本机审计排除。

R65 的实际结论是：局部 quadratic response 已可精确组合化，但它目前不能
单独解释 R59–R63 的 finite-`t` cutoff chain。下一步应转向 `K_n/n!` 的
Mehler generating function 或直接寻找 uniform finite-`t` tail deficit。

新增本机审计为 `flat_shadow_quadratic_response_r65/audit_r65.py`。

## 63. R66：Mehler 分解与 associated-Hermite 投影尾（2026-09-06）

R66 将 K(z)=sum kappa_n z^n 分成两个性质不同的部分：
K(z)=D(z)-P(z)，其中 D(z)=sum D_n z^n/n! 是 same-factor even
quadratic term，P(z)=sum P_n z^n/n! 且 P_n=||q_n||_gamma^2 是
lower-triangular projection norm。网页端公式已用本机 exact symbolic audit
复核；这里统一使用普通分式记法，避免浏览器堆叠分式的阅读歧义。

### 63.1 D-part 的闭合

Mehler kernel 的对角线给出 D(z)=L_2[M_z(x,x)]，Hermite product formula
给出精确二项式变换

D(z)=1/(1-z) sum_(m>=0) (v_(2m)/m!) (z/(1-z))^m。

令 B(w)=sum b_m w^(2m) 为 same-factor pair term。由
A_(2m)=3 binom(2m,m)/6^m 与 full same-factor hierarchy，
v_(2m)/m!=-(6^m m!/3)b_m，从而

D(z)=-1/(3z) integral_0^infinity exp(-(1-z)u/z)
       B(sqrt(6u)) du。

本机 exact coefficient checks 对 D 到 n=10、same-factor conversion 到
m=8 通过。利用 U(w)=w^3/6+O(w^5) 与
U(w)=-4/w^3+O(w^(-5))，角向 zero-neighborhood 分解给出
B(w)=O(w^(-4))（大 w）及 B(w)=O(w^6)（小 w），因此在相应
analytic convergence domain 内 D(1-) 有限，且误差为
O((1-z)log(1/(1-z)))。这排除了 D 部分在 z=1 的 pole；边界估计的
analytic hypotheses 与形式系数计算需继续区分。

### 63.2 projection part 的闭合

有限 head 的一阶 monic correction 满足

q_0=q_1=0、q_2=-H_1、q_3=-H_0、
q_(n+1)=xq_n-nq_(n-1)（n>=3），

并有 P_n=||q_n||_gamma^2。其 EGF Q(x,w) 由一个精确积分闭式给出；
将 R(xi,eta)=integral Q(x,xi)Q(x,eta)d gamma(x) 作角向对角提取，得到

H(y)=sum ||q_n||^2 y^n/(n!)^2，
P(z)=integral_0^infinity e^(-s) H(zs) ds
=sum ||q_n||^2 z^n/n!。

显式二重积分中的 Gaussian-shift polynomial 已由本机 symbolic audit 核验，
包括关键因子 st/4。因此 lower-triangular finite sum 已真正压缩为一个
associated-Hermite norm tail，而不是被误当成原始 OU law 或形式谱测度。

### 63.3 实际影响与唯一剩余目标

在 P_n>=0 且相应级数收敛的条件下，K(z) 在 z=1 的主奇性只能来自
P(z)；若 sum ||q_n||^2/n!<infinity，则 K(1-) 有限，若发散则
K(z)=-P(z)+O(1)。因此当前 Gaussian-local quadratic response 的唯一
未闭合项是

p_n=||q_n||_gamma^2/n!

的严格大阶行为，或等价的 P(z) 在 z=1 的 leading singularity。R65 的
有限级符号检查不能替代这一 asymptotic proof；eventual sign、n^(-1/2)
尺度、finite-t cutoff、backward divisibility 与 D.1 仍 OPEN。

新增本机审计为 `flat_shadow_mehler_projection_r66/audit_r66.py`。

## 64. R67：associated-Hermite 投影尾的严格平方根律（2026-09-07）

R67 继续沿用 R66 的 finite-head tangent，固定
q_0=q_1=0、q_2=-H_1、q_3=-H_0、q_(n+1)=xq_n-nq_(n-1)。
引入 associated-Hermite 多项式
A_(-1)^(c)=0、A_0^(c)=1、A_(m+1)^(c)=xA_m^(c)-(m+c)A_(m-1)^(c)，
则对 n>=3、m=n-3，

q_n=-A_m^(3)+3xA_(m-1)^(4)。

其普通 Hermite 展开为

A_m^(c)=sum_(j=0)^(floor(m/2)) (-1)^j binom(m-j,j)(c)_j H_(m-2j)，

合并后得到

q_n=sum_j c_(m,j)H_(m-2j)，
c_(m,j)=(-1)^(j+1)((j+1)(j+2)(j^2+5j-2m)/2)((m-j-1)!/(m-2j)!)。

因此投影范数拥有全正有限和

p_n=||q_n||_gamma^2/n!
=1/(4(m+3)!) sum_j (j+1)^2(j+2)^2(j^2+5j-2m)
^2*((m-j-1)!^2/(m-2j)!)。

将 j=y sqrt(m) 后，精确 factorial ratio 的主项为
rho_(m,j)=m^5(m-j-1)!^2/((m-2j)!(m+3)!) -> exp(-y^2)；
对数不等式与 entropy 区域给出可积 Gaussian majorant。于是得到严格

p_n ~ (33 sqrt(pi)/128)n^(-1/2)。

等价地，投影生成函数在径向 z->1- 满足

P(z)=sum p_n z^n ~ (33 pi/128)(1-z)^(-1/2)，

而 R66 的 D(z) 仍只有有限 Abel 边界，所以
K(z)=D(z)-P(z) ~ -(33 pi/128)(1-z)^(-1/2)，均在现有 analytic
boundary hypotheses 下理解。本机 exact audit 核验 associated 展开、正有限和、
rho 乘积、Riemann 项归一化与常数积分；没有把 finite samples 当作证明。

这给出了一个可独立报告的 Gaussian-local projection 结果，但尚不能推出完整
kappa_n 或 Lambda_n 的 coefficientwise 渐近：缺口是 D_n/n! 及其 first
difference 的 transfer bound。因此 eventual sign、full Lambda_n asymptotic、
shrinking cutoff、backward divisibility 与 D.1 仍 OPEN。

新增本机审计为 `flat_shadow_associated_hermite_r67/audit_r67.py`。

## 65. R68：D-part 的系数级 transfer（2026-09-07）

R68 在 R64–R67 的 conditional full same-factor hierarchy 下，把 R66 的
Laplace 表示进一步展开为参数积分的有理核。记

`D(z)=sum d_n z^n`、`d_n=D_n/n!`，并令
`alpha=s(1-s)r_i^2`、`beta=t(1-t)r_j^2`、`c=alpha+beta`、
`lambda=1-6c`。由于 `0<=c<=1/4`，有 `-1/2<=lambda<=1`，从而

`D(z)=average sum_(i<j) integral q_s q_t r_i^3 r_j^3`
`[-432 z^3/(1-lambda z)^4 + 5184 c z^4/(1-lambda z)^5`
` -77760 alpha beta z^5/(1-lambda z)^6] ds dt`。

这给出 slit domain
`C\([1,infinity) union (-infinity,-2])` 上的参数解析延拓，并给出

`d_n=average sum_(i<j) integral q_s q_t r_i^3 r_j^3`
`[-432 binom(n,3)lambda^(n-3) + 5184 c binom(n,4)lambda^(n-4)`
` -77760 alpha beta binom(n,5)lambda^(n-5)] ds dt`。

网页端进一步利用 `r_0+r_1+r_2=0` 在三个 simple-zero 邻域的 leading
pair cancellation，把 R66 的 `B(w)=O(w^(-4))` 强化为 sectorial
`B(w)=O(|w|^(-5))`。若相应的 complex-sector contour rotation 假设成立，
则 `f(u)=B(sqrt(6u))` 有两个绝对矩，Laplace 余项为
`O(|1-z|^(3/2))`，Cauchy–Hankel transfer 给出

`d_n=O(n^(-5/2))`，
`n(d_n-d_(n-1))=O(n^(-3/2))`。

本机 `flat_shadow_dpart_transfer_r68/audit_r68.py` 精确核验了 u 次幂积分的
1296、15552、233280 常数、z-有理核常数、系数提取、slit 域端点、D3 根的
抵消几何、两矩余项的 `3/2` 标度以及 transfer 指数。需要保留的边界是：
有限 Abel 极限本身不能推出系数界；R68 的 full Delta-domain 结论依赖其明确
写出的复扇区增长与 contour-rotation 条件，若具体 formal model 尚未逐项验证，
则 `O(n^(-5/2))` 应按该条件性理解。

在这些条件下，R67 的投影平方根律终于得到 coefficient-level 合并：

`kappa_n=d_n-p_n ~ -(33 sqrt(pi)/128)n^(-1/2)`，
但
`Lambda_n=n(p_(n-1)-p_n)+O(n^(-3/2))`。

因此 full `Lambda_n` 的 eventual sign 仍 OPEN；唯一剩余目标收缩为证明
`p_(n-1)-p_n ~ (33 sqrt(pi)/256)n^(-3/2)`。这会关闭 Gaussian-local
quadratic-response 的符号问题，但仍不会单独证明 D.1；它只会排除由大 n
Gaussian-local negative slope 驱动 shrinking cutoff 的机制。

新增本机审计为 `flat_shadow_dpart_transfer_r68/audit_r68.py`。

## 66. R69：projection 一阶差分渐近与 Gaussian-local 符号闭合（2026-09-07）

R69 直接比较 R67 正有限和的相邻阶，而不是对
`p_n~C n^(-1/2)` 做形式差分。令 `m=n-3`，写

`p_(m+3)=sum_j T_(m,j)`，
`T_(m,j)=((j+1)^2(j+2)^2(j^2+5j-2m)^2)/(4(m+3)!)`
` *((m-j-1)!^2/(m-2j)!)`。

在共同范围内令
`A_(m,j)=j^2+5j-2m` 与
`L_(m,j)=(m+3)(m-2j)/(m-j-1)^2`。精确相邻阶约去阶乘后，

`T_(m-1,j)-T_(m,j)`
`=base_(m,j)[L_(m,j)(A_(m,j)+2)^2-A_(m,j)^2]`，

其中 `base_(m,j)` 是 `T_(m,j)` 去掉 `A_(m,j)^2` 的部分。引入 R67 的
`rho_(m,j)` 并令 `G_(m,j)=m^2(T_(m-1,j)-T_(m,j))`，得到

`G_(m,j)=(1/4)((j+1)^2(j+2)^2/m^2)rho_(m,j)B_(m,j)`，

`B_(m,j)=m(L_(m,j)-1)(A_(m,j)/m)^2`
` +4L_(m,j)(A_(m,j)/m)+4L_(m,j)/m`，

以及精确恒等式
`L_(m,j)-1=(5m-j^2-8j-1)/(m-j-1)^2`。

在 `j=y sqrt(m)` 的共同尺度上，R67 的 `rho_(m,j)->exp(-y^2)`，故

`G_(m,j)->(1/4)(-y^10+9y^8-20y^6+12y^4)exp(-y^2)`。

R67 的全区间 Gaussian majorant 与上述精确恒等式给出可积支配
`|G_(m,j)|<=C(1+y_j^10)exp(-c y_j^2)`。floor 边界若出现额外项，
`T_(m,m/2)=O(m^4 2^(-m))`，故不贡献极限。于是

`m^(3/2)(p_(m+2)-p_(m+3)) -> integral_0^infinity G(y)dy`
`=33 sqrt(pi)/256`，换回 `n=m+3` 得到严格

`p_(n-1)-p_n ~ (33 sqrt(pi)/256)n^(-3/2)`。

本机 `flat_shadow_projection_difference_r69/audit_r69.py` 精确核验相邻项
恒等式、差分缩放、局部极限多项式、floor 端点中心二项式化、积分常数和换标。
R67 的 factorial-ratio 全区间 majorant 作为解析输入保留，不以有限数值取代。

结合 R68 的 conditional D-part transfer
`d_n=O(n^(-5/2))`、`n(d_n-d_(n-1))=O(n^(-3/2))`，在
R64–R68 full same-factor hierarchy 下终于得到

`Lambda_n=n(kappa_n-kappa_(n-1))`
`~(33 sqrt(pi)/256)n^(-1/2)>0`。

因此 Gaussian-local quadratic-response 的 eventual sign 在该条件框架下闭合，
并且 `|Lambda_n|/n->0`，与 R65 局部 shrinking-cutoff 所需的
`|Lambda_n|/n->infinity` 相反。这个里程碑排除了 large-n Gaussian-local
negative-slope 机制，但不证明 D.1；若 R59–R63 的 shrinking finite-stage
cutoffs 继续存在，剩余机制必须是 finite-t nonlinear/boundary-layer effect。

新增本机审计为 `flat_shadow_projection_difference_r69/audit_r69.py`。

## 67. R70：finite-t nonlinear boundary-layer 必要性（2026-09-07）

R70 将问题从 Gaussian-local slope 推进到有限 `t` 的非线性尾部。对条件性
formal branch 记

`beta_hat_n(t)=beta_n(t)/n=1+ell_n t+N_n(t)`，其中
`ell_n=Lambda_n/n`、`N_n(t)=sum_(r>=2) b_(n,r)t^r`。

若在解析半径内存在零 `tau_n>0`，则有精确恒等式

`N_n(tau_n)=-1-ell_n tau_n`，

从而 `sum_(r>=2)|b_(n,r)|tau_n^r >= 1+ell_n tau_n`。特别地，若
`tau_n->0`，非线性 Taylor 尾部必须在 shrinking scale 上承担 order-one
负响应，而不可能由有限阶 slope 单独造成。

R70 还给出一个只用二阶余项的必要条件。令
`M_n(s)=sup_(0<=u<=s)(-beta_hat_n''(u))_+`，则

`beta_hat_n(t)>=1+ell_n t-(1/2)M_n(s)t^2`，

并且任何零 `tau_n` 都必须满足
`tau_n^2 M_n(tau_n)>=2(1+ell_n tau_n)`。因此 shrinking zero 要求
`M_n(tau_n)>=(2+o(1))/tau_n^2`，未归一化时相应为
`sup(-beta_n'')_+ >=(2+o(1))n/tau_n^2`。

解析半径版本也排除了一个常见误读：若 `beta_hat_n` 在 `|t|<R_n` 内解析，
且圆盘上统一有界，则 Cauchy 估计给出
`sum_(r>=2)|b_(n,r)|s_n^r <= M(s_n/R_n)^2/(1-s_n/R_n)`。
若 `s_n/R_n->0`，则 `beta_hat_n=1+o(1)`，所以 shrinking zero 只能发生在
`tau_n` 不再远小于解析半径，或该统一有界性失效。

这是一条 scale-free 的 necessary/no-go lemma，而非 D.1 的证明，也没有构造
positive exact backward tower；所有结论仍处于 R64–R69 的 conditional
same-factor/Jacobi formal hierarchy。下一步唯一应攻克的是全阶 nonlinear-tail
scaling：构造 `N_n(s_n x)` 的非平凡极限并得到负值，或证明其在某尺度上统一为
`o(1)`（从而排除 reversal）。

新增本机审计为 `flat_shadow_boundary_layer_r70/audit_r70.py`。

## 68. R71：Hermite–Gram all-order boundary-layer barrier（2026-09-07）

网页端本轮明确报告连接器未能读取 R70 两处本机记录，因此本节只把其新推导
中可独立核验的部分纳入，并以本机 R70/R64 记录校正浏览器纯文本中的分式方向。

令 `e_k=H_k/sqrt(k!)`、`V_n=span(e_0,...,e_n)`，并在 conditional
full same-factor canonical formal branch 下定义有限 Hermite Gram 块

`G_n(a)=(L_a[e_j e_k])_(0<=j,k<=n)`，`t=a^2`。

Gaussian 点为 `G_n(0)=I`。写

`G_n(a)=I+a A_n+mathcal R_n(a)`，
`(A_n)_(j,k)=L_1[e_j e_k]`。

R64 的一阶 tangent transform 为
`U(z)=z^3 integral_0^1 q exp(-q z^2)(1-q z^2/2)ds`，其中 `q=s(1-s)`。
用 Gaussian Hermite transform `T` 和 `R=x-partial_x`，其一阶 functional 有
显式代表

`g_1(x)=integral_0^1(qR^3-q^2R^5/2)psi_q(x)ds`，
`psi_q=(1-2q)^(-1/2)exp(-q x^2/(1-2q))`。

因为 `T psi_q=exp(-qz^2)`、`T(Rf)=zT(f)`，并利用 `q=s(1-s)` 的两个端点，
可得 `g_1 in L^infinity(gamma)`。故

`A_n=P_n M_(g_1)P_n`，`sup_n ||A_n||_op<=||g_1||_infinity=:M_*<infinity`。

这是比 scalar `Lambda_n` 更强的 Gaussian 一阶统一界。

再令 `gamma_n(a)=h_n(a)/n!`。规范化 Hermite 块的 Schur complement 给出
`gamma_n`，故

`beta_n(t)/n=gamma_n(a)/gamma_(n-1)(a)`。

若前级 norm ratios 为正且 `beta_n(tau_n)=0`，则 lower block 可逆，Schur
complement 的 kernel vector 说明 `G_n(sqrt(tau_n))` 奇异。于是

`||G_n(sqrt(tau_n))-I||_op>=1`。

而 `sqrt(tau_n)A_n` 在 `tau_n->0` 时一致趋于零，所以任何 shrinking exit
必须满足

`||mathcal R_n(sqrt(tau_n))||_op>=1-o(1)`。

换言之，趋零退出不可能由 Gaussian 一阶 tangent 累积产生；二阶及以上的
same-factor/Jacobi Hermite tail 必须在 Gram operator norm 中造成 order-one
变形。若某点满足 `||G_n(a)-I||_op<1`，则所有 leading blocks 的 Schur
complements 都为正，从而得到一个 exact finite-stage no-reversal certificate。

该障碍还能化为全阶 Hermite moment tail。令
`eta_m(a)=L_a[e_m]`、
`r_m(a)=eta_m(a)-delta_(m,0)-aL_1[e_m]`，则 Hermite product formula 给出

`mathcal R_n(a)=sum_(m=0)^(2n)r_m(a)T_(m,n)`，
`(T_(m,n))_(j,k)=<e_j e_k,e_m>_gamma`。

Hölder `(4,2,4)` 与 Gaussian hypercontractivity 给出
`||T_(m,n)||_op<=3^((n+m)/2)`，因此

`||mathcal R_n(a)||_op<=mathcal M_n(a)`，
`mathcal M_n(a)=3^(n/2)sum_(m=0)^(2n)3^(m/2)|r_m(a)|`。

这提供了一个真正的 conditional all-order reduction：若能在显式 `a_n->0`
上证明 `sup_(|a|<=a_n)mathcal M_n(a)->0`（或统一小于 `1-delta`），便在
原变量 `0<=t<=a_n^2` 得到 no-reversal；但 R71 本身还没有证明这个 source
majorant。

同一轮还校正并记录了 angular solver 的确切尺度。对
`r_j=sqrt(2/3)cos(theta+2pi j/3)`，

`A(z^(2k))=A_(2k)z^(2k)`，
`A_(2k)=3 binom(2k,k)/6^k`，
`A_(2k+2)/A_(2k)=(2k+1)/(3(k+1))<1`。

故 degree `<=2n` 的 coefficient-`ell^1` inverse norm 为 `A_(2n)^(-1)`，且
`A_(2n)^(-1)~sqrt(pi n)/3*(3/2)^n`。这是 solver 的潜在指数放大器，不能
单独推出 cutoff 或其尺度。

R71 仍未证明 (A) 负 profile、(B) 无附加假设的显式 no-reversal scale、D.1、
positive backward tower 或 backward OU divisibility。下一条唯一目标是从
same-factor nonlinear source recursion 控制 `mathcal M_n(a)`，或在该潜在放大
尺度上建立非平凡 operator profile。

新增本机审计为 `flat_shadow_gram_barrier_r71/audit_r71.py`。

## 69. R72：analytic Wiener 范数下的 angular tame 与 conditional source closure（2026-09-07）

R72 在 R71 的 Gram barrier 上继续分离 even angular solver 与 canonical odd
solver。网页端本轮明确报告连接器仍不可读 R71 本机文件，因此本节只记录其
新推导中经本机校正和审计的部分。

令 `q=sqrt(2/3)`，`e_m=H_m/sqrt(m!)`，并写

`F_a(z)=sum_(m>=0)L_a[e_m] z^m/sqrt(m!)=1+f_a(z)`。

full same-factor identity 的 even 部分给出精确 coefficientwise 方程

`f_e=-A_e^(-1)[Q(f,f)+C(f,f,f)]`，

其中 `A(z^(2k))=A_(2k)z^(2k)`、`A(z^(2k+1))=0`，且
`A_(2k)=3 binom(2k,k)/6^k`。在截断 analytic Wiener 范数
`||g||_R=sum_m|g_m|R^m` 下，`|r_j|<=q` 给出

`||Q(f,f)||_R<=3||f||_(qR)^2`，
`||C(f,f,f)||_R<=||f||_(qR)^3`。

Wallis 下界
`binom(2k,k)>=4^k/(2sqrt(k))` 导致
`A_(2k)>=3q^(2k)/(2sqrt(k))`。因此对任意固定 `0<theta<1`，

`||A_e^(-1)g||_(theta qR)<=C_A(theta)||g||_R`，
`C_A(theta)=(2/3)sup_(k>=1)sqrt(k)theta^(2k)<infinity`。

特别 `C_A(1/2)=1/6`，故

`||f_e||_(qR/2)<=1/6[3||f||_(qR)^2+||f||_(qR)^3]`。

这严格说明：在付出固定 analytic-radius loss 后，angular inverse 没有随 `n`
增长的 operator norm；系数级 `A_(2n)^(-1)~sqrt(pi n)(3/2)^n/3` 的指数增长
会被 `r_j` 的半径缩放抵消，不能单独解释 nonlinear remainder 的 order-one
增长。

再写 `f_o=aU+o`、`e=f_e`，并把 canonical odd remainder 记为
`o=O_n(a,e)`。R72 暴露出的唯一未审计输入是如下 tame estimate：取
`rho_n=4sqrt(n)`、`sigma_n=8sqrt(n)`，在 `||e||_(rho_n)<=1` 的 connected
branch 上假设

`||O_n(a,e)||_(sigma_n)<=Omega_n(|a|^3+|a| ||e||_(rho_n))`。

这是 `alpha_k=0 (k>=3)` 的 triangular odd solver 的全阶 Banach 稳定性；当前
没有 `Omega_n` 的可审计 `n` 依赖，也没有把该假设误报成定理。

在该假设下，令 `U_n=||U||_(sigma_n)`，并使用 R64 tangent 的粗界

`U_n<=bar U_n=(256/3)n^(3/2)(1+8n)e^(16n)`。

若 `U_n>1` 且
`|a|bar U_n<=4^(-(n+1))`、`|a|<=1/(4Omega_n)`，even source bootstrap 给出

`||e||_(rho_n)<=3|a|^2U_n^2`，
`||o||_(sigma_n)<=|a|^2U_n^2`，
`||e+o||_(rho_n)<=4|a|^2U_n^2`。

若 `w=e+o=sum_(m<=2n)r_m(a)z^m/sqrt(m!)`，则 R71 的 Gram majorant 满足

`mathfrak R_n(a):=3^(n/2)sum_(m<=2n)3^(m/2)|r_m(a)|`
`<=4C_B3^(n/2)|a|^2U_n^2`，
`C_B=1/(1-sqrt(6)/4)`。

因此定义条件性尺度

`a_n#=min{1/n,1/(4M_*),1/(4^(n+1)bar U_n),1/(4Omega_n),`
`1/(2bar U_n sqrt(n C_B 3^(n/2)))}`。

在 odd tame estimate 及其适用域成立时，对 `|a|<=a_n#` 有
`mathfrak R_n(a)<=1/n` 且
`||G_n(a)-I||_op<=1/4+1/n<1`（充分大 `n`）。于是原变量的区间
`0<=t<=(a_n#)^2` 上所有 `beta_k(t)>0 (k<=n)`。这是一个真正的 conditional
all-order no-reversal window，但它不是无条件结果，因为 `Omega_n` 与 odd
solver 的 analytic domain 仍未控制。

所以 R72 的实质性推进是：even angular recursion 已在合适 analytic norm 中
tame；任何 order-one boundary profile 必须来自 odd-solver instability、source
累积或 analytic-radius collapse，而非 angular inverse 的裸系数放大。D.1、
positive backward tower 与 backward OU divisibility 仍 OPEN。下一条唯一目标是
直接证明 canonical odd-solver 的上述 Banach tame estimate，并给出 `Omega_n`
的明确增长率；在此之前不再增加 degree 或计算新的 Gaussian-point 导数。

新增本机审计为 `flat_shadow_odd_solver_majorant_r72/audit_r72.py`。

## 70. R73：explicit canonical odd-solver majorant（2026-09-07）

R73 在 R72 的唯一未量化缺口上继续推进。网页端本轮仍报告连接器无法读取
本机 R72 记录，因此本节只采纳其原始 DOM 数学源，并由本机脚本逐项核验分式
方向与常数。网页纯文本曾把若干分数显示反向；校正后的关键数值是

`rho_n=4sqrt(n)`、`sigma_n=8sqrt(n)`，
`g_m=L[e_m]/sqrt(m!)`，`e_m=H_m/sqrt(m!)`，以及
`d_k=sqrt((2k+1)!)/k!`。

### Exact triangular odd recursion

令 `eta_m=L[e_m]`，`phi_k=pi_k/sqrt(k!)=e_k+sum_(j<k)v_(k,j)e_j`，并记

`G_(k-1)=(L[e_i e_j])_(i,j<k)`、
`g_k=(L[e_k e_j])_(j<k)`。

块正交方程给出精确的 `v_k=-G_(k-1)^(-1)g_k`。canonical diagonal
`alpha_1=a`、`alpha_2=-a`、`alpha_k=0 (k>=3)` 与
`L[x phi_k^2]=alpha_k L[phi_k^2]` 结合

`x phi_k^2=d_k e_(2k+1)+sum_(m<=2k)c_(k,m)e_m`

给出唯一的新 odd moment

`eta_(2k+1)=k!/sqrt((2k+1)!)*[alpha_k gamma_k-
sum_(m<=2k)c_(k,m)eta_m]`，其中 `gamma_k=L[phi_k^2]`。

这是一条真正的 exact triangular source recursion：第 `k` 步未知只出现在
`eta_(2k+1)`，source 只到 `2k`，并保留了 factorial inverse；even identity
并未被用来解 odd coefficient。

### Conditional analytic majorant

取 `V_n=span(e_0,...,e_n)`、`T_(m,n)=P_(V_n)M_(e_m)P_(V_n)`。creation /
annihilation normal ordering 给出

`||T_(m,n)||_op<=2^m(n+m)^(m/2)/sqrt(m!)`。

所以对 `3<=m<=2n`、`n>=3`，

`sqrt(m!)/rho_n^m * ||T_(m,n)||
 <=(1/2 sqrt(1+m/n))^m<=27/64`。

若 perturbation 没有 degree 1、2 项，则
`||G_n-I||_op <=(27/64)||f||_(rho_n)`。在网页端给出的复域
`||e||_(rho_n)<=17/16`、`||Y_n||_(sigma_n)<=1` 上，odd 起始 degree 为 3，
故 `||Y_n||_(rho_n)<=1/8`、`||f||_(rho_n)<=19/16`，从而

`||G_n-I||_op<=513/1024<1`，`||G_k^(-1)||<1024/511<2.01`。

在这一 Gram-domain/source estimate 作为解析输入时，粗 source 权重由
`32*7^n*k!*sigma_n^(2k+1)/(2k+1)!` 控制，并可统一压到

`B_n=512 n(448n)^n`。

若 `S_k` 是累计的 sigma-weighted odd coordinates，则

`S_k<=(1+B_n)S_(k-1)+B_n|a|`，
`S_n<=L_n|a|`，`L_n=(1+B_n)^n`。

取 `r_n=1/(4L_n)`，再用 `Y_n(-a,e)=-Y_n(a,e)` 和 Cauchy 估计，得到

`||O_n(a,e)||_(sigma_n)<=Omega_n(|a|^3+|a| ||e||_(rho_n))`,
`Omega_n=22L_n^3`，

以及显式增长

`Omega_n<=22(1024n)^(3n)(448n)^(3n^2)=exp(O(n^2 log n))`。

因此 R72 的 odd tame hypothesis 获得了一个显式但很粗的 conditional bound。
配合 R72 even bootstrap，令

`a_n#=min{r_n/2, 1/(20*4^n U_n),
sqrt(U_n/[2Omega_n(1+10U_n^2)])}`，
`t_n#=(a_n#)^2`，

可得到 `||G_n-I||<1`、`gamma_k>0`、`beta_k(t)>0 (k<=n)` 对
`0<=t<=t_n#` 成立。这里 `U_n=||U^(n)||_(sigma_n)`。

这关闭的是 R72 的“显式 odd majorant”缺口，不是 D.1。该窗口仍极其保守，
不能与 natural angular cutoff 做有意义的尺度比较；也没有构造 positive
infinite exact tower 或 backward OU divisibility。R73 本机审计为
`flat_shadow_odd_solver_bound_r73/audit_r73.py`。下一轮只推进
degree-local odd Green-function sharpening：保留每一级
`k!/sqrt((2k+1)!)`，争取把 `exp(O(n^2 log n))` 降到 `e^(O(n log n))` 或
`C^n n^p`。

## 71. R74：degree-local odd Green kernel 与 exponential conditional tame（2026-09-07）

R74 继续保留 R73 exact triangular recursion 的 factorial transfer，而不再把
每一级 source 都压到同一个 `B_n`。网页端本轮仍报告连接器不可读 R72/R73
本机记录，因此本节只采纳其原始 `data-math-source` 并由本机审计；其中
Gaussian kernel、半径常数和 bootstrap 算术通过，完整 Duhamel/resolvent
链仍明确属于 conditional analytic lemma。

### 1. Gaussian degree-local kernel

规范化固定为 `e_m=H_m/sqrt(m!)`、`eta_m=L[e_m]`、
`phi_k=pi_k/sqrt(k!)`。因此 `d_k=sqrt((2k+1)!)/k!`，并且

`eta_(2k+1)=k!/sqrt((2k+1)!)*[alpha_k gamma_k-
sum_(m<=2k)c_(k,m)eta_m]`。

Gaussian 点 `phi_k=e_k` 时，Hermite product formula 与
`xH_m=H_(m+1)+mH_(m-1)` 给出

`[x e_k^2]_(e_(2j+1)) = sqrt((2j+1)!)*k!/[j!^2(k-j)!]
*(1+2(k-j)/(j+1))`。

令 `y_j=|eta_(2j+1)|sigma_n^(2j+1)/sqrt((2j+1)!)`，
`sigma_n=8sqrt(n)`，则真实的线性下三角 transfer 是

`K_(k,j)=(k!)^2(2j+1)!/[(2k+1)!j!^2(k-j)!]
*(1+2(k-j)/(j+1))*sigma_n^(2(k-j))`。

写 `d=k-j`，阶乘比满足

`(k!)^2(2j+1)!/[j!^2(2k+1)!]
=prod_(r=1)^d (j+r)^2/[(2j+2r)(2j+2r+1)] <=4^(-d)`。

所以

`K_(k,j)<=(1+2d)(16n)^d/d!`，
`sum_(j<k)K_(k,j)<=(1+32n)e^(16n)-1`。

这是本轮最干净的 unconditional algebraic result：Gaussian linearized odd
Green row 只有 `e^(O(n))` 大小，故 R73 的 `e^(O(n^2 log n))` 确实来自
uniform source recursion 的人为累乘，而非 factorial denominator 本身。

### 2. Conditional finite-head Jacobi resummation

有限 Jacobi matrix 写成 `J=B+aD`，其中
`D=diag(0,1,-1,0,...)`，`B` 为 zero-diagonal Jacobi part，Gaussian 值
`B_0` 的 off-diagonal 为 `sqrt(k)`。对 degree `<=2n+1`，

`Phi_(B,a)(z)=e^(-z^2/2)<e_0,e^(z(B+aD))e_0>`，
`Y(a,B)=[Phi_(B,a)-Phi_(B,-a)]/2`。

在 `rho_n=4sqrt(n)`、`||E||_rho<=1`、`||Y||_rho<=1/16` 的 Gram-domain
下，R74 给出条件性的 parity-Schur estimate

`|gamma_k(E,Y)-gamma_k(E,0)|<=40||Y||_rho^2`，
`|beta_k/k-1|<=5||E||_rho+275||Y||_rho^2`，
`||B-B_0||<=sqrt(n)(10||E||_rho+550||Y||_rho^2)`。

其结构含义是精确的：odd moment block `C` 在 Gram inverse 的 diagonal
上一阶必然消失，因此 `Delta B=O(E)+O(Y^2)`，而不是 `O(Y)`。不过这些
Schur-complement 常数和之后的 Duhamel 估计需要完整写出 resolvent 细节，
本机当前审计的是公式之间的归一化和常数相容性，不把它们误报成已脱离
conditional domain 的 unconditional theorem。

取 `R=2sigma_n=16sqrt(n)`，网页端的粗 resolvent bound 为 `e^(224n)`，
并给出

`||Y-aU||_sigma <=1024n e^(224n)|a|||B-B_0||
 +1366n^(3/2)e^(224n)|a|^3`。

代入 parity estimate，并利用 odd degree `>=3` 的 radius loss，得到

`||o||_sigma <= C_n(|a|||E||_rho+|a|^3)
 +17600n^(3/2)e^(224n)|a|||o||_sigma^2`，
`C_n=2^25 n^3e^(544n)`。

在 `|a|<=r_n=2^(-31)n^(-3)e^(-544n)` 上二次项可吸收，从而条件性地得到

`||O_n(a,E)||_sigma<=Omega_n(|a|^3+|a|||E||_rho)`,
`Omega_n=2^26n^3e^(544n)=e^(O(n))`。

### 3. Conditional no-reversal window

直接在输入半径 `sigma_n`、输出半径 `rho_n=sigma_n/2` 上使用 angular
coefficient bound：

`A_(2k)^(-1)(rho_n/sigma_n)^(2k)<=1/4`。

这与 R72 的固定 `q` 半径损失表述不同，但本身的系数算术成立。令
`Ubar_n=32sqrt(n)e^(160n)`，则 sufficient scales 为

`|a|<=min{r_n,1/(12*4^n Ubar_n),
sqrt(Ubar_n/[4Omega_n(1+3Ubar_n^2)])}`。

bootstrap 的严格改善必须使用 `||o||_sigma<=|a|Ubar_n/4` 和
`||E||_sigma<=|a|Ubar_n/4`，从而 `X<=3|a|Ubar_n/2`；若直接替换成
`2|a|Ubar_n`，在系数 `1/4` 下不够推出严格改善。充分大 `n` 时
`r_n` 最小，于是得到 conditional

`a_n#=2^(-31)n^(-3)e^(-544n)`，
`t_n#=2^(-62)n^(-6)e^(-1088n)`，
并有 `gamma_k(t)>0`、`beta_k(t)>0 (k<=n)` 在 `0<=t<=t_n#` 上成立。

这把 R73 的 super-exponential gap 降为 pure-exponential gap，但仍远未匹配
`A_(2n)~3(2/3)^n/sqrt(pi n)` 的 natural angular scale。D.1、positive
infinite exact backward tower 与 backward OU divisibility 仍 OPEN；下一条
唯一目标是 moving-radius Green kernel，在第 `k` 层用 `sigma_k~sqrt(k)`，
继续压低指数 `544` 并检验 `t_n#` 能否逼近 `A_(2n)`。

新增本机审计为 `flat_shadow_odd_green_r74/audit_r74.py`。

## 72. R75：moving-radius conjugation 的符号校正（2026-09-07）

R75 的 moving-radius factorization 本身成立，但其 Volterra 方程出现了一个
必须纠正的符号。对任意正半径 `sigma_k`，定义

`v_k=(k!)^2 sigma_k^(2k+1)/(2k+1)!`，
`Z_k=eta_(2k+1)sqrt((2k+1)!)/(k!)^2`。

R74 的带权 transfer 精确因子化为

`K_(k,j)^mov=(v_k/v_j)q_(k,j)`，
`q_(k,j)=1/(k-j)!*(1+2(k-j)/(j+1))`。

这一步完全吸收了 moving radius 与 factorial weight；它是本轮保留的
unconditional algebraic lemma。

但 R73 exact recursion 是

`eta_(2k+1)=factor_k*[alpha_k gamma_k-sum_(m<=2k)c_(k,m)eta_m]`，

而 Gaussian 的 `c_(k,2j+1)>0`。因此 signed conjugated variable 的确切方程
是

`Z_k=S_k-sum_(j<k)q_(k,j)Z_j`，

不是网页端原先写出的 plus 号。令 `Z(x)=sum Z_k x^k`、
`S(x)=sum S_k x^k`、`F(x)=integral_0^x Z(t)dt`，正确的解析式为

`Z+2F=e^(-x)S`，
`F'+2F=e^(-x)S`，
`F=e^(-2x) integral_0^x e^tS(t)dt`，
`Z=e^(-x)S-2e^(-2x) integral_0^x e^tS(t)dt`。

因此 signed Gaussian Green 对 entire source 不产生 `2-e^x` 分母，也没有
真实的 `log(2)` 极点。网页端给出的
`(2-e^x)^{-1}`、`(log 2)^(-1)` 和 resonance functional 只适用于将 signed
递推取绝对值后的 positive majorant；它们不能被记录为 canonical Gaussian
odd propagation 的谱障碍。R64 tangent 的交替号

`z_m=(-1)^(m-1)m(m+1)/(2m!)`

恰好通过 corrected signed Volterra equation；本机审计用 `S(x)=x+x^2/2`
复现了 `z_1=1,z_2=-3/2,z_3=1,z_4=-5/12`。

所以 R75 的可报告进展不是“发现了 `1/log 2` 的真实障碍”，而是把
moving-radius Green 的半径共轭精确化，并排除了一个由绝对值 majorant 引入
的假谱障碍。它也说明：要升级到 nonlinear odd tame，必须保留 canonical
source 的符号/结构，不能直接使用 positive Volterra row sum。R75 的另一个
网页估计 `e^(64mu n/e)` 也没有纳入，因为其从
`k!/(2k+1)!` 到指数常数的推导尚未通过本机审计。

D.1、positive infinite exact backward tower 与 backward OU divisibility 仍
OPEN。下一条唯一目标改为 R76：从 `alpha_k=0` 的 exact Jacobi/Gram recursion
导出 sign-preserving nonlinear source，检查其在 corrected signed Green 下的
实际 cancellation，而不是研究 artificial `log(2)` resonance。

新增本机审计为 `flat_shadow_odd_green_mov_r75/audit_r75.py`。

## 73. R76：corrected signed source 与 factorial-transfer 接口（2026-09-07）

网页端 R76 已完成，但其连接器仍返回账户连接错误，未能实际读取本机
R75 的 framework/README/audit。这里把网页端返回的 raw math sources 与本机
R75 校正基线重新对齐后记录；因此以下是已审计公式与明确条件的研究记录，
不是把网页端未读到的本机文件当作已读证据。

R76 的第一个无条件代数对象是 exact signed nonlinear source。沿用
`e_m=H_m/sqrt(m!)`、`eta_m=L[e_m]`、`phi_k=pi_k/sqrt(k!)`、
`gamma_k=L[phi_k^2]`，精确 Jacobi 展开为

`x phi_k^2 = sqrt((2k+1)!)/k! e_(2k+1) + sum_(m<=2k)c_(k,m)(E,Y)e_m`，

`T_k=1/k![alpha_k(a)gamma_k(E,Y)-sum_(m<=2k)c_(k,m)(E,Y)eta_m]`，

`Z_k=eta_(2k+1)sqrt((2k+1)!)/(k!)^2`。

R75 已审计的 Gaussian linearization 是

`D_Y T_k(0)[Z]=-sum_(j<k)q_(k,j)Z_j`，

其中

`q_(k,j)=(1+2(k-j)/(j+1))/(k-j)!`。

所以必须定义

`S_k:=T_k+sum_(j<k)q_(k,j)Z_j`，

从而 exact signed recursion 仍是

`Z_k=S_k-sum_(j<k)q_(k,j)Z_j`。

这个 `S_k` 是 R76 的关键 source residual；它与取绝对值后的正 majorant
不同，不能混用。

R76 的第二个代数里程碑是 parity ideal。反射给出

`phi_k(E,-Y;x)=(-1)^k phi_k(E,Y;-x)`，`gamma_k(E,-Y)=gamma_k(E,Y)`。

结合 `alpha_1=a`、`alpha_2=-a`、`alpha_k=0 (k>=3)`，在 involution
`(a,Y)->(-a,-Y), E->E` 下 source 为 odd。减去已校正的 Gaussian tangent

`S^(1)(x)=x+x^2/2`，令 `S_tilde=S-aS^(1)`，则在 Gram inverse 存在的
formal/analytic neighborhood 中有精确理想包含

`S_tilde in a(E,Y^2)+EY+Y^3`。

对 `k>=3` 因为没有显式 `alpha_k`，更精确地有
`S_k in EY+Y^3`。这里的内容是反射与 exact Jacobi linearization 强迫的
代数消去，不是把 `O(a^3)` 当作尚未证明的 uniform norm bound。代入
`Y=O(a)`、`E=O(a^2)` 后 source 从 cubic canonical order 开始。

R76 的第三个结果是把 corrected signed Green 写成整个函数的 Volterra 算子。
令 `Z(x)=sum Z_k x^k`、`S(x)=sum S_k x^k`、`F=int_0^x Z(t)dt`，则

`Z+2F=e^(-x)S`，

`F=e^(-2x)int_0^x e^tS(t)dt`，

`Z=e^(-x)S-2e^(-2x)int_0^x e^tS(t)dt`。

所以 entire source 产生 entire signed solution，不存在 signed Green 的
`log(2)` 极点；该极点只属于丢失交替抵消后的 absolute-value majorant。
取 `S^(1)=x+x^2/2` 时得到

`Z^(1)=e^(-x)(x-x^2/2)`，
`[x^k]Z^(1)=(-1)^(k-1)(k+1)/(2(k-1)!)`，`k>=1`，

与 R64 已审计的 alternating tangent 完全一致。

R76 还给出一个严格的 conditional transfer theorem。若

`|S_k|<=M mu^k/k!`，`mu>=0`，

则由 `Z'+2Z=e^(-x)(S'-S)` 和 `b_k=k!|Z_k|` 得

`b_(k+1)<=M(mu+1)^(k+1)+2b_k`，`b_0<=M`。

当 `mu!=1` 时其 equality majorant 为

`b_k<=M[2^k+(mu+1)((mu+1)^k-2^k)/(mu-1)]`，

`mu=1` 时为 `b_k<=M(k+1)2^k`。故 signed propagation 只产生固定
exponential-type shift `lambda_mu=max(2,mu+1)`，而不是 `log(2)` resonance。

这一转移仍是 conditional 的，因为 source 自身的 uniform factorial bound
尚未证明。当前最小缺口定义为 `FS_mu`：存在与 `n` 无关的 `C,mu`，使

`|S_tilde_k|<=C mu^k/k! Xi`，

`Xi=|a|(||E||+||Y||^2)+||E||||Y||+||Y||^3`。

若 `FS_mu` 成立，则在 `sigma_n=8sqrt(n)` 上由
`(2k+1)!/k! >= (k+1)!` 得条件性 odd tame conversion

`||o||_(sigma_n)<=C C_mu [8sqrt(n)/(64lambda_mu n)]
(exp(64lambda_mu n)-1)Xi`。

这会把 R74 的问题进一步归结为一个清晰的 Gram-to-source degree-local
factorial estimate，而不是 Green propagation resonance。

本轮边界：R76 没有证明 `FS_mu`、D.1、positive infinite exact backward
tower 或 backward OU divisibility；也没有宣称新的 unconditional no-reversal
window。已新增本机审计
`flat_shadow_odd_green_source_r76/audit_r76.py`，覆盖 source 符号、tangent
系数、形式 ideal、factorial convolution/transfer 及 common-radius 算术。

下一轮唯一目标是 R77：直接从 exact Gram/Jacobi source map、Gram inverse 与
Hermite product 证明 `FS_mu`，或给出最小的 degree-local 失败边界；不再把所有
degree 压成顶层 `n` 的粗 uniform source bound。

## 74. R77：degree-local Gram-to-source factorial estimate（2026-09-07）

网页端 R77 完成时连接器仍返回账户连接错误，未实际读取 R76 本机文件；本节
采用其 raw math sources，并以 R76 的 exact source、parity ideal 与 corrected
signed Green 为已审计基线。关键是把新结果写成明确的局部条件定理，而不是
把“Gram-connected”泛化成仅凭正定/可逆即可。

令 `rho_k=4sqrt(k)`，在 degree `<=2k` 的 Hermite moments 上定义

`||h||_(rho_k)=sum_(m=3)^(2k)|eta_m|rho_k^m/sqrt(m!)`，`h=E+Y`。

在 degree-local Hermite-Wiener 小球
`||E||_(rho_k)+||Y||_(rho_k)<=delta_*=1/40` 内，R77 给出以下
source estimate：对任意固定 `mu>3`，存在与 `k,n` 无关的 `C_mu`，使 `k>=3`
时

`k!|S_k(E,Y)| <= C_mu mu^k
(||E||_(rho_k)||Y||_(rho_k)+||Y||_(rho_k)^3)`。

恢复 finite head `alpha_1=a`、`alpha_2=-a` 并减去
`S^(1)(x)=x+x^2/2` 后，

`k!|S_tilde_k(a,E,Y)|<=C_mu mu^k Xi_k`，

`Xi_k=|a|(||E||_(rho_k)+||Y||_(rho_k)^2)
 +||E||_(rho_k)||Y||_(rho_k)+||Y||_(rho_k)^3`。

因此得到局部的 `FS_(3+epsilon)`，对任意 `epsilon>0` 成立；端点
`FS_3` 仍 OPEN。这里的“局部”是实质限制：若只知道每个 finite Gram
matrix 正定或可逆，而没有统一的 weighted small-ball/derivative control，
R77 的结论不能直接推出。

R77 的 Gram 端算术如下。Hermite multiplication 的 degree-local bound 为

`||P_(V_k)M_(e_m)P_(V_k)||<=2^m(3k)^(m/2)/sqrt(m!)`。

配合 `rho_k=4sqrt(k)`，每个 moment perturbation 的加权贡献恰为
`(sqrt(3)/2)^m`，故

`||G_(k-1)-I||<=C_G||h||_(rho_k)`，
`C_G=(sqrt(3)/2)^3/(1-sqrt(3)/2)<5`。

在 `delta_*=1/40` 时它小于 `1/8`，从而
`||G_(k-1)^(-1)||<=8/7`。resolvent derivative identity 给出

`||D^rG^(-1)||<=r!(8/7)^(r+1)C_G^r`，`r<=3`，

说明在该局部域内 Gram inverse 的有限阶导数不产生 `k!` 或 `n` 灾难。
`phi_k=e_k+v_k` 的相应一至三阶 degree-local 导数界是本结论需要显式
保留的 analytic input，不能仅由 positivity 自动推出。

source numerator 的 degree growth 来自 `x psi chi`。固定 `mu>3`，令

`q_mu=mu+1`，`p_mu=2(mu+1)/(mu-3)`，
`1/2=1/p_mu+2/q_mu`。

Gaussian hypercontractivity 与 Holder 给出

`||xpsi chi||_2<=||x||_(p_mu)mu^k||psi||_2||chi||_2`。

对 `phi_k` 及其至多三阶导数应用后，exact triangular numerator 的导数
满足 `||D^rB_k||<=C_(mu,r)mu^k`。因 `T_k=B_k/k!`，这个 `k!` 分母
正好转化为 `FS_mu` 所需的 factorial scale。`mu=3` 端点在当前证明中
对应 `p_mu=infinity`，而高斯下 `x` 不属于 `L^infinity`；这是当前
Holder–hypercontractive 方法的失败边界，不等于最佳常数已被证明为 3。

parity 部分沿用 R76：对 `k>=3`，`B_k(E,Y)` 对 `Y` 为 odd，且
`S_k=T_k+sum_(j<k)q_(k,j)Z_j` 恰好去掉 Gaussian Y-linear term。沿 E、Y
分别使用 Taylor 公式，得到 `EY+Y^3`；finite head 只增加
`a(E,Y^2)`。所以 lower odd feedback 不在 source estimate 中再作一次
卷积，而留给 corrected signed Green 一次处理。

对 `k<=n`，`rho_k<=rho_n`，绝对值序列范数单调，因此局部估计统一为

`k!|S_tilde_k|<=C_mu mu^k
[|a|(||E||_(rho_n)+||Y||_(rho_n)^2)
 +||E||_(rho_n)||Y||_(rho_n)+||Y||_(rho_n)^3]`。

取 `mu=3+epsilon` 并接上 R76 的 signed factorial transfer，令
`lambda_mu=4+epsilon`，得到条件性 common-radius odd bound

`||Z_tilde||_(sigma_n)<=C_epsilon n^(-1/2)
 exp((256+64epsilon)n)Xi`，`sigma_n=8sqrt(n)`。

结合此前审计的 `||U||_(sigma_n)<=32sqrt(n)e^(160n)`，保守 bootstrap
代数给出

`|a|<=c_epsilon n^(-1/4)e^(-(288+32epsilon)n)`，
`t=a^2<=c_epsilon^2 n^(-1/2)e^(-(576+64epsilon)n)`。

该 scale 仍是 conditional 的：它需要前面 even response 与 Gram-domain
closure；它约为 `e^(-576n)`，显著优于 R74 的 `e^(-1088n)`，但仍远小于
`A_(2n)~3e^(-0.405465n)/sqrt(pi n)`。因此 R77 是一个真正的 all-degree
local source milestone，却不是 D.1 或 positive tower 的解决。

本轮尚未证明 `FS_3`、仅凭 Gram positivity 的 global theorem、D.1、positive
backward tower 或 backward OU divisibility。下一条唯一目标转为
**factorial-type even bootstrap without common-radius conversion**：在与
`k!|S_k|<=Cmu^k` 兼容的 sequence norm 中闭合 same-factor even angular
solver，去除 `e^(64lambda_mu n)` 与 `4^n` 的共同半径损失。

新增本机审计为 `flat_shadow_odd_green_source_r77/audit_r77.py`。

## 75. R78：same-radius factorial even bootstrap（2026-09-07）

网页端 R78 完成时连接器仍返回账户连接错误，未实际读取 R77 本机文件；本节
采用其 raw math sources，并以 R77 的局部 `FS_(3+epsilon)` 与 R76 的 signed
factorial transfer 为基线。结论必须保留为有限层、局部、条件性的 same-factor
闭包，不把任意 even forcing 的 angular inverse 当成已解决。

令 Gaussian-normalized Hermite series 为

`f(z)=E(z)+Y(z)=sum_(m>=1)f_m z^m`，`f_m=L[e_m]/sqrt(m!)`。

在 exact same-factor angular identity 的 `2k` 次系数中，假设其形式为

`A_(2k)E_(2k)+Q_(2k)(f,f)+C_(2k)(f,f,f)=0`，

`A_(2k)=3 binom(2k,k)/6^k`，并具有角系数绝对值控制

`|C_(r,s)+C_(s,r)|<=2A_(2k)`，
`|D_(r,s,t)|<=A_(2k)`，

其中 `r+s=2k`、`r+s+t=2k`。由加权 Young 不等式，实际同因子 source
满足

`|E_(2k)|<=sum_(r+s=2k)|f_r f_s|
 +sum_(r+s+t=2k)|f_r f_s f_t|`。

因此 arbitrary-source 的 `A_(2k)^(-1)~sqrt(k)(3/2)^k` 不进入实际
same-factor nonlinear source。这里的角系数绝对值控制是明确的 conditional
input；没有它，不能把这个 cancellation 推给任意 even forcing。

对固定 truncation `n`，取单一系数 Wiener 半径
`R_n=4sqrt(n)`，范数
`||g||_n=sum_(m<=2n+1)|g_m|R_n^m`。普通卷积的三角不等式给

`||gh||_n<=||g||_n||h||_n`，

并从上述 exact same-factor coefficient majorant 得到 conditional even
bootstrap lemma

`||E||_n<=||f||_n^2+||f||_n^3`，`f=E+Y`。

这一步消除了两种人为损失：不再把 `rho_n=4sqrt(n)` 换到
`sigma_n=8sqrt(n)`，也不再单独支付 `4^n`；但它并没有说明完整解已经处于
R77 的 Gram 小球。

与 R77 结合时，若 `||E||_n+||Y||_n<=1/40`，因为
`rho_k<=R_n` 对 `k<=n`，每个 prefix 都满足 R77 的局部条件。取任意
`mu>3`、`lambda=mu+1`，R76 signed transfer 给

`|Z_tilde_k|<=D_mu lambda^k/k! Xi`，可取
`D_mu<=2mu C_mu/(mu-1)`。

换回 odd Hermite coefficient
`|o_(2k+1)|<=D_mu Xi k!lambda^k/(2k+1)!`，直接在同一 `R_n` 求和。
利用 `k!/(2k+1)!<=1/(k+1)!` 及末项比值控制，得到

`||o||_n<=Gamma_(n,mu)Xi`，
`Gamma_(n,mu)=K_mu n^(-1/2)[16e(mu+1)]^n`，
`K_mu=256mu C_mu/[31(mu-1)]`。

R64 tangent 的同范数大小记为 `H_n`。其精确 odd coefficient 与相邻比值给出

`H_n<=8/3 n^(3/2)16^n`。

令 `x=|a|H_n`，采用
`||Y||_n<=2x`、`||E||_n<=8x^2`、`x<=1/100`。even lemma 严格改善，
R77 source factor 则满足 `Xi<=36x^3`；若
`36Gamma_(n,mu)x^2<=1`，odd 也严格改善。故保守的 conditional local
window 为

`a_(n,mu)#=H_n^(-1)min{1/100,[36Gamma_(n,mu)]^(-1/2)}`，
`t_(n,mu)#=(a_(n,mu)#)^2`。

使用 `H_n` 与 `Gamma` 的显式上界，充分大 `n` 时可取

`a_(n,mu)# >= [16sqrt(K_mu)]^(-1)n^(-5/4)
[64sqrt(e(mu+1))]^(-n)`，

`t_(n,mu)# >= [256K_mu]^(-1)n^(-5/2)
[4096e(mu+1)]^(-n)`。

这比 R77/R74 共同半径链条的 `e^(-1088n)` 更好，也准确说明了新的主要
瓶颈：不是 angular inverse 的 `(3/2)^n`，不是额外 `4^n`，而是为了进入
R77 Gram 小球而支付的 Gaussian tangent 同范数 `H_n~n^(3/2)16^n`，以及
在该 growing radius 上的 signed Green evaluation loss。与
`A_(2n)~3(2/3)^n/sqrt(pi n)` 比较仍有巨大指数差距。

R78 尚未证明 D.1、positive backward tower、backward OU divisibility，也
没有把 Gram 小球中心从 `0` 移到大背景 `aU`。下一条唯一目标是
**tangent-centered Gram/source bootstrap**：利用 R71 的
`A_n=P_nM_(g_1)P_n`、`sup_n||A_n||<infinity`，写
`G_n(a)=I+aA_n+R_n(a)`，只约束 `(E,o)` 的小量而把 `aU` 作为精确背景，
检验能否移除 `16^n` tangent penalty。

新增本机审计为 `flat_shadow_even_same_radius_r78/audit_r78.py`。

## 76. R79：tangent-centered Gram/source bootstrap（2026-09-07）

网页端 R79 的完整回复已在本机提取；本轮将其作为 R78 的后续局部定理，
并对算子域、奇偶理想、bootstrap 算术及反馈边界作独立审计。R79 的核心
进展是把“大切向量在 growing Wiener radius 中很大”与“切向 Gram 作用的
算子范数有界”区分开来，而不是把二者继续混为同一个小量条件。

令 `e_j=H_j/sqrt(j!)`，`V_n=span{e_0,...,e_n}`，`P_n` 为 Gaussian
正交投影。若 `L_(a,E,o)=L_0+aL_1+L_(E+o)`，且 `L_1[p]` 的代表函数为
有界的 `g_1`，则有精确 Gram 分解

`G_n(a,E,o)=I+aA_n+Hcal_n(E+o)`，
`A_n=P_nM_(g_1)P_n`，`sup_n||A_n||_op<=||g_1||_infinity`。

在 `R_n=4sqrt(n)` 及 `||h||_n=sum|h_m|R_n^m` 下，沿用 R77 的 degree-local
Hermite 乘法估计

`||Hcal_n(h)||_op<=C_G||h||_n`，
`C_G=(sqrt(3)/2)^3/(1-sqrt(3)/2)<5`。

所以只要

`|a|M_1+C_G(||E||_n+||o||_n)<=1/2`，

就有 `||G_n^(-1)||_op<=2`。resolvent 的一至三阶导数只看
`M_1|dot a|+C_G||dot h||_n`，从 Gram 逆本身移除了 `|a| ||U||_n` 的小量
要求。这是 R79 最可靠的 structural operator lemma。

反射给出 `PA_nP=-A_n`、`PHcal_n(E)P=Hcal_n(E)`、
`PHcal_n(o)P=-Hcal_n(o)`，即
`PG_n(a,E,o)P=G_n(-a,E,-o)`。写 `Y=aU+o` 并减去 R64 finite-head
切向源 `aS^(1)`（`S^(1)(x)=x+x^2/2`）后，R76/R77 的 signed-source
机制在局部假设下给出

`S_tilde in E(a,o)+(a,o)^3`，

其中 `E(a,o)` 表示含一个 `E` 且至少含一个 `a` 或 `o` 的项，后者表示
关于 `(a,o)` 总次数至少三。相应 factorial 源估计为

`k!|S_tilde_k|<=C_mu mu^k[(|a|+||o||_n)||E||_n
 +( |a|+||o||_n)^3]`，`mu>3`，

signed Green 后得到

`||o||_n<=Gamma_(n,mu)[(|a|+||o||_n)E_*+(|a|+||o||_n)^3]`，
`Gamma_(n,mu)=K_mu n^(-1/2)[16e(mu+1)]^n`。

与 R78 同因子 even 方程结合，令 `x=|a|H_n`、`E_*=||E||_n`、
`O=||o||_n`，则局部 bootstrap 给出 `E_*<=5x^2` 及（当
`48Gamma x^2<=1`）`O<=x/2`。切向精确系数满足

`H_n=sum_(k=1)^n k(k+1)!/[2(2k+1)!](4sqrt(n))^(2k+1)
 <=4n^3(4e)^n`。

因此当前可写出条件性的窗口

`a#=min{1/(4M_1), x#/H_n}`，
`x#=min{x_0,[48Gamma_(n,mu)]^(-1/2)}`，
`x_0=min{1/100,1/(32C_G)}`。

但 R79 同时给出不可忽略的失败边界：标量模型

`E=x^2`，`O=Gamma(aE+EO)`，故
`O=Gamma aE/(1-Gamma E)`。

所以有界 `A_n` 只修复 Gram 逆的中心问题，不能自动消除 `Gamma E_*<1`
这一残差反馈条件。用粗界仍只有

`a#>=c_mu n^(-11/4)[4e sqrt(16e(mu+1))]^(-n)`，
`(a#)^2>=c'_mu n^(-11/2)[256e^3(mu+1)]^(-n)`。

这是一项真实的局部算子/源项里程碑，但不是 D.1、positive backward tower
或 backward OU divisibility 的证明。下一步唯一主攻目标是 R80：把 R64 的
二次偶响应写成 `E=a^2V+Ehat`，证明 `sup_n||Hcal_n(V)||_op<infinity`
并吸收为 `I+aA_n+a^2B_n`，或者直接证明该 `a^2V` 对 odd signed Green
的贡献有统一 `O(a^2)` 乘子。若成功，`Gamma a^2H_n^2` 将被替换为统一
`Ca^2`，才可能取得实质强于 R79 的窗口。

新增本机审计为 `flat_shadow_tangent_centered_r79/audit_r79.py`。

## 77. R80：quadratic-even centered operator lemma（2026-09-07）

网页端 R80 已完成，但桥接在本轮仍返回账户连接错误，因此网页端没有
实际读取 R79 本机记录；本机只把其完成回复与 R64/R79 基线逐项对照，且不
把条件性层级误写成无条件正性结论。

在 R64 的 formal same-factor equation 下，写
`F_a=1+aU+a^2V+O(a^3)`。Beta 恒等式
`1/binomial(2m,m)=(2m+1) integral_0^1[tau(1-tau)]^m dtau`
给出系数级精确逆
`A^(-1)W=(1/3) integral(1+z partial_z)W(sqrt(6q_tau)z)dtau`。
对 `B=average sum_(i<j)U(r_i z)U(r_j z)`，令
`xi=6q_tau q_s r_i^2`、`eta=6q_tau q_u r_j^2`、`alpha=xi+eta`，则
`alpha<=3/8<1/2`，且反 Hermite 表示使用
`psi_alpha=(1-2alpha)^(-1/2)exp[-alpha x^2/(1-2alpha)]`。

本机符号审计确认了四项微分多项式、Beta 逆以及
`R^m psi_alpha=delta^(-(m+1)/2)H_m(x/sqrt(delta))
exp[-alpha x^2/delta]`（`R=x-partial_x`）。注意微分多项式必须在
`alpha=xi+eta` 后比较；这是公式成立所用的隐含关系。

网页端给出的参数端点估计也被本机独立加强。对
`I(a,b)=integral q_s q_u a^(3/2)b^(3/2)/(a q_s+b q_u)^3 dsdu`，四象限
对称性和 `s/2<=q_s<=s`（`s<=1/2`）把问题化为 `I<=32J`。令
`x=as,y=bu`，精确积分
`integral_[0,A]integral_[0,B]xy/(x+y)^3 dxdy=AB/[2(A+B)]`
给出 `J=sqrt(ab)/[4(a+b)]<=1/8`，故实际有 `I<=4`，强于网页端
使用的 `I<=32`。因此显式 Gaussian multiplier `g_2` 满足
`||g_2||_infinity<=4C_*=:M_2`，条件是 R64 formal quadratic equation 与
三因子 angular 几何成立。

于是在 normalized Hermite basis `e_k=H_k/sqrt(k!)` 下，无条件的
operator identity（相对于上述 formal V）为
`Hcal_n(V)=P_nM_(g_2)P_n`，从而
`sup_n||Hcal_n(V)||_op<=M_2`。写 `E=a^2V+Ehat` 后，Gram background
变为
`G_n=I+aA_n+a^2B_n^(2)+Hcal_n(Ehat+o)`，其中
`B_n^(2)=P_nM_(g_2)P_n`。这证明二次偶响应不是 Gram-level boundary-layer
blow-up 来源；`aU` 与 `a^2V` 都可在 operator norm 中作为背景处理。

依赖 R77 factorial transport 在新背景上重做的 conditional lemma 为
`k!|S_tilde_k|<=C_mu^(2)mu^k[(|a|+||o||)||Ehat||
+(|a|+||o||)^3]`，`mu>3`。与 R78 exact even closure 拼接，令
`x=|a|H_n`、`G=Gamma_(n,mu)`、`η=Ga^2H_n`、`ζ=Ga^4H_n^4`，在
`x,η,ζ<=10^(-4)` 下，本机审计确认网页端 bootstrap
`O<=16|a|(Ga^2+ζ)`、`Ehat_*<=8(xO+x^4)` 的标量算术闭合。

相应条件性窗口可写为
`a#=min{a_bg,delta/H_n,sqrt(delta/(Gamma H_n)),
(delta/(Gamma H_n^4))^(1/4)}`，其中
`a_bg=min{1,1/(8M_1),1/sqrt(8M_2)}`。结合
`H_n<=4n^3(4e)^n`、`Gamma<=K_mu^(2)n^(-1/2)[16e(mu+1)]^n`，大 n 的
主导条件变为 `Gamma a^2 H_n<=delta`，即
`t# >= c_mu n^(-5/2)[64e^2(mu+1)]^(-n)`。与
`A_(2n)~3(2/3)^n/sqrt(pi n)` 的比值为
`O_mu(n^(-2)[3/(128e^2(mu+1))]^n)`，仍趋于零；但相对 R79 已移除一
个完整的 tangent H_n 因子。

严格边界：`sup_n||Hcal_n(V)||<infinity` 不蕴含 signed-Green 后
`Ehat->o` multiplier 的 n-uniform `O(a^2)` 界；当前仍有
`Gamma a^2H_n` 反馈。下一目标是混合算子
`o -> A^(-1)Q(U,o) -> signed-Green D_E S` 的 cancellation。D.1、
positive infinite exact backward tower、backward OU divisibility、全局
positivity 以及 endpoint `FS_3` 继续 OPEN。

新增本机记录与审计：`flat_shadow_quadratic_even_r80/README.md`、
`flat_shadow_quadratic_even_r80/audit_r80.py`。

## 78. R81：mixed tangent–residual operator cancellation（2026-09-07）

R81 网页端已完成，但最终回复再次说明桥接账户连接错误，未实际读到 R80
本机文件或独立核验 `7c42885`；以下记录严格按本机 R80 基线审计。

在 `Y=aU+o`、`E=a^2V+Ehat` 坐标中，令
`M_n=A_e^(-1)Q(U,·)`，令 `L_n` 为 corrected signed-Green 后的
`D_Ehat` odd source map。R81 给出 formal same-factor/Jacobi 层级内的精确
Schur 补恒等式
`D_o Ehat[o]=-2aM_no`、`D_Ehat o[Ehat]=aL_nEhat`，所以 mixed Jacobian
为 `D_o o_new=-2a^2K_n`、`K_n=L_nM_n`。R80 中的 `Gamma_n H_n` 正是
将这两个因子分别粗估后丢掉复合结构的结果。

一个新的 operator-level 正结果是：若 `U=Tg_1`、`o=Th` 且 `g_1,h` 为
bounded Gaussian multipliers，则对 `r^2+s^2<=1` 可选择标准 Gaussian
`Y_1,Y_2`，使其无条件独立、条件均值为 `rX,sX`、条件噪声协方差为 `-rs`。
于是 Wick contraction 满足
`||Gamma_r g_1 diamond Gamma_s h||_infinity
<=||g_1||_infinity||h||_infinity`。
由于三因子 angular 几何有 `r_i^2+r_j^2<=1`，故 angular inverse 之前的
mixed source 满足 dimension-free bound
`||T^(-1)Q(U,o)||_infinity<=3||g_1||_infinity||h||_infinity`。
因此 R80 的 `H_n~(4e)^n` 不是 U-leg 本身产生的，而是后续 angular inverse
与 triangular source transport 的损失。

R81 同时给出两个严格失败边界。第一，generic even Hermite mode
`W_k=z^(2k)/sqrt((2k)!)` 的 `L^2` 范数为 1，但
`||A_e^(-1)W_k||=A_(2k)^(-1)~sqrt(pi k)(3/2)^k/3`；所以 bounded
multiplier 的 pre-inverse 估计不能由抽象 operator theory 推成 `M_n` 的
uniform bound，必须利用 actual mixed image 的 signed degree localization。

第二，Gram-Schmidt 一阶导数含 strict-lower-triangular projection
`Dphi_k[H]=-sum_(j<k)H_(jk)e_j`。对离散 Hilbert 矩阵
`H_(jk)=1/(j-k)`，full compression operator norm 有界，但取常向量可得
`||L_-(H)||_op>=c log N`。所以即使 `Hcal_n(M_no)` 的 operator compression
uniformly bounded，也不能仅凭此控制 `D_E S` 的 n-uniform derivative；实际
mixed image 若有 cancellation，必须另证。

R81 将缺口化为精确 weighted column criterion。若
`omega_(n,j)=((j!)^2/(2j+1)!)R_n^(2j+1)`、`R_n=4sqrt(n)`，则
`||K_n||_(l^1(omega)->l^1(omega))` 恰为
`sup_j omega_(n,j)^(-1)sum_k omega_(n,k)|K_(k,j)^(n)|`。
故需要核验
`sup_(n,j)sum_k|K_(k,j)^(n)|omega_(n,k)/omega_(n,j)<infinity`。
固定 gap `d` 且 `j/n` 保持在 `(0,1]` 时，权重比
`omega_(n,j+d)/omega_(n,j)~(4n)^d`；无跨 degree cancellation 时，必须有
`K_(j+d,j)^(n)=O(n^(-d))`。

定义 `MGK(C_K)` 为上述 column bound。若它成立，mixed linear feedback
从 R80 的 `Gamma a^2H_n` 改为 `2C_Ka^2<1`。但 quartic even remainder
仍给出 `Gamma a^4H_n^4<<1`，故当前 machinery 只能条件性地改善为
`t#>=c_mu n^(-23/4)[64e^2 sqrt(e(mu+1))]^(-n)`；固定 `mu downarrow3`
时 denominator base 趋近 `128e^2 sqrt(e)`，仍远低于 angular natural
scale `A_(2n)~3(2/3)^n/sqrt(pi n)`。

本机已审计 Schur 补、Wick 协方差、angular inverse 增长、triangular no-go、
weighted fixed-gap 比值、quartic 指数和 MGK column norm。新增记录与审计为
`flat_shadow_mixed_kernel_r81/README.md`、
`flat_shadow_mixed_kernel_r81/audit_r81.py`。

## 79. R82：exact degree-local mixed kernel 的 actual obstruction（2026-09-07）

R82 网页端完成了完整 mixed kernel 推导，但最终仍报告桥接账户连接错误，
没有实际读取 R81 本机文件或独立核验 `1a3839f`；本机按形式
same-factor/Jacobi hierarchy 记录，并对首个通道做精确有理审计。

令 `c_j=(j!)^2/(2j+1)!`、`o_(2j+1)=c_jZ_j`，且
`U(z)=sum upsilon_r z^(2r+1)`，其中
`upsilon_r=(-1)^(r-1)r(r+1)!/[2(2r+1)!]`。若
`C_(p,q)=average sum_(i<j)r_i^pr_j^q`，则
`o -> A_e^(-1)Q(U,o)` 的 finite/formal 系数核为
`M_(m,j)=c_j upsilon_(m-j-1)
[C_(2m-2j-1,2j+1)+C_(2j+1,2m-2j-1)]/[2A_(2m)]`
（`m>=j+2`，否则为零）。

Gaussian diagonal 的 tangent derivative 使用
`q_0=q_1=0`、`q_2=-H_1`、`q_3=-H_0`、
`q_(ell+1)=xq_ell-ell q_(ell-1)`，并令
`P_ell=H_(ell+1)q_ell-ell H_ell q_(ell-1)`。若
`P_ell=sum_(m<ell)p_(ell,m)H_(2m)`，则
`R_(ell,m)=-2(2m)!p_(ell,m)/(ell!)^2`。结合 corrected signed Green
`sum_(k>=ell)G_(k,ell)x^k=e^(-x)x^ell
-2e^(-2x)integral_0^x e^t t^ell dt`，得到完整 kernel
`K_(k,j)^(n)=sum_(ell=j+3)^kG_(k,ell)
sum_(m=j+2)^(ell-1)R_(ell,m)M_(m,j)`，`n` 只负责截断。

本机对固定 `j=0,1,2,4` 精确核验了两个首通道。第一，`d=3`：
`K_(j+3,j)=2(j+6)/[3(j+1)(j+2)(j+3)^2]`
`=2/(3j^3)+O(j^(-4))`，所以 `n^3K_(j+3,j)` 在 `j/n->theta` 时
有有限极限 `2/(3theta^3)`，与 weighted criterion 相容。

第二，`d=4` 的两条 direct source path 加上一阶 Green 回传后精确给出
`K_(j+4,j)=-(3j^3+146j^2+1001j+1560)
 /[15(j+1)(j+2)(j+3)^2(j+4)^2]`
`=-1/(5j^3)+O(j^(-4))`。因此在 `j/n->theta>0` 时
`n^4K_(j+4,j)=-n/(5theta^3)+O(1)`，实际 canonical `d=4` 通道已经
否定 R81 所需的 `n^dK_(j+d,j)=O(1)`。

对 R81 权重
`omega_(n,j)=((j!)^2/(2j+1)!) (4sqrt(n))^(2j+1)`，固定 gap 比值为
`omega_(n,j+d)/omega_(n,j)~(4n)^d`。故 `d=4` 单列贡献为
`|K_(j+4,j)|omega_(n,j+4)/omega_(n,j)
~256n/(5theta^3)`；取 `j=floor(n/2)` 得
`||K_n||_(ell^1(omega_n)) >=(2048/5+o(1))n`。所以
`MGK(C_K)` 的 n-一致 `O(1)` 版本在 actual canonical kernel 中严格为假，
不是 arbitrary-matrix no-go。

还有一个更强的单半径不相容性。若 `R_n=cn^alpha`，actual `d=4` 通道
要求 mixed-kernel uniformity 至少满足 `alpha<=3/8`；但
`H_4H_n=...+6n(n-1)H_n+...` 使 degree-four Gram compression 需要
`n^2R_n^(-4)=O(1)`，即 `alpha>=1/2`。因此同一个 power-radius
coefficient-Wiener norm 不可能同时给出 dimension-free Gram control 与
actual mixed-kernel uniformity。

这不意味着 R81 路线无效：当前实际 lower bound 只有 `cn`。若能证明完整
all-gap kernel 仅有 `O(n^p)`，则在 R80 已有指数 shrinking 的窗口中，
mixed linear loop 仍可能是 tame；若 growing-gap family 产生指数下界，才
需要切换 hybrid Gram/triangular operator space。下一目标是 R83：保留 gap
generating function，判定 full all-gap growth，而不再追求已被 d=4 否定的
uniform `O(1)`。

新增本机记录与审计：`flat_shadow_exact_mixed_kernel_r82/README.md`、
`flat_shadow_exact_mixed_kernel_r82/audit_r82.py`。

## 80. R83：all-gap mixed-kernel growth 与固定-gap生成函数（2026-09-07）

R83 网页端继续报告桥接无法读取 R82 本机文件，因此本节严格区分形式
same-factor/Jacobi 层级推导与本机审计范围。网页端从 R82 的 exact kernel
出发，保留 gap、Hermite band 与 signed Green 回传，得到固定 gap 的统一主项。

令 `r>=1`、`m=j+r+1`，root-of-unity filter 给出 mixed angular ratio
`B_(r,j)=-1/(2*4^r)+O_r(j^(-1))`，故
`M_(j+r+1,j)=c_j upsilon_r B_(r,j)`。同时，`q_ell` 的 exact Hermite band
系数为
`Q_(ell,a)=(-1)^(a+1)(a+1)(a+2)[a^2+5a-2(ell-3)]
 (ell-a-4)!/[2(ell-3-2a)!]`，并由 Hermite product formula 得到
`p_(ell,ell-s)=2ell^(2s-2)/(s-1)!+O_s(ell^(2s-3))`。

signed Green 的 exact gap coefficient 为
`G_(ell+g,ell)=(-1)^g/g!
-2sum_(u=0)^(g-1)(-2)^(g-1-u)/[(g-1-u)!u!(ell+u+1)]`。
固定 gap 时其 leading generating factor 是 `exp(-z)`；source band 的求和给出
`exp(z)`，两者精确抵消。于是形式 fixed-gap theorem 为
`K_(j+d,j)=kappa_d j^(-3)+O_d(j^(-4))`，其中
`kappa_d=2(-1)^(d-1)(d-2)(d-1)!/(2d-3)!`，所有 `d>=3` 均非零。

其 gap generating function为
`sum_(d>=3)kappa_d z^d=4z^(3/2)U(sqrt(z))`
`=4z^3 integral_0^1 q_s exp(-q_s z)(1-q_s z/2)ds`，并有
`sum_d4^d|kappa_d|<infinity`。因此 R82 的 `d=3`、`d=4` 通道只是这一
完整 fixed-gap profile 的前两项，而不是孤立异常。

对 R82 权重 `omega_(n,j)=((j!)^2/(2j+1)!)(4sqrt(n))^(2j+1)`，若
`j/n->theta in (0,1)`，则单个固定 gap 的 weighted channel为
`4^d|kappa_d|theta^(-3)n^(d-3)(1+o(1))`。由于每个固定 `d>=3` 的
`kappa_d` 非零，对任意固定 `p` 取 `d>p+3`，便得到当前 weighted mixed
norm 快于 `n^p` 的严格 lower-growth 结论。这里不能把 fixed-gap 结果偷换
成 `d=d(n)`，所以尚未得到 exponential lower bound；`d/j->delta>0` 与
uniform moderate-gap remainder 仍 OPEN。

路线判断发生了实质更新：当前 `4sqrt(n)` coefficient-Wiener norm 不仅
无法给出 `O(1)` MGK，也无法给出任意固定 polynomial bound。将权重乘以
`n^(-j)` 可消除 fixed-gap 的 `n^d` 因子，并保留可求和的 `4^d|kappa_d|`，
但该 rescaling 不能单独承担 Gram/strict-triangular stability。因此更合理
的下一步是 hybrid Gram + triangular + rescaled-coefficient norm，并首先证明
`d=o(sqrt j)` 的 uniform moderate-gap theorem，或从 proportional-gap saddle
point 提取真实 rate function。

本机新增：`flat_shadow_all_gap_r83/README.md`、
`flat_shadow_all_gap_r83/audit_r83.py`。审计以 exact rational arithmetic
核验 root filter、Hermite band、Green coefficient、`d=3..8` 的 fixed-gap
主项与生成函数 Taylor 系数；不将这些有限核验冒充 proportional-gap 证明。

严格边界：R80 safe window 尚未改善；D.1、全局 positivity、positive infinite
exact backward tower、backward OU divisibility、endpoint `FS_3` 以及
proportional-gap regime 继续 OPEN。

## 81. R84：uniform logarithmic moderate-gap theorem（2026-09-07）

R84 将 R83 的 fixed-gap 结论推进到真正增长的 gap。网页端本轮已实际读取
R83 framework、worklog、README 与 audit；它仍把 uniform analytic estimates
放在 formal same-factor/Jacobi hierarchy 内，本机审计只接受 exact algebraic
block、有限锚点与算术边界，不把未展开的常数估计冒充完整证明。

角向 root-filter 可写成 central coefficient 的复数 saddle 表示。形式上在
`r<=log(j)/16` 时得到相对误差 `O(r^2/j)`；Hermite top band 在
`s=O(log ell)` 时给出相对误差 `O(s^2/ell)`；signed Green 则有 exact
positive integral
`G_(ell+g,ell)=(-1)^g/g![1+2g integral_0^1t^ell(2-t)^(g-1)dt]`，
且 `g<=ell/2` 时无 `3^g` 损失。

单路径的共同主项仍是 `j^(-3)`。但 source 的 `exp(z)` 与 Green 的
`exp(-z)` cancellation 对误差有 condition number；R84 正确保守为
`|j^3K_(j+d,j)/kappa_d-1|<=C(d^2/j)e^(8d)`，不能未经额外高阶抵消
直接写成 `exp(O(d^2/j))`。因此在 `3<=d<=log(j)/16` 内得到形式上的
uniform theorem
`K_(j+d,j)=kappa_d j^(-3)[1+O((log j)^2/sqrt(j))]`，其中
`kappa_d=2(-1)^(d-1)(d-2)(d-1)!/(2d-3)!`。

取 `j=floor(n/2)`、`d_n=floor(c log n)+3`、`0<c<1/16`，原
`4sqrt(n)` Wiener 权重由单个 actual channel 给出
`||K_n||>=exp[c_*(log n)^2-c_*(log n)loglog n-C_*log n]`。
这是真正的 stretched-superpolynomial lower bound，虽仍为 `e^(o(n))`，
不能宣称 exponential-in-n。与此同时，`tilde omega_(n,j)=n^(-j)omega_(n,j)`
在整个 logarithmic moderate-gap sector 将权重比降为
`4^d exp(O(d^2/j))`，结合 `sum_d4^d|kappa_d|<infinity`，该 sector 的
rescaled coefficient propagation uniformly tame；Gram/triangular stability
和 proportional-gap 仍未解决。

本轮还发现一个必须修正的简单参数错误。若 `delta=j/r`，比例 saddle 中正确
参数为 `rho=r/(j+r)=1/(1+delta)`；若 `delta=r/j`，则
`rho=delta/(1+delta)`。它满足
`Psi'_rho(x)=0 <=> 1+(1-omega)(2rho-1)x-omega x^2=0`。
网页输出的 `rho=(1+delta)/delta` 与该方程不一致，本机记录采用修正版。
角向 saddle 仍只是 proportional-gap exact reduction，尚未与 source/Hermite
和 Green phase 组合成 full kernel rate function。

本机新增 `flat_shadow_moderate_gap_r84/README.md`、
`flat_shadow_moderate_gap_r84/audit_r84.py`；审计通过 root-filter、修正版
saddle、Green integral、fixed-gap anchors、hybrid weight 与 stretched exponent。
R80 safe window、D.1、global positivity、positive infinite exact backward tower、
backward OU divisibility、`FS_3` 以及 proportional-gap 继续 OPEN。

## 82. R85：proportional-gap joint saddle 与 signed-cancellation 边界（2026-09-07）

R85 将增长 gap 推进到 `d/j -> delta>0`，但明确保持“full signed kernel 的上界”与
“实际 lower/equality”之间的边界。网页端在 formal same-factor/Jacobi hierarchy 中从
R82 exact simplex decomposition 出发，分别保留 angular root-filter、Hermite/source
band、signed Green 三条 leg，得到
`limsup_j j^(-1) log(j^d |K_(j+d,j)|) <= delta(1+log(3/delta))`。
也就是
`|K_(j+d,j)| <= j^(-d) exp(j*delta(1+log(3/delta))+o(j))`。

这条 bound 是 full `K` 的一侧 bound，而不是从 modulus 最大路径得到的 lower。它直接
推出原 `4sqrt(n)` 权重下 proportional channel 至多 exponential-in-`n`；若把系数权重
再乘 `n^(-j)`，则固定 `delta>0` 的 channel 在 `j log j` 尺度上严格为负，因而
super-exponentially tame。于是 hybrid coefficient route 没有被 proportional sector
否定，但 full Gram/triangular 稳定性仍未由此获得。

R85 的三个结构块如下。第一，若 `rho=r/(j+r)`，angular saddle 方程为
`1+(1-omega)(2rho-1)x-omega x^2=0`；若写 `delta=j/r`，则
`rho=1/(1+delta)`，若写 `delta=r/j`，则 `rho=delta/(1+delta)`。第二，
`G_(ell+g,ell)=(-1)^g/g![1+2g integral_0^1 t^ell(2-t)^(g-1)dt]`，其
interior rate 为
`J_G(L,gamma)=L log(2L/(L+gamma))+gamma log(2gamma/(L+gamma))`，且在约束
`L=1+delta-gamma` 下导数为 `log(gamma/L)`。第三，比例 source band 的 endpoint
sum 给出非零 prefactor
`p_(ell,ell-s)/T_0 -> (1-lambda)/(1+lambda)^3`，其中
`T_0=2(s-1)! binom(ell+1,s-1)binom(ell-3,s-1)`；因此 Hermite/source
交错和本身没有把 proportional leg 指数级消掉。

丢掉 angular decay 后，三变量实 simplex 上的 absolute action 最大值是
`delta(1+log(3/delta))`。在 Green interior branch 令 `a=alpha+beta` 并先取
`alpha=beta=a/2`，约束导数明确为 `log(2(1+a)/a)>0`，所以该 branch 只能在
`gamma=L` 边界达到最大；随后由三项 entropy 的等分最大性得到上述上界。

真正的 obstruction 也被压缩成严格命题：signed phase 在 `gamma<L` 时要求
`log(beta/gamma)+i*pi=0`，在 `gamma>L` 时要求 `log(beta/L)+i*pi=0`；两者都不可能
在 positive-real simplex 上成立。因此 modulus saddle 不能直接给 actual exponential
lower。形式 complex cancellation `gamma=-beta` 再强迫 `alpha=delta`，指向 candidate
rate `delta(1-log(delta))+Lambda_A(delta)`，但还缺 `PSC_delta`：合法 contour deformation、
无更大 Stokes 项、conjugate angular saddle 无指数级抵消且前因子非零。`PSC_delta`、
actual proportional lower/equality、mesoscopic `log(j)<<d<<j`、full hybrid
Gram/triangular norm、R80 safe-window improvement、D.1、global positivity、positive
infinite backward tower、backward OU divisibility 与 `FS_3` 继续 OPEN。

本机新增 `flat_shadow_proportional_saddle_r85/README.md` 与
`flat_shadow_proportional_saddle_r85/audit_r85.py`。审计以 exact rational/symbolic
方式通过 root-filter 与 corrected saddle、signed Green rate/phase obstruction、source
endpoint finite anchors、source–mixed proportional prefactor anchors、entropy optimization
和 rescaled weight arithmetic；不把网页端未逐行展开的 uniform saddle remainder 或
`PSC_delta` 冒充已证明结论。

## 83. R86：exact Green-resummed generating identity 与 endpoint correction（2026-09-07）

R86 的第一步可以在 exact finite/formal 层级闭合。定义
`R_m(z)=sum_(s>=1)R_(m+s,m)z^s`，
`S_j(z)=sum_(r>=1)M_(j+r+1,j)z^(r+1)R_(j+r+1)(z)`，则
`[z^h]S_j(z)=sum_(m=j+2)^(j+h-1)R_(j+h,m)M_(m,j)`，并且完整 mixed kernel 的
gap generating series 满足
`K_j(z)=e^(-z)S_j(z)-2ze^(-2z)integral_0^1e^(zu)u^jS_j(zu)du`。
因此 `[z^d]K_j(z)=K_(j+d,j)`。本机用 exact rational finite blocks 对多个 `j,d`
逐项核验了该 identity 与旧的 `exact_K` 完全一致；这一步把 signed `s/g`
convolution 真正折叠为单一 entire/formal operator。

第一 Green 项在 `r/j->alpha`、`s/j->beta`、`d/j->delta`、`z=jzeta` 下的 action 为
`Phi_1=Phi_A(alpha)+alpha+beta-alpha log alpha-beta log beta`
`+(alpha+beta-delta)Log zeta-zeta`。其 `beta,zeta` stationary equations 为
`beta=zeta` 与 `zeta=alpha+beta-delta`，所以自动给出 `alpha=delta`、
`gamma=delta-alpha-beta=-beta`。这里 `Phi_A` 必须包含 root-filter 外部相位
`2alpha Log(omega)`；只取实部会破坏 signed phase bookkeeping。第二 Green 项的
formal action 给出
`zeta=-gamma/(2-u)=-L/u`、`u_*=2L/(L+gamma)`，其中 `L=1+alpha+beta`，
且 `u_*=1` 正好是 `gamma=L` 的 Green transition。

本轮钉死了一个前因子修正。若 `u=1` endpoint branch 合法，
`integral_0^1e^(zu)u^(Lj)du ~ e^z/[j(zeta+L)]`，故两项 Green 合并因子是
`P_G=1-2zeta/(L+zeta)=(L-zeta)/(L+zeta)`，而不是其倒数。形式 PSC 点
`alpha=delta,beta=zeta,L=1+delta+zeta` 的前因子为
`P_G^PSC=(1+delta)/(1+delta+2zeta)`。本机 exact audit 已验证这一化简；但不把
它升级为“endpoint contour 一定占优”，因为 endpoint legality 仍是 PSC 缺口。

因此 R86 目前交付的是：exact Green-resummed identity、corrected complex saddle
equations、Green endpoint factor correction，以及 `g<j` 区间的 factorial-majorant
算术（`|G|<=C_epsilon/g!` 的积分比较和
`sum_{r+s+g=D}1/(r!s!g!)=3^D/D!`）。尚未证明 complex source endpoint continuation、
Green endpoint/interior separation、angular conjugate phase control 或完整 `PSC_delta`；
candidate rate `delta(1-log delta)+Phi_A(delta)` 仍为 conditional。下一步应围绕这些
缺口推进，或把 factorial-majorant 补成 all-gap `n^(-j)` rescaled upper，而不是把
形式 saddle 当成 actual lower。

本机新增 `flat_shadow_green_resummed_r86/README.md` 与
`flat_shadow_green_resummed_r86/audit_r86.py`。审计通过
`R86_EXACT_GREEN_RESUMMED_IDENTITY_PASSED`、
`R86_CORRECTED_SADDLE_AND_PHASE_BOOKKEEPING_PASSED`、
`R86_GREEN_ENDPOINT_FACTOR_CORRECTION_PASSED`、
`R86_MESOSCOPIC_FACTORIAL_MAJORANT_ARITHMETIC_PASSED` 与
`R86_GREEN_RESUMMED_AUDIT_COMPLETED`；没有使用扫描、行列式、优化器或远程计算。

## 84. R87：small-proportional safety window audit and endpoint corrections（2026-09-07）

R87 网页端提出了两轨路线：先尝试小比例 `PSC_delta`，若 complex source/phase 仍不能闭合，则切换到 `n^(-j)`-rescaled coefficient 的 mesoscopic factorial upper。网页方案的方向有价值，但本机逐项审计发现其中的端点因子在不同段落出现了互为倒数的写法，故本轮只提交修正后的代数层结论。

令 `omega=exp(2*pi*i/3)`、`rho=alpha/(1+alpha)`，取 root-filter saddle `x(0)=1` 的解析分支。因为 `P_x(0,1)=-(1+omega)!=0`，隐函数定理给出局部非退化分支。完整 angular phase 的 envelope derivative 为 `Phi_A'=2*Log(omega*(1+omega*x))-Log(x)-2*log(2)`，所以 PSC stationary 参数满足 `zeta=4*alpha*x/(omega^2*(1+omega*x)^2)=4*alpha+O(alpha^2)`。从而 `L=1+alpha+zeta`、`Delta=L+zeta=1+alpha+2*zeta` 满足 `Delta=1+9*alpha+O(alpha^2)`。

source proportional endpoint 的参数必须是 `lambda=zeta/L`（不是 `L/zeta`）。因此 `P_H=(1+lambda)^3/(1-lambda)=Delta^3/((1+alpha)L^2)`。R86 已经钉死的 Green 端点因子仍是 `P_G=1-2*zeta/(L+zeta)=(L-zeta)/(L+zeta)=(1+alpha)/Delta`，而不是其倒数。正确乘积为 `P_H P_G=Delta^2/L^2`；网页 R87 中出现的 `Delta^4/((1+alpha)^2L^2)` 正是误用倒数后的乘积。本机记录以正确式为准。

在 `Re(Delta)>=eta>0` 的小比例安全窗内，实 `u` 段的局部 Green exponent `phi(u)=zeta*u+L*Log(u)` 满足 `Re(phi'(u))=Re(Delta)+(1/u-1)Re(L)>=eta`，故 `u=1` 是原始实段的唯一端点最大值；但这仍需 uniform source amplitude bounds 才能升级成 endpoint Laplace theorem。

网页 R87 的 conjugate-phase lemma 也需补充非退化条件：`C!=0` 单独不够，因为 `Theta=0` 且 `C` 纯虚时两共轭主项恒等相消。应要求 `Theta notin pi*Z` 或 `Re(C)!=0`，然后才可从 Cesàro 平方均值推出 limsup lower。

fallback 的有限算术已核验 `sum 1/(r!s!g!)=3^D/D!`，但 angular bound 中的 `(1+r)^2` 会留下显式 `(1+D)^2` 多项式因子；因此 R87 的固定 `q=6` 形式不能由三条目标不等式直接推出，必须重新校准 polynomial prefactor。

本轮新增 `flat_shadow_green_region_r87/README.md` 与 `audit_r87.py`。审计通过 angular branch/zeta、endpoint correction、Green endpoint derivative、conjugate non-degeneracy 与 fallback multinomial arithmetic；不把 PSC、source analytic continuation 或 uniform upper 写成已证定理。整体主线仍是：先关闭 rescaled coefficient propagation，再处理 hybrid Gram/triangular stability；positive backward tower、OU divisibility、global positivity 与 `FS_3` 仍在更高层开放。

## 85. R88：带显式余项的 real-`u` endpoint lemma（2026-09-07）

R88 选择了 A 路，先把 Green 的实积分从 PSC 的复 contour 问题中剥离出来。对
`phi(u)=zeta*u+L*Log(u)`、`Delta=L+zeta`，假设参数集上
`Re(Delta)>=eta>0`、`Re(L)>=ell_0>0`，并给定 normalized source amplitude
`A_j in C^1([0,1])` 满足 `||A_j||_{C^1}<=M`，则一次分部积分给出真正的抽象定理
`integral_0^1 exp(j*phi(u))A_j(u)du = exp(j*zeta)A_j(1)/(j*Delta)+R_j`，且
`|R_j| <= (M/eta)(1/c+L_max/c^2) exp(j*Re(zeta))/j^2`，其中
`c=min(eta,ell_0)`。证明只用
`B_j=A_j/phi'=A_j*u/(zeta*u+L)`、
`B_j'=A_j'*u/(zeta*u+L)+A_j*L/(zeta*u+L)^2`，以及
`Re(phi'(u))=Re(Delta)+(1/u-1)Re(L)>=eta`；下端点因 `Re L>0` 消失。

若另有 `|A_j(1)|>=m>0`，可将余项写成相对 `1+O(j^(-1))`。代回 R86 exact
Green operator 后得到 analytic realization of the corrected factor
`P_G=1-2*zeta/Delta=(L-zeta)/(L+zeta)=(1+alpha)/Delta`。与仍属 conditional
的 source endpoint `P_H=Delta^3/((1+alpha)L^2)` 拼接时，正确乘积仍是
`P_H P_G=Delta^2/L^2`。

这一轮真正关闭的是“给定 uniform amplitude 假设的 endpoint theorem”，不是 actual
source 的复延拓。要把它升级为 PSC，仍需证明：actual source amplitude 的 uniform
`C^1` 控制及端点非零、`z`-Cauchy contour 的合法变形与 Stokes 排除、angular
conjugate branch 的非退化 limsup。因而本轮不宣称 proportional lower/equality。

本机新增 `flat_shadow_endpoint_lemma_r88/README.md` 与 `audit_r88.py`。审计通过
endpoint differentiation、endpoint geometry、explicit remainder constant、corrected
Green factor 与 lower-boundary bookkeeping；`py_compile`、`git diff --check` 通过。

## 86. R89：source factorization、moving-saddle obstruction 与 conditional absolute majorant（2026-09-07）

R89 对 R88 的 uniform-amplitude 假设做了正确的压力测试。定义
`T_(m,s)=2(s-1)! binom(m+s+1,s-1)binom(m+s-3,s-1)` 与无除法的
`Xi_(m,s)=p_(m+s,m)/T_(m,s)`，则 exact source 公式严格化简为
`R_(m+s,m)=-4(2m)!/((m+2)!(m-2)!) * (m+s+1)/((m+s)(m+s-1)(m+s-2)) * Xi_(m,s)/(s-1)!`。
本机 exact rational blocks 已逐项核对。若使用 `Theta=T/Xi` 的记号，则 source 中应出现 `1/Theta`；因此本轮统一使用 `Xi`，避免与网页端 source factor 的正反定义混淆。

由此 `R_m(z)` 可形式地写成 `-C_m z e^z E[D_(m,N+1)Xi_(m,N+1)]`，其中
`C_m=4(2m)!/((m+2)!(m-2)!)`、`D_(m,s)=(m+s+1)/((m+s)(m+s-1)(m+s-2))`、`N~Poisson(z)`；这是 coefficient-by-coefficient 的 formal identity，不是复 source asymptotic。

本轮又纠正一个敏感代数点。令 `y=omega*x`、`q=exp(-i*pi/6)`、`y=qv`，saddle 方程化为
`v^2-sqrt(3)(2rho-1)v+1=0`。实 `alpha>=0` 的连续分支满足 `|y|=1`、`arg(y) in [0,2*pi/3]`，并且把已审计的
`zeta=4*alpha*x/(omega^2(1+omega*x)^2)` 代入后得到
`zeta=4*alpha*y/(1+y)^2=alpha/cos(arg(y)/2)^2>0`。
网页 R89 某段写成 `4*alpha(1+y)^2/y`，这是倒数错误；虽然在 `alpha=0` 的首阶展开上看不出来，本机 audit 已拒绝该式。

固定 endpoint saddle 的 fully-resummed source normalization 在 leading model
`R_m(z) proportional to z e^z` 下满足
`A_src^(0)(u)=u^(1-(alpha+zeta)j)exp(j*zeta(u-1))`，故
`log|A_src^(0)(u)|=j[zeta(u-1-log u)-alpha log u]+log u`。
对固定 `0<u<1`、实 `zeta>0`，主指数严格为正。这给出一个结构性 no-go：R88 的 global frozen-saddle `C^1` amplitude 假设不能直接套在 fully-resummed source 上。它否定的是该归一化方式，不是否定 PSC；后续必须采用 moving source saddle、endpoint boundary layer 或 absolute majorant。

若另行证明 `|Xi_(m,s)|<=C exp(C s^2/m)`，则 exact factorization、`D_(m,s)<=9/m^2` 与 R87 angular/Green 目标不等式条件性推出
`|K_(j+D+1,j)| <= C j^(-3)(1+D)^3 3^D/D! exp(CD^2/j)`。
其中 `(1+D)^3` 的三次来源已明确：angular 的 `(1+r)^2` 与 source 的
`1/(s-1)!=s/s!`。这仍是 conditional target，因为 source band、angular band 和 uniform Green majorants 尚未全部证明。

rescaled coefficient weight 的 exact ratio 为
`tilde omega_(n,j+D)/tilde omega_(n,j)=16^D c_(j+D)/c_j`
`=16^D prod_(h=1)^D(j+h)^2 / prod_(h=1)^(2D)(2j+1+h)`，成对化简为
`prod_(h=1)^D 8(j+h)/(2(j+h)+1)<4^D`。因此一旦 conditional kernel upper 真实闭合，weighted target 只增加 `12^D`，factorial 从 `D~C log j` 起可吞掉显式多项式因子。

本机新增 `flat_shadow_source_majorant_r89/README.md` 与 `audit_r89.py`。审计通过 exact source factorization、Poisson coefficient bookkeeping、corrected zeta substitution、leading-model no-go、source majorant arithmetic 与 rescaled weight ratio；R89 不宣称 actual source majorant、PSC 或 proportional lower。

## 87. R90：corrected exact source-band majorant（2026-09-07）

网页端 R90 找到了一个真正可能关闭 source leg 的局部定理：对 `m>=8`、
`1<=s<=m/8`，有 `|Xi_(m,s)|<28`。本机复核发现网页展示的归一化 factorial
比值方向写反：按网页字面代入 `a=0` 会得到 `A_(m,s,0)=(m+s-3)^2`，
而不是其同时要求的 `A_(m,s,0)=1`；source 中 central-binomial 上界的分子分母
也必须按 exact R factorization 取倒数。故本轮没有盲目接受网页式子，而是从 R83
`p_band_formula` 重新化简并审计修正版。

令 `ell=m+s`，则正确的两组归一化项为

`A_(m,s,a)=(-1)^(a+1)(a+1)(a+2)/4`
`*[a^2+5a-2ell+6]*(ell-a-4)!/(ell-3)!`
`*(s-1)!/(s-a-1)!*(m+2)!/(m+a+2)!*(m-2)!/(m-a-2)!`，

`B_(m,s,a)=(-1)^(a+1)(a+1)(a+2)/4`
`*[a^2+5a-2ell+8]*ell/(ell+1)*(ell-a-5)!/(ell-3)!`
`*(s-1)!/(s-a-2)!*(m+2)!/(m+a+2)!*(m-2)!/(m-a-2)!`。

这些式子与 exact R83 finite band 逐项一致，且 `A_(m,s,0)=1`。在
`q=s/(m-2)<=1/6` 下，有限乘积给出
`|A_(m,s,a)|<=(a+3)^4 q^a/8`、
`|B_(m,s,a)|<=(a+4)^4 q^(a+1)/8`；关键是
`(m+2)!/(m+a+2)!*(m-2)!/(m-a-2)!<=1`，而不是网页中倒置后声称的
contraction。精确几何和为 `681843/25000<28`，因此 source theorem
`|Xi_(m,s)|<28` 在该 mesoscopic source band 上成立。

再用 exact R89 factorization、`D_(m,s)<=9/m^2` 及
`(2m)!/((m+2)!(m-2)!)<=4^m/sqrt(m)`，得到实际显式 bound

`|R_(m+s,m)|<=1008*4^m*m^(-5/2)/(s-1)!`
`=1008*4^m*m^(-5/2)*s/s!`。

权重方面，R89 文本中的 denominator index 也需修正。对
`c_j=(j!)^2/(2j+1)!`，有全局精确式
`tilde omega_(n,j+D)/tilde omega_(n,j)=16^D c_(j+D)/c_j`
`=prod_(h=1)^D 8(j+h)/(2(j+h)+1)<4^D`；若卷积输出是
`K_(j+D+1,j)`，应用时把 gap 换成 `D+1`。

本机新增 `flat_shadow_source_majorant_r90/README.md` 与 `audit_r90.js`。
BigInt 有理审计通过：`R90_CORRECTED_A_B_FORMS_PASSED`、
`R90_LITERAL_WEB_FORM_REJECTED`、`R90_UNIFORM_TERM_AND_XI_ANCHORS_PASSED`、
`R90_EXACT_GEOMETRIC_SUM_PASSED`、`R90_EXPLICIT_SOURCE_BOUND_ANCHORS_PASSED`、
`R90_WEIGHT_PRODUCT_AND_BOUND_PASSED` 与
`R90_CORRECTED_SOURCE_MAJORANT_AUDIT_COMPLETED`。因此状态实质更新为：
source leg 在上述小比例 band 上 **PROVED**；angular、uniform Green、full
kernel 拼接、PSC moving saddle、比例下界/等式及更高层 positive tower/OU/`FS_3`
仍 OPEN 或 CONDITIONAL。

## 89. R92：global source polynomial bound and all-gap rescaled closure（2026-09-07）

R92 没有把 R85 的 proportional saddle `o(j)` 强行升级成 compact-uniform
估计，而是从 R90 修正版的 exact `A/B` finite sums 取一个粗但全局的 bound。
R83 binomial support 强制每个非零项满足 `a<=m-2`。对 `m>=3`，corrected
`m`-factor product 不超过 1；剩余 factorial 比值配对后，对 `s>=2` 的 A 组和
`s>=3` 的 B 组分别可压到 `1/(s-1)`、`1/(s-2)`，而多项式因子至多为
`4*ell^2` 量级。计数项数并单独处理 `s=1,2`，得到全带 actual theorem

`|Xi_(m,s)|<=16*(m+s)^4`，`m>=3,s>=1`。

结合 R89 exact factorization、`D_(m,s)<=9/m^2` 和正确方向的
`(2m)!/((m+2)!(m-2)!)<=4^m/sqrt(m)`，得到
`|R_(m+s,m)|<=576*4^m*m^(-5/2)*(m+s)^4*s/s!`。

Green exact coefficient 可全局分解为
`|G_(ell+g,ell)|<=1/g!+2^g/((ell+1)(g-1)!)`（`g>=1`，`g=0` 时 `G=1`）。
与 R91 global angular bound 及 exact convolution 拼接后，对 `j>=1,D>=2` 有

`|K_(j+D+1,j)|<= (256/3)j^(-3)(j+D+1)^4`
`*D(D^2+6D+2)3^D/D!`
` +18j^(-3)(j+D+1)^3`
`*D(D-1)(D^2+7D-2)4^D/D!`。

两个 polynomial 都来自精确生成函数：第一项为
`(x^2+3x+1)e^x * x e^x * e^x`，第二项为
`(x^2+3x+1)e^x * x e^x * 2x e^(2x)`。没有把大 gap 的 source 或 Green
当作 fixed-gap 渐近外推。

R90 的 global weight inequality `<4^(D+1)` 使 weighted terms 仅增加
`12^D/D!`、`16^D/D!`。在 `D>=j/8` 时 `j<=8D`、`j+D+1<=10D`，
故 tail 被可求和序列 `C D^7 16^D/D!` 控制；R91 已证明的 `D<=j/8`
区间负责其余部分。于是 exact mixed-kernel decomposition 的
`n^(-j)`-rescaled coefficient column 全 gap 有界：

`sup_(n,j>=1) sum_k |K_(k,j)^(n)|*tilde omega_(n,k)/tilde omega_(n,j)<infinity`。

本机新增 `flat_shadow_global_tail_r92/README.md` 与 `audit_r92.js`。
BigInt 有理审计通过 `R92_GLOBAL_SOURCE_ANCHORS_PASSED`、
`R92_GLOBAL_GREEN_BOUND_ANCHORS_PASSED`、
`R92_GLOBAL_CONVOLUTION_IDENTITIES_PASSED`、`R92_TAIL_ARITHMETIC_PASSED` 与
`R92_GLOBAL_TAIL_AUDIT_COMPLETED`。R92 期间还明确拒绝网页端 central-binomial
分式倒置写法；状态因此更新为：rescaled coefficient propagation 已全 gap
**PROVED**，下一主瓶颈转移到 hybrid Gram/strict-triangular stability，随后
才是 PSC lower/equality、global positivity、positive backward tower、OU
divisibility 与 `FS_3`。

## 88. R91：mesoscopic angular/Green/full-kernel closure（2026-09-07）

R90 已把 source theorem 关闭在 `m>=8`、`s<=m/8`。R91 网页端进一步给出两条
可以直接和该窗口拼接的 elementary estimates。本机复核发现其 central-binomial
induction 的 ratio 也写反了一次：正确的是
`a_(k+1)/a_k=(2k+1)/(2k+2)`，并由
`(2k+1)^2-4k(k+1)=1` 得到
`C(2k,k)>=4^k/(2 sqrt(k))`。修正后，R83/R87 exact root-filter formula
`M_(j+r+1,j)=c_j upsilon_r B_(r,j)` 给出全局 angular upper

`|M_(j+r+1,j)|<=4^(-j-r) j^(-1/2) (r+1)^2/r!`，

因为 root-filter probability 的 `rho` 落在 `[0,3]`，故 `|B|<=1`，而
`c_j=(j!)^2/(2j+1)!` 与 `|upsilon_r|` 分别由同一 central-binomial lower bound
控制。

Green 部分不需要 R88 的 amplitude 或 PSC contour 假设。R83/R86 exact coefficient
为
`G_(ell+g,ell)=(-1)^g/g!*[1+2g integral_0^1 t^ell(2-t)^(g-1)dt]`。
由 `t(2-t)<=1` 得积分不超过 `1/(ell-g+2)`。在共同窗口
`D=r+s+g<=j/8`、`ell=j+r+s+1` 下，`ell>=j+3`、`g<=j/8`，从而
`2g/(ell-g+2)<2/7`，即
`|G_(ell+g,ell)|<=9/(7g!)`。

现在令 `D=r+s+g`。当 `j>=16`、`2<=D<=j/8` 时，每条非空路径都满足
`m=j+r+1>=8`、`s<=D<=j/8<=m/8`，所以 R90 source theorem 可逐路径应用。
三条已证上界给出单路径
`|GRM|<=5184*j^(-3)(r+1)^2*s/(r!s!g!)`。利用精确生成函数
`sum_r (r+1)^2x^r/r!=(x^2+3x+1)e^x`、
`sum_s sx^s/s!=xe^x`，有

`sum_(r+s+g=D)(r+1)^2s/(r!s!g!)`
`=(3^D/D!)*D(D^2+6D+2)/27`。

因此 exact mixed-kernel 分解在整个区间 `2<=D<=j/8` 上满足真正的 theorem

`|K_(j+D+1,j)|<=192*j^(-3)*D(D^2+6D+2)*3^D/D!`。

再用 R90 已证的全局权重比
`tilde omega_(n,j+D+1)/tilde omega_(n,j)<4^(D+1)`，得到区间级的
rescaled column bound

`sum_(2<=D<=j/8)|K_(j+D+1,j)|`
`*tilde omega_(n,j+D+1)/tilde omega_(n,j)`
`<=2405376*e^12*j^(-3)`。

本机新增 `flat_shadow_mesoscopic_kernel_r91/README.md` 与 `audit_r91.js`。
BigInt 有理审计通过 `R91_CENTRAL_BINOMIAL_INDUCTION_PASSED`、
`R91_ANGULAR_MAJORANT_ANCHORS_PASSED`、`R91_GREEN_WINDOW_BOUND_PASSED`、
`R91_CONVOLUTION_IDENTITY_AND_CONSTANTS_PASSED` 与
`R91_MESOSCOPIC_KERNEL_AUDIT_COMPLETED`。所以状态实质更新为：source、global
angular、共同窗口 Green，以及 `D<=j/8` 的 full kernel/weighted column 均
**PROVED**（基于已有 exact decomposition）；真正剩余的 coefficient-propagation
大缺口收窄为 `D/j>=1/8` 的 compact-uniform upper，再之后才是 hybrid stability、
PSC lower/equality、positive backward tower、OU divisibility 与 `FS_3`。

## 90. R93：weighted Volterra stability versus Gram triangular loss（2026-09-07）

R93 处理两个不同的 triangular objects，不能把它们合并：其一是 R82--R92
的 mixed coefficient kernel `K`，它严格提高 degree；其二是 Gram--Schmidt 的
矩阵截断 `L_-`，它只保留矩阵的严格下三角。

### 90.1 mixed kernel 的 column tails、紧性与 resolvent

令 `w_j=16^j(j!)^2/(2j+1)!`，这是 `n^(-j)omega_(n,j)` 去掉公共因子
`4sqrt(n)` 后的权重。定义

`kappa_j=w_j^(-1)sum_(k>j)w_k|K_(k,j)|`。

R91 在 `D<=j/8` 给出 `C_91 j^(-3)`；R92 的 all-gap majorant 加上已审计的
`w_(j+D+1)/w_j<4^(D+1)`，在 `D>=j/8` 时用
`j+D+1<=10D`、`D^2+6D+2<=9D^2`、`D^2+7D-2<=4D^2`，得到安全显式上界
`C_92 D^7 16^D/D!`，可取 `C_92=31,008,000`。因此

`kappa_j <= C_91 j^(-3)+C_92 sum_(D>=j/8)D^7 16^D/D! ->0`。

这里使用 exact factorial tail，没有把 moving-gap 渐近外推到 source-large 区域。
于是对 `ell^1(w)` 的有限首坐标投影 `P_J`，

`||K-KP_J||=sup_(j>=J)kappa_j ->0`。

因为 `KP_J` 是 finite rank，得到 mixed coefficient operator 的 compactness。
更强地，按 `P_JX+(I-P_J)X` 分块，严格 degree-raising 给出

`K=[[K_H,0],[C,K_T]]`，

其中 `K_H^J=0`、`||K_T||<=epsilon_J`、`||C||<=C_K`。对固定 `lambda` 取
`|lambda|epsilon_J<=1/2`，tail resolvent 满足 `||R_T||<=2`，head resolvent 是
有限和 `R_H=sum_(q=0)^(J-1)lambda^qK_H^q`。因此 exact block inverse 给出每个
固定 `lambda` 下所有 finite sections `K^(n)=P_nKP_n` 的 uniform resolvent
bound；同一论证对任意非零谱参数给出 `sigma(K)={0}`。在已审计的 formal
exact decomposition 层面，`K` 是 compact quasinilpotent / Volterra-type operator。

这一步明确不等价于 full nonlinear Gram bootstrap。unilateral shift 是最小 no-go：
`||S_N||=1`、`S_N^N=0`，但 `||(I-S_N)^(-1)||=N`。所以 “column bounded +
triangular” 不足；真正的新输入是 `kappa_j->0`。

### 90.2 Gram--Schmidt 投影的 sharp logarithmic loss

对 `0,...,N-1` 的矩阵，`(L_-H)_(jk)=1_(j>k)H_(jk)`。取
`D_theta=diag(1,e^(itheta),...,e^((N-1)itheta))` 与
`p_N(theta)=sum_(d=1)^(N-1)e^(-idtheta)`，系数抽取得

`L_-H=(2pi)^(-1)integral p_N(theta)D_theta H D_theta^*dtheta`。

`|p_N(theta)|<=min(N,pi/|theta|)` 从而
`||L_-H||_op<=(1+log N)||H||_op`。R81 的离散 Hilbert-matrix witness 给出
`||L_-||>=c log N`，故 generic Gram triangular loss 是 `Theta(log N)`，而非
dimension-free。若 `(1+log N)epsilon_N<1`，线性化 inverse 有显式 bound
`||(I+L_-H_N)^(-1)|| <= [1-(1+log N)epsilon_N]^(-1)`。

对真正的 `G=I+H`、`C=I+L`，strict-lower part 只给出 exact nonlinear identity

`L=-L_-[H+LH+HL^*+LL^*+LHL^*]`。

本轮已审计此恒等式的符号与有限矩阵展开，但没有把它升级成 contraction。

### 90.3 当前状态分层

**PROVED（基于 R91/R92 exact decomposition）：** rescaled column vanishing、
compact/quasinilpotent mixed kernel、每个固定参数的 finite-section resolvent；
`L_-` 的 Fourier upper bound 与 Cholesky off-diagonal identity。

**Sharp/inherited：** R81 离散 Hilbert witness 的 `c log N` lower。

**仍 OPEN：** uniform nonlinear Gram--Schmidt theorem、global positivity、positive
infinite backward tower、backward OU divisibility 与 `FS_3`。这些结论不能从
mixed-kernel resolvent 或 Gram linearization 自动推出。

本轮新增 `flat_shadow_triangular_stability_r93/README.md` 与 `audit_r93.js`；
Node BigInt/rational audit 输出
`R93_TAIL_CONSTANTS_AND_FACTORIAL_DECAY_PASSED`、
`R93_WEIGHT_RATIO_AND_COLUMN_VANISHING_ANCHORS_PASSED`、
`R93_FINITE_STRICT_RESOLVENT_PASSED`、
`R93_NONLINEAR_GRAM_IDENTITY_PASSED`、
`R93_SHIFT_NO_GO_AND_FOURIER_SELECTOR_PASSED` 与
`R93_TRIANGULAR_STABILITY_AUDIT_COMPLETED`。

## 91. R94：finite-horizon nonlinear Gram stability（2026-09-07）

R94 先把 R93 的 abstract Volterra theorem 写成显式版本，再继续处理 D1 的
nonlinear Gram--Schmidt 闭合。对 `X=ell^1(w)`、`C_K=sup_j kappa_j`、
`epsilon_J=sup_(j>=J)kappa_j`，若 `|lambda|epsilon_J<=1/2`，则

`sup_n||(I-lambda P_nKP_n)^(-1)||`
`<=max(2,(1+2|lambda|C_K)sum_(q=0)^(J-1)(|lambda|C_K)^q)`。

本结论只作用于 R81 mixed linearized coefficient loop；它不作用于 nonlinear
Gram map，也不直接作用于 positivity。

### 91.1 finite-horizon nonlinear Gram theorem

设 `N>=2`、`Lambda_N=1+log N`，并明确要求 `H=H^*` 为 Hermitian Gram
perturbation。令

`Phi_H(L)=-L_-[H+LH+HL^*+LL^*+LHL^*]`，

且 `h=||H||`。若

`h<=1/[64 Lambda_N^2]`，`r=2Lambda_N h`，

则在严格下三角矩阵的 operator-norm ball `||L||<=r` 上，

`||Phi_H(L)||<=Lambda_N[h(1+r)^2+r^2]`，

并且

`||Phi_H(L)-Phi_H(M)||`
`<=2Lambda_N[h+r(1+h)]||L-M||`
`<=97/1024 ||L-M||`。

使用 `r<=1/32`、`r^2/h<=1/16`、`(1+r)^2+r^2/h<=1153/1024<2`，Banach
fixed point theorem 给出唯一严格下三角解

`L=Phi_H(L)`, `||L||<=2(1+log N)||H||`。

由于 `H=H^*` 且 `h<1`，`G=I+H>0`；令 `C=I+L`，则
`L_-(CGC^*)=0`。Hermitian 性使 `CGC^*` 的上、下三角同时消失，故它是
正 diagonal matrix，并满足

`(1-r)^2(1-h)I<=CGC^*<=(1+r)^2(1+h)I`。

这是一个真正的 finite-horizon nonlinear Gram factorization 小定理。`H=H^*`
是正性结论的必要条件，已在本机记录中显式补上。

### 91.2 generic operator norm 的严格 dimension-free no-go

取 `A_(jk)=1/(j-k)`、`H=iA`。`A` 是 skew-symmetric，故 `H` Hermitian；离散
Hilbert transform 使 `||H||` 可保持有界，而严格下三角部分作用于常向量的
norm 至少为 `c log N`。因此 Cholesky solution map 在零点的导数

`D Psi_N(0)[H]=-L_-H`

满足 `||D Psi_N(0)||>=c log N`。不存在固定 operator-norm 小球上的
`N`-uniform Lipschitz 常数。故 `Lambda_N^(-2)` 是严格的 sufficient scale，
不是 optimal claim；仅凭 `LL^*>=0` 不能去掉 logarithmic loss。

当前真正值得攻的结构化小 lemma 是 actual Hermite Gram compression 的
dimension-free triangular bound，例如

`||L_-H_n(h)||_op<=C[||H_n(h)||_op+||h||_(ell^1(w))]`。

这仍为 **CONDITIONAL/OPEN**，不能由 arbitrary-matrix operator theory 推出。

### 91.3 大局状态

R92--R94 已把 linear coefficient propagation 层真正移出主瓶颈：当前有
`kappa_j->0`、compact/quasinilpotent formal `K` 和固定参数的 horizon-uniform
resolvent；并且 finite horizon 的 nonlinear Gram 小球已闭合。剩余的最小高层
缺口仍是 actual Hermite structure 的 dimension-free triangular cancellation，
以及它之后的 fixed-parameter all-degree positivity。positive infinite backward
tower、backward OU divisibility 与 `FS_3` 仍是更高层 OPEN。

本轮新增 `flat_shadow_nonlinear_gram_r94/README.md` 与 `audit_r94.js`；
Node exact audit 输出 `R94_CONTRACTION_CONSTANTS_PASSED`、
`R94_FINITE_RESOLVENT_ANCHOR_PASSED`、
`R94_HERMITIAN_WITNESS_ANCHOR_PASSED` 与
`R94_NONLINEAR_GRAM_AUDIT_COMPLETED`。

## 92. R95：Hermite gap-Wiener algebra and an actual multiplier obstruction（2026-09-07）

R95 直接处理 R94 留下的 actual Hermite triangular cancellation，而不是
再次估计任意矩阵。对 `e_k=H_k/sqrt(k!)`、`Hcal_n(h)=P_nM_hP_n`、
`eta_m=L_h[e_m]`，Hermite product formula 给出精确矩阵元

`Hcal_n(h)_(ij)=sum_r r! binom(i,r)binom(j,r)
sqrt((i+j-2r)!/(i!j!)) eta_(i+j-2r)`。

等价地，`m=i+j-2r` 时只在 `|i-j|<=m<=i+j` 且
`m=i+j (mod 2)` 的 degree-local/parity 支持上出现。其双变量生成恒等式为

`sum_(i,j>=0)Hcal(h)_(ij)z^i/sqrt(i!) w^j/sqrt(j!)`
`=exp(zw)F_h(z+w)`。

### 92.1 gap-Wiener 代数

令 `D_theta=diag(1,e^(itheta),...,e^(intheta))`，以 Fourier 投影
`Delta_d A` 提取 `i-j=d` 的一条矩阵对角线，并定义

`||A||_(W_n)=sum_(d=-n)^n||Delta_dA||_op`。

逐项恒等式为

`Delta_d(AB)=sum_r Delta_r(A)Delta_(d-r)(B)`，
`||AB||_(W_n)<=||A||_(W_n)||B||_(W_n)`，
`||A^*||_(W_n)=||A||_(W_n)`，
以及 `||L_-A||_(W_n)<=||A||_(W_n)`。

因此 `L_-` 在这个结构化代数中是 contractive，generic operator norm 的
`log n` 不再出现；这一步是 exact gap convolution，不是把 generic
Hilbert estimate 误用于 actual class。

### 92.2 dimension-free structured theorem

使用 R77 已审计的 degree-local bound
`||P_nM_(e_m)P_n||_op<=2^m(3n)^(m/2)/sqrt(m!)`，取
`rho_n=4sqrt(n)`、`q=sqrt(3)/2` 和
`||h||_(rho_n)=sum_(m<=2n)|eta_m|rho_n^m/sqrt(m!)`，得到

`||Hcal_n(h)||_(W_n)<= (189/64)||h||_(rho_n)`，

以及只保留正 gaps 的更尖锐估计

`||L_-Hcal_n(h)||_op <= (27sqrt(3)/32)||h||_(rho_n)<(3/2)||h||_(rho_n)`。

常数与 `n` 无关；`189/64` 的标量最大项在 `m=6`，正-gap常数的最大
奇项在 `m=5`。于是若 `H=H^*` 且
`||H||_(W_n)<=1/64`，R94 的 nonlinear map 在 `W_n` 中以半径
`2||H||_(W_n)` 严格收缩，给出唯一 strict-lower `L`，

`||L||_(W_n)<=2||H||_(W_n)`，

并使 `(I+L)(I+H)(I+L)^*` 成为正 diagonal；全套常数对 horizon `n`
一致。特别地，`||h||_(rho_n)<=1/189` 足以给出该结构化 Gram 闭合。

### 92.3 bounded multiplier 的 actual no-go

上述结论不能降格为“所有 bounded Hermite multiplier 都成立”。取实际
乘子 `h(x)=sgn(x)`，有 `||Hcal_n(h)||_op<=1`。OU 半轴 Green 恒等式给出
对 `i=2p+1,j=2q`

`Hcal_n(sgn)_(2p+1,2q)=2gamma(0)sqrt(2p+1)e_(2p)(0)e_(2q)(0)`
`/[2(p-q)+1]`，其中
`e_(2r)(0)=(-1)^r sqrt((2r)!)/(2^r r!)`。

中央二项式下界与一个带符号的 even 输入块共同给出
`||L_-Hcal_n(sgn)||_op >= c log n-C`；R94 的 generic Fourier upper 给出
相反方向。因此实际 Hermite multiplier 也可以达到
`||L_-Hcal_n(sgn)||_op=Theta(log n)`，而 odd parity 本身不能消除障碍。

### 92.4 大局更新与边界

**PROVED（在 R77 degree-local estimate 的已审计前提下）：** 精确 Hermite
矩阵元与双变量恒等式、gap-Wiener product algebra、growing-radius 类的
dimension-free triangular bound、`1/64` 小球上的 horizon-uniform nonlinear
Gram factorization，以及 bounded multiplier 类的 actual `sgn` 对数障碍。

**CONDITIONAL：** 若项目实际的 Gaussian-mixture backgrounds 满足

`sup_n||Hcal_n(g1)||_(W_n)<infinity`，
`sup_n||Hcal_n(g2)||_(W_n)<infinity`，

且 residual 在同一 hybrid 小球内，则 R95 theorem 可接回固定非零参数的
all-degree Gram factorization。

**OPEN：** `g1,g2` 的具体 gap-Wiener 可和性；
`||Z(h)||_(ell^1(w))+||Hcal_n(h)||_(W_n)` 的 nonlinear same-factor
invariance；global positivity；positive infinite backward tower；backward
OU divisibility；以及 `FS_3`。

所以 R95 的整体判断是：linear coefficient propagation 已真正移出主瓶颈，
Gram 侧的 generic `log n` 也已被结构化代数替代；当前最小项目特异问题
已经收缩为 `g1,g2` 两个具体 Gaussian-mixture background 是否具有统一
gap summability。

本轮新增 `flat_shadow_hermite_gap_wiener_r95/README.md` 与
`audit_r95.js`。Node 固定精确/代数锚点审计输出：
`R95_HERMITE_ENTRY_AND_LOCALITY_PASSED`、
`R95_GAP_CONVOLUTION_IDENTITY_PASSED`、
`R95_STRUCTURED_CONSTANTS_PASSED`、
`R95_TANGENT_MOMENT_NORMALIZATION_PASSED`、
`R95_SIGN_GREEN_IDENTITY_ANCHORS_PASSED`、
`R95_SIGN_LOWER_CONSTRUCTION_ANCHOR_PASSED` 与
`R95_HERMITE_GAP_WIENER_AUDIT_COMPLETED`。

## 9. R96：真实背景的 gap-Wiener 分叉与背景中心化（2026-09-07）

R96 首次把 R95 的 gap-Wiener 问题直接作用于项目自身的 `g1,g2`，并保留
Gaussian-mixture 参数端点。结论不是“两个背景都进入小球”：canonical tangent
`g1` 的统一 gap-Wiener 可和性严格失败，而 quadratic `g2` 暂只得到端点安全的
逐 gap 上界。

### 9.1 `g1`：精确 gap 公式与 `Theta(log n)`

由 R71 的
`g1=integral_0^1(qR^3-q^2R^5/2)psi_q ds`、`T(R^m psi_q)=z^m exp(-qz^2)`
及 R95 双变量恒等式，若 `K_(d,n)^(m)(q)=Delta_d Hcal_n(R^m psi_q)`，则

`Delta_d Hcal_n(g1)=integral_0^1[q K_(d,n)^(3)(q)-q^2 K_(d,n)^(5)(q)/2]ds`。

其单 entry 的有限系数抽取为

`c_(j,d)^(m)(q)=sqrt((j+d)!j!)
 [z^(j+d)w^j] exp(zw)(z+w)^m exp(-q(z+w)^2)`。

R82/R83 的 canonical Jacobi tangent 给出同一实际矩阵的 closed form：gap 1
除有限 head `A_(2,1)=1/sqrt(2)` 外完全消失；gap 3 从 finite head 后为
`A_(k+3,k)=-2sqrt(k!/(k+3)!)`；对 `a>=1`，gap `2a+3` 为

`A_(k+2a+3,k)=(-1)^a (a+1)(a+2)[a(a+1)-2k](k+a-1)!
 sqrt(k!/(k+2a+3)!)/(2k!)`。

令 `R_(k,a)^2=prod_(r=1)^(a-1)(k+r)/prod_(r=a)^(2a+3)(k+r)`。
在 `k=a(a+1)` 处得到 `||Delta_(2a+3)A_n|| >= exp(-7/2)/(2(a+1))`
（当 `a^2+3a+3<=n`）。配对分子分母则给 `||Delta_(2a+3)A_n||<=864/(a+1)`，
有限 head 单独吸收。因此本机拟核验的结论是

`||Hcal_n(g1)||_(W_n)=Theta(log(n+2))`,
`sup_n||Hcal_n(g1)||_(W_n)=infinity`。

这是实际 R71 tangent 的障碍，不是 R95 的 `sgn` 替代反例。

### 9.2 `g2`：端点安全但尚未求和

R80 的四项 representer 令 `A=r_i^2,B=r_j^2`、
`xi=6q_tau q_sA`、`eta=6q_tau q_uB`、`alpha=xi+eta`，并有 signed weight
`w_(ij)=(6q_tau)^3q_sq_ur_i^3r_j^3`。对 gap `d` 的 exact formula 是把同一
`c_(j,d)^(m)(alpha)` 代入 `R^6,R^8,R^10,R^12` 四项组合；奇数 gap 恒为零。

不能假设 `alpha` 有固定正下界。整体组合满足 `||g_(alpha,xi,eta)||_infty
<=C_R80 alpha^(-3)`，且

`|w_(ij)|alpha^(-3)=q_sq_uA^(3/2)B^(3/2)/(Aq_s+Bq_u)^3`。

因此 `q_tau^3` 精确抵消，R80 的 endpoint integral 给出
`sup_(n,d)||Delta_d Hcal_n(g2)||_op<=M2:=4C_R80`。这只推出
`||Hcal_n(g2)||_(W_n)<=M2(n+1)`；`g2` 的绝对 gap sum 仍 OPEN。

### 9.3 路线修正：background 必须先吸收

因为 `A_n` 只占 odd gaps、`B_n^(2)` 只占 even gaps，

`||aA_n+a^2B_n^(2)||_(W_n)=|a|||A_n||_(W_n)+a^2||B_n^(2)||_(W_n)`。

所以固定 `a!=0` 时，`g1` 的 `log n` 增长阻止 uncentered background 进入 R95 的
`1/64` 小球；但 R80 的 operator bound 仍允许
`|a|M1+a^2M2+sup_n||Hcal_n(Ehat(a)+o(a))||_op<1` 作为 conditional
all-degree positivity criterion。

正确目标是先取 `C_(0,n)G_(0,n)C_(0,n)^*=D_(0,n)`，再对
`E_n=C_(0,n)Hcal_n(h)C_(0,n)^*` 证明 uniform structured bound，并同时保持
`0<c_-<=D_(0,n)<=c_+`。这条 background-conjugation lemma、`g2` gap sum、hybrid
invariance、global positivity、positive infinite tower、backward OU divisibility
和 `FS_3` 仍为 OPEN。

### 9.4 R92/R93 与 growing-radius norm 的精确不匹配

若 `o(z)=sum_j c_jZ_jz^(2j+1)`、`c_j=(j!)^2/(2j+1)!`、`w_j=16^jc_j`，则

`||o||_(rho_n)=4sqrt(n)sum_j n^jw_j|Z_j|`。

故 `ell^1(w)` 不会均匀嵌入 R95 的 growing-radius 球。对单位 `Z_j` 模式令
`gamma_(n,j)=||Hcal_n(o^(j))||_(W_n)`，并设 `v_(n,j)=w_j+gamma_(n,j)`；一个明确
的 sufficient hybrid column criterion 是

`sup_(n,j) v_(n,j)^(-1)sum_k v_(n,k)|K_(k,j)^(n)|<infinity`。

R92/R93 已覆盖只含 `w` 的部分，含 `gamma` 的 Gram-transfer 部分尚未证明。

R96 本机记录目录为 `flat_shadow_background_gap_r96/`；审计应只使用固定精确
恒等式和代表性 channels，不以数值 sweep 代替上述 factorial-ratio 证明。

### 9.5 R97：background-centered finite-horizon theorem 与线性 no-go

对任意 Hermitian `G=I+H`、`||H||op<=h<1`，不用 determinant 的 finite LDL
递归给出 `G=TDT^*`、`C=T^{-1}` 以及精确恒等式 `CGC^*=D`。Schur complement
的变分表示直接给出

`1-h<=D_ii<=1+h`，`||C||op^2,||C^{-1}||op^2<=kappa(h):=(1+h)/(1-h)`。

所以正式背景 `G_(0,n)=I+aA_n+a^2B_n^(2)` 在
`h_0=|a|M_1+a^2M_2<1` 下有与 `n` 无关的 operator conditioning；这一步是
PROVED，但不等同于 `W_n` conditioning。

若 `E=C_(0,n)H C_(0,n)^*`，则 trace norm 给出真正 uniform 的替代：

`||E||_1<=kappa(h_0)||H||_1`，

`||D_(0,n)^(-1/2)E D_(0,n)^(-1/2)||_1
 <=(1+h_0)/(1-h_0)^2 ||H||_1`。

故在 horizon `N=n+1` 上，只要

`[(1+h_0)/(1-h_0)^2]||H||_1 <=1/[64(1+log N)^2]`

即可调用 R94 的 finite-horizon strict-lower contraction；这是一个可发表的
finite-horizon corollary，不是 infinite-horizon closure。

另一方面，对 `G_n(a)=I+aA_n` 在 `a=0` 微分，严格下三角部分强制
`C_n'(0)=-L_-A_n`。R96 对实际 `g1` 已证 `||L_-A_n||_(W_n)>=c log(n+2)`，
所以 `sup_n||C_n'(0)||_(W_n)=infinity`。这严格否定任何基于该范数的
dimension-free background local-Lipschitz/perturbative conjugation 论证；它是
linearized PROVED no-go，不声称每个固定非零 `a` 的 conjugation 都发散。

R97 本机记录目录为 `flat_shadow_background_centered_r97/`，审计目标为
`R97_BACKGROUND_CENTERED_AUDIT_COMPLETED`。background-relative `W_n` norm、
`g2` 全 gap sum、hybrid `gamma` feedback、global positivity、positive
backward tower、backward OU divisibility 与 `FS_3` 继续标为 OPEN。

### 9.6 网页端 R97 强化：relative Jacobi norm 与 (g_2) growing-gap theorem

网页端随后给出了比本机初始 R97 摘要更强、也更适合主路线的版本。令

`w_a=1+a g_1+a^2g_2`、`delta_a=|a|M_1+a^2M_2<1`、
`d mu_a=w_a d gamma`，并对 `G_(0,n)` 做 monic Gram--Schmidt。若 `C_(0,n)`
为所得 unit-lower factor、`D_(0,n)=diag(d_k)`，则 exact recursion 是

`u_k=-(G_(0)^[k-1])^(-1)b_k`、
`phi_k=e_k+sum_(j<k)(u_k)_j e_j`、
`d_k=<phi_k,phi_k>_(mu_a)`、
`C_(0,n)G_(0,n)C_(0,n)^*=D_(0,n)`。

由 `1-delta_a <= w_a <= 1+delta_a` 得

`1-delta_a <= d_k <= 1+delta_a`，
`||C_(0,n)||op,||C_(0,n)^(-1)||op <= sqrt((1+delta_a)/(1-delta_a))`。

这一步是 horizon-uniform 的 exact background absorption，但不声称
`C_(0,n)` 在原始 gap-Wiener 范数中有界。

定义 `S_(0,n)=D_(0,n)^(-1/2)C_(0,n)` 与
`bar E_n=S_(0,n)Hcal_n(h)S_(0,n)^*`。令
`h^[2n]=sum_(m<=2n)eta_m e_m`、`r_(a,n)=h^[2n]/w_a`，再令
`p_(a,n)[h]=Pi_(<=2n)^(mu_a) r_(a,n)`。由于
`deg(psi_i psi_j)<=2n`，有 exact identity

`(bar E_n)_(ij)=int p_(a,n)[h] psi_i psi_j d mu_a`。

若 `p_(a,n)[h](x)=sum_m b_m x^m`，背景 Jacobi 矩阵 `J_a` 满足

`||J_a^[N]||op <= 2 sqrt(kappa_a) sqrt(N+1)`,
`kappa_a=(1+delta_a)/(1-delta_a)`，
`||J_a^[N]||_(W) <= 6 sqrt(kappa_a) sqrt(N+1)`。

于是对 `R_(a,n)=6 sqrt(kappa_a) sqrt(3n+1)` 定义

`P_(a,n)(h)=sum_(m<=2n)|b_m|R_(a,n)^m`，即可得到实际的
background-centered bound

`||bar E_n||_(W_n) <= P_(a,n)(h)`。

这不是把 `C_(0,n)` 粗暴地当作原始 Wiener multiplier，而是把 residual
精确改写成背景正交多项式基下的 polynomial multiplier。代入 exact centered
equation 后，若 `P_(a,n)(h)<=1/64`，R95 的同一标量估计给出

`q_contr<=97/1024<1`、`||tilde L_n||_(W_n)<=2P_(a,n)(h)`，以及
`||L_n||_(W_n)<=2 sqrt(kappa_a) P_(a,n)(h)`。

因此固定非零 `a` 的 all-degree positivity 有明确的 conditional criterion：

`delta_a<1` 且 `sup_n P_(a,n)(h(a))<=1/64`

推出 `G_n(a)>0` 对所有 `n`。条件性只剩 actual same-factor branch 是否进入
这个 relative-background ball，Gram/triangular 代数本身已闭合。

对 quadratic background，令 `N e_k=k e_k`。精确交换子恒等式为

`[N,M_g]=M_(Ng)-2M_(g') partial_x`，

`ad_N^2(M_g)=M_(N^2g)-2M_((Ng)')partial_x-2M_(N(g'))partial_x
 +4M_(g'')partial_x^2+2M_(g')partial_x`。

因此若

`C_2(g)=||N^2g||_infty+2|| (Ng)'||_infty+2||N(g')||_infty
       +4||g''||_infty+2||g'||_infty`，

则 `||P_n ad_N^2(M_g)P_n||<=C_2(g)(n+1)`，并对 `d!=0` 有

`||Delta_d Hcal_n(g)|| <= C_2(g)(n+1)/d^2`。

R80 四项 Gaussian block 在 `alpha->0` 时仍由同一
`alpha^(-3)` endpoint majorant 控制，且 signed weight 满足
`|w|alpha^(-3)=q_s q_u A^(3/2)B^(3/2)/(Aq_s+Bq_u)^3`；故 `C_2(g_2)<infinity`
是 endpoint-safe 的解析结论（本机审计核对代数与求和，不冒称已独立证明全部
端点微分常数）。和 R96 的 per-gap `M_2` 合并，得到

`||Delta_d B_n^(2)|| <= min{M_2,C_2(g_2)(n+1)/d^2}`。

从而 proportional-gap tail 对 `D=ceil(delta(n+1))` 满足
`sum_(|d|>=D)||Delta_d B_n^(2)|| <=4C_2(g_2)/delta`，并且

`||B_n^(2)||_(W_n) <= 3M_2+4 sqrt(M_2 C_2(g_2)(n+1))=O(sqrt n)`。

这是严格优于此前 `O(n)` 的 growing-gap theorem；尚不能推出 `B_2^triangle<infinity`。
剩余未知窗口已精确压缩到 `1<<d<<n`，交叉尺度为 `d~sqrt n`。要得到绝对 gap
可和性，仍需 uniform 的 `C/(1+d)^(1+epsilon)` 或可求和的 two-parameter envelope。

最后，对 unit odd mode 定义 `Gamma_(a,n,j)=P_(a,n)(h^(j))`，并取
`v_(a,n,j)=w_j+Gamma_(a,n,j)`。R92/R93 已证
`C_w=sup_(n,j)w_j^(-1)sum_k w_k|K_(k,j)^(n)|<infinity`；新的、未证但精确的
Gram-transfer 条件是

`C_Gamma(a)=sup_(n,j)Gamma_(a,n,j)^(-1)sum_kGamma_(a,n,k)|K_(k,j)^(n)|<infinity`。

若该条件成立，则 hybrid column norm 不超过 `max(C_w,C_Gamma(a))`；否则必须
从实际 mode 构造 lower obstruction或改用相对背景权重。故当前大路线明确分层：
relative finite-horizon Gram theorem 与 `g_2` growing-gap bound 为 PROVED；
actual branch 的 relative hybrid invariance、`C_Gamma`、mesoscopic `g_2` envelope、
global positivity、positive backward tower、backward OU divisibility 与 `FS_3` 仍 OPEN。

### 9.7 R98：R97 growing-radius Γ hybrid criterion 的 Gaussian-endpoint no-go

R97 把 unit odd mode 的 Gram cost 定义为
`Gamma_(a,n,j)=P_(a,n)(h^(j))`，并提出
`C_Gamma(a)=sup_(n,j)Gamma_(a,n,j)^(-1)sum_kGamma_(a,n,k)|K_(k,j)^(n)|`。
本轮本机把这个候选条件在最容易被误判的 `a=0` endpoint 精确否证。

按 R92/R93 的实际 mode normalization，`h^(j)=c_j e_(2j+1)`、
`c_j=(j!)^2/(2j+1)!`。当 `a=0` 时 relative projection 不改变该 mode，且
R97 的 polynomial cost 精确为

`Gamma_(0,n,j)=c_j A_(2j+1)(R_n)`、`R_n=6sqrt(3n+1)`，

其中 `A_m(R)` 是 `e_m=H_m/sqrt(m!)` 的绝对 monomial coefficient sum。固定
`j`、`D`，令 `k=j+D`，最高次项立即给出

`Gamma_(0,n,k)/Gamma_(0,n,j)`
`~(c_k/c_j)sqrt((2j+1)!/(2k+1)!)R_n^(2D)`。

R82 的 actual canonical gap-four channel 为

`K_(j+4,j)=-(3j^3+146j^2+1001j+1560)`
`/[15(j+1)(j+2)(j+3)^2(j+4)^2]`，

故 `K_(5,1)=-271/3600`。它对所有 `n>=5` 都是同一个非零有限-section
channel，于是

`C_Gamma(0)>=|K_(5,1)|Gamma_(0,n,5)/Gamma_(0,n,1)`，

而右端按 `R_n^8` 发散。因此

`C_Gamma(0)=infinity`。

这不是 generic matrix obstruction，也不否定 R92/R93：后者使用的是去掉
`n^j` 的 rescaled `ell^1(w)`，而 R97 的 `P_(a,n)` 把 growing radius 留在每个
mode cost 中。结论是：R97 的 `C_Gamma` 不能在含 `a=0` 的邻域中原样使用；任何
“小 a 统一有限”的证明都必须先改变 mode cost。自然替代是
`GammaHat_(a,n,j)=R_n^(-(2j+1))Gamma_(a,n,j)`（至少在 Gaussian endpoint），
或直接构造 degree-local background/Jacobi cost，使 fixed canonical channel ratio
不携带 `R_n^(2D)`。对某个固定非零 `a` 的 projected higher-degree cost、其
renormalized column bound 与 nonlinear invariance 仍保持 OPEN。

本机小定理状态：`C_Gamma(0)=infinity` 为 PROVED；uniform neighborhood transfer
用原始 `Gamma` 为严格 NO-GO；replacement norm、fixed nonzero `a`、global
positivity、positive backward tower、backward OU divisibility 与 `FS_3` 仍 OPEN。

### 9.8 R98 强化：Gaussian endpoint 的 degree-renormalized hybrid column theorem

原始 `Gamma` 的失败并不意味着 hybrid transfer 本身失败，而是指出
`P_(a,n)` 的 growing radius 必须从 mode ratio 中除去。`a=0` 时令

`GammaHat_(0,n,j)=R_n^(-(2j+1))Gamma_(0,n,j)`、`R_n=6sqrt(3n+1)`。

若 `A_m(R)` 是 `e_m` 的绝对 monomial coefficient sum，则正系数 Hermite 递归为

`A_(m+1)=(R A_m+sqrt(m)A_(m-1))/sqrt(m+1)`，

且 `A_(m-1)/A_m<=sqrt(m)/R`。在 `k=j+D`、`n>=k+1` 时，中间次数不超过 `2n`，
所以 `2n/R_n^2<1/54`，从而

`A_(2k+1)(R_n)/A_(2j+1)(R_n)`
`<=R_n^(2D)(55/54)^(2D)/sqrt((2j+2)_(2D))`。

另一方面
`c_(j+D)/c_j=product_(t=1)^D(j+t)^2/[(2j+2t-1)(2j+2t)]<=2^(-D)`。
定义 `rho_*=((55/54)^2)/2=3025/5832<1`，得到 exact usable ratio bound

`GammaHat_(0,n,j+D)/GammaHat_(0,n,j)<=rho_*^D`。

这消除了原始 `Gamma` 的 `R_n^(2D)` 爆炸。与 R91 的 `D<=j/8` weighted column
bound 合并，再对 `D>=j/8` 使用 R92 的 `3^D/D!`、`4^D/D!` all-gap majorant，
乘以 `rho_*^(D+1)` 后得到 polynomial-times-factorial 的收敛级数。因此在
odd mode 已被 `2n` moment projection 包含的 interior range `n>=k+1` 上，得到

`sup_(n>=1,j>=1)sum_(k=j+3)^(n-1)|K_(k,j)^(n)|
 GammaHat_(0,n,k)/GammaHat_(0,n,j)<infinity`。

这是一个新的小定理：**PROVED**（在已审计的 formal R91/R92 kernel 身份下）
Gaussian endpoint 的 renormalized linear hybrid transfer；同时
`C_Gamma(0)=infinity` 的 unrenormalized no-go 仍成立。fixed nonzero `a` 的
background projection 会生成 higher-degree components，故其 renormalized ratio、
horizon boundary、nonlinear centered invariance 与 positivity 仍 **OPEN**。
该结果修复的是 mixed coefficient feedback 的尺度，不等于已经证明 Gram
small-ball 或 positive backward tower。

### 9.9 R98 方法学障碍：固定阶交换子不能单独突破 (g_2) 的 (sqrt n) 窗口

网页下一轮若仅把 R97 的二阶交换子换成任意固定阶 `r`，即使能够证明

`||P_n ad_N^r(M_(g2))P_n||op<=C_r(n+1)^(r/2)`，

也只能得到
`||Delta_d B_n^(2)||<=min{M_2,C_r(n+1)^(r/2)/|d|^r}`。
令 `D_*^r` 首次超过 `C_r(n+1)^(r/2)/M_2`，则

`sum_(d>=1)min{M_2,C_r(n+1)^(r/2)/d^r}`
`<=M_2(D_*+1)+C_r(n+1)^(r/2)D_*^(1-r)/(r-1)`。

两项都具有
`M_2^(1-1/r)C_r^(1/r)(n+1)^(1/2)` 的尺度，因为
`r/2+(1-r)/2=1/2`。所以任意固定阶 commutator decay 都只能重现
`O(sqrt n)`，无法单独决定绝对 gap sum。

这是 **PROVED method barrier**，不是 `g_2` 的 `sqrt n` lower bound。R80 端点下
高阶 `C_r` 是否有限还需新的 endpoint 审计；真正剩余的理论必须利用固定阶交换子
看不到的 four-term cancellation、低 gap subtraction 或可求和的 two-parameter
envelope。因而 R98 后的 (g_2) 研究目标从“继续提高交换子阶数”收紧为“直接
证明结构性中尺度 cancellation”。

### 9.10 R98：actual `g2` 的 exact gap-6 lower anchor

R71 切向生成函数满足 `U(z)=z^3/6+O(z^5)`。因此 R80 二阶方程
`A V=-B` 的最低阶项为 `[z^6]B=C_(3,3)/36`。对
`r_j=sqrt(2/3)cos(theta+2pi(j-1)/3)`，用
`sum r_j=0`、`sum r_j^2=1` 及
`r_1r_2r_3=(2/3)^(3/2)cos(3theta)/4`，精确得到
`C_(3,3)=-7/72`。又 `A_(6)=5/18`，所以 `[z^6]V=7/720`。

由于 `Tg2=V`，`g2` 的 normalized Hermite moment 是
`eta_6=sqrt(6!)[z^6]V=7sqrt(5)/60`。于是对 `n>=6`，由 `e_6e_0=e_6`，
`||Delta_6 B_n^(2)||>=7sqrt(5)/60`；加上负 gap 后
`||B_n^(2)||_(W_n)>=7sqrt(5)/30`。

更精确地，最低 degree-six mode 给出完整 boundary corner：当 `i+j=6` 时，
`(B_n^(2))_(i,6-i)=eta_6 sqrt(binomial(6,i))`。所以 gaps `6,4,2,0` 的
首个 boundary entries 分别为 `eta_6,sqrt(6)eta_6,sqrt(15)eta_6,
sqrt(20)eta_6`。这是 finite-degree corner certificate，不是 mesoscopic
growth conclusion；它只排除 all-even-gap cancellation，仍不决定 `g2` 的
全 gap 增长。

这是 **PROVED exact lower anchor**，只排除 all-even-gap cancellation，
不决定 `g2` 的全 gap 增长；`O(1)`、`Theta(log n)` 及其它 mesoscopic 行为仍 **OPEN**。

### 9.11 R99：positive backward-OU Hermite cone

本轮把“positive backward preimage 对高 Hermite coefficients 的约束”写成了
一个 exact finite-dimensional cone。令 `psi_m=He_m/sqrt(m!)`，
`a_m(g)=E_g psi_m`，并设 `g=P_t h`，其中 `h d gamma` 是正的 centered
variance-one probability law。由于 OU multiplier 是 `t^(m/2)`，
`b_m(h)=t^(-m/2)a_m(g)`。于是每个有限 Gram block 都满足

`M_t(g)=[E_h(psi_i psi_j)]_(0<=i,j<=r) >=0`,

且 product formula 给出

`(M_t(g))_(ij)=sum_(ell=0)^[min(i,j)]
 ell! binom(i,ell)binom(j,ell)
 sqrt((i+j-2ell)!/(i!j!))
 t^(-(i+j-2ell)/2)a_(i+j-2ell)(g)`.

这是真实正 preimage 的 moment cone，而不是 operator-only 反例。若 `h` 是
`L^2(gamma)` 密度，任意有限 block 实际为正定：非零多项式的零集为
Lebesgue 零集，不能在正概率密度上使其平方积分为零。

取 principal minor `(0,m)` 得高阶墙

`a_m(g)^2 <= sum_(ell=0)^m c_(m,ell)t^ell a_(2m-2ell)(g)`,

`c_(m,ell)=m!sqrt((2m-2ell)!)/(ell!(m-ell)!^2)`。

在 centered variance-one 情形，`a_1=a_2=0`，低阶两条明确为

`a_4(g)>-t^2/sqrt(6)`,

`a_4(g)>(3t^(-1)a_3(g)^2-t^2)/sqrt(6)`,

以及独立的 `(0,3)` 墙

`a_3(g)^2<2sqrt(5)a_6(g)+3sqrt(6)t a_4(g)+t^3`。

第二条等价于 raw centered moments 的 exact inequality

`m_3(g)^2<t(m_4(g)-3+2t^2)`.

若是深度 `N` 的固定因子塔，`g^(0)=P_(q^N)g^(N)`，只需令 `t=q^N`。
特别地

`a_4(g^(0))>-q^(2N)/sqrt(6)`,

且若 `a_4(g^(0))<=0`，则
`|a_3(g^(0))|<q^(3N/2)/sqrt(3)`。

这给出了一个可报告的 local backward-divisibility theorem：深度不能让一个
固定负的 fourth-Hermite defect 留在底层；若底层 excess kurtosis 非正，
skewness 甚至按 `q^(3N/2)` 衰减。它尚未连接 `P_3 K`，因为 third Hermite
moment 与 projected cubic charge 仍是不同对象；也不能把该锥约束冒充完整
zero-set rigidity。真正的下一步是从 same-factor exact-zero identity 中抽取
`a_3,a_4,a_6` 的关系，再将其代入这组严格 cone walls。

本节的本机审计为 `positive_backward_hermite_cone_r99/audit_r99.py`，状态为
`R99_POSITIVE_BACKWARD_HERMITE_CONE_AUDIT_COMPLETED`。Gaussian rigidity、
`P_3K` bridge、mesoscopic tail 与 fixed nonzero branch 仍 **OPEN**。

### 9.12 R100：finite-depth certificate from the positive cone

R99 的锥约束还能转成深度证书。定义

`F_m(t;g)=sum_(ell=0)^m c_(m,ell)t^ell a_(2m-2ell)(g)-a_m(g)^2`,

其中 `c_(m,ell)=m!sqrt((2m-2ell)!)/(ell!(m-ell)!^2)`。若 `g=P_t h` 且
`h` 是正的 `L^2(gamma)` density，则对每个 `m` 有严格 `F_m(t;g)>0`；
所以 `F_m(t;g)<=0` 是 exact finite-dimensional no-preimage certificate。
对于 depth-`N` fixed-factor tower，把 `t` 直接替换为 `q^N`。

`[psi_1,psi_2]` Schur complement 在 centered variance-one 下等价于

`f_(3,4)(t)=t^3+sqrt(6)a_4(g)t-3a_3(g)^2>0`。

当 `a_3!=0` 时，该三次式恰有一个正根 `tau_(3,4)`：`a_4>=0` 时严格递增；
`a_4<0` 时先降后升，且起点和极小值均为负。因此任何正 backward preimage
都必须满足 `t>tau_(3,4)`，而 depth-`N` tower 必须满足
`q^N>tau_(3,4)`。若 `0<tau_(3,4)<1`，得到
`N<log(tau_(3,4))/log(q)`；若根不小于 1，则该深度根本不可能。
当 `a_3=0,a_4<0` 时阈值简化为
`t>sqrt(-sqrt(6)a_4)`。

这是一个非局部的 finite-depth obstruction，而不只是局部导数估计。它把
主命题剩余的 charge bridge 精确化：若 same-factor exact-zero identity 能证明
非零 `P_3K` 必导致某个 `F_m(q^N;g)<=0`，或迫使 `tau_(3,4)` 有统一正下界，
则任意深 positive tower 即被排除。当前尚未证明该 charge-to-cone implication；
高阶/角向 charge 仍可能躲过低阶一维 moments。

本节审计为 `positive_backward_hermite_cone_r100/audit_r100.py`，状态为
`R100_FINITE_DEPTH_CERTIFICATE_AUDIT_COMPLETED`。Gaussian rigidity、`P_3K`
bridge、mesoscopic tail 和 fixed nonzero branch 继续 **OPEN**。

### 9.13 R101：Angular Herglotz Charge Cone

本轮把正性、same-factor cubic map 与 OU backward divisibility 首次放进同一
个真实概率测度锥。对 genuine full-exact centered variance-one law `mu`，令

`r_j(theta)=sqrt(2/3)cos(theta+2pi(j-1)/3)`，
`Y_theta=sum_j r_j(theta)X_j`，其中 `X_j` iid `mu`，并记其 law 为 `mu_theta`。

full-exact characteristic identity 与 Fourier uniqueness 给出真实测度恒等式

`(1/(2pi))int_0^(2pi)mu_theta dtheta=gamma`。

定义

`nu_r(B)=(1/(2pi))int exp(-3 i r theta)mu_theta(B)dtheta`。

于是 `nu_0=gamma` 且 `|nu_r|<=gamma`。令 `chi_r=dnu_r/dgamma`，得到
`|chi_r|<=1`。对任意有限复向量 `c`，

`sigma_c=sum_(p,q)c_p conjugate(c_q)nu_(p-q)>=0`

是正测度，因此有 pointwise infinite Herglotz cone

`[chi_(p-q)(x)]_(p,q=0)^M >=0` `gamma`-a.e.，对每个 `M` 成立。

这是 measure-level positivity，不使用 determinant、SDP 或 optimizer。与其相关
的 Fourier Gram 形式必须谨慎书写：完整带 charge index 的块是正的；单个复的
`T_r` 不在没有额外 reality convention 时直接写成 Loewner-Hermitian 顺序。

令 `e_m=He_m/sqrt(m!)`、`a_m=E_mu[e_m]`，则 Hermite addition law 给出完整
same-factor cubic charge map

`beta_(m,r)=sum_(k1+k2+k3=m)sqrt(m!/(k1!k2!k3!))`
` A_r(k1,k2,k3)prod_j a_(k_j)`，

其中 `A_r` 是 `prod_j r_j(theta)^(k_j)` 的 `3r` Fourier coefficient。选择律为
`beta_(m,r)=0`（若 `m<3|r|` 或 `m != r mod 2`）。因为 `|chi_r|<=1`，Parseval
给出全阶、非线性的概率锥

`sum_(m>=3|r|, m=r mod 2)|beta_(m,r)|^2<=1`。

若 `mu=P_t nu` 且两者均 genuine full-exact，则
`chi_r(mu)=P_t chi_r(nu)`、`beta_(m,r)(mu)=t^(m/2)beta_(m,r)(nu)`，故任意
正的 `t`-preimage 满足

`sum_(m>=3|r|, m=r mod 2)t^(-m)|beta_(m,r)(mu)|^2<=1`。

`r=1` 的前四个非零结构经过本机 exact symbolic audit：

`beta_(3,1)=sqrt(6)a_3/12`，
`beta_(5,1)=5sqrt(6)a_5/72`，
`beta_(7,1)=7sqrt(6)a_7/144`，

`beta_(9,1)=7sqrt(6)a_9/216-7sqrt(14)a_6a_3/144+sqrt(70)a_3^3/216`。

最后一式是首个 genuine nonlinear charge mixing，不能把 charge 偷换成 `a_3`。

若 law moment-determinate，取首个非零 odd Hermite coefficient `a_d`，则
`beta_(d,1)=Lambda_d a_d`，其中

`Lambda_d=3(sqrt(2/3)/2)^d binom(d,(d-3)/2)>0`。

所以得到新的 angular asymmetry theorem：

`chi_1=0 <=> mu symmetric`。

定义 `S_3(t;mu)=sum_(m=3,5,...)t^(-m)|beta_(m,1)(mu)|^2` 与
`tau_ang(mu)=inf{t in (0,1]:S_3(t;mu)<=1}`。任何 asymmetric genuine exact law
都有 `tau_ang(mu)>0`，任何正的 exact preimage 都满足 `t>=tau_ang(mu)`；因而
同一个 asymmetric exact base 的 positive backward OU depth 必有限。这是比只看
`a_3` 更强的可独立报告弱定理，允许 asymmetry 首先出现在任意高 odd Hermite
degree。

逻辑边界必须保留：本结果对 varying-bottom sequence 不给 uniform `tau_ang` 下界，
也没有得到 `P_3K != 0 => chi_1 != 0`。因此 `P_3K` 与 angular charge 的
audited zero-set bridge、symmetric even-sector rigidity、以及完整 Positive
Backward-Tower Exact Zero-Set Rigidity 仍 **OPEN**。若项目中 `RK=1` 尚未独立
证明等价于 genuine full-exact law，则上述测度/矩恒等式只对 genuine full-exact
class **PROVED**，对 bare scalar `RK=1` 为 **CONDITIONAL**。

本节新增 `angular_charge_cone_r101/README.md` 与 `audit_r101.py`，审计状态为
`R101_ANGULAR_HERGLOTZ_CHARGE_CONE_AUDIT_COMPLETED`。下一步只应核对原始
`P_3K` 定义与 `chi_1` 的 zero-set 关系，若失败则转向另一个真正的 angular
Fourier sector；不要再增加没有 charge 接口的低阶 moment minors。

### 9.14 R102：log-cumulant charge symmetry theorem

网页端从早期 R4 的 angular MGF 记号恢复了 `P_3K` 的定义级接口。对 centered
variance-one law `mu`，令 `M_mu(z)=E exp(zX)`、`K_mu=log M_mu`，并取
`a_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`。定义

`mathscr K_mu(z,theta)=sum_j K_mu(z*a_j(theta))-z^2/2`,

`P_3K(mu;z)=(1/(2*pi))*int exp(-3*i*theta)*mathscr K_mu(z,theta)dtheta`.

由于 `sum a_j=0`、`sum a_j^2=1`，quadratic Gaussian 项完全消去。若
`K_mu(z)=sum_(m>=1) kappa_m z^m/m!`，则 D3 root filter 给出精确公式

`P_3K(mu;z)=sum_(m>=3, m odd) Lambda_m*kappa_m*z^m/m!`,

`Lambda_m=3*(sqrt(2/3)/2)^m*binomial(m,(m-3)/2)>0`.

本机 R102 exact audit 核验了该公式的 Laurent/Fourier 常数、`P_3K` 的
累积量投影、反射律 `P_3K(check(mu))=-P_3K(mu)`、OU 协变
`P_3K(P_t mu)(z)=P_3K(mu)(sqrt(t)*z)`，以及首个非零 odd sector 的
`[z^d]P_3K=beta_(d,1)/sqrt(d!)`。因此在局部 MGF 存在且 MGF 唯一的范围内，

`P_3K==0  iff  all odd cumulants vanish  iff  mu is symmetric`.

结合 R101 genuine full-exact、moment-determinate class 中的
`chi_1==0 iff mu symmetric`，得到该 class 内的 qualitative zero-set bridge
`P_3K==0 iff chi_1==0`。这只是 zero-set 等价，不能把两个 observable
相互替换；在首个非零 odd degree 才有上述精确线性比较，后续 degrees 有
exponentiation-induced nonlinear mixing。

这是战略性进展：若存在一个 asymmetric genuine full-exact law `h`，则
`g_N^(j)=P_(q^(N-j))h` 自动给出任意深、正的 exact tower，且
`P_3K(g_N^(0))(z)=P_3K(h)(q^(N/2)z)` 对每个有限 `N` 仍非零。故“任意深
varying-bottom tower 的非零 charge”与“存在 asymmetric genuine exact law”
在该 class 内等价；depth-independent 的普通 charge 振幅下界不可能成立。
正确的 primitive target 必须先做 OU-invariant normalization，例如
`Theta_ang=r(mu)^2*tau_ang(mu)`，而不是要求底层未归一化振幅 uniform noncollapse。

本段的证据边界：R102 的有限公式与变换律已由
`log_cumulant_charge_r102/audit_r102.py` exact audit；`P_3K` 定义本身的
历史来源由网页端恢复，需与项目原始 R4 文本继续做 provenance 对照。上述
zero-set bridge 对 genuine full-exact class 为 PROVED under the stated
analytic/MGF hypotheses，对 bare scalar `RK=1` 仍 CONDITIONAL。asymmetric
genuine exact law exclusion、primitive uniform closure、symmetric even sector
和最终 Positive Backward-Tower Exact Zero-Set Rigidity 仍 OPEN。

### 9.15 R103：asymmetric genuine exact-law exclusion 的全阶推进与障碍

R103 沿三条结构同时推进：固定实 `z` 的 Herglotz/Toeplitz positivity、
`<exp(mathscr K)>=1`、以及 iid same-factor cubic factorization。网页端给出并由
本机 `asymmetric_exact_exclusion_r103/audit_r103.py` exact audit 的新结果：

- 令 `w_z=exp(mathscr K)`、`c_r(z)=<exp(-3*i*r*theta)w_z>`、
  `R=<mathscr K>`。一阶 Szegő predictor 给出 sharp bound
  `exp(R)<=1-c_1(z)^2`；二阶 predictor、令 `b=c_2-c_1^2`，给出
  `exp(R)<=1-c_1^2-b^2`（充分小的实 `z`）。Poisson kernel 取等，故这些
  one-sided compensation inequalities 单独不能排除 asymmetry。
- 若 `d` 是首个非零 odd cumulant，same-factor exactness 强制
  `kappa_m=0`（`4<=m<2d` 且 `m` even），并强制
  `kappa_(2d)=-(2d)!/(2(d!)^2)*<p_d^2>/<p_(2d)>*kappa_d^2<0`。
  若 `q_r=[z^d]Q_r`，则有全角向能量恒等式
  `-[z^(2d)]R=sum_(r:3r<=d,r odd)|q_r|^2`。其相对 `P_3K` 首模的
  tax `T_d>=1`，且 `T_d>1` 对所有 `d>=9`。
- 对危险的 `d=3,5,7`，第二预测器仍被 same-factor 结构强制产生非零
  channel：`[z^(2d)]Q_2=-eta_d q_1^2`，其中
  `eta_d=binom(2d,d-3)/binom(2d,d)`，分别为 `1/20,5/28,7/24`。

R103 同时构造了明确的 non-genuine measure-level obstruction：
`h_0(x)=sin(x)-(exp(3/2)/2)sin(2x)`、
`f_theta=1+2*epsilon*h_0(x)cos(3theta)`（`epsilon` 足够小）。该族真实、
positive、centered、variance-one、D3/reflection-covariant，有 Gaussian
barycenter、完整 pointwise Herglotz cone 和 `<exp(mathscr K)>=1`，但其
degree-6 log-charge 比为 `1/2`，而 genuine iid same-factor law 必须为
`Lambda_(6,2)/<p_6>=(1/72)/(5/18)=1/20`，故在六阶被精确排除。它不是
genuine counterexample，而是说明前两层 probability cone 不能替代
same-factor all-degree coherence。相反，formal same-factor jet
`kappa_3=epsilon, kappa_6=-3*epsilon^2` 在六阶仍可满足 barycenter identity，
所以有限 cumulant/finite-minor 方法原则上不足以关闭问题。

因此当前战略状态进一步清晰：R103 已把“缺口”压缩为
`same-factor factorization + all-degree Schur/Herglotz coherence + one-body
probability realization` 的无限维兼容性问题；但
`genuine => P_3K=0`、primitive uniform closure、symmetric even sector 和
最终 Positive Backward-Tower Exact Zero-Set Rigidity 仍 **OPEN**。下一轮
不再增加低阶 moment minor，转攻 infinite Schur-cumulant cascade。

### 9.16 R104：Infinite Schur–Cumulant Cascade 与 Schur–Abel realization test

网页端 R104 已完成上一节指定的主攻，并把“全阶角向相容性”改写成一个可审计
的全局变换。固定 admissible 实 `z`，令

`w_z(theta)=exp(mathscr K(z,theta))`、`phi=3theta`，并以
`d sigma_z(phi)=w_z(phi/3)dphi/(2pi)` 定义单位圆上的正测度。其 Fourier moments
`c_r(z)` 组成实 Toeplitz correlation sequence。对单项式
`1,zeta,zeta^2,...` 做 OPUC/Gram–Schmidt，定义 reflection parameters

`alpha_n(z)=-Phi_(n+1)(0;z)`，

则

`E_(n+1)=E_n(1-alpha_n^2)`、`E_0=1`，

且首两项为

`alpha_0=c_1`、`alpha_1=(c_2-c_1^2)/(1-c_1^2)`，

`E_2=1-c_1^2-(c_2-c_1^2)^2/(1-c_1^2)`。

对严格正连续权，Szegő 预测极限给出

`exp(R(z))=prod_(n>=0)(1-alpha_n(z)^2)`、`R=<mathscr K>`，

或

`S(z):=sum_n -log(1-alpha_n(z)^2)=-R(z)`。

这使 R103 的有限 predictor 不再是孤立不等式，而是一个 exact infinite
prediction budget。

same-factor D3 几何给出全阶 locality/parity：

`alpha_(r-1)(z)=O(z^(3r))`、`alpha_(r-1)(-z)=(-1)^r alpha_(r-1)(z)`。

若 `d` 是首个非零 odd cumulant，则整个首阶 Schur vector 同时被激活：

`[z^d]alpha_(r-1)=Lambda_(d,r)kappa_d/d!`，

对 odd `r` 且 `3r<=d`。因此 R103 的 all-charge energy identity 正是
`S=-R` 在首个 `z^(2d)` 系数上的展开：

`-[z^(2d)]R=sum_(r:3r<=d,r odd)(Lambda_(d,r)kappa_d/d!)^2`。

另一方面，令 `A_(2N)=<p_(2N)>=3*binom(2N,N)/6^N`，则所有 forced-even
cumulants 满足严格 triangular recursion

`kappa_(2N)=-(2N)!/A_(2N) [z^(2N)]S(z)`。

只有 `r<=floor(N/3)` 的 Schur charge 能进入该阶；这为“odd free / even forced”
提供了 prediction-loss 解释，而非新的独立假设。

R104 的关键全局接口是 Abel 重构。令 `K_e(r)=(K(r)+K(-r))/2`、
`rho=sqrt(2/3)`，以及

`(A f)(r)=(2/pi)int_0^r f(s)/sqrt(r^2-s^2) ds`。

则

`A K_e(r)=r^2/4-(1/3)S(r/rho)`，

从而

`K_e(r)=r^2/2-(1/3)J(r)`、
`J(r)=d/dr int_0^r s*S(s/rho)/sqrt(r^2-s^2) ds`。

若 `K=log M` 来自 genuine probability law，则 Cauchy–Schwarz 与 CGF convexity
强制 `K_e(r)>=0`、`K_e''(r)>=0`，即

`J(r)<=3r^2/2`、`J''(r)<=3`。

这把 one-body realization 具体化为整个 Schur cascade 的两个全局实轴约束。
它们是 genuine probability constraints，不是 formal Fock 或有限 minor 结论。

本机新增 `infinite_schur_cumulant_r104/README.md` 与 `audit_r104.py`，exact
symbolic audit 通过：D3 harmonic weights、首两级 Schur 递推、grade-12
forced-even/Szegő budget、OU grade/first-odd Schur vector，以及 Abel monomial
multiplier。审计只核验有限 grade；严格正连续权下的无限乘积和 Abel inversion
属于网页端 analytic theorem，formal infinite Schur completion 仍不能代替
probability realization。

R104 的证据边界：

- `Infinite Schur–Abel Representation`：**ANALYTICALLY PROVED，LOCAL-AUDITED**；
- 任意 formal odd cumulant data 的 coefficientwise Schur completion：
  **FORMAL-PROVED，不是概率律**；
- `Schur–Abel Convexity Breakdown Lemma`：**OPEN**；
- asymmetric genuine full-exact law exclusion、symmetric even-sector rigidity、
  bare `RK=1` 到 genuine full-exact identification、以及最终
  Positive Backward-Tower Exact Zero-Set Rigidity：继续 **OPEN / CONDITIONAL**。

当前不再计算更多孤立的 `alpha_n` 低阶展开。下一轮网页端必须先阅读本总纲、
`PROJECT_WORKLOG_APPEND.md`、R103/R104 README 与 audit；主攻

`P_3K!=0 => exists r>0: J(r)>3r^2/2 or J''(r)>3`，

或给出严格反例并精确说明必须补上的 genuine Bochner 正定性。不得把
`J` 约束、formal branch 或固定 `z` 的 Schur 正性误写成最终 rigidity。

## 9.17 R105：Schur–Abel 实轴 no-go 与 genuine homometric phase obstruction

网页端 R105 完成了 R104 指定的 global real-axis route 审查，并给出一个真实
概率律层面的 phase-retrieval obstruction。本节只把有限符号与有限支撑计算记为
本机已核验的内容；无限维 phase rigidity 仍保持 OPEN。

### 9.17.1 已证的实轴 slack

由 R104 的 Abel reconstruction

`K_e(r)=r^2/2-J(r)/3`,

和 `K_e=(K(r)+K(-r))/2`，对任意具有相应实 MGF 的非退化概率律有

`J(r)=3r^2/2-(3/2)log(M(r)M(-r))`.

因此 Cauchy–Schwarz 与 tilted-variance identity 给出（`r>0`）

`J(r)<3r^2/2`, `J'(r)<3r`, `J''(r)<3`,

并且

`3r^2/2-J(r)=(3/2)log(M(r)M(-r))`,

`3-J''(r)=(3/2)(Var_{mu_r}X+Var_{mu_{-r}}X)`。

这里 `mu_{±r}` 是指数倾斜律。故 `P_3K!=0` 导致 real-axis convexity
breakdown 不是一个有独立增益的中间命题：只要非对称 genuine full-exact law
存在，它就会满足上述严格 slack，并直接反驳该 breakdown lemma；若不存在
非对称 exact law，该 lemma 只是最终排除结论的推论。

### 9.17.2 genuine homometric pair

网页端构造并由 `homometric_phase_obstruction_r105/audit_r105.py` 核验了两条
有限支撑律：

`mu_sym=(-3/2,0,3/2)` 的概率为 `(2/9,5/9,2/9)`；

`mu_asym=(-1,1/2,2)` 的概率为 `(4/9,4/9,1/9)`。

两者都 centered、variance-one，且 `m_4=9/4`；但三阶矩分别为 `0` 与 `1/2`。
令 `m(s)=2/3+e^s/3`，则

`M_sym(r)=m(3r/2)m(-3r/2)`,

`M_asym(r)=e^{-r}m(3r/2)^2`,

从而

`M_sym(r)M_sym(-r)=M_asym(r)M_asym(-r)`。

因此两律有相同差分律、自相关、`K_e`、`J` 与 `|phi|^2`，但对称性不同。
这是 genuine probability obstruction，不是形式 jet；它不是原项目的
counterexample，因为 full-exact 四阶条件为 `kappa_4=0`，即 `m_4=3`，而两律
均有 `m_4=9/4`。

### 9.17.3 exactness 四阶审计与路线转向

若 `Z(z)=<exp(mathscr K(z,theta))> = 1` 是 genuine full-exact identity，则
`<p_4>=1/2`，且三阶项平方到六阶才出现，所以四阶系数为 `kappa_4/48`，从而
`kappa_4=0`、`m_4=3`。这一步已由本机 exact symbolic audit 通过。

R105 的战略结论是：Schur–Abel cascade 已恢复 one-body autocorrelation，剩余
Gaussian rigidity 是 same-factor cubic constraint 下的 Bochner characteristic
phase-rigidity，而非实轴 convexity 问题。项目的 bare `RK=1` 到 genuine
full-exact law 的识别仍 **CONDITIONAL**。

### 9.17.4 R106 最小 OPEN

**Exact-Constrained Bochner Phase-Lift Rigidity — OPEN**：给定 R104/R105
重构出的 difference law `D` 与 `psi=widehat D`，研究满足

`|phi(y)|^2=psi(y)`, `phi(0)=1`, `EX=0`, `EX^2=1`,

`<prod_j phi(a_j(theta)y)> = e^{-y^2/2}`

的所有 characteristic phase lifts，能否证明 `phi(y)=phi(-y) in R`。

网页端提出的最尖锐子引理是

`<prod_j |phi(a_j y)|> <= e^{-y^2/2}`。

它尚未证明；exact identity 通过三角不等式只给出相反方向
`e^{-y^2/2} <= <prod_j |phi(a_j y)|>`。因此 phase alignment、odd-cumulant
消失、非对称 exact-law exclusion 与最终 positive backward-tower rigidity
继续 **OPEN**。禁止将该反向模不等式当作已证结论，也不得以 numerical sweep、
SDP、optimizer 或 remote computation 代替它。

## 9.18 R106：Exact-constrained Bochner phase lift 与首个 modulus excess

网页端 R106 完成了 R105 指定的 phase-lift 审查。本节将候选反向模长上界的
逻辑地位和 genuine Bochner 的新接口分开记录；本轮没有把 conditional branch
升级为主命题的证明。

### 9.18.1 exact phase-defect identity

令 `F_y(theta)=prod_j phi(a_j(theta)y)=r_y(theta)exp(iV_y(theta))`、
`A(y)=<r_y>`、`g(y)=exp(-y^2/2)`，并以 `r_y/A(y)` 加权得到 `pi_y`。由
full exactness，`E_(pi_y)exp(iV_y)=g(y)/A(y)`，从而得到

`A(y)-g(y)=2A(y)E_(pi_y)sin^2(V_y/2)>=0`。

所以 R105 的候选 `A<=g` 在局部非零区间内等价于 triangle equality、phase
alignment；结合 R102 的 analytic charge identification，它与 `P_3K=0`、
对称性及局部 exact equality 等价。该等价链不是一个独立的 modulus bridge。

### 9.18.2 conditional first excess

若 hypothetical genuine full-exact law 满足 `P_3K!=0`，令首个非零 odd degree
为 `d`，R103 的 all-charge energy 为

`S_d=sum_(r:3r<=d,r odd)|q_r|^2>0`。

R103/R104 的 exact even-sector cancellation 给出
`A(y)/exp(-y^2/2)=1+S_d y^(2d)+O(y^(2d+2))`，且
`S_d=1/2<V_d^2>`。因此非对称 exact branch 会在小非零 `y` 上严格满足
`A(y)>exp(-y^2/2)`。这是 **CONDITIONAL** genuine obstruction，而不是已构造
的反例。

### 9.18.3 genuine three-point Bochner interface

任意 characteristic function 满足

`|phi(x+v)-phi(x)phi(v)|^2 <= (1-|phi(x)|^2)(1-|phi(v)|^2)`。

取 `x=a_1y`、`v=a_2y`，利用 `a_1+a_2=-a_3`，得
`1+2r_1r_2r_3cos(V_y)-(r_1^2+r_2^2+r_3^2)>=0`。

令 `psi=|phi|^2`、`rho=sqrt(2/3)`，平均并使用 exact identity，得到新的
phase-free necessary condition

`3<psi(rho y cos(theta))>_theta <= 1+2exp(-y^2/2)`.  (20)

同时，`0<=A-g<=1/2[1+2A-3<psi(rho y cos(theta))>]`。这把相位缺陷和
difference-law 的 Bochner budget 分开，是下一轮比反向模长上界更合适的接口。
它只涉及 R105 已重构的差分律/自相关数据，但单靠当前三点约束还没有证明
非零 odd charge 必然造成 breakdown。

### 9.18.4 证据边界与 R107

本机新增 `bochner_phase_lift_rigidity_r106/README.md` 与 `audit_r106.py`；
有限符号 audit 只核验 phase-defect algebra、三点 Bochner reduction、平均约束
以及首项系数，不替代 infinite-dimensional phase-lift proof。

R107 最小 OPEN 为 `P_3K!=0` 是否必导致某个有限 `y!=0` 上的严格反向
`3<psi(sqrt(2/3)y cos(theta))> > 1+2exp(-y^2/2)`。若不能，应进入 higher-point
Bochner constraints；不得重开 R99–R106，也不得使用 numerical sweep、SDP、
optimizer 或 remote computation。

## 9.19 R107：三点 Bochner breakdown 的 genuine obstruction 与四点升级

网页端 R107 对 R106 的 Difference–Bochner Breakdown Lemma 给出否定性的结构
判决：该 breakdown 在 genuine full-exact 类内与排除 asymmetric exact law 等价，
不可能从一个本来对所有 genuine law 都成立的必要条件独立推出。更强的是，
存在一个 genuine、同 difference law、同 `m_4=3`、但含 nonzero odd charge 的
obstruction，使三点条件本身无法识别 symmetry。

### 9.19.1 exact-fourth homometric Bernoulli-convolution pair

取 `p(1-p)=1/6`、`a=sqrt(3)`，令 `B_1,B_2` 为独立 Bernoulli(p)，定义

`X_sym=a(B_1-B_2)`、`X_asym=a(B_1+B_2-2p)`。

二者均 centered、variance-one、`m_4=3`，但 `m_3` 分别为 `0` 与 `1`，且
两者的第六累积量都是 `kappa_6=-6`。若 `m(s)=1-p+p exp(s)`，则

`M_sym(r)=m(ar)m(-ar)`、
`M_asym(r)=exp(-2par)m(ar)^2`，

所以 `M_sym(r)M_sym(-r)=M_asym(r)M_asym(-r)`。这给出完全相同的
`psi=|phi|^2`/difference-law 数据，但对称性不同。它不是 full-exact counterexample：
degree-six same-factor fingerprint 要求 `kappa_6=-3m_3^2`，而非对称 law
给出 `-6`。

对 `X_lambda=sqrt(lambda)X+sqrt(1-lambda)G` 作有限 OU/Gaussian smoothing，
二者仍同 `psi` 且 `m_4=3`；非对称分支有 `m_3=lambda^(3/2)`、
`kappa_6=-6lambda^3`，保持 `P_3K!=0`，但仍不满足 degree-six exactness。

### 9.19.2 三点条件对充分强平滑全局成立

令 `B_lambda(y)=1+2exp(-y^2/2)-3<psi_lambda(sqrt(2/3)y cos(theta))>`。
由 `psi_lambda(t)=psi_0(sqrt(lambda)t)exp(-(1-lambda)t^2)`，在 `lambda=0`
时令 `x=y^2/3`，有

`B_0(y)=1+2exp(-3x/2)-3exp(-x)I_0(x)`。

等价地比较 `cos(theta)` 与离散律 `V in {1,-1/2}`（概率 `1/3,2/3`）的
MGF。它们的 0、1、2 阶矩相同；奇数阶 `n>=3` 中 `E V^n>0=E cos(theta)^n`，
偶数阶 `n>=3` 中 `E V^n>1/3` 而 `E cos(theta)^n<=5/16<1/3`。逐项比较给
`B_0(y)>0` 对 `y!=0`。原点附近平滑族的首项为

`B_lambda(y)=((1-lambda^3)/216)y^6+O(y^8)`；

结合紧区间连续性和远端高斯尾界，得到某个 `lambda_0>0`，使所有
`0<lambda<lambda_0` 时 `B_lambda(y)>0` 对所有实 `y!=0` 成立。

因此 genuine nonzero-charge、exact-fourth 的 law 可以全局满足 R106 三点
Difference–Bochner inequality；三点 difference/autocorrelation 数据不能完成
phase rigidity。这是对 R107 原命题的 genuine obstruction，而不是主问题反例。

### 9.19.3 最小新的对象是四点 multiplicative Gram

三点层被上述 obstruction 钉死后，取 `x=a_1y`、`z=-a_2y`、
`U=exp(ixX)`、`V=exp(izX)`，对 `U-u,V-v,UV-w` 的协方差矩阵

`Gamma_4 = [[1-|u|^2, c-u*conj(v), conj(v)-u*conj(w)],
            [conj(c)-conj(u)*v, 1-|v|^2, conj(u)-v*conj(w)],
            [v-conj(u)*w, u-conj(v)*w, 1-|w|^2]] >= 0`,

其中 `u=phi(x)`、`v=phi(z)`、`w=phi(x+z)`、`c=phi(x-z)`。其上方 `2x2`
block 是 R106 三点约束，第三行/列首次引入 companion frequency
`w=phi((a_1-a_2)y)`。若 `C>0`，等价 Schur complement 为
`q^*C^(-1)q<=1-|w|^2`，其中
`q=(conj(v)-u*conj(w),conj(u)-v*conj(w))^T`。

四点足够完成 rigidity 仍 **OPEN**，但它是当前最小合理的 phase-coherence
对象。R108 必须把该矩阵与 same-factor exact identity 做 angular averaging，
寻找不能塌缩为 `psi` 的 signed functional；若四点仍完全塌缩，才进入五点层。

### 9.19.4 证据边界

本机新增 `bochner_breakdown_obstruction_r107/README.md` 与 `audit_r107.py`。
有限概率/矩/同自相关、OU 累积量缩放、三点 `y^6` 系数和四点 Schur 结构均
**PROVED / LOCAL-AUDITED**。充分小 `lambda` 的全局三点不等式为网页端给出的
解析连续性+尾界证明，记录为 **ANALYTICALLY PROVED**，但不冒充 full-exact
反例。asymmetric genuine exact-law exclusion、四点 phase rigidity、bare `RK=1`
识别和最终 positive backward-tower theorem 继续 **OPEN**。

## 9.20 R108：Four-point bispectrum separation 与 shear-cocycle interface

网页端 R108 在 R107 的四点 candidate 上完成了一个重要的结构升级：四点
multiplicative Bochner 层没有塌回 `psi=|phi|^2`，而是第一次留下真正的
bispectrum phase / phase-cocycle 信息。但最浅的四点 principal minor 仍只恢复
旧的 `m_3^2<=2` cone wall，因此不能把四点本身宣布为 rigidity theorem。

### 9.20.1 四点 Gram 与精确 Schur 残差

取

`a_1=sqrt(2/3) cos(theta)`、
`a_2=sqrt(2/3) cos(theta+2pi/3)`、
`a_3=sqrt(2/3) cos(theta-2pi/3)`，

令 `x=a_1y`、`z=-a_2y`、`U=exp(ixX)`、`V=exp(izX)`，并写
`u=phi(x)`、`v=phi(z)`、`w=phi(x+z)`、`c=phi(x-z)`。对
`U-u,V-v,UV-w` 的 covariance Gram 有

`Gamma_4 = [[1-|u|^2, c-u*conj(v), conj(v)-u*conj(w)],
            [conj(c)-conj(u)*v, 1-|v|^2, conj(u)-v*conj(w)],
            [v-conj(u)*w, u-conj(v)*w, 1-|w|^2]] >= 0`。

其左上 `2x2` block `C` 是 R106 三点约束；若 `C>0`，令
`q=(conj(v)-u*conj(w),conj(u)-v*conj(w))^T`，则新信息是

`1-|w|^2-q^*C^(-1)q>=0`。

清除 `det C` 后，`det Gamma_4` 的 phase terms 为

`4 Re(c*conj(u)*v)+4 Re(u*v*conj(w))`
`-2 Re(c*conj(u)^2*w)-2 Re(c*v^2*conj(w))`。

其中第一项在 full exact angular average 中被 exact identity 固定，最后两项
则保留相邻 bispectrum cycles 的相位相容性。

### 9.20.2 椭圆坐标与 bispectrum

令 `s=a_2y`、`t=(a_1-a_2)y`。则
`a_1y=s+t`、`a_2y=s`、`a_3y=-(2s+t)`，且固定 `y` 的椭圆为

`6s^2+6st+2t^2=y^2`。

定义 `B(s,t)=phi(s)phi(t)conj(phi(s+t))`。full exact identity 正好是

`<B(s,s+t)>_{E_y}=exp(-y^2/2)`。

另一方面，四点 `U,UV` principal minor 给出

`1+2 Re B(s,t)-psi(s)-psi(t)-psi(s+t)>=0`。

角向平均，令 `Q_4=Re<B(s,t)>_{E_y}`、
`H_c=<psi(cy cos(theta))>`、`rho=sqrt(2/3)`，得到

`1+2Q_4-2H_rho-H_sqrt2>=0`。

这是四点层的第一个 phase-sensitive 必要条件。R107 homometric pair 在同一
`psi` 下满足 `kappa_3=0` 与 `lambda^(3/2)`，而 `Q_4` 对应系数
`(-a_1,a_2,a_1-a_2)`，有 `<(sum b_j^3)^2>=5/4`，故

`Q_4,asym-Q_4,sym=-5lambda^3 y^6/288+O(y^8)`。

因此 `Q_4` 不能由 difference law 或 `psi` 重构。这条结论已由本机 exact
audit 核验，是 R105/R107 autocorrelation ambiguity 到 R108 bispectrum
coherence 的实质推进。

### 9.20.3 完整四点 phase functional

令 `f_j=phi(a_jy)`、`h=phi((a_1-a_2)y)`，并定义

`T_4=Re<conj(f_3)*conj(f_1)^2*h>`、
`mathfrak Q_4=Q_4-T_4`。

由 `det Gamma_4` 的 exact 展开、full exact identity 及 reflection symmetry，
完整 angular-averaged Schur inequality可写为

`P_psi+4exp(-y^2/2)+4mathfrak Q_4>=0`，

其中 `P_psi` 完全由 `psi` 决定。`T_4` 的系数 multiset 是
`(-a_3,-a_1,-a_1,a_1-a_2)`，并有
`<(sum b_j^3)^2>=4/3`。同一 homometric pair 给出

`T_4,asym-T_4,sym=-lambda^3 y^6/54+O(y^8)`，

从而

`mathfrak Q_4,asym-mathfrak Q_4,sym=lambda^3 y^6/864+O(y^8)`。

所以四点完整 Schur 残差也不能由 difference law 重构。以局部 phase
`phi(r)=|phi(r)|exp(i vartheta(r))` 表示时，`T_4` 测量的正是

`delta(s,t)-delta(s,s+t)`，其中
`delta(s,t)=vartheta(s)+vartheta(t)-vartheta(s+t)`。

这给出了四点层真正的新对象：shear `(s,t)->(s,s+t)` 下相邻 bispectrum
cocycle 的相容性。

### 9.20.4 可关闭的条件接口与首阶边界

若局部 `B(s,t)>0`，则 `delta(s,t)=0`，连续 Cauchy 方程、centered 条件和
解析唯一性给出 `P_3K=0`。更贴合完整 Schur 项，若原点邻域内

`delta(s,t)=delta(s,s+t)`，

则 `vartheta(t+2s)-2vartheta(t+s)+vartheta(t)=0`，二次求导得到
`vartheta''=0`，再由 centered 得 `vartheta=0`，同样推出 `P_3K=0`。

这两个是 **PROVED conditional interfaces**，而不是对 full exact branch 的无条件
结论。因为在 genuine full-exact branch 中，四点 companion principal minor 的
首阶仍为

`1+2Q_4-2H_rho-H_sqrt2=5(2-m_3^2)y^6/144+O(y^8)`，

仅恢复旧约束 `m_3^2<=2`。

### 9.20.5 证据边界与 R109

本机新增 `four_point_bispectrum_shear_r108/README.md` 与 `audit_r108.py`，
核验了：四点 Gram/Schur determinant、椭圆坐标、bispectrum cycle rewrite、
`Q_4/T_4` 的同模长分离、anisotropic quadratic form 的系数矩、Gaussian
anchor 及 full-exact 首阶。网页端给出的 phase separation 现标为
**PROVED / LOCAL-AUDITED**。

pointwise shear alignment 是否可由 `Gamma_4>=0` 加
`<B(s,s+t)>_{E_y}=exp(-y^2/2)` 推出，仍为 **OPEN**；bare `RK=1` 到 genuine
full-exact、asymmetric exact-law exclusion 和最终 positive backward-tower
rigidity 也仍为 **OPEN**。

因此 R109 不应立即升级到五点。当前最小命题是
**Four-Point Shear–Bispectrum Alignment Lemma**：在 local zero-free
characteristic neighborhood 内，证明或反驳上述四点条件是否推出
`delta(s,t)=delta(s,s+t)`。只有找到保留 nonzero shear cocycle 的 genuine
characteristic phase lift，才进入五点 Gram。

## 9.21 R109：Parallelogram Bochner cocycle disk 与 exactness gap

网页端 R109 对 R108 的 Shear–Bispectrum Alignment Lemma 给出了否定性的独立
判决：四点条件本身不能推出 pointwise shear alignment。它同时给出一个 sharp
cocycle disk，并把真正缺失的机制压缩为 elliptic modulus saturation；这不是
退回三点，而是对“exact average 如何变成 pointwise 控制”的精确定位。

### 9.21.1 公共 edge Schur 分解

令 `a=phi(s)`、`b=phi(t)`、`c=phi(s+t)`、`d=phi(2s+t)`。频率集合
`{0,s,s+t,2s+t}` 的 Gram 为

`G_4=[[1,conj(a),conj(c),conj(d)],
     [a,1,conj(b),conj(c)],
     [c,b,1,conj(a)],
     [d,c,a,1]]>=0`。

沿公共 edge `{0,s}` 做 Schur 消元，令

`Delta_0=1+2Re(a*b*conj(c))-|a|^2-|b|^2-|c|^2`、
`Delta_1=1+2Re(a*c*conj(d))-|a|^2-|c|^2-|d|^2`，

`N=conj(a)(1-|a|^2+|c|^2)-b*conj(c)-c*conj(d)+a*b*conj(d)`。

则在 `0<|a|<1` 时

`G_4/A_s=(1/(1-|a|^2))*[[Delta_0,N],[conj(N),Delta_1]]`，

从而四点 PSD 的新增条件精确为

`|N|^2<=Delta_0*Delta_1`。

这是 R109-A 的 sharp four-point cocycle inequality；本机
`parallelogram_bochner_cocycle_r109/audit_r109.py` 已精确核验矩阵分解。

### 9.21.2 shear phase 的圆盘而非等式

若 `r_0=|a|`、`r_1=|b|`、`r_2=|c|`、`r_3=|d|`，
`delta_0=arg(ab*conj(c))`、`delta_1=arg(ac*conj(d))`、
`eta=delta_0-delta_1`，则 `N=conj(a)Xi` 且

`Xi=P+exp(-i*eta)Q`，

`P=1-r_0^2+r_2^2-(r_1r_2/r_0)exp(i*delta_0)`、
`Q=exp(i*delta_0)(-r_2r_3/r_0+r_1r_3exp(i*delta_0))`。

因此 `exp(-i*eta)` 位于单位圆与闭圆盘的交集。一般该可行域是一个 arc，
而不是单点；四点 pointwise PSD 没有自动强迫 `eta=0` 的 equality mechanism。

Gaussian kernel 在四个频率互异时严格正定，故 `Delta_0>0`、`Delta_1>0`、
`|N|^2<Delta_0Delta_1`。Gaussian alignment point 在 disk 严格内点，说明
不存在仅依赖四点 PSD slack 的 pointwise phase-rigidity 证明。

### 9.21.3 genuine 与 formal 的互补 obstruction

R107 的 OU-smoothed asymmetric homometric law 是 genuine probability law，
故原点邻域 zero-free 且所有 `Gamma_4` 自动 PSD；其
`kappa_3=lambda^(3/2)` 给出

`eta(s,t)=-lambda^(3/2)s^2(s+t)+O((|s|+|t|)^5)`。

它实现了 `Gamma_4>=0` 但 `delta(s,t)!=delta(s,s+t)`。不过它不是 full-exact
law。用 R103/R104 的 exactness functional `Z`，其六阶系数为

`[z^6](Z-1)=(kappa_6+3kappa_3^2)/2592=-lambda^3/864`，

沿 `z=iy` 则
`Z(iy)=1+lambda^3 y^6/864+O(y^8)`。

反过来，R104 的 formal exact Schur cascade 可保留
`kappa_3!=0`、`kappa_6=-3kappa_3^2` 和 coefficientwise `Z=1`，但没有
probability realization。因此真正 OPEN 的正是 genuine characteristic
realization 与 full exactness 的交集。

### 9.21.4 Alignment 与主 asymmetric exclusion 同层级

在 genuine full-exact analytic/MGF class 内，四点 Gram 与 ellipse identity 对
每个 law 都自动成立；而 R108-E 已证明

`delta(s,t)=delta(s,s+t) locally => P_3K=0`。

结合 R102 的 `P_3K=0` 与 symmetry 接口，得到：在该 class 内，所有 law 都满足
shear alignment 与排除 asymmetric genuine exact law 是同一个命题，R109 不是
更弱的独立中间定理。

### 9.21.5 真正缺失输入：elliptic modulus saturation

一个足以关闭非对称 sector 的条件是 exact ellipse 上逐点满足

`|B(s,s+t)|<=exp(-y^2/2)`、`6s^2+6st+2t^2=y^2`。

由于 exactness 给出 `<B(s,s+t)>_{E_y}=exp(-y^2/2)`，有

`exp(-y^2/2)=|<B>|<=<|B|> <= exp(-y^2/2)`。

故所有不等式取等，`B` 逐点正且模长饱和；局部 Cauchy 方程、centered 条件和
解析唯一性推出 `vartheta=0`、`P_3K=0`。更强但更简单的充分条件是局部
`|phi(r)|<=exp(-r^2/2)`，它通过
`s^2+(s+t)^2+(2s+t)^2=y^2` 立即推出 product majorant。

这说明 positive backward divisibility 可能需要贡献的不是更多 pointwise Gram，
而是一个 uniform modulus domination/saturation mechanism；varying-bottom tower
能否提供它仍为 **OPEN**。

### 9.21.6 证据边界与 R110

本机新增 `parallelogram_bochner_cocycle_r109/README.md` 与 `audit_r109.py`，
核验了 parallelogram Gram、公共 edge Schur 分解、cocycle disk factorization、
shear 三阶展开、六阶 exactness gap 和椭圆 product geometry。R109 的 sharp
四点 disk 与 genuine/formal obstruction 分别标为 **PROVED / LOCAL-AUDITED**、
**ANALYTICALLY PROVED** 与 **FORMAL**；elliptic modulus saturation、asymmetric
genuine exact-law exclusion 和最终 positive backward-tower rigidity 继续
**OPEN**。

下一轮不升五点，先攻 **Elliptic Modulus-Saturation Lemma**：从 Schur–Abel
difference data、四点 cocycle disk 与 positive backward-preimage cone 出发，
证明或反驳局部 product majorant。只有出现 genuine obstruction，才进入五点 Gram。

## 9.22 R110：Gaussian-relative modulus defect 与 q^(3N) 尺度

网页端 R110 在连接器账户错误的情况下仍给出了可独立复核的 provisional
解析推导；本机新增 elliptic_modulus_defect_r110/README.md 与
audit_r110.py，并把网页端通信限制与数学证据严格分开。

### 9.22.1 缺陷 transport 与有限深度上界

对原点邻域定义

L_mu(r)=log|phi_mu(r)|+r^2/2。

若 mu=P_tau nu，则 OU characteristic transport 精确给出

L_(P_tau nu)(r)=L_nu(sqrt(tau)r)。

故 g^(0)=P_(q^N)g^(N) 时

L_(g^(0))(r)=L_(g^(N))(q^(N/2)r)。

只用 |phi_(g^(N))|<=1 则有

|phi_(g^(0))(r)|<=exp(-(1-q^N)r^2/2)，

以及 R109 椭圆上的 product bound

|phi(s)phi(s+t)phi(2s+t)|
<=exp(-(1-q^N)y^2/2)，

其中 y^2=6s^2+6st+2t^2。这是无条件但仅为 q^N 二次尺度的上界，不能
偷换为 Gaussian modulus domination。

### 9.22.2 首个 odd charge 的严格局部反号

在 R103/R104 的 same-factor exact analytic 输入下，首个非零 odd cumulant kappa_d
强制一个负的 kappa_(2d)，并使

L_mu(r)=c_d*kappa_d^2*r^(2d)+O(r^(2d+2))，c_d>0。

特别地，R103/R104 的六阶 fingerprint kappa_6=-3*kappa_3^2 给出

L_mu(r)=kappa_3^2*r^6/240+O(r^8)。

因此 hypothetical asymmetric exact branch 在小非零椭圆上严格产生 positive
product defect M=L(s)+L(s+t)+L(2s+t)>0，正好反向于 R109 的
elliptic modulus-saturation 目标。这是排除命题的局部符号接口，不是已构造的
exact-law counterexample。

### 9.22.3 varying-bottom obstruction 与 clean conditional theorem

R107 的 genuine asymmetric exact-fourth law H 满足
kappa_3=1,kappa_4=0,kappa_6=-6。令

g_N^(j)=P_(q^(N-j))H。

它给出任意有限深度的 positive OU chain，但

L_(g_N^(0))(r)=q^(3N)r^6/120+O(q^(4N)r^8)>0

在小非零频率上成立。它不是 full-exact counterexample，因为 full exactness
要求的六阶值应为 -3。该例说明 varying-bottom 不能仅靠 finite depth 推出
L<=0，并且 q^(3N) 是真实可达到的局部尺度。

若另有统一常数 C_*,r_*>0 使整个底层类满足

|L_mu(u)|<=C_*|u|^6（|u|<=r_*），

则严格得到

|L_(g^(0))(r)|<=C_*q^(3N)|r|^6

及椭圆版本

|M_(g^(0))(s,t)|<=C_*q^(3N)y^6，

在 |r|<=r_*q^(-N/2) 的量词下成立。这是可报告的 clean conditional theorem。

### 9.22.4 证据边界与下一轮

本机 audit 已核验 OU defect transport、q^N positivity majorant、椭圆几何、
d=3 的 1/240 系数、R107 H 的矩/cumulant 与 q^(3N) 展开，以及条件
定理的幂和代数。R12 本身没有记录 C_*,r_* 的统一 modulus envelope；R101
关于 square-exponential envelope 的 moment-determinacy 假设也不能自动替代它。

因此当前等级为：上述有限结构 PROVED / LOCAL-AUDITED；首个 odd charge 的
反号为 ANALYTICALLY PROVED under exactness inputs；统一 q^(3N) theorem
为 CONDITIONAL；genuine asymmetric exact-law exclusion、varying-bottom
uniform modulus domination 与最终 Positive Backward-Tower Exact Zero-Set
Rigidity 仍 OPEN。

下一最小命题改为 Uniform q^(3N) Modulus-Defect Theorem：从 positive
backward-preimage cone、R104 Schur–Abel 约束和 genuine probability realization
中真实推出（或反驳）统一 C_*,r_*，不得把条件包络当作既有输入。

## 9.23 R111：统一 square-exponential moment 是 uniform modulus 的显式来源

网页端 R111 因 connector 三次账户错误未能新增网页端 LOCAL-AUDITED 结论，但
它准确指出最小缺口是统一 zero-free disk。本机随后新增
uniform_modulus_source_r111/README.md 与 audit_r111.py，在显式假设下补齐
这条 analytic bridge。

### 9.23.1 显式 zero-free disk

若 centered variance-one law 类 C 存在与成员无关的 a>0,B<infinity，满足

sup_(mu in C) E_mu exp(aX^2)<=B，

令

rho=min(sqrt(a)/2,sqrt(a*e/(8B)))。

由中心化 Taylor remainder、Young inequality 和
X^2 exp(aX^2/2)<=2 exp(aX^2)/(a e) 得

|M_mu(z)-1|<=B|z|^2 exp(|z|^2/(2a))/(a e)<=exp(1/8)/8<1/2

在 |z|<=rho 上成立。因此 MGF 在统一圆盘内 zero-free，K=log M 可取统一
branch，且 |K(z)|<=log 2。Cauchy 给出

|kappa_n|/n!<=log(2)/rho^n。

### 9.23.2 显式 conditional q^(3N) theorem

若再有 kappa_4=0，则在 r_*=rho/2 上

|L_mu(u)|<=2 log(2)|u|^6/rho^6。

由 R110 exact transport，任意
g^(0)=P_(q^N)g^(N) 满足

|L_(g^(0))(r)|<=C_*q^(3N)|r|^6，
C_*=2 log(2)/rho^6，

只要 |r|<=r_*q^(-N/2)。R109 椭圆上相应有

|M_(g^(0))(s,t)|<=C_*q^(3N)y^6

及 Gaussian product modulus 的双边指数夹逼。审计核验了 radius constants、
几何幂和、OU 六阶缩放与 R103/R104 的 d=3 正号接口。

### 9.23.3 重要边界与下一步

该结果把 R110 的“存在统一解析包络”升级为可引用的显式条件定理，但没有
证明项目 exact positive backward class 满足 E exp(aX^2)<=B。R12 仍只有
parity/Fredholm exact defect map，R101 只引用 square-exponential envelope
作 moment-determinacy 输入；二者都没有给出这里所需的统一 a,B。

更重要的是 absolute bound 不提供 L<=0 的符号；R110 的首个 odd charge
仍会给出正 defect。因此主问题的关键缺口已从“统一解析性”进一步收缩为：
能否从 positive backward cone、Schur–Abel 和 exact realization 得到统一
square-exponential moment，继而再找到 primitive charge annihilation 或带符号
estimate。该层仍为 CONDITIONAL/OPEN。

## 9.24 R112：genuine exact class 的统一 square-exponential envelope

网页端 R112 在 connector 仍不可读时依据 R111 自包含桥完成了一个重要的
全局化推导。本机新增 uniform_subgaussian_exact_r112/README.md 与
audit_r112.py；网页端答复与本机审计都严格把 genuine full-exact angular
realization 和 bare scalar RK=1 区分开。

### 9.24.1 R101 angular realization 给出的 radial law

对 iid X_1,X_2,X_3，令

Q=sum_j(X_j-X_bar)^2、D=X_1-X_2。

在 genuine full-exact angular barycenter 的 measure realization 下，R101 的
radial transform 识别

Q~chi^2_2，E exp(tQ)=1/(1-2t)（0<=t<1/2）。

这一步不是抽象 Herglotz Toeplitz cone 的结论；它使用 Gaussian angular
barycenter 加 iid same-factor realization。因而从 bare RK=1 推到这里仍需
单独的 identification theorem。

### 9.24.2 一步 deterministic inequality 加 Jensen

本机精确核验了

2Q-D^2=(X_1+X_2-2X_3)^2/3>=0，

故对 0<a<1/4

E exp(aD^2)<=E exp(2aQ)<=1/(1-4a)。

取独立副本 X'，由 E[X-X'|X]=X 与 exp(a x^2) 的严格凸性，

E exp(aX^2)<=E exp(a(X-X')^2)。

于是得到 genuine exact one-body 的统一 envelope

E exp(aX^2)<=1/(1-4a)、0<a<1/4，

特别是 E exp(X^2/8)<=2。该常数与 law、depth、varying-bottom 层号无关。

### 9.24.3 R110/R111 bridge 的 unconditional genuine-class 版本

把 a=1/8,B=2 代入前两轮的 explicit zero-free bridge，可取

rho=sqrt(e/128)、r_*=sqrt(e/512)、
C_*=2^22 log(2)/e^3。

每个 genuine full-exact layer 因而统一满足

|L_mu(u)|<=C_*|u|^6、|u|<=r_*。

若 g^(0)=P_(q^N)g^(N)，则严格得到

|L_(g^(0))(r)|<=C_*q^(3N)|r|^6、
|r|<=r_*q^(-N/2)，

以及 R109 椭圆三点的

|log(prod_j|phi(r_j)|/exp(-y^2/2))|<=C_*q^(3N)y^6。

中间层同样有 q^(3(N-j)) 的精确缩放。这一层的 uniform analytic radius、
sixth-order remainder 和 q^(3N) modulus scale 已从 CONDITIONAL 提升为
genuine full-exact class 下的 PROVED / ANALYTICALLY PROVED。

### 9.24.4 全局路线的真正变化

R112 排除了 varying-bottom 的 analytic escape：困难不再是 tail constants 漂移、
MGF zero-free radius 缩小或 sixth-order remainder 爆炸。剩余瓶颈纯化为

O(q^(3N)y^6) modulus budget 如何约束 R109 的 shear phase mismatch，

以及如何由此 annihilate nonzero primitive odd charge。绝对小量控制仍不能给出
L<=0，因为 R110 的首个 odd charge 局部 defect 正号。

因此下一轮不再研究 tail/envelope，定为 Uniform Shear-Cocycle Budget
Theorem：从 R109 sharp four-point cocycle disk 和 R112 uniform modulus
budget 出发，证明一个 q^(3N/2)y^3 或 square 型 phase budget，或构造
最小 genuine/formal obstruction。bare RK=1 identification 和最终
Positive Backward-Tower Exact Zero-Set Rigidity 仍为 OPEN。

## 9.25 R113：Uniform shear-cocycle budget 与 primitive cubic limit

网页端 R113 继续沿 R109/R112 的自包含输入推进；connector 未恢复读取能力，
故通信状态与数学证据分开记录。本机新增
`uniform_shear_cocycle_budget_r113/README.md` 与 `audit_r113.py`，只把
可逐项核验的代数标为 LOCAL-AUDITED。

### 9.25.1 Gaussian 邻域的四点 disk slack

沿 R109 的四频率配置令

`a=phi(s)`、`b=phi(t)`、`c=phi(s+t)`、`d=phi(2s+t)`，
`V0=s*t*(s+t)`、`V1=s*(s+t)*(2s+t)`，并令
`y^2=s^2+(s+t)^2+(2s+t)^2`。

网页端给出 centered variance-one 且 `m4=3` 时的邻域展开

`Delta0=((2-m3^2)/4)V0^2+O(y^8)`，
`Delta1=((2-m3^2)/4)V1^2+O(y^8)`，
`N=((2-m3^2)/4)V0V1+O(y^7)`。

`Delta0Delta1-|N|^2` 的 degree-12 terms cancel；Gaussian leading slack
为

`S_G=det(H3)/144*s^6*t^2*(s+t)^4*(2s+t)^2+O(y^16)`。

Gaussian moment Gram `H3` 的 determinant 是 12，因此 generic coefficient 是
`1/12`，通常严格为正。由此 Gaussian alignment 位于四点 disk 内部；
R109 pointwise PSD 没有 equality-rigidity，也不能单独提供 q,N 衰减。

### 9.25.2 从 analytic phase transport 得到的粗预算

局部 phase 的 leading term 为

`vartheta(u)=-m3*u^3/6+O(u^5)`，
`eta=vartheta(t)-2*vartheta(s+t)+vartheta(2s+t)`
`   =-m3*s^2*(s+t)+O(y^5)`。

但可用的 uniform bound 不是从 modulus slack 开平方，而是来自 R112 的统一
zero-free analytic logarithm。令 `tau=q^(N-j)`，则 exact OU phase transport
为 `vartheta_j(r)=vartheta_bottom(sqrt(tau)r)`。取

`rho=sqrt(e/128)`、`r_*=rho/2`、
`C_ph=2(3+2sqrt(2))*log(2)/rho^3`，

利用 `|s+t|,|2s+t|<=|y|` 与 `|t|<=sqrt(2)|y|`，在
`|y|<=r_*tau^(-1/2)` 上有

`|eta_j(s,t)|<=C_ph*tau^(3/2)|y|^3`，
`|eta_j(s,t)|^2<=C_ph^2*tau^3|y|^6`。

所以粗 phase scale `q^(3N/2)y^3` 已在 genuine full-exact analytic class
下得到；R107 varying-bottom 例的非 full-exact branch 表明该尺度一般不可仅
靠 probability、positivity 和 finite backward chain 改善。

### 9.25.3 全局判断与 R114

R113 的意义是把“modulus 是否能推出 phase budget”这个中间问题关闭为：
有 uniform analytic input 时可以得到 phase budget，但四点 disk 本身仍是
strict interior cone，不能给 primitive phase annihilation。R107 的
`kappa6=-6` 与 full-exact d=3 fingerprint `kappa6=-3kappa3^2` 的差异
说明真正缺口是 full exactness 对 primitive odd phase 的额外约束。

因此下一最小命题是 R114 **Primitive Cubic Shear Limit**：令
`tau=q^N`，精确计算

`tau^(-3)*(Delta0Delta1-|N|^2-S_G)`

并同步计算 exact angular `tau^3` limit。若 normalized four-point limit
仍只是旧 cone，则得到明确 four-point no-go；若它强制 primitive coefficient
`c_N` 消失，则 cubic sector 关闭。两种结果都比继续做未定向的 radial Fock
展开更接近主命题。

R113 证据边界：cubic shear identity、ellipse geometry、Gaussian Gram
determinant、显式 constants、OU sixth scaling 与 R107 exactness gap 为
PROVED / LOCAL-AUDITED；Gaussian-neighborhood full asymptotic expansion 与
uniform phase estimate 为网页端 ANALYTICALLY PROVED；bare scalar `RK=1`
到 genuine full-exact identification、primitive annihilation 和最终
Positive Backward-Tower Exact Zero-Set Rigidity 仍 OPEN。

## 9.26 R114：Primitive cubic shear limit 与四点 local no-go

网页端 R114 沿 R113 的要求完成了真正必要的尺度区分；connector 仍不可读，
故本节把网页端解析输入与本机可复核代数分开。本机新增
`primitive_cubic_shear_limit_r114/README.md` 与 `audit_r114.py`。

### 9.26.1 fixed-frequency `tau^3` residual

令 `tau=q^N`、`h_N=g_N^(N)`、`mu_(tau,N)=P_tau h_N`、
`c_N=kappa_3(h_N)`。OU transport 加 full-exact d=3 fingerprint 给出

`log phi_mu(r)=-r^2/2-i*tau^(3/2)c_Nr^3/6+tau^3c_N^2r^6/240+...`。

在 R109 四点 `x=(0,s,s+t,2s+t)` 上，若 `G` 是 Gaussian four-point Gram，
Schur residual `S_mu=Delta0Delta1-|N|^2` 与 full determinant 的精确关系为

`S_mu=(1-|phi_mu(s)|^2)det(G4(mu))`。

对 cubic matrix `A` 与 sixth-order real matrix `B` 做 fixed-frequency
perturbation，网页端得到

`S_mu=S_G+tau^3c_N^2F4(s,t)+O(tau^4)`，

其中

`F4=S_G(tr(G^(-1)B)-1/2tr((G^(-1)A)^2))`
`   -exp(-s^2)s^6det(G)/120`。

这是物理频率固定的展开，不能把 primitive frequency window 混入其中。

### 9.26.2 Gaussian baseline 严格为正，relative correction 不具正号

设 `Pi=s^6t^2(s+t)^4(2s+t)^2`、
`y^2=s^2+(s+t)^2+(2s+t)^2`。Vandermonde leading law 给出

`S_mu=det(H3)/144*Pi+O(y^16)`。

对 exact degree-six compatible jet，令 `d_N=kappa_5(h_N)`，则

`m3=tau^(3/2)c_N`、`m4=3`、
`m5=10tau^(3/2)c_N+tau^(5/2)d_N`、
`m6=15+7tau^3c_N^2`，并有精确恒等式

`det(H3)=12-30tau^3c_N^2-12tau^4c_Nd_N`
`        -tau^5d_N^2-6tau^6c_N^4`。

故 Gaussian 邻域的 primitive 首项为

`S_mu-S_G=-(5/24)tau^3c_N^2Pi+...`。

Gaussian `S_G>0`，所以 `S_mu>=0` 不能转化为
`(S_mu-S_G)/tau^3>=0`；relative correction 的负号不产生 `c_N=0`。
这严格关掉了“把四点绝对 PSD 当作 Gaussian-relative saturation”的路线。

### 9.26.3 exact angular `tau^3` limit 与 primitive rescaling

对 normalized angular functional `Z_tau`，利用已审计的
`<p6>=5/18`、`<p3^2>=1/12`，网页端得到

`tau^(-3)(Z_tau(y)-1)=-y^6(kappa_6(h_N)+3c_N^2)/2592`。

full exactness 使该式恒为零，只恢复 `kappa_6=-3c_N^2`。固定 `s,t` 时，

`tau^(-3/2)eta_tau(s,t)->-c_Ns^2(s+t)`；若改取
`s=tau^(-1/2)sigma`、`t=tau^(-1/2)xi`，Gaussian off-diagonal 进入指数小区间，
`G4->I`，没有可与 fixed-frequency `tau^3` 系数拼接的 polynomial limit。

网页端还给出 genuine finite-jet bump realization，证明 degree-six exactness
加四点 Bochner PSD 与 nonzero `c` 相容；由于它没有 all-degree exactness，
证据等级是 finite-order obstruction，不是主命题 counterexample。

### 9.26.4 结论与 R115

R114 的严格局部结论是：normalized four-point cone 仍只返回既有 primitive
bound `|c_N|<=sqrt(2)`，不推出 `c_N->0`。当前缺的不是 `tau^4` 或更高的
有限 determinant 系数，而是 all-degree Gaussian-relative comparison。

下一轮 R115 定为 **Gaussian Four-Point Slack Saturation Lemma**：寻找一个固定
generic 小 parallelogram，使 positive backward + all-degree exactness 给出

`S_(g_N^(0))(s0,t0)>=S_G(s0,t0)-o(q^(3N))`，

或证明 genuine all-degree obstruction；后一结果将说明必须更换 global functional。

R114 证据边界：moment/cumulant substitution、`H3` determinant、Gaussian 与
primitive leading coefficients、angular cancellation、scale/shear identities
为 PROVED / LOCAL-AUDITED；full trace formula 与 finite-jet bump realization
为网页端 ANALYTICALLY PROVED；bare scalar `RK=1` identification、all-degree
relative saturation、primitive annihilation 和最终 rigidity 仍 OPEN。

## 9.27 R115：Gaussian-relative slack saturation 不是独立引理

网页端 R115 对 R114 预定的 saturation route 做了完整的结构性收束；本机新增
`gaussian_four_point_saturation_r115/README.md` 与 `audit_r115.py`，并保持
网页通信失败与数学证据分离。

### 9.27.1 固定 generic parallelogram 上的等价性

取 sufficiently small generic `(s_0,t_0)` 使 R114 的 `F_4<0`，记
`lambda_4=-F_4>0`、`tau_N=q^N`、`h_N=g_N^(N)`、`c_N=kappa_3(h_N)`、
`mu_N=P_(tau_N)h_N`。R114 fixed-frequency expansion 在 uniform remainder 下为

`S_(mu_N)(s_0,t_0)=S_G(s_0,t_0)-lambda_4*tau_N^3*c_N^2+R_N`，
`|R_N|<=C_4*tau_N^4`。

若要求的 Gaussian-relative comparison

`S_(mu_N)(s_0,t_0)>=S_G(s_0,t_0)-epsilon_N*tau_N^3`、
`epsilon_N->0`

成立，则

`lambda_4*c_N^2<=epsilon_N+C_4*tau_N`，从而 `c_N->0`。反向若 `c_N->0`，
则 `S_(mu_N)-S_G=o(tau_N^3)`，自动得到同一比较。故

`Gaussian-relative slack saturation <=> kappa_3(h_N)->0`。

若 `|c_N|>=c_*>0` 沿子序列成立，反而得到
`S_(mu_N)<=S_G-(lambda_4c_*^2/2)q^(3N)`；这不违反 `S_(mu_N)>=0`，因为
`S_G>0`。所以 obstruction 是 absolute PSD 与 Gaussian-relative sign 的
结构差异，不是余项精度不足。

### 9.27.2 varying-bottom 复杂度被压缩为 single-law 问题

任意 genuine full-exact top law `h_N` 自动生成
`g_N^(j)=P_(q^(N-j))h_N`，但 varying-bottom 定义不要求 `h_N` 与 `h_(N+1)`
有关；positive backward OU 本身不提供跨 N 的 `c_N` coherence。R112 的
`E exp(X^2/8)<=2` 统一包络给出 tightness 与所有固定矩的 uniform
integrability。若 `limsup|c_N|>0`，可取 `h_N=>h`、`c_N->c!=0`；矩收敛给
`kappa_3(h)=c`，且 exact angular identity 对固定频率由 dominated convergence
传给 h，所以 h 是 genuine full-exact 单律。反向对任意这样的 h 取
`h_N=h` 即可。于是

`exists varying-bottom nonvanishing cubic sequence`
`<=> exists genuine full-exact single law with kappa_3!=0`。

这是 R115 的主要小里程碑：tower complexity 从 cubic sector 中 quotient 掉了。

### 9.27.3 有限局部锥不能再推进主命题

R114 的 genuine finite-jet 与 R115 的 formal/all-finite-order obstruction
说明任意有限 exact rows、有限 Bochner minors、有限 `tau` 系数都能被非零
odd-charge 的 genuine moment-matching law 穿过。普通 positive Gram minor 还
有 `F(Gaussian)>0`，不具备 Gaussian-centered extremality。

要直接排除 cubic charge，global functional 至少需要

`F(Gaussian)=0`、`F(mu)>=0`（来自 genuine one-body/global factorization）、
`F(P_tau h)=-C*c^2*tau^3+o(tau^3)`、`C>0`。

这说明 R115 saturation 目标如果成功，已经与单律 cubic exclusion 同层级；
不能继续把它当作更弱的中间结论。

### 9.27.4 结论与 R116

R115 的 PROVED / LOCAL-AUDITED 内容是 determinant、scale 与 saturation
implication 的代数骨架；uniform remainder、tightness/limit passage 与
有限阶 moment matching 为网页端 ANALYTICALLY PROVED / FINITE-ORDER
OBSTRUCTION。`RK=1` 到 genuine full-exact identification 仍 CONDITIONAL。

OPEN 已进一步压缩为 R116 **Single-Law Factorized Gaussian-Radial Cubic
Exclusion**：令三个 iid factor 的二维 residual 为 `R`，其 characteristic
function 为严格 same-factor product，且 `|R|^2~chi^2_2`；判断是否必有
`kappa_3(X)=0`。若该单律命题成立，R115-B 立即关闭所有 varying-bottom
cubic sequences；若失败，则得到主命题 genuine all-degree obstruction。

## 9.28 R116：single-law factorization 的全局 angular-mode 压缩

网页端 R116 将 R115 的 single-law 目标写成二维复 residual，并给出
`single_law_gaussian_radial_cubic_r116/README.md` 与 `audit_r116.py`；本机
审计通过。令 `omega=exp(2*pi*i/3)`、`X_1,X_2,X_3` iid centered variance-one，

`Z=sqrt(2/3)(X_1+omega X_2+omega^2X_3)`。

### 9.28.1 精确 residual 与 cubic 接口

`|Z|^2=sum_j(X_j-Xbar)^2`，所以 full exactness 等价于
`|Z|^2~chi^2_2`；iid 的循环置换与交换给 residual law 自动的 `D_3` 对称性。
若 `Z=R exp(i Theta)`、`u_1(r)=E[exp(3iTheta)|R=r]`，则

`E Z^3=2 sqrt(2/3) kappa_3(X)`，

`kappa_3(X)=sqrt(3/8) int r^3 u_1(r) r exp(-r^2/2)dr`。

主目标因此只需要 annihilate 一个 weighted first-harmonic moment；要求整个
`u_1` 消失是更强的命题。

### 9.28.2 Fourier/Hankel 与 MGF/Bessel 双桥

取长度 `sqrt(2/3)` 的 120-degree tight frame `v_j`，有
`sum v_j=0`、`sum v_jv_j^T=I_2`，且

`Phi(rho,alpha)=prod_j phi(rho sqrt(2/3) cos(alpha+2*pi*(j-1)/3))`。

其 order-3 harmonic 为

`H_1(rho)=int J_3(rho r)u_1(r)r exp(-r^2/2)dr`，

并且 `J_3(x)=x^3/48+O(x^5)` 给
`H_1(rho)=sqrt(2/3)kappa_3(X)rho^3/24+O(rho^5)`。径向 exactness 只固定
`H_0(rho)=exp(-rho^2/2)`，没有自动固定 `H_1`。

用 `M(z)=E exp(zX)` 定义三因子 MGF 后，相同的 angular charge 为

`c_1(z)=exp(-z^2/2) int I_3(zr)u_1(r)r exp(-r^2/2)dr`

`=sqrt(2/3)kappa_3(X)z^3/24+O(z^5)`。故
`u_1 <-> H_1 <-> c_1` 是同一 cubic sector 的三种全局坐标，不能与
`P_3K`、Schur scalar 或 zeroth radial mode 混淆。

### 9.28.3 regularity、非因子化 obstruction 与条件性结果

若 genuine full-exact 单律有非零 cubic charge，前向 OU `P_t` 保持 exactness、
把 cubic 缩放为 `t^(3/2)`，并给出严格正 analytic density；所以 regularity 不是
缺口。对应的 real-space residual density是

`p_f(z)=int prod_j f(m/sqrt(3)+v_j dot z)dm`，

其 circular radialization 为二维 Gaussian。这一 factorization 才是不可替代的
结构。

仅有二维 Gaussian radial law 与 positivity 不够：
`dnu_epsilon=[1+2epsilon Re(z^3)exp(-|z|^2)]d gamma_2`
在足够小非零 `epsilon` 下严格正、径向 exact、但
`E Z^3=(16/27)epsilon!=0`。网页端曾给出 `16/9`，本机 exact integral audit
纠正为 `16/27`；非零性与 obstruction 结论不变，故记录以本机值为准。

另有条件性小定理：若 one-body law classical infinitely divisible 且有需要的
exponential moments，则 `kappa_6=int x^6 Pi(dx)>=0`；full exact degree-six
fingerprint `kappa_6=-3kappa_3^2` 立即给 `kappa_3=0`，再得 Levy measure 消失，
于是 law 为 centered Gaussian。varying-bottom positive OU 不自动提供这一
classical infinite divisibility，不能偷换假设。

### 9.28.4 判决与下一步

PROVED / LOCAL-AUDITED：复 residual、tight frame、cubic moment 系数、Bessel
leading term、OU radial preservation、非因子化 smooth obstruction 的积分；
ANALYTICALLY PROVED：Hankel/Bessel 表示、injectivity、density regularity 与
real-space factorization。CONDITIONAL PROVED：infinite divisibility 分支。

核心 OPEN 保持为

`|Z|^2~chi^2_2` 且 `Phi(xi)=prod_j phi(v_j dot xi)`
`=> kappa_3(X)=0`。

这已不再是 finite Gram/minor 或 tau 高阶展开问题，而是 same-factor three-line
convolution 是否必然 annihilate weighted first harmonic。R117 最小命题固定为：
对严格正 analytic `f` 的该 convolution，在 Gaussian circular radialization 下证明
`int r^3u_1(r)r exp(-r^2/2)dr=0`；优先研究 spherical-harmonic/total-positivity
或正核 `I_3(zr)`，不回到有限阶数值路线。

## 9.30 R118：reflection gap 是正的 skew-energy，但仍不够 annihilate

网页端 R118 在 R117 heat-flow reduction 上构造了反射极化 gap，并给出
`reflection_gap_skew_energy_r118/README.md` 与 `audit_r118.py`；本机审计通过。
令 `u_t=P_t f`、`check u_t(x)=u_t(-x)`、`e_t=(u_t+check u_t)/2`、
`o_t=(u_t-check u_t)/2`，定义

`C(t)=int u_t^2 check u_t`、`D(t)=int u_t^3-C(t)`。

逐点展开的奇项在全空间积分后消失，得到真正的积分恒等式

`D(t)=4 int e_t o_t^2`
`=(1/2)int(u_t+check u_t)(u_t-check u_t)^2>=0`。

Hölder 等号当且仅当 `u_t=check u_t`；热核 Fourier multiplier 无零点，因此
`D(t)=0` 对一个 `t>0` 即推出 `f=check f` 与 `kappa_3(f)=0`。这是一个 genuine
global equality mechanism，Gaussian/symmetric state 在此 gap 上处于 boundary。

### 9.30.1 mixed-reflection Laplace order

取 `Y=(X_1,X_2,-X_3)`、`Qsharp=sum(Y_j-Ybar)^2`。Gaussian completion 给

`C(t)=(2*pi*t*sqrt(3))^(-1)E exp(-Qsharp/(2t))`。

R117 exact heat curve 因而给

`D(t)=(2*pi*t*sqrt(3))^(-1)`
`*[t/(1+t)-E exp(-Qsharp/(2t))]>=0`，

即得到无 phase cancellation 的 global order

`E exp(-Qsharp/(2t))<=t/(1+t)=E exp(-Q/(2t))`。

这是 same-factor/reflection 结构的真实单边不等式，但方向不是消灭 cubic charge
所需的 opposite comparison。

### 9.30.2 barycenter 控制与正能量首项

写 `h_t=o_t/e_t`，则 `|h_t|<1`、
`B(t)=int x e_t^3(3h_t+h_t^3)`，从而

`B(t)^2<=4D(t)int x^2e_t^3`
`<=2(1+t)/(pi*t) D(t)`。

所以 `D=o(t^(-4))` 会推出 R117 的 `B=o(t^(-2))` 与 `kappa_3=0`。

但 exact degree-six moments `m_4=3`、`m_6=15+7kappa_3^2` 对 mixed-sign statistic
给出

`E Qsharp=2`、`E Qsharp^2=8`、
`E Qsharp^3=48+(224/27)kappa_3^2`。

于是 `lambda=1/(2t)` 时

`E exp(-lambda Q)-E exp(-lambda Qsharp)`
`=(112/81)kappa_3^2lambda^3+O(lambda^4)`，

并且

`D(t)=7/(81*pi*sqrt(3))*kappa_3^2*t^(-4)+O(t^(-5))`。

因此 `t^4D(t)->7kappa_3^2/(81*pi*sqrt(3))`，也即
`D=o(t^(-4))<=>kappa_3=0`；若 `kappa_3!=0`，还与 R117 的 barycenter 形成
`D/B^2->28*pi/(3sqrt(3))` 的精确比值。

### 9.30.3 polarization、障碍与 R119

对 `f_lambda=((1+lambda)/2)f+((1-lambda)/2)check f`，有

`int(P_t f_lambda)^3=A_G(t)-3/4(1-lambda^2)D(t)`。

故 asymmetric endpoints 是该 reflection-mixture path 的 overlap maxima，
symmetric midpoint 低出 `3D/4`；zeroth overlap 只表达 symmetric deficit 与
odd positive energy 的补偿，不能单独杀掉 odd component。

现有 strict total positivity / variation-diminishing 只允许自然
`D(t)~kappa_3^2t^(-4)`，而 Hölder/reflection 给出的 mixed Laplace order 在
三阶矩上是 `E Qsharp^3>=48`，正好与所需 `<=48` 相反。因而

PROVED / LOCAL-AUDITED：reflection gap、mixed Laplace order、barycenter bound、
前三阶 mixed-sign moments、positive skew-energy coefficient、`D/B^2` 比值与
reflection-mixture polarization。CONDITIONAL：若另有
`E exp(-Qsharp/(2t))=t/(1+t)-o(t^(-3))`，或仅有 `E Qsharp^3<=48`，即可推出
`kappa_3=0`。FORMAL：nonzero odd all-degree branches保留自然 `t^(-4)` gap。

OPEN 仍为 `B(t)=o(t^(-2))<=>kappa_3=0`。R119 最小命题是 **Mixed-Reflection
Third-Moment Reversal**：能否从其它 global same-factor structure 得到
`E Qsharp^3<=48`，或至少使 Laplace gap 为 `o(lambda^3)`；若 standard
rearrangement/total-positivity 不可能给出 opposite comparison，则转向
conditional-mean diagonal transform `E[Xbar J_0(rho sqrt(Q))]`。

## 9.29 R117：Gaussian radial exactness 的 cubic heat-flow 等价

网页端 R117 把二维 angular-mode 目标进一步压到一维热流，并形成
`heat_escort_barycenter_r117/README.md` 与 `audit_r117.py`；本机审计通过。
取 centered variance-one density `f`、`u_t=P_t f` 与
`Q=sum_j(X_j-Xbar)^2`，Gaussian completion 给出

`int (P_t f)^3 dx = (1/(2*pi*t*sqrt(3))) E exp(-Q/(2t))`。

因而

`Q~chi^2_2 <=> ||P_t f||_3^3=1/(2*pi*sqrt(3)*(1+t))` 对所有 `t>0`。

这是 genuine global 的双向 Laplace 等价，不是 finite jet。

### 9.29.1 heat curvature 与 strict-interior 再确认

令 `A=int u_t^3`、`I=int u_t(u_t')^2`、`J=int u_t(u_t'')^2`。热方程与分部
积分给 `A'=-3I`、`I'=-J`；exact curve `A=C/(1+t)`、
`C=1/(2*pi*sqrt(3))` 给

`I=C/(3(1+t)^2)`、`J=2C/(3(1+t)^3)`、`A J=6I^2`。

一般正密度仅有 `A J>=4I^2`，故 exact value `6` 仍在基础 positivity cone
内部；zeroth cubic overlap、Cauchy、Fisher 或简单 rearrangement equality
不能直接产生 Gaussian rigidity。

### 9.29.2 cubic heat-escort barycenter 提取器

定义 `A_t(lambda)=int exp(lambda y)u_t(y)^3dy`、
`B(t)=int y(P_t f(y))^3dy`。精确 completion 给

`A_t(lambda)=exp(lambda^2t/6)/(2*pi*t*sqrt(3))`
` * E[exp(lambda Xbar)exp(-Q/(2t))]`，

从而

`B(t)=1/(2*pi*t*sqrt(3))E[Xbar exp(-Q/(2t))]`。

由于 `E[Xbar Q]=2*kappa_3(f)/3`，

`B(t)=-kappa_3(f)/(6*pi*sqrt(3))*t^(-2)+O(t^(-3))`。

对 cubic escort law `dnu_t=(P_t f)^3dx/int(P_t f)^3dx`，等价地

`E_nu_t[Y]=-kappa_3(f)/(3t)+O(t^(-2))`，

所以

`kappa_3(f)=-3 lim_(t->infty)t E_nu_t[Y]`。

R117 的新小里程碑是：cubic annihilation 等价于证明这个 escort barycenter
比自然的 `t^(-1)` 尺度多衰减一阶。

### 9.29.3 conditional-characteristic 双表示与精确缺口

令 `M=(X_1+X_2+X_3)/sqrt(3)`、`R=sqrt(Q)`，定义

`G(xi,rho)=avg_theta prod_j phi(xi/sqrt(3)+rho a_j(theta))`
`=E[exp(i xi M)J_0(rho R)]`。

径向 exactness 只给 `G(0,rho)=exp(-rho^2/2)`；而

`D(rho)=partial_xi G(0,rho)=iE[MJ_0(rho R)]`
`=-i*kappa_3(f)rho^2/(2sqrt(3))+O(rho^4)`。

定义 signed measure `eta(dq)=E[Xbar;Q in dq]`，则 `B(t)` 是 eta 的 Laplace
变换，`D(rho)=i*sqrt(3)int J_0(rho sqrt(q))eta(dq)` 是其 Hankel 变换；
目标只需 `int q eta(dq)=2*kappa_3/3=0`。因此缺口被精确改写为：same-factor
three-line structure 对 `E[Xbar|Q=q]` 有什么 global coherence？

### 9.29.4 I3 / rearrangement 路线的边界、判决与 R118

非因子化密度
`p_epsilon=(2*pi)^(-1)e^(-r^2/2)[1+2epsilon r^3e^(-r^2)cos(3theta)]`
在小 `epsilon` 下严格正、Gaussian radial、且 `u_1=epsilon r^3e^(-r^2)`，
其 weighted cubic moment 为 `(16/27)epsilon`。所以 `I_3` 正性、total
positivity、`D_3` 与 radial positivity 单独不足；同因子 three-line structure
仍必须真正使用。只控制 `int(P_t f)^3` 的 rearrangement 也碰不到
`int x(P_t f)^3` 的 escort center drift。

PROVED / LOCAL-AUDITED：Gaussian overlap/Laplace equivalence、heat derivatives、
tilted completion、`E[Xbar Q]` 与 cubic leading coefficients、非因子化
`I_3` obstruction integral。ANALYTICALLY PROVED：Laplace/Hankel injectivity、
global regularity 与 conditional representations。OPEN：

`same-factor three-line convolution + Gaussian radialization`
`=> int x(P_t f)^3dx=o(t^(-2)) <=> kappa_3(f)=0`。

R118 最小命题固定为 **Heat-Escort Barycenter Annihilation**，优先寻找带线性
tilt 的 rearrangement、three-line total positivity 或
`E[Xbar|Q]` 的 sign/variation-diminishing theorem；不回到 finite Gram/minor、
tau 高阶或数值路线。

## 9.31 R119：universal sign-flip identity 与 conditional radial-score shell

网页端 R119 对 R118 的 mixed-reflection 路线作了最终收束，并给出
`conditional_radial_score_shell_r119/README.md` 与 `audit_r119.py`；本机审计通过。

### 9.31.1 reverse third-moment 不是独立桥梁

令 `Q=sum(X_j-Xbar)^2`、`Y=(X_1,X_2,-X_3)`、
`Qsharp=sum(Y_j-Ybar)^2`。直接有

`Qsharp=Q+(4/3)X_3(X_1+X_2)`。

对任意 centered iid law（仅六阶矩有限）纯矩代数给出

`E Qsharp=EQ`、`E Qsharp^2=EQ^2`、
`E Qsharp^3-EQ^3=(224/27)(EX^3)^2`。

因此在 exact class 中 `E Qsharp^3<=48` 与 `kappa_3=0` 完全等价；同样，
`L(lambda)-Lsharp(lambda)=(112/81)kappa_3^2lambda^3+O(lambda^4)`，所以
Laplace `o(lambda^3)` saturation 也与 cubic annihilation 等价。R119 因而
排除把 reverse third moment 继续当作更弱的中间引理。

modulus-only mixed-sign characteristic 数据逐点满足
`|phi(ra_1)phi(ra_2)phi(-ra_3)|=|phi(ra_1)phi(ra_2)phi(ra_3)|`，所以任何只依赖
modulus、difference law、Schur–Abel modulus 或 radial product magnitude 的路线
都看不到 cubic sign；ordinary same-factor positivity 的 universal 三阶方向严格
是 `+kappa_3^2`。reverse 若存在，必须在 all-degree exact radial identity 的
真正 global 位置使用它。

### 9.31.2 conditional mean profile 与新 score-shell 结构

在 full exact 下令 `h(q)=E[Xbar|Q=q]`、
`nu(dq)=1/2 exp(-q/2)dq`。centeredness 只给
`int h dnu=0`，而

`kappa_3=(3/2)int qh(q)dnu`。

这说明缺失的是从 `h` 对 `1` 的正交推出其对 `q` 的第二个正交。profile-level
单调/一次变号不够：`h_0(q)=q-2` 对 `nu` 均值为零，但
`int qh_0dnu=4`；这不是 genuine exact counterexample，只是精确的 profile
obstruction。

令 `rho=(log f)'`、
`Sigma_0=sum_j rho(X_j)`、
`Sigma_R=sum_j(X_j-Xbar)rho(X_j)`。在
`M=sqrt(3)Xbar`、`|Z|^2=Q` 的 mean-residual coordinates 中，score integration
by parts 给

`E[psi(Q)Sigma_0]=0`、`E[Xbar Sigma_0|Q]=-1`，

而 residual radial divergence 加 exact `Q~chi^2_2` 的 Stein identity 给

`E[Sigma_R|Q=q]=-q`。

对 `Xbar psi(Q)` 再作同样分部，得到核心新接口

`E[Xbar Sigma_R|Q=q]=2q h'(q)-qh(q)`，

即

`boxed{2q h'(q)=Cov(Xbar,Sigma_R|Q=q).}`

并且

`kappa_3=(3/2)E[Cov(Xbar,Sigma_R|Q)]`。

这是 genuinely same-factor、score-sensitive、conditional、global-in-q 的
结构，已把原问题精确转为 conditional radial-score covariance 的符号问题。

### 9.31.3 reflection-stable sign lemma、判决与 R120

若能对整个 exact class 证明

`Cov(Xbar,Sigma_R|Q=q)>=0` a.e. `q`

或 universally `<=0`，则应用于 reflected law `check f(x)=f(-x)`；`Q` 不变、
`h_check=-h`、`h'_check=-h'`，两侧固定符号迫使 `h'=0`，centered 再给 `h=0`
与 `kappa_3=0`。这形成精确的 **Reflection-Stable Radial-Score Sign Lemma**。

但若只能得到 `sign h'=sign kappa_3` 这种 orientation-dependent 单调性，reflection
后完全相容，不能产生矛盾。故

PROVED / LOCAL-AUDITED：universal sign-flip 三阶恒等式、Laplace 系数、profile
obstruction、score-shell covariance 代数接口与 reflection sign logic。
ANALYTICALLY PROVED：score integration by parts、conditional disintegration 与
exact radial Stein step。CONDITIONAL：reflection-stable covariance sign lemma。
FORMAL：R104 nonzero odd all-degree branch。OPEN：`kappa_3(f)=0`。

R120 最小命题固定为 **Conditional Radial-Score Sign / Total-Positivity Lemma**：
在 strict positive analytic genuine exact three-line class 中，能否由 same-factor
product、Gaussian radial marginal 与 TP/rearrangement/conditional MLR 推出
`Cov(Xbar,Sigma_R|Q=q)` 的 reflection-stable 固定符号？若不能，构造 genuine
same-factor、最好 strict log-concave/TP2 的有限 exact obstruction，证明标准 TP2
只能产生 orientation-dependent monotonicity。

## 9.32 R120：shell TP 取向与 angular-mixture coherence 缺口

网页端 R120 进一步审计了 R119 的 score-shell 目标，并给出
`angular_mixture_coherence_r120/README.md` 与 `audit_r120.py`；本机审计通过。

### 9.32.1 shell kernel 的 exact MLR 形式

令 `a_j(theta)=sqrt(2/3)cos(theta+2*pi*(j-1)/3)`，则
`sum a_j=0`、`sum a_j^2=1`。定义

`F_theta(q,m)=prod_j f(m+sqrt(q)a_j(theta))`、
`K_f(q,m)=avg_theta F_theta(q,m)`。

除固定 polar Jacobian 外，`K_f` 是 `(Q,Xbar)` 联合 shell density。exact radial
marginal 只固定 `A(q)=int K_f(q,m)dm=C_0e^{-q/2}`。若
`rho=(log f)'`、`Sigma_R=sum_j(X_j-Xbar)rho(X_j)`，则

`partial_q log F_theta=Sigma_R/(2q)`，
`partial_q log(K_f/A)=E[Sigma_R|q,m]/(2q)+1/2`，

故

`h'(q)=Cov(Xbar,Sigma_R|Q=q)/(2q)`。

这将固定 covariance sign 精确识别为 shell kernel 的 universal MLR orientation。

### 9.32.2 TP2/RR2 与 reflection

`K_f TP2` 给 `h'>=0`、`Cov>=0`；`K_f RR2` 给相反方向。反射满足

`K_check f(q,m)=K_f(q,-m)`、`h_check=-h_f`、`C_check=-C_f`，并精确交换
`TP2 <-> RR2`。因此“每个 f 的方向依赖 skew”只能是 orientation detector，
不可能 annihilate skew。

若额外能证明整个 exact class 的 shell kernel 统一 TP2（或统一 RR2），则对 `f`
及其反射同时应用，得到 shell kernel 同时 TP2/RR2；严格正性使所有 `2x2`
minor 为零，因而 `K_f=A(q)B(m)`、`Xbar` 与 `Q` 独立，最终 `kappa_3=0`。
这是 **Reflection-TP Rigidity**，但目前只有 CONDITIONAL 地位。

### 9.32.3 strict log-concavity 与 anglewise TP 的边界

逐角交叉曲率为

`partial_m partial_q log F_theta`
`=(1/(2sqrt(q)))sum_j a_j rho'(m+sqrt(q)a_j)`。

strict log-concavity 只给 `rho'<0`，不固定该和的符号；若额外 `rho'` 非减，
Chebyshev 可给 anglewise TP2，若 `rho'` 非增则给 anglewise RR2，但这些条件
自身仍会在 reflection 下翻转。

更重要的是，anglewise TP 即便成立，正的 angular mixture 也不自动 TP2。显式
正 rank-one 矩阵

`A=[[1,10],[10,100]]`、`B=[[10,1000],[1,100]]`

各自 determinant 为零，但 `det(A+B)=-8910`。所以真正缺的是跨角的 joint
angular coherence/MTP，而非逐角 MLR。

### 9.32.4 within/between 精确分解与新的 obstruction

令 `A_theta=int F_theta dm`、`w_q(theta) proportional A_theta(q)`、
`m_theta=E[Xbar|q,theta]`、`r_theta=E[Sigma_R|q,theta]`。则

`2q h'(q)=E_w[Cov(Xbar,Sigma_R|q,theta)]`
`+Cov_w(m_theta,r_theta)`。

第一项是 ordinary anglewise MLR 可触及的 within-angle term；第二项是
between-angle reweighting/coherence term。exact radial 只给 `E_w r_theta=-q`，
不控制第二项；这就是 anglewise TP 到 shell TP 所缺的精确位置。

此外，analytic、strict-log-concave、same-factor、degree-six-compatible 的
小 Hermite 对偶扰动可实现非零 `kappa_3=c`、`kappa_4=0`、
`kappa_6=-3c^2`，并可与反射配对 `f_{-c}=check f_c`。这不是 full-exact project
counterexample，却排除了 regularity、log-concavity、same-factor 和有限
fingerprint 已经足以导出 reflection-stable sign 的可能。

### 9.32.5 判决与 R121

PROVED / LOCAL-AUDITED：shell frame、exact MLR scaling、TP/RR reflection algebra、
anglewise TP mixture obstruction、within/between coherence decomposition 与
conditional rank-one logic。ANALYTICALLY PROVED：score integration-by-parts、
small Hermite perturbation obstruction。CONDITIONAL：reflection-stable fixed
orientation TP/RR theorem。OBSTRUCTION：strict log-concavity、score monotonicity、
anglewise TP、ordinary variation-diminishing 与 finite fingerprints 均不足。

OPEN：`Cov(Xbar,Sigma_R|Q=q)` 的 reflection-stable sign 或恒零，进而
`kappa_3(f)=0`。

R121 最小命题固定为 **Angular-Mixture Coherence Lemma**：只攻
`C_ang(q)=Cov_w(m_theta(q),r_theta(q))`，判断 genuine all-degree angular
exactness / R101 Herglotz structure 能否给出其 quadratic-form 表示，或至少给出
它与 within-angle term 的强制相对符号/抵消关系。若不能，则正式关闭 TP/MLR 主
路线并转向 conditional-mean diagonal transform。

## 9.33 R121：angular Esscher–Fisher cross term 与正二次型 no-go

网页端 R121 对 R120 的 between-angle coherence 项完成了 global 化，并给出
`angular_esscher_fisher_r121/README.md` 与 `audit_r121.py`；本机审计通过。

### 9.33.1 Esscher transverse direction

对 `F_theta(q,m)=prod_j f(m+sqrt(q)a_j(theta))` 定义

`A_theta(q,lambda)=int e^(lambda m)F_theta(q,m)dm`、
`Z(q,lambda)=avg_theta A_theta(q,lambda)`、
`w_(q,lambda)=A_theta/Z`。

`lambda=3s` 正是 one-body Esscher tilt `f_s proportional e^(sx)f(x)` 在三因子
乘积中的 common-mean 方向，因此是 genuine same-factor transverse direction。
其 angular scores 为

`S_lambda=m_theta-h(q)`、
`S_q=(r_theta+q)/(2q)`。

exact row mass 给 `E_w r_theta=-q`，故

`C_ang(q)=Cov_w(m_theta,r_theta)=2q I_ang_(lambda q)`。

### 9.33.2 Positive Toeplitz/Fisher representation

令 `alpha_k=partial_lambda u_k|_0`、
`beta_k=partial_q u_k`，其中 `u_k` 是 `w_q` 的 conditional angle harmonics。
严格正性使 `T_(1/w_q)` 为正 Toeplitz operator，并给出

`C_ang/(2q)=<alpha,T_(1/w_q)beta>`，

`I_(lambda lambda)=<alpha,T_(1/w)alpha> >=0`、
`I_(q q)=<beta,T_(1/w)beta> >=0`。

所以 Herglotz/Fisher positivity 自动产生的唯一强约束是

`|C_ang|^2<=4q^2 I_(lambda lambda)I_(q q)`。

`C_ang` 是正 metric 中的 off-diagonal bilinear cross term，而不是
`sum lambda_k|charge_k|^2` 的正 quadratic energy；后者与 reflection parity
不相容。

### 9.33.3 reflection、Fisher chain rule 与 radial exactness 边界

反射满足

`A_theta^check(q,lambda)=A_(theta+pi)^f(q,-lambda)`，
`w^check_(q,lambda)(theta)=w^f_(q,-lambda)(theta+pi)`。

因此 `I_(lambda q)^check=-I_(lambda q)^f`，而两个 diagonal Fisher energies
不变，特别 `C_ang^check=-C_ang^f`。R120 的 within/between 分解正是 Fisher
chain rule：

`h'=E_w[I_(lambda q)^(m|theta)]+I_ang_(lambda q)`，

或

`2qh'=E_w[Cov(Xbar,Sigma_R|q,theta)]+C_ang`。

两项都是 off-diagonal Fisher 元，正性只给绝对值界，不给 cancellation 或固定符号。

在 polar residual 坐标，exactness 只固定 angular zero mode `u_0(q)=1`；高阶
`u_k` 与新 Esscher tangent `alpha_k=partial_lambda u_k|_0` 并没有被 static
R101 Herglotz rows 直接指定。Esscher-tilted law 一般不保持 exactness，故不能
对 exact identity 直接求 transverse derivative并置零；那会加入额外的一阶稳定性
假设。

### 9.33.4 精确 obstruction 与 R122

任意有限 exact angular Taylor rows 都可通过小的 bounded analytic Hermite 对偶
exponential family 实现，同时保持 probability、strict positivity、analyticity、
strict log-concavity 与 same-factor，并保留非零 cubic charge；这不是 full-exact
counterexample，只证明必须用无限阶/global coherence。

因此 R121 的 PROVED / LOCAL-AUDITED 内容是 Esscher score、Toeplitz cross
representation、reflection parity、Fisher chain rule、zero-mode boundary 与
normal-derivative algebra；ANALYTICALLY PROVED 的 score/conditional 论证和
finite-row obstruction 不冒充主命题证明。CONDITIONAL 是 Esscher–radial Fisher
orthogonality 或 reflection-stable fixed-sign cross theorem；OBSTRUCTION 是 static
Herglotz positivity、finite rows、strict log-concavity与 Fisher square energies
均不能给 `C_ang` 的反射稳定符号。

OPEN：`C_ang` 是否在 genuine all-degree exact class 中有特殊 cancellation，或
`h'(q)=0`、`kappa_3=0`。

R122 最小命题固定为 **Same-Factor Normal-Derivative Reconstruction Lemma**：
对 `Phi(u,v)=phi(u)phi(v)phi(-u-v)` 和 `s=phi'/phi`，核验

`s(x)=-partial_v log Phi(-x,v)|_(v=0)`，

并将 Esscher mean-charge tangent 改写成 residual trace 的非局部 functional，
判断 Gaussian radialization、positive-definiteness 与 same-factor functional
equation 是否产生 static Herglotz 看不到的 first-harmonic identity。若仍只有
reflection-odd bilinear pairing，则正式关闭 R101/Herglotz angular-coherence 主路线。

## 9.34 R122：same-factor 法向导数、Bochner trace 与 first-harmonic obstruction

网页端 R122 在读取 R121 记录后完成了 residual trace 的法向数据重构；本机新增
`normal_derivative_bochen_trace_r122/README.md` 与 `audit_r122.py`。这一轮的核心
不是再增加一个有限系数展开，而是把 R121 的 Esscher mean-charge tangent 精确
识别为 same-factor trace 的 first normal Cauchy datum。

### 9.34.1 exact reconstruction 与 interior compatibility

对 `Phi(u,v)=phi(u)phi(v)phi(-u-v)`、`s=(log phi)'`，沿 `u=-x` 有

`partial_v log Phi(-x,v)|_(v=0)=s(0)-s(x)=-s(x)`，

所以 centeredness 给出

`s(x)=-partial_v log Phi(-x,v)|_(v=0)`。

令 `d=-s`，则 full trace 满足

`partial_u log Phi(u,v)=d(-u-v)-d(u)`、
`partial_v log Phi(u,v)=d(-u-v)-d(v)`。

这确证 normal datum 可由 same-factor trace 的 tangential boundary derivative
重构，但本质是 factorization 的 compatibility，不是新的 positivity inequality。

### 9.34.2 三维 log-wave extension

取 `v_j=sqrt(2/3)(cos(theta+2*pi*j/3),sin(theta+2*pi*j/3))`，
`tilde Phi(xi,eta)=prod_j phi(xi/sqrt(3)+v_j dot eta)`。由
`sum_j v_j v_j^T=I_2` 与 `|v_j|^2=2/3`，得到 exact same-factor PDE

`Delta_eta log tilde Phi=2 partial_xi^2 log tilde Phi`。

其法向 datum 为

`partial_xi log tilde Phi(0,eta)=(1/sqrt(3))sum_j s(v_j dot eta)`，

并且 mean-charge trace 为 `Psi=Phi/(i*sqrt(3))*partial_xi log tilde Phi`。
因此 `Phi` 是 Dirichlet trace、`Psi` 是 reflection-odd first normal Cauchy
datum。log-wave equation 与 circular Dirichlet average 都没有自动决定这个 odd
datum。

### 9.34.3 charge/Hankel transport 与 exact target

R101 的 static charges 是 residual angular Fourier trace；`Psi` 的 charges 则对应
`g_k(q)=E[Xbar exp(-3ikTheta)|Q=q]`，并通过 Hankel inversion 与 `Phi` 关联。
零阶 mean-charge mode 满足

`G_0(rho)=E[Xbar J_0(rho sqrt(Q))]`

以及

`G_0(rho)=-kappa_3rho^2/6+O(rho^4)`。

在 log trace 层，first-harmonic lowering operator 满足

`N_0=rho^(-1)M P_1^log`，

`M(rho^(2m+1))=sqrt(2)((m+1)(m+2)/m)rho^(2m+1)`；因此
`P_1^log=-i kappa_3rho^3/(12sqrt(6))+...` 被 transport 成
`N_0=-i kappa_3rho^2/(2sqrt(3))+...`，不是被 annihilate。

### 9.34.4 Bochner/Schwarz 的真实边界

exact radial branch 只给 reflection-even Schwarz budget

`|G_0(rho)|^2 <= (1/3)e^(-rho^2)(I_0(rho^2)-1)
=rho^4/12+O(rho^6)`。

该 budget 不随 reflection 翻号，故不能推出 `G_0=O(rho^4)`。这正式关闭
“静态 Herglotz + trace reconstruction 自动给 first-harmonic zero”的局部路线：
法向数据虽被 exact 重构，但现有正性只看到其平方能量。

### 9.34.5 genuine tangent obstruction

取 `psi(x)=sin(ax)-c sin(bx)`、
`c=a exp(-a^2/2)/(b exp(-b^2/2))`，则高斯基点有
`E[Xpsi(X)]=0`，但
`E[H_3(X)psi(X)]=a(b^2-a^2)exp(-a^2/2) !=0`。
通过 IFT 的 centered/variance-one exponential family 可保持 positive、analytic、
strict-log-concave、same-factor，同时使 `kappa_3` 一阶变化非零；然而任意
radial test `F(Q)` 的一阶变化因 global reflection oddness 全部为零。这是真实
analytic tangent obstruction，说明任何证明必须利用 all-degree/global realizability，
不能只靠 radial observables 的一阶信息。

### 9.34.6 判决与 R123

PROVED / ANALYTICALLY PROVED：normal reconstruction、trace compatibility、
log-wave equation、mean-charge/Hankel correspondence、log harmonic lowering、
exact Schwarz budget 与 analytic tangent obstruction。CONDITIONAL：Esscher 一阶
稳定性或其它额外正则接口可关闭目标，但它们是强假设。FORMAL：R104 all-degree
branch 仍不能升级为 genuine probability counterexample。

OPEN：`G_0=O(rho^4)` / `kappa_3=0`。

R123 固定为 **Global Bochner–Cauchy-Data Rigidity Lemma**：在完整三维联合特征
函数上，寻找超越 `N^2` reflection-even budget 的 nonlinear wave-flux 或
conditional-variance zero identity；若所有 natural flux 都只是 odd normal datum
的平方，便关闭 Fourier/Herglotz/normal-derivative 主路线并转向 global one-body
probability realizability。

## 9.35 R123：Global Bochner–Cauchy-Data Rigidity No-Go 与紧性二分

网页端 R123 在读取 R122 记录后完成了 full 3D Bochner–Cauchy-data 检验；本机新增
`global_bochner_cauchy_no_go_r123/README.md` 与 `audit_r123.py`。本轮得到一个
重要的全局降维：

`tilde Phi in PD(R^3) iff phi in PD(R)`。

令 `w_j=(1/sqrt(3),v_j)`，这些向量在 mean–residual 坐标中构成正交标准基，故
`tilde Phi(y)=prod_j phi(w_j dot y)` 的三维 Bochner 正定性由一维因子的正定性
推出；沿 `y=t w_1` 的 factor-axis 限制又恢复 `phi(t)`。因此三维 Bochner
positivity 没有超出 one-body probability realizability 的隐藏信息。

### 9.35.1 Cauchy hierarchy 与矩阵值 flux

对 `L=log tilde Phi`、`L_0=L(0,eta)`、`N=partial_xi L(0,eta)`，log-wave equation
给出

`partial_xi^(2k)L(0,eta)=2^(-k)Delta^k L_0`，
`partial_xi^(2k+1)L(0,eta)=2^(-k)Delta^k N`。

所以 `L_0` 与 `N` 正好分居 even/odd normal Cauchy hierarchy；PDE 传播 odd
datum，但不把它消灭。令 `M=(X_1+X_2+X_3)/sqrt(3)`、`R` 为 residual vector，
并定义 `F=E exp(i eta dot R)`、`J_1=E[M exp(i eta dot R)]`、
`J_2=E[M^2 exp(i eta dot R)]`，则

`J_1=-iFN`，
`J_2=-F[1/2 Delta L_0+N^2]`。

条件矩阵 `[[1,E(M|R)],[E(M|R),E(M^2|R)]]` 的 Schur complement 是
`Var(M|R)>=0`；因此 matrix-valued Bochner、Schur、conditional variance 和
quadratic wave-flux 都只产生 odd-odd pairing 或偶能量。

### 9.35.2 Global Quadratic-Bochner Parity Lemma

全局 reflection `(M,R)->(-M,-R)` 使 `N`、`J_1` 等 odd datum 翻号，`J_2`、
conditional variances、Schur determinants 与 quadratic Gram energies 不变。
故任何由 matrix-valued Bochner positivity 经 quadratic form、Schur complement、
conditional variance 或 reflection-even radial 加权积分得到的 scalar flux，均对
`N->-N` 偶。它可以产生 `N^2`、odd-odd pairing 或 magnitude bound，不能给
universal reflection-stable linear sign。

这不是逻辑上排除“偶能量取零”的宣称；真正需证明的是 exact radialization 是否
把某个 Gaussian-baseline-zero energy 强制固定为零。R123 的 explained-mean bound

`E H(Q)^2 >= kappa_3^2/3`，其中 `H=E[M|Q]`，

反而表明 nonzero cubic 产生 positive explained-mean energy，而现有 exactness
没有将其置零。更细的 circular flux

`H_2(rho)-e^(-rho^2/2)=<F[1/2|grad L_0|^2-N^2-rho^2/2]>`

是 exact identity，但其左侧含有未由 Q-marginal 决定的 `E[M^2J_0]`，不是
rigidity inequality。

### 9.35.3 Bochner-only genuine obstruction 与 formal same-factor obstruction

即使取整个 residual vector `R~N(0,I_2)`，令
`M|Q=q~N(epsilon(e^(-q)-1/3),1-epsilon^2(e^(-q)-1/3)^2)`，仍有 genuine
full 3D positive-definite joint law、exact `Q~chi^2_2`、`EM=0`、`EM^2=1`，但

`E[M Q]=-4epsilon/9 !=0`。

该模型不满足 same-factor product representation，所以不是项目反例；它证明
任何有效 R123 机制必须使用 one-body factorization，而不是继续寻找新的
Bochner inequality。另一方面 R104 formal all-degree odd branch 同时满足
same-factor、log-wave、circular exactness，却保留 `N_0~c rho^2`；这仍是 FORMAL，
缺口正是该 branch 能否由 genuine one-body PD factor 实现。

### 9.35.4 backward-OU 与路线降级

若 genuine asymmetric exact single law 存在，则 varying-bottom backward-OU
iteration 自动给 positive exact tower。因此 backward divisibility 不能单独
增加新的 single-law restriction。R123 正式将 Fourier/Herglotz/normal-derivative
flux 路线降级，主问题变成

`one-body PD ∩ all-degree same-factor exact odd branch`。

### 9.35.5 R124：Uniform-Envelope Finite-Row Realizability Dichotomy

固定 `c!=0`，令 `C_M(c)` 为 centered variance-one genuine laws，满足
`kappa_3=c`、前 `M` 个 exact rows，并统一满足 `E exp(X^2/8)<=2`。若
`C_M(c)` 对所有 `M` 非空，则 tightness、uniform integrability、moment
determinacy 与对角化给出 genuine full-exact asymmetric law；若 asymmetric
genuine exact law不存在，则某个有限 `M(c)` 必有 `C_M(c)=emptyset`。

该二分把 R115/R120 的 finite-row obstruction 提升到真正可证伪的 global 问题：
固定 primitive cubic gap 后，finite-row realization 是否能保持统一 envelope？
若不能，必须定位 positivity、固定 cubic、exact rows 或 uniform subGaussianity
中至少一项随 `M` 发生 blow-up。R124 由此不再搜索 `N^2` flux，而直接攻击
global one-body probability realizability。

R123 状态：PROVED 为 factor-axis Bochner equivalence、Cauchy hierarchy、矩阵值
conditional moments、explained-mean bound、circular flux identity、residual-
Gaussian obstruction；ANALYTICALLY PROVED 为 quadratic-Bochner parity no-go；
FORMAL 为 R104 odd branch；OPEN 仍是 `G_0=O(rho^4)` / `kappa_3=0`。
probability realizability。

## 9.36 R124：envelope-free finite-row compactness 与 cubic-radius dichotomy

网页端 R124 对 R123 的 global one-body realizability 路线完成了严格化；本机新增
`uniform_envelope_finite_row_r124/README.md` 与 `audit_r124.py`。本轮比原先设想更
强：统一 `E exp(X^2/8)<=2` 不必作为 finite-row 的先验假设，它由 exact rows
逐阶自动产生。

### 9.36.1 exact rows 的 moment definition

令 `Q=sum_j(X_j-Xbar)^2`，`a_j(theta)=sqrt(2/3)cos(theta+2pi(j-1)/3)`，
`Y_theta=sum_j a_j(theta)X_j`。有

`(1/(2pi))int Y_theta^(2r)dtheta=binom(2r,r)Q^r/4^r`。

对
`mathscr F_mu(z)=<prod_j M_mu(z a_j(theta))>-e^(z^2/2)`，

`[z^(2r)]mathscr F_mu=(E Q^r-2^r r!)/(4^r(r!)^2)`。

故第 `r` 个 exact row 无歧义地定义为

`R_r(mu):=E Q^r-2^r r!=0`。

### 9.36.2 R124-B：finite-row moment bootstrap

几何恒等式给

`(X_1-X_2)^2<=2Q`。

若第 `r` 个 row 成立，则

`E|X_1-X_2|^(2r)<=2^r E Q^r=4^r r!`。

对 independent centered copy `X'`，条件 Jensen 给

`E|X|^(2r)<=E|X-X'|^(2r)<=4^r r!`。

因此前 `M` rows 自动给

`E[sum_(r=0)^M(X^2/8)^r/r!]<=sum_(r=0)^M2^(-r)=2-2^(-M)`。

这是一条 ANALYTICALLY PROVED 的逐阶 square-exponential 控制，不依赖 full
exactness 或先验 envelope。

### 9.36.3 R124-C：Envelope-Free Fixed-c Compactness Theorem

定义 `E_M(c)` 为 genuine centered variance-one laws，满足 `kappa_3=c` 与
`R_1=...=R_M=0`，不加入尾部假设。若 `E_M(c)` 对所有 `M` 非空，variance one
给 tightness；对任意固定 moment order `p`，取足够大的 row `r` 用
`E|X|^(2r)<=4^r r!` 得到 uniform integrability。弱极限因此保留每个固定 moment、
`kappa_3=c` 和每个 row，并满足所有 even moment caps。

极限满足 `E X^(2r)<=4^r r!`，于是 monotone convergence 给
`E exp(X^2/8)<=2`。该 bound 导致 MGF entire；所有 rows 变成 entire function
`mathscr F_mu` 的全部 Taylor coefficients，identity theorem 加 Hankel uniqueness
给 genuine `Q~chi^2_2`。所以

`forall M E_M(c)!=empty => exists genuine full-exact law with kappa_3=c`。

这是 PROVED / ANALYTICALLY PROVED 的 compactness theorem；其 contrapositive
“若 cubic exclusion 成立，则某个 finite `M(c)` 失败”仍是 CONDITIONAL 于主命题，
不能误报为主命题证明。

### 9.36.4 fixed-gap radius 与 finite Hamburger certificate

令

`Gamma_M=sup{|kappa_3(mu)|: mu genuine centered variance-one,
R_1=...=R_M=0}`。

`Gamma_(M+1)<=Gamma_M`，且

`cubic exclusion iff Gamma_M->0`。

有限 moment 版本 `T_M(c)` 由 `y_0=1,y_1=0,y_2=1,y_3=c`、
`H_M(y)=[y_(i+j)]>=0`、`R_r(y)=0 (r<=M)` 及
`0<=y_(2r)<=4^r r!` 组成。若所有 `T_M(c)` 非空，则坐标对角化、Hankel
positivity、Hamburger theorem 与 Carleman 给 genuine full-exact law。因此若
固定 `c!=0` 的 genuine full-exact law不存在，必有有限 `M(c)` 使 `T_M(c)` 为空。
这是真正有限、可检验的联合 obstruction framework；但单个 finite `H_M>=0`
不必有 representing measure，singular non-flat ghost 只在 R125 中被明确区分；
这里的 Hamburger theorem 只用于所有 `M` 的一致对角极限。本轮没有声称知道
第一个失败的 principal minor 或显式 `M(c)`。

### 9.36.5 对 R115/R120 的精确解释与 R125

此前 finite-row perturbative constructions 只证明每个固定 `M` 存在某个
`c_*(M)>0` 的小 cubic 邻域；它们没有证明 `inf_M c_*(M)>0`。如果 cubic
exclusion 为真，则固定-gap realizability 必须在有限阶终止，等价地
`c_*(M)` 沿高阶趋于零或 finite Hamburger cone 发生联合不可行。

R124 的剩余 OPEN 被精确压成

`Gamma_M -> 0?`

即非零 formal odd exact branch 能否无限穿过 genuine Hamburger positivity cone。
R125 固定为 **Truncated-Hamburger Cubic-Radius Decay**：利用 exact-row 多项式
与 `H_M>=0` 构造随 `M` 增长的非负 polynomial certificate `P_M(X)^2`，争取给出
`|kappa_3|<=epsilon_M` 且 `epsilon_M->0`。这比继续寻找新的 Bochner flux 更贴近
当前主问题的 genuine one-body realizability 核心。

## 9.37 R125：truncated-Hamburger cubic radius 的渐近 exactness 与 no-go

网页端 R125 在读取 R124 后完成了 finite-row hierarchy 的进一步压缩；本机新增
`truncated_hamburger_cubic_radius_r125/README.md` 与 `audit_r125.py`。本轮没有
证明 `Gamma_M->0`，但得到三个实质性小结果，并纠正了 finite Hankel 的 representability
边界。

### 9.37.1 finite truncation 的 ghost 边界

单个 `H_M(y)>=0` 不保证 finite representing measure。反例
`(y_0,...,y_4)=(1,0,0,0,1)` 的 `H_2=diag(1,0,1)>=0`，但 `y_2=0` 会迫使任何
representing law 满足 `X=0` a.s.，从而不可能 `y_4=1`。finite ghost 只能位于
singular non-flat locus：`H_M>=0`、singular 且
`rank H_M>rank H_(M-1)`；positive definite 或 singular flat 情况可延拓/表示。

因此 finite genuine radius `Gamma_M` 与 relaxed radius `GammaHat_M` 在有限层
必须区分；R124 的 Hamburger 步骤只用于所有 `M` 的一致对角极限。

### 9.37.2 radius extremizers 与 asymptotic exactness

exact row 最高 moment 的 triangular coefficient 为

`R_r(y)=(2^r/3^(r-1))y_(2r)+P_r(y_0,...,y_(2r-1))-2^r r!`。

有限 relaxed 集合的 even moment caps 与 Hankel `2x2` minors 给 compactness，
故 `GammaHat_M` 取得最大值且单调不增。genuine `Gamma_M` 由 R124 的
finite-row moment bootstrap 保证有限，但顶阶矩在弱极限下未必连续，不能一般性
宣称 finite-level genuine supremum 取得；若某层有 genuine extremizer，才可用
至多 `2M+1` 原子的 Richter–Tchakaloff cubature 实现。R126 的 `M=3` 给出
不取得的明确修正。

定义 `Gamma_infty` 为 genuine full-exact class 的最大 cubic skew。对 genuine
extremizers 使用 R124 compactness，对 relaxed maximizers使用 coordinate diagonal
extraction、全阶 Hankel PSD、Carleman 与 Hamburger theorem，得到

`boxed{lim_M Gamma_M=lim_M GammaHat_M=Gamma_infty}`。

所以 `GammaHat_M-Gamma_M->0`，但不意味着每个有限 truncation 本身 representable。
若 fixed `epsilon>0` 能令 `GammaHat_M>=epsilon` 对所有 `M`，则必产生 genuine
full-exact law with nonzero cubic；固定非零 cubic 不能永远停留在 formal branch
同时通过全部 finite rows/caps/Hankel constraints。

### 9.37.3 growing Fourier window 与 anti-atomicity

对 genuine `mu in E_M`，前 `M` rows 使 `Y_theta=sum a_jX_j` 的 angular-averaged
moments 到 degree `2M` 与 Gaussian 一致。Taylor remainder 给

`|E J_0(t sqrt(Q))-e^(-t^2/2)|<=2|t|^(2M)/(2^M M!)`。

因此对 `|t|<=alpha sqrt(M)`、`alpha<sqrt(2/e)`，得到指数级 growing-window
近似 `<=2(e alpha^2/2)^M`。这仍只是 radial approximation，不含 first-harmonic
sign information。

令 `n=floor(M/2)`，Laguerre kernel
`P_n(q)=(n+1)^(-1)sum_(k=0)^nL_k(q/2)` 满足
`P_n(0)=1`、`E P_n(Q)^2=1/(n+1)`。故

`P(Q=0)<=1/(floor(M/2)+1)`，

在 iid 情形即 `sum_x mu{x}^3` 的 collision bound；有限原子 realizers 的支持数
至少为 `sqrt(floor(M/2)+1)`。该 anti-atomicity 不控制连续 asymmetric law 的 cubic。

### 9.37.4 判决与 R126

PROVED / ANALYTICALLY PROVED：finite triangular row structure；genuine/relaxed
extremizer；`lim Gamma_M=lim GammaHat_M=Gamma_infty`；fixed-gap no-purely-
formal escape；growing Fourier-window bound；Laguerre–Christoffel anti-atomicity。
CONDITIONAL：若主 cubic exclusion 成立，则 `Gamma_M` 与 `GammaHat_M` 均趋零；
这只是等价 reformulation。FORMAL：R104 odd branch；OBSTRUCTION：finite
Hankel ghosts、Fourier approximation、anti-atomicity与固定阶 PSD均不能 annihilate
cubic。OPEN：`Gamma_M->0`。

R126 固定为 **Singular-Ghost Elimination at the Cubic Extremum**：对 `T_M` 中
maximizing `y^(M)`，研究能否选取 `H_M` positive definite 或 flat；若不能，构造
singular non-flat extremizing branch并量化 `GammaHat_M-Gamma_M`，把 finite ghost
layer 变成下一层可检验 obstruction。

# 2026-09-07 — R126 M=3 Singular Ghost at the Cubic Extremum

本机在等待网页端连接期间先完成了 R126 的精确 `M=3` 层核验，新增
`singular_ghost_extremum_r126/README.md` 与 `audit_r126.py`。令 `c=y_3`，前三个
circular rows 在 centered variance-one 条件下给出

`R_2=(4/3)(y_4-3)`,

`R_3=(8/9)(y_6-7c^2+12y_4-51)`，即 `y_4=3`、`y_6=15+7c^2`。取 `y_5=4c` 后，
`H_2` 的行列式为 `2-c^2`，所以所有 PSD truncation 都满足 `|c|<=sqrt(2)`。

在 `c=sqrt(2)`，截断向量
`(1,0,1,sqrt(2),3,4sqrt(2),29)` 的 `H_3` 是 singular non-flat：
`rank(H_2)=2<3=rank(H_3)`。其 `H_2` kernel 给出
`X^2-sqrt(2)X-1=0`；任何 representing law 因而必须有 `y_6=11`，与 `R_3=0`
要求的 `y_6=29` 矛盾，所以该 relaxed maximizer 是 genuine ghost。

另一方面，对每个 `|c|<sqrt(2)`，同一族 `y_5=4c` 使 `H_3` positive definite，
其关键 principal minors 为 `2-c^2`、`6(1+c^2)`、`30+3c^2`、
`18+14c^2-7c^4` 和 `6(2-c^2)(1+c^2)`。一元 truncated Hamburger theorem
给出 representing law，因此 genuine laws 的 cubic skew 可任意逼近 `sqrt(2)`。
最终结论为

`boxed{GammaHat_3=Gamma_3=sqrt(2)}`，但 `GammaHat_3` 的最大值由 ghost 取得，
`Gamma_3` 只是一个不取得的上确界。

这不是 `Gamma_M->0` 的证明，而是一个严格的有限层修正：finite relaxed extremizer
不能被自动当作 genuine extremizer；R125 的渐近 squeeze 必须保留 `M->infty`
极限逻辑。R126 本机审计 marker 为
`R126_M3_ROW_ELIMINATION_PASSED`、`R126_M3_RELAXED_RADIUS_SQRT2_PASSED`、
`R126_M3_PD_APPROACHING_FAMILY_PASSED`、`R126_M3_GHOST_NONFLAT_PASSED`、
`R126_M3_ENDPOINT_NONREPRESENTABLE_PASSED`、
`R126_M3_GENUINE_SUPREMUM_NOT_ATTAINED` 和
`R126_SINGULAR_GHOST_EXTREMUM_AUDIT_COMPLETED`。

# 2026-09-07 — R127 M=4 cubic radius 与 flat extremum

在 R126 的 `M=3` ghost 之后，本机继续推进到 `M=4`。前三行消元后，第四行给出
`y_8=105-124c^2+32ca`（`c=y_3,a=y_5`）。对 `H_4` 关于固定 positive-definite
`H_2` 取 Schur complement，PSD 的必要条件可写成

`D(c,a)=-a^2+8ac-6c^4-10c^2+12>=0`,

`N(c,a)=2a^2+18ac^3-88ac-75c^4+512c^2-48<=0`。

第一式给 `a<=4c+sqrt(6(2-c^2)(1+c^2))`。在 `1<=c<sqrt(2)` 上 `N` 关于 `a`
严格递减，故只需考察上边界。令 `u=c^2`，边界值为

`F(u)=-15u^2+204u-24-18(4-u)sqrt(6u(2-u)(1+u))`。

`F(1)<0`、`F(2)>0`；消去根式后得到
`P(u)=216u^5-1919u^4+4072u^3+4704u^2-8000u+64`，其 Sturm 计数显示
`(1,2)` 内恰有一个根 `u_4=1.110047790304544...`。因此

`boxed{GammaHat_4=Gamma_4=c_4}`,

`c_4=sqrt(u_4)=1.053588055315997...`。

在 `a=4c_4+sqrt(6(2-c_4^2)(1+c_4^2))`、相应的 `b` 取 Schur 补零化值时，
`H_4` 为 flat，`rank H_2=rank H_3=rank H_4=3`；一元 flat extension theorem
给出至多三原子的 genuine representing law。故 R126 的 `M=3` non-flat ghost 在
下一行被严格消除，且新的 extremum 在 genuine flat locus 上取得。该结果仍不证明
全阶 `Gamma_M->0`，下一步应研究这种 Schur-defect/下一行兼容性是否可推广。

R127 本机审计 marker：`R127_M4_ROW_ELIMINATION_PASSED`、
`R127_M4_SCHUR_COMPLEMENT_PASSED`、`R127_M4_UNIQUE_ROOT_ISOLATION_PASSED`、
`R127_M4_FLAT_EXTREMIZER_INTERFACE_PASSED`、
`R127_M4_CUBIC_RADIUS_AUDIT_COMPLETED`。

# 2026-09-07 — R128 Singular extension compatibility and the `R_5` interface

R128 将 R126/R127 的有限层机制抽象为可复用引理。若
`H_M=(y_{i+j})_{0<=i,j<=M}>=0` 且 `p in ker H_M`，任何 PSD 扩展
`H_{M+1}=[[H_M,b],[b^T,y_{2M+2}]]` 都必须满足
`p^T b=0`，即 `b in Ran(H_M)`；其唯一新自由度是广义 Schur 缺陷
`delta=y_{2M+2}-b^T H_M^+b>=0`。`delta=0` 是 flat，`delta>0` 是
一步 singular non-flat ghost 的唯一可能方向。这是无条件 PSD 引理。

同时，本机在一致归一化
`Q=(1/3)sum_{i<j}(X_i-X_j)^2=sum_j(X_j-Xbar)^2`
下精确展开了下一 exact row：
`E Q^5=(32/81)(y_10-120y_3y_5-60y_3y_7+75y_4^2+90y_4y_6-51y_5^2+60y_6+30y_8)`，
因此 `R_5=0` 等价于
`y_10=120y_3y_5+60y_3y_7-75y_4^2-90y_4y_6+51y_5^2-60y_6-30y_8+9720`。

注意归一化必须与 R124–R127 一致：`Q=(1/3)sum_{i<j}(X_i-X_j)^2`。
此前曾用 `sum_{i<j}(X_i-X_j)^2/2` 做临时展开，产生错误的 `R_5` 常数和
虚假的严格下降；该计算已撤回。正确消元为
`y_10=120y_3y_5+60y_3y_7-75y_4^2-90y_4y_6+51y_5^2-60y_6-30y_8+9720`，
进一步在前三行、R4 下为 `y_10=3(17a^2-280ac+20bc+470c^2+315)`。

在 R127 的 flat endpoint 上，取 `y_9` 为新列兼容性值；R5 决定的 `H_5` Schur
补恰为 `diag(0,0,delta_5)`，其中
`delta_5=-18C(u_4)/(u_4-2)^2>0`。有理区间 `1.11<u_4<1.12` 给出
`C(u_4)<0`，故这是 rank-4 的 singular non-flat ghost，而不是 representing
measure。由于 `M=5` 投影包含于 `M=4` 可行集，同时该端点确实可构造，得到
`boxed{GammaHat_5=GammaHat_4=c_4}`。这是一条新的严格有限层事实：relaxed radius
在 M=5 不下降，但 extremizer 从 flat genuine 变成 singular ghost；`Gamma_5`
和全阶 `Gamma_M->0` 仍 OPEN。
本机新增 `singular_extension_compatibility_r128/` 并通过
`R128_SINGULAR_EXTENSION_AUDIT_COMPLETED`，包含 Gaussian 归一化、R5 消元和
ghost Schur 缺陷的区间证书。`Gamma_M->0` 仍 OPEN。

# 2026-09-08 — R129 M=6 exact row 与 R128 ghost 下一层 no-go

在不打断网页端 R129 推导的同时，本机完成了 `Q=(1/3)sum_{i<j}(X_i-X_j)^2`
归一化下的 `R_6` 精确展开。令 `c=y_3,a=y_5,b=y_7,d=y_9`，在已审计的
R2--R5 rows 消元后得到

`y_12=-7749c^4-16380c^2+14220ca-2160cb+100cd-1926a^2+252ab+10395`。

该式不含 `y_11`，Gaussian substitution 给 `y_12=10395`，并由 exact row
得到 `E Q^6=2^6 6!`。本机新增 `r129_m6_exact_extension_audit/`，脚本以精确
符号代数生成该式，不做扫描或优化。

更强的结果来自 R128 endpoint 的下一层 range compatibility。把 `H_5` 相对于
`A=H_2` 分块，R128 已给 `S_5=diag(0,0,delta_5)`，其中 `delta_5>0`。H6
新列相对于同一 `A` 的 Schur 补写成

`S_6=[[S_5,r],[r^T,sigma_6]]`,

`r=(d,y_10,y_11)^T-[u_3,u_4,u_5]^T A^{-1}(y_6,b,y_8)^T`。

由于 `S_5` 的前两个对角元为零，H6 PSD 必须先满足 `r_0=r_1=0`；`y_11` 只
出现在 `r_2`，因此不能修复前两项。令 R127 endpoint 的边界量满足 `B=0`，并
使用其根 `P(c^2)=0`，本机精确化简证明

`r_0=-P(c^2)/(2c(c^2-4)(c^2-2)^2)`,

`r_1-delta_5=P(c^2)/(2(c^2-4)(c^2-2)^2)`。

故在 endpoint 上 `r_0=0` 而 `r_1=delta_5>0`。这说明 R128 的具体 rank-4
singular non-flat ghost 不能延伸为满足 R6 的 PSD `H_6`；这是
`ANALYTICALLY PROVED` 的 M=6 endpoint no-go，且其数值审计值
`delta_5=913.705421573084...` 仅作为 exact expression 的核验，不是证明依据。

这里需要把 endpoint 结论与全局结论分层写清。R125 的紧性接口保证 M6
relaxed feasible set 的最大值取得；投影单调性给出
`GammaHat_6<=GammaHat_4=c_4`。若等号成立，M6 maximizer 的 M4 投影必须是
R127 的 equality point。R127 的边界不等式、对剩余参数的严格单调性以及
`D=0`/`N=0` 的联立，已把该 equality point 唯一化为
`(c_4,a_4,b_4)`（负号情形只由反射得到）；R4/R5 行再强制出 R128 的
rank-4 singular ghost。R129 已解析地证明该 ghost 无 PSD H6 extension，故
发生矛盾。因此在已审计的 R125 compactness 与 R127 equality classification
接口上，得到新的有限层严格结论

`boxed{GammaHat_6<GammaHat_5=GammaHat_4=c_4}`。

这不是 `GammaHat_6` 的显式数值，也不是 genuine `Gamma_6` 的等式；但由
feasible-set inclusion 立即有 `Gamma_6<=GammaHat_6<c_4`。本轮证据等级应改为：
`PROVED`（R6 与 Schur 线性代数）、`ANALYTICALLY PROVED`（R128 endpoint
no-go，以及结合 R125/R127 接口后的全局严格 relaxed bound）、`OBSTRUCTION`
（old-kernel defect cascade），`OPEN`（严格 gap 的显式下界、genuine 半径、
正性与 backward-OU 的统一衰减以及全阶 `Gamma_M->0`）。R130 应继续量化
`c_4-GammaHat_6` 或构造 endpoint 邻域的 uniform gap，并研究
kernel-adapted recurrence basis 如何接到 positive backward-OU cone。

# 2026-09-08 — R130 M=6 explicit rational-box gap certificate

R130 已将 R129 的定性严格下降推进为可复核的显式数值 gap。新增
`r130_m6_gap_audit/`；脚本只使用精确有理数区间算术、Sturm 根计数和直接符号
Schur 恒等式，不使用 optimizer、浮点可行性扫描或未审计的数值猜测。

在反射下只需考虑 `c=y_3>=0`。R127 的唯一根证书先给出
`1.05358<c_4<1.05359`，而 R130 对反证窗口
`1.0535<=c<=1.05359` 施加 R127 的两个 H4 Schur 不等式。精确导数符号和
端点符号把 `a=y_5` 压入 `7.5698<a<7.571`，并得到
`0<=S_00<1/100`、`0<=S_11<1/16`。H4 的非对角项写成
`S_01=b-b_*(c,a)`，有理区间给 `70.29<b_*<70.4`；PSD 的二阶主子式于是给
`70.2<b=y_7<70.5`。

对 H6 关于正定 H2 的 Schur 补，R129 的首个未检测兼容性残差就是
`S_13=r_1`。同一有理盒上的精确区间核验给出 `r_1>800`，而
`S_11<1/16`。另一方面 `S_33<=y_12`，且 R125 的 T6 矩约束给
`y_12<=4^6 6!=2,949,120`。因此 H6 PSD 的 2×2 主子式要求
`r_1^2<=S_11S_33<184,320`，却有 `r_1^2>640,000`，矛盾。故窗口内没有
H6-feasible point，得到

`boxed{GammaHat_6<=1.0535<c_4}`，

以及显式下界 `c_4-GammaHat_6>0.00008`，从而
`Gamma_6<=GammaHat_6<=1.0535`。本轮把“严格但未定量”提升为
`ANALYTICALLY PROVED` 的有限层显式上界；它仍不等于求出了 `GammaHat_6`，
也不直接给出 genuine `Gamma_6`、全阶衰减或 positive/backward-OU rigidity。

R130 审计 marker：`R130_C4_ROOT_INTERVAL_PASSED`、
`R130_H4_PARAMETER_BOX_PASSED`、`R130_BSTAR_INTERVAL_CERTIFICATE_PASSED`、
`R130_R1_LOWER_BOUND_CERTIFICATE_PASSED`、`R130_M6_SCHUR_IDENTITIES_PASSED`、
`R130_M6_SCHUR_2X2_CONTRADICTION_PASSED`、
`R130_M6_EXPLICIT_GAP_CERTIFICATE_PASSED`、
`R130_M6_EXPLICIT_GAP_AUDIT_COMPLETED`。

下一轮 R131：在不把区间证书误称为精确值的前提下，尝试细分有理盒得到更强的
显式上界，或把 `S_13` 缺陷推广成 kernel-adapted recurrence-defect lemma，
并检查这条离散 defect 链能否与正的 backward-OU 可除性建立定量接口。

# 2026-09-08 — R130 网页强 gap 的本机复核

网页端 R130 在上述基础上给出了 endpoint 邻域的更强候选估计。本机新增
`r130_web_gap_audit/`，逐式复核其 exact factorization 和被省略的常数链。
复核通过后，在 R125 compactness/cap 接口和 R127 equality/root 接口上，结论
升级为

`boxed{c_4-\widehat\Gamma_6>25/28196}`，

即 `\widehat\Gamma_6<c_4-25/28196<1.052702`，并有
`\Gamma_6\le\widehat\Gamma_6`。证据等级为
`ANALYTICALLY PROVED`；这仍是 relaxed finite-level 的显式上界，不是
`\widehat\Gamma_6` 或 genuine `\Gamma_6` 的精确值。

复核的核心链为：令 `u=c^2`、`w=sqrt(6u(2-u)(1+u))`，在
`1.1<=u<=1.12` 上，R127 boundary function `F` 满足 `0<F'<266`，且
`F(u_4)=0`。令 `x=-F(u)`、`h=a_+-a`，H4 Schur 条件和
`-partial_aN>40` 给 `h<=x/40`，继而
`A=S_00<=17x/88`、`B=S_11<=25x/22`、
`|b-b_*(c,a)|<=x/2`。沿 flat boundary 的 R129 residual 与 R128 defect
满足精确恒等式

`r_+(u)-delta(u)=F(u)[3(23u^2-68u-280)+G(u)]/[18(u-4)(u-2)^2]`,

且 `9P(u)=F(u)G(u)`。本机特别修正了网页原文的一个常数跳步：不能由
polynomial part `<252` 推出 `C<-33`；精确端点单调估计给出更强的
`polynomial part<247`，再由第二项 `<-280` 得到 `C<-33`，所以
`delta(u)>700`。同时本机证明 `|partial_b r_1|<250`、
`|partial_a r_1(c,a,b_*)|<3000`，从而在 `x<=1/2` 时 `r_1>580`。

H5 的 compatibility value `d_*` 在同一有理盒中满足 `0<d_*<1400`；由
`(d-d_*)^2<=B y_10` 和 `y_10<=4^5 5!` 得 `|d|<1665`。代入 R129
精确 R6 row，并利用此处已核验的 `b>0`，得 `y_12<453000`。于是 H6
Schur 的 2×2 主子式要求
`r_1^2<=B sigma_6<25·453000/44<257387`，但 `r_1>580` 给
`r_1^2>336400`，矛盾。故 `x>1/2`，再用 `|F'|<266` 得
`u_4-u>1/532`，并由 `c+c_4<53/25` 得
`c_4-c>25/28196`。`u<=1.1` 的部分由
`c_4>1.05358` 和 `sqrt(1.1)<1.049` 直接覆盖，反射覆盖负侧。

本轮还把网页端的坐标化 proposition 记录为可复用接口：对
`H_{m+1}=[[H_m,b],[b^T,tau]]>=0` 和任意系数矩阵 `K`，令
`G=K^T H_m K`、`d=K^T b`，则
`d in Ran(G)` 且 `d^T G^+ d<=tau`；若 `K` 张成 `ker H_m`，则 `d=0`。
对 `p(x)=sum p_jx^j`，compatibility defect
`C(p)=sum p_j y_{m+1+j}` 对新 top odd moment `eta=y_{2m+1}` 满足
`partial_eta C(p)=p_m`。故 degree `<m` 的旧 kernel 方向完全不能由新 odd
moment 修复，而 degree `m` 方向至多提供一维可调自由度。这是 R129 的
`p,xp` old-kernel obstruction 的坐标无关版本。

审计目录 marker 包括：`R130W_EXACT_F_BOUNDARY_IDENTITY_PASSED`、
`R130W_EXACT_9P_FG_FACTORISATION_PASSED`、
`R130W_EXACT_RPLUS_DELTA_IDENTITY_PASSED`、
`R130W_C_POLYNOMIAL_TIGHT_BOUND_PASSED`、
`R130W_DELTA_LOWER_BOUND_PASSED`、`R130W_DSTAR_INTERVAL_PASSED`、
`R130W_Y12_R6_UPPER_BOUND_PASSED` 和
`R130W_EXPLICIT_GAP_CANDIDATE_AUDIT_COMPLETED`。

仍然 `OPEN` 的是 `\widehat\Gamma_6` 精确值、genuine 半径、归一化后的高阶
defect propagation、`Gamma_M->0`，以及 positive/backward-OU 条件下由
`P_3K\ne0` 到 exact-zero-set rigidity 的完整推出。R131 应以这条已复核的
显式 gap 为输入，先构造 normalized kernel-defect recurrence，再测试其是否
能给出随阶数增长而不被 `4^M M!` 吞掉的 coercivity。

# 2026-09-08 — R131 normalized Jacobi/Hankel coercivity interface

网页端 R131 在读取 `11ebfac` 后完成了一轮新的理论推进。本机新增
`r131_normalized_defect_audit/`，并把结论严格分层。

对 genuine density `dmu=g dgamma`，若 `g>=0`、`g in L^2(gamma)`，令
`epsilon=||g-1||_2`。Gaussian hypercontractivity 的 degree-`m` 形式
`||p||_4<=3^(m/2)||p||_2` 给出

`(1-epsilon 3^m)||p||_gamma^2 <= ||p||_mu^2
 <= (1+epsilon 3^m)||p||_gamma^2`。

因此 `epsilon 3^m<1` 时，normalized Hermite Gram 满足
`||G_m^mu-I||_op<=epsilon 3^m`；若 `h_k^mu` 是 monic orthogonal norm，
则 `(1-delta_k)k!<=h_k^mu<=(1+delta_k)k!`、`delta_k=epsilon3^k`，并有

`k(1-delta_k)/(1+delta_(k-1)) <= beta_k
 <= k(1+delta_k)/(1-delta_(k-1))`。

这是 `PROVED`（以标准 Gaussian hypercontractivity 为输入）的 genuine
`L^2` coercivity 结果；它不是 relaxed finite Hankel ghost 的结论。固定
shift `j` 后，Gaussian multiplication 给
`||x^j p||_mu^2 <= 4^j (m+j)!/m! · (1+delta_(m+j))/(1-delta_m)
·||p||_mu^2`，解释了为什么在 genuine near-Gaussian 窗口内是 polynomial-in-
`m` 的 fixed-shift growth，而 raw cap `4^m m!` 不足以传播一个小 kernel defect。

网页端还给出并由本机精确审计了三个无扫描的 algebraic interfaces：

1. `R_7` 的 exact row 为 `E Q^7=(128/729)y_14+P_7(y_0,...,y_12)`，
   `y_13` 完全缺席；一般地，`Q^(m+1)` 的总次数为 `2m+2`，若出现
   `y_(2m+1)`，其余指数和为 1，因 `y_1=0` 而消失。这是 `PROVED` 的
   top-odd invisibility。
2. 对 flat rank-`r` 的 `H_m`，kernel generator `p` 的 shifted compatibility
   `C_j=sum_i p_i y_(m+1+j+i)=0` 中，`j=0,...,m-r-1` 不含新 top odd
   `y_(2m+1)`，只有 `j=m-r` 的系数为 monic coefficient `1`。因此有
   `m-r` 条 frozen equations，至多一条可调 odd equation，之后 exact row
   固定 `y_(2m+2)`，再检查 generalized Schur defect。这是 `PROVED` 的 flat
   kernel freedom count；singular non-flat ghost 仍应使用 kernel-compression
   Schur lemma，不能擅自套用 flat ideal。
3. normalized Hermite Gram determinant `D_k` 与 Jacobi coefficient 满足
   `h_k/k!=D_k/D_(k-1)`、`beta_k/k=D_kD_(k-2)/D_(k-1)^2`。故 normalized
   recurrence defect 等价于 Gram determinant 的离散二阶曲率。

本机 marker：`R131_R7_TOP_ODD_INVISIBILITY_PASSED`、
`R131_HERMITE_DETERMINANT_JACOBI_DICTIONARY_PASSED`、
`R131_FLAT_KERNEL_ODD_FREEDOM_COUNT_PASSED`、
`R131_OU_CUBIC_EIGENSCALING_INTERFACE_PASSED`、
`R131_NORMALIZED_DEFECT_AUDIT_COMPLETED`。

必须降级的一点是：网页端使用了
`||P_(rho^N)h_N-1||_2=O(rho^(3N/2))` 的 uniform tower 假设来推出
`m=theta N` 的 growing Jacobi window。当前本机已有 R57 直接支持的是
`m_3^2<=2lambda(2-lambda)`，这不足以自动给出整段 `L^2` smoothing。因此
该 growing-window corollary 标为 `CONDITIONAL`，不能列入无条件主定理。

当前真正的 OPEN 已被压缩为：证明或构造反例说明 uniform `L^2` smoothing，
并建立一个 same-factor separation：非零 `P_3K` 必在
`k<=c log(1/||g-1||_2)` 的 normalized Jacobi/Gram 曲率上产生固定缺陷。
若该桥成立，R131 的 `epsilon3^m` 窗口即可与之矛盾；否则仍不能从
`m_3=0` 偷换到 `P_3K=0`，也不能完成 positive backward-OU exact-zero-set
rigidity。

## 62. R132：exact-law OU smoothing 与 log-density 弱桥接（2026-09-08）

网页端 R132 对 R131 暂时条件化的 uniform backward-OU 输入作了独立审计，
并把 genuine all-row exact class 与 scalar `RK=1` 路线严格分开。本轮本机新增
`r132_exact_law_smoothing_audit/`，审计脚本核验 Mehler 常数、OU 半群因子、
log-density 常数以及 fixed-level Jacobi 关系。

### 62.1 all-row exactness 给出统一尾部

设 `mu` 是 centered、variance-one 的真实概率律，`X_1,X_2,X_3` 独立同分布，
并且实际满足所有

`E Q^r=2^r r!`, `Q=sum_i (X_i-Xbar)^2`。

Carleman 条件成立，因为
`(2^r r!)^(-1/(2r)) >= (2r)^(-1/2)`，故 `Q` 的矩问题在 `[0,infty)` 上
determinate；于是 `Q~chi^2_2`，从而对 `0<eta<1/4`

`E exp(eta X^2) <= exp(-eta)/(1-4 eta)`。

这里的 all-row 真实 expectation 是实质条件。有限行、formal row、relaxed
Hankel ghost，或尚未证明等价的 scalar `RK=1`，均不能直接使用该尾界。

### 62.2 uniform smoothing theorem

若 `h=dmu/dgamma`，且采用项目约定 `P_t psi_n=t^(n/2)psi_n`，则网页端给出

`||P_t h-1||_2 < 8 t^(3/2)`, `0<t<=1/2`。

证明链为：

1. 用 all-row exactness 和 Carleman 得到 `Q~chi^2_2`；
2. 由 `Q>= (X_1-X_2)^2/2` 与条件 Jensen 得到上述 square-exponential tail；
3. 用一次 `P_(1/2)` 的 Mehler 预平滑和 tail bound 得
   `||P_(1/2)h-1||_2<2 sqrt(2)`；
4. centered/variance-one 消掉 Hermite 0、1、2 阶，再用半群性
   `P_t h-1=P_(2t)(P_(1/2)h-1)`，得到常数 `8`。

同样由 Gaussian hypercontractivity 外层分解，还得到

`||P_t h-1||_p <= 8(p-1)^(3/2)t^(3/2)`,

对 `p>=2` 且 `t<=1/(2(p-1))`。因此 genuine all-row depth-`N` tower 的
`g_N=P_(q^N)h_N` 满足

`||g_N-1||_2 <= 8 q^(3N/2)`，

并在 `m_N=floor(theta N)`、
`theta<3 log(1/q)/(2 log 3)` 时得到 growing normalized Hermite-Gram/Jacobi
window。该结论现在是 `PROVED`，但只在 genuine all-row exact class 内成立。

### 62.3 Mehler 精确公式的文字纠正

在上述参数约定下，若 `M_s` 是相对于 `gamma` 的 Mehler kernel，则直接配方给出

`int M_s(x,y)^2 dgamma(x)
 = (1-s^2)^(-1/2) exp(s y^2/(1+s))`。

此前记录把精确前因子误写成 `(1+s)^(-1/2)`，原因是配方后漏掉了 `1-s`；
正确的 `(1-s^2)^(-1/2)` 才是 exact identity。本机 R132 审计现已改为直接
核验该式。它在 `s=1/2` 时产生算子范数因子 `(4/3)^(1/4)`，与尾界中的
`exp(-1/6)` 合并仍小于 `1`，故 `||P_(1/2)h||_2<3` 和后续常数 `8` 不变。

### 62.4 从正性到 log-density 的局部结果

令 `g=P_t h` 且 `t<=1/64`。由 `E X^2=1`、Chebyshev 和 Mehler 正性，

`g(x)>=(3/4) exp(-3) exp(-x^2/63)`。

因此 `g^(-1)` 有显式 inverse-
`L^4` 控制；配合 R132 的 `L^4` smoothing，得到

`||log g||_2 <= C_K t^(3/2)`。

若 `ell_3(g)=<log g,He_3/sqrt(6)>`，则

`ell_3(g)=t^(3/2)m_3(h)/sqrt(6)+O(t^3)`。

这首次把 `P_3 log g` 与 genuine cubic moment 连接起来，但只是弱桥接，不是
zero-set rigidity。full exact class 中 `y_4=3` 还给出

`1-beta_2(g)/2=m_3(g)^2/2=3 a_3(g)^2`，

说明 fixed Jacobi level 只看见随振幅消失的二次缺陷，不能自行产生 fixed
positive separation。

### 62.5 明确障碍与当前 OPEN

仅 positivity、mean zero、variance one 和 individual `L^2` 不给 uniform
fixed-time smoothing：稀有远端 Gaussian mixture 可使平滑后的 likelihood-ratio
`L^2` 范数发散。故 R132 的统一性来自 all-row exactness 产生的 tail，而非
普通 OU smoothing。

本轮仍未解决：

- scalar `RK=1` 到 all-row/full-`Q` law 的严格接口；
- `P_3K != 0` 到 logarithmic-degree normalized Jacobi/Gram fixed defect 的
  same-factor angular-to-Jacobi amplification；
- `Gamma_M->0` 与 Positive Backward-Tower Exact Zero-Set Rigidity。

R132 将下一轮唯一目标压缩为：从 exact same-factor identity 直接构造
`log-density -> normalized Gram determinant curvature` 的 all-degree quantitative
identity，或给出严格 no-go。证据等级：R132 smoothing、`L^p`、log-density 弱桥接
和 fixed-level Jacobi/log 关系为 `PROVED`（以标准 Gaussian 分析输入为前提）；
scalar `RK=1` 应用和最终 separation 仍为 `CONDITIONAL/OPEN`。

## 63. R133：首个奇阶 Jacobi 包与有限行盲区

### 63.1 必须先固定的对象层级

网页端本轮把空间 log-density
`K_sp=log g`、`ell_3=<K_sp,psi_3>` 与 normalized Bargmann log
`C_g=log B_g` 分开。一般 `C_g=log B(e^{K_sp})`，并不等于 `B(K_sp)`；因此
只有在项目定义明确把 `P_3K_sp` 表示为 `ell_3` 时，才能把
`P_3K_sp!=0` 直接代入下面的 charge 结论。

同样，下面的 same-factor identity

`< exp(sum_j C_g(z r_j(theta))) >_theta=1`,

其中 `r_j=sqrt(2/3)cos(theta+2pi(j-1)/3)`，只在 genuine full exact law
并具备原点解析性时使用。scalar `RK=1`、relaxed Hankel ghost 或未经平滑的
非 `L^2` 顶层不能自动套用；对 `g=P_t h`、`t>0` 的 genuine smoothed level
则可在相应解析性条件下应用。

### 63.2 Theorem R133-A（首个奇阶精确包）

设 `d=2s+1>=3` 是第一个非零奇 cumulant 阶数，`k=s+1`，并假设上述
same-factor identity 成立。角平均的偶阶递推首先给出

`kappa_4=kappa_6=...=kappa_{2d-2}=0`。

这是关键逻辑补全：不能仅凭“首个非零奇阶为 d”就声称低阶 moments 全为
Gaussian；必须先用 identity 的偶系数方程逐阶消去这些 even cumulants。于是
到次数 `d+1` 为止，唯一非 Gaussian Hermite coordinate 是
`a_d=kappa_d/sqrt(d!)`，并且

`alpha_0=...=alpha_{s-1}=0`, `beta_j=j (1<=j<=s)`,

`alpha_s=kappa_d/s!`,

`1-beta_{s+1}/(s+1)
 = alpha_s^2/(s+1)
 = binom(2s+1,s)a_{2s+1}^2`.                         (R133-A)

等价的 monic determinant 形式为

`D_{s+1}D_{s-1}/D_s^2-1
 = -binom(2s+1,s)a_{2s+1}^2`.                         (R133-A')

证明是一个单一的末端 `2x2` Gram block：Hermite product formula 给出唯一
非单位项 `G_{s,s+1}=sqrt(binomial(d,s))a_d`，其 determinant 为
`1-binomial(d,s)a_d^2`；Jacobi dictionary
`beta_j/j=D_jD_{j-2}/D_{j-1}^2` 与
`d!/(s!^2(s+1))=binomial(d,s)` 完成等式。该条目在 genuine analytic
full same-factor 假设下为 `PROVED`，对原始 scalar `RK=1` 接口仍是
`CONDITIONAL`。

若项目 convention 下 `P_3K_sp!=0` 等价于 `ell_3!=0`，则 `g` 非偶，因而
存在某个首个奇阶 `d`，并得到某个 `k=(d+1)/2` 的严格缺陷。这里“严格”只
表示对每个固定对象 `Delta_k>0`，不表示有与对象无关的 fixed positive gap，
因为 `d` 可漂移且 `a_d` 可趋于零。

### 63.3 首个 packet 的严格 no-go

令 `epsilon=||g-1||_2`。Parseval 和 (R133-A) 给出

`Delta_k<4^k epsilon^2`。

若 `k<=log_3(1/epsilon)`，则

`Delta_k<=epsilon^(2-log_3 4)->0`,

因为 `4<3^2`。所以首个 odd packet 不能在 R131 的 subcritical normalized
Gram window 内产生 fixed separation；剩余问题确实是跨 degree 的 cascade，
而不是再优化同一首个 odd coefficient。

### 63.4 Proposition R133-B（有限行 genuine blindness）

固定 `m>=2`。可取非零 `f∈C_c^infty((2,3))` 满足
`int x^r f dgamma=0`、`0<=r<=2m`。令 `g=1+lambda f`，并把 `lambda`
取得足够小，则 `g` smooth、strictly positive、centered、variance-one，且
前 `2m` 个 moments 与 Gaussian 完全一致，所以前 `m` 个 Jacobi 系数仍是
`beta_j=j`。但因为 `psi_3>0` 于 `(2,3)`，

`Q_f=int f^2 psi_3 dgamma>0`,

且

`<log(1+lambda f),psi_3>
 = -lambda^2 Q_f/2+O(lambda^3)<0`。

故任何固定有限行（即便允许 genuine positive density）都不能单独把 nonzero
log charge 推成 finite Jacobi defect。这是 `PROVED` obstruction，不是原始
全阶 same-factor exact 命题的反例；它也排除了把 R132 的 growing window 单独
当作最终 rigidity 证明的做法。

### 63.5 当前唯一下一步：R134 Critical-Layer Same-Factor Jacobi Cascade

必须从 same-factor angular identity 推导跨所有 degree 的 cumulative normalized
Jacobi curvature 的 energy/telescoping identity，或者严格给出其 obstruction。
所需结果应明确输入（genuine positivity、full exact rows、(SF)、OU backward
divisibility）和输出（可累积的 curvature charge、depth-independent lower
bound 或相反的构造）。任何 `9^m` amplification 只能在精确 identity 推出后
写入；不能用猜测替代证明。R133 本机审计目录为
`r133_first_odd_jacobi_audit/`，marker 与 R132 精确 Mehler 修正均已记录。

## 64. R135：Critical Tensor-Leakage Anti-Shielding

### 64.1 路线位置与边界

R135 把 R134 剩下的未知量 `rho_(n,theta)` 明确成真实概率空间上的正投影
二次型。结论必须分层：genuine positive law、有限矩和所需解析性下的
R135-A 为 `PROVED`；从 scalar `RK=1` 迁移到 full-SF/all-row 仍为
`CONDITIONAL`；R135-B 只有 finite-SF prefix，不能称为原命题反例；
all-degree probability completion 仍为 `OPEN`。

### 64.2 Theorem R135-A：精确投影与首层条件方差

令 `X_1,X_2,X_3` 独立同分布于 `mu`，`Y_theta=sum_j r_j(theta)X_j`，
`Pi_n^theta` 是 `Y_theta` 分布的 monic degree-n OP。以 one-body
orthonormal Jacobi basis 的 tensor total-degree 分解写

`Pi_n^theta(Y_theta)/sqrt(n!) = F_(n,theta)+R_(n,theta)`，

其中 `F` 属于 total degree `n`，`R` 属于 degrees `<n`，并定义
`rho_(n,theta)=||R_(n,theta)||^2`。若 `P_<n^theta` 是
`span{1,Y_theta,...,Y_theta^(n-1)}` 的正交投影，且
`E_(n,theta)=psi_n(Y_theta)-F_(n,theta)`，则

`R=(I-P_<n^theta)E`，
`rho=<E,(I-P_<n^theta)E>`。

因此 `rho` 是显式 positive Schur/Christoffel projection，而不是任意残差。
若 `U_(m,l)=<psi_m,varphi_l>_mu` 是 Hermite-to-Jacobi connection matrix，
则 `U` 由 one-body Jacobi matrix 的递推完全决定；对每个 tensor index
`a`，`E` 的系数为

`C_a = sum_{i_1+i_2+i_3=n, i_j>=a_j}
 sqrt(binomial(n;i_1,i_2,i_3)) prod_j r_j^(i_j) U_(i_j,a_j)`。

若 `B` 是 `P_<n^theta` 在 tensor basis 中的正交列矩阵，则
`rho=C^*(I-BB^*)C`。

进一步令 one-body Jacobi diagonal cumulative sum
`S_m=sum_(l=0)^m alpha_l`。在 total degree `n-1` 上，设
`a_1+a_2+a_3=n-1`、`p_j=r_j^2`、
`Z_a=n sum_j r_j S_(a_j)/(a_j+1)`，则

`rho^[n-1] = (1/n) sum_|a|=n-1 multinomial(n-1;a) p^a q_a
 (Z_a-S_(n-1)^theta)^2`.

除以 `T_(n-1,theta)` 后，等价于

`rho^[n-1] = T_(n-1,theta)/n *
 [ Var_nu(Z) + (E_nu Z-S_(n-1)^theta)^2 ]`.

特别有 `rho >= T_(n-1,theta) Var_nu(Z)/n`。这给出 R135 的首个真正
`PROVED` coercivity，但它只约束首层 transverse fluctuation，并非对整个
`rho` 的 uniform anti-shielding。

### 64.3 Theorem R135-B：finite-SF 的近乎完全 shielding

固定 `n>=3`，令 `d=2n-1`。在 `L^1(gamma)` 中对
`V_n=span{x^r:0<=r<=2n, r!=d}` 做 `x^d` 的最佳逼近 `v_*`，令
`R=x^d-v_*`、`f_n=sign(R)`。一阶最佳逼近条件给出

`int x^r f_n dgamma=0 (0<=r<=2n, r!=d)`，
`int x^d f_n dgamma=int |R| dgamma>0`。

于是 `g_epsilon=1+epsilon f_n` 在 `0<epsilon<1` 时是严格正的
probability density，且 centered、variance-one、`||g_epsilon-1||_2=epsilon`。
到 degree `2n`，唯一非 Gaussian Hermite coordinate 是 `a_d!=0`；因 `d`
为奇数且 `2d>2n`，其 same-factor angular identity 逐系数精确到 `z^(2n)`。

令 `Delta_n=binom(2n-1,n-1)a_d^2`，则 angular law 上有精确三分解

`sigma_(n,theta)=Delta_n p_(2n-1)(theta)^2`，
`rho_(n,theta)=Delta_n[p_(2n)(theta)-p_(2n-1)(theta)^2]`，
`rho+sigma=Delta_n p_(2n)(theta)`。

由 `|r_j|^2<=2/3` 和 Cauchy-Schwarz，
`p_(2n-1)^2 <= (2/3)^(n-2) p_(2n)`，从而

`rho/(rho+sigma) >= 1-(2/3)^(n-2)`。

同时所有 angular Hermite charges 到 degree `n` 为零，且原始 normalized
Jacobi curvatures 对 `j<n` 完全 Gaussian、`beta_n/n=1-Delta_n`。取
`epsilon_n=3^(-n)`，恰有 `n=log_3(1/epsilon_n)`，并由 `|a_d|<=epsilon_n`
得 `Delta_n<(4/9)^n ->0`，而 shielding 比例趋于 1。

该构造是 genuine positive `L^2` density 和 finite-SF obstruction，
但不是 all-degree SF，因此没有构造原始命题的 counterexample。它严格排除
任何只使用当前有限 charge horizon 的 `rho_n<=eta_n A_(<=n)` 或 universal
fixed-fraction anti-shielding 证明机制，并显示真实 charge horizon 至少要到
`2n-1`，存在 degree-doubling barrier。

### 64.4 cubic tangent 与 critical-layer 判决

在 fixed `n` 的 cubic tangent `g_c=1+c psi_3/sqrt(6)+o(c)` 下，本机核验

`<rho_n> = [n(n-1)/4] c^2 <p_4-p_3^2> + o(c^2)`，

而 D3 角平均 `<p_4>=1/2`、`<p_3^2>=1/12`，故
`<rho_n>=(5/48)n(n-1)c^2+o(c^2)`。因此 cubic Hessian 只有 `O(n^2)`，
`9^n` 仍只是 generic Gram/residual upper capacity，不是 lower gain。
在 R135-B 中，`lambda_n^{-1}` 的指数因子被 production 自带的同一个
`lambda_n` 完全抵消：`lambda_n^(-1)(1-<T_n>)=Delta_n`。

### 64.5 对总命题的含义与下一轮

对彼此不相容的 finite-depth positive backward towers，任意 growing-but-finite
SF prefix 仍可能把缺陷藏在未来 degree，因此必须使用真正 all-degree
coherence；projectively compatible infinite tower 仍沿既有 production-decay
路线处理。当前 Jacobi 路线应精确判定为：`local/rowwise anti-shielding =
NO-GO`，`global all-degree extension = OPEN`。

R135 之后唯一任务更新为 **R136 — Full-SF Leakage Extension Rigidity**：
判断 R135 的 near-total finite prefix shielding 是否能延拓为 genuine
all-degree one-body SF law；必须寻找全阶 positive sum rule，或证明该 completion
仍可存在。不得再重复估计当前行的 `rho`，也不得把 finite prefix 当成原命题反例。

## 65. R136：Full-SF 形式完成与 genuine 全阶边界

### 65.1 路线位置

R136 对 R135 的 finite-prefix shielding 做了最小但关键的升级：不再估计某一行
Jacobi 残差，而是把 full same-factor identity 的所有系数写成一个角平均的
形式生成函数。令 `C(z)=sum_(m>=3)c_m z^m`，

`F_C(z)=< exp(sum_(m>=3)c_m p_m(theta)z^m) >_theta`，

其中 `p_m=sum_j r_j^m`、`r_j=sqrt(2/3)cos(theta+2pi(j-1)/3)`。原点恒等式
要求 `F_C(z)=1`。这一步仍在 full-SF、原点解析性和 genuine 接口成立的条件
下使用；它不是从 scalar `RK=1` 自动推出的等式。

### 65.2 Theorem R136-A：形式系数代数的精确结论

平移 `theta -> theta+pi` 使 `p_m -> (-1)^m p_m`。因此每个奇总次数的
角平均恒等式自动为零，奇系数方程本身不提供约束。对偶次数 `2N`，最新偶
变量 `c_(2N)` 的系数是

`A_(2N)=<p_(2N)>=3 binom(2N,N)/6^N>0`。

故给定任意奇形式序列，偶变量可以逐阶唯一递归补齐；这说明 full-SF 的
coefficient algebra 本身不能强迫首个 odd charge 消失。证据等级是
`FORMAL-PROVED`：递推不等于收敛，也不等于存在概率分布。

若 `d` 是首个非零奇次数，则在 `2d<=M<4d` 的 exact future band 中，偶方程
只有一个线性 pivot 和 odd-pair source：

`A_M c_M + 1/2 sum_(a+b=M, a,b odd>=d) B_(a,b)c_a c_b=0`,

`B_(a,b)=<p_a p_b>`。

特别地，`c_(2d)=-B_(d,d)c_d^2/(2A_(2d))<0`；但下一阶含有
`-B_(d,d+2)c_d c_(d+2)/A_(2d+2)` 的 mixed term，符号不再固定。若只给
`c_d` 而令其余 odd 变量为零，形式支撑只落在 `2kd`，仍没有逐系数正性
矛盾。这是对“SF/Jacobi 代数自动产生正级联”这一想法的严格 `NO-GO`。

本机目录 `r136_full_sf_formal_audit/` 的审计 marker 为：

`R136_PARITY_AND_EVEN_PIVOT_PASSED`

`R136_FIRST_FUTURE_BAND_PASSED`

`R136_EXPLICIT_FUTURE_COEFFICIENTS_PASSED`

`R136_SPARSE_SUPPORT_PASSED`

`R136_BOCHNER_BOUNDARY_RECORDED`

`R136_AUDIT_COMPLETED`

### 65.3 R136-B：有限截断的 genuine realization 不是全阶反例

对任意固定 cutoff `M`，形式解只涉及有限个 cumulant/Hermite 坐标。可以在
Gaussian 空间中取紧支撑、有界的双函数，消去 `psi_0,psi_1,psi_2` 并匹配
所需的有限 Hermite jet；充分小的振幅给出 smooth strictly positive、
centered、variance-one 的 `L^2(gamma)` density，实现同一个有限 jet。因此
任何固定有限 cutoff 都不能阻止 non-Gaussian positive realization。

但该构造的正性阈值依赖 `M`，函数也随 `M` 改变。它没有给出单个密度实现
所有次数的形式 completion；更没有证明 `phi(t)=exp(-t^2/2+C(it))` 是
positive definite。故 R136-B 的等级是 `FINITE-CUTOFF PROVED`，不是原始
all-degree 命题的 counterexample。

### 65.4 生成函数能量与真正的剩余问题

若 full angular law 能解释为概率密度 `sigma_z`，则相对熵

`S(z)=D(uniform || sigma_z)=-<K_z> >=0`

是 genuine 的全函数非负性，但非负函数的 Taylor 系数不必逐项非负；因此
熵的正性不能恢复被奇偶对称消掉的 odd equations。任何更强的 Szego/Hankel
表示都必须先核验适用的测度、正则性和归一化，不能作为未经证明的 sign
cascade。

于是总路线得到一个明确的小里程碑：

* `PROVED / FORMAL`：all-degree SF/Jacobi coefficient algebra 对任意 odd
  formal input 存在唯一 even formal completion；
* `PROVED / FINITE-CUTOFF`：每个固定 cutoff 可由 genuine positive density
  实现；
* `NO-GO`：局部 rowwise anti-shielding、finite-prefix curvature、以及
  coefficientwise SF/Jacobi 正级联均不足以完成 rigidity；
* `OPEN`：这些形式 completion 是否能统一满足 Bochner positive
  definiteness、全阶 Hankel/Jacobi 正性、解析增长和单个 all-degree density。

### 65.5 下一步：R137 Uniform Genuine-Realization Breakdown

唯一值得继续的方向是研究 cutoff `M` 增大时 genuine realization 的统一性：

1. 证明任意实现 R136 形式 jet 的 positivity、Bochner 或 Hankel/Jacobi
   常数必随 `M` 崩溃，从而把有限截断障碍升级为全阶 rigidity；或
2. 构造 cutoff-uniform 的 positive realization，若能通过 Bochner、解析增长和
   all-degree SF 检查，则得到 genuine non-Gaussian completion，直接改变总命题
   的判决。

R137 必须报告量化的 uniform norm/positivity constant、明确的 tightness 或
   compactness 论证，并把 scalar `RK=1` 到 full-SF 的接口单独标成
   `CONDITIONAL`。在此之前，不得把形式递推或任意有限 prefix 写成原命题反例。

## 66. R137：Uniform Genuine-Realization Breakdown / Bochner Tail Rigidity

### 66.1 固定 sparse odd branch 的第一 Hankel cap

本轮先审计 R137 的量词，而不是把网页端推导直接当作仓库事实。固定
`d=2s+1>=5`，令 `c_d=a` 且其余 odd cumulants 为零；formal even coefficients
仍由 full-SF 递归决定。由于 `kappa_d=d!a`，其首个 Jacobi packet 满足

`1-beta_(s+1)/(s+1)=d! binom(d,s) a^2`.

直接从 `M(z)=exp(z^2/2+a z^d)` 构造到阶 `2(s+1)` 的 formal moments，可得

`det H_(s+1)(a)=(prod_(j=0)^s j!) [1-d! binom(d,s)a^2]`.

故任何 PSD Hankel jet 都必须满足
`|a|<=R_d=[d! binom(d,s)]^(-1/2)`。

### 66.2 Theorem R137-A：square-exponential law 的 finite odd-support rigidity

设 centered probability law `mu` 满足 `E_mu exp(eta X^2)<infty` 对某个 `eta>0`。
则 `M(z)=E exp(zX)` 为 entire，`K=log M` 在实轴上 real analytic。若 odd
cumulant support有限，则 `K_o(t)=(K(t)-K(-t))/2` 是一个 odd polynomial。

在 R132 的全阶 exact-tail 接口下，取 `eta=1/8` 得

`M(t)<=2 exp(-1/8) exp(2t^2)`, `M(t)>=1`,

因而 `|K_o(t)|<=K_e(t)<=2t^2+L`，其中 `L=log 2-1/8`。非零 odd polynomial
次数 `>=3` 不满足该二次增长；centered 又消去一次项。因此所有 odd cumulants
必须为零。证据等级：`PROVED`。特别地，R136 sparse branch 的 `a!=0` 不可能
来自 square-exponential genuine law；此结论本身不需要 SF，SF 只在应用时提供
全阶 tail。

### 66.3 Theorem R137-B：fixed-d Hankel feasibility radius collapse

令 `H_M(a)=[m_(i+j)(a)]_(i,j=0)^M`，并定义

`I_M^H(d)={a:H_M(a) >= 0}`，

`I_M^+(d)` 为存在 strictly positive centered variance-one `g dgamma`、匹配
formal moments 至 `2M` 阶的 genuine 集合。则

`I_(M+1)^H subset I_M^H`，`I_M^+ subset I_M^H`，且 `I_M^H subset [-R_d,R_d]`
对 `M>=s+1`。若某个 `a!=0` 属于所有 `I_M^H`，全阶 Hamburger 表示测度的
三变量 zero-sum mixture 具有 Gaussian 的所有 polynomial moments；对
`Q=sum_i(X_i-Xbar)^2` 得 `E Q^r=2^r r!`。R132 的 Carleman/差分桥随后给
square-exponential tail，R137-A 与 `kappa_d=d!a!=0` 矛盾。因此

`intersection_(M>=s+1) I_M^H(d)={0}`.

由于这些集合嵌套、闭且被 `[-R_d,R_d]` 统一包含，令
`rho_M(d)=max{|a|:a in I_M^H(d)}`，则

`rho_M(d) down 0`。

这给出 construction-independent 的 fixed-`d` feasibility-radius collapse，
并推出每个 fixed `a!=0` 在某个有限 Hankel/Jacobi level失败。证明是定性紧性
证明；没有得到 first-failure index `m_0(a,d)` 的显式阶，也没有排除
`d_M->infty, a_M->0` 的移动 selector 序列。

### 66.4 cutoff-uniform compactness 与 Bochner边界

R136 的 finite interpolation 保证每个固定 `M` 有某个 `delta_M>0`，但 R137
证明其最大可行幅度满足 `0<rho_M^+(d)<=rho_M(d)->0`；因此这不是某个插值构造
的偶然缺陷。若 finite-jet densities另有 `sup_M ||g_M||_p<infty`（`p>1`）
或统一 square-exponential moment，弱紧性与一致可积性产生 all-moment genuine
极限；要得到 pointwise analytic SF，需后一个统一解析尾条件，单独 `L^p` 弱
收敛只保证 moment realization。

固定点集的低阶 Bochner minor 不能直接提供 rigidity：`0,t,2t` 的 `3x3`
行列式 Gaussian 主项从 `t^6` 开始，而 hidden odd degree `d>=5` 的相位经二次
进入通常要到 `a^2 t^(2d)`；这解释了 local test 的失效，但没有否定需要更高阶
全局测试的可能性。

### 66.5 本轮总判决与下一步

`PROVED`：finite odd support 在 square-exponential tail下只能为零；固定 `d`
的 Hankel 可行半径 `rho_M(d)->0`；统一 `L^p`/square-tail 是从 finite jets
到 all-moment law 的充分紧性接口。

`OBSTRUCTION`：R137 未给出 `m_0(a,d)` 的显式增长率；`d_M->infty`、`a_M->0`
的 incompatible selector sequence 仍未排除；单个低阶 Bochner minor 不够。

`CONDITIONAL`：scalar `RK=1` 到 genuine full-SF/all-row，以及 `K_sp=log g`
与 `C_g=log B_g` 的识别。

`OPEN`：具有 infinitely many nonzero odd cumulants 的 genuine full-SF law 是否
存在。路线因此没有升级为 global no-go；但 fixed sparse branch 已被严格排除，
唯一下一轮任务是 **R138 — Infinite-Odd-Tail Bochner Phase Rigidity**。

## 67. R138：Infinite-Odd-Tail Bochner Phase Rigidity 审计

### 67.1 零点除子与 odd cumulant tail

若 genuine centered law 满足 `E exp(eta X^2)<infty`，则 ordinary MGF
`M(z)=E exp(zX)` 是 order 至多二的 entire function。genus-two Hadamard
分解给出，对 `m>=3`：

`kappa_m=-(m-1)! sum_nu zeta_nu^(-m)`。

按零点重数定义 `R_Delta=min{|zeta|:n(zeta)!=n(-zeta)}`，空集取 `infty`。
在最小非配对半径上，有限 reciprocal-zero exponential sum 的 Cesaro mean
square 严格为正，因此

`limsup_(m odd)(|kappa_m|/(m-1)!)^(1/m)=1/R_Delta`。

这是 `PROVED` 的零点/odd-tail 对应。故 finite odd support 和
`limsup_(m odd)(|kappa_m|/(m-1)!)^(1/m)=0` 的超指数 normalized tail 都会
强制对称；普通指数衰减不能被此机制排除，因为它正对应有限半径的非配对零点。

若 `C_g=log B_g` 能延拓为 entire function，则 `B_g=e^{C_g}` zero-free；
有限阶 Hadamard rigidity 与 centered variance-one normalization 给 Gaussian。
在 full-SF 下，有限总零点也同样给 Gaussian。因此 genuine non-Gaussian
candidate 必须同时具有 infinitely many complex MGF zeros 和 infinitely many
nonzero odd cumulants。这一段是 `PROVED`，但不等于 global phase rigidity。

### 67.2 full-SF 实轴预算和 Fisher identity

令 `K=log M=t^2/2+C`，`E=(K(t)+K(-t))/2`，`O=(K(t)-K(-t))/2`，
`H(t,theta)=sum_j C(t r_j(theta))`。Jensen、centeredness 和 full-SF 给出

`0<=E(t)`，`|O(t)|<=E(t)`，`average E(R cos theta)<=R^2/4`，
以及更强的 `E(x)<=x^2`。

对 `t!=0`，角向二阶导数与 `r_j''=-r_j`、`(r_j')^2=2/3-r_j^2` 给出

`<e^H(H_t^2+H_theta^2/t^2)>`
`=(2/3)[3-<e^H sum_j K''(t r_j)>]<=2`。

因此 `int_0^T |O''|<=E'(T)`，并有安全的
`int_0^T |O''|<=8T+(log 2-1/8)/T`。进一步把 `H` 分成 even/odd angular
parts，若 `Q_r=<H_o exp(-3ir theta)>`，则

`sum_(r>=1,r odd)|Q_r(t)|^2 <= exp(t^2/2)(1-exp(-S(t)))`
`<= (t^2/2)exp(t^2/2)`。

这是 `PROVED` 的全阶 resummed odd-charge budget；它控制 Fourier 重求和，
不控制每个 odd cumulant 的绝对值，因而仍允许跨 degree cancellation。

### 67.3 Bochner、Hankel 与 compactness 边界

固定节点 `x_0,...,x_m` 时，square-exponential tail 下的 small-frequency
Bochner determinant 满足

`det[phi(h(x_i-x_j))]`
`=h^(m(m+1)) Vandermonde(x)^2 Delta_m/prod_(k=0)^m(k!)^2`
`+O(h^(m(m+1)+2))`。

节点 `0,1,...,m` 时 Vandermonde 恰好抵消。hidden degree `d=2s+1` 的第一
个敏感矩阵是 `(s+2)x(s+2)`，而 `0,t,2t` 的 Gaussian minor 开头为
`2t^6-4t^8+O(t^10)`；hidden phase 先以 `a^2t^(2d)` 进入。因此有限固定
Bochner test 是 `OBSTRUCTION`，不是 global no-go。

若同一个 formal full-SF moment sequence 的 finite-jet genuine realizations
满足 `sup_M E exp(eta X_M^2)<infty`，或满足
`sup_M ||g_M||_(L^p(gamma))<infty`（`1<p<infty`），则 tightness、uniform
integrability 和 weak compactness 给出 genuine all-moment limit；square-tail
还把形式 SF 逐项升级为实际 entire-MGF identity。这是 `PROVED` 的充分接口，
不是 uniform bound 的来源。对 fixed sparse branch，R137 已证明
`rho_M(d)->0`；对 `d_M->infty,a_M->0` 的 moving selector 则不能套用 fixed-d
结论。

### 67.4 两类 positive backward tower

在 genuine full-SF/all-row 假设下，R132 tail 给每个 law 统一的 MGF zero-free
disk `|z|<=1/4`。若 single bottom law 满足
`g_0=P_(q^N)h_N` 对所有 `N`，则 normalized Bargmann scaling
`B_(g_0)(z)=B_(h_N)(q^(N/2)z)`。bottom 的任意零点会被缩到所有顶层共有的
zero-free disk 内，故 bottom zero-free；finite-order rigidity 立即给
`g_0=Gaussian`。这是 `PROVED`，但从 bare scalar `RK=1` 到 genuine full-SF
仍为 `CONDITIONAL`。

对每个 `N` 可更换顶层的 incompatible finite-depth towers，bottom law 也随
`N` 变化，且 moving degree `d_N->infty`、amplitude `a_N->0` 仍可逃逸；该
情形是 `OPEN`。固定 finite-SF selector、moving selector sequence 和 single
genuine all-degree law 必须分开。

### 67.5 R138 判决

* `PROVED`：Hadamard zero-divisor formula；非配对零点半径的 odd-tail root
  formula；finite-zero/zero-free rigidity；full-SF Fisher 与 resummed odd
  budget；finite Bochner leading term；cutoff-uniform compactness interface；
  compatible genuine backward-tower Gaussian rigidity。
* `OBSTRUCTION`：finite local Bochner tests、coefficientwise positivity、
  real-axis convexity alone、merely exponential normalized odd-tail bounds，
  以及 fixed sparse branch 的 first failing Hankel index 尚无显式阶。
* `CONDITIONAL`：scalar `RK=1` 到 genuine full-SF/all-row，以及从 ordinary
  MGF/Bargmann 结论回到 spatial `P_3 K_sp`。
* `OPEN`：具有 infinitely many nonzero odd cumulants 和 asymmetric infinite
  zero divisor 的 genuine full-SF law是否存在；以及 incompatible moving-top
  positive backward tower。

下一轮只研究：**R139 — infinite zero-divisor phase rigidity / cross-degree
Bochner majorization**。目标是在已知非配对零点半径和 `Q_r` 总预算的条件下，
寻找跨所有 Fourier charges 的正定性不等式；若不能闭合，给出明确的
finite-node cancellation witness 和剩余的最小 global gap。

## 68. R139：zero-divisor phase / cross-charge Bochner audit

### 68.1 零点除子与无限变号

网页端 R139 的长篇推导经本机独立审计后，保留以下 genuine square-exponential
结论。按 `zeta -> -zeta` 轨道合并零点重数，令
`delta(zeta)=n(zeta)-n(-zeta)`，则奇数阶满足

`kappa_m/(m-1)!=-sum_R delta(zeta)zeta^(-m)`。

最小非配对壳上的 finite exponential sum 在 Cesaro mean square 意义下严格
非零，所以 `limsup_(m odd)(|kappa_m|/(m-1)!)^(1/m)=1/R_Delta`，并在无穷
子序列上有相应 quantitative lower bound。逐阶 lower bound 不成立；共轭壳
`R exp(+-i pi/6)` 给 `2R^(-m)cos(m pi/6)` 的精确 formal cancellation
witness。

新的 genuinely analytic partial theorem 是：非对称 square-exponential law 的
odd cumulants 必有无限多个正值和无限多个负值。证明是 finite odd Taylor
radius 与实轴 real analyticity 的组合，Pringsheim 只在该有限半径条件下使用，
不能泛化到可能 entire 的 odd series。

### 68.2 跨 Fourier charge 的正能量与失败机制

把 `H_o` 展开成 `3r`、`r` odd 的 Fourier modes，Fisher identity 和
`H>=-t^2/2` 给出 `PROVED` 的

`sum_(r odd)(|Q_r'|^2+9r^2|Q_r|^2/t^2)<=exp(t^2/2)`。

任意非负 `t` 权、右端可积时可由 Tonelli 积分。不同 charges 在该能量中不
能互相抵消；剩余的精确逃逸是同一个 `Q_r` 内不同 degrees/zero shells 的
相消。有限 odd degree 线性代数给出了 `Q_r(t_0)=Q_r'(t_0)=0` 的 nonzero
formal witness，因此该上界目前不能反向成为 first-shell coercive lower gap。

### 68.3 Bochner、even cone 与路线边界

hidden degree `d=2s+1` 首次进入 Hankel/Bochner level `s+1`，对应矩阵尺寸
`(d+3)/2`。任意有限测试族仍能在足够小的 finite-SF prefix 附近由严格正的
紧支撑光滑扰动精确隐身；这只是 `OBSTRUCTION`，不是 probability counterexample。

可单列为 genuine probability-level lemma：full-SF 且
`kappa_(2m)>=0`（所有 `m>=2`）则 Gaussian。因为角平均系数
`A_(2m)=3 binom(2m,m)/6^m>0`，Jensen 强制所有高阶偶累积量为零，继而
`M(t)M(-t)=exp(t^2)`，Cramer decomposition 闭合。square-exponential
infinitely divisible full-SF law 是其推论。

### 68.4 R139 判决

* `PROVED`：R138 零点接口的严格量词；非配对壳的 subsequential lower bound；
  非对称 square-exponential law 的 odd-cumulant 无限变号；angular `H^1`
  cross-charge upper majorization；有限 Bochner 首敏感阶；even-cumulant
  cone Gaussian rigidity；uniform compactness interface；compatible genuine
  backward-tower rigidity。
* `OBSTRUCTION`：同一 `Q_r` 内跨 degree cancellation；有限 Bochner 测试族
  的局部隐身；从 real-axis upper energy 推不出 first-shell lower gap。
* `CONDITIONAL`：scalar `RK=1` 到 genuine full-SF/all-row；由 ordinary MGF/
  Bargmann 到 spatial `P_3 K_sp`；formal witness 到 genuine law。
* `OPEN`：无限非配对 MGF zero divisor 的 genuine full-SF law是否存在；以及
  incompatible moving-top positive backward tower。

下一轮唯一任务：寻找 first-shell mass 到 real-axis angular/Bochner energy 的
反向 coercive lower bound；若失败，继续精确化 cancellation obstruction，不能
宣称已构造 non-Gaussian full-SF law。

## 69. R140：gap/separation shell-to-energy audit

网页端 R140 已按提交 `5569c32c41e2ff078cb4d7e7d25479e170d7d028` 读取 R139
基线并完成长篇推导。本机新增 `r140_gap_separation_shell_audit/`；网页端
“(d+3)/2 首次敏感”经审计改写为“第一处 Hankel-leading coefficient 被 hidden
degree 改变”，而任意非退化 `3x3` triangle 的 direct odd phase 可在 `h^(2d)`
阶出现。even-cumulant cone 仍要求 `kappa_(2m)>=0` 对所有 `m>=2`。

在第一非配对壳 reciprocal angular frequencies 有显式分离 `sigma>0`、下一壳
有 `Gamma>1` 径向间隔、且 outer signed divisor 有
`B_3=sum|delta|(R/|zeta|)^3` 定量界时，shifted Cesàro block + finite monomial
Gram 给出一个明确的 shell-to-energy lower bound。利用 odd tail 从 `M+2`
开始的步长 2，尾项满足
`||tail||_2<=4B*tau^(M+5/2)/((M+2)*sqrt(2M+5))`（`B=L+B_3`、
`tau<=1/2`），故网页端的常数 8 可直接核验：
`tau^2<=a*sqrt(h_M)*(M+2)*sqrt(2M+5)/(8*(L+B_3))`。由此
`E(T)>=Psi>0`，而 full-SF Fisher 只给 `E(T)<=int_0^T exp(t^2/2)dt`；若
`Psi` 超过该上界，则该明确 regular-shell geometry 与 genuine full-SF 不相容。
该结论是 `PROVED under explicit analytic hypotheses`，不是仅依赖
`(R_Delta,V_Delta)` 的 universal gap。

R140 同时给出两类 genuine probability/Bochner obstruction：Bernoulli 非对称
MGF 加 Gaussian/rescale 使 angular separation 塌缩但 `R_Delta,V_Delta` 固定；
以及 `B_p-cB_p'` 加 Gaussian/rescale 使 radial gap `Gamma=1/c` 塌缩但 angular
separation 固定。两族均不是 full-SF counterexample，却说明两种几何控制都
不可省。R140 的 full-SF `3x3` triangle majorization
`3<|phi(rho t cos(theta))|^2><=1+2e^(-t^2/2)` 保留为 `PROVED`，但它只
控制 modulus/even sector，仍没有 zero-shell phase 的 global lower gap。

因此：`PROVED` 为带 gap/separation/tail 假设的条件性 shell-to-energy theorem、
full-SF triangle majorization、此前 R139/R138 的严格接口和 compatible tower
rigidity；`OBSTRUCTION` 为 angular/radial coalescence、同一 `Q_r` 跨 degree
cancellation 与 finite-test invisibility；`CONDITIONAL` 仍是 scalar `RK=1`
到 full-SF/all-row 以及 ordinary MGF/Bargmann 到 spatial `P_3 K_sp`；`OPEN`
仍是 full-SF 是否自动排除 shell coalescence，以及 `R_Delta->infty` characteristic
scale 上是否存在 uniform phase gap。下一轮唯一任务：**R141 — Renormalized
Zero-Shell Bochner Phase Compactness**。
