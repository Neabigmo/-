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
