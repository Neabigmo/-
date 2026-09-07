# R123 — Global Bochner–Cauchy-Data Rigidity No-Go

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（factor-axis Bochner equivalence, Cauchy
hierarchy, matrix-valued conditional moments, explained-mean bound, radial flux
identity）；FORMAL；OBSTRUCTION；核心 OPEN。

## 1. 主判决

R123 检验了完整三维 `Bochner positivity + log-wave + Gaussian circular Dirichlet`
是否能单独排除非零 first normal Cauchy datum。结论是：不能。

最关键的 exact reduction 是：same-factor 三维 extension 的正定性与原一维
characteristic factor 的正定性等价。三维 Bochner 没有隐藏出比 one-body
probability realizability 更强的 positivity。

同时，所有由 matrix-valued Bochner、Schur complement、conditional variance、
quadratic wave-flux 产生的自然标量量，在 reflection 下都只看到 `N^2` 或两个
odd quantities 的 pairing。Gaussian circular boundary 只固定 residual radial
marginal，不能把这些能量固定为零。

因此 R123 正式把主问题收缩为

`one-body positive-definite characteristic`
`intersection`
`all-degree same-factor exact odd branch`。

## 2. Factor-axis Bochner equivalence（PROVED）

令

`w_j=(1/sqrt(3),v_j)`，其中 `|v_j|^2=2/3`、`v_i dot v_j=-1/3`（`i!=j`）。
于是 `w_i dot w_j=delta_ij`，`w_1,w_2,w_3` 是 mean–residual coordinates 中的
正交标准基。三维 extension 为

`tilde Phi(y)=prod_j phi(w_j dot y)`。

若 `phi` 是一维 characteristic function，则每个 `phi(w_j dot y)` 正定，乘积
仍正定。反过来，沿 factor axis `y=t w_1` 限制得

`tilde Phi(t w_1)=phi(t)phi(0)^2=phi(t)`。

正定函数在线性子空间上的限制仍正定，所以

`boxed{tilde Phi in PD(R^3) iff phi in PD(R)}`。

这条等价性是 R123 的第一条可发表级别的路线判决：任何真正排除 odd branch
的机制必须使用 one-body factorization 的全局可实现性，而不是再换一种三维
Bochner Gram minor。

## 3. Log-wave Cauchy hierarchy（PROVED）

令 `L=log(tilde Phi)`、`L_0(eta)=L(0,eta)`、
`N(eta)=partial_xi L(0,eta)`。R122 的 PDE 为

`partial_xi^2 L=(1/2)Delta_eta L`。

反复微分给出

`partial_xi^(2k)L(0,eta)=2^(-k)Delta_eta^k L_0(eta)`，

`partial_xi^(2k+1)L(0,eta)=2^(-k)Delta_eta^k N(eta)`。

所以 `L_0` 控制全部 even normal derivatives，`N` 控制全部 odd normal
derivatives。PDE 不会自动把 odd Cauchy datum 设为零；它只是传播该 datum。
更重要的是，exact radialization 只知道

`<exp(L_0(rho e_theta))>=exp(-rho^2/2)`，

并不知道完整的非径向 `L_0`。

## 4. Matrix-valued Bochner moment kernel（PROVED）

令 `M=(X_1+X_2+X_3)/sqrt(3)`、残差向量为 `R`，并定义

`F(eta)=E exp(i eta dot R)=exp(L_0(eta))`，
`J_1(eta)=E[M exp(i eta dot R)]`，
`J_2(eta)=E[M^2 exp(i eta dot R)]`。

则

`J_1=-i F N`，

而 log-wave equation 给出

`J_2=-F[1/2 Delta L_0+N^2]`。

这已经是一个超出 static Herglotz 的 nonlinear wave-flux，但 `N` 的第一次
纯粹出现仍是 algebraic square，而不是有符号的线性项。

条件于 `R=r` 定义

`mu_1(r)=E[M|R=r]`、`mu_2(r)=E[M^2|R=r]`。Bochner 的矩阵值版本给出

`[[1,mu_1(r)],[mu_1(r),mu_2(r)]] >= 0`，

等价于 `mu_2-mu_1^2=Var(M|R)>=0`。因此 Schur complement、conditional
variance 与其积分只会产生 `|J_1|^2`、variance 或 odd-odd pairing。

## 5. Global quadratic-Bochner parity lemma（ANALYTICALLY PROVED）

全局 reflection 为 `(M,R) -> (-M,-R)`，因此 `N`、`J_1` 等 odd normal datum
翻号，而 `J_2`、conditional variances、Schur determinants 和 quadratic Gram
energies 不变。

**命题（quadratic-Bochner parity no-go）。** 对任意由 matrix-valued Bochner
positivity 通过 quadratic form、Schur complement、conditional variance 或其
reflection-even radial 加权积分得到的 scalar flux，该 flux 对 `N -> -N` 是
reflection-even。它可以给 `N^2`、odd-odd pairing 或 magnitude bound，但不能给
universal reflection-stable 的线性符号条件 `N_0>=0` / `N_0<=0`。

这不是说偶能量永远不能证明 `N=0`；若 exactness 能额外把某个 Gaussian-baseline
zero energy 固定为零，当然可以。但 R123 证明现有 exact radial identity 并没有
提供这种 equality case。

## 6. Explained-mean energy 与精确 radial wave-flux（PROVED）

令 `H(q)=E[M|Q=q]`、`nu(dq)=1/2 exp(-q/2)dq`。在 exact radial branch，
`E_nu H=0`，且

`kappa_3=(sqrt(3)/2) E_nu[(Q-2)H(Q)]`。

由 `Var_nu(Q)=4` 的 Cauchy–Schwarz，

`boxed{E_nu H(Q)^2 >= kappa_3^2/3}`。

这说明非零 cubic 必然产生 positive explained-mean energy，但 positivity 只给
该量 `>=0`，没有给它等于零。相应地

`E Var(M|Q)=1-EH^2 <= 1-kappa_3^2/3`，

而 Gaussian 的 conditional variance 是 `1`；exact radialization 没有反向
不等式把它压回 `1`。

更细的 circular wave-flux identity 为

`H_2(rho)-exp(-rho^2/2)`
`=<F[1/2|grad L_0|^2-N^2-rho^2/2]>_theta`，

其中 `H_2(rho)=E[M^2 J_0(rho sqrt(Q))]`。这是 exact identity，但左侧含有
未由 Q-marginal 决定的 `M^2`-weighted transform；故不是 rigidity inequality。

## 7. Genuine Bochner/Dirichlet obstruction outside same-factor（PROVED）

取 `R~N(0,I_2)`，于是整个 residual vector 都是 Gaussian，特别
`Q=|R|^2~chi^2_2`。令

`H_eps(q)=eps(exp(-q)-1/3)`，并取
`M|Q=q ~ N(H_eps(q),1-H_eps(q)^2)`。

对足够小的 `eps`，这给 genuine positive、analytic、full `R^3`-PD joint law，
并满足 `EM=0`、`EM^2=1`；但

`E exp(-Q)=1/3`，`E[Q exp(-Q)]=2/9`，

所以

`E[M Q]=E[Q H_eps(Q)]=-4 eps/9 !=0`。

因此 `E[M J_0(rho sqrt(Q))]` 有非零 `rho^2` coefficient。该例不是项目反例，
因为它没有 same-factor product representation；它严格说明任何有效机制必须
使用 factorization，而不能只是更聪明的 Bochner positivity。

## 8. Formal same-factor obstruction 与路线降级（FORMAL / OPEN）

R104 的 nonzero-cubic all-degree formal branch 经过 R122 reconstruction 后，
仍可 coefficientwise 满足 same-factor、log-wave 与 exact circular Dirichlet
identity，同时

`N_0(rho)=-i c rho^2/(2sqrt(3))+O(rho^4) !=0`。

该 branch 是否来自 genuine positive-definite one-body characteristic function
仍未知，严格标记 FORMAL，不能作为项目反例。

由于 varying-bottom backward-OU tower 会从任何 genuine asymmetric exact
single law 自动生成，backward divisibility 也不能在此处单独提供额外 restriction。
因此 R123 将下一步从“三维 flux 搜索”转向 global one-body probability
realizability。

## 9. R123 证据等级与 R124

PROVED：factor-axis Bochner equivalence；log-wave even/odd Cauchy hierarchy；
matrix-valued conditional moment representation；explained-mean lower bound；
nonlinear circular flux identity；full-residual-Gaussian Bochner obstruction。

ANALYTICALLY PROVED：quadratic Bochner / conditional-variance flux 的
reflection-parity no-go。

FORMAL：R104 nonzero-cubic exact Cauchy branch。

OBSTRUCTION：三维 PD 不强于一维 PD；Gaussian residual Dirichlet 不控制 odd
normal datum；现有 flux 没有 Gaussian-baseline-zero 的 exact equality。

OPEN：`G_0(rho)=O(rho^4)` / `kappa_3=0`，等价于是否存在 genuine one-body
PD factor 实现 formal all-degree odd branch。

R124 固定为 **Uniform-Envelope Finite-Row Realizability Dichotomy**。固定
`c!=0`，令 `C_M(c)` 为 centered variance-one genuine laws，满足 cubic `c`、
前 `M` 个 exact rows，并统一满足 `E exp(X^2/8)<=2`。证明：若
`C_M(c)` 对所有 `M` 非空，则 tightness、uniform integrability、moment
determinacy 与对角化给出 genuine full-exact asymmetric law；反之若 asymmetric
genuine law不存在，则某个有限 `M(c)` 的集合必为空。真正要查的是固定 primitive
gap 的 finite-row constructions 能否保持统一 envelope；若不能，必须定位
positivity / fixed cubic / exact rows / uniform subGaussianity 中哪一项发生
global blow-up。
