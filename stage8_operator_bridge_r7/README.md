# Stage 8 operator bridge — R7

This package replaces the invalid R6 pointwise sign-transfer target with the
exact operator interface that the available structure actually supplies.
It replays:

- Hermite addition and the number-projected coherent-state identity;
- positivity of the Hermite Gram operator and its sharp automatic
  Cauchy–Schwarz bound for the Stage-8 mixed matrix element;
- the algebraic log-derivative identity used by the global R5
  posterior-angle/Hermite bridge (the analytic/probabilistic inputs are
  recorded as assumptions, not claimed as proved by this replay);
- a finite exact PSD countermodel showing that positivity alone does not
  determine the sign of an off-diagonal matrix element.

The result is deliberately not a counterexample to the original theorem: the
finite model does not satisfy the Fock equations.  It only invalidates the
implication “PSD alone implies the Stage-8 pointwise parity sign”.

Run from this directory:

```text
python exact_replay.py
python -m pytest -q
```
