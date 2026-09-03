# All-degree angular-kernel proof

Put `a_l(theta)=a_* cos(theta+phi_l)`, `a_*=sqrt(2/3)`, and
`phi=(0,2*pi/3,4*pi/3)`.  With `x=exp(i*theta)`,

```text
a_l = a_*/2 * (omega^(l-1) x + omega^(-(l-1)) x^(-1)),
omega^3=1, 1+omega+omega^2=0.
```

For arbitrary nonnegative `i,j,k`, expand the three powers by the binomial
theorem.  The angular integral is the constant Fourier coefficient.  If
`n=i+j+k` is odd, every exponent is odd and the coefficient is zero.  If `n`
is even, the zero exponent condition is `p+q+r=n/2`, giving

```text
A_ijk = a_*^n 2^(-n) sum_{p+q+r=n/2}
        binom(i,p) binom(j,q) binom(k,r)
        omega^((j-2q)+2*(k-2r)).
```

This is an all-degree proof; the degree-8 replay is only a regression check.
The integral also gives `|A_ijk| <= a_*^n` pointwise.  For `n=2m`,
`A_n00=a_*^n binom(2m,m)/4^m`, so the central-binomial lower bound gives a
universal `O(sqrt(n))` ratio bound.  In the dominant case `i=2a`, `m=2b`,
`a>=b`, the exact product

```text
c_i/c_(i+m) = product[t=0..b-1] 2(a+t+1)/(2(a+t)+1)
```

and `log(1+x)<=x` give `c_i/c_(i+m)<=exp(b/(2a+1))<2`.

