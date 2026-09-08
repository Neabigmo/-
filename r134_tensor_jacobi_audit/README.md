# R134 — tensor–Jacobi energy audit

日期：2026-09-08

本目录审计网页端 R134 的有限代数部分，重点是 `T_n` 的 multinomial 指数生成函数、
`D_m=\prod_{n\le m}q_n` 与 Jacobi ratio 的字典、angular pure-block 系数 `lambda_n`、
Bregman 行列式能量的标量上下界、`81/4` 临界层常数、`R134-C` 的二次残差常数，
以及自然 `log T_n` 泛函只有多项式局部权重的组合事实。

审计只确认公式和常数，不把网页端的分析假设自动升级：`R134-A/B/C` 的完整结论
仍需要 genuine probability law、full same-factor identity、相应的 `L^2`/hypercontractive
Gram 控制；仅有 scalar `RK=1` 或 relaxed Hankel ghost 不能直接套用。

## 证据等级

* **PROVED / locally audited**：上述有限代数恒等式、determinant dictionary、pure angular
  coefficient、Bregman 常数和 residual 上界中的常数代数。
* **CONDITIONAL**：从 scalar `RK=1` 到 full-SF/all-row probability class 的迁移，以及
  网页端对 tensor leakage `rho_n` 的解析范数估计。
* **OPEN**：critical layer 中 genuine same-factor realizability 是否阻止 `rho_n` 吸收
  全部 angular charge；这正是 R135 的唯一任务。

审计命令：`F:\\anaconda3\\python.exe r134_tensor_jacobi_audit\\audit_r134.py`
