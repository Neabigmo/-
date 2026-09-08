# R151 — Critical Hermite-Gram Shape / Canonical Rescue Modulus

Date: 2026-09-08  
Status: exact coefficient identities and a canonical finite-dimensional modulus
are established; the semiclassical positive-cone limit remains open.

## 0. Global audit and publication boundary

The webpage first audited the route through R150 and then corrected an
ambiguity in the earlier continuity radius.  The conservative publication
verdict remains:

`无（目前没有足够独立、完整、可审稿的发表性结果）`

The project has a coherent sequence of probability-level and operator-level
lemma packages, but it does not yet contain a closed characterization or a
novelty-checked theorem suitable for an independent paper.  The unresolved
bridges are still `RK=1 => full-SF/all-row`, the genuine positive backward
tower, the moving-degree limit, and the spatial `P_3 K` bridge.

This directory records only claims that can be independently checked from the
Hermite generating function.  It does not promote a formal jet, a finite
truncation, or a conditional asymptotic into a genuine probability theorem.

## 1. Canonical finite-dimensional quantities

Let `Gamma_M(a,b)` be the Hermite-basis moment Gram matrix associated with a
finite odd coefficient vector, with `H_M` its monomial-Hankel congruent form.
Then

`Gamma_M >= 0  <=>  H_M >= 0`.

For the sparse slice with only `c_d=a`, define

`M_d^sharp(a)=min{M: Gamma_M(a,0) is not PSD}`,

and

`delta_d^sharp(a)=-lambda_min Gamma_(M_d^sharp(a))(a,0)>0`.

The canonical finite rescue modulus is

`eta_d^sharp(a)=inf{||b||_infty: Gamma_(M_d^sharp(a))(a,b) >= 0}`,

with value infinity if the set is empty.  This removes the non-intrinsic
choice of an arbitrary sufficiently small continuity radius in R150.

For

`L_(d,M)(a,r)=sup_(||b||_infty<=r) sum_j ||partial_(b_j)Gamma_M(a,b)||_op`,

the mean-value estimate and Weyl's inequality give the computable lower bound

`eta_d^sharp(a) >= sup{r>0: r L_(d,M_d^sharp(a))(a,r)<delta_d^sharp(a)}`.

This is a finite-dimensional exact implication.  It is not a power law because
R137 supplies no rate for `M_d^sharp(a)` or `delta_d^sharp(a)`.

## 2. Exact Hermite-Gram generating identity

If `C(z)=log B_mu(z)=sum_(k>=3)c_k z^k` and
`Gamma_mn=E_mu[He_m(X)He_n(X)]/sqrt(m! n!)`, then

`sum_(m,n>=0) Gamma_mn u^m/sqrt(m!) v^n/sqrt(n!)`
`= exp(uv+C(u+v))`.  (2.1)

Consequently, at the Gaussian point,

`partial_(c_k)Gamma_mn|_0`
`=sqrt(m! n!)[u^m v^n] exp(uv)(u+v)^k`.

Put `r=(m+n-k)/2`.  The derivative is zero unless `r` is an integer and
`0<=r<=min(m,n)`; otherwise

`partial_(c_k)Gamma_mn|_0`
`=sqrt(m! n!) binom(k,m-r)/r!`.  (2.2)

For the adjacent entry `m=M`, `n=M+1`, and `k=2ell+1`, this becomes

`L_(k,M)=binom(k,ell) sqrt(M+1) (M)_(under ell)`.  (2.3)

For `d=2s+1`, the next odd coefficient has the exact sensitivity ratio

`L_(d+2,M)/L_(d,M)=4(d+2)/(d+3) * (M-s)`.  (2.4)

Thus cancelling this one adjacent entry at linear order would require

`c_(d+2)=-a(d+3)/(4(d+2)(M-s))`,

which is only a linearized block cancellation and is not a positive full-SF
construction.

More generally, for `j>=0`,

`L_(d+2j,M)/L_(d,M)`
`=[binom(d+2j,s+j)/binom(d,s)] (M-s)_(under j)`.  (2.5)

These formulas are the main independently auditable R151 milestone.

## 3. Critical scale and OU-invariant shape

At `M~tau |a|^(-2/d)`, the first packet satisfies
`a L_(d,M)=O(1)`.  A tail coefficient of scale

`c_(d+2j)=u_j |a|^(1+2j/d)`

also has `c_(d+2j)L_(d+2j,M)=O(1)`.  Hence every fixed higher odd mode survives
at the same semiclassical Hankel scale.  The first-order exponent
`1+2/d` is therefore intrinsic to the adjacent Hermite band, but it cannot by
itself give rigidity: the all-order shape vector

`u_j=c_(d+2j)/|c_d|^(1+2j/d)`

must be controlled.

Under OU scaling, `c_n(P_lambda mu)=lambda^(n/2)c_n(mu)`, so
`c_d(P_lambda mu)=lambda^(d/2)c_d(mu)` and every `u_j` is exactly invariant.
This identifies the true moving-top object: an OU-invariant critical shape,
not the raw coefficient norm.

## 4. Evidence grading and next theorem

`PROVED`: the canonical finite definitions, (2.1)–(2.5), the critical powers,
and exact OU invariance of the shape coordinates.

`CONDITIONAL`: any rigidity conclusion obtained from a nonzero scaled negative
Hankel gap or from a lower bound on `eta_d^sharp`.

`FORMAL/FINITE-ONLY`: the single-block linear cancellation and any finite-support
critical vector calculation.

`OPEN`: `M_d^sharp(a)~tau_d^*|a|^(-2/d)`, a nonzero scaled negative gap, the
all-order critical shape cone, uniformity as `d->infinity`, genuine positive
backward-tower closure, and the spatial `P_3 K` bridge.

The next unique target is **R152 — Semiclassical Sparse Hankel Limit / Critical
Shape Cone**: first derive a normalized limit for `Gamma_M` with
`c_d=A lambda^(d/2)`, `c_(d+2j)=U_j lambda^((d+2j)/2)`, and
`M=floor(tau/lambda)`; then determine whether the limiting all-order positive
cone is empty, nonempty, or only conditionally defined.  A nonempty cone is not
automatically a counterexample: it must still lift to a genuine positive iid
law and satisfy the original exact-zero and charge conditions.

The local audit script checks coefficient extraction, adjacent and higher-j
ratios, critical exponents, and OU shape invariance.  It does not claim the
R152 limit, full characterization, novelty, or publication readiness.
