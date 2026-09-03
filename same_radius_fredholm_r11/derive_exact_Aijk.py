"""Exact finite-degree angular-kernel and corrected Beta replay."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
x = sp.symbols("x")
t = sp.symbols("t", real=True)
# Use an algebraic representative so exact simplification does not depend on
# SymPy recognizing exp(2*pi*I/3) and the corresponding quadratic root as the
# same number.
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
omega_bar = -sp.Rational(1, 2) - sp.sqrt(3) * sp.I / 2
a_star = sp.sqrt(sp.Rational(2, 3))


def omega_pow(power: int) -> sp.Expr:
    return (sp.Integer(1), omega, omega**2)[power % 3]


def beta_moment(n: int, power: int) -> sp.Expr:
    if power % 2:
        return sp.Integer(0)
    s = power // 2
    return sp.simplify(sp.rf(sp.Rational(1, 2), s) / sp.rf((sp.sympify(n) + 1) / 2 - s, s))


def direct_beta_integral(n: int, power: int) -> sp.Expr:
    alpha = sp.Rational(n, 2) + 1
    num = sp.integrate(t**power / (1 + t**2) ** alpha, (t, -sp.oo, sp.oo))
    den = sp.integrate(1 / (1 + t**2) ** alpha, (t, -sp.oo, sp.oo))
    return sp.simplify(num / den)


def angular_kernel(i: int, j: int, k: int) -> sp.Expr:
    n = i + j + k
    if n % 2:
        return sp.Integer(0)
    total = sp.Integer(0)
    for p in range(i + 1):
        for q in range(j + 1):
            for r in range(k + 1):
                if p + q + r == n // 2:
                    phase = (j - 2 * q) + 2 * (k - 2 * r)
                    total += sp.binomial(i, p) * sp.binomial(j, q) * sp.binomial(k, r) * omega_pow(phase)
    return sp.simplify(a_star**n * total / 2**n)


def _laurent_mul(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    for e1, c1 in left.items():
        for e2, c2 in right.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + c1 * c2
    return {e: sp.simplify(c) for e, c in out.items()}


def _laurent_pow(base: dict[int, sp.Expr], power: int) -> dict[int, sp.Expr]:
    out = {0: sp.Integer(1)}
    for _ in range(power):
        out = _laurent_mul(out, base)
    return out


def _angular_laurent(i: int, j: int, k: int) -> dict[int, sp.Expr]:
    # x is exp(i*theta); phases are exact cube roots of unity.
    bases = [
        {1: a_star / 2, -1: a_star / 2},
        {1: a_star * omega / 2, -1: a_star * omega_bar / 2},
        {1: a_star * omega_bar / 2, -1: a_star * omega / 2},
    ]
    out = {0: sp.Integer(1)}
    for base, power in zip(bases, (i, j, k)):
        out = _laurent_mul(out, _laurent_pow(base, power))
    return out


def direct_angular_constant(i: int, j: int, k: int) -> sp.Expr:
    return sp.simplify(_angular_laurent(i, j, k).get(0, 0))


def roots_of_unity_filter(i: int, j: int, k: int) -> sp.Expr:
    # q=2n+1 exceeds every nonzero Fourier exponent, so the q-root filter
    # isolates precisely exponent 0 without numerical quadrature.
    n = i + j + k
    q = 2 * n + 1
    coeffs = _angular_laurent(i, j, k)
    return sp.simplify(sum(c for e, c in coeffs.items() if e % q == 0))


def run_replay(max_degree: int = 8) -> dict:
    beta_rows = []
    # The density has finite moments only for powers strictly below n+1.
    # These n values make every requested power 0..6 integrable.
    for n in (8, 10, 12):
        for power in range(7):
            lhs = beta_moment(n, power)
            rhs = direct_beta_integral(n, power)
            beta_rows.append({"n": n, "power": power, "residual": str(sp.simplify(lhs - rhs))})
    angular_rows = []
    for i in range(max_degree + 1):
        for j in range(max_degree - i + 1):
            for k in range(max_degree - i - j + 1):
                exact = angular_kernel(i, j, k)
                direct = direct_angular_constant(i, j, k)
                roots = roots_of_unity_filter(i, j, k)
                angular_rows.append({"i": i, "j": j, "k": k, "direct_residual": str(sp.simplify(exact - direct)), "roots_residual": str(sp.simplify(exact - roots)), "value": str(exact)})
    payload = {
        "beta_rows": beta_rows,
        "beta_all_zero": all(row["residual"] == "0" for row in beta_rows),
        "angular_rows": angular_rows,
        "angular_all_zero": all(row["direct_residual"] == "0" and row["roots_residual"] == "0" for row in angular_rows),
        "degree": max_degree,
        "markers": ["R11_BETA_CORRECTION_REPLAYED", "R11_EXACT_A_IJK_SMALL_DEGREE_REPLAYED", "R11_ROOTS_OF_UNITY_REPLAYED"],
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "exact_Aijk.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in payload["markers"]:
        print(marker)
    print("R11_BETA_RESIDUALS", sorted({row["residual"] for row in beta_rows}))
    print("R11_A_IJK_DIRECT_RESIDUALS", sorted({row["direct_residual"] for row in angular_rows}))
    print("R11_A_IJK_ROOT_FILTER_RESIDUALS", sorted({row["roots_residual"] for row in angular_rows}))
    return payload


if __name__ == "__main__":
    run_replay()
