# 2026-09-04 — R18 Laguerre–Abel endpoint audit

- Branch: `chi2-laguerre-abel-endpoint-r18-2026-09-04`.
- Scope: theory-only exact Abel transform and finite symbolic checks.
- Certified: Abel/Poisson formula, positive quadratic kernel, operator form,
  and endpoint non-coercivity witness `c=(1,-1)`.
- Limitation: only `d0`–`d3` are present in the R17 source; no all-orders
  Fock-determined `D(r)` formula was available. No Gaussian rigidity claim.
- Decision: B; the missing full `D(r)` kernel/coercivity is now explicit.

# 2026-09-05 — Theory route framework and R8 cross-parameter correction

- Added `THEORY_ROUTE_FRAMEWORK.md` as the durable theory outline for the
  Positive Backward-Tower Exact Zero-Set Rigidity program.
- The framework records the target theorem, the exact-defect/Fock, positivity,
  backward-OU, and spatial-escort layers, plus the stop conditions for routes
  that only produce finite-jet or operator-only evidence.
- R8 web review audited the transport identities and corrected the status of
  the former integrated-compensation target: `∫_0^q S = -Var_{nu_q}(K'_q)`
  under the Gaussian endpoint condition, so it is equivalent to rigidity and
  is not an intermediate lemma.
- The current concrete gap is the anisotropic same-factor posterior-variance
  coherence behind `Var(Y|X=x) <= tau`; this is recorded as the next minimal
  OPEN problem. No finite computation was needed.
- From this round onward, each C2C theory prompt must ask ChatGPT to read the
  framework and this append log through the connector before proposing work.

# 2026-09-05 — R9 posterior bridge and anisotropic ordering reduction

- Web review confirmed the posterior identities
  `W-τ=τ²K''_q`, `E_{ν_q}W=τ`, and that pointwise `W≤τ` would already force
  `K''_q=0`; it is therefore not a useful intermediate estimate.
- Audited new bridge identity: for `H_q=P_{s-q}H_s`, with `μ_{q,s}` the `Y`
  marginal of the cubic-escort three-copy bridge and
  `𝒟=E_{ν_q}Var_{π_{q,s}}(K'_s(Y))`,
  `E_{μ_{q,s}}K''_s=-𝒟≤0`, while `E_{ν_s}K''_s=0`.
- Audited escort–MMSE identity: if `λ_q=p_q dx`, `ν_q∝p_q^3dx`, and
  `ω_q=p_q^2/∫p_q^3`, then
  `E_{λ_q}W=τ-τ²E_{λ_q}(K'_q)^2`, `E_{ν_q}W=τ`, and
  `Cov_{λ_q}(W,ω_q)=τ²E_{λ_q}(K'_q)^2≥0`.
- Exact obstruction is now a missing ordering/coherence statement comparing the
  anisotropic marginal `μ_{q,s}` with the scalar escort `ν_s`; ordinary positivity,
  total positivity, finite nested horizons, and arbitrary tangents do not provide it.
- R10's proposed curvature ordering is now treated as a strict probability-level
  no-go for any non-Gaussian positive top level, not as an OPEN intermediate lemma.

# 2026-09-05 — R10 residual-Fisher reduction and shell correction

- Validated the three-copy residual dictionary
  `I_perp(q,s)=2 D_{q,s}` and
  `E_{mu_{q,s}} K''_s=-D_{q,s}=-(1/2)I_perp(q,s)`.
  For a non-Gaussian positive top level, posterior full support makes this strict
  for every `q<s`; therefore the proposed reverse curvature ordering is a strict
  probability-level no-go, not an OPEN intermediate estimate.
- Validated the nested decomposition
  `D_{q,s}=D_{q,r}+E_{mu_{q,r}} Var_{pi_{r,s}}(K'_s)` and the regular small-bridge
  asymptotic `D_{s-tau,s}/tau -> E_{nu_s}(K''_s)^2`.
- Corrected a material error in the web response: under non-Gaussian
  `lambda_s^3`, `Q/s` is not `chi^2_2`; that law belongs to the Gaussian reference.
  Consequently the claimed exponential shell density and complete monotonicity of
  `D/r` are not established and are removed from the framework.
- The pre-R11 minimal OPEN was Residual-Fisher Production Coherence: whether a
  genuine positive same-factor all-degree tower has a nested small-bridge sequence
  with `D=o(tau)`, or can rigorously sustain `D>=c tau`. R11 reclassified this after
  the fixed-factor depth audit; no finite Codex computation was needed.

# 2026-09-05 — R11 fixed-factor depth decay and compatible-tower no-go

- Independently audited the OU–heat conjugacy with a distinct OU factor `rho`:
  `P_rho=S_sqrt(rho) P_heat_(1-rho)`. For `H_a^(j)=P_heat_(1-a)g^(j)`, an exact
  backward step is `H_a^(j)(x)=H_(rho a)^(j+1)(sqrt(rho)x)`. The fixed factor
  therefore creates moving heat parameters and synchronized dilation; it does not
  create a fixed-top-level small-bridge sequence.
- For `Delta_j(a)=D^(j+1)_(rho a,a)`, the chain-rule scaling was audited as
  `Delta_j(a)=rho Delta_(j+1)(rho a)`, equivalently
  `a Delta_j(a)=(rho a) Delta_(j+1)(rho a)`.
- Positivity of `g` and the posterior Hessian give the outer-horizon cap
  `0<=D_(q,s)<=1/(1-s)` for `0<q<s<1`. Combining it with nested production and the
  scaling yields, for any genuine depth-N tower,
  `0<=D^(1)_(rho s,s)<=rho^(N-1)/(1-s)`.
- Consequence: a first pair that is projectively compatible with arbitrary depth is
  Gaussian (the bound forces `D=0`, then the R10 strict residual-Fisher no-go and
  heat injectivity close the argument). This rules out compatible non-Gaussian exact
  infinite fixed-factor towers without using the near-Gaussian assumption.
- Scope correction: the original problem still permits mutually incompatible
  depth-N towers. The bound only gives exponentially small production for that
  sequence, not exact zero at finite N. The new minimal OPEN is
  `Depth-to-Zero Production Rigidity`: obtain depth-independent zero-set isolation /
  tensor coercivity from all-degree exactness plus positivity, or identify a genuine
  probability-level tail-escape obstruction. No Codex computation was needed.

# 2026-09-05 — R12 exact-law compactness and OU-invariant-shape obstruction

- Logic-level audit: the new tail and OU statements are unconditional for the
  genuine full exact probability class `Q=sum_i(X_i-Xbar)^2 ~ chi^2_2`. They must not
  be silently inferred from a single scalar `RK=1` equation unless that equivalence
  has separately been proved. The requested nonzero `P_3K` charge sector remains a
  separate qualifier.
- From `Q >= (X1-X2)^2/2`, the exact chi-square Laplace transform, and conditional
  Jensen, obtained the uniform bound
  `E exp(eta X^2) <= exp(-eta)/(1-4 eta)` for `0<eta<1/4`. This gives uniform
  probability tightness, fixed-moment uniform integrability, and local complex MGF
  control across exact laws and tower depths; physical probability-tail escape is
  excluded.
- The same MGF estimate gives a law-independent exponential Hermite coefficient
  envelope. With OU Hermite scaling and centered variance-one cancellation of modes
  one and two, every depth-N top endpoint satisfies the uniform estimate
  `||P_(rho^N) h_N - 1||_2 = O(rho^(3N/2))` for large N.
- Audited exact OU closure geometrically: the residual-plane vector has chi-square
  radius and is sent to `sqrt(t) R + sqrt(1-t) G`; isotropic Gaussian noise preserves
  the Gaussian radial law. Thus `g in E => P_t g in E` for the full exact class.
- A single genuine nonGaussian exact law automatically generates mutually
  incompatible finite-depth towers by `g_N^(j)=P_(rho^(N-j))h`; hence Case B is
  essentially the original nonGaussian exact-law existence problem. For the required
  `P_3K != 0` sector, charge survival along this orbit must still be proved, not
  assumed.
- Absolute local isolation of Gaussian in the exact class is equivalent to global
  uniqueness because of OU closure, `L2` convergence, and OU injectivity. Therefore
  `D_N -> 0` plus ordinary continuous coercivity cannot yield finite-N exact zero.
  Physical tail escape is gone; only amplitude/spectral high-chaos escape remains.
- Reclassified the minimal OPEN as `OU-Invariant Shape Rigidity`: find an
  amplitude-normalized OU-homogeneous same-factor tensor invariant, or prove a
  genuine spectral noncompactness obstruction. No Codex computation was needed.

# 2026-09-05 — R13 primitive shape and Bochner-tail closure

- Scope audit: all reverse-OU statements below are for the genuine full exact
  class `Q=sum_i(X_i-Xbar)^2 ~ chi^2_2`, not for an unproved scalar `RK=1`
  identity. The `P_3K != 0` charge sector remains separate.
- Reverse exactness: in the residual plane,
  `R_t=sqrt(t)R+sqrt(1-t)G`. The conditional Laplace transform and the change
  `theta=t z/(1+(1-t)z)` show that if `P_t mu` is full exact, then `mu` is
  full exact. Thus actual positive OU preimages cannot leave the exact class.
- Define the probability-level maximal backward radius
  `r(mu)=sup{r>=1: mu=P_(r^-2)nu}`. The inverse characteristic-function
  candidate is `phi_nu(u)=phi_mu(r u) exp((r^2-1)|u|^2/2)`. Uniform exact-law
  sub-Gaussian bounds make preimages tight; cumulant scaling
  `kappa_m(nu)=r^m kappa_m(mu)` makes `r=+infinity` impossible for a
  nonGaussian law. A maximizing preimage exists at the probability-law level
  by weak compactness and uniform integrability, but it need not be an `L2`
  density or belong to the K-tensor regularity class.
- The radius and primitive representative are OU-invariant in the expected
  orbit coordinates:
  `r(P_tmu)=r(mu)/sqrt(t)` and `Pi(P_tmu)=Pi(mu)`. If `d>=3` is the first
  nonzero normalized Hermite moment, then
  `Theta(mu)=r(mu)|a_d(mu)|^(1/d)=|a_d(Pi(mu))|^(1/d)>0` is an OU-invariant
  primitive-shape scalar. It separates amplitude from shape but does not prove
  primitive uniqueness.
- Under the score regularity needed for the anchor expansion, the R13 local
  residual-Fisher quantity obeys
  `F_mu(a)=C_(d,rho) a^(d-1)|a_d(mu)|^2+o(a^(d-1))`, with
  `C_(d,rho)=d E Var[psi_(d-1)(Xi+sqrt(1-rho)Z)]>0` and
  `C_(3,rho)=(1-rho)(3-rho)`. Its scaling
  `F_(P_tmu)(a)=t F_mu(t a)` means it decays like `t^d` along an orbit, so it
  cannot supply the missing primitive coercivity from R11's fixed-s depth
  estimate.
- Strict obstruction: a depth-N first law factors as
  `mu_N=P_(t_N)pi_N`, `t_N<=rho^N`, `r(pi_N)=1`. R11 controls only `t_N`; any
  OU-invariant shape sees only `pi_N`. Combining the two cannot close Case B
  without primitive exact-shape uniqueness.
- Remaining escape is global inverse-OU positive-definiteness: primitive laws
  may conceivably converge weakly to Gaussian while, for fixed `r>1`, the
  inverse candidate fails Bochner positivity only at unbounded frequencies,
  Gram sizes, degenerate point configurations, or vanishing margins. This is
  distinct from the already excluded physical X-tail escape. `P_3K` survival
  is automatic only in the local d=3 leading-mode regime; general survival is
  still open.
- Reclassified the minimal OPEN as
  `Primitive Exact Shape Rigidity / Bochner-Tail Closure`: determine whether
  same-factor product plus all-degree exactness rules out that global
  inverse-OU tail escape. No Codex computation was needed; the remaining work
  is an infinite-dimensional positivity/shape argument.

# 2026-09-05 — R14 finite-complexity Bochner closure

- R14 first re-audited the R13 reverse-OU radius and primitive endpoint. Those
  probability-level statements remain valid with the same caveat: the
  primitive endpoint need not be an `L2` density or have the project's score/K
  regularity.
- New exact obstruction: writing
  `a_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`, the full exact law obeys
  `average_theta product_j phi(a_j(theta)u)=exp(-u^2/2)`. For the inverse
  candidate `Phi_r(u)=exp((r^2-1)u^2/2) phi(r u)`, the identity remains exactly
  true because `sum_j a_j(theta)^2=1`. Its finite Gram/Hadamard tensor lifts
  remain true even when `Phi_r` is not positive definite. Hence exact
  equality, even in the all-degree tensor hierarchy, cannot by itself detect
  the primitive boundary; Bochner positivity is genuinely additional.
- Finite-complexity closure: for primitive `pi_N => gamma`, fixed `r>1`, and
  `K_N(u)=exp((r^2-1)u^2/2) phi_(pi_N)(r u)`, the R12 square-exponential bound
  gives `K_N -> exp(-u^2/2)` in every fixed local `C^k` topology. For fixed
  Gram size `m`, divide the determinant by the squared Vandermonde and use
  confluent divided differences. The Gaussian kernel has
  `D_m=e^(-sum x_i^2) det[e^(x_i x_j)]`, and Cauchy-Binet's first term gives
  `D_m/Vandermonde^2 >= e^(-m L^2)/product_{j=0}^{m-1} j!` on `|x_i|<=L`.
  Therefore, for every fixed `r,M,L`, all Gram tests with `m<=M` and bounded
  frequency are eventually PSD, even with arbitrary point collisions.
- This sharpens R13's four-way list: for primitive inverse candidates, any
  negative Bochner witness must escape through unbounded frequency diameter or
  unbounded Gram/spectral rank. Collision, small Gaussian eigenvalue margin,
  and vanishing finite-witness margin are not independent channels once the
  confluent determinant argument is used.
- Strict remaining obstruction: bounded-window `C^k` convergence does not
  control all Gram sizes because the Gaussian kernel's compact integral
  operator has eigenvalues tending to zero. The needed target is a uniform
  Gaussian-relative quadratic-form estimate, not ordinary local smooth
  convergence. The same-factor angular map is inward-contracting
  (`|a_j|<=sqrt(2/3)`), so it gives no outward frequency positivity induction.
- Conditional closure: a uniform bounded-complexity negative-witness theorem,
  or a bounded-frequency reduction plus Gaussian-relative form compactness,
  would rule out primitive exact laws converging to Gaussian. Without one of
  these, the minimal OPEN is now `Relative Bochner Closure`, with frequency
  escape and spectral-rank escape as the only remaining channels.
- `P_3K` was kept separate. The d=3 leading-mode local survival statement is
  safe; general primitive endpoint regularity and charge survival remain OPEN.
  No numerical or long Codex computation was needed; this was a proof-level
  audit and a durable framework/worklog update.

# 2026-09-05 — R15 local Bochner-to-Hankel reduction

- R15 re-read the post-R14 framework/worklog through the repaired bridge and
  attacked only `Relative Bochner Closure`. The inverse candidate for a genuine
  full-exact primitive law is
  `K_r(z)=exp((r^2-1)z^2/2) phi_pi(rz)`, with fixed `r>1`.
- Unconditional local-to-global lemma: R12's square-exponential bound gives
  `K_r` an entire order-2 growth estimate and inverse formal moments
  `m_k^(r)=i^(-k)K_r^(k)(0)` of Gaussian-type moment growth. If `K_r(x-y)` is
  PSD for every finite Gram configuration in any nonempty interval, confluent
  finite differences at zero give all inverse Hamburger matrices PSD. Hamburger
  then supplies a probability law; the order-2 growth gives a square-exponential
  moment and moment determinacy, so its characteristic function must equal
  `K_r` globally. This is a positive r-backward OU preimage, contradicting
  primitiveness. Thus every `L>0` already contains a finite negative witness;
  frequency escape is eliminated.
- Define `M_r(pi)=min{M: H_M^(r) is not PSD}`. For every primitive law this
  order is finite. If primitive full-exact laws `pi_N=>gamma`, each fixed inverse
  Hankel matrix converges to the strictly positive Gaussian one, hence
  `M_r(pi_N)->infinity`. The remaining Bochner obstruction is therefore purely
  an unbounded Hamburger/Gram rank escape.
- The proposed Gaussian-relative quadratic-form estimate on any bounded window
  is not a weaker compactness lemma: the local negative witness has
  `Q_K<0` while the Gaussian form is strictly positive, so its relative defect
  is `>1` (possibly infinite) for every primitive inverse candidate. Such an
  estimate would already be a closure theorem and cannot be assumed as an
  intermediate consequence.
- A proof audit of the Hermite stress test was recorded. With odd `n`,
  `q_n=1+A_n psi_(2n)` and `g_n=P_(r^-2)q_n`, choose
  `A_n=2/|min psi_(2n)|`. Then `q_n` is signed, `g_n` is eventually positive,
  centered and variance-one, and `g_n->1` in `L2`. Cauchy-Schwarz and
  `||psi_(2n)||_2=1` give uniform `E exp(eta X^2)` for every `eta<1/4`;
  orthogonality makes all moments below order `2n` Gaussian, while a higher
  Hankel matrix must fail because `q_n` is signed. This is not a full-exact
  counterexample; it proves only that positivity, MGF tightness and fixed-order
  Hermite convergence alone cannot bound inverse-Hankel rank.
- Minimal OPEN is now `Uniform Inverse-Hankel Rank Closure`: does the genuine
  same-factor all-degree exact hierarchy plus forward positivity force an
  N-independent finite inverse-Hankel failure order? `P_3K` remains separate;
  no uniform charge-to-Hankel implication was obtained. No long computation or
  numerical scan was needed.

# 2026-09-05 — R16 primitive closedness / tail-to-head viability

- R16 re-read the post-R15 local record through the repaired connection. It did
  not prove a uniform inverse-Hankel bound. Its substantive result is a sharper
  reformulation: `M_r(pi)` is the exit time of an inverse exact Jacobi control
  trajectory from the Hankel viability strip.
- Using the already established full-exact Jacobi factorization, with formal
  inverse moments `m_k^(r)`, Jacobi coefficients `alpha_j,beta_j`, and
  `S_j=sum_{ell<=j} alpha_ell`, the exact `Q^n` identity has the form
  `G_n=(2^n/3^(n-1))*product_{j<n} beta_j*(beta_n+S_(n-1)^2-B_n)`.
  Before the first Hankel exit this gives `beta_n=B_n-S_(n-1)^2`; with
  `u_n=S_(n-1)/sqrt(B_n)`, positivity is exactly `|u_n|<=1`.
- The `Q^n` equation is triangular in the moments: the coefficient of the new
  even moment is `3(2/3)^n`, while `m_(2n-1)` cannot occur because a term with
  that exponent leaves total exponent one in the other variables and is killed
  by centering (`m_1=0`). Thus higher exact equations do not algebraically feed
  back to previously selected odd controls. Any uniform rank bound, if true,
  must come from nonlocal infinite-tail positivity/growth.
- Finite-horizon no-go: for any finite `M`, perturb a Gaussian moment prefix by a
  small nonzero `m_(2M-1)` while keeping `m_(2M)` Gaussian. Strict positivity of
  the Gaussian truncated Hankel block and the one-dimensional truncated
  Hamburger theorem give a real positive centered variance-one non-Gaussian law
  passing the first `M` exact `Q` checks. A forward OU step preserves positivity
  and the same finite `Q`-moment checks. This is not a full-exact counterexample;
  it rules out only finite-prefix proofs of a uniform `M(r)`.
- Let `E` be the genuine full-exact probability class and
  `A_M(r)={mu in E: H_M^(r)(mu)>=0}`. Combining fixed-moment continuity from R12
  with the R15 local-Hamburger lemma gives
  `intersection_M A_M(r)={mu in E: backward_radius(mu)>=r}`.
  Consequently fixed-r Uniform Inverse-Hankel Rank Closure is equivalent to
  primitive laws not accumulating on the deeper backward-divisible stratum;
  over all `r>1`, it is equivalent to weak closedness of the primitive stratum
  inside `E`. Ordinary probability/MGF compactness supplies only upper
  semicontinuity of backward radius and permits an upward jump in the limit.
- `P_3K` remains logically separate. No audited implication from nonzero third
  charge to `m_3!=0`, or to a uniformly bounded inverse-Hankel failure order,
  was found. Even d=3 local survival can have arbitrarily small amplitude while
  every fixed Gaussian Hankel block remains strictly interior.
- Minimal OPEN is now `Primitive Closedness / Tail-to-Head Viability`: determine
  whether full-exact probability positivity and uniform exact-law growth force
  backward divisibility depth to be stable under weak limits. A rank-escape
  sequence would have every fixed prefix asymptotically Gaussian but
  `M_r(pi_N)->infinity`; no genuine full-exact example is known. No long
  numerical computation was needed.

# 2026-09-05 — R17 OU–Laguerre spectral-tail viability

- R17 re-read the post-R16 framework/worklog through the repaired connection.
  The genuine full-exact class `E` is weakly compact and weakly closed under the
  R12 uniform square-exponential bound: tensor-product weak convergence and the
  continuous map `Q` preserve the exact `chi^2_2` law, while uniform
  integrability preserves centering and variance.
- For fixed `r>1`, the backward-divisible stratum satisfies
  `E_r={mu in E: radius(mu)>=r}=P_(r^-2)(E)`, by forward-OU continuity and
  reverse exactness. Hence `E_r` is compact/closed and the backward radius is
  upper semicontinuous. Primitive closedness needs the missing opposite
  stability; ordinary probability/MGF compactness does not supply it.
- New exact OU–Laguerre coordinates: with
  `U=(X1+X2+X3)/sqrt(3)=sqrt(3)*barX` and `T=Q/2~Exp(1)`, define
  `C_(ell,n)(mu)=E[psi_ell(U)L_n(T)]`. Common/residual orthogonal coordinates
  show the exact diagonal law
  `C_(ell,n)(P_s mu)=s^(n+ell/2) C_(ell,n)(mu)`.
  The local `conditional_laguerre_odd_r17` replay already verifies the ordinary
  Laguerre convention, orthogonality, odd highest-moment triangularity, and the
  finite conditional-moment formulas; the scaling itself follows from chaos
  degree `ell+2n`.
- For a positive full-exact law, conditional Bessel/Parseval gives
  `sum_n C_(ell,n)^2 <= E psi_ell(U)^2 <= A_ell`, with `A_ell` uniformly
  controlled for fixed `ell` by R12 growth. Therefore any positive
  `r`-backward preimage forces the all-order sector inequality
  `sum_n r^(4n+2ell) C_(ell,n)(mu)^2 <= A_ell`.
  In the `ell=1` sector, `C_(1,n)=sqrt(3)c_n` for
  `c_n=E[barX L_n(T)]` and `E U^2=1`, giving
  `3*sum_n r^(4n+2)c_n^2 <= 1` and the individual radius bound
  `radius(mu) <= (3*c_n^2)^(-1/(4n+2))` when `c_n!=0`.
- This is a genuine full-exact all-order viability constraint, but only
  sector-wise. It does not yet give cross-sector weighted-tail tightness, so it
  does not prove primitive closedness. The missing exchange is between weak
  coefficientwise convergence and sums weighted by `r^(4n+2ell)`; mass may move
  to `n->infinity` unless simultaneous all-degree control is proved.
- Stronger ordinary-class no-go: for odd `n`, let
  `psi_(2n)=H_(2n)/sqrt((2n)!)`, `b_n=min psi_(2n)<0`, and
  `g_n=1+(-1/b_n)psi_(2n)` relative to Gaussian. Each is a nonnegative
  centered variance-one density touching zero. Its inverse OU candidate becomes
  negative at the minimum for every nontrivial inverse step, so it is primitive;
  `a_n=O(n^(1/4))` gives weak convergence to Gaussian and the generating
  function gives uniform square-exponential moments for every `eta<1/4`.
  Orthogonality makes its first `n-1` `Q`-moments exactly chi-square. This is
  not a full-exact counterexample (the nth `Q` moment changes), but proves that
  ordinary positivity, growth, and arbitrarily long finite exact prefixes cannot
  replace simultaneous all-degree exactness. It also has `||g_n-1||_2=a_n`,
  so it is a weak/MGF, not an L2-near-Gaussian, stress test.
- Minimal OPEN is now `All-Degree Spectral-Tail Tightness`: can genuine
  full-exact product structure plus positivity prevent OU-eigenmode,
  Laguerre, and Jacobi control mass from escaping to infinite chaos degree?
  A sufficient target is uniform inverse-weighted tail tightness across the
  complete conditional/angular sectors. `P_3K` remains separate: no audited
  charge-to-Laguerre lower bound or uniform inverse-Hankel implication was
  obtained. No long numerical computation was needed.

# 2026-09-05 — R18 same-factor matrix Hardy gain / relative tail-to-head coercivity

- R18 re-read the durable framework and worklog through the repaired connection
  before starting. It attacked only the R17 target `All-Degree Spectral-Tail
  Tightness`, and did not claim primitive closedness or Gaussian rigidity.
- The complete conditional generating function is a single cross-sector object.
  With `U=(X1+X2+X3)/sqrt(3)`, `T=Q/2~Exp(1)`, `C_(ell,n)=E[psi_ell(U)L_n(T)]`,
  `0<=q<1`, and `d=1-q`, the tilted triple law
  `dP_q=d^(-1) exp(-qT/d)d(mu^3)` gives
  `M_mu(q,z)=E_Pq exp(zU-z^2/2)
  =sum_(ell,n) C_(ell,n) q^n z^ell/sqrt(ell!)`.
  Its kernel `K_q(z,w)=exp(z*conj(w))*M_mu(q,z+conj(w))` is PSD because it is
  a Gram kernel. A Hubbard–Stratonovich step gives the same-factor cubic
  representation through `A_q(y)=E_mu exp(yX-qX^2/(2d))`:
  `M_mu(q,z)=d^(-1)exp(-z^2/2)E_G A_q((z+sqrt(q/d)G)/sqrt(3))^3`.
- A new unconditional spectral lemma follows from Mehler. If
  `a_m(mu)=E_mu psi_m(X)`, then for `rho<1`, the R12 square-exponential bound
  gives a uniform `sum_m rho^m a_m(mu)^2` bound. Unitary common/residual
  rotation preserves total-degree energy, so the full conditional/angular
  coefficients `B_(D,alpha)` satisfy
  `sup_(mu in E) sum_(D,alpha) rho^D |B_(D,alpha)|^2 <= K(rho)^3`.
- More importantly, in `E_r`, `r>1`, write `mu=P_(r^-2)nu`, `nu in E`. OU degree
  scaling and the preceding subcritical estimate imply, for `1<lambda<r^2`,
  `sup_(mu in E_r) sum_(D,alpha) lambda^D |B_(D,alpha)|^2
  <= K(lambda/r^2)^3`; for `1<lambda_0<lambda<r^2`, the tail is bounded by
  `K(lambda/r^2)^3(lambda_0/lambda)^M`. Thus complete cross-sector
  supercritical moving-scale tightness is already true inside the deeper
  backward-divisible stratum.
- A conditional closure target is now explicit. If `pi in E_R`, `1<r<R`, write
  `pi=P_(R^-2)xi` and `nu_r=P_(r^2/R^2)xi`. Chebyshev plus the OU kernel gives a
  Gaussian minorant `nu_r >= c gamma_tau` for every `0<tau<1-r^2/R^2`, hence
  `L_(nu_r)(p^2)>=c E_(gamma_tau)p^2`. Therefore a relative quadratic-form
  estimate
  `sup_p |(L_(N,r)-L_(nu_r))(p^2)|/E_(gamma_tau)p^2 -> 0`
  would force positivity of the limiting inverse formal form and, by the R15
  Hamburger/moment-determinacy bridge, rule out primitive convergence into
  `E_R`. This is the missing relative matrix/Loewner Hardy gain.
- Strict no-go: conditional/angular PSD, exact radial `T~Exp(1)`, and uniform
  growth alone do not control the Abel boundary. An explicit exchangeable but
  non-iid construction with `U_omega=sigma_omega Z+epsilon(cos(omega T)-
  (1+omega^2)^(-1))` has Laguerre transform
  `1/(1+omega^2(1-q)^2)-1/(1+omega^2)`; its complex poles approach `q=1` and
  its spectral mass escapes to high Laguerre degree. It is deliberately not a
  `mu^3` law, so it is not a genuine full-exact counterexample; it only shows
  that same-factor iid factorization must be used essentially.
- `P_3K` remains separate. No audited charge-to-Laguerre/Loewner lower bound or
  charge-to-Hankel rank estimate was found. A nonzero qualitative charge may
  still sit at radial index `n->infinity`.
- Local proof-level checks: `F:/anaconda3/python.exe
  conditional_laguerre_odd_r17/audit_r17.py` passed with
  `R17_AUDIT_COMPLETED`; `F:/anaconda3/python.exe
  laguerre_abel_endpoint_r18/audit_r18.py` passed with
  `R18_AUDIT_COMPLETED` and retained its earlier decision that the Abel
  endpoint is non-coercive. No optimizer, Gram scan, long numerical campaign,
  or remote computation was needed.
- Minimal OPEN is now `Same-Factor Matrix Hardy Gain / Relative Tail-to-Head
  Coercivity`: can genuine iid same-factor all-degree exactness make the
  supercritical tail bound open/stable around `E_R`? The exchangeable model is
  not promoted to a project counterexample, and Gaussian rigidity remains
  OPEN.

# 2026-09-05 — R19 posterior witness alignment / reverse-Schur coercivity

- R19 re-read the durable framework and worklog through the R18 commit
  `8d38b82` before working. It remained restricted to the genuine full-exact
  iid class and did not claim Gaussian rigidity.
- The new coordinate is the maximal Gaussian component
  `g(mu)=sup{a: mu=rho*gamma_a}`, which is equivalent to the backward radius by
  `g(mu)=1-r(mu)^(-2)`. Under the quadratic/Esscher posterior
  `dmu_(t,y) proportional to exp(yx-tx^2/2)dmu`, complete-the-square algebra
  gives the exact conjugacy `g(mu_(t,y))=g(mu)/(1+t*g(mu))`. Thus posteriorization
  preserves, rather than removes, the primitive boundary.
- For `r>1`, `d_r=1-r^(-2)`, define
  `sigma_(r,t)^2=d_r/(1+d_r*t)` and
  `B_(r;t,y)(z)=exp(-sigma_(r,t)^2*z^2/2)A_t(y+z)/A_t(y)`. In the established
  growth/determinacy range, `mu in E_r` is equivalent to this fixed-slice
  posterior deconvolution being a probability MGF, or equivalently to the
  complete posterior Wick–Hankel quadratic form
  `W_(r,t,y)[p]=E_(mu_(t,y))[(exp(-sigma_(r,t)^2*partial_x^2/2)p^2)(X)]`
  being nonnegative for every polynomial `p`.
- If `pi in E_R` and `1<r<R`, the limit has a strict posterior Gaussian margin
  `Delta_(R,r,t)=(d_R-d_r)/((1+d_R*t)(1+d_r*t))>0`. Therefore a relative
  Wick–Hankel convergence estimate on one fixed posterior slice would force
  positivity for all polynomial squares and, via Hamburger determinacy, rule out
  primitive convergence into `E_R`.
- The same-factor iid cube can be rewritten with the escort
  `deta_t(y)=(1+t)A_t(y)^3 dgamma_(t/3)(y)` and residual coefficients satisfying
  `sum alpha_j=0`, `sum alpha_j^2=1` as an escort-averaged cubic identity for
  the candidates `B_(r;t,y)`. Its second-order content is only a positive
  average variance deficit, not a pointwise Loewner floor.
- R19's strict iid-compatible obstruction is a quantifier mismatch: primitive
  slices yield `for every y there exists a high-rank negative witness`, while
  the cubic average would need `there exists one coherent witness` effective
  on a nontrivial set of `y`. No reverse-Schur/common-witness theorem is known
  here. Log-convexity only reaches rank 2; posteriorization is an exact
  conjugacy; translation covariance only relabels the escort parameter.
- `P_3K` remains logically separate. No charge-to-Laguerre, charge-to-Loewner,
  or fixed-rank negative lower bound was obtained, and no genuine full-exact
  iid non-closed sequence was constructed.
- Added `posterior_witness_alignment_r20/audit_r20.py`. It passed six small
  symbolic checks and printed `R20_AUDIT_COMPLETED`: Gaussian-component
  conjugacy, posterior deconvolution moments, strict gap, Gaussian escort
  identity, Gaussian escort normalization, and translation covariance. The
  Gaussian identity check is explicitly only a consistency check, not a
  rigidity proof.
- Minimal OPEN is now `Same-Factor Uniform Witness Alignment / Reverse-Schur
  Coercivity`. Gaussian rigidity remains OPEN.

# 2026-09-06 — R20 affine-Hankel diagonal capture / multiscale reverse-Schur

- R20 re-read the durable framework and worklog through commit `7ec40ac` before
  working. It stayed within the genuine full-exact iid class: no finite-prefix,
  formal-kernel, exchangeable, or Gaussian-only object was treated as a counterexample.
- The posterior deconvolution slices have an exact Esscher-affine relation. With
  `C(z)=B_(r;t,0)(z)`,
  `B_(r;t,y)(z)=exp(sigma^2*y*z) C(y+z)/C(y)`. Their Hankel Gram matrices are
  positive scalar plus invertible positive diagonal congruences of the same base
  Hankel kernel at translated nodes. Hence minimum negative-Gram size is invariant
  in `y`, and a base witness can be explicitly transported to every posterior slice.
  The former slice-wise witness-alignment obstruction is therefore solved.
- The same-factor cubic is exactly a diagonal tensor compression:
  `A1 o A2 o A3 = J^*(A1 tensor A2 tensor A3)J`, where
  `Je_i=e_i tensor e_i tensor e_i`. The remaining geometry is multiscale affine
  alignment across `y/2+alpha_j*s` and dimension-free diagonal-tensor capture.
- A strict finite-dimensional generic reverse-Schur no-go was audited with the
  tridiagonal Toeplitz matrix `A_m=I+(3/5)(S+S^*)`, `m>=5`: `A_m` is indefinite,
  while `A_m^(o3)` is positive definite with lower eigenvalue above `71/125`.
  Its spread-out negative sine mode has diagonal-capture mass at most `8/m^2`.
  This is not a probability or full-exact iid counterexample; it only rules out a
  generic Loewner-to-Hadamard converse.
- Conditional closure now requires a Hankel-specific negative-direction alignment,
  a uniform diagonal-capture lower bound, and dimension-independent domination of
  the positive remainder. Overlap alone does not force a negative compressed
  Rayleigh quotient.
- `P_3K` remains disconnected: no charge-to-capture, charge-to-Laguerre, or
  charge-to-Loewner quantitative bridge was obtained, and no genuine full-exact
  iid non-closed sequence was constructed.
- Extended `posterior_witness_alignment_r20/audit_r20.py` with symbolic/numeric
  checks for the Esscher-affine congruence, diagonal compression, Toeplitz
  reverse-Schur no-go, and `O(m^(-2))` capture bound. The run passed and printed
  `R20_AUDIT_COMPLETED`; it is an algebraic consistency audit, not a rigidity proof.
- Minimal OPEN is now `Affine-Hankel Diagonal-Capture / Multiscale Reverse-Schur`.
  Gaussian rigidity remains OPEN.

# 2026-09-06 — R21 post-failure tensor-tail domination

- R21 re-read the durable framework and worklog through commit `8075da1` before
  working. It remained within the genuine full-exact iid inverse formal hierarchy;
  no finite matrix, non-iid object, or formal candidate was treated as a full-exact
  probability counterexample.
- A two-dimensional residual rotational lift was isolated. For
  `A A^T=I_2`, `A^T A=I_3-11^T/3`, the SO(2)-average of any residual polynomial
  square depends only on `Q=|AX|^2`; existing all-degree exactness therefore
  identifies its formal value with the corresponding `gamma_2` value. This is an
  algebraic lift inside the existing formal hierarchy, not a positivity claim.
- If the first nonflat inverse-Hankel failure is at `M`, with
  `h_0,...,h_(M-1)>0` and `h_M<0`, degree-`M` residual polynomial tests have the
  exact decomposition `h_M sum_j |H_M(O v_j)|^2 + R_F(O)`, with `R_F>=0`.
  Rotational averaging gives the first-pivot capture factor
  `3(2/3)^M ||H_M||_(L2(S1))^2`; pointwise residual coefficients obey the same
  exponential scale. Thus a dimension-free reverse-Schur theorem using only the
  first failing block is impossible even in the genuine iid residual geometry.
- For the ridge, this multiplier is
  `lambda_(2M)=3(2/3)^M binom(2M,M)/4^M`, asymptotic to
  `3(2/3)^M/sqrt(pi*M)`, matching the previously audited even-mode Fock loss.
- The whole cubic hierarchy is not thereby ruled out. At degree `3M`, the
  `(M,M,M)` tensor partition has a triple-negative `h_M^3` contribution with exact
  angular coefficient
  `Gamma_M=((3M)!/(M!^3))^2 binom(2M,M)/(54^M*4^M)`, whose Stirling scale is
  `3(27/2)^M/(4*pi^(5/2)*M^(5/2))`. Unknown signs and sizes of
  `h_(M+1),...,h_(3M)` and other partitions may still cancel it.
- The new conditional closure target is therefore post-failure Jacobi/tensor-tail
  domination: a bound such as
  `R_M <= (1-epsilon) Gamma_M |h_M|^3` for a suitable degree-`3M` test would
  expose the negative pivot and close primitive rank escape. No such bound is
  currently proved.
- The residual `cos(3*theta)` harmonic is not the nonlinear log-density charge
  `P_3K`; no quantitative `P_3K` bridge was found. Gaussian rigidity remains OPEN,
  and no genuine full-exact iid non-closed sequence was constructed.
- Added `post_failure_tensor_tail_r21/audit_r21.py` and its README. The audit passed
  residual projection geometry, a representative rotational lift, first-failure
  capture/ridge multiplier, and the exact `Gamma_M` formula with a small
  log-Stirling check, printing `R21_AUDIT_COMPLETED`.
- Minimal OPEN is now `Post-Failure Tensor-Tail Domination`. Gaussian rigidity
  remains OPEN.

# 2026-09-06 — R22 adjacent heat-Hankel transversality / flat leakage

- R22 re-read the durable framework and worklog through commit `13f36d2` before
  working. It stayed within the genuine full-exact iid inverse formal hierarchy;
  no finite matrix, non-iid law, or formal candidate was promoted to a
  full-exact counterexample.
- Forward positivity can be written after scaling `tilde(mu)=D_r mu` as a
  backward Gaussian heat transform with `b=r^2-1`. Vandermonde harmonicity and
  the heat product identity give
  `D_n(Lambda_r)=sum_k (-b)^k C_(n,k)`, with every `C_(n,k)>=0` and universal top
  coefficient `C_(n,N_n)=prod_(j=0)^n j!`. This is a genuine all-order positivity
  constraint, but it is an alternating polynomial at negative heat time.
- The expansion does not compare the different coefficient arrays for
  `D_M,D_(M+1),...,D_(3M)`. Thus it gives no zero interlacing, small-value
  transversality, determinant-ratio bound, or uniform flat-leakage horizon. In
  particular, absolute moment growth does not prevent `D_M` from approaching zero.
- At a corank-one flat crossing, the first Jacobi norm crosses transversely:
  `h'_M=L[(P'_M)^2]>=M^2 h_(M-1)>0`. The next determinant has the exact leakage
  formula `D_(M+1)=-D_(M-1)*ell_M^2`. If `ell_M` is nonzero, the first nearby
  post-failure norm is generically positive, so the nearest mixed tensor sector
  helps rather than cancels the negative `h_M^3` channel. If `ell_M=0`, coherent
  leakage can be delayed; infinite delay would force a finite-atomic flat branch,
  incompatible with the continuous chi-square radial law, but no uniform delay
  bound is known.
- For a fixed countable sequence, real-analytic determinant dependence permits a
  generic radius avoiding all individual determinant zeros, giving quasi-definite
  Jacobi coordinates. This is only fixed-sequence coordinate hygiene and does
  not yield uniform near-flat coercivity.
- Any degree-`3M` residual test with nonzero top part has a nonzero rotationally
  averaged `h_(3M)` channel. Translation invariance also forces six adjacent
  coefficients around a nonzero `(M,M,M)` coefficient, with the sharp lower bound
  `sum_six |c_adj|^2 >= 3M^2/(2(M+1)^2)|c_(M,M,M)|^2`. If `h_M,h_(M+1)<0`, these
  adjacent sectors are positive and can already compete with the central cubic
  term under the stated Jacobi-ratio threshold.
- Exact triangularity leaves the new odd moment `m_(2M+1)` free at the relevant
  stage, and the near-flat denominator in `alpha_M` can blow up. Therefore no
  relative `beta_(M+1)/|beta_M|` bound follows from exactness plus absolute
  growth alone. The most precise missing bridge is cross-rank heat-Hankel
  zero/small-value geometry or a flat-leakage horizon theorem.
- `P_3K` remains disconnected. The residual `cos(3*theta)` harmonic is not the
  nonlinear log-density charge, and no charge-to-leakage, charge-to-Jacobi, or
  charge-to-determinant estimate was obtained. Gaussian rigidity remains OPEN,
  and no genuine full-exact iid non-closed sequence was constructed.
- Added `post_failure_tensor_tail_r22/audit_r22.py` and its README. The audit
  passed the Vandermonde heat identity/top coefficient, flat transversality,
  flat leakage determinant, adjacent coefficient bound, and representative
  degree-`3M` `h_(3M)` channel check, printing `R22_AUDIT_COMPLETED`.
- Minimal OPEN is now `Adjacent Heat-Hankel Transversality / Flat-Leakage
  Control`. Gaussian rigidity remains OPEN.
