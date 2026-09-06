# R79 — Tangent-centered Gram/source bootstrap

R79 isolates the first genuinely global-looking operator feature of the
finite hierarchy: the Gaussian tangent is large in the growing coefficient
Wiener norm, but its Gram action is a uniformly bounded compression. The
remaining nonlinear residual can therefore be treated around that tangent
background. The result is still a local, conditional finite-level theorem;
it does not by itself prove D.1 or construct a positive infinite backward
tower.

## 1. Center the Gram operator at the tangent

Let `e_j=H_j/sqrt(j!)`, `V_n=span{e_0,...,e_n}`, and `P_n` be the Gaussian
orthogonal projection. Decompose the functional as

    L_(a,E,o)=L_0+a L_1+L_(E+o),

where `E` is even, `o` is odd, and `L_1[p]=integral p g_1 d gamma` is the
audited tangent representer. With

    A_n=P_n M_(g_1) P_n,
    Hcal_n(h)=(L_h[e_i e_j])_(0<=i,j<=n),

the exact Gram identity is

    G_n(a,E,o)=I+a A_n+Hcal_n(E+o).

Since `g_1` is bounded,

    M_1=sup_n ||A_n||_op <= ||g_1||_infinity < infinity.

For `R_n=4 sqrt(n)` and the coefficient norm
`||h||_n=sum_(m<=2n+1)|h_m| R_n^m`, the degree-local Hermite multiplication
estimate gives

    ||Hcal_n(h)||_op <= C_G ||h||_n,
    C_G=(sqrt(3)/2)^3/(1-sqrt(3)/2)<5.

Consequently, on

    |a| M_1+C_G(||E||_n+||o||_n)<=1/2,

`||G_n^(-1)||_op<=2`. The resolvent derivative bounds depend on the tangent
direction through `M_1 |dot a|` and on residual directions through
`C_G ||dot h||`; no factor `|a| ||U||_n` is paid merely to invert the Gram
matrix.

## 2. Parity and the centered source ideal

Reflection gives

    P A_n P=-A_n,
    P Hcal_n(E)P=Hcal_n(E),
    P Hcal_n(o)P=-Hcal_n(o),

and hence `P G_n(a,E,o)P=G_n(-a,E,-o)`. Let `U` be the exact R64 tangent
and write `Y=aU+o`. After subtracting the finite-head tangent source
`a S^(1)`, `S^(1)(x)=x+x^2/2`, the source residual satisfies the formal local
ideal inclusion

    S_tilde in E(a,o)+(a,o)^3.

Here `E(a,o)` means terms containing one factor of `E` and at least one
factor of `a` or `o`; `(a,o)^3` means total degree at least three in the
centered variables. In particular there is no constant, linear, or pure
quadratic `a^2` source term after centering. The degree-local factorial
estimate, conditional on the R77 Gram/source derivative hypotheses, is

    k! |S_tilde_k| <= C_mu mu^k
      ((|a|+||o||_n)||E||_n+(|a|+||o||_n)^3),

for every fixed `mu>3`. The signed Green transfer then yields

    ||o||_n <= Gamma_(n,mu)
      ((|a|+||o||_n)||E||_n+(|a|+||o||_n)^3),

    Gamma_(n,mu)=K_mu n^(-1/2)[16 e (mu+1)]^n.

## 3. What closes and what does not

The R78 same-factor even estimate remains

    E_* <= (E_*+x+O)^2+(E_*+x+O)^3,

where `E_*=||E||_n`, `O=||o||_n`, and

    x=|a| H_n,
    H_n=sum_(k=1)^n k(k+1)!/[2(2k+1)!] (4 sqrt(n))^(2k+1)
       <=4 n^3 (4e)^n.

For `x<=x_0=min(1/100,1/(32 C_G))`, the local bootstrap gives
`E_*<=5x^2` and, provided `48 Gamma_(n,mu) x^2<=1`, `O<=x/2`. Thus the
tangent-centered Gram domain is compatible with the bootstrap at

    a#=min{1/(4M_1), x#/H_n},
    x#=min{x_0,[48 Gamma_(n,mu)]^(-1/2)}.

The important gain is structural: the inverse domain itself no longer asks
for `|a| H_n` to be small. The obstruction has merely moved to the residual
even size in the `E o` feedback. The scalar model

    E=x^2,   O=Gamma(a E+E O),
    O=Gamma a E/(1-Gamma E)

shows that a uniform estimate still needs `Gamma E<1`; boundedness of `A_n`
alone cannot remove this requirement.

Using the coarse displayed bounds gives only

    a# >= c_mu n^(-11/4)
      [4e sqrt(16e(mu+1))]^(-n),
    (a#)^2 >= c'_mu n^(-11/2)
      [256 e^3(mu+1)]^(-n).

This is a real local/operator milestone, but it remains far below the natural
angular scale `A_(2n)~3(2/3)^n/sqrt(pi n)`. D.1, positivity-driven global
closure, the positive backward tower, backward OU divisibility, and the
endpoint `FS_3` remain OPEN.

## 4. R80 target

Let `V` denote the audited R64 quadratic-even response and split
`E=a^2 V+Ehat`. The next target is to prove either

    sup_n ||Hcal_n(V)||_op < infinity,

so that `a^2 V` can be absorbed into `I+a A_n+a^2 B_n`, or directly prove a
uniform signed-Green estimate for the `a^2 V` contribution to the odd source.
Either result would replace the worst `Gamma a^2 H_n^2` feedback by a uniform
`O(a^2)` term and is the shortest route to a materially stronger local result.

