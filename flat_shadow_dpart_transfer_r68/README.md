# R68 — D-part coefficient transfer

R68 isolates the remaining same-factor even term in the conditional
R64–R67 formal-moment framework. The full same-factor hierarchy is still an
assumption here; this record does not construct a non-Gaussian exact tower or
identify a Favard spectral measure with the original OU law.

## 1. Normalization and exact rational kernel

Write

    D(z)=sum_(n>=0) d_n z^n,       d_n=D_n/n!,

and retain the R66 normalization

    D(z)=-1/(3z) integral_0^infinity exp(-(1-z)u/z)
       B(sqrt(6u)) du,

    B(w)=average_theta sum_(i<j) U(r_i(theta)w)U(r_j(theta)w).

For q_s=s(1-s), q_t=t(1-t), put

    alpha=q_s r_i^2, beta=q_t r_j^2, c=alpha+beta,
    lambda=1-6c.

Since 0<=q_s,q_t<=1/4 and r_i^2+r_j^2<=1, one has
`0<=c<=1/4` and `-1/2<=lambda<=1`. Substitution of

    U(r_i w)=r_i^3 w^3 integral_0^1 q_s exp(-alpha w^2)
             (1-alpha w^2/2) ds

and exact integration of the resulting u^3,u^4,u^5 terms gives

    D(z)=average_theta sum_(i<j) integral_[0,1]^2 q_s q_t r_i^3 r_j^3
      [ -432 z^3/(1-lambda z)^4
        +5184 c z^4/(1-lambda z)^5
        -77760 alpha beta z^5/(1-lambda z)^6 ] ds dt.

The parameter integral is analytic on

    Omega=C minus ([1,infinity) union (-infinity,-2]),

because the possible zeros of `1-lambda z` lie on the removed rays. Expanding
the rational kernel also gives the exact coefficient identity, with
`binom(n,k)=0` for `n<k`:

    d_n=average_theta sum_(i<j) integral_[0,1]^2 q_s q_t r_i^3 r_j^3
      [ -432 binom(n,3) lambda^(n-3)
        +5184 c binom(n,4) lambda^(n-4)
        -77760 alpha beta binom(n,5) lambda^(n-5) ] ds dt.

The audit checks these constants and the coefficient extraction exactly.

## 2. Boundary cancellation and the transfer statement

With `J(xi)=integral_0^1 exp(-xi s(1-s)) ds`,

    U(w)=w^3[-J'(w^2)-w^2 J''(w^2)/2].

Watson expansion in fixed right-half-plane sectors gives

    U(w)=-4 w^(-3)+O(|w|^(-5)),
    U'(w)=12 w^(-4)+O(|w|^(-6)),

and `U(w)=w^3/6+O(w^5)` at zero. The relation `r_0+r_1+r_2=0`
cancels the leading pair contribution in each simple-zero neighborhood. A
zero-neighborhood/complement decomposition then yields

    B(w)=O_epsilon(|w|^(-5))

uniformly when `|arg(w^2)|<=pi/2-epsilon`; near zero `B(w)=O(w^6)`. Hence
`f(u)=B(sqrt(6u))` has two finite moments on the positive ray:

    F_0=integral_0^infinity f(u)du,
    F_1=integral_0^infinity u f(u)du.

The intended slit-domain continuation of the Laplace representation gives,
for a closed Delta-sector at `z=1`,

    D(z)=D_*+D_1(1-z)+O(|1-z|^(3/2)),
    D_*=-F_0/3,  D_1=-(F_0-F_1)/3.

The corresponding Cauchy–Hankel transfer is

    d_n=O(n^(-5/2)),
    n(d_n-d_(n-1))=O(n^(-3/2)).

This is a coefficient-level claim, stronger than the R66 radial Abel bound.
The local audit certifies the algebraic kernel, its domain geometry, the
moment-to-remainder bookkeeping, and the transfer exponent. The contour
rotation used to promote the positive-ray Laplace estimate to a full
Delta-domain estimate must retain the stated sectorial bounds; if those
complex-sector hypotheses are not available for the concrete formal model,
the `O(n^(-5/2))` conclusion is conditional on them rather than a consequence
of `D(1-)` being finite.

## 3. Consequence for the projection singularity

R67 gives

    p_n=||q_n||^2/n! ~ (33 sqrt(pi)/128)n^(-1/2).

Under the R68 transfer hypotheses,

    kappa_n=d_n-p_n
      ~ -(33 sqrt(pi)/128)n^(-1/2),

and the generating-function singularity is now coefficientwise consistent,
not merely radial Abel information. However

    Lambda_n=n(kappa_n-kappa_(n-1))
      =n(p_(n-1)-p_n)+O(n^(-3/2)).

The asymptotic `p_n~C n^(-1/2)` alone does not control this first difference;
eventual sign and the constant `33 sqrt(pi)/256` remain OPEN.

Thus R68 removes the D-part as the leading asymptotic obstruction and leaves
one precise target: prove the first-difference asymptotic for the positive
R67 finite sum. Even after that, the result only rules out a shrinking cutoff
driven by a large-n Gaussian-local quadratic slope; it does not prove D.1.

Audit command:

    python flat_shadow_dpart_transfer_r68/audit_r68.py

