# R74 — Degree-local odd Green kernel and exponential conditional tame bound

R74 keeps the factorial transfer in the exact odd Jacobi recursion instead of
replacing every level by the same `B_n`. The Gaussian linearized kernel has an
explicit Volterra form and its row sum is only `e^(O(n))`. A finite-head Jacobi
Duhamel argument then proposes the conditional bound

    Omega_n <= 2^26 n^3 exp(544 n),

which improves R73's `exp(O(n^2 log n))` to pure exponential growth. The local
audit accepts the exact kernel and all displayed arithmetic. The passage from
the parity/Gram estimates to the full Duhamel constants is recorded as a
conditional analytic lemma, not as an unconditional construction of the
infinite positive tower.

## 1. Exact normalization

Use

    e_m=H_m/sqrt(m!),
    eta_m=L[e_m],
    phi_k=pi_k/sqrt(k!),

so `phi_k=x^k/sqrt(k!)+lower degree`. Hence

    x phi_k^2=d_k e_(2k+1)+sum_(m<=2k)c_(k,m)e_m,
    d_k=sqrt((2k+1)!)/k!,

and the canonical Jacobi equation gives

    eta_(2k+1)=k!/sqrt((2k+1)!) *
      [alpha_k gamma_k-sum_(m<=2k)c_(k,m)eta_m].

For `k>=3`, `alpha_k=0`; the current odd coefficient is the only new
unknown. This is the same normalization as R73, with no fraction reversal.

## 2. Gaussian degree-local kernel

At the Gaussian point `phi_k=e_k`. The product identity

    H_k^2=sum_(r=0)^k r! binom(k,r)^2 H_(2k-2r)

and `x H_m=H_(m+1)+m H_(m-1)` give, for `0<=j<k`,

    [x e_k^2]_(e_(2j+1))
      =sqrt((2j+1)!) * k!/[j!^2(k-j)!]
        * (1+2(k-j)/(j+1)).

With

    y_j=|eta_(2j+1)| sigma_n^(2j+1)/sqrt((2j+1)!),
    sigma_n=8 sqrt(n),

the exact linearized transfer from `y_j` to `y_k` is

    K_(k,j)^(n)=
      (k!)^2(2j+1)!/[(2k+1)! j!^2(k-j)!]
      * (1+2(k-j)/(j+1)) sigma_n^(2(k-j)).

Putting `d=k-j`,

    (k!)^2(2j+1)!/[j!^2(2k+1)!]
      =prod_(r=1)^d (j+r)^2/[(2j+2r)(2j+2r+1)]
      <=4^(-d),

so

    K_(k,j)^(n)<= (1+2d)(16n)^d/d!,
    sum_(j<k)K_(k,j)^(n)<=(1+32n) exp(16n)-1.

This is the sharpest unconditional algebraic result of R74: the Gaussian
linearized odd Green row has `e^(O(n))` size. It does not by itself control the
non-Gaussian Gram feedback.

## 3. Conditional Jacobi Green resummation

Write the finite Jacobi matrix as

    J=B+aD,
    D=diag(0,1,-1,0,...),

where `B` is zero-diagonal with Gaussian value `B_0` having off-diagonals
`sqrt(k)`. For degrees up to `2n+1`,

    Phi_(B,a)(z)=exp(-z^2/2)<e_0,exp(z(B+aD))e_0>,
    Y(a,B)=[Phi_(B,a)-Phi_(B,-a)]/2.

The parity/Gram estimate is formulated on

    rho_n=4 sqrt(n),
    ||E||_(rho_n)<=1,
    ||Y||_(rho_n)<=1/16.

Using the truncated Hermite multiplication operators gives

    ||G_n-I|| <=(2/3)||E+Y||_(rho_n),
    lambda_min(G_0)>=1/3,
    lambda_min(G)>=7/24,

and, conditionally on the associated Schur-complement/resolvent estimates,

    |gamma_k(E,Y)-gamma_k(E,0)|<=40||Y||_(rho_n)^2,
    |beta_k/k-1|<=5||E||_(rho_n)+275||Y||_(rho_n)^2,
    ||B-B_0||<=sqrt(n)[10||E||_(rho_n)+550||Y||_(rho_n)^2].

The point is structural: odd moments do not perturb the zero-diagonal Jacobi
part at first order; the feedback is `O(E)+O(Y^2)`.

Taking `R=2 sigma_n=16 sqrt(n)`, the stated operator norms imply the crude
resolvent bound `exp(224n)` on `|z|=R`. A Duhamel expansion with one
`B-B_0` insertion and the cubic odd remainder gives the conditional estimate

    ||Y-aU||_(sigma_n)
      <=1024 n exp(224n)|a| ||B-B_0||
        +1366 n^(3/2) exp(224n)|a|^3.

Substitution and the degree-3 contraction
`||Y||_(rho_n)<=||Y||_(sigma_n)/8` reduce the feedback to

    ||o||_(sigma_n)
      <= C_n(|a| ||E||_(rho_n)+|a|^3)
        +17600 n^(3/2) exp(224n)|a| ||o||_(sigma_n)^2,

where `C_n=2^25 n^3 exp(544n)`. For

    |a|<=r_n=2^(-31)n^(-3) exp(-544n),

the quadratic term is absorbable on the connected branch, yielding the
conditional Odd Green Tame bound

    ||O_n(a,E)||_(sigma_n)
      <=Omega_n(|a|^3+|a| ||E||_(rho_n)),
    Omega_n=2^26 n^3 exp(544n).

## 4. Correct even bootstrap and no-reversal window

The direct coefficientwise angular inverse at the ratio
`rho_n/sigma_n=1/2` satisfies

    A_(2k)^(-1)(rho_n/sigma_n)^(2k)<=1/4.

Thus the R72 even source equation can be used in the form

    E_n<=1/4(3X_n^2+X_n^3),
    X_n=||aU+o+E||_(sigma_n).

With `Ubar_n=32 sqrt(n) exp(160n)`, the sufficient conditions are

    |a|<=min{r_n,
      1/(12*4^n Ubar_n),
      sqrt(Ubar_n/[4 Omega_n(1+3 Ubar_n^2)])}.

The strict bootstrap uses the two quarter bounds
`||o||_(sigma_n)<=|a|Ubar_n/4` and
`||E||_(sigma_n)<=|a|Ubar_n/4`, hence
`X_n<=3|a|Ubar_n/2`; replacing this by `2|a|Ubar_n` would not itself give a
strict improvement with the coefficient `1/4`.

For sufficiently large `n`, the first term `r_n` is the smallest, so one may
take conditionally

    a_n#=2^(-31)n^(-3) exp(-544n),
    t_n#=2^(-62)n^(-6) exp(-1088n),

and obtain `gamma_k(t)>0`, `beta_k(t)>0` for `k<=n` and `0<=t<=t_n#`.

## 5. Status

R74 closes the super-exponential bookkeeping loss in the odd solver and shows
that the Gaussian local kernel itself is not the source of an
`exp(O(n^2 log n))` barrier. Quantitatively, `t_n#` is still far below

    A_(2n)~3 (2/3)^n/sqrt(pi n),

so the natural angular exponent is not matched. D.1, a positive infinite
exact backward tower, and backward OU divisibility remain OPEN. The next target
is the moving-radius kernel: use `sigma_k~sqrt(k)` at level `k` and propagate
the exact gap kernel between radii, with the aim of reducing the exponent `544`
and testing whether the no-reversal scale can approach `A_(2n)`.

