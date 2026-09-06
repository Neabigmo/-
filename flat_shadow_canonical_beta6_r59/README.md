# R59 — canonical beta6 contraction and the OU/Jacobi bridge boundary

R59 made two useful decisions in the same Project conversation.

First, it selected the negative bridge result: the R53 Favard/Hamburger law
is an auxiliary spectral measure for the Jacobi moment functional.  Positivity
of that functional does not identify it with the original OU density law or
with its cubic escort.  An OU transfer needs law identification (or an
explicit map), normalization and moment preservation, and intertwining with
the OU operator.  The conditional consequence remains valid: if
`mu_*=P_(q^N) nu_N` for every `N`, then

```text
h_2(mu_*) >= 2*(1-q^N)^2,
m_3(mu_*)^2 <= 2*q^N*(2-q^N),
```

so `m_3(mu_*)=0` as `N -> infinity`.

Second, R59 continued the one-parameter canonical family with `a=m_3`,
`t=a^2`, `alpha_1=a`, `alpha_2=-a`, and `alpha_n=0` for `n>=3`.
Set

```text
p4(t) = t^2 - 64*t + 16,
p5(t) = 253*t^3 - 1278*t^2 + 816*t + 160,
P6(t) = 532*t^6 - 45655*t^5 + 351508*t^4
        - 625952*t^3 + 110432*t^2 + 83200*t - 7680.
```

The new exact moments and locally corrected norms are

```text
m11 = a*(140*t^2 - 913*t - 30)/(2-t),
m12 = (2849*t^3 - 19102*t^2 - 15987*t + 20790)/(2-t),
h5  = 3*p5(t)/(2*(2-t)*(1+t)),
h6  = -6*P6(t)/((2-t)^2*p4(t)).
```

With the project convention `beta_n=h_n/h_(n-1)`, the corrected new formula is

```text
beta6(t) = -4*(1+t)*P6(t)/((2-t)*p4(t)*p5(t)).
```

The browser response displayed the reciprocal orientation for the `delta`
and `beta6` fractions; this README and the audit use the locally recomputed
`h6/h5` orientation.  The sign conclusion is unchanged.  On

```text
0 < t < r,  r=32-12*sqrt(7),
```

`p4,p5,2-t` are positive.  Moreover `P6` is strictly increasing there,
`P6(1/20)<0`, and `P6(1/10)>0`.  Hence there is a unique

```text
tau6 in (1/20,1/10),  P6(tau6)=0,
```

and the nonzero-skew canonical prefix satisfies

```text
beta2,...,beta6 > 0  iff  0 < t < tau6.
```

Thus the viable interval contracts strictly at the sixth Jacobi level.  This
is a genuine finite-stage theorem, not a full-exact counterexample: the
signs of `beta7,beta8,...` remain unknown.

## Global meaning

The bridge failure prevents using `q^N -> 0` to settle the auxiliary `mu_*`
without an additional transfer hypothesis.  The beta6 contraction is
unconditional within the audited canonical moment recurrence and does not
swap the OU and Jacobi laws.  It is a compact, reportable intermediate result:
the first five-level nonzero-skew window is reduced to an explicitly isolated
root interval at level six.

The next unique lemma is the `beta7` positivity-interval contraction on
`0<t<tau6`: either find a root `tau7<tau6`, or prove `beta7>0` throughout
that interval.  No broad numerical scan is needed.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation was used.
