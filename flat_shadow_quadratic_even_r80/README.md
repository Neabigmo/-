# R80 — quadratic-even centered operator lemma

Date: 2026-09-07.

This record follows the completed R80 webpage response.  The bridge still
reported an account-connection error while the webpage was working, so the
webpage did not actually read the R79 files or verify commit `c7cd92a`.
The equations below are therefore compared with the local R64/R79 baseline
and are explicitly split into verified identities, conditional statements,
and open steps.

## 1. The local milestone

Assume the R64 formal same-factor hierarchy and write the Gaussian-normalized
transform as

`F_a(z)=1+aU(z)+a^2V(z)+O(a^3)`.

The tangent is

`U(z)=z^3 integral_0^1 q_s exp(-q_s z^2)(1-q_s z^2/2) ds`,
`q_s=s(1-s)`.

The quadratic equation is

`A V=-B`,
`B(w)=average_theta sum_(i<j) U(r_i w)U(r_j w)`,

with

`A z^(2m)=A_(2m) z^(2m)`,
`A_(2m)=3*6^(-m)*binomial(2m,m)`.

The main R80 result is conditional on this exact R64 equation:

`sup_n ||Hcal_n(V)||_op < infinity`,

where `Hcal_n(V)` is the Gram compression in the normalized Gaussian
Hermite basis.  The proof supplies an explicit bounded multiplier `g_2`
with `T g_2=V`.

## 2. Exact Beta inverse and explicit multiplier

The finite coefficient identity

`1/binomial(2m,m)=(2m+1) integral_0^1 [tau(1-tau)]^m d tau`

gives the coefficientwise exact inverse

`A^(-1)W(z)=(1/3) integral_0^1 (1+z partial_z)
 W(sqrt(6q_tau) z) d tau`.

For one pair, put `a=r_i^2`, `b=r_j^2` and

`xi=6q_tau q_s a`, `eta=6q_tau q_u b`, `alpha=xi+eta`.

Since `q<=1/4` and `a+b<=1`, `0<=alpha<=3/8<1/2`.  Direct symbolic
differentiation gives

`(1+z partial_z)[z^6 exp(-alpha z^2)
 (1-xi z^2/2)(1-eta z^2/2)]`

`=exp(-alpha z^2)[7z^6-(13/2)alpha z^8
 +(alpha^2+(11/4)xi eta)z^10 -(1/2)alpha xi eta z^12]`.

With `R=x-partial_x`,

`psi_alpha=(1-2alpha)^(-1/2)
 exp[-alpha x^2/(1-2alpha)]`,

the exact transform rule is `T(R^m psi_alpha)=z^m exp(-alpha z^2)`.  Thus

`g_2(x)=-(1/3) average_theta sum_(i<j) integral_[0,1]^3
 W_(tau,s,u)^(ij) g_(alpha,xi,eta)(x) d tau ds du`,

where `g_(alpha,xi,eta)` is the four-term `R^6,R^8,R^10,R^12`
combination displayed above.  This is an explicit representative of `V`.

## 3. Endpoint estimate — independently tightened

The only delicate endpoint is `alpha -> 0`.  If

`I(a,b)=integral_[0,1]^2 q_s q_u a^(3/2)b^(3/2)
 /(a q_s+b q_u)^3 dsdu`,

symmetry reduces to `s,u<=1/2`.  There `s/2<=q_s<=s` and
`u/2<=q_u<=u`, so

`I(a,b)<=32 J(a,b)`,

`J(a,b)=integral_[0,1/2]^2 su a^(3/2)b^(3/2)/(as+bu)^3 dsdu`.

For positive `a,b`, the exact substitution `x=as`, `y=bu` and the exact
integral

`integral_0^A integral_0^B xy/(x+y)^3 dxdy=AB/[2(A+B)]`

give

`J(a,b)=sqrt(ab)/[4(a+b)]<=1/8`.

The boundary cases follow by continuity.  Hence the webpage's bound `32`
is valid but very coarse; the local audit proves the stronger `I(a,b)<=4`.
The finite Hermite-polynomial estimate gives

`||g_(alpha,xi,eta)||_infinity <= C_* alpha^(-3)`,

so, with three pairs and the outer factor `1/3`,

`||g_2||_infinity <= 4 C_* =: M_2 < infinity`.

This closes the parameter endpoint at the multiplier level.  It does not
yet prove the full infinite positive tower.

## 4. Uniform Gram compression and centered background

For `e_k=H_k/sqrt(k!)`, `V_n=span(e_0,...,e_n)`,

`Hcal_n(V)=P_n M_(g_2) P_n`,

therefore

`sup_n ||Hcal_n(V)||_op <= M_2`.

Writing `E=a^2V+Ehat`, `Y=aU+o`, the exact centered decomposition is

`G_n=I+aA_n+a^2B_n^(2)+Hcal_n(Ehat+o)`,
`B_n^(2)=P_nM_(g_2)P_n`.

With the inherited residual estimate
`||Hcal_n(h)||_op<=C_G||h||_(4sqrt(n))`, the conditional Gram domain

`|a|M_1+a^2M_2+C_G(||Ehat||_n+||o||_n)<=1/2`

gives `||G_n^(-1)||_op<=2` and the usual first three resolvent derivative
bounds.  This is an operator-norm result in Gaussian `L^2`, not a claim that
the growing coefficient-Wiener norm of `V` is bounded.

## 5. Conditional residual bootstrap

The R79 parity ideal, after tangent subtraction, is
`S_tilde in E(a,o)+(a,o)^3`.  Substitution of `E=a^2V+Ehat` gives

`S_tilde in (a^2V+Ehat)(a,o)+(a,o)^3`.

The bounded-multiplier representation removes `V` from the source norm only
conditionally: the R77 hypercontractive/factorial transport must be rerun
around the background `I+aA_n+a^2B_n^(2)`.  Under that conditional lemma, for
fixed `mu>3`,

`k! |S_tilde_k| <= C_mu^(2) mu^k
 [(|a|+||o||_n)||Ehat||_n+(|a|+||o||_n)^3]`,

and the signed Green transfer gives

`O:=||o||_n <= Gamma_(n,mu)[(|a|+O)Ehat_*+(|a|+O)^3]`,

`Gamma_(n,mu)=K_mu^(2)n^(-1/2)[16e(mu+1)]^n`.

The exact same-factor even estimate remains coefficientwise:

`Ehat_* <= 2xO+O^2+P^2+3(x+O)^2P+P^3`,
`x=|a|H_n`, `P=x^2+Ehat_*`.

For `delta=10^(-4)`, the audited bootstrap assumptions

`x, Gamma a^2 H_n, Gamma a^4 H_n^4 <= delta`

close with

`O<=16|a|(Gamma a^2+Gamma a^4H_n^4)`,
`Ehat_*<=8(xO+x^4)`.

Thus the improved statement is conditional but real: the old quadratic
`E=O(a^2H_n^2)` is absorbed into the operator background, and only the
quartic residual feeds back into the odd equation.

## 6. Safe window and comparison with the angular scale

One explicit conditional endpoint is

`a_bg=min(1,1/(8M_1),1/sqrt(8M_2))`,

`a_(n,mu)#=min{a_bg, delta/H_n,
 sqrt(delta/(Gamma_(n,mu)H_n)),
 (delta/(Gamma_(n,mu)H_n^4))^(1/4)}`.

Using `H_n<=4n^3(4e)^n` and
`Gamma_(n,mu)<=K_mu^(2)n^(-1/2)[16e(mu+1)]^n`, the dominant large-n
condition is `Gamma a^2 H_n<=delta`.  Therefore

`t_(n,mu)^safe=(a_(n,mu)#)^2
 >= c_mu n^(-5/2)[64e^2(mu+1)]^(-n)`.

The base tends to `256e^2` as fixed `mu downarrow 3`.  Since

`A_(2n)~3(2/3)^n/sqrt(pi n)`,

`t_(n,mu)^safe/A_(2n)
 =O_mu(n^(-2)[3/(128e^2(mu+1))]^n)->0`.

The quadratic centering removes one complete tangent factor from the
previous sufficient window, but it is still far from the angular natural
boundary layer.

## 7. Exact status boundary and next target

Unconditional relative to the stated R64 formal equation: Beta inversion,
the differential polynomial, `alpha<1/2`, the endpoint integral, and the
explicit multiplier construction are checked locally.  The stronger
`||g_2||_infinity<=4C_*` bound is also checked.

Conditional: the passage from this bounded multiplier to the full factorial
source lemma, the connected finite Jacobi branch, positivity, and the safe
window above.

Still OPEN: a uniform `O(a^2)` bound for the `Ehat -> o` signed-Green
multiplier.  Bounded Gram compression alone only gives the existing
`Gamma a^2 H_n` feedback scale.  The next structural target is the mixed
operator composition

`o -> A^(-1)Q(U,o) -> signed-Green D_E S`,

seeking an `n`-uniform bound.  D.1, a positive infinite exact backward tower,
backward OU divisibility, and global positivity remain OPEN.

Audit command:

`python flat_shadow_quadratic_even_r80/audit_r80.py`

The audit uses exact symbolic arithmetic and fixed checks only; it uses no
determinants, optimizers, SDP, sweeps, relaxed measure LP, or remote
computation.
