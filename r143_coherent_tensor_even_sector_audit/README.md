# R143 — Coherent-frame tensor positivity and even-sector closure

日期：2026-09-08

本目录记录网页端在公开提交
`e16d79105cf430d9ce9381e85ccbd71cd6479646` 的 R142 基线上完成的 R143。
本轮只推进 `Positive Backward-Tower Exact Zero-Set Rigidity` 的
coherent/tensor 接口；没有构造 genuine non-Gaussian full-SF probability law，
也没有证明该 law 不存在。

全程区分：spatial `K_sp=log g`、ordinary
`K=log E exp(tX)`、normalized Bargmann
`B_mu(z)=exp(-z^2/2)M_mu(z)`、`C_g=log B_g`、formal cumulants、真实 moments、
Hankel/Jacobi 系数、MGF `M` 与 characteristic function `phi(t)=M(it)`。
从 bare scalar `RK=1` 到 genuine full-SF/all-row 仍然是 `CONDITIONAL`；从
`B_mu`/`C_g` 到 spatial `P_3 K_sp` 的桥仍然 `OPEN/CONDITIONAL`。

## 1. R142 审计收束

R142 的 form identity 保持不变。对 `mu_lambda=P_lambda mu`、局部变量
`x=sqrt(lambda)u`、`y=sqrt(lambda)v`，令

`K_tilde_(lambda,R)(u,v)=phi_lambda(R(u-v))`,

`G_R(u,v)=exp(-R^2(u-v)^2/2)`.

在 Schwartz/form domain 上

`q_K(f)=int |f_hat(Rx)|^2 dmu_lambda(x)`,

`q_G(f)=int |f_hat(Rx)|^2 dgamma(x)`.

当 `0<lambda<1` 时 OU smoothing 给出 `mu_lambda << gamma`，记
`g_lambda=dmu_lambda/dgamma`。相对算子

`A_lambda=G_R^(-1/2) K_tilde_(lambda,R) G_R^(-1/2)`

只能首先理解为 closed quadratic-form 的 generalized normalization；在
Gaussian spectral representation 中为 `M_(g_lambda)>=0`。`G_R^(-1/2)` 与
`M_(g_lambda)` 都不能无条件地写成 bounded operator。脚本 marker 只检查有限
代数/标度接口，不认证无限维 form representation、dominated convergence 或
谱极限。

令

`k_z(x)=exp(zx-z^2/2-|z|^2/2)`.

Square-exponential tail 使所有固定 `z` 及局部参数导数落在相应的 form domain。
R142 的 coherent identity 为

`<k_z,A_lambda k_w>_gamma`
`=exp(conj(z)w-(|z|^2+|w|^2)/2) B_(mu_lambda)(conj(z)+w)`.

由于 `B_(mu_lambda)(z)=B_mu(sqrt(lambda)z)`，对实 `y`

`<k_(y/(2sqrt(lambda))), A_lambda k_(y/(2sqrt(lambda)))>=B_mu(y)`.

这是真正的 positive Rayleigh recovery，但 `B_mu(y)>0` 对 genuine probability
law 本身是自动事实，不是 rigidity。

## 2. coherent kernel 与 tensor positivity

R143 把 form-domain 问题转成直接的 measure Gram kernel：

`C_mu(z,w)=exp(conj(z)w-(|z|^2+|w|^2)/2)B_mu(conj(z)+w)`

`=int overline(k_z(x)) k_w(x) dmu(x)`.

Square-exponential moment 的精确定义域是整个 `C x C`；对任意有限
`z_1,...,z_m` 与复系数 `c_1,...,c_m`，

`sum_(i,j) conj(c_i)c_j C_mu(z_i,z_j)`
`=int |sum_j c_j k_(z_j)(x)|^2 dmu(x) >= 0`.

因此 `C_mu` 是整个复参数平面上的 Hermitian PSD kernel，不要求在 R143
中先假设 `mu << gamma`。参数微分的 Gram blocks 由局部 dominated
convergence 获得；在零点附近经 Gaussian triangular change of basis，它们
回到 Hermite/Hankel blocks。

任意 tensor power

`C_mu^(tensor m)(z,w)=prod_(a=1)^m C_mu(z_a,w_a)`

同样 PSD，且有 `mu^(tensor m)` 的直接 Gram 表示。Schur product 只给出
“PSD quotient => PSD product”；不能由 `C_mu=C_gamma circ D_mu` 反推
`D_mu(z,w)=B_mu(conj(z)+w)` PSD。

## 3. full-SF tensor identity：新定理

取

`r_j(theta)=sqrt(2/3) cos(theta+2pi(j-1)/3)`,

则 `||r(theta)||=1` 且 `r(theta) dot r(phi)=cos(theta-phi)`。在
`L^2(mu^3)` 中定义

`V_t(theta)=tensor_(j=1)^3 k_(t r_j(theta)/2)`.

对实参数，

`F_t(theta):=||V_t(theta)||^2 = prod_j B_mu(t r_j(theta))`.

所以 genuine full-SF 的 same-factor identity 是
`<F_t>=1`，但 tensor Gram 还给出更强的角自相关。令
`theta=alpha+delta/2`、`phi=alpha-delta/2`，则

`<V_t(alpha+delta/2),V_t(alpha-delta/2)>`
`=exp(-t^2(1-cos(delta))/4) F_(t cos(delta/2))(alpha)`.

再次对 `alpha` 平均并用 full-SF，得到

`< <V_t(alpha+delta/2),V_t(alpha-delta/2)>_alpha >`
`=exp(-t^2(1-cos(delta))/4)`.

若
`V_(t,n)=(2pi)^(-1) int V_t(theta) exp(-in theta)dtheta`，则 Fourier
比较给出 genuine Hilbert-space identity

`||V_(t,n)||^2=exp(-t^2/4) I_n(t^2/4)`，对所有 `n in Z`。

这说明 full-SF 精确固定了所有 angular mode 的 energy，且与 Gaussian 完全
相同。循环置换三个 tensor factors 给出 `S_3` sector 分解：

`<V_(t,n),V_(t,m)>=0` 若 `n != m (mod 3)`.

仍可能存在、且只可能存在的非 Gaussian 信息是同一 `mod 3` sector 中的
off-diagonal cross-harmonic coherence。

进一步令

`S_t=(2pi)^(-1) int |V_t(theta)><V_t(theta)| dtheta`.

它是 positive trace-class frame operator，`Tr(S_t)=1`，并且
`S_t=sum_n |V_(t,n)><V_(t,n)|`。由上面的 autocorrelation 可得精确 purity
identity

`Tr(S_t^2)=exp(-t^2/2) I_0(t^2/2)`
` +(2pi)^(-1) int exp(-t^2(1-cos(delta))/2)`
`    Var_alpha[F_(t cos(delta/2))(alpha)] ddelta`.

故

`Tr(S_t^2)-exp(-t^2/2)I_0(t^2/2)`
`=sum_(n != m, n=m mod 3) |<V_(t,n),V_(t,m)>|^2 >=0`.

这给出本轮的独立小结果：

**Coherent-Frame Bessel Spectrum and Purity-Defect Theorem.**

对 square-exponential genuine law，若 full-SF 成立，则所有 angular mode
energy 等于 Gaussian；非 Gaussianity只能位于同一 `mod 3` sector 的
cross-coherence，并且其总平方正好是上述 positive frame-purity excess。
若某个 `t>0` 达到 Gaussian purity equality，则方差项为零，`F_s(theta)=1`
在一个实区间内恒成立；实解析性与 `sum_j C(s r_j(theta))=0` 随即强制
`B_mu` 恒等于 1，从而得到 Gaussian。注意 full-SF 本身只给 purity excess
`>=0`，不提供 equality。

## 4. even-sector closure 尝试

取 `z_+=y/2`、`z_-=-y/2`。普通 coherent PSD 的二阶子式是

`[[B(y), exp(-y^2/2)], [exp(-y^2/2), B(-y)]] >= 0`,

因此只有

`B(y)B(-y)>=exp(-y^2)`.

目标所需的 deconvolved reflection positivity 是

`[[B(y),1],[1,B(-y)]] >= 0`,

等价于 `B(y)B(-y)>=1`。tensor antipode 也只把 Gaussian overlap 从
`exp(-t^2/2)` 变成同样的尺度关系；提高 tensor power 不会把这个下界升到
1。

若额外假设 `B(y)B(-y)>=1` 对全部实 `y`，则令
`C=log B`、`C_e=(C(y)+C(-y))/2`、`C_o=(C(y)-C(-y))/2`。full-SF 与
`theta -> theta+pi` 配对给

`1=< exp(H_e) cosh(H_o) >`,

其中 `H_e=sum_j C_e(t r_j)>=0`。故被积函数处处不小于 1，平均等于 1，
只能有 `H_e=H_o=0`，从而 `B=1`。这是一条完整的 conditional closure
theorem；新增的真正假设正是 Gaussian-deconvolved even-sector domination，
而不是普通 PSD。

更强的局部信息反而指向相反方向。假设 hypothetical non-Gaussian genuine
full-SF law 的第一个非零 Bargmann-log degree 为 `d>=3`。full-SF coefficient
identity 迫使 `d` 为 odd，并把低于 `2d` 的 even cumulant消掉；在 `2d` 阶

`A_(2d)c_(2d)+(1/2)<p_d^2>c_d^2=0`，`A_(2d)>0`。

于是

`log(B(y)B(-y))`
`=-(<p_d^2>/A_(2d)) c_d^2 y^(2d)+O(y^(2d+2))`，

因此任何 surviving non-Gaussian candidate 必须在小非零 `y` 上满足
`B(y)B(-y)<1`。所以从 full-SF 推出 `>=1` 会闭合大命题，但它不是普通
coherent positivity 能够提供的结论。

## 5. 严格失败机制与 witness

`C_mu=C_gamma circ D_mu` 中，`C_mu` 与 `C_gamma` 都 PSD，并不意味着
Schur quotient `D_mu` PSD。二阶层面允许的完整区间是

`exp(-y^2) <= B(y)B(-y) < 1`；这正好容纳上面的 hypothetical local
full-SF even-sector dip。

在 residual Fock space 中取 vacuum `e_0` 与
`f_6=(e_(+6)+e_(-6))/sqrt(2)`，定义

`T_epsilon=I-epsilon(|e_0><f_6|+|f_6><e_0|)`, `0<epsilon<1`。

其非平凡二维块 eigenvalues 为 `1+epsilon` 与 `1-epsilon`，故严格正；
它保持 rotation `2pi/3` 与 reflection 对称。其 coherent Q-symbol 具有

`Q_epsilon(r,theta)=1-epsilon c_6 r^6 exp(-r^2) cos(6theta)`，

角平均恒为 1，却在 reflection axis 上出现小于 1 的 anisotropy。这是
`OPERATOR-LEVEL STRICT OBSTRUCTION`：all-rank coherent PSD、`D_3` 对称和
Gaussian radial average 仍不能推出 pointwise even domination。它不是
`A^(tensor 3)` 的 scalar full-SF law，因此不能冒充 counterexample。

还有一个 genuine probability-level 的二维 residual witness：令
`Z=R(cos Theta,sin Theta)`，`R^2~chi^2_2`，而
`dP_Theta=(1+epsilon cos(6theta))dtheta/(2pi)`，`|epsilon|<1`。它具有
Gaussian radial law、centered covariance `I_2`、完整 `D_3` symmetry，并且
所有 common-rotation tensor multiplicative moments 都与 Gaussian 相同；但
其一维坐标满足

`E He_6(Z_1)=3epsilon/4`,
`B_(Z_1)(y)=1+epsilon*y^6/960+O(y^8)`。

当 `epsilon<0` 时，`B_(Z_1)(y)B_(Z_1)(-y)<1`。它不是 iid scalar residual
law，所以仍不是 genuine full-SF scalar counterexample；它只证明“Gaussian
residual radius + symmetry + common-rotation identities”不足以消灭角向
各向异性。真正尚未使用的特殊输入是 iid one-dimensional product
factorization。

## 6. rank / semiclassical 节点族

- 固定 coherent states：所有 finite Gram minors 只是 `C_mu>=0`，不产生
  Gaussian-deconvolved reflection positivity。
- Imaginary pair：`z_-= -iy/(2sqrt(lambda))`、
  `z_+=iy/(2sqrt(lambda))` 给
  `<k_(z_-),A_lambda k_(z_+)> = exp(-y^2/(2lambda))B_mu(iy)`；复相位仍
  受到指数小 overlap。
- Coherent chain：若相邻 overlap 至少为 `exp(-C^2/2)`，跨越距离
  `|y|/sqrt(lambda)` 至少需要 `m_lambda >= |y|/(C sqrt(lambda))`。
- Hermite/confluent：`n lambda -> tau` 才能把 fixed odd degree 的
  `lambda^(d/2)` entry 信号放回 `O(1)`；典型能量是 `n~lambda^(-1)`，但极限
  仍为自动正的 Toeplitz symbol `T_r(B_mu(2sqrt(tau)cos theta))`。
- Infinite-rank completeness 只给 identifiability：全部 real coherent data
  在解析条件下能确定 `B` 及其延拓，但解析延拓高度病态且不保持正性；
  `identifiability != positive coercivity`。

所以“再增大 rank”本身不是答案：mode energy 已被 full-SF 固定，剩余目标
是同一 `mod 3` block 的 cross-coherence；而复方向还要付出 coherent overlap
的半经典代价。

## 7. Positive Backward Tower 含义

对 `g_N=P_(q^N)h_N`，令 `lambda_N=q^N`。R142 的 positive relative form
满足

`<k_(y/(2q^(N/2))), A_N k_(y/(2q^(N/2)))>=B_(h_N)(y)`.

bottom `g_N -> 1` 没有消灭 top Bargmann shape，而是把它推到
`|z|~q^(-N/2)` 的 coherent radius和 `n~q^(-N)` 的 Hermite energy。当前
exact/Jacobi 控制是 `m=O(N)`，与恢复该 shape 所需的 exponential energy
存在明确的 linear-versus-exponential gap。

R143 把剩余逃逸再精确命名为
`exponential-energy residual angular cross-coherence escape`：mode energy
并没有逃逸，逃逸的是同一 `mod 3` sector 内的 off-diagonal coherence。
若 iid factorization 能推出这些 cross-coherences 全部消失，或能给出 frame
purity 的反向估计

`Tr(S_t^2)<=exp(-t^2/2)I_0(t^2/2)`,

则与 R143 的 `>=` 立即合成 equality，进而排除 genuine full-SF class 中
的 incompatible finite-depth towers。compatible single infinite tower 仍由
R138 的 common zero-free disk 独立解决；从 `B_mu/C_g` 到 spatial
`P_3 K_sp=0` 的桥仍未闭合。

## 8. 证据分层与下一轮

**PROVED（分析层，带明确 square-exponential/full-SF 假设）**

- `C_mu` 在整个复参数域上的 measure Gram 表示、PSD 与 tensor powers；
- coherent-frame autocorrelation；
- full-SF 固定 Gaussian Bessel mode energies；
- `S_3` block orthogonality；
- frame-purity defect identity与 purity equality rigidity；
- ordinary coherent reflection minor 只给 `B(y)B(-y)>=exp(-y^2)`；
- first non-Gaussian full-SF packet 的局部 even-sector reversal。

**CONDITIONAL**

- `RK=1` 到 genuine full-SF/all-row；
- `B_mu/C_g` rigidity 到 spatial `P_3K_sp=0`；
- 从 full-SF 自动推出 deconvolved `B(y)B(-y)>=1`；
- iid ridge-product factorization 消灭 residual cross-coherence。

**OBSTRUCTION**

- Schur deconvolution 不保 PSD；
- full-SF 固定 angular energies 而不固定同一 `mod 3` block 的 coherence；
- complex coherent overlap 的 `exp(-y^2/(2lambda))` 阻尼；
- operator-level 与 residual-vector witnesses 说明 radial/symmetry 数据不足。

**OPEN**

`genuine non-Gaussian full-SF law` 是否存在仍未解决。R143 后最小的
probability-level gap 是：给定 residual characteristic 的 iid ridge-product
结构

`Phi(u,v)=phi(u/sqrt(2)+v/sqrt(6))`
`*phi(-u/sqrt(2)+v/sqrt(6))*phi(-2v/sqrt(6))`,

并且所有 circular averages 满足 full-SF Gaussian identities，是否能强制
`Phi(u,v)=exp(-(u^2+v^2)/2)`，或至少强制 residual cross-coherence 消失。

下一轮唯一任务：**R144 — IID Ridge-Product Residual Angular Rigidity /
Bispectrum Coherence**。继续保持 scalar `RK=1` 桥接与 spatial `P_3K_sp`
接口的 `CONDITIONAL/OPEN` 标签。
