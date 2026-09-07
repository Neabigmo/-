# R108 — Four-point bispectrum separation and shear-cocycle interface

日期：2026-09-07

本轮承接 `bochner_breakdown_obstruction_r107`，把三点
difference/autocorrelation 条件升级为四点 multiplicative Bochner Gram，并把
剩余问题压缩到一个明确的 shear-bispectrum alignment lemma。

## 1. 核心结论

### PROVED / ANALYTICALLY PROVED — 四点层首次穿透 `psi`

取

`a_1=sqrt(2/3) cos(theta)`,
`a_2=sqrt(2/3) cos(theta+2*pi/3)`,
`a_3=sqrt(2/3) cos(theta-2*pi/3)`,

于是 `a_1+a_2+a_3=0`、`sum a_j^2=1`。令

`x=a_1 y`, `z=-a_2 y`, `U=exp(ixX)`, `V=exp(izX)`,

并写

`u=phi(x)`, `v=phi(z)`, `w=phi(x+z)`, `c=phi(x-z)`。

对 `U-u,V-v,UV-w` 的 covariance Gram 为

`Gamma_4 = [[1-|u|^2, c-u*conj(v), conj(v)-u*conj(w)],
            [conj(c)-conj(u)*v, 1-|v|^2, conj(u)-v*conj(w)],
            [v-conj(u)*w, u-conj(v)*w, 1-|w|^2]] >= 0`.

若上方 `C` 正定，令

`q=(conj(v)-u*conj(w), conj(u)-v*conj(w))^T`，

则新约束是

`1-|w|^2-q^* C^(-1)q >= 0`。

这是 genuine characteristic-function positivity，不需要 full exactness。

## 2. Bispectrum 坐标与 exact identity

令

`s=a_2 y`, `t=(a_1-a_2)y`。

则 `a_1 y=s+t`、`a_2 y=s`、`a_3 y=-(2s+t)`，并且固定 `y` 的椭圆为

`6s^2+6st+2t^2=y^2`。

定义 translation-invariant bispectrum

`B(s,t)=phi(s) phi(t) conj(phi(s+t))`。

原 exact identity 正好变成

`<B(s,s+t)>_{E_y}=exp(-y^2/2)`。

也就是说 exactness 固定的是一个 sheared bispectrum 的 ellipse average，
而不是 `B(s,t)` 本身。

取四点 Gram 的 `U,UV` principal minor，得到

`1+2 Re B(s,t)-psi(s)-psi(t)-psi(s+t) >= 0`。

角向平均后，令

`Q_4(y)=Re <B(s,t)>_{E_y}`、
`H_c(y)=<psi(c y cos(theta))>_theta`、`rho=sqrt(2/3)`，有

`1+2 Q_4(y)-2 H_rho(y)-H_sqrt2(y) >= 0`.

这已经是 phase-sensitive 的四点必要条件。

## 3. `Q_4` 不能由 `psi=|phi|^2` 重构

R107 的 symmetric/asymmetric homometric pair 在 OU smoothing 后仍有完全相同
的 `psi`，但 `kappa_3` 分别为 `0` 与 `lambda^(3/2)`，且 `kappa_6` 相同。
`Q_4` 对应 coefficient multiset

`b^(Q)=(-a_1,a_2,a_1-a_2)`，

其和为零且

`< (sum_j (b_j^(Q))^3)^2 >= 5/4`。

因此

`Q_4,asym-Q_4,sym = -5 lambda^3 y^6/288 + O(y^8)`.

故四点 companion observable 严格不能是 difference-law/`psi` 的 functional。

## 4. 完整 Schur 残差与 phase cocycle

令 `f_j=phi(a_j y)`、`h=phi((a_1-a_2)y)`。清除 Schur 分母后，

`Delta_4 = 1-|c|^2-|w|^2-2|u|^2-2|v|^2
          +|u|^4+|v|^4-2|u|^2|v|^2+|c|^2|w|^2
          +4 Re(c conj(u)v)+4 Re(uv conj(w))
          -2 Re(c conj(u)^2 w)-2 Re(c v^2 conj(w))`.

full exactness 消去 `Re <c conj(u)v>`，reflection 对称使另一个末端相位项平均
相等。定义

`T_4(y)=Re < conj(f_3) conj(f_1)^2 h >`，

以及

`mathfrak Q_4[phi](y)=Q_4(y)-T_4(y)`。

那么完整 angular-averaged Schur inequality可写成

`P_psi(y)+4 exp(-y^2/2)+4 mathfrak Q_4[phi](y) >= 0`，

其中

`P_psi=<1-psi_3-psi_h-2psi_1-2psi_2
          +psi_1^2+psi_2^2-2psi_1 psi_2+psi_3 psi_h>`

完全由 `psi` 决定。因此 `mathfrak Q_4` 是真正的 signed phase observable。

对 `T_4` 的 coefficient multiset

`b^(T)=(-a_3,-a_1,-a_1,a_1-a_2)`

有

`< (sum_j (b_j^(T))^3)^2 >= 4/3`，

故同一 R107 pair 给出

`T_4,asym-T_4,sym = -lambda^3 y^6/54 + O(y^8)`，

从而

`mathfrak Q_4,asym-mathfrak Q_4,sym
  = lambda^3 y^6/864 + O(y^8)`.

### R108-A / R108-C — PROVED

`Q_4` 以及完整 `mathfrak Q_4` 都不能由 `psi` 或 difference law 重构。
三点 autocorrelation ambiguity 在四点层第一次被 bispectrum phase 穿透。

在 `phi` 的局部零自由区写 `phi(r)=|phi(r)| exp(i vartheta(r))`，令

`delta(s,t)=vartheta(s)+vartheta(t)-vartheta(s+t)`。

在 `psi(s)>0` 时，`T_4` 的 phase 正是
`delta(s,t)-delta(s,s+t)`；四点 Gram 测量的是 shear
`(s,t) -> (s,s+t)` 下相邻 bispectrum cocycle 的相容性。

## 5. 当前能关闭的条件接口

### R108-D / R108-E — PROVED conditional interface

若局部有 `B(s,t)>0`，则 `delta(s,t)=0`，连续 Cauchy 方程给
`vartheta(t)=ct`；centered 条件 `phi'(0)=i E X=0` 迫使 `c=0`，从而
`P_3K=0`。更贴合完整四点残差地，若在原点邻域成立

`delta(s,t)=delta(s,s+t)`，

则

`vartheta(t+2s)-2 vartheta(t+s)+vartheta(t)=0`。

对 `s` 二次求导得到 `vartheta''(t)=0`，再由 centered 得 `vartheta=0`，
故同样推出 `P_3K=0`。

这两个接口是已证明的；尚未证明的是 full exact ellipse average 与
`Gamma_4 >= 0` 是否足以推出该 pointwise shear alignment。

## 6. Gaussian anchor 与首阶边界

`Q_4` 是 anisotropic three-copy transform。若 `X_1,X_2,X_3` 独立，

`Q_4(y)=E J_0(y sqrt(Ecal))`，

`Ecal=(2/3)(X_1^2+X_1X_2-3X_1X_3+X_2^2-3X_2X_3+3X_3^2)`。

该 quadratic form 的 eigenvalues 为 `0,1/3,3`。Gaussian law 给出闭式

`Q_4^G(y)=exp(-5y^2/6) I_0(2y^2/3)`。

在 genuine full-exact branch (`m_4=3`、`kappa_6=-3m_3^2`) 只有

`Q_4(y)=1-5y^2/6+11y^4/24-(245+8m_3^2)y^6/1296+O(y^8)`，

以及 companion principal minor 的首项

`1+2Q_4-2H_rho-H_sqrt2
  =5(2-m_3^2)y^6/144+O(y^8)`。

因此四点虽已有新的 phase 数据，其最浅 principal minor 仍只恢复旧 cone
约束 `m_3^2<=2`；不能声称四点已经完成 rigidity。

## 7. 证据等级与下一步

- **PROVED / LOCAL-AUDITED**：四点 Gram、Schur determinant 展开、ellipse/bispectrum
  坐标、`Q_4`/`T_4` 的 `psi` 分离、同模长 pair 的 `y^6` 分离、anisotropic
  quadratic form 与 Gaussian anchor、full-exact 首阶系数。
- **PROVED conditional interface**：pointwise positive bispectrum 或 shear-cocycle
  alignment 一旦成立，即推出 `P_3K=0`。
- **CONDITIONAL**：full exact ellipse average + four-point PSD 是否强制 pointwise
  shear alignment；`RK=1` 是否提升到 genuine full-exact identification。
- **OPEN**：Four-Point Shear–Bispectrum Alignment Lemma、asymmetric genuine
  full-exact exclusion，以及最终 positive backward-tower rigidity。

因此 R109 不应升级到五点。下一轮最小命题是：在 local zero-free characteristic
neighborhood 内，证明或构造反例于

`Gamma_4 >=0` 与 `<B(s,s+t)>_{E_y}=exp(-y^2/2) for all y`

是否推出 `delta(s,t)=delta(s,s+t)`。只有找到 genuine characteristic phase lift
保留 nonzero shear cocycle，才有理由再进入五点 Gram。

禁止 numerical sweep、SDP、optimizer 或 remote computation。
