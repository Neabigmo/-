# Positive angular mixture

令 `a_j(theta)=sqrt(2/3) cos(theta+2*pi*(j-1)/3)`，`L_theta=sum_j a_j(theta) X_j`，`K=log M`。

目标恒等式给出

`average_theta exp(sum_j K(z a_j)-z^2/2)=1`。

因此 `w_z(theta)=exp(sum_j K(z a_j)-z^2/2)` 是严格正的后验混合密度，并且平均值为 1。脚本逐项核验 `sum a=sum b=0`、`sum a^2=sum b^2=1`、`sum ab=0`、`a_j^2+b_j^2=2/3`。

