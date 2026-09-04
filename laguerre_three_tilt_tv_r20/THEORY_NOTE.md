# R20 — three-tilt variance audit

## Question

The proposed gate is

\[
 K''(u_1)+K''(u_2)+K''(u_3)\ge 3,
 \qquad u_1+u_2+u_3=0.
\tag{TV}
\]

Writing \(H(s)=K(s)-s^2/2\), this is the subharmonicity condition
\(\Delta_\Pi[H(u_1)+H(u_2)+H(u_3)]\ge0\).

The available Fock relation is only the circular zeroth-mode identity

\[
 \frac1{2\pi}\int_0^{2\pi}e^{\Phi(\rho\alpha(\theta))}\,d\theta=1,
 \qquad \Phi=\sum_i H(u_i).
\tag{F}
\]

## Exact local calculation

Use the unit-circle parameterization of \(\Pi\) with
\(\sum_i\alpha_i=0\) and \(\sum_i\alpha_i^2=1\). Exact Laurent averaging gives

\[
\langle p_3\rangle=0,\quad \langle p_4\rangle=\frac12,
\quad \langle p_5\rangle=0,
\quad \langle p_6\rangle=\frac5{18},
\quad \langle p_3^2\rangle=\frac1{12}.
\]

For a local jet \(H=h_3s^3+h_4s^4+h_5s^5+h_6s^6+\cdots\), the coefficients of (F)
through order six force

\[
h_4=0,\qquad h_6=-\frac3{20}h_3^2,
\]
while the odd coefficient \(h_5\) is not constrained at this order.  Setting
\(h_5=0\) gives a compatible formal jet whose Laplacian has

\[
\Delta_\Pi\Phi(\rho\alpha)
=30h_6\rho^4p_4(\alpha)+O(\rho^5),
\]

and therefore a negative quartic leading term when \(h_3\ne0\).  This is an
exact local obstruction to deriving (TV) from the currently used finite jet of
(F).  It is not a probability-law counterexample: higher-order Fock constraints
or positivity of a genuine mgf could still rule out the formal jet.

## Independent probability sanity check

For the standardized Rademacher law, \(K(s)=\log\cosh s\) and
\(K''(s)=\operatorname{sech}^2s\).  At \((a,-a,0)\),

\[
K''(a)+K''(-a)+K''(0)-3=2\operatorname{sech}^2a-2<0
\quad(a\ne0).
\]

Thus (TV) is not a generic consequence of variance positivity or exponential
tilting.  The missing proof must use an additional, genuinely cross-parameter
Fock identity, if one exists.

## Decision

R20 does not prove or refute (TV) for the complete chi-square law.  It does
show that the currently stated circle-average identity is insufficient as a
standalone route, and that the task must not be reported as a theorem.
