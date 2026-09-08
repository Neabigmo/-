# R145 — Shifted Bispectrum / Common–Residual Regression Audit

Date: 2026-09-08  
Status: probability-level inequalities and conditional closure recorded; the
positive backward-tower rigidity problem remains open.

## Scope and evidence boundary

This round leaves the residual plane `s=0` and uses the common/sample-mean
coordinate. The web-side derivation was required to read public commit
`4e31ab30930609b7ee18e552897d0116312a8e55` before working. This file records
the resulting mathematics and its limitations. The companion Python script
checks only finite algebra, Taylor identities, and an explicit relaxed
probability witness. It does not certify existence of a non-Gaussian genuine
full-SF law, the scalar `RK=1` to all-row bridge, or the spatial `P_3 K_sp`
bridge.

Throughout, `X_1,X_2,X_3` are iid, centered, variance-one variables whenever a
genuine iid statement is made. The full-SF/all-row hypothesis is kept
conditional: it is used only through the exact residual law

`R^2=U^2+V^2 ~ chi^2_2`.

## 1. Common/residual coordinates and mixed cumulants

Set

`C=(X_1+X_2+X_3)/sqrt(3)`,
`U=(X_1-X_2)/sqrt(2)`,
`V=(X_1+X_2-2X_3)/sqrt(6)`.

The inverse orthogonal map is

`X_1=C/sqrt(3)+U/sqrt(2)+V/sqrt(6)`,

`X_2=C/sqrt(3)-U/sqrt(2)+V/sqrt(6)`,

`X_3=C/sqrt(3)-2V/sqrt(6)`.

Thus, in Fourier variables `(s,u,v)`,

`a_1=u/sqrt(2)+v/sqrt(6)`,
`a_2=-u/sqrt(2)+v/sqrt(6)`,
`a_3=-2v/sqrt(6)`,

and the genuine three-dimensional characteristic function is

`Psi(s;u,v)=prod_j phi(s/sqrt(3)+a_j(u,v))`.

On a local zero-free branch, with `k=log phi`, the line `v=0` gives

`log Psi(s;u,0)`
`= k(s/sqrt(3)+u/sqrt(2))`
`+ k(s/sqrt(3)-u/sqrt(2)) + k(s/sqrt(3))`.

Consequently,

`partial_u^2 log Psi(s;0,0)=k''(s/sqrt(3))`,

and, for every `m>=3` for which the cumulant derivative exists,

`partial_s^(m-2) partial_u^2 log Psi(0;0,0)`
`= 3^(-(m-2)/2) i^m kappa_m`.

Equivalently,

`cum(C,...,C,U,U)=3^(-(m-2)/2) kappa_m`,

with `m-2` copies of `C`. This is an exact common-mode/residual coupling
identity, not a rigidity result.

## 2. Finite 3D positivity: exact upper bound and its limitation

For any finite set of three-dimensional nodes, the iid characteristic Gram
matrix factorizes as

`G = G^(1) circ G^(2) circ G^(3)`,

where each factor is a one-dimensional Bochner Gram matrix. Hence finite 3D
positivity is a Schur-product consequence of one-dimensional positivity. It
does not by itself force a mixed cumulant to vanish or have a sign.

Let `W=(U,V)`, `Z=exp(i s C)`, and `Y=exp(i w dot W)`. The four-node Gram
matrix for `1,Z,Y,ZY` has the centered covariance Schur complement

`[[1-|A|^2, Psi(s;-w)-A conj(B)],`
 ` [conj(Psi(s;-w)-A conj(B)), 1-|B|^2]] >= 0`,

where `A=phi(s/sqrt(3))^3` and `B=Psi(0;w)`. Therefore

`|Psi(s;-w)-A conj(B)|^2`
`<= (1-|A|^2)(1-|B|^2)`.

This is a genuine mixed-dependence upper bound. Its direction is important:
it is not a reverse estimate and does not imply `C` is independent of the
residual contrast.

## 3. Shifted Bessel–Schur inequality

Assume the genuine full-SF/all-row consequence `R^2~chi^2_2`. Define

`A(s,t)=E[ exp(i s C) J_0(t R) ]`.

The radial law gives

`E J_0(tR)=exp(-t^2/2)`,

`Var(J_0(tR))=exp(-t^2)(I_0(t^2)-1)`.

Cauchy–Schwarz for the centered variables `exp(i s C)` and `J_0(tR)` yields

`|A(s,t)-phi(s/sqrt(3))^3 exp(-t^2/2)|^2`
`<= (1-|phi(s/sqrt(3))|^6) exp(-t^2)(I_0(t^2)-1)`.

This is an analytically proved, probability-level two-parameter inequality
under the stated full-SF hypothesis. Expanding at `t=0` gives the
division-free form

`|E[exp(i s C)(R^2-2)]|^2 <= 4(1-|phi(s/sqrt(3))|^6)`.

Writing `x=s/sqrt(3)` and using iid differentiation,

`E[exp(i s C)(R^2-2)]`
`= -2 phi(x)[phi(x)^2+phi(x)phi''(x)-phi'(x)^2]`.

Hence, for every real `x`, including zeros of `phi`,

`|phi(x)|^2 |phi(x)^2+phi(x)phi''(x)-phi'(x)^2|^2`
`<= 1-|phi(x)|^6`.

On a local zero-free branch this can be written as

`|phi(x)|^6 |1+k''(x)|^2 <= 1-|phi(x)|^6`.

The result is a curvature-defect upper bound. It does not force `k''=-1`.

## 4. Conditional variance and Appell regression coordinates

Permutation symmetry conditional on `C` gives

`E[U|C]=E[V|C]=E[UV|C]=0`,

`E[U^2|C]=E[V^2|C]=1/2 E[R^2|C]`.

Define the regression defect

`H(C)=E[R^2-2|C]`.

For the ordinary MGF `M(t)=E exp(tX)` and `K=log M`, common exponential
tilting gives

`E_t[R^2]=2 K''(t/sqrt(3))`.

Let the normalized cumulant-Appell polynomials of `C` be defined by

`exp(tC)/E exp(tC)=sum_n P_n^C(C)t^n/n!`.

Then comparison of coefficients gives, for `n>=1`,

`E[(R^2-2)P_n^C(C)] = 2 3^(-n/2) kappa_(n+2)`,

or equivalently

`E[H(C)P_n^C(C)] = 2 3^(-n/2) kappa_(n+2)`.

Thus the full higher-cumulant sequence is exactly the Appell-coordinate
sequence of the conditional sample-variance regression defect. In particular,
under the full-SF radial law,

`0 <= E[H(C)^2] <= 4`,

and Cauchy–Schwarz yields

`E[H(C)^2] >= 4 3^(-n) kappa_(n+2)^2 / E[(P_n^C(C))^2]`.

For a first odd degree `d` whose lower moments agree with Gaussian moments,
the available first-packet information gives the specialized lower bound

`E[H(C)^2] >= 4 kappa_d^2 /(3^(d-2)(d-2)!)`.

This is another positive defect, not a contradiction.

There is, however, a sharp conditional closure theorem: if

`E[R^2|C]=2` almost surely,

then `K''(t/sqrt(3))=1` near zero, hence `K(t)=t^2/2` near zero and the law
is standard Gaussian (under, for example, a neighborhood MGF hypothesis; the
stronger square-exponential hypothesis is sufficient). Full-SF has not been
shown to imply this constant regression condition.

## 5. Shifted bispectrum derivatives and no reverse sign

Set `x=s/sqrt(3)` and

`beta_s(a,b)=phi(x+a)phi(x+b)phi(x-a-b)`.

Locally,

`partial_a partial_b log beta_s(a,b)=k''(x-a-b)`,

so

`partial_s^n partial_a partial_b log beta_s(0,0)`
`=3^(-n/2)i^(n+2) kappa_(n+2)`.

The real-MGF Hessian is only the tilted variance `K''`; its positivity is
automatic for a non-degenerate exponential tilt. Therefore the shifted
bispectrum Hessian cone does not annihilate higher derivatives.

The entropy identity `I(C;R^2)>=0` has the same direction as the R143 purity
excess and the R144 balanced-convolution defect. It measures dependence but
does not provide the needed reverse inequality.

## 6. Strict obstruction outside the iid scalar cone

To show why complete 3D positivity is insufficient without iid factorization,
let `(U,V)` be standard two-dimensional Gaussian, `S=U^2+V^2`, let `Z` be an
independent standard Gaussian, and set

`h(S)=exp(-S)-1/3`,
`sigma_epsilon^2=1+4 epsilon^2/45`,
`C_epsilon=(Z+epsilon h(S))/sigma_epsilon`.

Then `(C_epsilon,U,V)` is a centered, variance-normalized,
square-exponential genuine joint law with exact Gaussian residual vector and

`cum(C_epsilon,U,U)=-2 epsilon/(9 sigma_epsilon)`.

It is exchangeable after the inverse orthogonal transform, but not iid. It
proves the probability-level no-go

`3D Bochner + exchangeability + exact Gaussian residual vector`
`does not imply common/residual independence.`

It is not a counterexample to the scalar iid full-SF problem. Constructing one
would directly challenge the classical fixed-sample-size chi-square
characterization layer, which remains open in the relevant generality.

## 7. Relation to R143/R144 and the backward tower

R143 measures real-axis same-`mod 3` coherent cross-coherence by a nonnegative
frame-purity excess. R144 measures the same harmonic family on the
characteristic axis by the nonnegative balanced-symmetrization defect. R145
adds the nonnegative common-mode regression defect `E[H(C)^2]`. At a first
odd packet all three defects start at the square of the same non-Gaussian
coefficient. No reverse inequality has been obtained.

For `g_N=P_(q^N)h_N`, ordinary cumulants scale as

`kappa_m(g_N)=q^(Nm/2) kappa_m(h_N)`,

so fixed physical mixed derivatives are damped. The shifted defect has the
Gaussian-renormalized scaling

`D_hat_(P_lambda mu)(s,t)=D_hat_mu(sqrt(lambda)s,sqrt(lambda)t)`,

and hence

`D_hat_(g_N)(q^(-N/2)s,q^(-N/2)t)=D_hat_(h_N)(s,t)`.

Common/residual dependence is therefore transported to the same
`q^(-N/2)` characteristic scale found in R141–R144, not eliminated. The
compatible single infinite tower remains covered by R138; the incompatible
moving-top tower remains open. The bridge from ordinary/Bargmann rigidity to
the spatial `P_3 K_sp` statement also remains open/conditional.

## Evidence grading and publication decision

**PROVED under stated assumptions:** the orthogonal coordinate formulas; the
mixed-cumulant identity; the finite Gram Hadamard factorization and Schur
upper bound; the shifted Bessel–Schur inequality; the division-free curvature
inequality; the Appell regression identity; and the constant-regression
Gaussian closure theorem.

**CONDITIONAL:** `RK=1` to genuine full-SF/all-row; full-SF to constant
conditional sample-variance regression; ordinary/Bargmann rigidity to the
spatial `P_3 K_sp` conclusion; and any reverse inequality capable of closing
R143/R144.

**OBSTRUCTION:** finite 3D Bochner positivity is a Schur-product tautology for
an iid characteristic function; Hessian/entropy positivity has the wrong
direction; and the explicit exchangeable witness is not a legal iid scalar
candidate.

**OPEN:** whether the genuine iid fixed-sample-size chi-square/full-SF
condition forces constant regression or Gaussianity, whether this can be made
uniform along an incompatible positive backward tower, and whether the
ordinary-to-spatial bridge can be closed.

Strict publication assessment for the current package:

`无（目前没有足够独立、完整、可审稿的发表性结果）`。

The most useful small milestone is the **Shifted Common–Residual
Schur/Regression Lemma package**: it is a rigorous probability-level family of
upper/lower defect identities and a sharp conditional closure interface, but
it is currently a lemma package inside the main open problem rather than an
independent publishable theorem. No genuine non-Gaussian full-SF law has been
constructed.

## Next task

The unique next round is **R146 — Tilted Sample-Variance Laplace /
Constant-Regression Rigidity**. Study

`Lambda(a,z)=E[exp(aC-zR^2)]/E exp(aC)`, `z>=0`,

with boundary data `Lambda(0,z)=(1+2z)^(-1)`. Test whether iid product
factorization, Gaussian heat-kernel structure, total positivity, or
log-convexity can force `-partial_z Lambda(a,0)=2`; if not, record a legal
exponential-family no-go. Do not return to rank/tensor routes already shown to
have the wrong sign.
