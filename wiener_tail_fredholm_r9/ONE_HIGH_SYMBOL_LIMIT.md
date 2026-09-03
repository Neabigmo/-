# One-high symbol limit

For fixed low pair `m=j+k`, the supplied Stage-7 replay is
`A_{n-m,j,k}/A_{n00} -> (-1/2)^m`. At fixed finite band this yields a finite
convolution candidate; first take `n -> infinity` at fixed `M`, then control
the `m>M` tail. The actual Stage-7 kernel and its uniform tail are not present
in this workspace, so the candidate `D_R(z)=[R(z/2)^2+R(-z/2)^2]/2` is not
declared theorem-level here.

