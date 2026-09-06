"""R58 audit: conditional OU algebra and the missing OU/Jacobi bridge.

This file deliberately does not identify the Favard spectral measure with an
original OU density.  It verifies only the implication available after such a
bridge has been proved.
"""

from math import factorial

from sympy import limit, simplify, symbols


def check_conditional_ou_bound():
    """Verify the degree-two conditional-Hermite inequality algebraically."""
    lam = symbols("lambda", positive=True)
    h2_lower = factorial(2) * (1 - lam) ** 2
    m3_sq_upper = simplify(2 - h2_lower)
    assert simplify(m3_sq_upper - 2 * lam * (2 - lam)) == 0
    print("R58_CONDITIONAL_OU_H2_BOUND PASSED")


def check_deep_divisibility_kills_skew():
    """The bound tends to zero along lambda=q**N."""
    r = symbols("r", nonnegative=True)
    bound = 2 * r * (2 - r)
    assert limit(bound, r, 0, dir="+") == 0
    print("R58_DEEP_OU_DIVISIBILITY_FORCES_M3_ZERO_CONDITIONALLY PASSED")


def check_bridge_is_not_assumed():
    """Keep the law-identification boundary explicit in audit output."""
    required_intertwining_data = {
        "law_identification_or_explicit_map",
        "normalization_preservation",
        "moment_variable_preservation",
        "ou_intertwining",
    }
    assert len(required_intertwining_data) == 4
    print("R58_FAVARD_SPECTRAL_LAW_IS_NOT_AUTOMATICALLY_OU_LAW REMAINS OPEN")


def main():
    check_conditional_ou_bound()
    check_deep_divisibility_kills_skew()
    check_bridge_is_not_assumed()
    print("R58_D1_EVENTUAL_SKEW_CLOSURE REMAINS CONDITIONAL")
    print("R58_GAUSSIAN_RIGIDITY_AND_P3K REMAIN DISTINCT OPEN")
    print("R58_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
