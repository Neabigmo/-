# R121 — Angular Esscher–Fisher Cross Term 与 Angular-Mixture Coherence

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（结构表示，待本机 audit）；CONDITIONAL；
OBSTRUCTION；核心 OPEN。

## 1. 判决

R121 说明 `C_ang(q)` 有一个干净的 global quadratic-kernel 表示，但它不是正
quadratic form，而是正 Fisher/Herglotz metric 中的 off-diagonal cross term。因此
static angular positivity 只能控制 `|C_ang|` 的平方能量，不能给
reflection-stable sign。真正新增的是：引入 one-body Esscher tilt 后，mean-charge
tangent 可以显式进入 angular Fisher geometry；R101 的 static charges 并不控制
这个横向导数。

## 2. Angular Esscher family（PROVED）

对 R120 shell integrand

`F_theta(q,m)=prod_j f(m+sqrt(q)a_j(theta))`

定义

`A_theta(q,lambda)=int exp(lambda m)F_theta(q,m)dm`，
`Z(q,lambda)=avg_theta A_theta(q,lambda)`，
`w_(q,lambda)(theta)=A_theta(q,lambda)/Z(q,lambda)`。

`w_(q,lambda)dtheta/(2*pi)` 是严格正 angular probability law，且
`w_q=w_(q,0)` 是 `Q=q` 下的 residual-angle law。

若 `f_s(x)=exp(sx)f(x)/M_f(s)` 是 one-body Esscher tilt，则三因子乘积带有
`exp(s(X_1+X_2+X_3))=exp(3s Xbar)`，因此 `lambda=3s` 是 genuine
same-factor transverse direction，而不是外加参数。

## 3. 两个 angular scores 与 Fisher cross identity（PROVED）

定义 conditional angle harmonics

`u_k(q,lambda)=int exp(-3iktheta)w_(q,lambda)(theta)dtheta/(2*pi)`。

在 `lambda=0` 定义 mean-charge 与 radial-charge tangent

`alpha_k(q)=partial_lambda u_k(q,lambda)|_0`
`=E[(Xbar-h(q))exp(-3ikTheta)|Q=q]`，

`beta_k(q)=partial_q u_k(q)`
`=(1/(2q))E[(Sigma_R+q)exp(-3ikTheta)|Q=q]`。

`alpha_0=beta_0=0`。在 angular law 上定义 scores

`S_lambda=partial_lambda log w_(q,lambda)|_0=m_theta(q)-h(q)`，
`S_q=partial_q log w_q=(r_theta(q)+q)/(2q)`。

因 exact radial row mass 给 `E_w r_theta=-q`，所以

`boxed{C_ang(q)=Cov_w(m_theta,r_theta)=2q I_ang_(lambda q)(q)}`，

其中

`I_ang_(lambda q)=E_w[S_lambda S_q]`。

这给出了 R121 所需的明确 global representation，但它是非对角 Fisher 元素，
没有预定符号。

## 4. Positive Toeplitz/Herglotz representation（PROVED）

令 `c_n(q)` 为 `1/w_q` 的 Fourier coefficients。严格正性使 Toeplitz operator

`T_(1/w_q)=[c_(k-l)]_(k,l in Z)`

正定，因为对任意有限 Fourier polynomial `P`：

`<P,T_(1/w_q)P>=int |P(exp(3itheta))|^2/w_q(theta)dtheta/(2*pi)>=0`。

于是 angular Fisher entries 写为

`I_ang_(lambda lambda)=<alpha,T_(1/w)alpha> >=0`，
`I_ang_(q q)=<beta,T_(1/w)beta> >=0`，

而 cross term 是

`boxed{C_ang(q)/(2q)=<alpha(q),T_(1/w_q)beta(q)>}`。

因此自动得到的只有 Cauchy–Schwarz 能量界

`boxed{|C_ang(q)|^2 <=4q^2 I_ang_(lambda lambda)I_ang_(q q)}`。

不能诚实写成 `C_ang=sum lambda_k|charge_k|^2`、`lambda_k>=0`；原因是 reflection
parity：`C_ang` 翻号，而正 square energy 不翻号。

## 5. Reflection 与 Fisher chain rule（PROVED）

对 `check f(x)=f(-x)`：

`A_theta^check(q,lambda)=A_(theta+pi)^f(q,-lambda)`，
`w_(q,lambda)^check(theta)=w_(q,-lambda)^f(theta+pi)`。

所以

`S_lambda^check(theta)=-S_lambda^f(theta+pi)`，
`S_q^check(theta)=S_q^f(theta+pi)`，

从而

`I_ang_(lambda q)^check=-I_ang_(lambda q)^f`，
`I_ang_(lambda lambda)^check=I_ang_(lambda lambda)^f`，
`I_ang_(q q)^check=I_ang_(q q)^f`，

及

`boxed{C_ang^check(q)=-C_ang^f(q)}`。

R120 的 within/between 分解正是 Fisher information chain rule：

`h'=I_joint_(lambda q)`，

`h'=E_w[I_(lambda q)^(m|theta)]+I_ang_(lambda q)`，

等价地

`2q h'=E_w[Cov(Xbar,Sigma_R|q,theta)]+C_ang(q)`。

两项都是 off-diagonal Fisher terms；Fisher positivity 只给各自 Cauchy–Schwarz
界，不给它们相对符号，也不强迫它们抵消。

## 6. radial exactness 与 static Herglotz 的精确边界（PROVED / OBSTRUCTION）

在 polar residual coordinates：

`p_f(r,theta)=(1/(2*pi))exp(-r^2/2)w_(r^2)(theta)`。

full exactness 只固定

`u_0(q)=1` 对所有 `q`，并不直接给 `u_k(q)=0`（`k!=0`）。高 angular modes
仍只受 positivity、same-factor realizability、analyticity 与 R101 类型 Herglotz
inequalities 约束。

R121 的新 tangent `alpha_k=partial_lambda u_k|_0` 是 Esscher mean-charge tangent。
由于 Esscher-tilted one-body law 一般不再 full-exact，不能对 exact identity
直接求 `lambda` 导数并把结果置零；那会偷偷加入“exact class 对 Esscher tilt
一阶稳定”的强假设。事实上 radial law 的 Esscher 一阶导数满足

`partial_s log p_(Q,s)(q)|_0=3h(q)`。

若额外假设该 radial density 在 Esscher 方向一阶不动，则直接得到 `h=0`；这只是
原 annihilation 的强重写，不是独立桥梁。

## 7. 有限行 obstruction 与条件性小引理（OBSTRUCTION / CONDITIONAL）

R104 formal recursion 对任意有限 `M` 允许选择小非零 `kappa_3=c` 并满足 radial
exact Taylor equations through degree `M`。以 bounded real-analytic、二阶导有界
的 Hermite 对偶函数构造有限维 exponential family，可由 inverse-function theorem
实现这些 finite rows，同时保持 genuine probability、strict positivity、
real-analytic、strict log-concavity 与 same-factor。它们不是 all-degree exact
project counterexample，只证明 R121 必须使用真正的无限阶 angular coherence。

一个精确但条件性的接口是：若 genuine exact class 满足

`I_joint_(lambda q)(q)=0` a.e. `q`

（Esscher–Radial Fisher Orthogonality），则 `h'=0`、`h=0`、`kappa_3=0`；但这
就是目标的 information-geometric 重写。只假设 `I_ang_(lambda q)=0` 还不够，
因为 within-angle cross term 仍可能非零。

## 8. R121 判决与 R122

### 已确立

- angular Esscher family 是 genuine same-factor transverse direction；
- `C_ang` 是 positive Toeplitz/Fisher metric 中的 cross term；
- static Herglotz/Fisher positivity 只能给 `|C_ang|` 的平方界；
- reflection 精确翻转 cross term、保持 diagonal energies；
- R120 within/between 分解是 Fisher chain rule；
- radial exactness 只固定 angular zero mode；
- 任意 finite exact angular rows 加 analytic/strict-log-concave same-factor 仍不足。

### 仍为 OPEN

`C_ang(q)` 是否在 genuine all-degree exact class 中有特殊 cancellation，或
`h'(q)=0`，进而 `kappa_3=0`，仍未关闭。

### R122 最小命题

研究 **Same-Factor Normal-Derivative Reconstruction Lemma**。定义 residual Fourier
plane trace

`Phi(u,v)=phi(u)phi(v)phi(-u-v)`，并在统一 zero-free neighborhood 定义
`s(x)=phi'(x)/phi(x)`。same-factor 结构给

`boxed{s(x)=-partial_v log Phi(-x,v)|_(v=0)}`

（centeredness 给 `s(0)=0`）。进一步

`Psi(u,v)=(1/(3i))[s(u)+s(v)+s(-u-v)]Phi(u,v)`

可由 residual trace 的 tangential boundary derivatives 重构。R122 只问：将 R121
的 Esscher mean-charge tangent 用这一非局部 trace functional 完全改写后，
Gaussian radialization + positive-definiteness + same-factor functional equation
是否产生 static Herglotz 看不到的 first-harmonic identity？若仍只有 reflection-odd
bilinear pairing，则可正式关闭 R101/Herglotz angular-coherence 主路线。

## 9. 证据等级

`audit_r121.py` 只核验 Esscher score/cross scaling、reflection parity、Toeplitz
quadratic positivity 的代数接口与 `Phi` 法向导数重构公式。conditional
disintegration、Fisher chain rule 的正则性与 finite-row exponential-family
obstruction 保持 ANALYTICALLY PROVED / CONDITIONAL / OPEN。
