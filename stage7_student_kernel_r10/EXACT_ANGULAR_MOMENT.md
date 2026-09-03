# Exact angular moments

In the tangent chart used by the endpoint calculation, take
`p_n(t) proportional to (1+t^2)^(-n/2-1)`.  Beta integration gives, for
`s>=0`,

`E_n[T^(2s)] = (1/2)_s / ((n-1)/2)_s`,

and odd moments vanish.  In particular `E_n[T^2]=1/(n-1)`.  The replay
compares this Beta formula with direct symbolic integration for small even
degrees and uses it to evaluate the exact polynomial kernel.

