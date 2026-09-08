# R150 — Robust Sparse-Branch Hankel Collapse / Moving-Degree Resummation

Date: 2026-09-08  
Status: robust fixed-degree reduction proved at the stated abstract level;
the moving-degree rate and the full positive-cone classification remain open.

## 0. Evidence boundary

The webpage first performed the requested global R132–R149 audit against the
public repository and then continued the single R150 target.  At the time of
that audit the public refs both pointed to the R148 commit
`5397c979702731107536227d82f773eddef4ee83`; R149 was then recorded locally
and pushed in commit `7f7c037b55ce178d631a1eb88b97fe66c5c8dfb2`.

The webpage's conservative publication verdict was:

`无（目前没有足够独立、完整、可审稿的发表性结果）`

This directory records the mathematical reduction and finite checks.  It
does not certify the full classical characterization, a genuine
non-Gaussian full-SF law, a quantitative moving-degree lower bound, novelty,
or the bridges `RK=1 => full-SF/all-row` and ordinary/Bargmann `=> P_3 K_sp`.

## 1. Robust higher-odd-tail Hankel exclusion

Fix odd `d=2s+1>=5`.  Let the normalized Bargmann log have first odd
coefficient `c_d=a`, with lower odd coefficients zero.  The full-SF formal
triangular equations determine the even coefficients through any finite order
as polynomials in the finite odd vector

`(a,c_(d+2),c_(d+4),...,c_(2M-1))`.

Let `H_M(a,b)=[m_(i+j)]_(i,j=0)^M` be the corresponding finite Hankel
matrix.  R137 proves for the sparse vector `b=0` that its PSD feasibility
radius `rho_M(d)` decreases to zero as `M` increases.  Therefore, for
`0<epsilon<R_d`,

`M_*(d,epsilon)=min{M>=s+1: rho_M(d)<epsilon}`

is finite.  On the compact annulus
`K_(d,epsilon)={a: epsilon<=|a|<=R_d}`, every sparse matrix `H_(M_*)(a,0)`
has a strictly negative smallest eigenvalue.  Continuity gives

`delta_*(d,epsilon)=-max_(a in K) lambda_min H_(M_*)(a,0)>0`.

Uniform continuity of the finite polynomial matrix map and Weyl's inequality
then give a tail stability modulus `eta_*(d,epsilon)>0` such that

`epsilon<=|a|<=R_d` and
`max_(d<n<2M_*, n odd)|c_n|<=eta_*`

imply

`lambda_min H_(M_*)(a,b)<=-delta_*/2<0`.

This is a genuine robust necessary condition, conditional only on the
already recorded R137 fixed-degree radius collapse and the finite
full-SF triangular map.  It says that a genuine full-SF law with a first odd
packet of size at least `epsilon` must place a non-negligible higher odd
coefficient in a finite degree window.  It does not say that a law with an
infinite higher tail cannot exist.

For `0<a<R_d/2`, define

`M_d(a)=M_*(d,a/2)` and `eta_d(a)=eta_*(d,a/2)`.

Then a genuine law with `|c_d|=a` must satisfy

`max_(d<n<2M_d(a), n odd)|c_n|>eta_d(a)`.

The important point is the order of quantifiers: `M_d(a)` and `eta_d(a)`
may deteriorate as `d` increases and `a` decreases.

## 2. OU diagonal escape rate

For a fixed genuine law `h` with first odd degree `d` and `A=c_d(h)!=0`,
let `g_lambda=P_lambda h`.  Since

`B_(P_lambda h)(z)=B_h(sqrt(lambda) z)`,

the local analytic logarithm satisfies
`c_n(g_lambda)=lambda^(n/2)c_n(h)`.  Choose a zero-free disk `|z|<R` for
`C_h=log B_h` and let `S_R=max_|z|=R |C_h(z)|`.  Cauchy's estimate gives,
for `sqrt(lambda)<R` and `n>=d+2`,

`|c_n(g_lambda)| <= S_R R^(-(d+2)) lambda^((d+2)/2)`.

The robust exclusion applied at
`a_lambda=|A|lambda^(d/2)` therefore forces

`eta_d(a_lambda) <= S_R R^(-(d+2))lambda^((d+2)/2)`.

Equivalently, for a constant depending on `h` and `R`,

`eta_d(a) <= K_(h,R) a^(1+2/d)` as `a` decreases to zero.

Hence the following fixed-degree reduction is rigorous:

`limsup_(a down 0) eta_d(a)/a^(1+2/d)=infinity`

would rule out every genuine non-Gaussian full-SF law whose first odd degree
is that fixed `d`.  This is a small but concrete reduction from an
infinite-dimensional characterization to a finite Hankel stability-rate
problem.

## 3. Why this does not yet close moving degree

As `d` tends to infinity, the critical exponent `1+2/d` tends to one.
A lower bound such as `eta_d(a)>=c a^2` is too weak at high degree; one needs
control close to `a^(1+o_d(1))`, with constants and quantifiers uniform enough
to compare moving top degrees.  R137 supplies only
`rho_M(d)->0` for each fixed `d`, not a rate uniform in `d`.

For a moving-top family `g_N=P_(q^N)h_N`, the same argument can fail through
one of two precisely identified channels: the stability modulus may collapse
fast enough to permit higher-odd replenishment, or the zero-free radius of
`log B_(h_N)` may shrink to the OU scale and destroy uniform Cauchy control.
R132's square-exponential bound does not by itself provide a uniform
zero-free disk for `log B`.

No genuine non-Gaussian full-SF counterexample was constructed, and no
moving-degree rigidity theorem was proved in R150.

## 4. Local audit scope

`audit_r150.py` checks:

1. the inherited first Hankel cap and the R137 sparse determinant for several
   degrees;
2. the polynomial/continuity setup on a finite symbolic truncation;
3. OU Bargmann coefficient scaling and the critical exponent algebra;
4. the Cauchy tail estimate in a finite coefficient model;
5. the explicit logical boundary between fixed-degree reduction and the
   unresolved moving-degree rate.

The resulting status is: R150 supplies a robust fixed-degree stability
reduction and a sharp diagonal-escape upper-rate condition.  The one
remaining R150 target is to quantify `eta_d(a)` uniformly in the joint limit
`d->infinity`, `a->0`, or to construct a rigorously audited diagonal
positive-cone escape; finite/formal jets alone will not suffice.
