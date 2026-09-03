# Generic probability countermodels

Two exact symmetric probability laws already have nonzero symmetric complex
zeros.  For the Fock profile `R(z)=exp(-z^2/2)M(z)`, the zeros are unchanged.

1. For `X=pm1` with equal probabilities,

```text
M(t) = cosh(t),
R(t) = exp(-t^2/2) cosh(t),
R(i*pi/2) = R(-i*pi/2) = 0.
```

2. For `P(X=0)=3/4` and `P(X=pm2)=1/8`,

```text
M(t) = 3/4 + 1/4 cosh(2t),
R(t) = exp(-t^2/2) M(t),
a = (arcosh(3)+i*pi)/2,
M(a) = M(-a) = 0,  Re(a) != 0,  Im(a) != 0.
```

Both laws have mean zero and variance one.  Therefore positivity of a
probability law, symmetry, and the MGF/Laplace-transform representation alone
cannot exclude a symmetric nonzero complex pair.

These are exact countermodels to a generic probability shortcut; they are
not countermodels to the full three-variable Fock identity.
