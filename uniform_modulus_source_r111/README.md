# R111 — 从统一 square-exponential moment 到 uniform modulus defect

Date: 2026-09-07.

本记录分成两部分。网页端 R111 因 connector 三次返回账户错误，没有新增
LOCAL-AUDITED 的网页推导；它把最小缺口准确指出为统一 zero-free disk。
随后本机在一个明确、可检查的假设下补出了这条 analytic bridge，并标明该假设
尚未由项目既有 R12/R101/R104 记录推出。

## 1. 最小输入：统一 square-exponential moment

设一个 centered variance-one law 类 C 满足

sup_(mu in C) E_mu exp(a X^2) <= B

其中 a>0、B<infinity 与 mu 无关。令

rho=min(sqrt(a)/2, sqrt(a*e/(8B)))。

对 MGF M_mu(z)=E exp(zX)，中心化后的 Taylor remainder 给出

|M_mu(z)-1|
<= |z|^2/2 * E[X^2 exp(|z||X|)]
<= (B|z|^2/(a e))*exp(|z|^2/(2a))
<= exp(1/8)/8 < 1/2

当 |z|<=rho 时。第二个不等式只用 Young inequality
|z||X|<=aX^2/2+|z|^2/(2a) 以及
X^2 exp(aX^2/2)<=2 exp(aX^2)/(a e)。

因此 M_mu 在统一圆盘 |z|<=rho 内 zero-free，且可选取同一个解析
branch K_mu=log M_mu。同时

|K_mu(z)|<=log 2

在该圆盘内成立。Cauchy estimate 于是给出所有成员统一的 cumulant bound

|kappa_n(mu)|/(n!) <= log(2)/rho^n。

这正是网页端 R111 所说的最小核查链中“uniform exponential-square moment
=> uniform complex M bound => uniform zero-free disk”的完整定量版本。

## 2. uniform q^(3N) modulus-defect theorem（条件定理）

进一步限制到 kappa_4(mu)=0 的类 C。对

|u|<=r_*:=rho/2

有

L_mu(u)=log|phi_mu(u)|+u^2/2

以及

|L_mu(u)|
<= log(2) * sum_(m>=3) (|u|/rho)^(2m)
<= 2 log(2)*|u|^6/rho^6。

这里使用 centered、variance-one 消去二阶项，kappa_4=0 消去四阶项；
奇阶 cumulant 在 Re K(iu) 中自动消失。于是可以取

C_* = 2 log(2)/rho^6。

若 g^(0)=P_(q^N)g^(N) 且所有 bottom laws 属于 C，则 exact transport 给出

|L_(g^(0))(r)| <= C_* q^(3N)|r|^6

只要

|r|<=r_* q^(-N/2)。

对 R109 椭圆三点

r_1=s, r_2=s+t, r_3=2s+t,
y^2=sum_j r_j^2

同样有

|M_(g^(0))(s,t)|<=C_*q^(3N)y^6

以及

exp(-y^2/2-C_*q^(3N)y^6)
<=prod_j|phi_(g^(0))(r_j)|
<=exp(-y^2/2+C_*q^(3N)y^6)。

因此 R110 的 clean conditional theorem 可以升级为一个带有明确
a,B,r_*,C_* 的 conditional theorem，而不再只写“存在 uniform analytic
envelope”。

## 3. 这仍然没有关闭主命题

本条件定理只给 absolute two-sided control。R110 的 first-odd expansion 表明，
在 hypothetical full-exact asymmetric branch 上，L 的首项反而为正；因此
|L|=O(q^(3N)r^6) 不能推出目标符号 L<=0。

R107 的 varying-bottom obstruction 还说明 finite-depth positive towers 可以有
相同的 q^(3N) 正向局部缺陷。故真正剩余的不是把常数做小，而是：

- 从 positive backward-preimage cone、same-factor exactness 和 genuine
  realization 推出统一 square-exponential moment bound；或
- 直接证明 primitive odd charge annihilation；或
- 找到一个带符号的 exact estimate，排除 R110 首项的正号。

## 4. 与既有记录的证据边界

本机 parity_fredholm_ou_r12 只证明 parity principal symbol、OU covariance
和 compact-perturbed exact defect map，文件中没有明确的统一 a,B 或
inf|M_mu| 结论。R101 的 square-exponential envelope 只在
moment-determinacy 假设中被引用，也没有给出本节所需的 uniform constants。

所以：

- PROVED / LOCAL-AUDITED：square-exponential moment 假设下的 zero-free
  disk、uniform cumulant estimate、kappa_4=0 后的 C_*|u|^6 bound、
  OU depth transport 和 ellipse propagation 的有限代数。
- CONDITIONAL：项目 exact positive backward class 是否满足统一
  E exp(aX^2)<=B；从而是否能应用本节的 explicit theorem。
- OPEN：uniform square-exponential moment 的 tower来源、charge-relative
  remainder、genuine asymmetric full-exact exclusion，以及最终
  Positive Backward-Tower Exact Zero-Set Rigidity。

下一轮网页任务应只问一个更小的命题：在当前 exact positive class 中，能否从
R101 Herglotz cone 或 R104 Schur–Abel convexity 推出某个明确的统一
E exp(aX^2)<=B；若不能，给出满足所有已知有限约束但使该 uniform bound
失效的 formal/genuine obstruction。禁止把本条件假设当作已有事实。

