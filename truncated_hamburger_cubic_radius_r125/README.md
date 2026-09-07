# R125 — Truncated-Hamburger Cubic Radius: Asymptotic Exactness and No-Go

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（finite-row radius, relaxed compactness,
asymptotic exactness, Fourier window, Laguerre–Christoffel anti-atomicity）；
CONDITIONAL；FORMAL；OBSTRUCTION；核心 OPEN。

## 1. 主判决

R125 没有证明 `Gamma_M -> 0`。但它把 genuine finite-row hierarchy 与截断
Hamburger relaxation 的关系完全厘清，并得到三个可独立引用的 finite-row 结果：

1. `lim Gamma_M=lim GammaHat_M=Gamma_infty`，其中 `Gamma_infty` 是 genuine
   full-exact class 的最大 cubic skew；
2. 前 `M` rows 给出 growing Fourier window
   `|E J_0(t sqrt(Q))-e^(-t^2/2)| <= 2|t|^(2M)/(2^M M!)`；
3. 令 `n=floor(M/2)`，则 exact rows 给出
   `P(Q=0)<=1/(n+1)`，即 iid law 的 atom collision probability 被压低。

这些约束仍没有 first-harmonic sign 信息，也没有推出 `kappa_3=0`。真正剩余
问题是 `Gamma_M -> 0`，它与 single-law cubic exclusion 同层级。

## 2. 有限截断 Hamburger 的严格边界（PROVED）

令 `y=(y_0,...,y_{2M})`，`H_M(y)=[y_{i+j}]_{i,j=0}^M`。必须区分：

`H_M(y)>=0` 并不保证单个有限 truncation 有 representing probability measure。

反例为

`(y_0,y_1,y_2,y_3,y_4)=(1,0,0,0,1)`，

其 `H_2=diag(1,0,1)>=0`，但 `y_2=0` 的任何 representing law 都满足
`X=0` a.s.，因而不可能有 `y_4=1`。

有限层的 ghost gap 只能出现在 singular non-flat locus：

`H_M>=0`、`H_M` singular、`rank(H_M)>rank(H_(M-1))`。

若 `H_M` positive definite，则可扩展为 Hamburger moment sequence；若 singular
且 flat，则有 finite-atomic representing measure。无论如何，单个 finite PSD
truncation 不能被偷当成概率律。

## 3. Exact-row triangular structure（PROVED）

令

`q(x_1,x_2,x_3)=(2/3)(sum_j x_j^2-sum_(i<j)x_i x_j)`，
`Q=q(X_1,X_2,X_3)`。

把 `q^r` 展开成 monomials 后，row
`R_r=E Q^r-2^r r!` 是 `y_0,...,y_{2r}` 的有限多项式。最高 moment 只来自
三个纯平方项，因此

`R_r(y)=(2^r/3^(r-1))y_(2r)+P_r(y_0,...,y_(2r-1))-2^r r!`。

所以新最高 even moment 对每个 row 都是 affine 的；formal odd freedom 被藏在
lower moments 中。

## 4. 两个 finite cubic radii 与 extremizers（PROVED）

定义 genuine class

`E_M={mu: EX=0, EX^2=1, R_1=...=R_M=0}`，
`Gamma_M=sup_(mu in E_M)|EX^3|`。

定义截断 relaxation `T_M` 为

`y_0=1,y_1=0,y_2=1`，`H_M(y)>=0`，`R_r(y)=0 (r<=M)`，
`0<=y_(2r)<=4^r r!`，

并令 `GammaHat_M=sup_(y in T_M)|y_3|`。显然
`Gamma_M<=GammaHat_M`，但有限层不必相等。

`T_M` 是 compact：even coordinates 有 caps，Hankel `2x2` minors 给
`|y_(2r+1)|^2<=y_(2r)y_(2r+2)`；因此 `GammaHat_M` 取得最大值并随 M 不增。

对 `M>=2`，R124 bootstrap 给 genuine `E|X|^(2M)<=4^M M!`，所以
`Gamma_M` 也取得最大值。Richter–Tchakaloff 给一个至多 `2M+1` 原子的 law
保留 moments `0,...,2M`，因而保留所有前 M rows 和 cubic objective。

## 5. R125-A：genuine 与 relaxed 半径的渐近完全相同（PROVED）

令

`Gamma_infty=sup{|kappa_3(mu)|: mu genuine, Q_mu~chi^2_2}`。

R124 的 envelope-free compactness 对 genuine extremizers 给

`lim_M Gamma_M=Gamma_infty`。

对 `T_M` 的 maximizers做 coordinate diagonal extraction。极限序列满足所有
finite Hankel matrices PSD、所有 rows、所有 moment caps；Hamburger theorem 给
genuine measure，caps 给 Carleman 和 `E exp(X^2/8)<=2`，R124 analytic upgrade
给 full exact law。因此

`boxed{lim_M GammaHat_M=lim_M Gamma_M=Gamma_infty}`。

特别 `GammaHat_M-Gamma_M->0`，但这不意味着每个有限 `H_M` truncation 都
representable；ghost gap 只在有限层可能存在，渐近上消失。

若存在固定 `epsilon>0` 使 `GammaHat_M>=epsilon` 对所有 M，则 compactness
直接给 genuine full-exact law with `|kappa_3|>=epsilon`。所以固定非零 cubic
不能永远只是形式分支而同时通过全部 finite row/cap/Hankel constraints。

## 6. R125-B：没有固定 finite degree 能 annihilate cubic（PROVED / OBSTRUCTION）

已审计的 R115/R120 finite-row genuine perturbations 说明每个固定 M 在 Gaussian
附近都有 sufficiently small nonzero-cubic genuine law。因此 `Gamma_M>0` 对
每个有限 M；任何固定阶 SOS/Hankel certificate 都不能直接推出 `y_3=0`。

若最终 cubic exclusion 成立，certificate 必须随 `M` 累积，等价于
`Gamma_M downarrow 0`。这正是 R125 没有关闭的 OPEN，而不是某个固定阶的
local positivity gap。

## 7. R125-C：growing Fourier window（PROVED）

对 genuine `mu in E_M`，令 `Y_theta=sum_j a_j(theta)X_j`。前 M rows 使 angular
averaged moments 到 degree `2M` 与标准 Gaussian 一致。对 `e^(ix)` 使用 degree
`2M-1` Taylor remainder，得到

`|E J_0(t sqrt(Q))-e^(-t^2/2)|
 <=2|t|^(2M)/(2^M M!)`。

由 `M!>=(M/e)^M`，对任意 `0<alpha<sqrt(2/e)` 和 `|t|<=alpha sqrt(M)`，

`sup |E J_0(t sqrt(Q))-e^(-t^2/2)|
 <=2(e alpha^2/2)^M`。

这是指数级 growing-window radial approximation，但它只逼近已经 OPEN 的 exact
radial identity；不能从 approximation 本身推出 cubic zero。

## 8. R125-D：Laguerre–Christoffel anti-atomicity（PROVED）

令 `n=floor(M/2)`，以 `x=q/2` 写标准 Laguerre polynomials `L_k(x)`，并令

`P_n(q)=(1/(n+1))sum_(k=0)^n L_k(q/2)`。

相对于 `chi^2_2` measure，`P_n(0)=1` 且

`E[P_n(Q)^2]=1/(n+1)`。

因为 `1_{Q=0}<=P_n(Q)^2`，得到

`boxed{P(Q=0)<=1/(floor(M/2)+1)}`。

在 iid 情形 `Q=0` 等价于 `X_1=X_2=X_3`，故

`sum_x mu{x}^3<=1/(floor(M/2)+1)`，

`max_x mu{x}<= (floor(M/2)+1)^(-1/3)`。

若 law 有 N 个 atoms，则 `sum p_i^3>=1/N^2`，所以
`N>=sqrt(floor(M/2)+1)`。高 exactness 强制 atomic realizers 越来越 diffuse，
但连续 asymmetric law 本来就满足 `P(Q=0)=0`，所以该结果不控制 skew。

## 9. 证据等级与 R126

PROVED / ANALYTICALLY PROVED：finite-row triangular moment structure；两类半径
的 extremizer；relaxed 与 genuine 半径渐近完全相同；固定非零 gap 的 no-purely-
formal escape；growing Fourier window；Laguerre–Christoffel anti-atomicity。

CONDITIONAL：若 cubic exclusion 成立，则 `Gamma_M->0` 和 `GammaHat_M->0`；
这只是等价重写，不是本轮证明。

FORMAL：R104 odd all-degree branch 可通过任意预设 finite rows，但是否通过所有
genuine positivity layers未知。

OBSTRUCTION：finite `H_M>=0` 可含 singular non-flat ghosts；Fourier window 和
anti-atomicity没有 first-harmonic sign；任何 fixed finite degree 都不能 annihilate
cubic。

OPEN：`Gamma_M->0`，等价地 `GammaHat_M->0`、`Gamma_infty=0`，即非零 formal
odd exact branch 是否能无限穿过 genuine Hamburger cone。

R126 固定为 **Singular-Ghost Elimination at the Cubic Extremum**：令
`y^(M)` 是 `T_M` 中使 `y_3` 最大的 maximizer，研究能否选取它满足
`H_M(y^(M))>0` 或 flatness `rank H_M=rank H_(M-1)`；若不能，构造 singular
non-flat extremizing branch并量化 `GammaHat_M-Gamma_M`。目标是把 finite ghost
layer 本身变成可检验的下一层 obstruction。
