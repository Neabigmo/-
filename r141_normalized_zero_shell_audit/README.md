# R141 — Renormalized zero-shell Bochner phase compactness

日期：2026-09-08

本目录记录网页端在 R140 提交 `32f86ddb2d7b21b9dfaec7027dd49b987d2d34a0`
之后给出的 R141 推进，并把其中可以独立核验的公式落成本机审计。R141 的
目标不是宣称已经解决 Positive Backward-Tower Exact Zero-Set Rigidity，而是
把零点壳的尺度归一化、OU 变换和有限秩 Bochner 盲区放在同一条精确接口上。

对象仍须区分：`RK=1`、空间 `K_sp=log g`、normalized Bargmann 的
`C_g=log B_g`、ordinary `K=log E exp(tX)`、formal cumulants、真实矩以及
`phi(t)=M(it)`。凡需使用 full same-factor identity 的地方，都显式写作
genuine full-SF/all-row 假设。R141 没有构造 genuine non-Gaussian full-SF law。

## 1. R140 基线复核

R140 的 odd block 以步长 2 取项；若 `M` 为 odd 且 `tau<=1/2`，则

`||tail||_2 <= 4B*tau^(M+5/2)/((M+2)*sqrt(2M+5))`.

因此网页端使用的 `8` 是足够的：

`tau^2 <= a*sqrt(h_M)*(M+2)*sqrt(2M+5)/(8B)`.

R140 的 full-SF 三点 Bochner 约束也保留：令 `rho=sqrt(2/3)`，则

`3 < |phi(rho*t*cos(theta))|^2 > <= 1+2 exp(-t^2/2)`.

若 `P=prod_j phi(t*r_j)=A exp(i*Psi)`，full-SF 只给出相位松弛

`<A*(1-cos(Psi))> = <A>-exp(-t^2/2) >= 0`.

这提供 modulus/even-sector 控制，但尚未提供 zero-shell phase 的 universal
positive gap。

## 2. 归一化的 odd-ratio phase

写 `M(z)` 为 MGF，并在公共的 `+-` 零因子约去后定义

`F(z)=M(z)/M(-z)`, `Omega(z)=1/2 log F(z)`, `Omega(0)=0`.

在 `|z|<R_Delta` 的局部支上，`Omega` 是 odd analytic function。它在实轴
对应 ordinary odd log-cumulant；它不是 spatial `K_sp`，也不是未经说明的
formal/global branch。

沿网页端的 angular normalization，定义

`mathfrak Q_r(s) = -i Q_r(i*R_Delta*s/rho)`, `|s|<1`.

若存在统一的 regular normalized geometry

`J<=J0, sigma>=sigma0>0, Gamma>=Gamma0>1, B3<=b*sqrt(V)`,

取

`N*=ceil(max{1,4J0/sigma0})`,

`m*` 为最小 odd `>=3` 且
`b*Gamma0^(-(m*-3)) <= 1/sqrt(8)`，

`M*=m*+2(N*-1)`,

`ell* = min_{3<=n<=M*, n odd}
 [ (3/2^n) binom(n,(n-3)/2) ]/n`,

`a*=ell*/sqrt(8)`,

`h*=lambda_min[1/(d_i+d_j+1)]`, `D={3,5,...,M*}`,

`B*=sqrt(J0)+b`,

`tau*=min{1/2, sqrt(a*sqrt(h*)*(M*+2)*sqrt(2M*+5)/(8B*))}`.

则 R140 shell estimate gives the scale-free local conclusion

`int_0^tau* |V^(-1/2) mathfrak Q_1(s)|^2 ds
 >= c* = (1/4) a*^2 h* tau*^(2M*+1) > 0`.

这个结论的量词是关键：它是“在明确的 separation/radial-gap/tail 正则类中，
归一化 odd-ratio phase 形成非零 L2 gap”。它不是对所有 square-exponential
概率律的 universal Bochner gap。归一化后的函数族在单位圆盘内是 normal
family；任何局部一致极限仍非零。

## 3. OU 变换：零点几何不变，但 raw characteristic 会阻尼

对 `0<lambda<1`，OU 变换写作

`M_lambda(z)=exp((1-lambda)z^2/2) M(sqrt(lambda)*z)`.

故

`R_Delta,lambda=R_Delta/sqrt(lambda)`,

归一化零点坐标以及归一化 `mathfrak Q_r` 不变。实轴特征函数满足

`phi_lambda(R_lambda*s)
 = exp(-(1-lambda)R_Delta^2*s^2/(2lambda)) phi(R_Delta*s)`.

三点 angular product 的对应 Gaussian 因子还带 `rho^2`：

`exp(-(1-lambda)R_Delta^2*s^2/(2lambda*rho^2))`.

所以 raw phase slack 会被压低；raw Bochner positivity 不能单独给出 OU-invariant
的 scale-free phase gap。相对于 Gaussian 的量

`B_mu(z)=exp(-z^2/2) M(z)`

在 OU 下保留 shape，但一般不是 positive-definite characteristic function。
这正是下一阶段必须重新接上的 coercive interface。

另一个限制是：signed divisor 主要控制 `M(z)/M(-z)` 的 phase，公共的对称零点
因子会从 ratio 中消失，却仍可能改变 `phi` 的实符号和 modulus。因此，在把
odd divisor phase 放进 `Re(phi_1 phi_2 phi_3)` 之前，还必须控制 symmetric/even
sign sector。

## 4. 有限秩 Bochner 检验的真实盲区

若第一非零 odd cumulant degree 为 `d>=3`，则 OU 后实轴 imaginary part obeys

`sup_x |Im phi_lambda(R_lambda*x)|
 <= (E|X|^d/d!) * (d*lambda/(e*(1-lambda)))^(d/2)`.

在 R132 的 square-exponential tail bound 下，可使用

`epsilon_d(lambda) <= 2 exp(-1/8) * (4lambda/(1-lambda))^(d/2)`.

任何 `n` 点 normalized Gram matrix `G_lambda` 满足

`||G_lambda-Re(G_lambda)||_op <= (n-1) epsilon_d(lambda)`.

若 normalized node separation 为 `|x_i-x_j|>=a`，Gaussian modulus 又给出

`||G_lambda-I||_op
 <= (n-1) exp(-(1-lambda)R_Delta^2*a^2/(2lambda))`.

因此固定秩或满足
`n_lambda*(4lambda/(1-lambda))^(d/2)->0` 的 subcritical rank 检验，不能
保留 O(1) odd phase。真正还未排除的逃逸必须使用 rank growth、confluent/high
order normalization，或直接改用 Gaussian-relative 的谱对象。

## 5. backward tower 的含义

对有限深度 tower `g_N=P_{q^N}h_N`，若顶层有非对称零点，底层尺度满足

`R_Delta(g_N)=R_Delta(h_N) q^(-N/2) >= q^(-N/2)/4`,

而 normalized divisor geometry 与 normalized phase 不变。若 normalized node
separation 为 `a`、节点数为 `m_N`，则 raw Gram 的 Gaussian 估计为

`||G_N-I||_op <= (m_N-1)
 exp(-(1-q^N)*a^2/(32q^N))`.

当 `log m_N=o(q^(-N))` 时，raw Gram 趋于 identity；若 hidden odd degree 也随
`N` 增大，有限/次临界 rank 的 blindness 更强。故当前最清楚的剩余逃逸被命名为
`Gaussian-relative spectral-rank escape`。

## 6. 结论分级与下一步

`PROVED`：R140 的显式 regular-shell shell-to-energy theorem；R141 的归一化
odd-ratio normal-family 与非零 L2 gap；OU 下归一化零点/phase 不变；raw
Gaussian damping；finite-rank erasure；三点 full-SF triangle；以及此前的
compatible infinite-tower rigidity。

`CONDITIONAL`：scalar `RK=1` 是否升级为 full-SF/all-row；ordinary
MGF/Bargmann 结论如何升级为空间 `P_3 K_sp`；以及对假设存在的 genuine law
沿 OU 轨道作反证。

`OBSTRUCTION`：angular/radial shell coalescence、outer-degree cancellation、
公共 symmetric/even sign sector、raw Bochner damping，以及所有固定/次临界
秩的 phase erasure。

`OPEN`：构造一个保持 positivity 且能读出 OU-invariant `B_mu`/odd phase 的
Gaussian-relative positive quadratic form；或证明其谱特征值必然消失，从而给出
phase escape。下一轮唯一任务：**R142 — Gaussian-Relative / Semiclassical
Bochner Spectral Amplification**。

本地脚本 `audit_r141.py` 只做有限的代数、标度、最大值和指数接口检查；它不把
这些检查冒充为 infinite-dimensional theorem。
