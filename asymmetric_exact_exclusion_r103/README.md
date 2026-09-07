# R103 — asymmetric genuine exact-law exclusion: exact local advances and obstruction

This package records the R103 webpage derivation and its local exact audit. It does
not claim the asymmetric genuine full-exact exclusion or the final positive
backward-tower rigidity.

## New exact statements audited here

Let

`mathscr K(z,theta)=sum_j K(z*a_j(theta))-z^2/2`,
`w_z(theta)=exp(mathscr K(z,theta))`, and
`c_r(z)=<exp(-3*i*r*theta) w_z(theta)>`.

1. For real `z`, the Herglotz/Toeplitz positivity gives the sharp first predictor
   bound

   `exp(<mathscr K>) <= 1-c_1(z)^2`.

   With `b=c_2-c_1^2`, the two-step analytic predictor gives, for sufficiently
   small `z`,

   `exp(<mathscr K>) <= 1-c_1^2-b^2`.

   These inequalities are genuine measure-level consequences, but they are
   one-sided compensation bounds and do not by themselves exclude asymmetry.

2. If `d` is the first nonzero odd cumulant, same-factor cubic exactness forces
   every even `kappa_m` with `4<=m<2d` to vanish and forces

   `kappa_(2d)=-(2d)!/(2(d!)^2) * <p_d^2>/<p_(2d)> * kappa_d^2 < 0`.

   If `q_r=[z^d]Q_r` is the degree-`d` log-charge in angular sector `r`, then

   `-[z^(2d)]<mathscr K> = sum_{r: 3r<=d, r odd} |q_r|^2`.

   Thus the first odd cumulant pays an exact all-angular-charge energy tax. The
   ratio to the `r=1` charge is `T_d>=1`, with `T_d>1` for `d>=9`.

3. For `d=3,5,7`, the next predictor is already nontrivial:

   `[z^(2d)]Q_2 = -eta_d q_1^2`,
   `eta_d=binom(2d,d-3)/binom(2d,d)`,

   giving `eta_3=1/20`, `eta_5=5/28`, `eta_7=7/24`.

## Explicit non-genuine obstruction

The family

`h_0(x)=sin(x)-(exp(3/2)/2)sin(2x)`,
`f_theta(x)=1+2*epsilon*h_0(x)cos(3theta)`,

is a positive centered variance-one D3/reflection-covariant Gaussian-density
family for `0<epsilon<1/(2*||h_0||_infty)`. It has Gaussian barycenter and the
full pointwise Herglotz cone. Its normalized MGF is

`w_z(theta)=1+2*epsilon*H(z)cos(3theta)`,
`H(z)=exp(-1/2)(sin(z)-sin(2z)/2)`.

At degree six, its log coefficients satisfy
`[z^6]R=-q^2` and `[z^6]Q_2=-q^2/2`, where
`q=epsilon*exp(-1/2)/2`. A genuine iid same-factor cubic law with first odd
degree three would require the ratio `1/20`, since
`Lambda_(6,2)/<p_6>=(1/72)/(5/18)=1/20`. The explicit family has ratio `1/2`,
so it is exactly excluded at degree six. This is a measure-level
nonfactorization obstruction, not a genuine counterexample.

A formal same-factor jet with `kappa_3=epsilon`, `kappa_6=-3 epsilon^2` and
lower unused cumulants zero satisfies the exact barycenter identity through
degree six. Hence finite cumulant jets and finite positivity checks cannot close
the genuine problem; an all-degree Schur/Herglotz coherence plus one-body
probability-realization argument is still needed.

## Status

- `R103-A`, `R103-B`, `R103-C`, and the degree-six obstruction: **LOCAL-AUDITED**.
- Asymmetric genuine full-exact-law exclusion: **OPEN**.
- The `RK=1` to genuine full-exact identification remains **CONDITIONAL** unless
  established independently elsewhere in the project.

Run the audit with the project Anaconda interpreter:

`F:/anaconda3/python.exe asymmetric_exact_exclusion_r103/audit_r103.py`
