# R138 — infinite odd tail / Bochner phase audit

日期：2026-09-08

本目录记录网页端 R138 的独立本机审计。审计对象是 genuine centered
variance-one probability law `mu`，并且明确假设它属于 full same-factor
class；不能把 scalar `RK=1`、空间函数 `K_sp=log g`、normalized Bargmann
logarithm `C_g=log B_g` 和 ordinary log-MGF 混用。

## 1. 已核验的全阶结果

若 `E exp(eta X^2)<infty`，则 `M(z)=E exp(zX)` 是 order at most two 的 entire
function。Hadamard genus-two factorization gives, for `m>=3`,

`kappa_m = -(m-1)! sum_nu zeta_nu^(-m)`.

按零点重数定义

`R_Delta=min{|zeta|: n(zeta)!=n(-zeta)}`，

空集时取 `R_Delta=infty`。对奇数阶有

`limsup (|kappa_m|/(m-1)!)^(1/m)=1/R_Delta`.

这里的关键是把 `zeta` 与 `-zeta` 的重数先相减；在最小非配对半径上，
有限个 reciprocal zero 的奇次幂构成非零 finite exponential sum，其
Cesaro mean square 不为零。该结论是 PROVED，但它不是 phase rigidity：它只
把任何非对称 law 的 odd tail 定位到一个有限的非配对零点半径。

因此以下子类被严格排除：

* finite odd-cumulant support；
* `limsup_{m odd} (|kappa_m|/(m-1)!)^(1/m)=0` 的超指数 normalized odd tail；
* `C_g` 能够成为整个函数的情形（此时 `B_g=e^{C_g}` zero-free，finite-order
  Hadamard rigidity gives Gaussian）；
* 在 full-SF 假设下，MGF 只有有限个复零点的情形。

这里只能把 ordinary MGF 的 zero divisor 结论标为 PROVED；从 scalar `RK=1`
到 genuine full-SF/all-row 仍为 CONDITIONAL。

## 2. full-SF 的实轴预算

写

`K(t)=log E exp(tX)=t^2/2+C(t)`，
`E(t)=(K(t)+K(-t))/2`，`O(t)=(K(t)-K(-t))/2`。

Jensen and centering give

`0<=E(t)` and `|O(t)|<=E(t)`.

Full-SF and `r_j=sqrt(2/3) cos(theta+2pi(j-1)/3)` give the exact angular
identity. Jensen on that identity yields

`average_theta E(R cos(theta)) <= R^2/4`,

and convexity yields the sharper pointwise estimate

`E(x)<=x^2`,

which improves the earlier coarse `E(x)<=2x^2+log(2)-1/8` bound. The derivative
identity is

`<e^H (H_t^2+H_theta^2/t^2)>`
`=(2/3)[3-<e^H sum_j K''(t r_j)>] <= 2`,

where `H=sum_j C(t r_j)`; it is valid for `t!=0` and extends by the limit at zero.
Consequently

`int_0^T |O''(t)|dt <= E'(T)`

and the safe bound inherited from the quadratic estimate is

`int_0^T |O''(t)|dt <= 8T+(log(2)-1/8)/T`.

The angular odd part gives a stronger resummed, but not coefficientwise, control.
If

`Q_r(t)=<H_o(t,theta) exp(-3 i r theta)>`,

then

`sum_{r>=1, r odd}|Q_r(t)|^2 <= exp(t^2/2)(1-exp(-S(t)))`
`<= (t^2/2) exp(t^2/2)`.

This controls Fourier-resummed charges, not individual absolute cumulants. The
remaining infinite-tail escape is cancellation between degrees in the same
Fourier charge.

## 3. Bochner and compactness boundaries

For a fixed finite node set, the small-frequency Bochner determinant has leading
coefficient

`det[phi(h(x_i-x_j))]`
`=h^(m(m+1)) Vandermonde(x)^2 Delta_m / prod_{k=0}^m(k!)^2`
`+O(h^(m(m+1)+2))`.

For nodes `0,1,...,m`, the Vandermonde factor cancels. A hidden odd degree
`d=2s+1` is first visible in the `(s+2)x(s+2)` matrix (the `H_{s+1}` level),
not in any smaller fixed matrix. The `0,t,2t` determinant retains the Gaussian
`2t^6-4t^8+O(t^10)` beginning; a hidden phase first contributes quadratically at
order `a^2 t^(2d)`. Thus every fixed finite local test misses sufficiently small
hidden packets. This is an OBSTRUCTION, not a global counterexample.

If one fixed formal full-SF moment sequence has genuine finite-jet realizations
`mu_M` for every `M` and either

`sup_M E_muM exp(eta X^2)<infty`

for some `eta>0`, or `mu_M=g_M dgamma` with `sup_M ||g_M||_p<infty` for
`1<p<infty`, weak compactness plus uniform integrability gives one genuine
all-moment law. Under the square-exponential bound its MGF is entire, so every
formal SF coefficient identity becomes the actual analytic identity. This is a
PROVED compactness interface; it does not produce the uniform bound by itself.

## 4. Positive backward-tower consequences

For a single genuine full-SF law, the tail estimate implies a law-independent
zero-free disk `|z|<=1/4` for its MGF. If a fixed bottom law `g_0` has genuine
all-depth preimages `g_0=P_{q^N}h_N`, normalized Bargmann scaling gives

`B_{g_0}(z)=B_{h_N}(q^(N/2)z)`.

Any zero of `B_{g_0}` would therefore create zeros of `B_{h_N}` arbitrarily close
to zero, contradicting the common zero-free disk. Finite-order zero-free rigidity
then forces `g_0` Gaussian. This is PROVED under the genuine full-SF/all-row
assumptions.

For incompatible finite-depth towers, the bottom law changes with `N`; the
zero-free disk grows after OU rescaling, but moving degrees `d_N->infty` and
amplitudes `a_N->0` remain an escape route. That case is still OPEN. A fixed
finite-SF selector, a moving selector sequence, and one genuine all-degree law
are three different objects and are not interchangeable.

## 5. Final evidence split

* **PROVED**：zero-divisor formula; non-paired-zero radius formula; finite-zero and
  zero-free rigidity; full-SF Fisher/entropy budgets; fixed finite Bochner leading
  term; cutoff-uniform compactness interface; compatible genuine backward-tower
  Gaussian rigidity.
* **OBSTRUCTION**：finite local Bochner tests; coefficientwise positivity; real-axis
  convexity alone; merely exponential normalized odd-tail bounds; no explicit first
  failing Hankel index for the fixed sparse branch.
* **CONDITIONAL**：scalar `RK=1` to genuine full-SF/all-row, and any transfer from
  `C_g`/ordinary MGF statements back to the spatial `P_3 K_sp` statement.
* **OPEN**：existence or nonexistence of a genuine full-SF law with infinitely many
  nonzero odd cumulants and an asymmetric infinite MGF zero divisor; and the
  incompatible moving-top positive backward tower.

审计命令：

`F:\\anaconda3\\python.exe r138_infinite_tail_bochner_audit\\audit_r138.py`
