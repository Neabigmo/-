"""Formal Hermite--Fourier bridge, with its scope explicitly marked."""

from __future__ import annotations

import sympy as sp

try:
    from .common import require, write_json
except ImportError:
    from common import require, write_json

def bridge_data(degree: int) -> dict[str, object]:
    require(degree >= 3 and degree % 2 == 1, "degree must be odd and >=3")
    # Here pbar_d=sum cos(theta+phase)^d is deliberately unscaled.  The
    # geometric factor rho^d is carried once, in the OU expansion below.
    coeffs = [
        {
            "m": m,
            "cos_coefficient": sp.simplify(
                3 * sp.Rational(2 ** (1 - degree))
                * sp.binomial(degree, (degree - m) // 2)
            ),
        }
        for m in range(3, degree + 1, 6)
    ]
    mean_p2 = sp.factor(sp.Rational(1, 2) * sum(item["cos_coefficient"] ** 2 for item in coeffs))
    leading_H = sp.factor(mean_p2 / sp.factorial(degree - 1) ** 2)
    return {
        "d": degree,
        "harmonics": [item["m"] for item in coeffs],
        "mean_unscaled_p_d_squared": mean_p2,
        "leading_H_coefficient": leading_H,
        "formal_expansion": "2*pi*pi_x(theta)=1+rho^d*kappa_d*pbar_d(theta)*H_d(x)/d!+higher order",
        "missing_information_leading": "rho^(2d)*kappa_d^2*mean(pbar_d^2)*H_(d-1)(x)^2/((d-1)!)^2+higher order",
        "scope": "OU-smoothed first-order bridge; not a global rigidity theorem.",
    }

def main() -> None:
    write_json("stage8_bridge.json", {"status": "EXACT_STAGE8_HERMITE_FOURIER_BRIDGE_RECORDED", "cases": [bridge_data(d) for d in (3, 5, 7, 9)]})
    print("EXACT_STAGE8_HERMITE_FOURIER_BRIDGE_RECORDED")

if __name__ == "__main__":
    main()
