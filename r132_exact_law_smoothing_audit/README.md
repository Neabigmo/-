# R132 — exact-law OU smoothing and log-density bridge audit

日期：2026-09-08

网页端 R132 对 R131 的主要条件性缺口作了真正的分层处理：对 genuine、
centered、variance-one law，若实际满足所有 exact rows

`E Q^r = 2^r r!`, `r=0,1,2,...`,

则 Carleman determinacy 给出 `Q ~ chi^2_2`，进而给出 uniform square-exponential
tail。利用一次固定 `P_(1/2)` 预平滑和 centered/variance-one 消掉 Hermite
0、1、2 阶，得到

`||P_t h - 1||_2 < 8 t^(3/2)`, `0<t<=1/2`.

更一般地，Gaussian hypercontractivity 给出

`||P_t h - 1||_p <= 8 (p-1)^(3/2) t^(3/2)`,

当 `p>=2` 且 `t<=1/(2(p-1))`。因此 genuine all-row depth-`N` tower 的
底层 `g_N=P_(q^N)h_N` 有

`||g_N-1||_2 <= 8 q^(3N/2)`,

并在 `m=floor(theta N)`、`theta<3 log(1/q)/(2 log 3)` 时获得 growing
Hermite-Gram/Jacobi Gaussian window。这一段现在是 `PROVED`，但适用范围是
genuine all-row exact class；只有 scalar `RK=1` 而未证明 all-row/full-`Q`
equivalence 的对象仍然不能直接套用。

## 新的 log-density 弱桥接

对 `g=P_t h` 且 `t<=1/64`，Mehler 正性和 `E X^2=1` 给出 uniform lower bound

`g(x) >= (3/4) exp(-3) exp(-x^2/63)`.

结合 `L^4` smoothing 得到 `||log g||_2 <= C_K t^(3/2)`；并且

`<log g, He_3/sqrt(6)> = t^(3/2)m_3(h)/sqrt(6) + O(t^3)`.

这是真正的 `positive backward cone -> log-density` 局部结果，但仍不是
`P_3 K != 0 -> fixed Jacobi defect` 的 separation theorem。固定 Jacobi level
只给出二次小缺陷：在 full exact class 中

`1 - beta_2(g)/2 = m_3(g)^2/2 = 3 a_3(g)^2`.

故 `P_3 K` 的 qualitative nonzero 不能从普通 fixed-degree coercivity 自动
放大成 uniform positive defect；缺口仍是 same-factor angular-to-Jacobi
amplification。

## 公式纠正

项目约定 `P_s psi_n=s^(n/2) psi_n` 时，直接对 Mehler kernel 配方并积分，得到
精确平方范数为

`int M_s(x,y)^2 d gamma(x)
 = (1-s^2)^(-1/2) exp(s y^2/(1+s))`.

此前本目录和网页正文之间的表述曾把 `(1+s)^(-1/2)` 误记为精确前因子；这是
配方时漏掉 `1-s` 的笔误。正确的 `(1-s^2)^(-1/2)` 正是 exact identity，
并且在 `s=1/2` 时给出算子范数因子 `(4/3)^(1/4)`。结合尾界中的
`exp(-1/6)`，仍有 `(4/3)^(1/4)exp(-1/6)<1`，所以 `||P_(1/2)h||_2<3`
和常数 `8` 不变。审计脚本现在直接核验这个 exact prefactor。

## 障碍

仅有 positivity、mean zero、variance one 和 individual `L^2` 并不给 uniform
fixed-time smoothing；稀有远端 Gaussian mixture 可使平滑后相对于 `gamma` 的
`L^2` 范数发散。因此 all-row exactness（经 Carleman 产生 uniform tail）是
R132 平滑定理的实质输入。

审计命令：

`F:\\anaconda3\\python.exe r132_exact_law_smoothing_audit\\audit_r132.py`

证据等级：OU smoothing、`L^p` 推广、log-density `L^2` 弱桥接和 fixed-level
Jacobi/log 关系均记为 `PROVED`（以标准 Gaussian hypercontractivity 和
Mehler 计算为分析输入）；scalar `RK=1` 接口、same-factor logarithmic-degree
separation、以及最终 exact-zero-set rigidity 仍为 `OPEN/CONDITIONAL`。
