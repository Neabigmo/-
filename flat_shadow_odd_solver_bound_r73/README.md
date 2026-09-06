# R73 — Explicit canonical odd-solver majorant and conditional all-order window

R73 supplies the missing explicit `n`-dependent majorant for the canonical odd
Jacobi solver, conditional on the analytic Gram-domain/source estimate stated
below.  The result is deliberately coarse:

    Omega_n <= 22 L_n^3,
    L_n=(1+B_n)^n,
    B_n=512 n (448 n)^n,

and hence `Omega_n=exp(O(n^2 log n))`.  This is a real quantitative closure of
R72's previously unquantified odd-solver hypothesis, but it is far too large to
be compared sharply with the natural angular cutoff scale.  D.1, positivity of
an infinite exact tower, and backward OU divisibility remain open.

## 1. Exact triangular odd recursion

Use the normalized probabilists' Hermite basis

    e_m=H_m/sqrt(m!),
    eta_m=L[e_m],
    g_m=eta_m/sqrt(m!),
    ||g||_R=sum_m |g_m| R^m.

For `k<=n`, let `pi_k` be the monic orthogonal polynomial obtained from the
previous Gram block and put

    phi_k=pi_k/sqrt(k!)=e_k+sum_(j<k) v_(k,j)e_j,
    G_(k-1)=(L[e_i e_j])_(0<=i,j<k),
    g_k=(L[e_k e_j])_(j<k).

The block orthogonality equations are exactly

    v_k=-G_(k-1)^(-1) g_k.

For the canonical diagonal data

    alpha_1=a, alpha_2=-a, alpha_k=0 (k>=3),

the Jacobi relation is

    L[x phi_k^2]=alpha_k L[phi_k^2].

Since the leading term of `phi_k` is `x^k/sqrt(k!)`,

    x phi_k^2=d_k e_(2k+1)+sum_(m=0)^(2k)c_(k,m)e_m,
    d_k=sqrt((2k+1)!)/k!.

Therefore the only new odd coefficient is given exactly by

    eta_(2k+1)=k!/sqrt((2k+1)!) *
      [ alpha_k gamma_k - sum_(m=0)^(2k)c_(k,m) eta_m ],
    gamma_k=L[phi_k^2].

The source uses moments only through degree `2k`; the inverse factor is the
factorial `k!/sqrt((2k+1)!)`.  The even same-factor identity is not used to
solve this odd coefficient.

## 2. Gram stability on the analytic domain

Let `V_n=span(e_0,...,e_n)` and `T_(m,n)=P_(V_n) M_(e_m) P_(V_n)`.  Creation /
annihilation normal ordering gives the majorant

    ||T_(m,n)||_op <= 2^m (n+m)^(m/2)/sqrt(m!).

For `rho_n=4 sqrt(n)`, `3<=m<=2n`, `n>=3`,

    sqrt(m!)/rho_n^m * ||T_(m,n)||
      <= (1/2 sqrt(1+m/n))^m <= 27/64.

Thus a perturbation `f` with no degree-1 or degree-2 component satisfies

    ||G_n-I||_op <= (27/64)||f||_(rho_n).

On the complex domain

    ||e||_(rho_n)<=17/16,
    ||Y_n||_(sigma_n)<=1,
    sigma_n=8 sqrt(n)=2 rho_n,

the odd series starts at degree 3, so `||Y_n||_(rho_n)<=1/8` and
`||f||_(rho_n)<=19/16`.  Consequently

    ||G_n-I||_op <= 513/1024 < 1,
    ||G_k^(-1)||_op <= 1024/511 < 2.01.

This is the domain-stability input for the triangular construction.  The local
audit checks the constants and the radius arithmetic; it does not replace a
full proof of the analytic source estimate in every functional realization.

## 3. Coarse source and propagation bound

The normalized leading coefficient gives the weighted source factor

    32 7^n * k! sigma_n^(2k+1)/(2k+1)!.

For `k<=n`, this is bounded by

    256 sqrt(n) (448 n)^n <= B_n,
    B_n=512 n (448 n)^n.

If `S_k` denotes the accumulated sigma-weighted odd coordinates, the triangular
Schwarz estimate gives

    S_k <= (1+B_n) S_(k-1) + B_n |a|,
    S_n <= L_n |a|,
    L_n=(1+B_n)^n.

Taking `r_n=1/(4L_n)` keeps the odd solution inside the unit Gram domain.  The
reflection symmetry `Y_n(-a,e)=-Y_n(a,e)` makes `H_n=Y_n/a` even in `a`.  Cauchy
estimates then give

    ||Y_n(a,e)-Y_n(a,0)||_(sigma_n)
      <=16 L_n |a| ||e||_(rho_n),

and, with `U^(n)=H_n(0,0)`,

    ||Y_n(a,0)-a U^(n)||_(sigma_n)
      <=(4L_n/(3r_n^2)) |a|^3
      =(64/3)L_n^3 |a|^3.

Hence the R72 odd remainder obeys the explicit conditional estimate

    ||O_n(a,e)||_(sigma_n)
      <= Omega_n (|a|^3+|a| ||e||_(rho_n)),
    Omega_n=22 L_n^3.

Since `1+B_n <=1024 n (448n)^n`,

    Omega_n <=22 (1024n)^(3n) (448n)^(3n^2)
             =exp(O(n^2 log n)).

## 4. Conditional no-reversal window

Let

    U_n=||U^(n)||_(sigma_n),
    a_n#=min{
      r_n/2,
      1/(20*4^n U_n),
      sqrt(U_n/[2 Omega_n(1+10 U_n^2)])
    },
    t_n#=(a_n#)^2.

The R72 even source inequality

    E_n=||e||_(rho_n) <= (1/6)(3X_n^2+X_n^3),
    X_n=||aU+o+e||_(sigma_n),

bootstraps, for `|a|<=a_n#`, to

    E_n<=10 a^2 U_n^2,
    ||o||_(sigma_n)<=|a|U_n/2,
    4^n E_n<=|a|U_n/2,
    X_n<=2|a|U_n.

Together with the Gram estimate this gives `||G_n(a)-I||_op<1`, and therefore

    gamma_k(a)>0,
    beta_k(a^2)=gamma_k(a)/gamma_(k-1)(a)>0,
    0<=t<=t_n#,  k<=n.

This is an explicit conditional all-order no-reversal interval.  It only says
that any finite-stage reversal must lie outside this very conservative window;
it neither proves D.1 nor constructs a positive infinite backward tower.

## 5. Status and next target

R73 closes the bookkeeping gap in R72 by giving an explicit, auditable
`Omega_n`, but its `exp(O(n^2 log n))` growth is not sharp enough to settle the
natural boundary layer.  The next target is the degree-local odd Green-function
sharpening: retain the factorial factor `k!/sqrt((2k+1)!)` at each level instead
of replacing all source coordinates by `B_n`.  The desired outcome is an
`e^(O(n log n))` or `C^n n^p` majorant, which would make the no-reversal window
quantitatively comparable to the angular scale.

