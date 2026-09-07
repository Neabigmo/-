# R122 — Same-Factor Normal Derivative, Bochner Trace, and the First-Harmonic Obstruction

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（trace reconstruction, compatibility, log-wave
equation, charge/Hankel interfaces, Schwarz budget, tangent obstruction）；
CONDITIONAL；FORMAL；核心 OPEN。

## 1. 判决

R122 把 R121 的 Esscher mean-charge tangent 完全拉回 same-factor residual trace。
这确实增加了一个此前 static radial/Herglotz 表述没有显式展示的对象：
reflection-odd 的法向 Cauchy datum。但是，same-factor functional equation 只把
该 datum 重写成 Dirichlet trace 的非局部 Dirichlet-to-Neumann / harmonic-lowering
functional；Gaussian radialization 与 Bochner positive-definiteness 目前只给
reflection-even 的 quadratic budget，尚未给出 annihilation identity。

因此本轮正式关闭“只靠 R101 static Herglotz / residual trace 重构即可消灭
first harmonic”的路线，但不关闭主命题。下一轮转向 full 3D Bochner–Cauchy-data
rigidity：寻找真正依赖 joint positive-definiteness 的 nonlinear wave-flux 或
conditional-variance zero identity。

## 2. 二维 residual trace 的 exact normal reconstruction（PROVED）

令

`Phi(u,v)=phi(u)phi(v)phi(-u-v)`，`K=log(phi)`，`s=K'=phi'/phi`，并在
统一 zero-free neighborhood 内取解析分支。沿 `u=-x` 有

`Phi(-x,v)=phi(-x)phi(v)phi(x-v)`。

所以 centeredness 给 `s(0)=0`，且

`partial_v log Phi(-x,v)|_(v=0)=s(0)-s(x)=-s(x)`，

即

`boxed{s(x)=-partial_v log Phi(-x,v)|_(v=0)}`。

积分得到

`K(x)=-int_0^x partial_v log Phi(-t,v)|_(v=0) dt + K(0)`，

因此 same-factor trace 在局部确实确定 one-body factor（归一化由
`phi(0)=1` 固定）。若定义 `d=-s`，则 full interior compatibility 为

`partial_u log Phi(u,v)=d(-u-v)-d(u)`，

`partial_v log Phi(u,v)=d(-u-v)-d(v)`。

这不是新的 positivity inequality，而是 factorization 的可积性/相容性条件。

## 3. Mean-charge trace 与三维 log-wave equation（PROVED）

取 equilateral vectors

`v_j=sqrt(2/3)(cos(theta+2*pi*j/3), sin(theta+2*pi*j/3))`，

并定义

`tilde Phi(xi,eta)=prod_j phi(xi/sqrt(3)+v_j dot eta)`，
`tilde L=log(tilde Phi)`。

由于 `sum_j v_j v_j^T=I_2` 与 `|v_j|^2=2/3`，same-factor structure 给出

`boxed{Delta_eta tilde L=2 partial_xi^2 tilde L}`。

在 `xi=0` 的 normal datum 为

`partial_xi tilde L(0,eta)=(1/sqrt(3))sum_j s(v_j dot eta)`。

若 `Psi` 表示 mean-charge weighted residual transform，则

`boxed{Psi(eta)=Phi(eta)/(i*sqrt(3)) partial_xi tilde L(0,eta)}`

（等价地 `Psi=(Phi/(3i))*sum_j s(v_j dot eta)`，具体符号取决于 characteristic
约定）。所以 `Phi` 是 Dirichlet datum，而 `Psi` 是同一 factorization 强制的
first normal Cauchy datum；它在全局 reflection 下变号。

log-wave equation 的关键限制是二阶 PDE 对 even normal derivatives 的约束，
并不自动决定 reflection-odd 的 first normal datum。圆周 Dirichlet 平均也不足以
恢复该非径向 Cauchy datum。

## 4. R101 charges 与 mean-charge charges 的精确接口（PROVED）

在 residual polar coordinates，令 `Q=r^2`，`Theta` 为 residual angle，并记

`u_k(q)=E[exp(-3ik Theta)|Q=q]`，
`g_k(q)=E[Xbar exp(-3ik Theta)|Q=q]`，
`h(q)=E[Xbar|Q=q]`，
`alpha_k(q)=g_k(q)-h(q)u_k(q)`。

若 `F_k` 是 `Phi` 的 `3k`-harmonic Fourier charge，`G_k` 是 `Psi` 的对应
charge，则二维 Hankel transform 给

`F_k(rho)=i^(3k) H_(3k)[exp(-q/2)u_k(q)](rho)`，

`G_k(rho)=i^(3k) H_(3k)[exp(-q/2)g_k(q)](rho)`。

因此 `Phi -> Psi -> {u_k,g_k} -> {alpha_k}` 可由同一 trace 与 Hankel inversion
恢复。重要边界是：R101 的 static charge tower 对应完整 angular Fourier trace，
但并不等同于 `Psi` 的 mean-charge tower，也不等同于 `P_3 K` 的 annihilation。

在零阶 mean-charge mode，exact radial law `Q~chi^2_2` 只给

`G_0(rho)=E[Xbar J_0(rho sqrt(Q))]`

以及小频率展开

`boxed{G_0(rho)=-kappa_3 rho^2/6+O(rho^4)`。

所以目标 `kappa_3=0` 正好等价于把该 reflection-odd normal mode 从二阶开始
压掉；R122 没有找到这样的 exact identity。

## 5. Log first-harmonic lowering（PROVED）

令 `P_1^log(rho)=<exp(-3i theta) log Phi_rho(theta)>`，`E=rho partial_rho`，
并令 `N_0(rho)=<partial_xi tilde L(0,rho e_theta)>`。在奇次幂上定义

`M(rho^(2m+1))=sqrt(2)((m+1)(m+2)/m)rho^(2m+1)`，`m>=1`。

则

`boxed{N_0(rho)=rho^(-1) M P_1^log(rho)}`。

特别，若

`P_1^log(rho)=-i kappa_3 rho^3/(12 sqrt(6))+O(rho^5)`，

则

`boxed{N_0(rho)=-i kappa_3 rho^2/(2 sqrt(3))+O(rho^4)`。

这说明 same-factor reconstruction 把 cubic charge transport 到 normal datum，
而不是把它消掉；该算子是 reflection-odd 的非局部 harmonic-lowering operator。

## 6. Exact Schwarz budget（PROVED）

在 exact radial branch，`E[Xbar^2]=1/3`，且

`E[J_0(rho sqrt(Q))]=exp(-rho^2/2)`，

`E[J_0(rho sqrt(Q))^2]=exp(-rho^2) I_0(rho^2)`。

因此 Cauchy–Schwarz 给出

`boxed{|G_0(rho)|^2 <= (1/3) exp(-rho^2)(I_0(rho^2)-1)`

`=rho^4/12+O(rho^6)`。

该界与 reflection 偶，只有 magnitude budget，没有固定 sign 或 zero。它不能
推出 `G_0=O(rho^4)`。

## 7. Genuine tangent obstruction（ANALYTICALLY PROVED / OBSTRUCTION）

取 `a!=b`，

`c=a exp(-a^2/2)/(b exp(-b^2/2))`，
`psi(x)=sin(ax)-c sin(bx)`。

则高斯基点满足

`E_gamma[X psi(X)]=0`，但

`E_gamma[H_3(X) psi(X)]=a(b^2-a^2)exp(-a^2/2)!=0`。

在 exponential family

`f_eps proportional exp(-x^2/2+eps psi(x)+alpha(eps)x+beta(eps)(x^2-1))`

中由 IFT 选 `alpha,beta` 保持 centered、variance one。由于一阶约束与 `psi`
的奇偶性，`alpha'(0)=beta'(0)=0`，故 `kappa_3` 的一阶导数非零；小参数时仍
可保持 positive、analytic、strictly log-concave、same-factor、positive-definite。

但对任意有界 radial test `F(Q)`，基点处

`d/d eps E_eps[F(Q)]|_0=E_gamma^3[F(Q) sum_j psi(X_j)]=0`

因为 `Q` 偶而 score 为全局 reflection-odd。于是所有 radial observables 的一阶
变化看不到该 normal direction，而 mean-charge datum 一阶变化非零。这是真实的
analytic tangent obstruction，不是 all-degree exact counterexample；一般在二阶
就会离开 exact radial manifold。

## 8. 证据等级、路线判决与 R123

### PROVED / ANALYTICALLY PROVED

- same-factor residual trace 的 normal derivative reconstruction；
- interior tangential compatibility；
- 三维 same-factor log-wave equation；
- `Phi`、`Psi`、conditional mean-charge 与 Hankel transform 的接口；
- log first-harmonic lowering；
- exact Schwarz bound；
- strict-log-concave analytic tangent obstruction。

### CONDITIONAL / FORMAL

- 若额外假设 exact class 在 Esscher direction 一阶稳定，则 `h=0`；这是目标的
  重写，不是独立证明；
- 若 R104 formal all-degree branch 被实现为 genuine probability，则可保留非零
  cubic，但当前仍只是 FORMAL，不能作为反例。

### OPEN

`G_0(rho)=O(rho^4)`，等价地 `kappa_3=0`，仍未证明。

R123 固定为 **Global Bochner–Cauchy-Data Rigidity Lemma**：对完整三维联合
特征函数 `tilde Phi`，结合 log-wave equation、Gaussian circular Dirichlet
condition 与 Bochner positive-definiteness，寻找 reflection-even quadratic
budget 之外的 nonlinear wave-flux / conditional-variance zero identity，判断
能否排除非零 cubic normal Cauchy datum。若所有 natural flux 仍只含 `N^2`，则
关闭 Fourier/Herglotz/normal-derivative 路线，转向 global one-body probability
realizability。
