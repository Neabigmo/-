# First odd coordinates

The first four Laguerre coordinates are the exact quantities checked by the replay:

```text
c1 = -mu3/3
c2 = (mu5 - 10*mu3)/18
c3 = -(mu7 - 21*mu5 + 105*mu3)/162
c4 = (mu9 - 36*mu7 + 378*mu5 - 1260*mu3 - 100*mu3^3)/1944
```

Thus `m(T)=0` forces the displayed odd combinations to vanish.  Together with the general
triangular relation below, vanishing of all Laguerre coefficients forces all odd moments to
vanish recursively (subject to the square-integrability/moment-growth hypotheses already used
by the project).

