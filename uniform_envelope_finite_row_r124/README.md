# R124 — Envelope-Free Finite-Row Compactness and Cubic-Radius Dichotomy

日期：2026-09-07  
状态：PROVED / ANALYTICALLY PROVED（finite-row definition, moment bootstrap,
compactness, exact analytic upgrade, truncated-Hamburger interface）；
CONDITIONAL；FORMAL；核心 OPEN。

## 1. 主结果

R124 把原先的“统一指数平方包络紧性”加强为一个不需要先验包络的定理。
固定 `c!=0`。令 `X_1,X_2,X_3` iid，`EX=0`、`EX^2=1`，

`Q=sum_j(X_j-Xbar)^2`，

并令

`R_r(mu)=E Q^r-2^r r!`。

`R_r=0` 正是 angular MGF/circular exact identity 的第 `2r` 个 Taylor row。

定义 `E_M(c)` 为 genuine probability laws，满足 centered、variance one、
`kappa_3=c` 和 `R_1=...=R_M=0`，不额外要求 exponential-square envelope。

**Envelope-Free Fixed-c Compactness Theorem（PROVED / ANALYTICALLY PROVED）**：

`E_M(c)!=empty for every M`

推出存在 genuine full-exact law `mu_infty`，且 `kappa_3(mu_infty)=c`。特别地，
若固定非零 cubic 的 genuine full-exact law不存在，则必存在有限 `M(c)` 使
`E_M(c)=emptyset`。

这是服务主命题的真正 finite-certificate dichotomy；它不声称已经给出显式的
`M(c)` 或哪个具体 Hankel minor 先失败。

## 2. Exact rows 的无歧义定义（PROVED）

取

`a_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`，
`Y_theta=sum_j a_j(theta)X_j`。

在 residual plane 中 `Y_theta=R dot e_theta`、`|R|^2=Q`，并有

`(1/(2*pi)) int Y_theta^(2r) dtheta
 = binom(2r,r) Q^r/4^r`。

定义

`mathscr F_mu(z)=(1/(2*pi))int prod_j M_mu(z a_j(theta))dtheta-e^(z^2/2)`。

若 `m_k=E X^k`，则每个 row 是有限 moment polynomial：

`[z^(2r)] mathscr F_mu=R_r(mu)/(4^r(r!)^2)`。

因此前 `M` rows 明确就是 `R_1=...=R_M=0`，不是模糊的 formal phrase；odd
angular rows 自动因圆周对称为零。

## 3. 原始 uniform-envelope 版本（PROVED）

对一般 `delta>0,K<infinity`，加入
`E exp(delta X^2)<=K` 定义 `C_M^(delta,K)(c)`。该类在弱收敛下紧，
因为指数平方尾给 tightness、所有多项式矩的 uniform integrability、row
functional 和 `kappa_3` 的连续性；nested intersection 给

`C_M^(delta,K)(c)!=empty for all M`
`=> intersection_M C_M^(delta,K)(c)!=empty`。

统一 envelope 还使 `M_mu(z)` entire。所有 Taylor rows 为零后，identity theorem
给 `mathscr F_mu=0` 对所有复 `z` 成立；取 `z=it` 再由 Hankel uniqueness 得
`Q~chi^2_2`。所以 all rows 在这里是真正 global exact identity，而非 formal
moment germ。

## 4. Envelope-free moment bootstrap（PROVED / ANALYTICALLY PROVED）

关键几何不等式为

`(X_1-X_2)^2<=2Q`。

令 `D=X_1-X_2`，则

`E D^(2r)<=2^r E Q^r=4^r r!`

在第 `r` 个 exact row 下成立。由于独立副本 `X'` centered，条件 Jensen 给

`|X|^(2r)=|E[X-X'|X]|^(2r)<=E[|X-X'|^(2r)|X]`，

所以

`boxed{R_r=0 => E X^(2r)<=4^r r!}`。

特别，前 `M` rows 自动给

`E[sum_(r=0)^M (X^2/8)^r/r!] <= sum_(r=0)^M 2^(-r)=2-2^(-M)`。

即有限层已经逐阶产生截断 `exp(X^2/8)` 控制。

若 `E_M(c)` 对所有 `M` 非空，选 `mu_M in E_M(c)`。variance one 给 tightness；
对任意固定 moment order `p`，选 `r` 使 `2r>p`，当 `M` 足够大时上式给统一
`2r`-moment bound，故 `|X|^p` uniform integrable。弱极限沿对角子列保留所有
固定 moments、centeredness、variance、`kappa_3=c` 及每个 row，并得到

`E X^(2r)<=4^r r!` 对所有 `r`。

单调收敛于是给

`E exp(X^2/8)<=sum_r 2^(-r)=2`。

Carleman 条件成立，且由此得到的 MGF entire；所有 rows 通过 identity theorem
升级为真正的 full exact identity。故该极限是 genuine，而不是 formal branch。

## 5. Fixed-gap、cubic radius 与有限 Hamburger certificate（PROVED / CONDITIONAL）

令

`E_M(epsilon)={mu: centered, variance one, |kappa_3|>=epsilon,
R_1=...=R_M=0}`。

若所有 `M` 非空，则上面的 compactness 给 genuine full-exact law with
`|kappa_3|>=epsilon`；若 cubic exclusion 为真，则对每个 `epsilon>0` 存在
有限 `M(epsilon)` 使 `E_M(epsilon)=emptyset`。这是 CONDITIONAL 于主命题的
反命题，不是当前已经证明 cubic exclusion。

定义 genuine finite-row cubic radius

`Gamma_M=sup{|kappa_3(mu)|: mu genuine centered variance-one,
R_1=...=R_M=0}`。

则 `Gamma_(M+1)<=Gamma_M`，并且

`boxed{cubic exclusion iff Gamma_M -> 0}`。

在有限 moment language 中，令 `T_M(c)` 由

`y_0=1,y_1=0,y_2=1,y_3=c`，
`H_M(y)=[y_(i+j)]_(i,j=0)^M >=0`，
`R_r(y)=0 (1<=r<=M)`，
`0<=y_(2r)<=4^r r!`

组成。若所有 `T_M(c)` 非空，坐标对角化、Hankel positivity、Carleman 与
Hamburger moment theorem 给 genuine full-exact law；所以若该 law 不存在，
必有有限 `M(c)` 使 `T_M(c)=emptyset`。

这是真正有限、可检验的 obstruction framework，但本轮没有做 SDP 或 optimizer，
也没有声称知道第一个失败的 principal minor。

## 6. R115/R120 finite-row obstruction 的准确解释

此前 perturbative constructions 对每个固定有限 `M` 只保证存在某个
`c_*(M)>0` 使 `0<|c|<c_*(M)` 可实现；它们没有证明
`inf_M c_*(M)>0`。若 cubic exclusion 为真，R124 强制
`c_*(M)->0` 至少沿某个高阶序列。因为 finite-row laws 的 envelope 实际由 rows
自动控制，真正可能退化的是 admissible fixed-c cubic radius，而非先验尾界。

## 7. 证据等级与 R125

PROVED / ANALYTICALLY PROVED：row moment formula；uniform-envelope compactness；
all-row-to-global-exact upgrade；moment determinacy；envelope-free bootstrap；
fixed-gap compactness dichotomy；finite truncated-Hamburger certificate interface。

CONDITIONAL：若主 cubic exclusion 成立，则 `E_M(c)` 或 `T_M(c)` 在有限阶必空，
以及 `Gamma_M->0`；这些是定理的 contrapositive，不是主命题证明。

FORMAL：R104 nonzero-cubic all-degree branch 没有 genuine Hamburger/PD
realizability，因此不违反 R124。

OBSTRUCTION：R124 不给显式 `M(c)`、negative Hankel direction、`Gamma_M` decay
rate 或第一个失败约束；row equations alone 仍可 formal all-degree 解。

OPEN：`Gamma_M -> 0`，等价地非零 formal odd exact branch 是否能无限穿过
genuine Hamburger positivity cone。

R125 固定为 **Truncated-Hamburger Cubic-Radius Decay**：对有限 moment sets
`T_M` 或其不带预设 `c` 的 union，构造随 `M` 增长的 nonnegative polynomial
certificate `P_M(X)^2`，力争得到 `|kappa_3|<=epsilon_M`、`epsilon_M->0`。
即直接证明 finite-row hierarchy 的 cubic radius 衰减，而不再重复 compactness。
