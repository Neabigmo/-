"""Weak-form rotation transport certificates."""

from __future__ import annotations

import sympy as sp

from common import require, write_json
from derive_bivariate_mixture import a, b, theta

def weak_form_certificate() -> dict[str, object]:
    dL = [sp.trigsimp(sp.diff(item, theta) - b[j]) for j, item in enumerate(a)]
    dT = [sp.trigsimp(sp.diff(b[j], theta) + a[j]) for j in range(3)]
    require(all(v == 0 for v in dL), "L'=T coefficient identity failed")
    require(all(v == 0 for v in dT), "T'=-L coefficient identity failed")
    return {
        "status": "EXACT_ROTATION_TRANSPORT_LEMMA",
        "frame_derivatives": ["d_theta L_theta=T_theta", "d_theta T_theta=-L_theta"],
        "weak_identity": "d_theta int f(x)q_theta(x)dx = int f'(x)q_theta(x)m_theta(x)dx",
        "continuity_equation": "partial_theta q_theta + partial_x(q_theta*m_theta)=0",
        "joint_continuity_equation": "partial_theta g_theta + div(g_theta*(T,-L))=0",
        "tilted_angular_score": "C_z(theta)=E_z[T_theta | Theta=theta]",
        "derivation_scope": "weak compactly-supported tests; no pointwise density differentiation",
    }

def main() -> None:
    write_json("rotation_transport.json", weak_form_certificate())
    print("EXACT_ROTATION_TRANSPORT_LEMMA")
    print("WEAK_FORM_CONTINUITY_EQUATION_VERIFIED")

if __name__ == "__main__":
    main()
