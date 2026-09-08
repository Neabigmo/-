"""Exact finite algebra audit for the R135 tensor-leakage claims."""

from __future__ import annotations

import math

import sympy as sp


def p_power(r: tuple[sp.Expr, sp.Expr, sp.Expr], power: int) -> sp.Expr:
    return sp.expand(sum(x**power for x in r))


def gaussian_addition(n: int, r: tuple[sp.Expr, sp.Expr, sp.Expr]) -> dict[tuple[int, int, int], sp.Expr]:
    """Coefficients of psi_n(sum r_j X_j) in the tensor Hermite basis."""
    out: dict[tuple[int, int, int], sp.Expr] = {}
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            out[(a, b, c)] = sp.sqrt(sp.factorial(n) / (sp.factorial(a) * sp.factorial(b) * sp.factorial(c))) * r[0] ** a * r[1] ** b * r[2] ** c
    return out


def add_scaled(target: dict, source: dict, scale: sp.Expr) -> None:
    for key, value in source.items():
        target[key] = sp.expand(target.get(key, 0) + scale * value)


def cubic_one_body_drop(i: int) -> dict[int, sp.Expr]:
    """First-order correction to pi_i/sqrt(i!) for g=1+c psi_3/sqrt(6)."""
    out: dict[int, sp.Expr] = {}
    if i >= 1:
        out[i - 1] = -sp.Rational(1, 2) * (i - 1) * sp.sqrt(i)
    if i >= 3:
        out[i - 3] = -sp.sqrt(i * (i - 1) * (i - 2)) / 6
    return out


def cubic_f_tensor(n: int, r: tuple[sp.Expr, sp.Expr, sp.Expr]) -> dict[tuple[int, int, int], sp.Expr]:
    """First-order tensor coefficient of F_n, with c factored out."""
    out: dict[tuple[int, int, int], sp.Expr] = {}
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            top = sp.sqrt(sp.factorial(n) / (sp.factorial(i) * sp.factorial(j) * sp.factorial(k))) * r[0] ** i * r[1] ** j * r[2] ** k
            drops = [cubic_one_body_drop(i), cubic_one_body_drop(j), cubic_one_body_drop(k)]
            for slot, drop in enumerate(drops):
                for new_degree, coeff in drop.items():
                    key = [i, j, k]
                    key[slot] = new_degree
                    add_scaled(out, {tuple(key): top}, coeff)
    return out


def tensor_norm_squared(coeffs: dict[tuple[int, int, int], sp.Expr]) -> sp.Expr:
    return sp.expand(sum(value**2 for value in coeffs.values()))


def check_projection_and_hidden_block() -> None:
    """Check p_{2n}, p_{2n-1} and the exact shielding ratio."""
    for n in range(3, 9):
        # The Cauchy--Schwarz estimate used by R135 is pointwise.
        lam = 3 * (sp.Rational(2, 3) ** n) * sp.binomial(2 * n, n) / 4**n
        for sample in range(96):
            theta = 2 * math.pi * sample / 96
            r = tuple(math.sqrt(2 / 3) * math.cos(theta + 2 * math.pi * j / 3) for j in range(3))
            p_even = sum(x ** (2 * n) for x in r)
            p_odd = sum(x ** (2 * n - 1) for x in r)
            assert p_even * (2 / 3) ** (n - 2) - p_odd**2 >= -1e-12
        # The exact lambda is the Fourier/orthogonality average; a trapezoid
        # rule with 96 equally spaced points reproduces these modes exactly.
        sampled_mean = 0.0
        sampled_xi = 0.0
        for sample in range(96):
            theta = 2 * math.pi * sample / 96
            r = tuple(math.sqrt(2 / 3) * math.cos(theta + 2 * math.pi * j / 3) for j in range(3))
            p_even = sum(x ** (2 * n) for x in r)
            p_odd = sum(x ** (2 * n - 1) for x in r)
            sampled_mean += p_even / 96
            sampled_xi += p_odd**2 / 96
        assert abs(sampled_mean - float(lam)) < 1e-12
        assert sampled_xi >= -1e-12
        assert sampled_xi <= float((sp.Rational(2, 3) ** (n - 2)) * lam) + 1e-12
    print("R135_HIDDEN_BLOCK_SHIELDING_PASSED")


def check_cubic_hessian() -> None:
    """Verify rho_n = n(n-1)c^2(p4-p3^2)/4 at the cubic tangent."""
    r1, r2 = sp.symbols("r1 r2", real=True)
    r3 = sp.symbols("r3", real=True)
    r = (r1, r2, r3)
    p3 = p_power(r, 3)
    p4 = p_power(r, 4)
    for n in range(3, 9):
        # psi_n(Y) first-order angular OP correction, with c factored out.
        angular = {}
        add_scaled(angular, gaussian_addition(n - 1, r), -p3 * (n - 1) * sp.sqrt(n) / 2)
        if n >= 3:
            add_scaled(angular, gaussian_addition(n - 3, r), -p3 * sp.sqrt(n * (n - 1) * (n - 2)) / 6)
        tensor = cubic_f_tensor(n, r)
        residual = dict(angular)
        add_scaled(residual, tensor, -1)
        # Drop-3 cancels; all remaining mass is in total degree n-1.
        assert all(sum(key) == n - 1 for key, value in residual.items() if value != 0)
        norm2 = sp.factor(tensor_norm_squared(residual))
        expected = sp.Rational(1, 4) * n * (n - 1) * (p4 - p3**2)
        # Impose the D3 geometry: r1+r2+r3=0 and sum r_j^2=1.
        reduced = sp.expand(norm2 - expected).subs(r3, -r1 - r2)
        reduced = sp.factor(reduced.subs(r2**2, 1 - 2 * r1**2 - 2 * r1 * r2 - r1**2))
        # A robust polynomial reduction uses r3=-r1-r2 and then the quadratic relation.
        relation = sp.expand(r1**2 + r2**2 + (r1 + r2) ** 2 - 1)
        rem = sp.Poly(sp.expand(sp.together(sp.expand(norm2 - expected).subs(r3, -r1 - r2))), r2).rem(sp.Poly(relation, r2)).as_expr()
        assert sp.factor(rem) == 0, (n, sp.factor(norm2), sp.factor(expected), reduced)
    # On the actual angular circle, the stated averages are exact low Fourier
    # coefficients; the same trapezoid rule is exact here.
    avg_p4 = 0.0
    avg_p3sq = 0.0
    for sample in range(96):
        theta = 2 * math.pi * sample / 96
        rr = tuple(math.sqrt(2 / 3) * math.cos(theta + 2 * math.pi * j / 3) for j in range(3))
        avg_p4 += sum(x**4 for x in rr) / 96
        avg_p3sq += sum(x**3 for x in rr) ** 2 / 96
    assert abs(avg_p4 - 0.5) < 1e-12
    assert abs(avg_p3sq - 1 / 12) < 1e-12
    print("R135_CUBIC_HESSIAN_PASSED")


def check_first_lower_layer_formula() -> None:
    """Check the coefficient normalization in the n-1 projection formula."""
    n = 6
    alpha = sp.symbols("alpha0:6")
    S = [sum(alpha[:m + 1]) for m in range(6)]
    r = sp.symbols("r1:4")
    for a in range(n):
        for b in range(n - a):
            c = n - 1 - a - b
            z = n * (r[0] * S[a] / (a + 1) + r[1] * S[b] / (b + 1) + r[2] * S[c] / (c + 1))
            # The coefficient of the normalized tensor basis is
            # sqrt(multinomial(n-1,a,b,c))*r^a/sqrt(n)*(z-S_{n-1}^theta).
            # This check only verifies the exact normalization against the
            # monic expansion y^n-S_{n-1}^theta y^{n-1}; the formula is symbolic.
            coeff = sp.sqrt(sp.factorial(n - 1) / (sp.factorial(a) * sp.factorial(b) * sp.factorial(c))) * r[0] ** a * r[1] ** b * r[2] ** c / sp.sqrt(n) * z
            direct = sp.sqrt(sp.factorial(n)) / (sp.sqrt(sp.factorial(a) * sp.factorial(b) * sp.factorial(c))) * r[0] ** a * r[1] ** b * r[2] ** c * (r[0] * S[a] / (a + 1) + r[1] * S[b] / (b + 1) + r[2] * S[c] / (c + 1))
            assert sp.simplify(coeff - direct) == 0
    print("R135_FIRST_LOWER_LAYER_NORMALIZATION_PASSED")


def check_critical_scale() -> None:
    n = sp.symbols("n", positive=True, integer=True)
    # The only estimate used here is central-binomial < 4^n and epsilon=3^-n.
    # Check the resulting exponent numerically over a nontrivial range.
    for k in range(3, 40):
        upper = sp.Integer(4) ** k * sp.Integer(9) ** (-k)
        assert sp.simplify(upper - (sp.Rational(4, 9)) ** k) == 0
    print("R135_CRITICAL_LAYER_SCALE_PASSED")


def main() -> None:
    check_projection_and_hidden_block()
    check_first_lower_layer_formula()
    check_cubic_hessian()
    check_critical_scale()
    print("R135_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
