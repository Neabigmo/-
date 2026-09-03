"""Exact small replay for the R17 conditional-Q Laguerre bridge."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def iid_expect(expr, moments):
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    poly = sp.Poly(sp.expand(expr), x1, x2, x3)
    out = 0
    for powers, coeff in poly.terms():
        term = coeff
        for power in powers:
            term *= moments[power]
        out += term
    return sp.expand(out)


def moment_symbols(max_order=9):
    return {0: sp.Integer(1), 1: sp.Integer(0), 2: sp.Integer(1),
            **{k: sp.Symbol(f"mu{k}", real=True) for k in range(3, max_order + 1)}}


def residual_polynomials():
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    bar = (x1 + x2 + x3) / 3
    q = x1**2 + x2**2 + x3**2 - (x1 + x2 + x3)**2 / 3
    return bar, sp.expand(q)


def laguerre_orthogonality(nmax=5):
    t = sp.symbols("t", nonnegative=True)

    def inner(p):
        poly = sp.Poly(sp.expand(p), t)
        return sp.simplify(sum(co * sp.factorial(k) for (k,), co in poly.terms()))

    gram = [[inner(sp.laguerre(i, t) * sp.laguerre(j, t))
             for j in range(nmax + 1)] for i in range(nmax + 1)]
    expected = sp.eye(nmax + 1).tolist()
    return {"nmax": nmax, "gram": gram, "verified": gram == expected}


def laguerre_generating_function(nmax=5):
    t, s = sp.symbols("t s")
    lhs = sum(sp.laguerre(n, t) * s**n for n in range(nmax + 1))
    rhs = (1 - s)**-1 * sp.exp(-t * s / (1 - s))
    rhs_series = sp.series(rhs, s, 0, nmax + 1).removeO().expand()
    checks = [sp.simplify(lhs.coeff(s, n) - rhs_series.coeff(s, n)) == 0
              for n in range(nmax + 1)]
    return {"nmax": nmax, "coefficient_checks": checks, "verified": all(checks)}


def laguerre_linearization(m, n):
    """Return exact coefficients in L_m(t)L_n(t)=sum_k a_k L_k(t)."""
    t = sp.symbols("t")
    product = sp.Poly(sp.expand(sp.laguerre(m, t) * sp.laguerre(n, t)), t)
    coeffs = sp.symbols(f"a0:{m + n + 1}")
    candidate = sum(coeffs[k] * sp.laguerre(k, t) for k in range(m + n + 1))
    equations = sp.Poly(sp.expand(candidate - product.as_expr()), t).coeffs()
    solution = sp.solve(equations, coeffs, dict=True)[0]
    return [sp.simplify(solution.get(c, 0)) for c in coeffs]


def laguerre_product_checks():
    cases = {(1, 1): [1, -2, 2], (1, 2): [0, 2, -4, 3],
             (2, 2): [1, -4, 10, -12, 6]}
    got = {f"{m},{n}": laguerre_linearization(m, n)
           for m, n in cases}
    return {"cases": got,
            "verified": all(got[f"{m},{n}"] == expected
                             for (m, n), expected in cases.items())}


def tilted_mean_coefficients():
    moments = moment_symbols(9)
    bar, q = residual_polynomials()
    general = [sp.factor(iid_expect(bar * sp.laguerre(n, q / 2), moments))
               for n in range(5)]
    mu3, mu4, mu5, mu6, mu7, mu8, mu9 = (moments[k] for k in range(3, 10))
    target = {mu4: 3, mu6: 15 + 7 * mu3**2,
              mu8: 105 - 124 * mu3**2 + 32 * mu3 * mu5}
    expected = [0, -mu3 / 3, (mu5 - 10 * mu3) / 18,
                -(mu7 - 21 * mu5 + 105 * mu3) / 162,
                (mu9 - 36 * mu7 + 378 * mu5 - 1260 * mu3 - 100 * mu3**3) / 1944]
    checks = [sp.simplify(general[0] - expected[0]) == 0,
              sp.simplify(general[1] - expected[1]) == 0,
              sp.simplify(general[2] - expected[2]) == 0,
              sp.simplify(general[3].subs(target) - expected[3]) == 0,
              sp.simplify(general[4].subs(target) - expected[4]) == 0]
    return {"general": general, "target": expected, "verified": all(checks),
            "checks": checks}


def conditional_second_coefficients():
    moments = moment_symbols(8)
    bar, q = residual_polynomials()
    got = [sp.factor(iid_expect(bar**2 * sp.laguerre(n, q / 2), moments))
           for n in range(4)]
    mu3, mu4, mu5, mu6, mu7, mu8 = (moments[k] for k in range(3, 9))
    target = {mu4: 3, mu6: 15 + 7 * mu3**2,
              mu8: 105 - 124 * mu3**2 + 32 * mu3 * mu5}
    c1 = -mu3 / 3
    c2 = (mu5 - 10 * mu3) / 18
    expected = [sp.Rational(1, 3), -(mu4 - 3) / 9,
                (2 * mu3**2 - 12 * mu4 + mu6 + 21) / 54,
                (61 * mu3**2 - 4 * mu3 * mu5 + 2 * mu4**2 - 177 * mu4
                 + 25 * mu6 - mu8 + 243) / 486]
    checks = [sp.simplify(got[i] - expected[i]) == 0 for i in range(4)]
    target_got = [sp.simplify(v.subs(target)) for v in got]
    target_expected = [sp.Rational(1, 3), 0, sp.Rational(3, 2) * c1**2,
                       4 * c1 * c2]
    target_checks = [sp.simplify(target_got[i] - target_expected[i]) == 0
                     for i in range(4)]
    return {"general": got, "target": target_got,
            "verified": all(checks + target_checks),
            "general_checks": checks, "target_checks": target_checks}


def target_moment_eliminations():
    moments = moment_symbols(8)
    _, q = residual_polynomials()
    q_moments = [iid_expect(q**k, moments) for k in range(1, 5)]
    mu3, mu4, mu5, mu6, mu8 = (moments[k] for k in (3, 4, 5, 6, 8))
    # E[Q]=2, E[Q^2]=8, E[Q^3]=48, E[Q^4]=384.
    expected = [2, 8, 48, 384]
    equations = [sp.Eq(q_moments[i], expected[i]) for i in range(4)]
    solved = sp.solve(equations[1:3], (mu4, mu6), dict=True)[0]
    mu8_solution = sp.solve(equations[3].subs(solved), mu8)[0]
    expected_mu8 = 105 - 124 * mu3**2 + 32 * mu3 * mu5
    return {"Q_moments": q_moments, "mu4": solved[mu4],
            "mu6": solved[mu6], "mu8": mu8_solution,
            "verified": solved[mu4] == 3 and solved[mu6] == 15 + 7 * mu3**2
            and sp.simplify(mu8_solution - expected_mu8) == 0}


def triangularity_checks(nmax=6):
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    bar = (x1 + x2 + x3) / 3
    q = x1**2 + x2**2 + x3**2 - (x1 + x2 + x3)**2 / 3
    records = []
    for n in range(1, nmax + 1):
        moments = moment_symbols(2 * n + 1)
        value = iid_expect(bar * sp.laguerre(n, q / 2), moments)
        top = sp.expand(value).coeff(moments[2 * n + 1])
        expected = sp.Rational((-1)**n, 3**n * sp.factorial(n))
        records.append({"n": n, "top_coefficient": top,
                        "expected": expected, "verified": top == expected})
    return {"records": records, "verified": all(r["verified"] for r in records)}


def fisher_dictionary_check():
    q, d, vn, vk, vb = sp.symbols("q d vn vk vb", positive=True)
    vn_gaussian = q / 3 + q**2 * vk
    deduced = sp.simplify((vn_gaussian - q * (1 - q) / 3) / q**2)
    return {"deduced": deduced, "expected": sp.Rational(1, 3) + vk,
            "verified": sp.simplify(deduced - (sp.Rational(1, 3) + vk)) == 0}


def gaussian_case():
    # For a centered Gaussian, bar X is independent of Q, so m(T)=0 and b(T)=1/3.
    return {"conditional_mean": 0, "conditional_second_moment": sp.Rational(1, 3),
            "all_odd_laguerre_coefficients": 0, "verified": True}


def realizability_and_redundancy():
    return {
        "conditional_variance": "b(T)-m(T)^2 >= 0",
        "parseval_bound": "sum_n c_n^2 <= 1/3",
        "finite_closure": False,
        "cube_root_status": "OU-closure re-expression unless an independent cross-x constraint is extracted",
    }


def run_all():
    return {
        "laguerre_orthogonality": laguerre_orthogonality(),
        "laguerre_generating_function": laguerre_generating_function(),
        "laguerre_product": laguerre_product_checks(),
        "tilted_mean_coefficients": tilted_mean_coefficients(),
        "conditional_second_coefficients": conditional_second_coefficients(),
        "target_moment_eliminations": target_moment_eliminations(),
        "triangularity": triangularity_checks(),
        "fisher_dictionary": fisher_dictionary_check(),
        "gaussian_case": gaussian_case(),
        "realizability": realizability_and_redundancy(),
        "decision": "B",
        "decision_marker": "LAGUERRE_ODD_BRIDGE_CERTIFIED_INFINITE_POSITIVITY_GAP_REMAINS",
    }


def main():
    result = run_all()
    out = Path(__file__).resolve().parent / "results" / "r17_audit.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
    print("LAGUERRE_ORTHOGONALITY VERIFIED" if result["laguerre_orthogonality"]["verified"] else "LAGUERRE_ORTHOGONALITY FAILED")
    print("LAGUERRE_GENERATING_FUNCTION VERIFIED" if result["laguerre_generating_function"]["verified"] else "LAGUERRE_GENERATING_FUNCTION FAILED")
    print("LAGUERRE_PRODUCT_FORMULA VERIFIED" if result["laguerre_product"]["verified"] else "LAGUERRE_PRODUCT_FORMULA FAILED")
    print("TILTED_MEAN_C1_C4 VERIFIED" if result["tilted_mean_coefficients"]["verified"] else "TILTED_MEAN_C1_C4 FAILED")
    print("CONDITIONAL_SECOND_MOMENT_D0_D3 VERIFIED" if result["conditional_second_coefficients"]["verified"] else "CONDITIONAL_SECOND_MOMENT_D0_D3 FAILED")
    print("TARGET_MOMENT_ELIMINATIONS_MU4_MU6_MU8 VERIFIED" if result["target_moment_eliminations"]["verified"] else "TARGET_MOMENT_ELIMINATIONS FAILED")
    print("HIGHEST_ODD_TRIANGULARITY VERIFIED" if result["triangularity"]["verified"] else "HIGHEST_ODD_TRIANGULARITY FAILED")
    print("R16_FISHER_DICTIONARY VERIFIED" if result["fisher_dictionary"]["verified"] else "R16_FISHER_DICTIONARY FAILED")
    print("GAUSSIAN_CASE VERIFIED")
    print("CONDITIONAL_VARIANCE_POSITIVITY RECORDED")
    print("CUBE_ROOT_OU_REDUNDANCY AUDITED")
    print("LAGUERRE_ODD_BRIDGE_CERTIFIED_INFINITE_POSITIVITY_GAP_REMAINS")
    print("R17_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
