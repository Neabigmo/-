# Stage-7 endpoint and Toeplitz symbol

The fixed-band endpoint replay uses the certified asymptotic form

`A_{n-m,j,k}/A_{n,0,0} = (-1/2)^m (1 + O(1/n))`

for fixed `m`.  It is used only at fixed band before taking `m -> infinity`.
The exact candidate symbol is

`D_R(z) = [R(z/2)^2 + R(-z/2)^2]/2`.

The finite replay verifies the fixed-m limit and the Gaussian case.  A full
proof still has to control the order of the limits (`n` first at fixed `m`,
then the uniform tail in `m`) in the actual Stage-7 spaces.

