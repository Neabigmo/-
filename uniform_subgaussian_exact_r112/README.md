# R112 — Genuine exact three-sample law 的统一 square-exponential envelope

Date: 2026-09-07.

网页端 R112 在 connector 仍不可读时依据 R111 自包含定理继续推导，得到一个
重要的全局化结果。本机新增本记录并只把可核验部分写成明确的 theorem scope：
它对 genuine full-exact angular realization 成立；不能直接转移到 bare scalar
RK=1。

## 1. 统一 envelope 的来源

设 centered variance-one iid law X_1,X_2,X_3 满足 R101 的 genuine exact
angular barycenter。令

Q=sum_(j=1)^3 (X_j-X_bar)^2,
D=X_1-X_2。

angular exactness 的 radial representation 给出 Q 的分布识别

Q ~ chi^2_2,

因此

E exp(tQ)=1/(1-2t), 0<=t<1/2。

这里真正使用的是 Gaussian angular barycenter 加 iid same-factor
realization；抽象 Herglotz cone 的 positivity alone 不控制任何 one-body tail。

## 2. Sharp pair-difference inequality and Jensen transfer

有精确恒等式

2Q-D^2=(X_1+X_2-2X_3)^2/3>=0,

故 D^2<=2Q。对任意 0<a<1/4，

E exp(aD^2)<=E exp(2aQ)<=1/(1-4a)。

取独立副本 X'~X。由于 E[X'|X]=0，且 x -> exp(a x^2) 严格凸，

exp(aX^2)
 = exp(a(E[X-X'|X])^2)
 <= E[exp(a(X-X')^2)|X]。

积分后得到 genuine exact one-body envelope

E exp(aX^2)<=1/(1-4a), 0<a<1/4。

特别地，

E exp(X^2/8)<=2。

常数 2 来自 sharp 的 D^2<=2Q；它不依赖 law、depth 或 varying-bottom
层号。

## 3. Explicit zero-free and q^(3N) consequences

把 R111 的 explicit bridge 代入 a=1/8、B=2，可取

rho=sqrt(e/128), r_*=rho/2=sqrt(e/512),
C_*=2 log(2)/rho^6=2^22 log(2)/e^3。

于是每个 genuine full-exact layer 的 MGF 在 |z|<=rho 内统一 zero-free，
且在 kappa_4=0 时

|L_mu(u)|<=C_*|u|^6, |u|<=r_*,

其中 L_mu(u)=log|phi_mu(u)|+u^2/2。

若一条塔的底层 h_N=g_N^(N) 和所有中间层都属于该 genuine exact class，
并且 g_N^(0)=P_(q^N)h_N，则三层公式是：

Top/preimage:
|L_(h_N)(u)|<=C_*|u|^6, |u|<=r_*。

Intermediate:
g_N^(j)=P_(q^(N-j))h_N，
|L_(g_N^(j))(r)|<=C_*q^(3(N-j))|r|^6，
|r|<=r_*q^(-(N-j)/2)。

Base:
|L_(g_N^(0))(r)|<=C_*q^(3N)|r|^6，
|r|<=r_*q^(-N/2)。

R109 椭圆三点 r_1=s、r_2=s+t、r_3=2s+t 满足
sum r_j^2=y^2，因此

|log(prod_j|phi(r_j)| / exp(-y^2/2))|
<=C_*q^(3N)y^6,

并有相应的双边指数夹逼。由此，varying-bottom 的 analytic radius、
sixth-order remainder 和 q^(3N) modulus scale 均已统一控制。

## 4. 不能过度解读

这条 theorem 只给 absolute two-sided modulus budget，不给
L<=0。R110 的 exact first-odd expansion 说明 hypothetical nonzero odd
charge 反而产生正的 leading defect。因此它不能单独排除 asymmetric exact
law，也不能代替 primitive charge annihilation。

正确的证据边界是：

- PROVED / ANALYTICALLY PROVED under genuine angular realization：
  Q~chi^2_2 后的 (1-4a)^(-1) envelope、D^2<=2Q、Jensen transfer 和
  fixed-base/varying-bottom 统一性。
- PROVED / LOCAL-AUDITED algebra：D^2<=2Q 的平方恒等式、椭圆幂和、
  显式 a=1/8、B=2、rho、r_*、C_* 与 R111 q^(3N) bridge。
- CONDITIONAL：bare scalar RK=1 是否能识别为 genuine full-exact angular
  realization；若不能，以上 envelope 不能直接覆盖原始问题。
- OPEN：如何把 R109 sharp four-point cocycle disk 与
  O(q^(3N)y^6) modulus budget 转成 primitive shear-phase budget，并最终
  annihilate nonzero odd charge。

下一轮不再研究 tail/envelope，转向
Uniform Shear-Cocycle Budget Theorem：在统一 modulus budget 和 R109
four-point disk 下，能否得到 phase mismatch 的统一
q^(3N/2)y^3（或 square）控制；若不能，构造最小 genuine/formal obstruction。

