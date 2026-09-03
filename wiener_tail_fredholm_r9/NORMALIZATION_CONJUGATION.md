# Factorial conjugation

Write the ordinary Taylor series and Hermite-normalized series as
`R(z)=sum_n r_n z^n = sum_n b_n z^n/sqrt(n!)`.
Thus `r_n=b_n/sqrt(n!)`. Any recurrence written in `b_n` carries the factor
`sqrt(n!/(n-m)!)` in ordinary coefficients, so a constant-coefficient symbol
in the `b` normalization is not automatically a literal Wiener multiplier.
R9 records `B_NORMALIZATION_NOT_TOEPLITZ` until the actual Stage-7 conjugated
kernel is derived.

