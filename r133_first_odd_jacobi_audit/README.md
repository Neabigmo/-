# R133 — first-odd Jacobi packet, finite-row blindness, and the remaining cascade

日期：2026-09-08

本轮网页端提出了一个有价值的局部结构：在 genuine full same-factor exact
identity 下，第一个非零奇 Hermite/cumulant 阶数会在一个明确的 Jacobi
二阶块中产生精确曲率缺陷。本记录同时修正其适用条件，并把一个容易误读的
有限行结论明确标为 obstruction，而不是原主命题的反例。

## 1. 记号与 exact identity 的逻辑边界

令 `g` 是 centered、variance-one 的 genuine density，且 `g-1∈L²(γ)`，使
normalized Bargmann transform

`B_g(z)=E[g(X) exp(zX-z²/2)]`

在原点邻域解析。记

`C_g(z)=log B_g(z)=sum_{n>=3} κ_n z^n/n!`,

`a_n=E_g[psi_n(X)]`，因此在第一个非高斯阶之前
`a_n=κ_n/sqrt(n!)`。这里的空间量

`K_sp(x)=log g(x)`, `ell_3=<K_sp,psi_3>`

不能与 Bargmann 量 `C_g` 混同；一般 `C_g=log B(e^{K_sp})`，而不是
`B(K_sp)`。只有在项目约定把 `P_3K_sp` 识别为这个内积时，才可把
`P_3K_sp≠0` 写成 `ell_3≠0`。

真正使用的 same-factor 假设是

`(SF)  < exp(sum_{j=1}^3 C_g(z r_j(theta))) >_theta = 1`,

其中 `r_j(theta)=sqrt(2/3) cos(theta+2π(j-1)/3)`。这条式只对 genuine
full exact class（或已经证明其等价形式）可用；单独的 scalar `RK(g)=1`
以及 relaxed Hankel ghost 都不能自动提供它。对未保证 `L²`/解析性的顶层，
以下 theorem 只能应用于 genuine smoothed level `g=P_t h`（`t>0`）或另行
加入相应正则性假设。

## 2. Theorem R133-A — exact first-odd Jacobi packet

设 `d=2s+1>=3` 是第一个非零奇阶，亦即

`κ_3=...=κ_{d-2}=0`, `κ_d≠0`,

并假设 `g` 满足 (SF)。则 (SF) 的偶阶系数递推先强制

`κ_4=κ_6=...=κ_{2d-2}=0`。

因此在次数 `<=d+1` 内，除了 `κ_d` 以外的 normalized Hermite 非高斯
系数都为零；这一步是 theorem 的必要假设链，不能仅由“第一个奇系数是 d”
一句话替代。令 `k=s+1`，则

`alpha_0=...=alpha_{s-1}=0`, `beta_j=j (1<=j<=s)`,

`alpha_s=κ_d/s!=sqrt(d!)/s! * a_d`,

并且

`1-beta_{s+1}/(s+1)
 = alpha_s²/(s+1)
 = binom(2s+1,s) a_{2s+1}²`.          (R133-A)

用 monic Jacobi determinant `D_j` 表示同一结论为

`D_{s+1}D_{s-1}/D_s² - 1
 = -binom(2s+1,s) a_{2s+1}²`.          (R133-A')

证据等级：在 genuine、解析、centered/variance-one、(SF) 假设下
`PROVED`；对项目原始 scalar `RK=1` 目标仍为 `CONDITIONAL`。

### 证明链

写 `p_n(theta)=sum_j r_j(theta)^n`。偶数 `n` 有
`<p_n>_theta>0`，奇数的线性角平均为零。比较 (SF) 的 `z^n` 系数：在
`4<=n<2d` 的偶阶上，若较低偶阶已经归零，则任何含奇 cumulant 的非线性项
至少含两个奇因子，阶数至少 `2d`；含一个奇因子时总阶为奇数，不能出现在
偶阶方程中。所以归纳得到 `κ_{2r}=0`，`2<=r<d`。由于两个 `κ_d` 因子
要到 `2d` 才出现，`<=d+1` 的 moment/Hermite block 只有一个非高斯坐标
`a_d=κ_d/sqrt(d!)`。

Hermite product formula 随即说明 `G_{s+1}` 的唯一非单位项是

`G_{s,s+1}=G_{s+1,s}=sqrt(binomial(d,s)) a_d`。

故其末端 `2×2` 块的 determinant 是
`1-binomial(d,s)a_d²`。另一方面，`P_s=He_s` 时

`alpha_s=E[X He_s(X)^2]/s!=κ_d/s!`,

且 `beta_{s+1}=s+1-alpha_s²`。使用
`d!/(s!²(s+1))=binomial(d,s)`，得到 (R133-A)；再用
`h_j/j!=D_j/D_{j-1}` 与
`beta_j/j=D_jD_{j-2}/D_{j-1}²` 得 (R133-A')。

## 3. 对原始 `P_3K` 问题的实际含义

若项目定义下 `P_3K_sp` 的 charge 就是 `ell_3`，且 `ell_3≠0`，则 `g` 不
可能为偶函数，故存在某个第一个奇阶 `d=2s+1`。R133-A 给出一个定性的
结论：某个 `k=(d+1)/2` 必有 `beta_k<k`，其精确缺陷为

`Delta_k=binom(2k-1,k-1) a_{2k-1}²>0`。

这不是固定正下界，因为 `d` 可以向高阶漂移且 `a_d` 可以很小；也不能把
`ell_3` 直接替换成 `a_3`。因此它是从 same-factor zero set 到 Jacobi
曲率的第一个 exact local bridge，但尚未成为 rigidity separation theorem。

## 4. 严格 no-go：首个 odd packet 不能关闭 R131 窗口

令 `epsilon=||g-1||_2`。Parseval 给 `|a_d|<=epsilon`，且

`Delta_k < 4^k epsilon²`, `k=(d+1)/2`。

若 `k<=log_3(1/epsilon)`，则

`Delta_k <= epsilon^(2-log_3 4) -> 0`,

因为 `4<9` 即 `log_3 4<2`。所以第一个奇 packet 在 R131 的 subcritical
normalized Gram window 内不能制造固定量缺陷。要完成主命题，必须控制更高阶
的 same-factor cascade，不能只追踪首个非零奇系数。

## 5. Proposition R133-B — fixed finite-row log-charge blindness

对任意固定 `m>=2` 和 `eta>0`，存在 smooth、strictly positive、centered、
variance-one genuine density `g=1+lambda f`，满足

`0<||g-1||_2<eta`, `E_g[X^r]=E_gamma[X^r] (0<=r<=2m)`,

但 `ell_3=<log g,psi_3>≠0`。构造如下：取非零
`f∈C_c^∞((2,3))`，满足
`∫x^r f dγ=0`，`0<=r<=2m`。这类函数存在，因为有限个 moment
约束在无限维测试函数空间中只给出有限余维。由于 `psi_3>0` 在 `(2,3)` 上，

`Q_f=∫f² psi_3 dγ>0`。

当 `|lambda|` 足够小时，`g>0` 且

`ell_3(lambda)= -lambda² Q_f/2 + R_lambda`,

`|R_lambda| <= (2/3)|lambda|³∫|f|³|psi_3|dγ`，

所以 `ell_3<0`。前 `2m` 个 moments 仍精确高斯，故前 `m` 个 Jacobi
系数完全是 `beta_j=j`，但 log charge 已非零。

这只是对“有限行信息足以推出 `P_3K=0`”的 genuine obstruction；它不满足
全阶 (SF)，因此不是原始 exact-zero-set 命题的反例。它说明即使把 R132 的
`O(log(1/epsilon))` growing window 做成 unconditional，也仍必须使用
all-degree same-factor coherence。

## 6. 证据分层与下一轮

| 条目 | 等级 | 含义 |
|---|---|---|
| R133-A first-odd packet | `PROVED` / `CONDITIONAL` | genuine analytic + (SF) 下已闭合；scalar `RK=1` 接口仍缺 |
| R133-A1 qualitative nonzero charge ⇒ some defect | `PROVED` / `CONDITIONAL` | 只有非零，不给 fixed gap |
| R133-B finite-row blindness | `PROVED` | genuine 正密度 obstruction，不是 global counterexample |
| 首个 odd packet 在 R131 窗口内给 fixed separation | `NO-GO` | 精确指数估计排除 |
| Positive backward tower 的最终 exact-zero rigidity | `OPEN` | 仍需全阶 cascade |

唯一应继续推进的下一轮是 **R134 Critical-Layer Same-Factor Jacobi Cascade**：
从 (SF) 推导 cumulative normalized Jacobi curvature 的 telescoping/energy
identity，或者给出其严格 obstruction；目标是找出全阶累积量如何跨越首个 odd
packet 的 `4^k` 上界，而不是再次展开同一低阶系数。任何 `9^m` 放大都必须从
精确 identity 推出，不能作为猜测写入结论。

审计命令：

`F:\\anaconda3\\python.exe r133_first_odd_jacobi_audit\\audit_r133.py`

本目录 marker：

`R133_ANGULAR_EVEN_POSITIVITY_PASSED`

`R133_FIRST_ODD_COMBINATORIAL_IDENTITY_PASSED`

`R133_JACOBI_DETERMINANT_BLOCK_PASSED`

`R133_4K_SUBCRITICAL_NO_GO_PASSED`

`R133_FINITE_ROW_BLINDNESS_INTERFACE_PASSED`

`R133_AUDIT_COMPLETED`
