# Stage27U retry2 theory / numerical note

The exact OU-coherence relations are unchanged from Stage27U:

\[
b_n(q)=q^{n/2}a_n,
\qquad
u_n(q)=q^{(n-3)/2}a_n,
\]

so between `q_low=0.05` and `q_high=0.10`,

\[
u_n(0.10)=2^{(n-3)/2}u_n(0.05).
\]

The scaled Hermite feature obeys

\[
q^{n/2} g_n(q,\lambda,s)=g_n(1,q\lambda,s),
\]

hence the positivity domains are nested in the master variable `r=q*lambda`. Stage27U therefore uses low q only as a stable Fock-completion device and evaluates the obstruction at high q.

## Tail-envelope gradient

For fixed high-q witnesses, the normalized inner problem is

\[
\min_{\alpha\ge0}\; \alpha^T C\alpha+2c(u)^T\alpha,
\]

and the tail lower bound is

\[
m^2(u)=-\frac{1}{\epsilon^2}\min Q.
\]

Since

\[
\frac{\partial c_j}{\partial u_n}
=\epsilon\,\frac{g_{jn}}{d_j},
\]

the envelope derivative at a stable active set is

\[
\frac{\partial m^2}{\partial u_n}
=-\frac{2}{\epsilon}\sum_j\alpha_j\frac{g_{jn}}{d_j}.
\]

Retry1's formula used this coefficient correctly. The retry1 audit failure came from comparing it to finite differences after projecting perturbed points back to the ball, and from possible active-set switches. Retry2 audits the formula only at interior, branch-stable, active-set-stable points.

## Overflow regions

The triangular recurrence is carried internally in scaled coefficients `r_n`. Converting back to ordinary float `b_n` may overflow even when the scaled recurrence remains finite. Such regions are irrelevant to minimization once the high-q prefix energy is already far above `A=5`. Retry2 uses a scaled-r energy probe only as an **algorithmic exclusion test**. These barrier evaluations never contribute a scientific lower bound and never enter the finalist set.

## Scientific decision rule

The campaign still reports only one of:

- `COHERENT_HIGHQ_OBSTRUCTION_STRONG_NUMERIC_EVIDENCE`
- `COHERENT_SURVIVOR_FOUND`
- `COHERENT_OUTER_MINIMAX_UNRESOLVED`

and the independent retry2 numerical audit does not upgrade any of these to a theorem.
