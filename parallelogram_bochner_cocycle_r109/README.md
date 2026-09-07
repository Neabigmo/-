# R109 — Parallelogram Bochner cocycle disk and exactness gap

日期：2026-09-07

本轮承接 `four_point_bispectrum_shear_r108`，严格审查
Four-Point Shear–Bispectrum Alignment Lemma。结论不是无条件 rigidity，而是
给出一个 sharp 的四点 cocycle disk、一个 genuine characteristic obstruction，
以及把真正缺失的输入压缩为 elliptic modulus saturation。

## 1. 四频率 parallelogram Gram

令

`a=phi(s)`, `b=phi(t)`, `c=phi(s+t)`, `d=phi(2s+t)`。

对频率集合 `{0,s,s+t,2s+t}` 的 Bochner Gram 为

`G_4=[[1,conj(a),conj(c),conj(d)],
     [a,1,conj(b),conj(c)],
     [c,b,1,conj(a)],
     [d,c,a,1]] >= 0`.

沿公共 edge `{0,s}` 做 Schur 消元。记

`Delta_0=1+2 Re(a b conj(c))-|a|^2-|b|^2-|c|^2`,

`Delta_1=1+2 Re(a c conj(d))-|a|^2-|c|^2-|d|^2`，

`N=conj(a)(1-|a|^2+|c|^2)-b conj(c)-c conj(d)+a b conj(d)`。

在 `0<|a|<1` 时有精确恒等式

`G_4/A_s = (1/(1-|a|^2))*[[Delta_0,N],[conj(N),Delta_1]]`，

其中 `A_s=[[1,conj(a)],[a,1]]`。

因此得到无松常数的必要且局部等价条件

`|N|^2 <= Delta_0 Delta_1`。

## 2. Sharp shear-cocycle disk

写

`B(s,t)=a b conj(c)=|abc| exp(i delta_0)`，
`B(s,s+t)=a c conj(d)=|acd| exp(i delta_1)`，

并令 `eta=delta_0-delta_1`。若
`r_0=|a|,r_1=|b|,r_2=|c|,r_3=|d|`，则 `N=conj(a) Xi`，且

`Xi=P+exp(-i eta)Q`,

`P=1-r_0^2+r_2^2-(r_1r_2/r_0)exp(i delta_0)`,

`Q=exp(i delta_0)(-(r_2r_3/r_0)+r_1r_3 exp(i delta_0))`。

故四点 PSD 等价给出

`|P+exp(-i eta)Q| <= sqrt(Delta_0 Delta_1)/r_0`。

当 `Q!=0` 时，`exp(-i eta)` 落在单位圆与一个闭圆盘的交集中；一般是一个
arc，而不是单点。这是 R109-A 的 sharp four-point cocycle inequality。

## 3. 两个互补的 no-go

### R109-B — PROVED / genuine pointwise obstruction

Gaussian characteristic function在频率互异时给出严格正定的 Gaussian kernel，故
`Delta_0>0`、`Delta_1>0` 且 `|N|^2<Delta_0 Delta_1`。因此 Gaussian alignment
point 在 admissible disk 的严格内部；四点 PSD 本身没有 equality-case 机制强迫
`eta=0`。

R107 的 OU-smoothed asymmetric homometric law 是 genuine probability law，
所以其 characteristic function 在原点邻域 zero-free 且全部 Bochner Gram 自动
PSD。其 `kappa_3=lambda^(3/2)`，局部 phase

`vartheta(r)=-kappa_3 r^3/6+O(r^5)`，

从而 shear cocycle

`eta(s,t)=vartheta(t)-2vartheta(s+t)+vartheta(2s+t)
         =-lambda^(3/2)s^2(s+t)+O((|s|+|t|)^5)`。

它严格非零，同时仍满足 `Gamma_4>=0`。因此 pointwise four-point PSD 不能推出
shear alignment。

### R109-C — PROVED / formal obstruction

R104 的 formal exact Schur cascade允许 `kappa_3!=0`、
`kappa_6=-3 kappa_3^2` 且 coefficientwise `Z(z)=1`，但 formal phase 仍有
`eta=-kappa_3 s^2(s+t)+...`。它不能冒充 probability realization；真正 OPEN
正是 formal exactness 与 genuine characteristic realization 的交集。

对 R107 genuine law，normalized exactness functional在六阶满足

`[z^6](Z-1)=(kappa_6+3 kappa_3^2)/2592=-lambda^3/864`。

沿 `z=iy` 后

`Z(iy)=1+lambda^3 y^6/864+O(y^8)`。

这与 R108 完整 phase observable 的 `lambda^3 y^6/864` 分离处于同一精确尺度，
表明 exactness 要消掉的正是 nontrivial shear-phase 的首个尺度。

## 4. 与主命题的逻辑关系

在 genuine full-exact analytic/MGF class 内，`Gamma_4>=0` 与 ellipse exact
identity 对每个 law 都自动成立。R108-E 已证明

`delta(s,t)=delta(s,s+t) locally  =>  P_3K=0`。

而 R102 给出 `P_3K=0` 与 symmetry 的等价接口。因此“所有 genuine full-exact
law 都满足 shear alignment”与排除 asymmetric genuine exact law 是同一层级的
命题，并非更弱的独立中间定理。

## 5. 真正的缺失假设：elliptic modulus saturation

一个足以关闭非对称 sector、且不先假设 phase 对齐的条件是：在局部 exact ellipse
上逐点成立

`|B(s,s+t)| <= exp(-y^2/2)`,
`6s^2+6st+2t^2=y^2`。

因为 exactness 给出
`<B(s,s+t)>_{E_y}=exp(-y^2/2)`，于是

`exp(-y^2/2)=|<B>| <= <|B|> <= exp(-y^2/2)`。

所有不等式取等，故 `B(s,s+t)` 逐点为正且模长等于上界；椭圆坐标覆盖原点
邻域，连续 Cauchy 方程与 centered 条件给出 `vartheta=0`，从而 `P_3K=0`。

更简单但更强的充分条件是局部 Gaussian modulus domination
`|phi(r)|<=exp(-r^2/2)`；它由
`s^2+(s+t)^2+(2s+t)^2=y^2` 立即推出上述 product majorant。
任意深度的 positive OU divisibility 可能提供这类 domination，但 varying-bottom
tower 中其 uniform 极限机制仍需单独证明，不能在此处偷换。

## 6. 证据等级与下一步

- **PROVED / LOCAL-AUDITED**：四频率 Gram、公共 edge Schur 分解、sharp disk
  inequality、Gaussian strict-interior no-go、genuine shear expansion、六阶
  exactness defect，以及 product-majorant 一旦成立后的 rigidity 推论。
- **FORMAL**：formal exact nonzero-shear branch；无 probability realization。
- **CONDITIONAL**：full exact + positive backward divisibility 是否推出 elliptic
  modulus majorant；`RK=1` 到 genuine full-exact identification。
- **OPEN**：asymmetric genuine full-exact exclusion 与最终 positive
  backward-tower rigidity。

因此不应立刻升级到五点。下一轮最小命题是
**Elliptic Modulus-Saturation Lemma**：从 Schur–Abel difference data、四点
cocycle disk 以及 positive backward-preimage cone 出发，证明或反驳局部
`|phi(s)phi(s+t)phi(2s+t)|<=exp(-y^2/2)`。若该路线出现 genuine obstruction，
再把 obstruction 的最小结构升级为五点 Gram。

禁止 numerical sweep、SDP、optimizer 或 remote computation。
