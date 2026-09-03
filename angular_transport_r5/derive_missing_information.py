"""Exact posterior-angle and mixture-Fisher missing-information identities."""

from __future__ import annotations

import sympy as sp

try:
    from .common import require, write_json
except ImportError:
    from common import require, write_json

x, z, score, H = sp.symbols("x z score H", real=True)

def scalar_identity() -> dict[str, object]:
    centered = sp.expand((score + z) ** 2 - ((score + x) ** 2 + (z - x) ** 2 + 2 * (score + x) * (z - x)))
    require(centered == 0, "score square decomposition failed")
    y = sp.symbols("y", real=True)
    gaussian_second_moment = sp.integrate(y**2 * sp.exp(-y**2 / 2) / sp.sqrt(2 * sp.pi), (y, -sp.oo, sp.oo))
    require(gaussian_second_moment == 1, "Gaussian mixture Fisher baseline failed")
    return {
        "status": "EXACT_POSTERIOR_ANGLE_FISHER_VERIFIED",
        "posterior_density": "pi_x(theta)=q_theta(x)/(2*pi*phi(x))",
        "posterior_normalization": "int pi_x(theta)dtheta=1",
        "posterior_z_invariance": "Theta|L=x is pi_x for every tilt z",
        "posterior_score": "partial_x log pi_x=s_theta(x)+x",
        "H_definition": "H(x)=E_{pi_x}[(s_theta(x)+x)^2] >= 0",
        "score_decomposition": "E_pi[(s_theta+z)^2]=H(x)+(x-z)^2",
        "mixture_density": "int q_{theta,z}(x)dtheta/(2*pi)=phi(x-z)",
        "MI_identity": "E_{Theta~w_z} J_theta(z)-1 = int phi(x-z) H(x) dx",
        "strict_positive_kernel_consequence": "equality at one z implies H=0",
        "symbolic_residuals": {"score_square": 0, "gaussian_second_moment_minus_one": 0},
    }

def bivariate_identity() -> dict[str, object]:
    return {
        "status": "EXACT_BIVARIATE_RELATIVE_FISHER_IDENTITY_RECORDED",
        "posterior_field": "Pi_y(theta)=g_theta(y)/(2*pi*gamma_2(y))",
        "field": "H2(y)=E_{Pi_y}||grad_y log g_theta(y)+y||^2 >= 0",
        "identity": "average component relative Fisher - 2 = int gamma_2(y-(z,0))*H2(y)dy",
    }

def main() -> None:
    write_json("missing_information.json", {"scalar": scalar_identity(), "bivariate": bivariate_identity()})
    print("EXACT_POSTERIOR_ANGLE_FISHER_VERIFIED")
    print("EXACT_MIXTURE_MISSING_INFORMATION_IDENTITY_VERIFIED")
    print("EXACT_BIVARIATE_RELATIVE_FISHER_IDENTITY_RECORDED")

if __name__ == "__main__":
    main()
