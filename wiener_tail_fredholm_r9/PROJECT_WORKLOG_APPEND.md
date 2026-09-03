# 2026-09-04 — Wiener tail/Fredholm R9

- 建立独立分支 `chi2-wiener-tail-fredholm-r9-2026-09-04`，未启动远端任务、优化、SDP、参数网格、resultant 或数值零点搜索。
- 完成 Hermite `b_n` 与普通 Taylor `r_n=b_n/sqrt(n!)` 的精确换元回放，并明确 `B_NORMALIZATION_NOT_TOEPLITZ` 的 factorial shift。
- 完成普通 Wiener 空间半径损失尾界、中心二项式 benchmark、fixed-band Stage7 比值、简单/重零点除法范围条件和 Gaussian `D_R` 回放。
- 本地验证：逐文件 `py_compile` 通过，`pytest` 为 4 passed，输出 `R9_WIENER_TAIL_FREDHOLM_AUDIT_COMPLETED`。
- 可信结果：普通 Wiener 半径损失机制与有限范围回放通过；真实 Stage7 kernel 的普通系数公式及 `m`-uniform symbol limit 仍未导入，故不宣称 Fredholm 主算子或 Gaussian rigidity。
- 决策：`NORMALIZATION_REPAIRED_BUT_SYMBOL_LIMIT_NOT_UNIFORM`，等待 ChatGPT 复审。

