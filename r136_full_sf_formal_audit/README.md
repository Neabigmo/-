# R136 — full-SF formal completion audit

日期：2026-09-08

本目录审计网页端 R136 的 formal coefficient algebra：

* `theta -> theta+pi` 导致所有 odd SF coefficient equations 恒为零；
* even equations 的最新 even cumulant 系数
  `A_(2N)=<p_(2N)>=3 binom(2N,N)/6^N` 严格为正；
* hidden odd degree `d` 的 first future band
  `2d<=M<4d` 只有 current even pivot 与 odd-pair quadratic source；
* sparse odd input 只产生 `2kd` 支撑的 formal even completion；
* first negative pivot、后续 mixed coefficient 的符号不定，以及不产生
  coefficientwise positive cascade。

该审计不声称 formal completion 是 genuine probability law。Bochner positive
definiteness、所有 Hankel/Jacobi 正性、解析增长和单个 all-degree density
realization 仍是 OPEN。`RK=1` 到 full-SF 的接口继续是 CONDITIONAL。

审计命令：

`F:\\anaconda3\\python.exe r136_full_sf_formal_audit\\audit_r136.py`
