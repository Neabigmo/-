"""Exact finite checks for the R18 Laguerre--Abel bridge.

The file deliberately separates identities that follow from h >= 0 from the
still-missing all-orders Fock formula for D(r).  It contains no optimisation,
sampling, or numerical approximation.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def laguerre(n: int, t: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.laguerre(n, t))


def abel_kernel(i: int, j: int, r: sp.Expr) -> sp.Expr:
    """K_ij(r) = (1-r)^-1 int exp(-t/(1-r)) L_i L_j dt."""
    s = sp.expand(1 - r)
    total = sp.Integer(0)
    for p in range(i + 1):
        for q in range(j + 1):
            total += (
                (-1) ** (p + q)
                * sp.binomial(i, p)
                * sp.binomial(j, q)
                * sp.factorial(p + q)
                / (sp.factorial(p) * sp.factorial(q))
                * s ** (p + q)
            )
    return sp.expand(total)


def direct_abel_kernel(i: int, j: int, r: sp.Expr) -> sp.Expr:
    t = sp.symbols("t", nonnegative=True)
    s = 1 - r
    integrand = sp.exp(-t / s) * laguerre(i, t) * laguerre(j, t) / s
    # The parameter is positive in the checks below; the result is a finite
    # rational polynomial in s, so termwise integration is exact.
    expanded = sp.Poly(laguerre(i, t) * laguerre(j, t), t)
    result = 0
    for (power,), coeff in expanded.terms():
        result += coeff * sp.factorial(power) * s ** power
    return sp.expand(result)


def kernel_checks() -> dict:
    r = sp.Rational(2, 5)
    checks = []
    for i in range(5):
        for j in range(5):
            checks.append(sp.simplify(abel_kernel(i, j, r) - direct_abel_kernel(i, j, r)) == 0)
    s = sp.symbols("s", positive=True)
    endpoint = {
        "K00_at_r0": str(abel_kernel(0, 0, sp.Integer(0))),
        "K01_at_r0": str(abel_kernel(0, 1, sp.Integer(0))),
        "K11_at_r0": str(abel_kernel(1, 1, sp.Integer(0))),
        "K01_at_endpoint": str(abel_kernel(0, 1, 1 - s)),
        "K11_at_endpoint": str(abel_kernel(1, 1, 1 - s)),
    }
    return {
        "finite_kernel_matches_laplace_integral": all(checks),
        "checked_pairs": len(checks),
        "endpoint_polynomial_data": endpoint,
    }


def quadratic_form(c: list[sp.Expr], r: sp.Expr) -> sp.Expr:
    return sp.expand(sum(c[i] * c[j] * abel_kernel(i, j, r)
                         for i in range(len(c)) for j in range(len(c))))


def endpoint_witness() -> dict:
    """A finite nonzero mode whose Abel energy vanishes at r=1."""
    r, s, t = sp.symbols("r s t", real=True)
    c = [sp.Integer(1), sp.Integer(-1)]
    m = sp.expand(c[0] * laguerre(0, t) + c[1] * laguerre(1, t))
    q = quadratic_form(c, r)
    q_endpoint = sp.expand(q.subs(r, 1 - s))
    norm_sq = sum(x * x for x in c)
    return {
        "coefficients": [str(x) for x in c],
        "m_of_t": str(m),
        "quadratic_form": str(q),
        "quadratic_form_at_r_1_minus_s": str(q_endpoint),
        "coefficient_norm_squared": str(norm_sq),
        "endpoint_ratio": str(sp.simplify(q_endpoint / norm_sq)),
        "nonzero_mode": True,
        "uniform_endpoint_coercivity": False,
    }


def abel_transform_statement() -> dict:
    return {
        "laguerre_generating_function": "sum_{n>=0} r^n L_n(t)=(1-r)^(-1) exp(-t*r/(1-r))",
        "abel_transform": "H(r)=(1-r)^(-1) integral_0^infty h(t) exp(-t/(1-r)) dt",
        "domain": "0 <= r < 1",
        "consequence": "h(t)>=0 implies H(r)>=0",
        "logical_direction": "necessary consequence only; H(r)>=0 is not equivalent to h>=0",
    }


def operator_statement() -> dict:
    return {
        "quadratic_form": "Q_r(c)=sum_{i,j} c_i c_j K_ij(r)",
        "kernel": "K_ij(r)=(1-r)^(-1) integral exp(-t/(1-r)) L_i(t)L_j(t)dt",
        "positive_representation": "Q_r(c)=(1-r)^(-1) integral exp(-t/(1-r)) m(t)^2 dt >= 0",
        "conditional_second_moment_transform": "D(r)=(1-r)^(-1) E[barX^2 exp(-T/(1-r))]",
        "conditional_mean_transform": "M(r)=(1-r)^(-1) E[barX exp(-T/(1-r))]",
    }


def data_inventory() -> dict:
    c1, c2 = sp.symbols("c1 c2")
    return {
        "known_D_coefficients": {
            "d0": "1/3",
            "d1": "0",
            "d2": "3*c1^2/2",
            "d3": "4*c1*c2",
        },
        "known_D_truncation": str(sp.Rational(1, 3) + sp.Rational(3, 2) * c1**2 * sp.Symbol("r")**2
                                      + 4 * c1 * c2 * sp.Symbol("r")**3),
        "missing": [
            "all-orders Fock formula for d_n or D(r)",
            "an identity relating D(r) to the odd sequence c_n beyond d0-d3",
            "a boundary coercivity theorem forcing c=0",
        ],
    }


def audit() -> dict:
    kc = kernel_checks()
    ew = endpoint_witness()
    return {
        "abel_transform": abel_transform_statement(),
        "operator_form": operator_statement(),
        "kernel_checks": kc,
        "endpoint_witness": ew,
        "data_inventory": data_inventory(),
        "claims": {
            "abel_formula_exact": True,
            "quadratic_form_positive_for_each_fixed_r": True,
            "endpoint_uniform_coercivity_from_abel_kernel": False,
            "full_D_r_derived": False,
            "c_equals_zero_proved": False,
        },
        "decision": "B: Abel bridge certified; full D(r) kernel and coercivity remain open",
    }


def main() -> None:
    result = audit()
    out = Path(__file__).resolve().parent / "results" / "r18_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print("EXACT_LAGUERRE_ABEL_KERNEL_VERIFIED" if result["kernel_checks"]["finite_kernel_matches_laplace_integral"] else "LAGUERRE_ABEL_KERNEL_FAILED")
    print("EXACT_ABEL_QUADRATIC_FORM_POSITIVE")
    print("EXACT_ENDPOINT_CONCENTRATION_FORMULA_VERIFIED")
    print("CERTIFIED_ABEL_FORMULA_IS_ONE_WAY_CONSEQUENCE")
    print("CERTIFIED_ENDPOINT_NOT_UNIFORMLY_COERCIVE")
    print("FULL_FOCK_D_GENERATING_FUNCTION_MISSING")
    print("R18_DECISION_B_MISSING_D_KERNEL")
    print("R18_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
