# R66 — Mehler decomposition and associated-Hermite projection

R66 compresses the quadratic response into two separate generating-function
pieces. The webpage response was independently checked here with exact
symbolic/rational identities. The formulas below use ordinary fraction
notation to remove the browser's stacked-fraction reading ambiguity.

## 1. Scope and normalization

This remains a conditional formal-moment statement. Assume the canonical
finite-head tangent and the full same-factor hierarchy used in R64–R65. Write

    h_n(t)=n!+K_n t+O(t^2), kappa_n=K_n/n!,
    Lambda_n=n(kappa_n-kappa_(n-1)).

Set

    D_n=L_2[H_n^2],
    P_n=sum_(k<n) M_(n,k)^2/k!,
    K_n=D_n-P_n.

Then

    K(z)=sum_(n>=0) kappa_n z^n=D(z)-P(z),

where D(z)=sum D_n z^n/n! and P(z)=sum P_n z^n/n!.

## 2. D-part: exact Mehler/binomial transform

The diagonal Mehler kernel is

    M_z(x,x)=(1-z^2)^(-1/2) exp(z*x^2/(1+z)),

so, as a coefficient identity,

    D(z)=L_2[M_z(x,x)].

Using H_n^2=sum_(j=0)^n j! binom(n,j)^2 H_(2n-2j) and putting
m=n-j gives the exact transform

    D(z)=1/(1-z) * sum_(m>=0) (v_(2m)/m!) (z/(1-z))^m.

If B(w)=sum_(m>=0) b_m w^(2m) is the same-factor pair term

    B(w)=average_theta sum_(i<j) U(r_i(theta)w)U(r_j(theta)w),

then the same-factor identity gives

    A_(2m) v_(2m)/(2m)! + b_m=0,
    A_(2m)=3 binom(2m,m)/6^m.

Consequently

    v_(2m)/m!=-(6^m m!/3)b_m,

and the binomial transform has the single integral form

    D(z)=-1/(3(1-z)) integral_0^infinity exp(-s)
       B(sqrt(6 z s/(1-z))) ds

for the common formal/absolute-convergence domain. With u=(1-z)s/z,
this is

    D(z)=-1/(3z) integral_0^infinity exp(-(1-z)u/z)
       B(sqrt(6u)) du.

The audit checks the finite coefficient identities through n=10 and the
same-factor conversion through m=8.

## 3. Boundary estimate for the D-part

From the exact tangent integral,

    U(w)=w^3 integral_0^1 q(s) exp(-q(s)w^2)(1-q(s)w^2/2) ds,
    q(s)=s(1-s),

one has

    U(w)=w^3/6+O(w^5) as w->0,
    U(w)=-4/w^3+O(w^(-5)) as w->+infinity.

The second expansion follows by endpoint Laplace expansion of
J(lambda)=integral_0^1 exp(-lambda*s(1-s)) ds and
U(w)=w^3(-J'(lambda)-lambda*J''(lambda)/2), lambda=w^2.

Since the three r_j(theta) have simple, pairwise disjoint zeros, a split into
zero neighborhoods of width O(1/w) and their complement gives
B(w)=O(w^(-4)) as w->infinity; the small-w estimate gives B(w)=O(w^6).
Thus B(sqrt(6u)) is integrable on (0,infinity), and the representation
implies the conditional boundary statement

    D(1-)=-(1/3) integral_0^infinity B(sqrt(6u)) du is finite,

with

    D(z)=D(1-)+O((1-z) log(1/(1-z))) as z->1 from below.

This rules out a pole from the same-factor even D piece. The endpoint and
angular bounds are analytic estimates; the exact finite part is what the
local audit certifies.

## 4. Lower-triangular projection: associated-Hermite recurrence

Let

    q_n(x)=-sum_(k<n) M_(n,k) H_k(x)/k!.

The finite-head tangent gives

    q_0=q_1=0, q_2=-H_1, q_3=-H_0,
    q_(n+1)=x q_n-n q_(n-1) for n>=3.

Therefore P_n=||q_n||_(L^2(gamma))^2 exactly. Its exponential generating
function is the closed integral

    Q(x,w)=sum_(n>=0) q_n(x) w^n/n!

    =-exp(xw-w^2/2) integral_0^w
      [x s-(x^2-1)s^2/2] exp(-x s+s^2/2) ds.

Define

    R(xi,eta)=integral_R Q(x,xi)Q(x,eta) d gamma(x).

Then the exact angular diagonal extraction is

    H(y)=sum_(n>=0) ||q_n||^2 y^n/(n!)^2

    =1/(2 pi) integral_0^(2 pi)
      R(sqrt(y) exp(i theta),sqrt(y) exp(-i theta)) d theta.

The factorial Laplace transform is therefore

    P(z)=integral_0^infinity exp(-s) H(zs) ds
    =sum_(n>=0) ||q_n||^2 z^n/n!.

The latter equality is coefficientwise; analytic use of the Laplace integral
requires the corresponding convergence domain. This distinction matters at
z=1.

For reference, the Gaussian expectation in R can be written with
y=xi+eta-s-t and exponent
exp((y^2-xi^2-eta^2+s^2+t^2)/2). The polynomial factor is

    Phi(s,t;y)=s t/4 * [s t(y^4+4y^2+2)
                       -2(s+t)(y^3+2y)+4(y^2+1)].

The audit checks this factor symbolically; it is easy to lose the st/4
normalization when reading the stacked browser fraction.

## 5. What is proved and what remains open

The exact reduction is now clean:

    K(z)=D(z)-P(z),

    D(z) has the above finite Abel boundary estimate, while
    P_n=||q_n||^2>=0.

Hence the only possible dominant singularity of K(z) at z=1 is the
associated-Hermite projection tail P(z), subject to its convergence. If
sum_n ||q_n||^2/n! is finite, K(1-) is finite; if it diverges, then
K(z)=-P(z)+O(1) as z->1 from below.

No eventual sign of Lambda_n and no n^(-1/2) asymptotic is proved here.
The exact R65 signs at n=10,15,20,30,100,200 remain finite evidence only.

The next single target is the asymptotic of
p_n=||q_n||^2/n!, equivalently the leading singularity of P(z). This is
the remaining Gaussian-local projection problem; it still does not supply
backward OU divisibility or close D.1.

Audit command:

    python flat_shadow_mehler_projection_r66/audit_r66.py

The audit uses exact symbolic/rational arithmetic only. It does not use
determinants, optimizers, SDP, parameter sweeps, relaxed measure LP, or
remote computation.
