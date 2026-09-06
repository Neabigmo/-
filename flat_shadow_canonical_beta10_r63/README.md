# R63 — corrected degree-20 beta10 cutoff

R63 continues the audited canonical family from R62:

`a=m3`, `t=a^2`, `alpha1=a`, `alpha2=-a`, and `alpha_n=0` for `n>=3`.
The project convention is `beta_n=h_n/h_(n-1)`.  This is a finite-stage
statement only; it does not claim full positive viability or eventual skew
annihilation.

## Exact degree-20 rows

The condition `alpha9=0` gives

`m19 = 9a(55917589t^5-184963800t^4+55863471t^3+
             179281750t^2+11558100t-16463160)/(2-t)^3`.

Solving the degree-20 same-factor cubic row exactly for `m20` gives

`m20 = (-14571660838t^6+520027461774t^5-2971081076052t^4+
        6147868133237t^3-4337195160894t^2-8050748580t+
        5237832600)/(2-t)^3`.

This corrected `m20` is not the earlier exploratory truncated-series
expression.  The degree-20 row, the `alpha9=0` row, and the two moment values
are checked at `a=0,1/10,1/5` in `audit_r63.py`.

## Norm and beta10 factorization

Let `A10(t)` be the exact degree-20 polynomial

```text
19303333145383948416*t^20 + 9336515373991298872176*t^19
-208910696107696157240862*t^18 + 3132795951208162147007532*t^17
-31492383709438391894349288*t^16 + 202691932739973707278377072*t^15
-850332482279550438115981632*t^14 + 2370928857213057939311326080*t^13
-4378011401838561085608139008*t^12 + 5108605701650258496327470592*t^11
-3186879624701649350014623744*t^10 + 220941067309393252490711040*t^9
+897845469914321138096431104*t^8 -189117621665056236409847808*t^7
-303516089233560672506216448*t^6 +143112944494845026862366720*t^5
-8606305579913051916730368*t^4 -480320001616558833008640*t^3
+24287603537972979302400*t^2 +4429713304977408000*t
-191775658475520000.
```

The exact norm recurrence gives

`h10 = A10(t)/((t-2)^5 P8(t))`,

and therefore, using the audited R62 expression for `h9`,

`beta10 = h10/h9 = A10(t) P7(t)/(3(t-2)P8(t)Q9(t))`.

At the Gaussian point,

`m20(0)=19!!`, `h10(0)=10!`, and `beta10(0)=10`.

The first-order local expansion is

`beta10(t)=10-(1481/21)t+O(t^2)`.

## Exact cutoff certificate

The Bernstein certificates in `audit_r63.py` establish:

- `A10'(t)>0` on `[0,1/200]`;
- `A10(0)<0<A10(1/200)`;
- `A10(t)>0` on `[1/200,19/500]`, using five exact rational interval
  Bernstein certificates;
- `(t-2)^5 P8(t)<0` on `[0,19/500]`.

Thus there is a unique

`tau10 in (0,1/200)` with `A10(tau10)=0`.

R62 gives `tau9 in (1/100,19/500)` and `Q9>0` on `(0,tau9)`.  Since
`P7>0` and `P8>0` on that prior window, the factorization above yields the
strict sign result

`beta10(t)>0` iff `0<t<tau10`,

`beta10(t)<0` for `tau10<t<tau9`.

Consequently the canonical positive prefix contracts once more:

`tau6 > tau8 > tau9 > tau10 > 0`,

with the new exact localization `tau10<1/200<1/100<tau9`.  No floating-point
root is used in the statement.

## Scope and next structural question

R63 is a stronger finite-stage contraction result, not a proof of D.1,
eventual skew annihilation, Gaussian rigidity, or the `P_3 K` bridge.  It also
shows that the cutoff sequence cannot be dismissed as an even/odd artifact:
the tenth coefficient creates a further cutoff after the ninth.

The next useful target is now a structural all-even-stage lemma or a uniform
tail mechanism explaining why these exact cutoffs decrease.  Another large
unverified coefficient expansion should not be treated as progress by itself.

Audit command:

`python flat_shadow_canonical_beta10_r63/audit_r63.py`

The audit uses exact symbolic/rational arithmetic and Bernstein certificates;
it does not use determinant, optimizer, SDP, sweep, relaxed measure-LP, or
remote computation.
