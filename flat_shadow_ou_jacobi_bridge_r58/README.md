# R58 — OU/Jacobi bridge boundary

R58 tested the most important logical bridge left after R57: whether the
positive Favard/Hamburger law reconstructed from the ordinary Jacobi moments
is the same law, or a controlled image of the law whose density is the
original positive OU tower.

The webpage round was safely stopped after it distinguished the two objects,
but before it supplied a proof of an operator/measure map.  That distinction
is decisive.  Favard positivity reconstructs a probability measure for an
abstract moment functional in the Jacobi variable `x`; it does not, by itself,
identify that measure with an OU density `g^(j)`, an escort density, or a
fixed-factor OU image.  To transfer `g^(j)=P_q g^(j+1)` one must separately
prove:

```text
law identification or an explicit map,
normalization preservation,
moment/Jacobi-variable preservation,
and intertwining with P_lambda.
```

## Conditional theorem that would close the skew branch

Suppose the missing bridge is established and the R53 law `mu_*` satisfies
`mu_*=P_{q^N} nu_N` for every `N`, with `0<q<1`, while its exact second row
gives `h_2(mu_*)=2-m_3(mu_*)^2`.  The Gaussian conditional-Hermite argument
gives

```text
h_2(mu_*) >= 2*(1-q^N)^2,
m_3(mu_*)^2 <= 2*q^N*(2-q^N).
```

Letting `N` tend to infinity forces `m_3(mu_*)=0`.  This would rule out the
finite-head skew parameter in the R57 canonical family and close
“eventual-zero Jacobi diagonal plus deep positive OU divisibility implies
zero skew”.  It would still be only a conditional closure of D.1: it would
not prove Gaussian rigidity or the `P_3 K` bridge unless those identifications
are also supplied.

## Current boundary and next target

R58 therefore records no unconditional theorem about the original tower.
The exact missing statement is an OU–Favard transfer lemma.  If it cannot be
proved from the existing assumptions, the honest fallback is to continue the
canonical moving-deficit recurrence locally (starting with `beta_6` and
`beta_7`) without treating the auxiliary spectral law as an OU preimage.

No determinant, optimizer, SDP, sweep, relaxed measure-LP, or remote
computation was used.  The local audit only checks the conditional algebra and
the limit implication; it does not claim the missing bridge.

Run:

```text
F:\\anaconda3\\python.exe -u flat_shadow_ou_jacobi_bridge_r58\\audit_r58.py
```
