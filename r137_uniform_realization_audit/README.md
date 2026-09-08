# R137 — uniform genuine-realization breakdown audit

日期：2026-09-08

本目录记录网页端 R137 对 R136 sparse hidden-odd branch 的全阶审计。这里严格
区分三层对象：formal cumulants `c_m`，由 Bell 多项式产生的 formal
moments/Hankel matrices，以及 genuine probability law 的 Jacobi data；formal
SF 递归本身不保证后两层的正性。

## 1. 固定 sparse odd branch

固定奇数 `d=2s+1>=5`，令 `c_d=a`，其余 odd cumulants 为零，并令 even
coefficients 由 full-SF 的三角递归决定。因 `kappa_d=d!a`，首个 Jacobi packet
满足

`1-beta_(s+1)/(s+1) = d! * binom(d,s) * a^2`.

本机脚本直接从 `exp(z^2/2+a z^d)` 构造到阶 `2(s+1)` 的 formal moments，
并核验

`det H_(s+1)(a)=(prod_(j=0)^s j!) [1-d! binom(d,s)a^2]`

对 `d=5,7,9,11` 成立。因此任何 PSD Hankel jet 都必须满足
`|a| <= R_d := [d! binom(d,s)]^(-1/2)`。

## 2. 全阶 radius collapse

定义 `I_M^H(d)` 为 formal sparse branch 的 order-`M` Hankel matrix
`H_M(a)=[m_(i+j)(a)]_(i,j=0)^M` 的 PSD 可行集合；定义 `I_M^+(d)` 为存在
strictly positive centered variance-one density `g dgamma`、匹配 moments 至
`2M` 阶的 genuine 可行集合。则

`I_(M+1)^H subset I_M^H`，`I_M^+ subset I_M^H`，且 `I_M^H subset [-R_d,R_d]`
（`M>=s+1`）。

如果某个固定 `a!=0` 属于所有 `I_M^H`，Hamburger theorem 给出 representing
measure。formal SF 的每个系数等式随后给出其三变量 zero-sum mixture 的全部
polynomial moments 为 Gaussian；对 residual energy `Q` 得到

`E Q^r = 2^r r!`（`r=0,1,2,...`）。

Carleman determinacy 与既有 R132 bridge 产生 square-exponential tail。此时
`K_o(t)=(K(t)-K(-t))/2` 是实轴上的 odd analytic function；若 odd support
有限，它是 odd polynomial，而

`|K_o(t)| <= K_e(t) <= 2t^2 + (log 2 - 1/8)`。

故 centered 情形只能有 `K_o=0`，与 `kappa_d=d!a!=0` 矛盾。于是

`intersection_M I_M^H(d) = {0}`，

并由嵌套紧集得到 `rho_M(d):=max{|a|:a in I_M^H(d)} -> 0`。这是
fixed `d`、fixed nonzero `a` 的 construction-independent feasibility-radius
collapse；没有给出 first failing minor 的显式阶，也没有断言 `d_M->infty`
的 selector sequence 被排除。

## 3. genuine 与 cutoff-uniform 的量词

R136 的有限截断插值给出每个固定 `M` 的某个 `delta_M>0`，但不保证 uniform
下界。R137 的结论是

`0 < rho_M^+(d) <= rho_M(d) -> 0`。

故“每个 M 可实现”不能交换为“存在一个与 M 无关的非零幅度”。这不是某个
双函数插值构造的缺陷，而是由所有 Hankel 必要条件共同推出的半径结论。

另一方面，若 finite-jet densities 另有 `sup_M ||g_M||_p<infty`（`p>1`）或
uniform square-exponential moment，则弱紧性和一致可积性给出一个 genuine
all-moment limit；后者还保证解析/MGF 解释。单独的 `L^p` 弱极限只保证
nonnegative all-moment realization，不自动给 pointwise analytic SF。

## 4. 证据边界

* `PROVED`：有限 odd support 的 square-exponential rigidity；首个 Hankel
  cap；fixed-`d` Hankel feasibility radius collapse；uniform `L^p`/square-tail
  compactness接口。
* `OBSTRUCTION`：small-frequency finite Bochner minors 在 hidden degree
  `d>=5` 时只在约 `a^2 t^(2d)` 才敏感，不能单独提供 rigidity；未得到
  `m_0(a,d)` 的显式上界。
* `OPEN`：具有 infinitely many nonzero odd cumulants 的 genuine full-SF
  law 是否存在；这已成为下一轮 R138 的唯一核心。
* `CONDITIONAL`：从 scalar `RK=1` 到 genuine full-SF/all-row 的识别，以及
  `K_sp=log g` 与 `C_g=log B_g` 的互换。

审计命令：

`F:\\anaconda3\\python.exe r137_uniform_realization_audit\\audit_r137.py`
