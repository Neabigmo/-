# R47 — N=6 constraint-coupling exact audit

This audit checks the finite exact algebra behind the webpage R47 result.  It
does not claim that a finite positive prefix extends to a genuine all-degree
positive same-factor law, and it does not use optimizer, SDP, sweep,
relaxed-measure LP, or remote computation.

## Audited identities

For the rank-two flat shadow, write `U^2=tU+1`, with `EU=0`, `EU^2=1`, and
`t^2=2`.  The script checks the resulting two-atom moment recurrence and the
Hermite heads through degree 12.

It then independently reconstructs the angular same-factor cubic coefficients
and verifies

```text
b6 = 7*sqrt(5)/10 * b3^2
b10 = sqrt(30)*b3*b7 + 17*sqrt(7)/14 * b5^2
b12 = 10*sqrt(55)/11*b3*b9
       + 21*sqrt(22)/11*b5*b7
       - 369*sqrt(231)/440*b3^4
```

Substituting the rank-two shadow heads gives the exact mismatch identities

```text
b5*Delta7 = b5/(sqrt(30)*b3) * Delta10
             + 13*sqrt(42)/35 * Delta6^2

b3*Delta9 = sqrt(55)/50 * Delta12
             - 7*sqrt(3)/50 * (b5/b3) * Delta10
             - 1073*sqrt(105)/31500 * Delta6^2.
```

The Jacobian of `(Delta10,Delta12)` with respect to the free even-adjustment
coordinates `(b7,b9)` is

```text
10*sqrt(1650)/11 * b3^2,
```

which is nonzero on the rank-two shadow branch.  Thus finite same-factor
Fock/Hermite algebra does not collapse the two response coordinates to one;
it only changes coordinates between odd mismatch products and even mismatch
coordinates plus the fixed `Delta6^2` term.

## Output

```text
R47_SHADOW_TWO_ATOM_RECURRENCE PASSED
R47_DEGREE10_FOCK_IDENTITY PASSED
R47_DEGREE12_FOCK_IDENTITY PASSED
R47_MISMATCH_COORDINATE_IDENTITIES PASSED
R47_LOCAL_JACOBIAN_RANK2 PASSED
R47_ALL_DEGREE_POSITIVE_INTEGRATION REMAINS OPEN
R47_AUDIT_COMPLETED
```

The remaining issue is global: whether these finite-prefix directions can be
integrated simultaneously into genuine all-degree positive full-exact laws
with the required backward-tower and weighted-tail properties.

Run:

```text
F:\anaconda3\python.exe -u flat_shadow_constraint_coupling_r47\audit_r47.py
```
