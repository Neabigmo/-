# R19 theory note

Let `q` be the centered three-sample quadratic form and impose the target
relations `E[q^k]=2^k k!` for `k=2,...,5`. Exact elimination gives

\[
\mu_4=3,\quad \mu_6=15+7\mu_3^2,
\]
\[
\mu_8=105-124\mu_3^2+32\mu_3\mu_5,
\]
\[
\mu_{10}=945+1410\mu_3^2-840\mu_3\mu_5+60\mu_3\mu_7+51\mu_5^2.
\]

Using the ordinary Exp(1)-orthonormal Laguerre basis, the exact coefficients
are

\[
c_1=-\frac{\mu_3}{3},\qquad
c_2=\frac{\mu_5-10\mu_3}{18},\qquad
c_3=-\frac{105\mu_3-21\mu_5+\mu_7}{162},
\]

and

\[
d_4=\frac{4000\mu_3^2-800\mu_3\mu_5+20\mu_3\mu_7+19\mu_5^2}{1944}.
\]

The proposed identity predicts

\[
d_4^{\star}=5c_1c_3+\frac52c_2^2.
\]

Exact subtraction gives

\[
d_4-d_4^{\star}
 =\frac{(10\mu_3-\mu_5)^2}{486}
 =\frac23c_2^2.
\]

Therefore the proposed identity is **not** an identity in the currently
known Fock/Q-law moment quotient. It is not legitimate to call this an
actual probability counterexample, because the quotient has not been shown
to contain a full probability law satisfying every all-order condition. The
correct conclusion is narrower and decisive for planning: the scalar closure
route cannot proceed from the current finite identities alone. To resurrect
it, one must supply an independent all-order relation implying `c2=0` (or a
different source-Hessian formula). Otherwise the cross-parameter/spatial
coherence route must be restored as the primary theory target.
