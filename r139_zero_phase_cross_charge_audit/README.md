# R139 — zero-divisor phase / cross-charge Bochner audit

日期：2026-09-08

本目录审计网页端 R139 的长篇推导。对象始终是 centered、variance-one、
`E exp(eta X^2)<infty` 的 genuine probability law，并在需要处额外假设
full same-factor identity (SF)。`RK=1`、空间的 `K_sp=log g`、normalized
Bargmann 的 `C_g=log B_g`、ordinary `K=log E exp(tX)`、formal moments 与
真实 moments 不能互换。网页端给出的新的 genuine law 仍然没有被构造。

## 1. 零点除子：严格结果

平方指数矩给出 entire ordinary MGF `M`，order 至多二；genus-two Hadamard
分解和 `sum n(zeta)|zeta|^(-3)<infty` 给出

`kappa_m/(m-1)! = -sum n(zeta) zeta^(-m)`, `m>=3`.

按 `zeta -> -zeta` 的轨道选 representative，置
`delta(zeta)=n(zeta)-n(-zeta)`。奇数阶时，成对零点先严格抵消：

`kappa_m/(m-1)! = -sum_R delta(zeta) zeta^(-m)`, `m odd`.

令 `R_Delta` 为 `delta != 0` 的最小模，若存在；第一壳是有限集。对
`m=2k+1`，第一壳给 finite exponential sum

`A_k=sum_j delta_j exp(-i(2k+1)theta_j)`.

在先按 `+/-` 轨道合并后，不同 representative 给出不同
`lambda_j=exp(-2 i theta_j)`；故

`lim_N N^(-1) sum_{k<N}|A_k|^2=sum_j delta_j^2>0`.

外壳由 genus-two 的加权可和性控制，因而

`limsup_(m odd)(|kappa_m|/(m-1)!)^(1/m)=1/R_Delta`.

更定量地，存在无穷多个 `k` 使
`|kappa_(2k+1)|/(2k)! >= c_Delta R_Delta^(-(2k+1))`，其中可取的
`c_Delta` 只需依赖第一壳；外壳误差只影响该子序列从哪一项开始成立。
但逐阶 lower bound 不成立：formal divisor witness
`zeta=R exp(+i pi/6), R exp(-i pi/6)` 给 `2 R^(-m) cos(m pi/6)`，在
`m=3,9,15,...` 精确为零。它不是 probability counterexample。

同一零点表示还给出 odd part 的局部精确重求和。对
`|t| sqrt(2/3)<R_Delta`，

`O(t)=-sum_R delta(zeta)[atanh(t/zeta)-t/zeta]`.

若 `u(theta)=r_1 r_2 r_3`，则

`H_o(t,theta)=-sum_R delta(zeta) atanh(((t/zeta)^3 u(theta))/(1-(t/zeta)^2/2))`.

这是 zero divisor 到 all-degree angular odd field 的合法接口；它仍是局部
复解析恒等式，不是 positivity 结论。

## 2. 新的奇尾刚性：无限变号

`R_Delta<infty` 意味着 odd Taylor series `O` 有有限半径 `R_Delta`，但
`O` 在整个实轴仍 real analytic，因为 `M(t)>0`。若 odd cumulants 从某处起
全非负，则去掉有限 odd polynomial 后可写为 `t^(2K+1) F(t^2)`，其中 `F`
的系数非负、半径为 `R_Delta^2`。Pringsheim 定理要求 `F` 在正实点
`R_Delta^2` 有奇点；另一方面，实轴上 `O` 在 `t=R_Delta` 附近有复解析
延拓，故 `F` 在该正点可解析，矛盾。全非正同理。

因此可记录为 genuine square-exponential level 的 theorem：非对称 law 的
odd cumulants 必有无限多个正值和无限多个负值。这个证明的关键条件是
`R_Delta<infty`；不能把 Pringsheim 直接用于一个可能为 entire 的 odd
series，也不能把它误写成 formal-SF 结论。

## 3. full-SF 的跨 charge 能量

full-SF Fisher identity 与 `K(s)>=0` 给出

`<H_t^2+H_theta^2/t^2> <= 2 exp(t^2/2)`.

`H_o` 只有 Fourier modes `3r`、`r` odd。若
`Q_r=<H_o exp(-3 i r theta)>`，Parseval 给出真正的 weighted majorization

`sum_(r odd)[|Q_r'|^2+9 r^2 |Q_r|^2/t^2] <= exp(t^2/2)`.

因此不同 angular charges 在这个 `L^2` 能量中不能互相抵消；任意
measurable `w>=0` 且 `int_0^T w(t) exp(t^2/2)dt<infty` 时，Tonelli 给出
相应的 `t`-weighted integral inequality。特别地
`|Q_r(t)| <= |t| exp(t^2/4)/(3r)`。

这仍然是 upper bound，而不是从零点半径反推正下界。精确失败机制是同一
`Q_r` 内不同 cumulant degrees 相消。比如
`Lambda_(5,1)=15(rho/2)^5`、`Lambda_(7,1)=63(rho/2)^7`，取
`c_7=-(10/(7 t_0^2))c_5` 即可使 `Q_1(t_0)=0`，而 `c_5!=0`。
更一般地，取 `D=6q+1`、degrees `5,7,...,D`，变量数 `3q-1` 大于
`2q` 个条件 `Q_r(t_0)=Q_r'(t_0)=0`（`r=1,3,...,2q-1`），故存在非零
formal vector 使 `H_o(t_0,theta)=H_{o,t}(t_0,theta)=0`。这是严格的
formal cancellation obstruction，不是 positive law。

## 4. Bochner 与有限测试的边界

对固定有限节点 `x_0,...,x_m`，`phi(t)=M(it)` 的 small-frequency Gram
determinant 满足

`det T_m(h)=h^(m(m+1)) Vandermonde(x)^2 Delta_m / prod(k!)^2`
`+ O(h^(m(m+1)+2))`.

第一 hidden odd degree `d=2s+1` 只在 Hankel level `m=s+1` 首次出现，故
Bochner 矩阵尺寸为 `(d+3)/2`；固定有限尺寸只能看见有限 prefix。节点、尺度
和测试频率即使随 `d` 改变，只要每次仍是有限族，也没有 global phase
rigidity：在任意开区间内，有限个 polynomial moments 与有限个 sine/cosine
functionals 线性独立；紧支撑光滑扰动的有限维像为满射，足够小的 target
由 `g=1+f` 实现且保持严格正性。该结论只说明 finite-test invisibility，
不构成 relaxed Hankel ghost 或 full-SF counterexample。

## 5. 可严格排除的子类与新的小定理

已排除：finite/eventually-zero odd support；normalized odd root-limsup 为
零；`C_g` entire；full-SF 下 MGF 只有有限总零点；以及本节的 eventually
one-sign odd tail。

有限第一非配对壳、自然 reciprocal `l^1/l^2`、有限阶/有限型和单个 law 的
fixed zero-free disk 都不足以给 global rigidity；普通指数 normalized tail
也不能推出对称。

一个可独立成 lemma 的 genuine probability-level 结果是：若 full-SF law
满足 `kappa_(2m)>=0` 对全部 `m>=2`，则 Gaussian。因为

`<H>=sum_(m>=2) A_(2m) kappa_(2m)t^(2m)/(2m)! <=0`,
`A_(2m)=3 binom(2m,m)/6^m>0`，故所有高阶偶累积量为零；于是
`M(t)M(-t)=exp(t^2)`，所以 `X-X'` 是 Gaussian，Cramer decomposition
给出 `X` Gaussian。特别地，square-exponential infinitely divisible
full-SF law 也必 Gaussian，因为其高阶偶累积量由 Levy measure 给出非负项。

## 6. compactness 与 backward tower

固定 formal full-SF moment sequence，若 finite-jet genuine realizations
满足 `sup_M E exp(eta X_M^2)<infty`，则 tightness、polynomial uniform
integrability 和 subsequential moment convergence 产生 genuine all-degree
law；entire MGF 再把 formal SF 升级为 analytic SF。`L^p(gamma)` 的充分条件
是 `1<p<infty` 且 `sup ||g_M||_p<infty`。固定双侧 MGF 界只先给 strip，必须
按“strip -> actual SF -> R132 square tail”的顺序使用。

对 projectively compatible single bottom law，genuine full-SF/all-row 的
统一 zero-free disk 加上 `B_(P_s h)(z)=B_h(sqrt(s)z)`，使 bottom 的每个零点
被缩到共同 disk，故 bottom Gaussian。对每个深度更换顶层的 incompatible
moving tower，`d_N->infty,a_N->0` 仍未排除。

## 7. 证据分层与下一任务

* **PROVED**：zero-divisor root formula；最小非配对壳的 subsequential
  quantitative lower bound；非对称 square-exponential law 的 odd-cumulant
  无限变号；angular `H^1` cross-charge upper majorization；finite Bochner
  leading term；even-cumulant-cone Gaussian rigidity；uniform compactness
  interface；compatible genuine backward-tower rigidity。
* **OBSTRUCTION**：同一 `Q_r` 内跨 degree cancellation；任意有限 Bochner
  测试族的局部隐身；从 real-axis upper energy 得不到 zero-shell lower gap。
* **CONDITIONAL**：scalar `RK=1 -> genuine full-SF/all-row`；ordinary
  MGF/Bargmann 结论到 spatial `P_3 K_sp`；任何 formal cancellation witness
  到 genuine law。
* **OPEN**：具有无限非配对 MGF zero divisor、无限变号 odd tail 且满足
  full-SF 与 Bochner positivity 的 genuine law是否存在；以及 incompatible
  moving-top positive backward tower。

唯一下一轮任务：寻找能把 `R_Delta` 的 first-shell mass 反向传到 real-axis
angular/Bochner energy 的 coercive lower bound；若做不到，继续构造带明确量词
的 cancellation obstruction，不能宣称已经存在 non-Gaussian full-SF law。

