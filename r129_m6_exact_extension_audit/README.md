# R129 — M=6 exact row and exclusion of the R128 ghost

日期：2026-09-08  
状态：`PROVED` / `ANALYTICALLY PROVED` for the exact R6 elimination and for
the non-extendability of the specific R128 relaxed endpoint.  A global value
of `GammaHat_6`, the genuine `Gamma_6`, and the all-order decay remain `OPEN`.

## 1. Scope and normalization

All calculations use the project normalization

`Q=((X_1-X_2)^2+(X_1-X_3)^2+(X_2-X_3)^2)/3`

with independent centered variance-one copies.  Hence the Gaussian reference
row is `E Q^r=2^r r!`.  `H_M>=0` is treated only as a relaxed truncated
Hamburger condition; it is not silently upgraded to a representing measure.

The script `audit_r129.py` expands `Q^6` exactly with SymPy, substitutes the
already audited R2--R5 rows, derives the M=5 to M=6 range conditions, and
isolates the R127 root.  It does not scan or optimize.

## 2. Exact R6 elimination

Let

`c=y_3`, `a=y_5`, `b=y_7`, and `d=y_9`.

The exact expansion of `Q^6`, followed by the exact rows R2--R5, gives the
following affine top-moment equation:

`y_12 = -7749 y_3^4 - 16380 y_3^2 + 14220 y_3 y_5
         - 2160 y_3 y_7 + 100 y_3 y_9 - 1926 y_5^2
         + 252 y_5 y_7 + 10395.`

Equivalently,

`y_12 = -1926 a^2 + 252ab + 14220ac - 2160bc
         - 7749c^4 - 16380c^2 + 100cd + 10395.`

There is no `y_11` term, as required by the centered triangular structure.
The Gaussian substitution gives `y_12=10395` and `E Q^6=46080`, so the
normalization check is internal to the exact symbolic audit.

## 3. The M=5 endpoint in block form

Use

`A=H_2=[[1,0,1],[0,1,c],[1,c,3]]`,

and define the three old columns

`u_3=(c,3,a)^T`, `u_4=(3,a,y_6)^T`, `u_5=(a,y_6,b)^T`,

where

`y_6=15+7c^2`, `y_8=105-124c^2+32ca`,

and `y_9=d`, `y_10=3(17a^2-280ac+20bc+470c^2+315)`.

At the R127 endpoint write

`a=4c+s`, `s^2=6(2-c^2)(1+c^2)`,

and let

`B(c,s)=-5c^4+6c^3s+68c^2-24cs-8`.

The isolated endpoint satisfies `B=0` and

`P(c^2)=0`,

where

`P(u)=216u^5-1919u^4+4072u^3+4704u^2-8000u+64`.

The R128 construction chooses `d` from the H4 kernel compatibility.  Its
Schur complement relative to `A` is

`S_5=diag(0,0,delta_5)`,

with

`delta_5=-18 C(c,s)/(c^2-2)^2 > 0`,

and the R128 interval certificate proves the strict sign.  Thus the endpoint
is a rank-four singular non-flat relaxed truncation, not a representing law.

## 4. New H5 to H6 compatibility

The new H6 column, split relative to `A`, is

`u=(y_6,b,y_8)^T`, `v=(d,y_10,y_11)^T`.

The Schur complement of H6 relative to `A` has the block form

`S_6=[[S_5,r],[r^T,sigma_6]]`,

where

`r=v-[u_3 u_4 u_5]^T A^{-1}u`.

Because the first two diagonal entries of `S_5` are zero, positivity of H6
would force the two kernel compatibilities

`r_0=0` and `r_1=0`.

The exact symbolic audit gives, before imposing the endpoint equation,

`r_0=-3(36c^7-180c^5+5c^4s+72c^3-68c^2s+288c+8s)/(c^2-2)^2`,

`r_1=-3(144c^8-549c^6+115c^5s-198c^4-304c^3s
       +2016c^2+40cs-1152)/(c^2-2)^2`,

while `r_2` contains the only new odd variable `y_11`.  Thus `y_11` cannot
repair the first two conditions.

To state the endpoint reduction exactly, solve `B=0` for

`s=(5c^4-68c^2+8)/(6c^3-24c)`.

The audit proves the identities

`r_0=-P(c^2)/(2c(c^2-4)(c^2-2)^2)`,

`r_1-delta_5=P(c^2)/(2(c^2-4)(c^2-2)^2)`.

At the R127 endpoint `P(c^2)=0`, so

`r_0=0`, `r_1=delta_5>0`.

The second quantity is the first previously undetected recurrence defect.  It
is exactly the positive R128 non-flat Schur defect, not a numerical accident.
Consequently the zero row of `S_5` is coupled to the new column by a nonzero
entry.  Therefore no value of `sigma_6`, including the value forced by the
exact R6 row, can make `S_6` positive semidefinite.

## 5. R129 theorem and its limits

**ANALYTICALLY PROVED — endpoint no-go.** The specific R128 endpoint that
realizes `GammaHat_5=GammaHat_4=c_4` has no PSD H6 extension satisfying the
exact rows.  The obstruction is the exact identity `r_1=delta_5>0`.

**PROVED — exact algebra.** R6 reduces to the displayed `y_12` formula;
the M5-to-M6 range conditions and the Schur block are exact linear algebra.

**OBSTRUCTION.** The R128 ghost cannot be carried unchanged through the next
Hankel level.  The free odd moment `y_11` appears only in `r_2`, after the
failure has already occurred.

This does **not** yet prove a global strict inequality
`GammaHat_6<GammaHat_5`: another sequence of M6 feasible points could in
principle approach the M5 endpoint without attaining it.  Nor does it compute
the genuine radius `Gamma_6`.

## 6. General extension mechanism

Let `H_m>=0` be a truncated Hankel matrix and `K_m=ker(H_m)`.  Any extension
to `H_{m+1}` must satisfy

`p^T(y_{m+1},...,y_{2m+1})=0` for every `p in K_m`,

and then has one scalar generalized Schur defect.  If a flat extremizer at
level m satisfies these conditions but the next exact row makes that defect
strictly positive, the extension is a singular non-flat ghost.  The next
level tests the old kernel again through the new range conditions; any
nonzero component in a zero row of the old Schur complement kills the PSD
extension independently of the new top odd moment.

This is a general **linear-algebra lemma**, but it is not a theorem that the
defect must alternate at every level.  The required new freedoms are the
unfixed odd moments in the incoming column and the final Schur scalar.  If the
number of independent compatibility equations exceeds the available odd
freedoms, a no-go like R129 is forced; if not, the extension may survive.  A
universal alternation theorem therefore remains `OPEN`.

## 7. Relation to the main problem

Relaxed feasible sets project downward, so `GammaHat_M` is non-increasing;
the equality through R128 is a finite relaxed statement.  Genuine positivity
is stronger, and backward-OU divisibility is stronger still.  The R129 no-go
removes one relaxed endpoint but does not by itself supply the uniform
coercivity needed for `Gamma_M -> 0`.  The all-order compactness argument from
R125 still says that a fixed nonzero full-order cubic cannot remain merely a
formal ghost forever, but it does not specify the finite-level rate.

## 8. Next task: R130

1. Audit the exact R6 expression against the webpage derivation and add the
   raw expansion marker if the two forms agree.
2. Determine whether the R129 endpoint no-go can be upgraded to a local
   uniform gap near `c_4`, rather than only excluding the endpoint.
3. Track the compatibility-defect cascade in a basis adapted to the kernel,
   separating old-kernel defects from the genuinely new `y_11` direction.
4. Return to the positive/backward-OU cone and test whether an all-order
   weighted recurrence estimate can force `c -> 0`.

Audit command:

`F:\\anaconda3\\python.exe r129_m6_exact_extension_audit\\audit_r129.py`

Expected final marker: `R129_M6_EXACT_EXTENSION_AUDIT_COMPLETED`.
