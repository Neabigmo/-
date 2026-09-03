# R14 — symmetric-zero Fock factor audit

This is a theory-only audit of the last exceptional mechanism left by R13:

```text
R(a) = R(-a) = 0,  a != 0.
```

The purpose is to determine whether the exact Fock/angular identities add a
genuine probability restriction at such a symmetric complex zero.  It does
not run a zero search, optimization, determinant calculation, or remote
campaign.

The audit records the normalized Fock factor identity, OU zero scaling,
elementary three-root symmetric identities, and explicit symmetric probability
countermodels.  The notation is separate: `M(z)=E exp(zX)` is the MGF and
`R(z)=exp(-z^2/2) M(z)` is the Fock profile.  The countermodels show that being
an MGF, being symmetric, or having OU scaling does not by itself exclude the
exceptional pair.

Decision `FOCK_ZERO_RESONANCE_LEMMA_CERTIFIED_PROBABILITY_BRIDGE_REMAINS`
means the resonance algebra is consistent and the missing probability bridge
is explicit.  It is not Gaussian rigidity.
