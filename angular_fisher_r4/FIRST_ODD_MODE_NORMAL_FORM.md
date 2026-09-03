# First odd mode normal form

若首个非零 odd cumulant 为 `kappa_d`、`d>=3` odd，并结合目标 angular identity 排除低阶偶 cumulant 的独立贡献，则

`p_d=sum_j a_j^d`

只含 `3,9,15,... <= d` 的 cosine 谐波。`cos(3 theta)` 系数严格为

`3*(2/3)^(d/2)*2^(1-d)*binomial(d,(d-3)/2)`。

`log w = kappa_d z^d p_d/d! + ...`，
`A = kappa_d z^(d-1) p_d/(d-1)! + ...`，
`C = kappa_d z^(d-1) p'_d/d! + ...`。

因此

`E_z[A^2+C^2] = c_d*kappa_d^2*z^(2d-2)+...`

其中实现中的 `c_d` 是所有 surviving harmonics 的有限正和，而非只取 cos3 项。

