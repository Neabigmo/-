# R142 — Semiclassical Gaussian-relative Bochner amplification audit

日期：2026-09-08

本目录记录网页端在公开提交
`ec8ceb40741ad187a87dc4b046bc71a0cecfec7e` 上完成的 R142。R142 研究的不是
更多 bounded real-MGF Fisher 常数，而是：raw characteristic kernel 的 Gaussian
阻尼能否通过 generalized quadratic-form normalization 被保留下来的正性和谱
放大重新恢复为 OU-invariant shape information。

对象仍须严格区分：spatial `K_sp=log g`、ordinary
`K=log E exp(tX)`、normalized Bargmann `B_mu(z)=exp(-z^2/2)M(z)` 及其
`C_g=log B_g`、formal cumulants、真实 moments、Hankel/Jacobi 系数、MGF
`M(z)` 和 characteristic `phi(t)=M(it)`。`RK=1` 到 genuine full-SF/all-row
仍是 `CONDITIONAL`；R142 没有构造 genuine non-Gaussian full-SF law。

## 1. R141 基线与证据分层

R141 脚本 marker 为：

`R141_R140_NORMALIZATION_PASSED`、`R141_OU_SCALING_PASSED`、
`R141_TRIANGLE_AND_PHASE_SLACK_PASSED`、`R141_PHASE_ERASURE_MAXIMUM_PASSED`、
`R141_BOCHNER_TOWER_SCALE_PASSED`、`R141_AUDIT_COMPLETED`。

脚本只核验有限的代数、标度、矩阵行列式、最大值接口和 tower 指数；
normal-family、Bochner positivity 以及 shell theorem 仍是带假设的分析证明。
R140 的 odd-step-2 以及 denominator 8 也保留：`M` odd 时 tail 从 `M+2`
开始，并且

`||tail||_2 <= 4B*tau^(M+5/2)/((M+2)*sqrt(2M+5))`.

因此

`tau^2 <= a*sqrt(h_M)*(M+2)*sqrt(2M+5)/(8B)`

足以把 tail 压到 finite-part lower bound 的一半。三点 full-SF 只给

`3 < |phi(rho*t*cos(theta))|^2 > <= 1+2 exp(-t^2/2)`

及 modulus-weighted phase slack；这仍不是 zero-shell phase 的反向 universal
下界。

## 2. Gaussian-relative generalized quadratic form

令 `mu_lambda=P_lambda mu`，取 normalized characteristic scale 的局部坐标
`x=sqrt(lambda) u`、`y=sqrt(lambda) v`。对固定 `R>0` 定义

`K_tilde_(lambda,R)(u,v)=phi_lambda(R(u-v))`,

以及 Gaussian reference

`G_R(u,v)=exp(-R^2(u-v)^2/2)`.

在 Fourier/form domain 中，对 Schwartz `f`：

`q_K(f)=int |f_hat(Rx)|^2 dmu_lambda(x)`,

`q_G(f)=int |f_hat(Rx)|^2 dgamma(x)`.

若 `g_lambda=dmu_lambda/dgamma`，则相对于 Gaussian form 的 generalized
operator 是

`A_lambda := G_R^(-1/2) K_tilde_(lambda,R) G_R^(-1/2)`

并在 Gaussian spectral representation 下对应 multiplication by `g_lambda`.
这不是 entrywise Schur quotient；其 positivity 来自 `g_lambda>=0`，所以应把
`A_lambda` 首先理解为 form-level positive operator。涉及 `G_R^(-1/2)` 时不可
无条件当作 bounded operator，而要在 Gaussian quadratic-form domain 上表述。

取 normalized coherent vector

`k_z(x)=exp(zx-z^2/2-|z|^2/2)` in `L^2(gamma)`.

直接计算得到

`<k_z,A_lambda k_w>
 = exp(conj(z)w-(|z|^2+|w|^2)/2) B_(mu_lambda)(conj(z)+w)`.

OU shape invariance 是

`B_(mu_lambda)(z)=B_mu(sqrt(lambda) z)`.

故对实 `y`：

`< k_(y/(2sqrt(lambda))), A_lambda k_(y/(2sqrt(lambda))) > = B_mu(y)`.

这给出 R142 的第一个严格结果：一个 genuine positive Rayleigh quotient 可以
无误差恢复 OU-invariant 的 real Bargmann shape。

## 3. 半经典谱标度

### 3.1 两节点与三点直接相位

若 `x_0=0`、`x_1=sqrt(lambda) u`，则

`K_lambda(x_0,x_1)=exp(-R^2u^2/2) B_mu(i sqrt(lambda) R u)`.

若第一 nonzero odd Bargmann degree 为 `d`，entry-level odd phase 是
`O(lambda^(d/2))`。两点 raw Gram 的 eigenvalues 是 `1+-|K_01|`，因此
odd phase 的 direct eigenvalue effect 是 `O(lambda^d)`；非退化三点 triangle
的 direct phase 也在 `lambda^d` 出现，因为 R141 的 `h^(2d)` 代入
`h=sqrt(lambda)`。这与第一处 Hankel-leading coefficient 敏感矩阵尺寸
`(d+3)/2` 完全不同。

### 3.2 raw Gaussian 小特征值

在 `|u_i|<=L` 的 m 点网格上，

`G_ij=exp(-R^2(u_i-u_j)^2/2)`

可作 rank-`m-1` 的 feature truncation，得到

`lambda_min(G_m) <= m sum_(k>=m-1) (R^2 L^2)^k/k!`.

当 `m-1>=2R^2L^2` 时进一步有

`lambda_min(G_m) <= 2m(R^2L^2)^(m-1)/(m-1)!`.

相应截断积分算子的第 `N+1` 个特征值满足

`lambda_(N+1)(T_G) <= 2L sum_(k>=N)(R^2L^2)^k/k!`.

这解释了 generalized normalization 为什么具有很大的 spectral amplification
room，但小特征值本身不自动提供负方向或 phase coercivity。

### 3.3 Hermite/confluent Toeplitz 极限

令 `psi_n=He_n/sqrt(n!)`，`a_j(mu)=E_mu psi_j(X)`。OU 给出

`a_j(mu_lambda)=lambda^(j/2)a_j(mu)`.

定义 fixed-offset block

`H_(lambda,n)^(r)=[ E_(mu_lambda)(psi_(n+p) psi_(n+q)) ]_(p,q=0)^r`.

若 `n lambda -> tau>0`，则

`H_(lambda,n)^(r) -> T_r(b_tau)`,

其中

`b_tau(theta)=B_mu(2 sqrt(tau) cos(theta))`,

`hat b_tau(k)=(2pi)^(-1) int_0^(2pi) b_tau(theta) exp(-ik theta)dtheta`.

一个 degree `d=2s+1` 的 adjacent odd contribution 具有精确极限

`lambda^(d/2) sqrt((n+1)! n! d!)/((n-s)! s! (s+1)!)
 -> sqrt(d!)*tau^(d/2)/(s!(s+1)!).`

因此 `n~lambda^(-1)` 正好把 fixed hidden odd degree 从 `lambda^(d/2)` 放大
回 `O(1)`。但对于 genuine probability law，`M_mu(x)>0` 对实 `x`，所以
`b_tau(theta)>0`，从而

`c^*T_r(b_tau)c=(2pi)^(-1)int b_tau(theta)|sum_j c_j exp(ij theta)|^2dtheta
 >= min_theta b_tau(theta)||c||^2`.

这说明 canonical fixed-energy limit 是 strict positive Toeplitz cone：它恢复
odd shape，却把该 shape 合法地吸收到正 symbol 中。故这是 amplification
theorem，同时也是 positivity-tautological no-go。

## 4. 正 coherent recovery 与条件闭合

定义

`R_lambda(y)=<k_(y/(2sqrt(lambda))), A_lambda k_(y/(2sqrt(lambda)))>`.

则 `R_lambda(y)=B_mu(y)>0` 对每个 `lambda` 精确成立。令

`O_lambda(y)=1/2 log(R_lambda(y)/R_lambda(-y))=1/2 log(M_mu(y)/M_mu(-y))`.

将其代入三方向 angular charge，可得

`C_(1,lambda)(s)=< sum_j O_lambda(Rs c_j(theta)) exp(-3i theta)>`

`=Q_1(Rs/rho)`.

因此 R141 regular normalized shell 的相同有限 odd Gram argument 给出

`int_0^(tau*) |V^(-1/2) C_(1,lambda)(s)|^2 ds >= c* >0`

对所有 `0<lambda<1`。这条 positive-form recovery 是 `PROVED` under the
R141 regular-shell hypotheses，并且不随 OU 参数消失。

但 `R_lambda(y)>0` 对一般 genuine law 本来就成立，故正性本身没有消除 odd
shape。一个足够闭合的条件是

`B_mu(y)B_mu(-y)>=1` for every real `y`.

在 genuine full-SF 下，令 `C=log B`、`C_e=(C(y)+C(-y))/2`、
`C_o=(C(y)-C(-y))/2`。该条件给 `C_e>=0`；full-SF 与
`theta -> theta+pi` 配对给

`1=< exp(H_e) cosh(H_o)>`, `H_e=sum_j C_e(t r_j)>=0`.

被积函数处处至少为 1，平均也为 1，所以 `H_e=H_o=0`，从而 `B=1`、
`M(z)=exp(z^2/2)`，law Gaussian。这个 R142-C 是 `CONDITIONAL`：真正尚未
证明的是 full-SF 是否自动提供该 even-sector domination，或一个足以替代它的
不等式。

## 5. 严格失败机制

### 5.1 复 coherent overlap 仍被指数阻尼

取 `z_-=-iy/(2sqrt(lambda))`、`z_+=iy/(2sqrt(lambda))`，则

`<k_(z_-),A_lambda k_(z_+)>
 = exp(-y^2/(2lambda)) B_mu(iy)`.

所以 complex/characteristic phase 只能通过指数小的 coherent off-diagonal
进入。对应的二点 coherent Gram 只给一个随 `lambda` 变得无效的上界；real
diagonal Rayleigh quotient 能无损恢复 `B_mu(y)`，却不能自动恢复 `B_mu(iy)`。

### 5.2 rank 的两个阈值

若要用 coherent chain 从 0 走到 imaginary displacement
`iy/sqrt(lambda)`，并要求相邻 overlap 不小于 `exp(-C^2/2)`，则三角不等式
给出

`m_lambda >= |y|/(C sqrt(lambda))`.

这是 coherent-chain rank 的 `Omega(lambda^(-1/2))` 下界。另一方面，
`k_z=exp(-|z|^2/2)sum_n z^n psi_n/sqrt(n!)` 的典型 Hermite level 为
`n~|z|^2`；在 `|z|~lambda^(-1/2)` 时，confluent/Hermite energy 需要
`n~lambda^(-1)`。两者是同一半经典尺度的 position/frequency 与 oscillator
energy 表述。

### 5.3 canonical spectral amplification 的 no-go

`H_(lambda,n)^(r)->T_r(B_mu(2sqrt(tau)cos(theta)))` 且该 symbol 对任何
genuine law 在实轴严格为正。因此 fixed-`tau` Hermite spectral amplification
不会产生 negative mode；它将 odd Fourier coefficient 吸收到合法的 positive
Toeplitz symbol 中。这是 genuine probability-level structure，而不是 relaxed
kernel ghost。

full-SF 在此极限只是

`< b_tau(theta)b_tau(theta+2pi/3)b_tau(theta+4pi/3)> = 1`.

所以新的最小问题是

`b_tau>0 + all-tau cubic same-factor identity  ?=>  b_tau=1`.

系数形式的 formal completion 不能替代 genuine positive realization。

## 6. 节点族与 backward tower

固定 normalized-separated nodes 的 raw Gram 趋于 identity；`x_j=sqrt(lambda)u_j`
的 semiclassical nodes 使 odd entry 为 `lambda^(d/2)`；三点 direct phase 为
`lambda^d`；第一 Hankel-leading sensitive size 仍为 `(d+3)/2`。dense finite
nodes 可能利用 Gaussian 小特征值做 generalized amplification，但任何单次
finite test 仍然只是 finite-level information。导数 Gram 在去掉 `R^(i+j)`
后就是 moment Hankel，再换到 Gaussian monomial-to-Hermite basis 即得到上述
Hermite block。固定 degree 的 odd shape 要恢复到 `O(1)`，必须达到
`n~lambda^(-1)`。

对 `g_N=P_(q^N)h_N`，令 `lambda_N=q^N`。Gaussian-relative positive operator
`A_N=M_(g_N)` 满足

`<k_(y/(2q^(N/2))),A_N k_(y/(2q^(N/2)))>=B_(h_N)(y)`.

因此 bottom `g_N->1` 并不消灭 top Bargmann shape；shape 被搬到
`|z|~q^(-N/2)` 的 coherent radius，以及 `n~q^(-N)` 的 Hermite energy。当前
exact/Jacobi 控制只到 `m=O(N)`，而 OU-invariant spectral recovery 需要指数级
`m~q^(-N)`，形成清楚的 linear-versus-exponential gap。

若 compatible single infinite tower，R138 的 common zero-free disk 加
Bargmann scaling 已独立给 Gaussian rigidity；R142 针对的是 incompatible
finite-depth sequences。若未来 full-SF/all-row 能在 `|z|~q^(-N/2)` 提供
depth-independent even-sector flattening（如 `B_h(y)B_h(-y)>=1`），则 R142
正恢复和 R141 regular-shell lower gap 可以矛盾，排除该类 tower。这个 flattening
目前仍未证明；从 `B_mu`/ordinary `K` 到 spatial `P_3 K_sp` 的桥也仍未闭合。

## 7. 证据分级与下一轮

`PROVED`：Gaussian-relative form representation（在 form domain 上）、positive
coherent kernel identity、OU-invariant real Bargmann recovery、R141 regular-shell
L2 gap 的正形式恢复、raw Gaussian 小特征值上界、Hermite–Toeplitz semiclassical
limit、`n~lambda^(-1)` odd spectral amplification、coherent-chain rank 下界，
以及 R141 之前已审计的结果。

`CONDITIONAL`：bare scalar `RK=1` 到 genuine full-SF/all-row；ordinary
MGF/Bargmann rigidity 到 spatial `P_3K_sp=0`；以及 full-SF 自动推出
`B(y)B(-y)>=1` 或同等 even-sector domination。

`OBSTRUCTION`：复 coherent off-diagonal 的指数阻尼、固定/次临界 raw rank 的
phase erasure、canonical Toeplitz positivity 的 non-coercivity、symmetric/even
zero-sign sector，以及 finite-test invisibility。

`OPEN`：能否从 full-SF + coherent tensor positivity 得到超出 `B(real)>0` 的
even-sector/off-diagonal coercivity；或者构造 positive coherent-kernel 层面的
严格 cancellation witness。下一轮唯一任务：**R143 — Coherent-State Tensor
Positivity / Even-Sector Closure**。
