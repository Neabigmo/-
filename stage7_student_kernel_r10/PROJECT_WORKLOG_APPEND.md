# 2026-09-04 — Stage7 Student kernel R10

- 建立独立分支 `chi2-stage7-student-kernel-r10-2026-09-04`，未启动远端计算、优化、SDP、参数网格、resultant 或数值零点搜索。
- 修正 Fock 归一化下 Gaussian：`R=1`、`D_R=1`。
- 完成 Student/Beta 偶矩、直接小次数角积分、fixed-band 首阶修正、中心二项式/归一化核 benchmark、Wiener 尾项和 Gaussian `D_R` 回放。
- 可信结论：有限核与半径损失回放通过；真实 Stage7 `A_ijk` 普通系数公式及 band-uniform operator theorem 仍需原始内核输入。
- 决策：`STUDENT_KERNEL_CERTIFIED_OPERATOR_GAP_REMAINS`。

