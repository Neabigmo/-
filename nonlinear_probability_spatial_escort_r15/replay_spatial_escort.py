"""Small exact replay for the R15 spatial-escort identities."""
from __future__ import annotations

import sympy as sp


def angular_power_sums():
    c = sp.symbols("c")
    p = {0: 3, 1: 0, 2: sp.Integer(1), 3: 3 * c}
    for n in range(4, 7):
        p[n] = sp.expand(sp.Rational(1, 2) * p[n - 2] + c * p[n - 3])
    averages = {
        "mean_c": sp.Integer(0),
        "mean_c2": sp.Rational(1, 108),
        "mean_p3_sq": sp.Rational(1, 12),
        "mean_p6": sp.Rational(5, 18),
    }
    return p, averages


def bell_angular_expression(order: int):
    d, z, c = sp.symbols("d z c")
    K = {r: sp.symbols(f"K{r}") for r in range(2, order + 1)}
    p, _ = angular_power_sums()
    exponent = sum(
        d**r * z**r * p[r] * K[r] / sp.factorial(r)
        for r in range(2, order + 1)
    )
    coeff = sp.expand(sp.diff(sp.exp(exponent), z, order).subs(z, 0))
    coeff = sp.expand(coeff).subs(c**2, sp.Rational(1, 108))
    coeff = sp.expand(coeff).subs(c, 0)
    return sp.factor(coeff), K


def expected_order_identities():
    d = sp.symbols("d")
    K2, K3, K4, K6 = sp.symbols("K2 K3 K4 K6")
    return {
        2: d**2 * K2,
        4: d**4 * (sp.Rational(1, 2) * K4 + 3 * K2**2),
        6: d**6 * (
            sp.Rational(5, 18) * K6
            + sp.Rational(15, 2) * K4 * K2
            + sp.Rational(5, 6) * K3**2
            + 15 * K2**3
        ),
    }


def posterior_variance_scaled_order6():
    d = sp.symbols("d")
    V, V1, V2, V4 = sp.symbols("V V1 V2 V4")
    expr = (
        V4 / d**2
        + 27 * (V2 / d**2) * ((V - d) / d**2)
        + 3 * (V1 / d**2) ** 2
        + 54 * ((V - d) / d**2) ** 3
    )
    return sp.factor(sp.expand(expr * d**6))


def gaussian_benchmark():
    d = sp.symbols("d")
    return {"Fq": sp.Integer(1), "K2": sp.Integer(0), "V": d}


def hubbard_straatonovich_check():
    t = sp.symbols("t")
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    total = x1 + x2 + x3
    q = x1**2 + x2**2 + x3**2 - total**2 / 3
    lhs = -t*(x1**2 + x2**2 + x3**2)/2 + t*total**2/6
    return sp.simplify(lhs + t*q/2) == 0


def q_t_normalization_check():
    q = sp.symbols("q")
    d = 1 - q
    t = q/d
    return sp.simplify(1/(1+t) - d) == 0


def common_shift_prefactor_check():
    q, d, z = sp.symbols("q d z")
    t = q/d
    target = d*sp.exp(d*z**2/2)
    converted = d**sp.Rational(3, 2)*d**(-sp.Rational(1, 2))*sp.exp(d*z**2/2)
    return (sp.simplify(converted - target) == 0
            and sp.simplify(d*t - q) == 0)


def stein_density_check():
    q, x = sp.symbols("q x", positive=True)
    K = sp.Function("K")
    log_density = 3*K(x) - 3*x**2/(2*q)
    score = sp.diff(log_density, x)
    return sp.simplify(-score - (3*x/q - 3*sp.diff(K(x), x))) == 0


def probability_countermodels():
    y, t = sp.symbols("y t", real=True)
    bernoulli = sp.exp(-t / 2) * sp.cosh(y)
    three_point = (
        sp.exp(-sp.sqrt(3) * t / 2 - sp.sqrt(3) * y) / 6
        + sp.Rational(2, 3)
        + sp.exp(-sp.sqrt(3) * t / 2 + sp.sqrt(3) * y) / 6
    )
    return {"bernoulli_L": bernoulli, "three_point_L": three_point}


if __name__ == "__main__":
    print(expected_order_identities())
