# R18 — Laguerre–Abel endpoint audit

## Exact bridge

For the ordinary Laguerre basis

\[
L_n(t)=\sum_{k=0}^n(-1)^k {n\choose k}t^k/k!,
\]

the generating function is

\[
\sum_{n\geq0}r^nL_n(t)=\frac1{1-r}\exp\!\left(-\frac{rt}{1-r}\right),
\qquad |r|<1.
\]

With the `Exp(1)` measure this gives, for `h >= 0`,

\[
H(r)=\sum_{n\geq0}e_nr^n
 =\frac1{1-r}\int_0^\infty h(t)
       \exp\!\left(-\frac{t}{1-r}\right)dt\geq0,
\qquad 0\leq r<1.
\]

This is an exact necessary consequence of pointwise conditional-variance
positivity. It is not an equivalence: positivity of one Laplace family does
not by itself imply pointwise positivity of `h`.

## The odd-data quadratic form

If `m(t)=sum c_n L_n(t)`, then

\[
\mathcal Q_r(c)=\sum_{i,j}c_ic_jK_{ij}(r)
 =\frac1{1-r}\int_0^\infty e^{-t/(1-r)}m(t)^2dt\geq0,
\]

where the exact finite formula is

\[
K_{ij}(r)=\sum_{p=0}^i\sum_{q=0}^j
 \frac{(-1)^{p+q}{i\choose p}{j\choose q}(p+q)!}{p!q!}
 (1-r)^{p+q}.
\]

The conditional second moment has the exact operator representation

\[
D(r)=\frac1{1-r}\mathbb E\!\left[\bar X^2e^{-T/(1-r)}\right],
\]

but R17 only supplies `d0,...,d3`; it does not supply an all-orders
Fock-determined formula for `D(r)`.

## Endpoint obstruction

The Abel kernel concentrates at `t=0` as `r` tends to one. This is not a
uniform norm coercivity mechanism. The exact finite witness

\[
c_0=1,\quad c_1=-1,\quad m(t)=L_0(t)-L_1(t)=t
\]

has `||c||_2^2=2` but

\[
\mathcal Q_r(c)=2(1-r)^2\longrightarrow0.
\]

Thus the endpoint transform alone cannot yield a bound of the form
`Q_r(c) >= kappa ||c||^2` with a positive endpoint-uniform `kappa`.

## Honest conclusion

R18 certifies the Abel bridge and identifies a precise obstruction. It does
not derive the missing all-orders `D(r)` relation and does not prove
`c_n=0`. The next theory task must provide additional Fock structure (or a
different positive kernel) that controls Laguerre modes invisible to the
endpoint jet.
