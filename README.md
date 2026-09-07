# 数学定理证明：理论记录镜像

这是 `8.22统计` 理论研究工作区的 GitHub 镜像，供网页端研究会话读取和审阅。仓库保留完整的历史推导、审计脚本和工作日志；结论必须以文档中的证据等级为准，不能把 relaxed Hankel 截断结果直接当作 genuine probability law。

## 网页端首选读取顺序

1. `THEORY_ROUTE_FRAMEWORK.md`：整体路线、已关闭方向、当前 OPEN 命题和各轮结论。
2. `PROJECT_WORKLOG_APPEND.md`：按轮次记录研究进度、纠错和审计状态。
3. `truncated_hamburger_cubic_radius_r125/README.md`：R125 的有限行半径接口。
4. `singular_ghost_extremum_r126/README.md`：M=3 singular non-flat ghost。
5. `m4_cubic_radius_flat_extremum_r127/README.md`：M=4 flat extremizer。
6. `singular_extension_compatibility_r128/README.md`：纠正后的 M=5 singular ghost 延拓。

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
- 当前下一步：独立推进 R129 的 M=6 exact row、kernel compatibility、Schur defect 和 recurrence obstruction，并回到全局的 positive/backward-OU 主线。

## 证据等级

文档使用 `PROVED`、`ANALYTICALLY PROVED`、`CONDITIONAL`、`FORMAL`、`OBSTRUCTION`、`OPEN` 区分结论强度。`SDP`、数值扫描、optimizer、形式 jet 或 operator-only 样例不自动构成 genuine 概率律证明。
