# R10 correction: Student/Beta angular moment

For the endpoint density proportional to `(1+t^2)^(-n/2-1)`, odd moments
vanish and, for `s >= 0`,

```text
E_n[T^(2s)] = (1/2)_s / (((n+1)/2)-s)_s
            = (2s-1)!! / ((n-1)(n-3)...(n-(2s-1))).
```

The shorthand `(1/2)_s / ((n-1)/2)_s` in the R10 note was wrong.  The
denominator is a falling-start rising factorial beginning at
`(n+1)/2-s`, equivalently the displayed odd descending product.

This file is an audit correction, not a change to the old R10 branch.

