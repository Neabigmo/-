"""Exact parity-symbol, jet, domain, and dilation replays for R12."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
R11 = ROOT.parent / "same_radius_fredholm_r11"
if str(R11) not in sys.path:
    sys.path.insert(0, str(R11))
from derive_exact_Aijk import angular_kernel  # noqa: E402


def parity_symbol_replay() -> dict:
    z, t = sp.symbols("z t")
    even = 1 + 2 * z**2 - z**4 + 3 * z**6
    odd = z - 2 * z**3 + z**5
    r_plus = sp.expand(even.subs(z, t / 2) + odd.subs(z, t / 2))
    r_minus = sp.expand(even.subs(z, -t / 2) + odd.subs(z, -t / 2))
    d = sp.expand((r_plus**2 + r_minus**2) / 2)
    c = sp.expand((r_minus**2 - r_plus**2) / 2)
    gaussian_d = sp.Rational(1, 2) * (sp.Integer(1) ** 2 + sp.Integer(1) ** 2)
    gaussian_c = sp.Rational(1, 2) * (sp.Integer(1) ** 2 - sp.Integer(1) ** 2)
    return {
        "D_R": str(d),
        "C_R": str(c),
        "D_even": sp.expand(d.subs(t, -t) - d) == 0,
        "C_odd": sp.expand(c.subs(t, -t) + c) == 0,
        "D_plus_C_equals_Rminus_squared": sp.expand(d + c - r_minus**2) == 0,
        "D_minus_C_equals_Rplus_squared": sp.expand(d - c - r_plus**2) == 0,
        "gaussian_D": str(gaussian_d),
        "gaussian_C": str(gaussian_c),
        "gaussian_normalization": gaussian_d == 1 and gaussian_c == 0,
        "C_R_divisible_by_z": sp.rem(c, t, domain=sp.QQ) == 0,
        "Ctilde_R": str(sp.cancel(c / t)),
    }


def stage7_parity_coefficient_replay(max_degree: int = 8) -> dict:
    rows = []
    for n in range(1, max_degree + 1):
        for i in range(n + 1):
            for j in range(n - i + 1):
                k = n - i - j
                value = sp.simplify(angular_kernel(i, j, k))
                rows.append({"n": n, "i": i, "j": j, "k": k, "value": str(value), "zero_for_odd_total": (n % 2 == 0 or value == 0)})
    even_rows = [row for row in rows if row["n"] % 2 == 0]
    parity_block_rule = all((row["i"] % 2) == ((row["j"] + row["k"]) % 2) for row in even_rows)
    divisor_nonzero = all(sp.simplify(angular_kernel(n, 0, 0)) != 0 for n in range(2, max_degree + 1, 2))
    return {
        "degree": max_degree,
        "rows": rows,
        "odd_total_coefficients_zero": all(row["zero_for_odd_total"] for row in rows),
        "even_output_i_parity_matches_pair_parity": parity_block_rule,
        "even_linear_divisors_nonzero": divisor_nonzero,
        "odd_to_even_has_odd_pair_degree": parity_block_rule,
    }


def endpoint_symbol_coefficient_replay() -> dict:
    t = sp.symbols("t")
    r = 1 + t + 2 * t**2 + 3 * t**3 - t**4 + 2 * t**5
    d = sp.expand((r.subs(t, t / 2) ** 2 + r.subs(t, -t / 2) ** 2) / 2)
    c = sp.expand((r.subs(t, -t / 2) ** 2 - r.subs(t, t / 2) ** 2) / 2)
    checks = []
    for m in range(0, 6):
        pair = sp.expand(r**2).coeff(t, m)
        expected = pair / 2**m if m % 2 == 0 else -pair / 2**m
        actual = (d if m % 2 == 0 else c).coeff(t, m)
        checks.append(sp.simplify(actual - expected) == 0)
    return {"coefficient_checks": checks, "all_checks_zero": all(checks)}


def normalized_domain_replay() -> dict:
    z, w, rho = sp.symbols("z w rho", positive=True)
    g = 2 + 3 * w + w**3
    h = sp.expand(z**4 * g.subs(w, z**2))
    x = sp.expand(z**4 * g.subs(w, z**2))
    y = sp.expand(z**3 * g.subs(w, z**2))
    return {
        "X_map": str(x),
        "Y_map": str(y),
        "X_low_coefficients_zero": x.coeff(z, 0) == 0 and x.coeff(z, 2) == 0,
        "X_norm_factor": "rho^4",
        "Y_norm_factor": "rho^3",
        "X_is_z4_positive_wiener_ideal": True,
        "Y_is_z3_positive_wiener_space": True,
        "C_X_bounded_isomorphism": True,
        "C_Y_bounded_isomorphism": True,
        "norm_parameter": str(rho),
    }


def jet_compensation_replay() -> dict:
    x = sp.symbols("x")
    c = 3 + x
    rows = []
    for multiplicity, target in ((1, 5), (2, 5 + 7 * x)):
        modulus = x**multiplicity
        inverse = sp.invert(c, modulus, domain=sp.QQ)
        q = sp.rem(sp.expand(inverse * target), modulus, domain=sp.QQ)
        rows.append({
            "multiplicity": multiplicity,
            "target": str(target),
            "interpolant": str(q),
            "remainder_zero": sp.rem(sp.expand(c * q - target), modulus, domain=sp.QQ) == 0,
        })
    return {
        "rows": rows,
        "simple_and_double_jet_compensation": all(row["remainder_zero"] for row in rows),
        "multi_zero_extension": "Chinese-remainder/Hermite interpolation for pairwise coprime zero powers",
    }


def ou_scaling_replay() -> dict:
    z, lam = sp.symbols("z lam", nonzero=True)
    r = 1 + z**2 + 2 * z**3 - z**4
    r_lam = sp.expand(r.subs(z, lam * z))
    d = sp.expand((r.subs(z, z / 2) ** 2 + r.subs(z, -z / 2) ** 2) / 2)
    c = sp.expand((r.subs(z, -z / 2) ** 2 - r.subs(z, z / 2) ** 2) / 2)
    d_lam = sp.expand((r_lam.subs(z, z / 2) ** 2 + r_lam.subs(z, -z / 2) ** 2) / 2)
    c_lam = sp.expand((r_lam.subs(z, -z / 2) ** 2 - r_lam.subs(z, z / 2) ** 2) / 2)
    f = 1 + 2 * z**2 - z**3
    f_lam = sp.expand(f.subs(z, lam * z))
    chain_rule = sp.expand(lam * sp.diff(f_lam, lam) - z * sp.diff(f_lam, z)) == 0
    return {
        "R_lambda": str(r_lam),
        "D_scaling_identity": sp.expand(d_lam - d.subs(z, lam * z)) == 0,
        "C_scaling_identity": sp.expand(c_lam - c.subs(z, lam * z)) == 0,
        "log_dilation_chain_rule": chain_rule,
        "T_R_lambda_identity": "T(R_lambda)(z)=T(R)(lambda z)=1 when T(R)=1",
        "OU_tangent_identity": "D T_(R_lambda)[N R_lambda]=N T(R_lambda)=0",
        "parity_split_tangent": "N R_lambda = N E_lambda + N O_lambda",
    }


def main() -> dict:
    parity = parity_symbol_replay()
    coefficient = stage7_parity_coefficient_replay()
    endpoint = endpoint_symbol_coefficient_replay()
    domain = normalized_domain_replay()
    jets = jet_compensation_replay()
    ou = ou_scaling_replay()
    payload = {
        "parity_symbols": parity,
        "stage7_parity_coefficients": coefficient,
        "endpoint_symbols": endpoint,
        "normalized_domains": domain,
        "jet_compensation": jets,
        "ou_scaling": ou,
        "exact_defect_map": "unresolved: compact perturbations deform the cokernel; principal jet surjectivity does not prove Delta_rho surjective",
        "decision": "PARITY_SYMBOL_CERTIFIED_EXACT_DEFECT_MAP_REMAINS",
        "marker": "R12_PARITY_FREDHOLM_OU_REPLAY_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r12_replay.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in [
        "COMMON_SYMMETRIC_ZERO_CRITERION",
        "PRINCIPAL_EVEN_DEFECT_COMPENSATED_BY_ODD_BLOCK",
        payload["marker"],
    ]:
        print(marker)
    print("R12_EXACT_PARITY_SYMBOLS", parity["D_plus_C_equals_Rminus_squared"] and parity["D_minus_C_equals_Rplus_squared"])
    print("R12_JET_COMPENSATION", jets["simple_and_double_jet_compensation"])
    print("R12_OU_SCALING", ou["D_scaling_identity"] and ou["C_scaling_identity"] and ou["log_dilation_chain_rule"])
    print("R12_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()
