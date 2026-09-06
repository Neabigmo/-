# R67 — associated-Hermite projection asymptotics

R67 closes the Gaussian-local projection sector left open in R66. The
webpage proof was independently checked at finite symbolic stages and its
normalizations are written here in ordinary fraction notation.

## 1. Exact associated-Hermite representation

Define

    A_(-1)^(c)=0, A_0^(c)=1,
    A_(m+1)^(c)(x)=x A_m^(c)(x)-(m+c)A_(m-1)^(c)(x).

For n>=3, with m=n-3, the projection recurrence gives

    q_n(x)=-A_m^(3)(x)+3x A_(m-1)^(4)(x).

The associated-Hermite polynomial has the exact ordinary-Hermite expansion

    A_m^(c)(x)=sum_(j=0)^(floor(m/2))
      (-1)^j binom(m-j,j) (c)_j H_(m-2j)(x).

After combining the c=3 and c=4 terms,

    q_n(x)=sum_(j=0)^(floor(m/2)) c_(m,j) H_(m-2j)(x),

where

    c_(m,j)=(-1)^(j+1)
      ((j+1)(j+2)(j^2+5j-2m)/2)
      ((m-j-1)!/(m-2j)!).

This is a polynomial identity, not a measure realization.

## 2. Positive finite sum for the projection norms

Gaussian Hermite orthogonality gives the exact positive sum

    P_n=||q_n||_gamma^2
       =sum_(j=0)^(floor(m/2)) c_(m,j)^2 (m-2j)!,

and hence

    p_n=P_n/n!
       =1/(4(m+3)!) sum_(j=0)^(floor(m/2))
          (j+1)^2(j+2)^2(j^2+5j-2m)^2
          ((m-j-1)!^2/(m-2j)!).

The audit checks the associated expansion, q formula, and positive norm sum
through n=18; it does not compute beta_11 or the degree-22 norm ratio.

## 3. Riemann-sum asymptotic

Introduce

    rho_(m,j)=m^5 (m-j-1)!^2 / ((m-2j)!(m+3)!).

The exact product form is

    rho_(m,j)=
      [product_(ell=j+1)^(2j-1) (1-ell/m)]
      /
      [product_(ell=-3)^j (1-ell/m)].

For j=y sqrt(m) with y in a fixed compact interval,

    rho_(m,j)->exp(-y^2),

uniformly. The elementary logarithm expansion gives this convergence; the
entropy estimate in the complementary j>=epsilon*m range and the usual
logarithm inequalities supply a Gaussian majorant

    rho_(m,j)<=C exp(-c j^2/m).

The j-th summand T_(m,j) in p_(m+3) satisfies

    m T_(m,j)=F_(m,j),

where, for y_j=j/sqrt(m),

    F_(m,j)=1/4 *
      ((j+1)^2(j+2)^2/m^2) *
      ((j^2+5j-2m)^2/m^2) *
      rho_(m,j).

Thus

    sqrt(m) p_(m+3)
      =1/sqrt(m) sum_(j=0)^(floor(m/2)) F_(m,j)
      -> integral_0^infinity F(y) dy,

with

    F(y)=1/4*y^4*(y^2-2)^2*exp(-y^2).

The Gaussian majorant makes the Riemann-sum passage legitimate. The integral
is

    integral F(y)dy=33 sqrt(pi)/128.

Therefore the new full asymptotic is

    p_n ~ (33 sqrt(pi)/128) n^(-1/2).

The exact audit checks the product identity, term normalization, and the
constant integral. Targeted exact values at n=100,200,500 are retained only
as orientation checks, not as proof.

## 4. Abel singularity and implications

Since p_n is nonnegative and p_n=O(n^(-1/2)), P(z)=sum p_n z^n is absolutely
convergent for |z|<1. The asymptotic and the Abelian estimate give

    P(z) ~ (33 pi/128) (1-z)^(-1/2)

as z approaches 1 from below. Therefore the projection part of
K(z)=D(z)-P(z) has a square-root pole, while the R66 D-part remains bounded
at z=1 under its stated analytic boundary estimate:

    K(z) ~ -(33 pi/128) (1-z)^(-1/2).

This is a genuine generating-function milestone. It still does not imply a
coefficientwise asymptotic for the full kappa_n, because R66 only established
a radial boundary estimate for D(z), not the coefficient-level transfer bound
needed to control D_n/n! and its first difference.

In particular, the projection contribution alone has

    -p_n ~ -(33 sqrt(pi)/128)n^(-1/2).

The full eventual sign of Lambda_n and the full Lambda_n asymptotic remain
OPEN until the D-part receives coefficient-level transfer control. If that
control is eventually shown to be lower order, the projection sector predicts
the positive slope constant 33 sqrt(pi)/256.

Audit command:

    python flat_shadow_associated_hermite_r67/audit_r67.py

The audit uses exact symbolic arithmetic and a few targeted exact orientation
values. It does not use determinants, optimizers, SDP, parameter sweeps,
relaxed measure LP, or remote computation.
