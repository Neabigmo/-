# R13-finalize decision

`EXACT_DEFECT_SURJECTIVITY_AWAY_FROM_COMMON_ZEROS_CERTIFIED`

The compact lower-triangular column lemma supplies the relative dual-tail
estimate that R13 previously lacked.  The documented R11 operator theorem
provides compactness, and its coefficient index relation `n=i+j+k >= i`
provides lower-triangular support.  The dual annihilator, tail normalization,
simultaneous recurrence, and shift-spectral common-root steps are therefore
certified under those audited hypotheses.

The exact conclusion is conditional in the mathematically explicit sense:
failure of `Delta_rho` surjectivity forces a nonzero common interior zero of
`D_R` and `C_R`, equivalently a symmetric nonzero pair `R(a)=R(-a)=0`.
This package does not claim that such a pair is impossible for a genuine
probability/Fock solution, and it does not claim Gaussian rigidity.

No numerical determinant search, numerical zero search, optimization, remote
computation, or automatic R14 is used.
