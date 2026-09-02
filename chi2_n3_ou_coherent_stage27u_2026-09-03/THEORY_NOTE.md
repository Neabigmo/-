# Stage27U theory note

## 1. OU coherence

Let the master Hermite/Fock transform be

    R(z)=1+sum_{n>=3} a_n z^n/sqrt(n!).

Under OU smoothing with rho=sqrt(q), the nth Hermite coefficient is multiplied by rho^n,
so

    b_n(q)=q^(n/2) a_n.

For the d=3 normalization used in Stages 24–27T, epsilon(q)=q^(3/2) and

    u_n(q)=b_n(q)/epsilon(q)=q^((n-3)/2) a_n.

Therefore

    u_n(q2)=(q2/q1)^((n-3)/2) u_n(q1).

At q1=.05, q2=.10 the squared contribution of order n is amplified by 2^(n-3).
This is the mechanism Stage27U is designed to test: higher odd rescue modes that are cheap
at small q may become prohibitively expensive at q=.10 when the same master sequence is
required.

## 2. Master feature identity

The scaled Hermite recurrence is

    g_0=1,
    g_1=s/sqrt(q),
    g_{n+1}=s/(sqrt(q)*sqrt(n+1)) g_n
             - lambda*sqrt(n/(n+1)) g_{n-1}.

Set h_n=q^(n/2) g_n. Then

    h_0=1,
    h_1=s,
    h_{n+1}=s/sqrt(n+1) h_n
             -(q lambda)*sqrt(n/(n+1)) h_{n-1}.

Hence exactly

    q^(n/2) g_n(q,lambda,s)=g_n(1,q lambda,s).

Thus a coherent positivity expression has the master form

    F_q(lambda,s)=1+sum a_n g_n(1,q lambda,s).

The effective lambda domain is r=q lambda in [0,q), so q1<q2 gives a nested positivity
domain. Stage27U therefore does not create redundant naive simultaneous-q positivity blocks.

## 3. Low-q completion / high-q certification

Outer coordinates are the high-q normalized odd coefficients

    y_n=u_n(qH), qH=.10.

They are downscaled to qL=.05:

    x_n=(qL/qH)^((n-3)/2) y_n,

completed by the triangular Fock recurrence at qL, and then every completed coefficient is
lifted back to qH. A direct qH completion is used only as a regression check at moderate N.

The high-q prefix energy is

    E_N^H=sum_{n=3}^N u_n(qH)^2.

For a fixed robust witness set W at qH, the normalized infinite-tail Gram is independent of
the outer coefficients. It is therefore built once per N. Outer evaluations update only the
prefix vector c(y) and solve the nonnegative NNQP. The resulting tail energy is a finite-witness
lower bound on the continuum required tail energy.

The numerical exclusion margin is

    D_A5(y)=E_N^H(y)+m_tail,W^2(y)-5.

Positive D_A5 for a candidate excludes it already with the finite witness set. Negative D_A5
does not by itself prove a survivor; `COHERENT_SURVIVOR_FOUND` is reserved for a final
candidate whose reduced-cost continuum validation reaches `COHERENT_CONTINUUM_STATIONARY`.

## 4. Outer gradient

For fixed W, the NNQP value satisfies the envelope identity

    d m2 / d c = -2 alpha / epsilon_H^2.

Combined with the exact triangular Fock Jacobian and OU lift, this gives an analytic gradient
of E_N^H+m2 with respect to high-q odd coordinates. The implementation spot-checks this
gradient by finite differences during local search.

## 5. Scope

This is numerical reconnaissance, not a proof. No Stage28, global theorem certificate,
independent-q primal repair, or N*q^alpha scan is launched automatically.
