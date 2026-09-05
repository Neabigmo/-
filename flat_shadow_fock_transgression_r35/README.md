# R35 — Fock first-grade linearity and SOS anchor tax

This folder records the finite proof-level audit after the R35 web round.  It
checks exact Fock polarization, the first shadow mismatch, the canonical first
ideal grade, and the algebraic square-completion obstruction.  It does not run
an optimizer, SOS solver, numerical degree search, large sweep, or relaxed-law
construction.

Run with:

```text
F:\anaconda3\python.exe -u flat_shadow_fock_transgression_r35\audit_r35.py
```

Expected output:

```text
R35_CUBIC_FIRST_GRADE_LINEARITY PASSED
R35_FIRST_IDEAL_GRADE_CANONICAL PASSED
R35_FOCK_SOS_ANCHOR_TAX PASSED
R35_BOUNDED_FOCK_SOS_TRANSGRESSION NO_GO
R35_CONSTRAINT_COUPLED_TRANSGRESSION REMAINS OPEN
R35_AUDIT_COMPLETED
```

## First mismatch and cubic grading

Let `N=2M+2`, let `b_j` be normalized Hermite/Fock coordinates, and let the
genuine law and positive flat shadow agree below `N` while
`Delta_N=b_N^mu-b_N^rho=q_M/sqrt(N!)`.  For the homogeneous same-factor cubic

`F_n(b)=sum_(i+j+k=n) sqrt(n!/(i!j!k!)) A_(ijk)b_i b_j b_k`,

the exact polarization is

`F(S+H)-F(S)=3B(H,S,S)+3B(H,H,S)+B(H,H,H)`.

With `ord_OU(H)=N`, the three terms begin at grades `N`, `2N`, and `3N`.
Consequently the first mismatch grade is purely linear.  In particular,
assuming the symmetric same-factor coefficient convention,

`F_N(b^mu)-F_N(b^rho)=3 A_(N00) Delta_N`,

and `A_(N00)=(2/3)^d binom(2d,d)/4^d>0` for `N=2d`.  The script checks the
finite identities and positivity of this coefficient formula.

## Canonical first ideal grade

For an ideal transgression `J=sum_d H_(d,K)F_d` with regular factors (no
negative OU grade), the shadow has `F_d(rho)=0` for `d<N`, and generators with
`d>N` start above grade `N`.  Therefore

`[u^N]J(rho_u)=H_(N,K)(g)F_N(rho)`.

This first nonzero ideal-grade coefficient is unaffected by the usual equality
gauge.  If the shadow remainder is required to be remote beyond `N` while
`q_M!=0`, its canonical coefficient must vanish, so the ideal part cannot carry
the first head defect.

## SOS anchor tax

Let a finite positivity part be `P=sum_r f_r^2`, and write
`c_r=f_r(g,xi_0)`, `d_r=partial_(b_N)f_r(g,xi_0)`.  Comparing the genuine law and
shadow at the first grade gives the exact transport equation

`q_M=2 Delta_N sum_r c_r d_r`.

For `q_M!=0`, this forces `sum_r c_r d_r=sqrt(N!)/2`, hence Cauchy–Schwarz yields

`P(g,xi_0) D_(N,K)^2 >= N!/4`,

where `D_(N,K)^2=sum_r |d_r|^2`.  Any fixed-grade evaluation functional bounded
by a law-independent analytic factor norm turns a K-uniform norm bound on the
factors into a K-uniform bound on `D_(N,K)`.  Thus the positive anchor budget
cannot tend to zero while the first signed head remains nonzero.

The scalar identity

`x=(c+x)^2/(2c)-c/2-x^2/(2c)`, `c>0`,

shows the same obstruction in one dimension: sending the grade-zero term
`c/2` to zero makes the remote coefficient `1/(2c)` blow up.  The cubic terms
are already remote at grades `2N` and `3N`; they cannot supply a hidden
first-grade positivity gain.

## Boundary of the no-go and next OPEN

This closes the route **Uniformly Bounded Finite Fock–SOS Graded Transgression**
on the `q_M!=0` branch.  It is a proof-mechanism obstruction, not a
full-exact counterexample.  It does not exclude a construction in which
positivity appears only after coupling signed homogeneous pieces to the exact
same-factor manifold and the probability cone, rather than through an ambient
finite SOS/quadratic-module factorization.

The minimum OPEN is therefore **Constraint-Coupled Non-SOS Graded Value
Transgression**: construct such a coupled non-SOS value identity with a
grade-zero defect tending to zero and a uniform remote norm, or prove that this
last coupled class is also impossible.  Gaussian rigidity and the `P_3K`
bridge remain OPEN and logically disconnected.
