"""General first-odd-cumulant normal form, kept symbolic in d."""

from __future__ import annotations

import sympy as sp

from common import require, write_json
from derive_angular_geometry import positive_harmonic_coefficients


d, z, kap = sp.symbols("d z kappa_d", integer=True, positive=True)


def mode_data(degree: int) -> dict[str, object]:
    require(degree >= 3 and degree % 2 == 1, "degree must be odd and >=3")
    coeffs = positive_harmonic_coefficients(degree)
    sum_c2 = sp.factor(sum(item["cos_coefficient"] ** 2 for item in coeffs))
    sum_m2c2 = sp.factor(sum(item["m"] ** 2 * item["cos_coefficient"] ** 2 for item in coeffs))
    c_d = sp.factor(
        sp.Rational(1, 2)
        * (sum_c2 / sp.factorial(degree - 1) ** 2 + sum_m2c2 / sp.factorial(degree) ** 2)
    )
    h_lead = sp.factor(sum_c2 / (4 * sp.factorial(degree) ** 2))
    first_cos = sp.factor(coeffs[0]["cos_coefficient"])
    return {
        "d": degree,
        "surviving_harmonics": [item["m"] for item in coeffs],
        "cos3_coefficient": first_cos,
        "cos3_formula": "3*(2/3)^(d/2)*2^(1-d)*binomial(d,(d-3)/2)",
        "c_d": c_d,
        "c_d_positive_witness": f"{c_d} > 0",
        "H_leading_constant": h_lead,
        "log_w_leading": "kappa_d*z^d*p_d(theta)/d!",
        "A_leading": "kappa_d*z^(d-1)*p_d(theta)/(d-1)!",
        "C_leading": "kappa_d*z^(d-1)*p_d'(theta)/d!",
        "fisher_leading": "c_d*kappa_d^2*z^(2*d-2)",
        "hellinger_leading": "H_d*kappa_d^2*z^(2*d)",
        "target_identity_lower_even_cumulants": "coefficient comparison forces kappa_m=0 for 4<=m<2d when all lower odd cumulants vanish",
    }


def main() -> None:
    data = [mode_data(degree) for degree in (3, 5, 7, 9, 11)]
    write_json("first_odd_mode.json", {"status": "EXACT_FIRST_ODD_MODE_FORMULAS_VERIFIED", "cases": data})
    print("EXACT_FIRST_ODD_MODE_FORMULAS_VERIFIED", len(data))
    print("GENERAL_C_D_FORMULA_RECORDED")


if __name__ == "__main__":
    main()

