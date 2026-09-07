# R116 — Single-Law Factorized Gaussian-Radial Cubic Exclusion

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（结构恒等式，待本机 audit）；CONDITIONAL PROVED；核心 OPEN。

## 1. 目标与诚实边界

取 centered variance-one law `X`，令 `X_1,X_2,X_3` 为 iid copies，并用
120-degree residual transform

`Z = sqrt(2/3) (X_1 + omega X_2 + omega^2 X_3)`,  `omega=exp(2*pi*i/3)`.

主问题是判断

`|Z|^2 ~ chi^2_2` 以及 residual characteristic 的 same-factor 分解

`Phi(xi)=prod_j phi(v_j dot xi)`

是否必然推出 `kappa_3(X)=0`。本轮没有证明该蕴含；它与单一 sample-size、无
symmetry 的 chi-square sample-variance characterization 层级相同，不能把
结构压缩误写成主定理。

## 2. 精确 residual 表示（PROVED）

直接恒等式为

`|X_1+omega X_2+omega^2 X_3|^2`
`= X_1^2+X_2^2+X_3^2-X_1X_2-X_2X_3-X_3X_1`.

若 `Q=sum_j (X_j-Xbar)^2`，则

`Q=(2/3)(X_1^2+X_2^2+X_3^2-X_1X_2-X_2X_3-X_3X_1)`,

所以 `|Z|^2=Q`。full exactness 等价于

`|Z|^2 ~ chi^2_2`,

即 residual radius 的密度为 `r exp(-r^2/2) dr`；角变量仍未被确定。

循环置换和交换 iid coordinates 分别给出 `Z -> omega^2 Z` 与 `Z -> conjugate(Z)`，
故 residual law 自动具有 `D_3` 对称性。

## 3. cubic skew = 第一角谐波的加权矩（PROVED）

写 `Z=R exp(i Theta)`，并取 regular conditional angular law
`sigma_r(d theta)=P(Theta in d theta | R=r)`。定义

`u_k(r)=int exp(i*3*k*theta) sigma_r(d theta)`.

`D_3` 对称性使 `u_k` 为实值且 `|u_k|<=1`。由 iid、centered 与
`E X_j^3=kappa_3(X)`，

`E Z^3 = 2 sqrt(2/3) kappa_3(X)`.

在 radial exactness 下，

`E Z^3 = int_0^infty r^3 u_1(r) r exp(-r^2/2) dr`,

因此

`kappa_3(X)=sqrt(3/8) int_0^infty r^3 u_1(r) r exp(-r^2/2) dr`.

所以 R116 只需杀掉一个 weighted first-harmonic moment；要求 `u_1=0` 是更强的
结论，并非当前必要目标。

## 4. Fourier/Hankel 与 MGF/Bessel 两条全局桥（PROVED）

取 `v_j` 为长度 `sqrt(2/3)` 的三条 120-degree vectors，使
`sum_j v_j=0`、`sum_j v_j v_j^T=I_2`。对 `xi=rho(cos alpha,sin alpha)`，

`Phi(rho,alpha)`
`= prod_j phi(rho*sqrt(2/3)*cos(alpha+2*pi*(j-1)/3))`.

Jacobi–Anger 展开给出 order-3 harmonic

`H_1(rho)=int_0^infty J_3(rho r) u_1(r) r exp(-r^2/2) dr`,

且按本轮 Fourier convention

`(1/(2*pi)) int exp(i*3*alpha) Phi(rho,alpha) d alpha = -i H_1(rho)`.

因为 `J_3(x)=x^3/48+O(x^5)`，

`H_1(rho)=sqrt(2/3) kappa_3(X) rho^3/24+O(rho^5)`.

径向 exactness 只给 zeroth mode

`H_0(rho)=int_0^infty J_0(rho r) r exp(-r^2/2)dr=exp(-rho^2/2)`。

因此已知的是 `H_0` 的 Gaussian 值，需要的是 `H_1` 在零点的三阶系数。

同一信息可由 real MGF 书写。令 `M(z)=E exp(zX)`、
`F(z,alpha)=prod_j M(z*sqrt(2/3)*cos(alpha+2*pi*(j-1)/3))`。径向 exactness
给 `(1/(2*pi)) int F(z,alpha)d alpha=exp(z^2/2)`。若

`c_1(z)=(1/(2*pi)) int exp(-3*i*alpha) exp(-z^2/2)F(z,alpha)d alpha`,

则

`c_1(z)=exp(-z^2/2) int_0^infty I_3(zr)u_1(r)r exp(-r^2/2)dr`,

`c_1(z)=sqrt(2/3) kappa_3(X) z^3/24+O(z^5)`。

于是

`u_1 <-> H_1 <-> c_1`

是同一 cubic sector 的三种全局坐标；它们不能与 `P_3 K` 或 Schur scalar
observable 混为一谈。Hankel injectivity 只说明 `H_1 identically 0` 等价于
`u_1=0`，不能由 zeroth radial mode 自动推出。

## 5. regularity reduction 与 real-space factorization（PROVED）

若存在 genuine full-exact law `mu` 且 `kappa_3(mu)!=0`，则对任意 `0<t<1`，
`mu_t=P_t mu` 仍 full-exact，且

`kappa_3(mu_t)=t^(3/2) kappa_3(mu)`。

`mu_t` 是 Gaussian convolution，具有严格正、光滑、real-analytic density；
因此 regularity 不是缺口。

若 `f` 是 one-body density，令 `v_j` 为上述 tight frame，则 residual density 为

`p_f(z)=int_R prod_j f(m/sqrt(3)+v_j dot z) dm`.

full exactness 只要求其 circular radialization 满足

`(1/(2*pi)) int_0^(2*pi) p_f(r e_theta)d theta`
`=(1/(2*pi)) exp(-r^2/2)`  对所有 `r`。

这把问题化成严格正 analytic 的 three-line convolution/marginal 的 Gaussian
radialization问题；same-factor 结构在此处仍不可替代。

## 6. 非 factorized smooth obstruction（PROVED，不是项目反例）

令 `gamma_2` 为标准二维 Gaussian，并取足够小的 `epsilon != 0`：

`d nu_epsilon(z)=[1+2 epsilon Re(z^3) exp(-|z|^2)] d gamma_2(z)`。

扰动有界，故可保持严格正；其角平均为零，所以仍有
`|Z|^2~chi^2_2`。但

`E_{nu_epsilon} Z^3 = (16/27) epsilon != 0`。

这证明 “二维 Gaussian radial law + positivity” 不足以消灭 cubic angular
mode。它不是项目 counterexample，因为目前没有办法把 `nu_epsilon` 实现成
上述同一个 one-body density 的 same-factor three-line convolution。

## 7. 一个可交付的条件性小定理（CONDITIONAL PROVED）

若 one-body law classical infinitely divisible 且具有所需 exponential moments，
Lévy–Khintchine 给出 `kappa_6=int x^6 Pi(dx)>=0`。而 full exact degree-six
fingerprint 已给

`kappa_6=-3*kappa_3^2`。

故 `0<=kappa_6=-3*kappa_3^2<=0`，从而 `kappa_3=0`、`kappa_6=0`；再由
`int x^6 Pi(dx)=0` 得 Lévy measure 消失，centered variance-one law 即为
Gaussian。结论为

`full exact + classical infinite divisibility => N(0,1)`。

它与主问题的区别必须保留：varying-bottom positive OU tower 不会自动赋予
top law classical infinite divisibility。

## 8. R116 判决与 R117

### 已确立

- residual 的复表示、`|Z|^2=Q` 与 `chi^2_2` 精确接口；
- `kappa_3` 与 `u_1` 的加权矩等价式；
- characteristic 的 order-3 Hankel bridge 与 MGF 的 `I_3` bridge；
- forward OU 可无损地限制到严格正 analytic one-body density；
- 非 factorized smooth Gaussian-radial cubic obstruction；
- classical infinite divisibility 下的 Gaussian 条件性刻画。

### 仍为 OPEN

`|Z|^2~chi^2_2` 且 `Phi(xi)=prod_j phi(v_j dot xi)`
`=> kappa_3(X)=0`。

这不是又一个 finite Gram/minor 缺口，而是 same-factor global angular-mode
annihilation；当前资料不足以声称其解答。

### R117 最小命题

对严格正 analytic `f`，若 `p_f` 如上且其 circular radialization 精确为二维
Gaussian，只证明

`int_0^infty r^3 u_1(r) r exp(-r^2/2)dr=0`。

工具优先级是 three-line convolution 的 spherical-harmonic/total-positivity
性质，或直接利用正核 `I_3(zr)` 对 R104 first Schur charge 的变换；不回到
`tau^4/tau^5`、有限 Schur minors、数值/SDP/optimizer。

## 9. 证据等级

`audit_r116.py` 只核验可机械复现的代数、矩、frame、Bessel leading term、
OU scaling 与 obstruction integral。Hankel injectivity、regular conditional
law、Gaussian convolution regularity、Lévy–Khintchine 与 global document-level
推导仍标为 ANALYTICALLY PROVED / CONDITIONAL，不冒充脚本已经证明无限维命题。
