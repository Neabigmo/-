# R144 — IID ridge-product / bispectrum balanced-symmetrization audit

Date: 2026-09-08  
Status: finite algebra and probability-level theorem recorded; the global
positive backward-tower rigidity problem remains open.

## Scope and boundary

This package records the completed R144 line.  Its purpose is to isolate what
the iid three-ridge factorization really gives after the R143 coherent-frame
reduction, and to prevent a tempting but invalid sign reversal from being used
as a Gaussian-rigidity proof.

The standing full-SF hypothesis is conditional throughout: whenever a genuine
one-dimensional probability law `mu` is assumed to satisfy the full circular
mean identity, the conclusions below are valid.  The scalar input `RK=1` has
not been upgraded to existence of a genuine full-SF law, and no non-Gaussian
full-SF law is constructed here.

## Residual coordinates and the local three-ridge equation

Use the orthonormal residual coordinates

`U=(X_1-X_2)/sqrt(2)`,

`V=(X_1+X_2-2X_3)/sqrt(6)`,

and

`a=u/sqrt(2)+v/sqrt(6)`,
`b=-u/sqrt(2)+v/sqrt(6)`,
`c=-2v/sqrt(6)`.

Then `a+b+c=0` and `a^2+b^2+c^2=u^2+v^2`.  For
`Phi(u,v)=phi(a)phi(b)phi(c)`, every local zero-free branch
`L=log Phi` satisfies the cubic-harmonic ridge PDE

`(partial_u^3 - 3 partial_u partial_v^2)L = 0`.

This is an exact consequence of the three 120-degree ridge directions.  It is
not, by itself, a positivity or Gaussianity theorem.

## Bispectrum mixed-derivative collapse

Writing `k=log phi` on a zero-free branch and

`ell(a,b)=k(a)+k(b)+k(-a-b)`,

the bispectrum derivatives obey

`ell_ab = k''(-a-b)`,

`ell_aa-ell_ab = k''(a)`,

`ell_bb-ell_ab = k''(b)`.

At the origin, for `p,q>=1`,

`partial_a^p partial_b^q ell(0,0)
 = (-1)^(p+q) i^(p+q) kappa_(p+q)`.

Thus all mixed bispectrum derivatives see one cumulant order, rather than a
new independent family of coefficients.  The weighted cocycle identity is

`beta(a,b) beta(a+b,c) |phi(b+c)|^2`
`= beta(a,b+c) beta(b,c) |phi(a+b)|^2`.

On a nonzero region the phase part is a 2-cocycle.  The identity is useful for
compatibility, but it does not supply the missing global one-dimensional
positive-definiteness estimate.

## Main probability-level result: balanced convolution has the wrong sign

Let `X_j,X'_j` be iid with law `mu`, and define

`Y_m=(sum_(j=1)^m X_j - sum_(j=1)^m X'_j)/sqrt(2m)`.

Its characteristic function is

`psi_m(s)=|phi(s/sqrt(2m))|^(2m)`.

Define the normalized residual bispectrum

`G_t(theta)=exp(t^2/2) prod_(j=1)^3 phi(t r_j(theta))`,

where `r_j(theta)=sqrt(2/3) cos(theta+2pi(j-1)/3)`.  The full-SF identity is
`<G_t>=1`.  Substituting `s=sqrt(2m)t` gives the exact identity

`R_(Y_m)(sqrt(2m)t) = <|G_t|^(2m)> >= 1`,

where the right side is the normalized square-exponential functional.  The
Lp norms satisfy

`||G_t||_2 <= ||G_t||_4 <= ... <= ||G_t||_infinity`.

Therefore balanced convolution/tensorization creates a nonnegative defect; it
cannot close the target by proving a defect `<=0`.

### Exact m=1 defect

If

`G_t(theta)=sum_(k in 3Z) g_k(t) exp(i k theta)`, with `g_0(t)=1`, then

`R_(Y_1)(sqrt(2)t)-1`
`=<|G_t-1|^2>`
`=sum_(ell != 0) |g_(3ell)(t)|^2`.

The first nonzero odd packet of degree `d` produces a strict positive leading
term

`2^(-d) c_d^2 <p_d^2> s^(2d) + O(s^(2d+2))`.

This is a genuine no-go statement for the balanced-symmetrization closure
route, not merely a numerical observation.

## Exact bridge to R143

R143 used

`F_t(theta)=prod_j B_mu(t r_j(theta))`
`=sum_(k in 3Z) f_k(t) exp(i k theta)`, with `f_0=1`.

The characteristic-side normalized object is the same harmonic family on the
imaginary parameter axis:

`G_t(theta)=F_(i t)(theta)`, hence `g_k(t)=f_k(i t)`.

The R143 same-`mod 3` cross-block formula is

`<V_(t,n),V_(t,m)>`
`=(1/(2pi)) int exp(-t^2(1-cos(delta))/4)`
`* f_(m-n)(t cos(delta/2)) exp(i(n+m)delta/2) d delta`.

Thus R144 does not introduce an unrelated statistic: it is the characteristic
axis of the same angular harmonics whose real-axis Gaussian/Bessel transform
is the R143 purity defect.  At the first odd packet both sides carry the same
positive coefficient energy `c_d^2`; there is no hidden reverse sign.

## Bochner barrier and conditional closure

The ordinary three-point Bochner minor gives only a modulus-weighted condition,
schematically

`1-|phi(a)|^2-|phi(b)|^2-|phi(a+b)|^2+2 Re beta(a,b) >= 0`.

It does not control the phase in the direction needed to reverse the balanced
convolution inequality.  Consequently:

`full-SF + balanced convolution + ordinary positivity` gives `R>=1`,
not `R<=1`.

Conditional closure is nevertheless exact: if some balanced `Y_m` is itself
full-SF, then its normalized defect is both at least and at most zero, so
`G_t=1` almost everywhere for each `t`; analyticity then gives `mu=gamma`.
Equivalently, any independently proved reverse estimate
`R_(Y_m)(s)<=1` would finish the Gaussian rigidity.  No such estimate follows
from the current positivity hypotheses.

## Backward-tower interpretation

For `g_N=P_(q^N)h_N`,

`G_(P_lambda mu,t)=G_(mu,sqrt(lambda)t)` and
`Delta_m^(P_lambda mu)(t)=Delta_m^mu(sqrt(lambda)t)`.

Hence

`Delta_m^(g_N)(q^(-N/2)t)=Delta_m^(h_N)(t)`.

The bottom convergence only moves the residual anisotropy to characteristic
scale `q^(-N/2)` and Hermite-energy scale `q^(-N)`.  Compatible single infinite
towers were handled separately by R138; the incompatible moving-top tower and
the final spatial `B_mu/C_g -> P_3 K_sp` bridge remain open.

## Evidence grading after R144

**PROVED under stated analytic/probability hypotheses:** the residual
coordinate identities; the cubic ridge PDE; the bispectrum mixed-derivative
collapse; the weighted cocycle; the iid balanced-convolution defect theorem;
the exact `m=1` angular `L^2` identity; strict first-odd positivity; the R143
harmonic bridge; and OU/tower defect scaling.

**CONDITIONAL:** `RK=1` implies a genuine full-SF/all-row law; Bargmann or
characteristic rigidity implies the spatial `P_3 K_sp` statement; an
independent reverse balanced-convolution bound; and iid ridge-product
liftability forcing all same-`mod 3` coherences to vanish.

**OBSTRUCTION:** local PDE and cocycle data are insufficient; ordinary Bochner
positivity is modulus-weighted; balanced convolution points in the wrong
direction; analytic continuation does not preserve positivity; and generic
`D_3` angular witnesses are not legal iid scalar candidates but show why the
remaining liftability hypothesis matters.

**OPEN:** whether a one-dimensional positive-definite `phi` whose iid
three-ridge lift has Gaussian circular mean must be Gaussian; and whether this
can be forced uniformly along the positive backward tower.  No genuine
non-Gaussian full-SF law has been constructed.

## R145 entry point

The unique next line is to leave the residual plane `s=0` and use the common
mode.  Set

`Psi(s;u,v)=prod_(j=1)^3 phi(s/sqrt(3)+a_j(u,v))`.

Along `v=0`,

`log Psi(s;u,0)`
`= k(s/sqrt(3)+u/sqrt(2))`
`+ k(s/sqrt(3)-u/sqrt(2)) + k(s/sqrt(3))`.

For `m>=3`, the target mixed derivative is

`partial_s^(m-2) partial_u^2 log Psi(0,0,0)`
`= 3^(-(m-2)/2) i^m kappa_m`.

The next task is to determine whether full three-dimensional positive
definiteness, together with the full-SF circular mean, forces these common-
mode/contrast couplings to vanish.  If it does for all `m>=3`, all higher
cumulants vanish.  If it does not, the failure should be recorded as a precise
positive-kernel no-go and not promoted to a theorem.

The next web round must also provide a separate whole-project audit: a
chronological map of the route, a result-by-result `PROVED / CONDITIONAL /
OBSTRUCTION / OPEN` table, and an honest publication assessment.  It must say
`无（目前没有足够独立、完整、可审稿的发表性结果）` if no result clears that
standard; it must not call formal calculations or finite audits publishable
theorems.
