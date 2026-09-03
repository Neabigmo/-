# Common symmetric zero exception

The only exceptional principal-symbol case is a common zero of `Dtilde` and
`Ctilde`.  For `w_0=zeta^2` with `zeta != 0`, the exact identities show this
is equivalent to

```text
R(zeta/2)=R(-zeta/2)=0.
```

This package does not assume that a probability MGF cannot have such complex
zeros, and it does not launch a new zero search.  Any future theorem must
either rule out this symmetric zero pair using an already-certified
probabilistic property or treat it as a separate branch.

