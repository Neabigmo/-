# 数学定理证明：理论记录镜像

这是 `8.22统计` 理论研究工作区的 GitHub 镜像，供网页端研究会话读取和审阅。仓库保留完整的历史推导、审计脚本和工作日志；结论必须以文档中的证据等级为准，不能把 relaxed Hankel 截断结果直接当作 genuine probability law。

## 网页端首选读取顺序

1. `THEORY_ROUTE_FRAMEWORK.md`：整体路线、已关闭方向、当前 OPEN 命题和各轮结论。
2. `PROJECT_WORKLOG_APPEND.md`：按轮次记录研究进度、纠错和审计状态。
3. `truncated_hamburger_cubic_radius_r125/README.md`：R125 的有限行半径接口。
4. `singular_ghost_extremum_r126/README.md`：M=3 singular non-flat ghost。
5. `m4_cubic_radius_flat_extremum_r127/README.md`：M=4 flat extremizer。
6. `singular_extension_compatibility_r128/README.md`：纠正后的 M=5 singular ghost 延拓。
7. `r129_m6_exact_extension_audit/README.md`：M=6 exact row、H6 compatibility 和全局严格 relaxed bound。
8. `r130_m6_gap_audit/README.md`：M=6 的显式有理区间 gap 证书。
9. `r130_web_gap_audit/README.md`：网页端强 gap 的本机补证与常数审计。
10. `r131_normalized_defect_audit/README.md`：genuine (L^2) 归一化缺陷接口与 M=7 exact algebra。
11. `r132_exact_law_smoothing_audit/README.md`：all-row exact law 的统一 OU 平滑、log-density 弱桥接与障碍审计。
12. `r133_first_odd_jacobi_audit/README.md`：首个奇 Hermite/Jacobi 精确包、有限行盲区与 R134 全阶 cascade 任务。

## 分支体系

- `main`：当前完整研究记录的稳定镜像；网页端默认读取此分支。
- `theory/r129-active`：当前理论推进工作分支，与 `main` 同步，后续 R129/R130 结果优先落在这里，再合并回 `main`。
- `archive/r125-baseline`：R125 截止点的可复核快照。
- `archive/r126-ghost`：R126 M=3 ghost 结果快照。
- `archive/r127-flat`：R127 M=4 flat extremizer 快照。
- `archive/r128-corrected`：R128 纠正归一化后的 M=5 延拓快照。

分支只用于区分稳定主线、当前推进和历史快照，不代表所有快照都含有后续结论。计算脚本和数值输出必须附带输入/输出契约及审计 marker，不能直接写入 `main`。

## 当前状态（2026-09-08）

- R126：`\widehat\Gamma_3=\Gamma_3=\sqrt 2`，但 relaxed maximizer 是 genuine class 外的 singular ghost，genuine supremum 不取得。
- R127：`\widehat\Gamma_4=\Gamma_4=c_4`，等号点为 flat genuine extremizer。
- R128：正确归一化下 `\widehat\Gamma_5=\widehat\Gamma_4=c_4` 的 relaxed singular non-flat ghost 已通过本机审计；`\Gamma_5` 是否等于该值仍为 OPEN。
- R129：R6 原始展开、R2–R5 消元及 H5→H6 kernel compatibility 已通过精确审计；R128 ghost 无 PSD H6 延拓。结合 R125 紧性与 R127 等号分类，已解析推出有限层严格界 `\widehat\Gamma_6<c_4`，并因此有 `\Gamma_6\le\widehat\Gamma_6<c_4`。
- R130：本机初证先给出 `\widehat\Gamma_6\le1.0535`；随后网页端给出更强的 endpoint-neighborhood 证书，经本机 `r130_web_gap_audit` 补齐常数后解析通过：`c_4-\widehat\Gamma_6>25/28196\approx8.8665\times10^{-4}`，故 `\widehat\Gamma_6<1.052702`。这仍是 relaxed finite-level 上界，不是 `\widehat\Gamma_6` 的精确值，也没有关闭 genuine 或正性/反向 OU 主线。
- R131：对 genuine `d\mu=g d\gamma`、`g\in L^2(\gamma)`，`\varepsilon=\|g-1\|_2` 时，次数 `m` 的 Hermite Gram 满足 `\|G_m-I\|_{op}\le\varepsilon3^m`（以 Gaussian hypercontractivity 为标准输入），从而得到 normalized Jacobi coercivity；M=7 的最高奇矩不可见和 flat kernel 的 odd-freedom 计数也已精确审计。其 fixed-shift 传播必须同时要求 `\varepsilon3^{m+j}<1`。
- R132：网页端证明：若 genuine centered/variance-one law 实际满足所有 exact rows `E Q^r=2^r r!`，则 Carleman 给出 `Q\sim\chi^2_2`，并有显式 `\|P_t h-1\|_2<8t^{3/2}`（`t\le1/2`）及相应 `L^p` 估计；进一步得到 `\|\log(P_t h)\|_2=O(t^{3/2})` 和 `P_3\log(P_t h)` 的 cubic 级弱桥接。普通 positivity/normalization/individual `L^2` 不足以给 uniform smoothing；只有 scalar `RK=1` 时仍不能自动套用 all-row 结论。
- R133：在 genuine analytic full same-factor identity 下，若首个非零奇阶为 `d=2s+1`，则强制低于 `2d` 的偶 cumulants 消失，并得到精确 Jacobi 缺陷 `1-\beta_{s+1}/(s+1)=\binom{2s+1}{s}a_d^2`。本机已补上首个奇阶推理所需的假设边界、组合恒等式和 finite-row blindness genuine obstruction；首个 packet 在 R131 subcritical window 内不能产生 fixed gap。
- 当前下一步：R134 **Critical-Layer Same-Factor Jacobi Cascade**，从 same-factor angular identity 推导全阶 cumulative normalized curvature 的 energy/telescoping 关系，或严格证明其 obstruction；不得把猜测的 `9^m` 放大当作结论。最终 separation 与 exact-zero rigidity 仍 OPEN。

## 证据等级

文档使用 `PROVED`、`ANALYTICALLY PROVED`、`CONDITIONAL`、`FORMAL`、`OBSTRUCTION`、`OPEN` 区分结论强度。`SDP`、数值扫描、optimizer、形式 jet 或 operator-only 样例不自动构成 genuine 概率律证明。
