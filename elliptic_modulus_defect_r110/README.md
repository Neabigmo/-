# R110 — Gaussian-relative modulus defect 与 q^(3N) 尺度

Date: 2026-09-07.

本轮记录网页端在连接器连续返回账户连接错误时给出的 provisional 推导，随后
用本机精确符号审计复核其有限代数。网页端本轮不能诚实地声称重新读取了本机
R109 文件；因此下面把“本轮解析证明”和“本机已核验的有限恒等式”分开标记。

## 1. Gaussian-relative modulus defect

对原点邻域内 phi_mu(r) != 0 的 centered variance-one probability law，定义

L_mu(r) = log|phi_mu(r)| + r^2/2.

于是 L_mu <= 0 正是 Gaussian modulus domination
|phi_mu(r)| <= exp(-r^2/2)。若 mu=P_tau nu，其中 0<tau<=1，OU
characteristic transport 是

phi_mu(r)=exp(-(1-tau)r^2/2)*phi_nu(sqrt(tau)*r),

从而有精确的 defect transport

L_(P_tau nu)(r)=L_nu(sqrt(tau)*r)。

因此一条长度为 N 的塔满足

g^(0)=P_(q^N)g^(N)、
L_(g^(0))(r)=L_(g^(N))(q^(N/2)r)。

这是本轮最重要的尺度恒等式：它把底层的局部 defect 直接压缩到
q^(3N)（当首个未消 odd charge 为三阶时）。

## 2. 无条件的 positivity-only majorant

仅使用 |phi_(g^(N))|<=1 即得

|phi_(g^(0))(r)| <= exp(-(1-q^N)r^2/2)

以及

L_(g^(0))(r) <= q^N r^2/2。

对 R109 的椭圆坐标

r_1=s, r_2=s+t, r_3=2s+t,
y^2=6s^2+6st+2t^2

有 r_1^2+r_2^2+r_3^2=y^2，所以

|phi(s)phi(s+t)phi(2s+t)|
 <= exp(-(1-q^N)y^2/2)
 = exp(-y^2/2) exp(q^N y^2/2)。

这个结论是无条件的，但只有 q^N 级别的二次误差，不能关闭 R109 所需的
局部 Gaussian product majorant。它也说明“正性 + 有限深度”不能被误写成
L<=0。

## 3. 首个 odd charge 的局部反号

沿用 R103/R104 的 same-factor exact analytic 输入：若首个未消 odd cumulant
为 kappa_d（d 为奇数），且低阶 even terms 已由 exactness 清除，则网页端
得到

kappa_(2d) = -(2d)!/(2(d!)^2) * (<p_d^2>/<p_(2d)>) * kappa_d^2 < 0,

并且

L_mu(r)=c_d*kappa_d^2*r^(2d)+O(r^(2d+2)),

其中

c_d=<p_d^2>/(2(d!)^2 <p_(2d)>) > 0。

所以只要这个 exact local branch 的首个 odd charge 非零，它在所有充分小的
非零实频率上严格满足 L_mu(r)>0，即严格反向于 Gaussian modulus domination。

最相关的 d=3 版本不需要保留抽象的 p_d 记号。R103/R104 的六阶 exact
fingerprint 是

kappa_6+3*kappa_3^2=0，

而 cumulant expansion 给出

L_mu(r)=kappa_3^2*r^6/240+O(r^8)。

这部分的常数和符号已由 audit_r110.py 独立精确核验。

## 4. OU 深度与椭圆 defect

若 g^(0)=P_(q^N)g^(N) 且底层满足上述 d=3 局部展开，则

L_(g^(0))(r)=q^(3N)*kappa_3(g^(N))^2*r^6/240
              +O(q^(4N)r^8)

（量词必须理解为先在底层统一局部解析范围内取
|r|<=r_*q^(-N/2)，否则不能把 remainder 写成 uniform 结论）。对 R109
椭圆 product defect 定义

M_mu(s,t)=log(|phi(s)phi(s+t)phi(2s+t)|/exp(-y^2/2))

则

M_mu=L_mu(s)+L_mu(s+t)+L_mu(2s+t)。

因此首个 odd charge 非零时

M_mu(s,t)=c_d*kappa_d^2*
 [s^(2d)+(s+t)^(2d)+(2s+t)^(2d)] + O(y^(2d+2))。

由幂平均不等式，令 x_j=r_j^2>=0，有

sum_j x_j^d >= 3^(1-d)*(sum_j x_j)^d=3^(1-d)y^(2d)。

故 hypothetical asymmetric exact branch 在所有充分小的非零椭圆上严格产生
M_mu>0，而不是 R109 需要的 M_mu<=0。这不是反例，因为这里假定的
nonzero exact branch 尚未被构造；它是一个把“最终排除”转成“正负号/余项”
问题的局部接口。

## 5. varying-bottom 的 genuine obstruction

R107 的 exact-fourth asymmetric law H 是 genuine probability law，满足

E H=0, E H^2=1, kappa_3(H)=1, kappa_4(H)=0, kappa_6(H)=-6。

令

g_N^(j)=P_(q^(N-j))H, 0<=j<=N。

则每条有限链都满足 g_N^(j)=P_q g_N^(j+1)，且
g_N^(0)->gamma。但是

kappa_3(g_N^(0))=q^(3N/2),
L_(g_N^(0))(r)=q^(3N)r^6/120+O(q^(4N)r^8)>0

在每个有限 N 的充分小非零频率上成立。

这证明了一个重要的边界：在 centered variance-one、kappa_4=0 的 genuine
probability 类中，有限正向后向深度不能单独推出 Gaussian modulus domination，
而 q^(3N) 正是可达到的局部尺度。它不是原始 full-exact 问题的 counterexample：
H 的六阶 exactness 要求应为 kappa_6=-3*kappa_3^2，但这里是 -6。

固定一个底层 law 与 varying-bottom 必须严格区分。若同一个 g 对任意 N
都有 g=P_(q^N)nu_N，则缺陷 transport 可以直接逼近原点；而上面的 H
族通过随 N 改变底层逃逸了这个固定-base 论证。

## 6. 可使用但尚未由既有记录提供的条件定理

若某个类 C 同时满足 centered、variance-one、kappa_4=0，并存在与成员及
N 无关的 C_*,r_*>0，使所有 mu in C 在 |u|<=r_* 上满足

|L_mu(u)|<=C_*|u|^6,

那么对每个深度 N

|L_(g^(0))(r)|<=C_* q^(3N)|r|^6

只要 |r|<=r_*q^(-N/2)。在 R109 椭圆上进一步有

|M_(g^(0))(s,t)|<=C_*q^(3N)y^6,

因为 sum_j |r_j|^6 <= (sum_j r_j^2)^3=y^6。

等价地，product modulus 有双边夹逼

exp(-y^2/2-C_*q^(3N)y^6)
 <= |phi(s)phi(s+t)phi(2s+t)|
 <= exp(-y^2/2+C_*q^(3N)y^6)。

这是一个有发表价值的 clean conditional theorem，但不能升级为 unconditional
结果：本机 parity_fredholm_ou_r12 只记录 parity/Fredholm exact defect map，
没有给出上述统一的 C_*,r_* modulus envelope。R101 中关于
square-exponential envelope 的表述只足以支撑其声明的 moment-determinacy
假设，不能自动替代这里所需的 uniform local bound。

## 7. 证据等级与下一最小命题

- PROVED / LOCAL-AUDITED：exact OU defect transport；positivity-only 的
  q^N majorant；椭圆几何；d=3 的 1/240 正系数；R107 H 的矩、
  cumulant 与 q^(3N) 展开；条件定理中的幂和估计。
- ANALYTICALLY PROVED under stated exactness inputs：首个 odd charge 的
  局部正 modulus defect及其椭圆版本；一般 d 的 forced-even 公式。
- CONDITIONAL：从 positive backward divisibility、R101 Herglotz cone、
  R104 Schur–Abel 约束推出统一 C_*,r_*；从 scalar RK=1 识别到 genuine
  full-exact law。
- OPEN：exact asymmetric law 的 genuine 排除；primitive odd charge
  annihilation；varying-bottom tower 的 uniform modulus domination；最终
  Positive Backward-Tower Exact Zero-Set Rigidity。

下一轮只攻一个明确目标：Uniform q^(3N) Modulus-Defect Theorem。网页端
必须给出统一 C_*,r_* 的真实来源；如果 R12/R101/R104 不能提供，就构造
最小 obstruction 并把缺失输入写成可独立验证的 lemma。禁止数值扫描、SDP、
optimizer 和 remote computation。

