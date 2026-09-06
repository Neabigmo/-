# R60 — beta7 stays positive on the beta6 window

R60 continued the canonical one-parameter family from R59:
`a=m_3`, `t=a^2`, `alpha_1=a`, `alpha_2=-a`, and
`alpha_n=0` for `n>=3`.  The sixth-level polynomial `P6` from R59 has its
unique root `tau6` in `(1/20,1/10)`, and the current candidate interval is
`0<t<tau6`.

## Correct degree-14 formulas

The new canonical odd and even moments are

```text
m13 = 3*a*(1145*t^2 - 2284*t - 2280)/(2-t),
m14 = (839909*t^3 - 1338415*t^2 - 187437*t + 270270)/(2-t).
```

Define

```text
p4(t) = t^2 - 64*t + 16,
p5(t) = 253*t^3 - 1278*t^2 + 816*t + 160,

P7(t) = 2150400 + 19281920*t - 206264064*t^2
        - 424134656*t^3 + 2523473440*t^4 - 4074599496*t^5
        + 2790646820*t^6 - 853051174*t^7 + 100963863*t^8
        - 2264192*t^9.
```

The locally recomputed norms are

```text
h6 = -6*P6(t)/((2-t)^2*p4(t)),
h7 =  3*P7(t)/((2-t)^3*p5(t)).
```

Therefore the project convention gives

```text
beta7(t)=h7/h6
         = -p4(t)*P7(t)/(2*(2-t)*p5(t)*P6(t)).
```

At `t=0`, this gives `h6=720`, `h7=5040`, and `beta7=7`, which is the
Gaussian sanity check.

The webpage response again displayed inverted norm fractions and a different
degree-14 polynomial.  The audit derives `m14` from the degree-14 same-factor
relation and computes `h7/h6` directly; the formulas above are the submitted
ones.

## Positivity conclusion

On `0<t<tau6`, R59 gives `p4>0`, `p5>0`, `2-t>0`, and `P6<0`.  To prove
`P7>0` without a sweep, express `P7( u/10 )` in the degree-nine Bernstein
basis on `0<=u<=1`.  Its exact Bernstein coefficients are

```text
2150400,
21281792/9,
567358096/225,
2289170384/875,
20832577373/7875,
4107379856063/1575000,
3505008609783/1400000,
420067934127913/180000000,
1890279866402383/900000000,
903062201058519/500000000.
```

They are all positive, so `P7(t)>0` for `0<=t<=1/10`, in particular on
`(0,tau6)`.  Hence

```text
beta7(t)>0  for every 0<t<tau6.
```

The seventh level therefore does not produce a new cutoff: there is no
`tau7<tau6` from this level.  This is a useful alternating obstruction to any
claim that every degree must contract the interval.

## Global meaning and next step

The unconditional finite-stage status is now `beta2,...,beta7>0` on
`0<t<tau6`, but no conclusion is available for all future `beta_n`.  Thus this
is not a full-exact non-Gaussian counterexample and D.1 remains open.  The
OU–Favard transfer is still a separate missing hypothesis; Gaussian rigidity
and the `P_3 K` bridge remain separate.

The next unique local lemma is the corrected degree-16 `beta8` sign lemma on
`0<t<tau6`: compute `m15`, `m16`, and `beta8=h8/h7`, then determine whether a
new cutoff appears.  No determinant, optimizer, SDP, sweep, relaxed
measure-LP, or remote computation was used.
