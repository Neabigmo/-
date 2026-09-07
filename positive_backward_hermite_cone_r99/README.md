# R99 — positive backward-OU Hermite cone

Date: 2026-09-07.

This note isolates a genuine probability consequence of one positive backward
OU preimage. If `g=P_t h`, with `g` and `h` nonnegative centered variance-one
densities relative to the standard Gaussian measure, then the Hermite
coefficients of `g` lie in an explicit `t`-dependent positive cone.

## 1. Exact cone

Let `psi_m=He_m/sqrt(m!)` and write
`a_m(g)=E_g[psi_m(X)]`, where `E_g` means integration against `g d gamma`.
Since the OU multiplier is `t^(m/2)`, a backward preimage has
`b_m=a_m(g)t^(-m/2)`.

For every finite `r`, positivity of `h d gamma` gives the exact Gram condition

`M_t(g)=[E_h(psi_i psi_j)]_(0<=i,j<=r) >= 0`,

where

`(M_t(g))_(ij) = sum_(ell=0)^[min(i,j)]
  ell! binom(i,ell) binom(j,ell)
  sqrt((i+j-2ell)!/(i!j!))
  t^(-(i+j-2ell)/2) a_(i+j-2ell)(g)`.

This is exactly the moment matrix of the positive preimage, not an
operator-only surrogate. If `h` is an `L^2(gamma)` density, every finite matrix
is in fact positive definite, because a nonzero polynomial cannot vanish on a
set of positive Lebesgue measure.

## 2. A high-order two-coefficient wall

Taking the principal minor indexed by `0,m` gives

`a_m(g)^2 <= sum_(ell=0)^m c_(m,ell) t^ell a_(2m-2ell)(g)`,

where
`c_(m,ell)=m! sqrt((2m-2ell)!)/(ell!(m-ell)!^2)`.

The leading term is `c_(m,0)a_(2m)` and the final term is `t^m`, since
`a_0=1`. This is the first direct high-Hermite cone constraint supplied by
positive backward divisibility.

## 3. Degree-three/degree-four local rigidity wall

For centered variance-one laws, `a_1=a_2=0`. The degree-two and degree-three
instances become

`a_4(g) > -t^2/sqrt(6)`,

and

`a_3(g)^2 < 2sqrt(5) a_6(g)+3sqrt(6)t a_4(g)+t^3`.

More strongly, the principal minor indexed by `1,2` gives

`a_4(g) > (3t^(-1)a_3(g)^2-t^2)/sqrt(6)`.

Equivalently, in raw centered moments `m_k=E_g[X^k]`,

`m_3^2 < t (m_4-3+2t^2)`.

The strict sign is for an absolutely continuous positive preimage; the
non-strict version holds for arbitrary probability preimages. The coefficient
is the exact determinant coefficient of the `[1,X,X^2]` moment matrix.

## 4. Finite backward towers

For a depth-`N` tower, `g^(0)=P_(q^N)g^(N)`, so the same inequalities hold with
`t=q^N`. In particular,

`a_4(g^(0)) > -q^(2N)/sqrt(6)`,

and

`a_3(g^(0))^2 < q^N( sqrt(6)a_4(g^(0))+q^(2N) )/3`.

Thus a depth-independent negative fourth-Hermite defect is impossible. If
`a_4(g^(0))<=0`, the sharper conditional bound is

`|a_3(g^(0))| < q^(3N/2)/sqrt(3)`.

This is a concrete quantitative local statement. It does not identify the
projected cubic charge `P_3 K`: the third Hermite moment and that charge remain
logically distinct. It also does not prove the full zero-set rigidity. What it
does provide is an exact interface: any future exact-zero identity that forces
an upper control on `a_4` or a relation between `a_4,a_6` can be inserted into
these walls, with no new positivity argument required.

## Status

- **PROVED:** the finite positive backward-preimage Gram cone and all displayed
  degree-three/four inequalities.
- **CONDITIONAL:** using the walls to eliminate a same-factor exact-zero branch
  requires a separate identity connecting that branch to `a_3,a_4,a_6`.
- **OPEN:** the charge bridge `P_3 K ->` a cone violation, mesoscopic all-degree
  closure, and the original positive backward-tower rigidity theorem.

Audit:

`F:/anaconda3/python.exe positive_backward_hermite_cone_r99/audit_r99.py`
