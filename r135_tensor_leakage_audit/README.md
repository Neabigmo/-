# R135 — critical tensor-leakage audit

日期：2026-09-08

本目录审计网页端 R135 的有限代数与可复核构造。重点是：

* lower-total-degree residual 的正投影公式；
* first lower layer 的条件方差表达式；
* finite-horizon positive density `g=1+epsilon f` 的 moment-selector 构造接口；
* 隐藏奇阶 `d=2n-1` 时 `rho/(rho+sigma)` 的精确分解与 critical-layer 标度；
* cubic tangent 下泄漏 Hessian 的 `n(n-1)/4` 常数。

审计只确认有限代数、Hermite/tensor coefficient 和常数；不把 finite-SF
prefix 自动升级为 genuine all-degree SF，也不把该构造称为原命题反例。
`RK=1` 到 full-SF/all-row 的迁移继续标为 CONDITIONAL。

审计命令：

`F:\\anaconda3\\python.exe r135_tensor_leakage_audit\\audit_r135.py`

## 证据等级

* **PROVED / locally audited**：投影二次型、`n-1` 层条件方差、隐藏奇阶
  finite-SF 模型的精确 `rho/sigma` 分解、critical-layer 上界和 cubic Hessian。
* **CONDITIONAL**：由 scalar `RK=1` 进入 genuine full-SF，以及把 finite prefix
  延拓到全阶概率实现。
* **OBSTRUCTION**：任何只依赖当前有限 angular charge 的
  `rho_n <= eta_n A_{<=n}` 和固定比例 anti-shielding 都不成立。
* **OPEN**：near-total tensor shielding 是否能够具有 genuine all-degree
  one-body SF completion。
