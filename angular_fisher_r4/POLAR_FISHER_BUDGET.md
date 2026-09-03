# Polar Fisher budget

记 `v=K''`、`A_z=partial_z log w_z`、`C_z=z^{-1} partial_theta log w_z`。精确得到：

`E_z[A_z]=0`；

`E_z[A_z^2+sum a_j^2 v(z a_j)]=1`；

`E_z[C_z^2+sum b_j^2 v(z a_j)]=1`；

相加并使用 `sum(a_j^2+b_j^2)=2`，得到 polar Fisher budget 等于 2。

此外 `g=sqrt(w)` 的周期是 `2*pi/3`，所以

`H=1-(average g)^2 <= z^2 E_z[C_z^2]/36`。

这组结果本身没有强迫 `E_z[C_z^2]=0`。

