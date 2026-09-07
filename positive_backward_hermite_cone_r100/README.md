# R100 — finite-depth certificate from the positive backward Hermite cone

Date: 2026-09-07.

R99 gave necessary positive backward-OU inequalities. This round extracts their
nonlocal consequence: a finite collection of observed Hermite moments can
certify that a density cannot have a backward tower deeper than a stated
amount.

## 1. General depth-feasibility polynomial

For a centered variance-one density `g`, let `a_m=E_g psi_m` and define

`F_m(t;g)=sum_(ell=0)^m c_(m,ell)t^ell a_(2m-2ell)-a_m^2`,

`c_(m,ell)=m!sqrt((2m-2ell)!)/(ell!(m-ell)!^2)`.

If `g=P_t h` for a positive `L^2(gamma)` density `h`, then R99 gives
`F_m(t;g)>0` for every `m>=1`. Therefore `F_m(t;g)<=0` is an exact
finite-dimensional obstruction to a positive backward preimage at parameter
`t`. For a depth-`N` fixed-factor tower one substitutes `t=q^N`; this uses the
whole relation `g^(0)=P_(q^N)g^(N)`, not merely its first edge.

## 2. A unique-root skew–kurtosis depth certificate

The `[psi_1,psi_2]` Schur complement from R99 is equivalent to

`f_(3,4)(t):=t^3+sqrt(6)a_4 t-3a_3^2>0`.

If `a_3 != 0`, `f_(3,4)` has exactly one positive root `tau_(3,4)`: if
`a_4>=0`, it is strictly increasing from `-3a_3^2` to `+infinity`; if
`a_4<0`, it first decreases and then increases, while its minimum is still
negative, so there is again exactly one positive root.

Consequently every positive backward preimage must satisfy
`t>tau_(3,4)`. For a depth-`N` tower, `q^N>tau_(3,4)`, so when
`0<tau_(3,4)<1`,

`N<log(tau_(3,4))/log(q)`.

If the root is at least one, no such depth is possible. If `a_3=0` and
`a_4<0`, the same certificate reduces to
`t>sqrt(-sqrt(6)a_4)`.

The certificate is strict for positive absolutely continuous preimages and
non-strict for arbitrary probability preimages.

## 3. Why this matters for the main OPEN

This converts the missing “charge-to-cone” step into a precise target. If the
same-factor exact-zero identity can show that a nonzero `P_3 K` charge forces
either a lower bound on `|a_3|` relative to `a_4`, or a finite-order violation
of some `F_m(q^N;g)`, then arbitrarily deep positive towers are excluded. The
current result does not supply that charge bridge: `P_3 K` may live in a higher
or angular sector while the one-dimensional low Hermite moments vanish.

## Status

- **PROVED:** exact finite-depth obstruction `F_m(q^N;g)<=0` and the unique-root
  skew–kurtosis depth certificate.
- **CONDITIONAL:** a charge-to-cone lower bound would close the corresponding
  tower subclass.
- **OPEN:** charge bridge, all-degree angular cone closure, and full Gaussian
  rigidity.

Audit:

`F:/anaconda3/python.exe positive_backward_hermite_cone_r100/audit_r100.py`
