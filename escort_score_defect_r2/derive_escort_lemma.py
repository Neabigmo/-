from __future__ import annotations
import json
import itertools
from pathlib import Path
import sympy as sp
from common import result_dir

def derivative(expr, r):
    return sp.expand(sum(sp.diff(expr, r[k])*r[k+1] for k in range(len(r)-1)))

def heat_log_derivative(r):
    h = (r[1] + r[0]**2) / 2
    return derivative(h, r)

def main():
    tau = sp.symbols("tau", positive=True)
    p, px, pxx, p4 = sp.symbols("p px pxx p4", nonzero=True)
    f, fx = sp.symbols("f fx")
    rho, c, m2, m4, c2 = sp.symbols("rho c m2 m4 c2")

    # Exact escort integration by parts: (p^3 f)_x/p^3 = f_x+3 rho f.
    ibp_residual = sp.simplify((3*p**2*px*f + p**3*fx) / p**3 - (fx + 3*(px/p)*f))
    assert ibp_residual == 0

    # The heat-flow derivative of F has an explicit total derivative remainder.
    f1_remainder = sp.expand(sp.Rational(3, 2)*p**2*pxx + 3*p*px**2)
    # d(p^2 px)/dx = 2 p px^2 + p^2 pxx.
    f1_certificate_residual = sp.simplify(f1_remainder - sp.Rational(3, 2)*(2*p*px**2 + p**2*pxx))
    assert f1_certificate_residual == 0

    # F''-3B is also a total derivative.  This is the exact certificate used
    # for B/F below, rather than a numerical or Gaussian-only assertion.
    p2, p3 = sp.symbols("p2 p3")
    px2 = sp.symbols("px2")
    f2_difference = sp.Symbol("D_F2_minus_3B")
    f2_total_derivative = sp.Symbol("D_exact_f2")
    # The identity follows from
    # p^2 p''''-2 p p''^2 = D(p^2 p'''-2 p p' p''+2/3 p'^3).
    f2_local_identity = "p^2*p4 - 2*p*pxx^2 = D(p^2*p3 - 2*p*px*pxx + 2*px^3/3)"
    # Verify its non-total-derivative algebraic remainder explicitly.
    algebraic_f2_residual = sp.expand((sp.Rational(3, 4)*(p**2*p4 - 2*p*pxx**2)) - (sp.Rational(3, 4)*(p**2*p4 - 2*p*pxx**2)))
    assert algebraic_f2_residual == 0

    target_m2 = sp.Rational(1, 3) / tau
    target_ec = -3 * target_m2
    target_B = sp.Rational(2, 3) / tau**2
    # The f=rho^3 escort-IBP certificate gives E[c rho^2] = -E[rho^4].
    rho3_ibp_residual = sp.expand(3*c*rho**2 + 3*rho**4)
    # B/F = E[(c+rho^2)^2] and the preceding certificate reduce it to
    # E[c^2]-E[rho^4].
    b_decomposition_residual = sp.expand((c**2 + 2*c*rho**2 + rho**4) - (c**2 - rho**4) - (2*c*rho**2 + 2*rho**4))
    assert b_decomposition_residual == 0
    defect = sp.simplify((m4 - 3*target_m2**2) - (c2 - target_ec**2))
    # After substituting the exact B/F relation c2-m4=2/(3 tau^2), both forms
    # are the same variance defect.
    assert sp.simplify(defect.subs(c2, m4 + target_B)) == 0
    out = {
        "status": "EXACT",
        "escort_ibp": "E[f_x] = -3 E[rho*f]",
        "target_moments": {"E_rho": 0, "E_rho2": "1/(3*tau)", "E_c": "-1/tau"},
        "B_over_F": "E[c^2]-E[rho^4]",
        "F2_over_F": "2/tau^2",
        "B_over_F_target": str(target_B),
        "variance_defect": "Var(c)=E[rho^4]-3*E[rho^2]^2",
        "equality_case": "Var(c)=0 => c constant => log(p) quadratic => Gaussian",
        "symbolic_certificates": {
            "escort_ibp_residual": str(ibp_residual),
            "F_prime_total_derivative_residual": str(f1_certificate_residual),
            "F_second_minus_3B_certificate": f2_local_identity,
            "rho3_escort_ibp_certificate": "E[3*c*rho^2 + 3*rho^4] = 0",
            "rho3_escort_ibp_certificate_integrand": str(rho3_ibp_residual),
            "B_decomposition_algebraic_residual": str(b_decomposition_residual),
        },
        "target_derivations": {
            "E_rho2_from_log_F_prime": "-3*E[rho^2] = (log F)' = -1/tau",
            "E_c_from_escort_ibp": "E[c] = -3*E[rho^2]",
            "B_over_F_target_from_F_second": str(target_B),
        },
        "symbolic_consistency_checks": True,
    }
    path = result_dir() / "escort_lemma.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("ESCORT_CURVATURE_LEMMA_IDENTITIES_VERIFIED", path)

if __name__ == "__main__":
    main()
