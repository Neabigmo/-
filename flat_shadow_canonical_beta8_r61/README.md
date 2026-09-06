# R61 — corrected beta8 cutoff

R61 continued the canonical family after the R60 result
`0<t<tau6`, where `tau6` is the unique root of `P6` in `(1/20,1/10)`.
The webpage correctly identified the qualitative alternative — degree 16
creates a new cutoff — but its rendered high-degree formulas did not survive
the local recurrence check.  The formulas below are the independently
recomputed ones, with `beta8=h8/h7`.

## Degree-16 continuation

With `a=m3`, `t=a^2`, `alpha1=a`, `alpha2=-a`, and all later canonical
diagonals zero, the exact odd and even moments are

```text
m15 = a*(42287*t^5 - 330144*t^4 + 228921*t^3
         + 556826*t^2 + 306060*t - 531720)/(2-t)^3,

m16 = 3*(12981388*t^3 - 26820320*t^2 - 837195*t + 1351350)/(2-t).
```

Define the degree-12 polynomial

```text
P8(t) = 1204550144*t^12 - 35494536455*t^11 - 2967319034778*t^10
        + 24133342031328*t^9 - 68513207463264*t^8
        + 75535499377824*t^7 - 6513636214656*t^6
        - 32358682547712*t^5 + 576720933888*t^4
        + 8343384129536*t^3 - 662433824768*t^2
        - 28728360960*t + 1651507200.
```

The corrected norm factors are

```text
h7 =  3*P7(t)/((2-t)^3*p5(t)),
h8 = -3*P8(t)/(2*(2-t)^3*P6(t)),
```

and therefore

```text
beta8(t) = h8/h7 = -p5(t)*P8(t)/(2*P6(t)*P7(t)).
```

At `t=0`, these give `h7=5040`, `h8=40320`, and `beta8=8`.  This Gaussian
check rejects the inverted fractions in the raw webpage rendering.

## Exact sign certificate

R59 gives `P6` strictly increasing on the prior interval and
`P6(9/100)>0`, so `tau6<9/100`.  On `0<t<tau6`, `p5>0`, `P7>0`, and
`P6<0`; hence `sign(beta8)=sign(P8)`.

The exact value

```text
P8(0)=1651507200>0,
P8(1/25)=-1513757948352138841097481/59604644775390625<0
```

gives a zero before `1/25`.  The Bernstein coefficients of `P8'` on
`[0,1/25]` are all strictly negative, so `P8` is strictly decreasing there.
The Bernstein coefficients of `P8` on `[1/25,9/100]` are all strictly
negative, so `P8` stays negative throughout the remainder of the possible
`tau6` interval.  Therefore there is a unique

```text
tau8 in (0,1/25),  P8(tau8)=0,
```

and

```text
beta8>0  iff  0<t<tau8,
beta8<0  for tau8<t<tau6.
```

Thus the positive canonical prefix window contracts again at degree 16, but
the corrected cutoff is below `0.04`, not the approximately `0.085` value
from the uncorrected webpage formula.

## Global status

This remains a finite-stage contraction, not a proof that every fixed nonzero
skew parameter eventually exits and not a full-exact non-Gaussian
counterexample.  The sequence of even cutoffs now has the reliable partial
pattern `tau6 > tau8 > 0`, while R60 showed that the intervening odd level
does not contract.  D.1, infinite positive viability, eventual skew
annihilation, Gaussian rigidity, and the `P_3 K` bridge remain distinct open
problems.

The next unique target is the corrected degree-18 `beta9` sign lemma on
`0<t<tau8`.  No determinant, optimizer, SDP, sweep, relaxed measure-LP, or
remote computation was used.
