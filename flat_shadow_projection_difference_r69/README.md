# R69 — Projection first-difference asymptotic

R69 closes the last Gaussian-local coefficient gap left by R67, subject to the
conditional R64–R68 full same-factor hierarchy and the sectorial D-part
transfer recorded in R68. No positive exact tower, backward OU divisibility,
Favard identification, or new degree expansion is used.

## 1. Exact adjacent-summand comparison

Put `m=n-3` and write the R67 positive sum as

    p_(m+3)=sum_(j=0)^[m/2] T_(m,j),

    T_(m,j)=((j+1)^2 (j+2)^2 (j^2+5j-2m)^2)/(4(m+3)!)
             * ((m-j-1)!^2)/(m-2j)!.

For the common range `0<=j<=floor((m-1)/2)`, set

    A_(m,j)=j^2+5j-2m,
    L_(m,j)=((m+3)(m-2j))/((m-j-1)^2).

Exact cancellation of neighboring factorials gives

    T_(m-1,j)=((j+1)^2 (j+2)^2)/(4(m+3)!)
              * ((m-j-1)!^2)/(m-2j)!
              * L_(m,j)(A_(m,j)+2)^2.

Define

    rho_(m,j)=m^5 (m-j-1)!^2/((m-2j)!(m+3)!),
    G_(m,j)=m^2(T_(m-1,j)-T_(m,j)),
    B_(m,j)=[L_(m,j)(A_(m,j)+2)^2-A_(m,j)^2]/m.

Then

    G_(m,j)=(1/4)*((j+1)^2(j+2)^2/m^2)*rho_(m,j)*B_(m,j),

and the useful exact identities are

    L_(m,j)-1=(5m-j^2-8j-1)/(m-j-1)^2,

    B_(m,j)=m(L_(m,j)-1)(A_(m,j)/m)^2
             +4L_(m,j)(A_(m,j)/m)+4L_(m,j)/m.

These identities compare adjacent positive sums directly; no differentiation
of the already-known asymptotic `p_n~C n^(-1/2)` is involved.

## 2. Difference Riemann limit

For `j/sqrt(m)->y`, the R67 factorial-ratio estimate gives
`rho_(m,j)->exp(-y^2)` locally uniformly, while

    m(L_(m,j)-1)->5-y^2,
    A_(m,j)/m->y^2-2,
    L_(m,j)->1.

Consequently

    G_(m,j)->G(y)

locally uniformly, where

    G(y)=(1/4)(-y^10+9y^8-20y^6+12y^4) exp(-y^2).

The R67 global bound
`rho_(m,j)<=C exp(-c j^2/m)`, together with the displayed identities and
`j<= (m-1)/2`, gives

    |G_(m,j)| <= C(1+y_j^10) exp(-c y_j^2),
    y_j=j/sqrt(m).

This integrable majorant handles both the Gaussian tail and the entropy region.
If `m` is even, the one extra endpoint term `T_(m,m/2)` is
`O(m^4 2^(-m))`; if `m` is odd the two upper limits agree. Therefore

    m^(3/2)(p_(m+2)-p_(m+3))
      =(1/sqrt(m)) sum_(j=0)^[floor((m-1)/2)] G_(m,j)+o(1)
      -> integral_0^infinity G(y)dy.

Using `integral_0^infinity y^(2r) exp(-y^2)dy
=sqrt(pi) Gamma(r+1/2)/2`,

    integral_0^infinity G(y)dy=33 sqrt(pi)/256.

Since `n=m+3`, this proves the strict difference theorem

    p_(n-1)-p_n ~ (33 sqrt(pi)/256)n^(-3/2),

or equivalently

    n^(3/2)(p_(n-1)-p_n)->33 sqrt(pi)/256.

The local audit checks the exact adjacent-term identities, the limiting
polynomial, and the Gaussian moment constant; the global majorant is the
R67 factorial-ratio lemma used as an analytic input.

## 3. Full quadratic-response consequence

R68 supplies, under its explicit complex-sector transfer hypotheses,

    d_n=D_n/n!=O(n^(-5/2)),
    n(d_n-d_(n-1))=O(n^(-3/2)).

With `kappa_n=d_n-p_n` and
`Lambda_n=n(kappa_n-kappa_(n-1))`, R69 gives

    Lambda_n
      =n(p_(n-1)-p_n)+O(n^(-3/2))
      ~ (33 sqrt(pi)/256)n^(-1/2)>0.

Thus the Gaussian-local quadratic-response eventual sign is positive in the
conditional formal hierarchy. Together with the corrected R65 cutoff scale,
this rules out a large-`n` negative Gaussian-local slope as the source of a
shrinking cutoff: `|Lambda_n|/n -> 0`, not infinity. It does not prove D.1;
any remaining shrinking finite-stage cutoff must come from finite-`t`
nonlinear or boundary-layer behavior.

The next target is therefore a finite-`t` nonlinear boundary-layer lemma, not
another Gaussian-point derivative or another isolated degree computation.

Audit command:

    python flat_shadow_projection_difference_r69/audit_r69.py

