# R130 网页端显式 gap 复核

日期：2026-09-08

本目录复核网页端 R130 给出的更强候选结论

`c_4-GammaHat_6 > 25/28196`。

复核目标不是重新做浮点扫描，而是检查网页证明中省略的常数链：两个 exact
factorization、`delta(u)>700`、参数盒、`d_*` 约束、R6 的 `y_12<453000`
以及最后的 H6 Schur 反证。所有数值不等式均以有理数端点和符号恒等式核验。

截至本轮，网页正文给出的核心 identity 和全部关键常数链均已通过
`audit_r130_web.py` 的本机精确复核，因此在 R125/R127 已审计接口上，
`25/28196` 可记为 `ANALYTICALLY PROVED`。

需要特别修正网页正文的一处表述：`C(u)<-33` 不能仅由 polynomial part `<252`
与第二项 `<-280` 得到；本审计将 polynomial part 收紧到 `<247`，再得到
`C<-33`，从而严谨推出 `delta>700`。

网页端 R130 已完成，本目录是其本机复核层。证书仍然是 relaxed finite-level
结果：它没有给出 `GammaHat_6` 的精确值、genuine `Gamma_6` 的精确值，
也没有关闭全阶 `Gamma_M->0` 或 positive/backward-OU rigidity。

本机补齐的关键修正是：网页原文用 `C` 的 polynomial part `<252` 直接声称
`C<-33`，数值上不构成该结论；这里证明更强的 polynomial part `<247`，再与
第二项 `<-280` 得到 `C<-33`，从而严谨推出 `delta(u)>700`。

审计命令：

`F:\\anaconda3\\python.exe r130_web_gap_audit\\audit_r130_web.py`
