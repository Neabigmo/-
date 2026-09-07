# R107 — 三点 Bochner 的 genuine obstruction 与四点相乘相容性

日期：2026-09-07

本轮承接 `bochner_phase_lift_rigidity_r106`，直接审查
`P_3K!=0` 是否必然击穿 R106 的 phase-free 三点不等式。

## 1. 结论

### PROVED — 三点 breakdown 没有独立增益

R106 的

`3 < psi(sqrt(2/3)y cos(theta))>_theta <= 1+2 exp(-y^2/2)`

是每一个 genuine full-exact probability law 的必要条件。因此在 genuine
full-exact 类内，“`P_3K!=0` 则三点不等式 breakdown”与排除非对称 exact law
处于同一逻辑层级；若非对称 exact law存在，它必满足不等式，不能由必要条件
本身推出矛盾。

### PROVED / ANALYTICALLY PROVED — genuine same-`psi` obstruction

取 `p(1-p)=1/6`，令 `a=sqrt(3)`、`B_1,B_2` 为参数 `p` 的独立 Bernoulli，
并定义

`X_sym=a(B_1-B_2)`,

`X_asym=a(B_1+B_2-2p)`。

两者都是 genuine centered variance-one laws，并且

`m_4=3`, `m_3(X_sym)=0`, `m_3(X_asym)=1`, `kappa_6=-6`。

若 `m(s)=1-p+p exp(s)`，它们的 MGF 是

`M_sym(r)=m(ar)m(-ar)`,

`M_asym(r)=exp(-2par)m(ar)^2`。

因此 `M_sym(r)M_sym(-r)=M_asym(r)M_asym(-r)`，两者拥有相同的差分律、
相同的 `psi=|phi|^2` 与相同的所有 phase-free 三点数据，但对称性和 `P_3K`
不同。

再作有限强度的 OU/Gaussian smoothing

`X_(lambda)=sqrt(lambda)X+sqrt(1-lambda)G`, `0<lambda<1`,

则两者仍同 `psi`、仍 `m_4=3`，而非对称者
`m_3=lambda^(3/2)`、`kappa_6=-6lambda^3`，所以 `P_3K!=0`。

对充分小但正的 `lambda`，三点 Difference–Bochner 不等式对所有实 `y` 成立。
证明分三段：

1. `lambda=0` 时，令 `x=y^2/3`，左侧为
   `3 exp(-x) I_0(x)`，并用
   `I_0(x)=E exp(x cos(theta))` 与离散律
   `P(V=1)=1/3, P(V=-1/2)=2/3` 的逐项矩比较，得
   `3I_0(x)<exp(x)+2exp(-x/2)` 对 `x>0`；
2. 在 `y=0` 附近，平滑 obstruction 的 slack 为
   `((1-lambda^3)/216)y^6+O(y^8)>0`；
3. 中间紧区间用连续性，远端用
   `|psi_lambda(t)|<=exp(-(1-lambda)t^2)` 的高斯尾界。

第一步的矩比较是严格的：`cos(theta)` 与 `V` 的 0、1、2 阶矩相同；奇数
阶 `n>=3` 中 `V` 的矩为 `(1-2^(1-n))/3>0`，而偶数阶 `n>=3` 中
`E V^n=(1+2^(1-n))/3>1/3`，同时
`E cos(theta)^n=binom(n,n/2)/2^n<=5/16<1/3`。

这是一条 genuine characteristic/difference-law obstruction：三点数据即使
已经满足 `m_4=3`，也不能识别 symmetry 或 nonzero odd charge。它不是
full-exact counterexample，因为 same-factor exactness 的 degree-six fingerprint
要求 `kappa_6=-3 m_3^2`，而该 obstruction 给出
`-6lambda^3 != -3lambda^3`。

## 2. 最小的新 Bochner 对象

三点平均已经被上述 obstruction 钉死。最小自然升级是 multiplicative
4-point Gram。取

`x=a_1(theta)y`, `z=-a_2(theta)y`, `U=exp(ixX)`, `V=exp(izX)`，

并令 `u=phi(x)`, `v=phi(z)`, `w=phi(x+z)`, `c=phi(x-z)`。对
`U-u,V-v,UV-w` 的协方差矩阵：

`Gamma_4 = [[1-|u|^2, c-u*conj(v), conj(v)-u*conj(w)],
            [conj(c)-conj(u)*v, 1-|v|^2, conj(u)-v*conj(w)],
            [v-conj(u)*w, u-conj(v)*w, 1-|w|^2]] >= 0`.

若上方 `2x2` block `C` 正定，令

`q=(conj(v)-u*conj(w), conj(u)-v*conj(w))^T`,

则等价 Schur complement 为

`q^* C^(-1) q <= 1-|w|^2`。

这里的 `w=phi((a_1-a_2)y)` 是三点 triangle 未看到的 companion frequency。
4-point 足够完成 rigidity 仍然 **OPEN**；本轮只证明它是最小合理的新增
phase-coherence 对象。

## 3. 证据边界与 R108

- **PROVED / LOCAL-AUDITED**：Bernoulli 卷积 pair 的概率、矩、MGF homometry、
  smoothing cumulant scaling、三点 `y^6` slack 系数及四点 Schur 结构。
- **ANALYTICALLY PROVED**：充分小 `lambda` 时三点不等式对所有 `y` 的连续性+
  尾界论证；本机不以数值扫描替代它。
- **NOT A COUNTEREXAMPLE**：该 pair 被 degree-six exactness 排除。
- **OPEN**：4-point multiplicative Gram 与 full exactness 是否强制 phase trivial；
  asymmetric exact-law exclusion；以及最终 positive backward-tower rigidity。

R108 最小命题：把 `Gamma_4` 的 Schur complement 与 same-factor exact identity
做 angular averaging，寻找一个真正依赖 phase、不能塌缩成 `psi` 的 signed
functional `Q_4[phi]`；若仍塌缩，再进入 5-point，而不是回到三点层。

禁止用 numerical sweep、SDP、optimizer 或 remote computation。
