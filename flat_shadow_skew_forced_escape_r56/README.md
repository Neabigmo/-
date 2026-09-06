# R56 — the factorial-escape gap is explicit, not solved

R56 was sent in the same Project conversation after the R55 local record.  It
asked for a proof or refutation of the following proposed lemma:

```text
full-exact + positive Jacobi chain + alpha_n=0 eventually + m_3 != 0
  ==> finite beta_n <= 0 or factorial-envelope escape.
```

The webpage response did not prove or refute this statement.  Its reliable
contribution is the isolation of the missing implication: full-exactness gives
the moving deficit/norm recurrence, while the R12 class gives an upper growth
bound, but no lower growth or sign mechanism has yet been derived.

## The correction that must govern future work

The statement

```text
limsup (1/n)*log(n!/h_n) = +infinity
```

is not equivalent to failure of

```text
h_n <= C*A^n*n!  for finite C,A.
```

Indeed, `h_n=n!/2^(n^2)` obeys the envelope with `C=A=1`, but the displayed
reversed logarithm tends to `+infinity`.  The correct root-test criterion,
for positive `h_n`, is

```text
there exist finite C,A with h_n <= C*A^n*n!
  <=> limsup (h_n/n!)^(1/n) < infinity.
```

Therefore envelope failure is equivalently

```text
limsup (1/n)*log(h_n/n!) = +infinity,
```

or `liminf (1/n)*log(n!/h_n)=-infinity`.  This is a necessary correction,
not a proof that the exact recurrence forces that growth.

## What remains exact

On the canonical centered tail, with all preceding norms positive,

```text
delta_n = c_n*h_n,       c_n=3*(2/3)^n,
beta_n = (3/2)*delta_n/delta_(n-1).
```

Thus positive `h_n` gives positive moving deficits, and a finite `beta_n<=0`
would be a finite canonical exit.  But this conditional sign identity is
circular as a proof of positivity: it only propagates a candidate chain after
the next norm has already been shown positive.

The finite-head family from R55 remains only a non-full-exact control example.
No full-exact positive non-Gaussian counterexample was produced in R56, and no
unconditional eventual-skew-annihilation theorem was obtained.

## Global status and next target

R56 sharpens, rather than closes, the smallest open bridge:

```text
full-exact recurrence + eventual zero diagonal + m_3 != 0
  --?-->  lower growth beyond C*A^n*n! or a finite positivity failure.
```

If this bridge is proved, it yields eventual-diagonal skew annihilation for
the R12 class and hence D.1 against the R47 bounded-head construction.  It
still does not by itself prove Gaussian rigidity or the `P_3 K` bridge.

The next round should not restate the invalid reversed-log equivalence.  It
should derive a concrete invariant from the all-degree recurrence, or present
a genuine full-exact positive counterexample, or prove a weakest additional
tail-transfer condition and test whether backward-OU positivity supplies it.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_skew_forced_escape_r56\audit_r56.py
```

The audit checks the two growth counterexamples and the canonical deficit
constants, while explicitly preserving the open-problem boundary.
