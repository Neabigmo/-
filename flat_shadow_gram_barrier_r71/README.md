# R71 — Hermite–Gram all-order boundary-layer barrier

R71 does not prove a negative boundary-layer profile and does not produce an
all-`n` no-reversal scale. It gives a stronger necessary condition for a
shrinking canonical exit, at the level of the finite Hermite Gram operator.
The statement remains conditional on the full same-factor formal moment
functional and on evaluating its finite-`t` branch; it is not a construction
of a positive exact backward tower.

## 1. Normalized finite Gram block

Let `e_k=H_k/sqrt(k!)`, `V_n=span(e_0,...,e_n)`, and let `L_a` denote the
canonical moment functional with `t=a^2`. Define

    G_n(a)=(L_a[e_j e_k])_(0<=j,k<=n).

At the Gaussian anchor, `G_n(0)=I`. Write the first-order expansion

    G_n(a)=I+a A_n+mathcal R_n(a),
    (A_n)_(j,k)=L_1[e_j e_k].

For the finite-head tangent, the audited transform is

    U(z)=z^3 integral_0^1 q exp(-q z^2)(1-q z^2/2) ds,
    q=s(1-s).

With the Gaussian Hermite transform `T f(z)=int f(x) exp(zx-z^2/2)d gamma(x)`
and `R=x-partial_x`, an explicit representative of `L_1` is

    g_1(x)=integral_0^1 (q R^3-q^2 R^5/2) psi_q(x) ds,
    psi_q(x)=(1-2q)^(-1/2) exp(-q x^2/(1-2q)),

because `T psi_q=exp(-q z^2)` and `T(Rf)=z T(f)`. The endpoint estimate
`q=s(1-s)` implies `g_1 in L^infinity(gamma)`; the two worst endpoint terms
are `s(1+|x|^3) exp(-s x^2/2)` and
`s^2(1+|x|^5) exp(-s x^2/2)`, both integrable with an `O(|x|^-1)` bound.
Thus

    A_n=P_n M_(g_1) P_n,
    sup_n ||A_n||_op <= M_*:=||g_1||_infinity < infinity.

This is a uniform bound on the whole first-order Gram perturbation, not merely
on the scalar slope `Lambda_n`.

## 2. Gram barrier for a shrinking exit

Put `gamma_n(a)=h_n(a)/n!`. The Schur-complement identity for the normalized
Hermite basis is

    gamma_n(a)=L_a[(e_n+u_n)^2] at the lower-triangular orthogonal choice,

equivalently it is the scalar Schur complement of the `V_(n-1)` block in
`G_n(a)`. Consequently

    beta_n(t)/n=gamma_n(a)/gamma_(n-1)(a),  t=a^2.

If all preceding norm ratios are positive and `beta_n(tau_n)=0`, then the
lower block is invertible and the Schur-complement kernel vector shows that
`G_n(sqrt(tau_n))` is singular. Hence

    ||G_n(sqrt(tau_n))-I||_op >= 1.

Since `sqrt(tau_n) A_n -> 0` uniformly whenever `tau_n -> 0`, every shrinking
exit must satisfy the operator-level necessary condition

    ||mathcal R_n(sqrt(tau_n))||_op >= 1-o(1).

So a shrinking exit cannot be accumulated from the Gaussian first tangent;
the second-and-higher same-factor/Jacobi response must create an order-one
Gram deformation.

If `||G_n(a)-I||_op<=epsilon<1`, every leading Gram block is positive
definite and its normalized Schur complements lie in `[1-epsilon,1+epsilon]`.
Therefore all corresponding `beta_k(t)` are positive. This is an exact
finite-stage no-reversal certificate.

## 3. Exact all-order coefficient majorant

Let

    eta_m(a)=L_a[e_m],
    r_m(a)=eta_m(a)-delta_(m,0)-a L_1[e_m].

Hermite product expansion gives the exact finite identity

    mathcal R_n(a)=sum_(m=0)^(2n) r_m(a) T_(m,n),
    (T_(m,n))_(j,k)=<e_j e_k,e_m>_gamma.

Hölder with exponents `(4,2,4)` and Gaussian hypercontractivity gives

    ||T_(m,n)||_op <= 3^((n+m)/2),

and hence the explicit majorant

    ||mathcal R_n(a)||_op <=
    mathcal M_n(a):=3^(n/2) sum_(m=0)^(2n) 3^(m/2)|r_m(a)|.

This is an exact conditional reduction of the boundary problem to the
nonlinear Hermite coefficient tail. It becomes a genuine no-reversal theorem
on any explicit `a_n -> 0` scale for which

    sup_|a|<=a_n mathcal M_n(a) -> 0,

or even stays below `1-delta`; the linear part contributes only `M_* a_n`.
In the original `t` variable the tested interval is `0<=t<=a_n^2`.
R71 does not supply such a uniform source bound.

## 4. Exact angular solver scale (locator, not existence)

For `r_j(theta)=sqrt(2/3) cos(theta+2 pi j/3)` and an even series `W`, the
angular operator `A W=average sum_j W(r_j z)` satisfies

    A(z^(2k))=A_(2k) z^(2k),
    A_(2k)=3 binom(2k,k)/6^k,
    A_(2k+2)/A_(2k)=(2k+1)/(3(k+1))<1.

Thus the coefficient-`ell^1` inverse on degrees at most `2n` has norm
`A_(2n)^(-1)`, with

    A_(2n)^(-1) ~ sqrt(pi n)/3 (3/2)^n.

This identifies an exponential possible amplifier in the same-factor linear
solver, but it does not imply `tau_n` has that scale and does not imply a
cutoff. The odd solver and repeated nonlinear source remain uncontrolled.

## 5. Status and next target

R71 therefore strengthens R70 from scalar Taylor-tail necessity to an
operator-level Hermite–Gram barrier. It still does not prove D.1, positive
backward-tower existence, or backward OU divisibility. The unique next target
is a source-recursion bound for `mathcal M_n(a)` on an explicit scale, or a
nontrivial operator profile at the possible angular-solver scale.

The local audit is `audit_r71.py`; it checks the normalization, transform
identities, block-kernel implication, coefficient majorant exponents, and
angular eigenvalue algebra without determinant computation, optimization,
SDP, numerical sweep, or remote computation.
