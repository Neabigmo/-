"""Finite exact benchmark bound and Wiener tail replay."""
from __future__ import annotations

import math
import sympy as sp


def central_binomial_replay(max_m: int = 20) -> dict:
    a_star = sp.sqrt(sp.Rational(2, 3))
    c = 1 / sp.sqrt(2)
    rows = []
    for m in range(1, max_m + 1):
        n = 2 * m
        ratio = sp.Rational(math.comb(2 * m, m), 4**m)
        rows.append({"n": n, "central_lower_holds": bool(ratio >= 1 / sp.sqrt(4 * m)), "requested_lower_holds": bool(a_star**n * ratio >= c * a_star**n / sp.sqrt(n + 1))})
    return {"a_star": str(a_star), "c": str(c), "rows": rows, "all_bounds_hold": all(row["central_lower_holds"] and row["requested_lower_holds"] for row in rows)}


def normalized_multinomial_bound(n: int = 8) -> dict:
    a_star = sp.sqrt(sp.Rational(2, 3))
    factor = a_star / 3
    rows = []
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            coeff = sp.factorial(n) / (sp.factorial(i) * sp.factorial(j) * sp.factorial(k)) * factor**n
            rows.append(coeff <= a_star**n)
    return {"degree": n, "all_multinomial_terms_le_a_star_n": bool(all(rows))}


def wiener_tail_replay(eta: sp.Rational = sp.Rational(1, 2), cutoffs=(2, 4, 8, 12)) -> dict:
    rows = []
    for N in cutoffs:
        two = max((sp.sqrt(n + 1) * eta**n for n in range(2 * N, 80)), default=sp.Integer(0))
        three = max((sp.sqrt(n + 1) * eta**n for n in range(3 * N, 80)), default=sp.Integer(0))
        rows.append({"N": N, "two_high_bound": str(two), "three_high_bound": str(three)})
    return {"eta": str(eta), "rows": rows, "tail_decreases_in_replay": all(sp.sympify(rows[i]["two_high_bound"]) >= sp.sympify(rows[i + 1]["two_high_bound"]) for i in range(len(rows) - 1))}

