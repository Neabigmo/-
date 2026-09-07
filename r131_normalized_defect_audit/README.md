# R131 — normalized kernel defect and top-odd interface audit

日期：2026-09-08

网页端 R131 给出了两类结果，必须分层记录。

## 已确认的 genuine-density 结果

若 `d mu=g d gamma`、`g>=0`、`g in L^2(gamma)`，令
`epsilon=||g-1||_2`，则对次数不超过 `m` 的 Gaussian polynomial，
超收缩性给出

`(1-epsilon*3^m)||p||_gamma^2 <= ||p||_mu^2
 <= (1+epsilon*3^m)||p||_gamma^2`.

因此在 `epsilon*3^m<1` 时，normalized Hermite Gram 是 coercive 的，monic
Jacobi norms 满足

`(1-delta_k)k! <= h_k^mu <= (1+delta_k)k!`,
`delta_k=epsilon*3^k`,

并得到 `beta_k/k` 的相应上下界。这是 genuine positive `L^2` 密度上的
PROVED（以标准 Gaussian hypercontractivity 为输入）结果，不能直接套到
relaxed finite Hankel ghost。

网页端给出的 exact algebra 也已纳入本审计：下一 exact row 的最高奇矩
`y_(2m+1)` 不出现；flat rank-`r` kernel 向下一层延拓时，有 `m-r` 条
不含新 top odd moment 的 frozen compatibility 方程，最后一条至多由该
一个 odd moment 调整；Hermite Gram determinant 与 Jacobi recurrence 的字典
也通过符号恒等式复核。

## 必须保留的条件与 OPEN

网页端还使用了
`||P_(rho^N)h_N-1||_2=O(rho^(3N/2))` 的 uniform 断言来推出 growing
Jacobi window。当前本机已有记录（尤其 R57）直接给出的是
`m_3^2<=2 lambda(2-lambda)`，并不足以自动推出该整段 `L^2` 估计。
故该 backward-OU window 记为 CONDITIONAL，除非补出统一的 `L^2` 输入。

`P_3 K != 0` 到 normalized recurrence defect 的 same-factor separation，
以及从该 separation 到 positive backward-OU exact-zero-set rigidity，仍是
OPEN。R131 的真实新桥是“genuine L2 smallness -> logarithmic-degree
coercivity window”，不是完整的 charge-to-cone 定理。

审计命令：

`F:\\anaconda3\\python.exe r131_normalized_defect_audit\\audit_r131.py`
