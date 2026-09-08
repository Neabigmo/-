# R146 — Tilted Sample-Variance Laplace / Laguerre–Heat Audit

Date: 2026-09-08
Status: exact analytic identities and conditional interfaces recorded; the
genuine iid fixed-sample-size chi-square characterization and the positive
backward-tower closure remain open.

## 0. Scope and evidence boundary

The web-side derivation was required to read the public R145 record and the
current public repository before working. The resulting strict publication
audit was:

`无（目前没有足够独立、完整、可审稿的发表性结果）`。

This is a negative publication audit, not a claim that R146 made no progress.
R146 supplies a coherent lemma package for a future paper: an iid tilted
Laplace transform, an exact Gaussian-heat representation, a Laguerre spectral
decomposition of the tilted residual law, a positive-source PDE, an explicit
conditional first-mode closure criterion, and an exact OU/tower scaling law.
None of these statements proves that a non-Gaussian genuine full-SF law exists,
and none closes the scalar `RK=1` to full-SF bridge or the spatial
`P_3 K_sp` bridge.

Throughout, `X_1,X_2,X_3` are iid centered variance-one variables whenever an
iid statement is made. Put

`C=(X_1+X_2+X_3)/sqrt(3)`,

`U=(X_1-X_2)/sqrt(2)`, `V=(X_1+X_2-2X_3)/sqrt(6)`, and

`Q=R^2=U^2+V^2=sum_j X_j^2-(sum_j X_j)^2/3`.

The exact residual boundary `Q~chi^2_2` is always labelled as a genuine
full-SF/all-row consequence, not as something obtained from scalar `RK=1`.

## 1. Tilted Laplace transform and iid factorization

Let `M(t)=E exp(tX)`, `K(t)=log M(t)`, and let

`Lambda(a,z)=E exp(a C-z Q) / E exp(a C)`, `z>=0`.

Writing `t=a/sqrt(3)` and introducing the exponential tilt

`d mu_t(x)=exp(t x-K(t)) d mu(x)`,

the quadratic identity for `Q` gives the exact iid form

`Lambda(sqrt(3)t,z)=E_{mu_t tensor 3} exp(-z Q)`.

Thus `Lambda` is a Laplace transform in `z` of the residual energy under a
common scalar tilt. If `M(t)<infinity`, it is well-defined for `z>=0`.
Under a local domination condition such as

`sup_{t in I} E[exp(tX+epsilon |X|+epsilon X^2)]<infinity`,

the derivatives can be exchanged:

`partial_a^m partial_z^r E exp(aC-zQ)`
`=(-1)^r E[C^m Q^r exp(aC-zQ)]`.

This is the correct interface between the one-dimensional exponential family
and the two-dimensional residual law; it is not yet a coercive inequality for
`K''`.

## 2. Exact Gaussian-heat representation

Set

`L(t,z)=E exp(tX-zX^2)`,

`F(t,z)=E exp(t sum_j X_j-zQ)`.

Since

`Q=sum_j X_j^2-(sum_j X_j)^2/3`,

a Gaussian linearization gives

`F(t,z)=P_{2z/3}[L(.,z)^3](t)`,

where `P_tau f(t)=E_G f(t+sqrt(tau)G)` is the one-dimensional Gaussian heat
semigroup. Consequently

`Lambda(sqrt(3)t,z)=F(t,z)/M(t)^3`.

This representation is genuinely iid-specific. It is useful because the
nonnegative source in the logarithmic PDE can be displayed exactly, but the
source prevents a boundary value at `t=0` from propagating to every tilt.

## 3. Exact boundaries, complete monotonicity, and density endpoint

Under full-SF at the untilted point,

`Lambda(0,z)=E exp(-zQ)=1/(1+2z)`.

For every fixed `a`, complete monotonicity is automatic:

`(-1)^r partial_z^r Lambda(a,z)`
`=E_{mu_t tensor 3}[Q^r exp(-zQ)] >= 0`.

The first derivative at the boundary is

`-partial_z Lambda(a,0)=2 K''(a/sqrt(3))`.

Therefore the desired constant-regression conclusion is equivalent to the
still-unproved identity

`-partial_z Lambda(a,0)=2` for all relevant `a`, or equivalently
`K''(t)=1`.

If the tilted law has a sufficiently regular density `p_t`, a separate
large-`z` endpoint is available:

`lim_{z->infinity} 2z Lambda(sqrt(3)t,z)`
`=2 pi sqrt(3) integral p_t(x)^3 dx`.

At `t=0`, the full-SF boundary yields

`2 pi sqrt(3) integral p(x)^3 dx=1`.

This recovers the cubic spatial escort endpoint in the density setting. It is
an exact bridge endpoint, but it does not imply the spatial cubic kernel
condition `P_3 K_sp=0`; the intermediate ordinary-to-spatial bridge remains
open.

## 4. Mixed derivatives and Appell regression identity

For the normalized tilted law proportional to `exp(aC-zQ)`,

`partial_z log Lambda=-E_{a,z} Q`,

`partial_zz log Lambda=Var_{a,z}(Q)>=0`,

`partial_az log Lambda=-Cov_{a,z}(C,Q)`.

At `z=0`,

`partial_az log Lambda(a,0)=-(2/sqrt(3)) K'''(a/sqrt(3))`.

At the origin this is `-(2/sqrt(3)) kappa_3`. These are exact identities, but
the covariance sign is not fixed by positivity.

Under the exact residual boundary, define the normalized cumulant-Appell
polynomials by

`exp(tC)/E exp(tC)=sum_n P_n^C(C) t^n/n!`.

Then, for `n>=1`,

`E[(Q-2) P_n^C(C)]=2 3^(-n/2) kappa_(n+2)`.

Equivalently, for `H(C)=E[Q-2|C]`,

`E[H(C) P_n^C(C)]=2 3^(-n/2) kappa_(n+2)`.

Thus the complete higher-cumulant sequence is an Appell-coordinate sequence of
the conditional sample-variance regression defect. The conditional closure
itself is rigorous:

`E[Q|C]=2 a.s.  =>  K''=1  =>  mu=N(0,1)`

under a neighborhood MGF (or stronger square-exponential) hypothesis. The
missing implication is full-SF `=> E[Q|C]=2`.

## 5. Exact Laguerre decomposition of the tilted residual law

Assume the full-SF boundary `Q~chi^2_2` at `a=0`. Put `T=Q/2`, so
`T~Exp(1)`, and let `L_m` be the standard Laguerre polynomials normalized by

`integral_0^infinity L_m(x)L_n(x) exp(-x) dx=delta_mn`.

Define

`ell_m(a)=E_a[L_m(Q/2)]`,

where `E_a` is the common `C`-tilt. The generating function

`sum_{m>=0} L_m(T) r^m=(1-r)^(-1) exp(-T r/(1-r))`

with

`r=2z/(1+2z)`

gives the exact expansion

`(1+2z) Lambda(a,z)=1+sum_{m>=1} ell_m(a) r^m`.

The first mode is especially important:

`ell_1(a)=1-E_a[Q]/2=1-K''(a/sqrt(3))`.

Therefore constant regression is exactly the vanishing of the first Laguerre
mode, `ell_1(a)=0` for all `a`.

Let `W_a=exp(aC)/E exp(aC)`. The `Q`-marginal Radon–Nikodym derivative is

`r_a(Q)=E[W_a|Q]`

and its Laguerre expansion is

`r_a(Q)=1+sum_{m>=1} ell_m(a) L_m(Q/2)`.

Under the displayed square-integrability assumptions, Parseval and conditional
expectation give

`sum_{m>=1} ell_m(a)^2`
`=chi^2(P_a^Q || chi^2_2)`
`<= E(W_a-1)^2`
`=M(2a/sqrt(3))^3/M(a/sqrt(3))^6-1`.

This is a sharp and reusable positive spectral interface. It controls the full
tilted residual distortion, but does not force the first coefficient to vanish:
the higher modes may carry the distortion.

## 6. Positive-source PDE and the exact obstruction to propagation

For `F` above, the web-side calculation gives

`(partial_z+(2/3)partial_t^2) log F(t,z)`
`=6 Var_{nu_(t,z)}(partial_y log L(y,z)) >=0`.

Here `nu_(t,z)` is the positive Gaussian-heat reweighting of `L(y,z)^3`.
At `t=0`, the full-SF boundary implies

`partial_t^2 log F(0,z)>=3/(1+2z)`

and hence

`partial_a^2 log Lambda(0,z)>=-2z/(1+2z)`,

or, equivalently,

`Var_(0,z)(C)>=1/(1+2z)`.

This is a genuine positive curvature theorem. It is not a rigidity theorem:
the Gaussian law has slack (`Var(C)=1`), and the nonnegative source is also
nonzero for the Gaussian when `z>0`. Therefore neither heat flow nor total
positivity can transport the single boundary `Lambda(0,z)` into the desired
all-tilt equality without an additional mechanism controlling the source.

The covariance Hessian of `log E exp(aC-zQ)` is positive semidefinite, but
`log Lambda` is a ratio after subtracting the `z=0` section. In particular,
`partial_aa log Lambda` has no fixed sign. This rules out treating ordinary
log-convexity as the missing reverse defect.

## 7. Conditional Laguerre sign closure and relaxed no-go

There is a concise conditional closure criterion. If a genuine analytic full-SF
law satisfies, for all sufficiently small `a`,

`ell_1(a) ell_1(-a)>=0`,

then the law is Gaussian. Indeed, if the first nonzero non-Gaussian cumulant has
degree `d`, the full-SF first-row recursion forces `d` to be odd. Then

`ell_1(a)=-c a^(d-2)+O(a^(d-1))`, `c!=0`,

so `ell_1(a)ell_1(-a)<0` near nonzero `a`, a contradiction. Even a one-sided
local inequality `K''<=1` or `K''>=1` would already imply Gaussianity.

The current positive-source, complete-monotonicity, and chi-square-divergence
tools do not produce either sign. This is the precise next closure interface,
not a hidden proof.

For a legal relaxed obstruction, take `(U,V)` standard Gaussian,
`S=U^2+V^2`, independent standard Gaussian `Z`,
`h(S)=exp(-S)-1/3`, and

`C_epsilon=(Z+epsilon h(S))/sigma_epsilon`,
`sigma_epsilon^2=1+4 epsilon^2/45`.

The inverse orthogonal map gives a centered, variance-normalized, exchangeable
three-dimensional law with exact Gaussian residual vector and
`Lambda_epsilon(0,z)=(1+2z)^(-1)`, but

`-partial_z Lambda_epsilon(a,0)`
`=2-(4epsilon/(9 sigma_epsilon))a+O(a^2)`.

This witness is not iid: if two independent scalar marginals had a Gaussian
difference coordinate, Cramer decomposition would force both marginals to be
Gaussian. Thus it is a probability-level no-go outside the iid scalar cone,
not a counterexample to the target problem.

## 8. OU transform, Laguerre mode scaling, and tower interface

For `mu_lambda=P_lambda mu`, the exact Mehler transform is

`Lambda_(mu_lambda)(a,z)`
`=1/(1+2(1-lambda)z)`
` * Lambda_mu(sqrt(lambda)a, lambda z/(1+2(1-lambda)z))`.

Under `r=2z/(1+2z)`, the fractional-linear map is simply

`r'=lambda r`.

Consequently,

`ell_m^(P_lambda mu)(a)=lambda^m ell_m^mu(sqrt(lambda)a)`.

In particular,

`ell_1^(P_lambda mu)(a)=lambda ell_1^mu(sqrt(lambda)a)`.

For a moving-top tower `g_N=P_(q^N)h_N`,

`ell_m^(g_N)(q^(-N/2)a)=q^(mN) ell_m^(h_N)(a)`

and the tilted Laguerre divergence obeys

`Xi_(g_N)(q^(-N/2)a)=sum_(m>=1) q^(2mN) ell_m^(h_N)(a)^2`.

Therefore the sharp sufficient tower interface is:

`Xi_(g_N)(q^(-N/2)a)=o(q^(2N))`

uniformly on every bounded `a`-window

`=> ell_1^(h_N)(a)->0`.

The existing unweighted bottom estimate `||g_N-1||_2<=8q^(3N/2)` does not imply
this tilted estimate, because common tilts probe exponentially shifted spatial
regions. Compatible single infinite towers were already closed by R138;
incompatible moving-top towers remain open.

## 9. Whole-project status and publication audit

The most coherent article-like chain currently is

`n=3 chi-square sample-variance characterization`
`=> zero-divisor/OU shape`
`=> coherent cross-coherence`
`=> iid bispectrum`
`=> common regression`
`=> tilted Laguerre spectrum`.

The irreplaceable unresolved implication is

`Q~chi^2_2 + iid scalar factorization  =>?  ell_1(a)=0 for all a`.

Current evidence grading:

| Round | Content | Evidence level |
|---|---|---|
| R132 | all-row residual chi-square, tails, OU smoothing, weak spatial log bridge | proved analytic under all-row; scalar `RK=1` bridge open |
| R133 | first odd Jacobi packet and finite-row blindness | first packet proved under full-SF; global realization open |
| R136 | arbitrary odd formal input and even formal completion | formal-proved only |
| R138 | zero divisor/root-limsup, Fisher/angular budget, compatible tower rigidity | proved analytic; moving-top tower open |
| R140 | gap/separation/tail to shell-to-energy | proved under explicit geometry; gaps are necessary |
| R141 | normalized zero-shell phase and raw Bochner erasure | proved analytic |
| R142 | positive Gaussian-relative form and Hermite–Toeplitz amplification | proved form-level/analytic; bounded inverse issue remains |
| R143 | coherent Bessel energies and purity cross-coherence defect | genuine Hilbert-space theorem; reverse direction open |
| R144 | iid ridge PDE/cocycle and balanced-convolution positive defect | genuine probability theorem; wrong sign for closure |
| R145 | mixed cumulants, shifted Bessel–Schur, Appell regression | genuine probability inequalities and conditional closure |
| R146 | tilted heat/Laguerre package, positive-source curvature, OU mode scaling | analytically proved under displayed hypotheses; no global rigidity |

Accordingly, the honest current answer to “是否已经有可独立投稿的发表成果” is
still **无**. The strongest defensible description is “a substantial, internally
coherent lemma package around an open characterization problem”, not a completed
publication. The next work should seek a theorem that removes one of the three
explicit gaps: scalar `RK=1` to genuine full-SF, full-SF to constant regression,
or ordinary/Bargmann to spatial `P_3 K_sp`.

## 10. Reproducibility boundary

`audit_r146.py` checks only finite orthogonal algebra, the Laguerre generating
interface at finite truncation, the first-mode identity, Gaussian normalization,
OU fractional-linear scaling, and the relaxed witness constants. Its markers do
not certify an infinite Laguerre expansion, analytic continuation, existence of a
non-Gaussian full-SF law, tower uniformity, or publication novelty.
