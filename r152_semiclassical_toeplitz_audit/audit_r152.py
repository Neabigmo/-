"""Finite numerical audit of the R152 bulk Toeplitz limit.

This checks coefficient extraction and convergence for finite-support critical
shapes.  It deliberately does not test or claim a genuine positive iid law,
uniform growing-support convergence, or the original rigidity theorem.
"""

from __future__ import annotations

import math
from typing import Dict

import mpmath as mp
import numpy as np


def exp_polynomial_coeffs(shape: Dict[int, float], degree: int) -> list[mp.mpf]:
    """Coefficients of exp(sum_k shape[k] z^k), through the requested degree."""
    p = [mp.mpf("0") for _ in range(degree + 1)]
    for k, value in shape.items():
        if k <= degree:
            p[k] = mp.mpf(str(value))
    coeff = [mp.mpf("0") for _ in range(degree + 1)]
    coeff[0] = mp.mpf("1")
    # If E'=P'E, then n E_n = sum_{k=1}^n k P_k E_(n-k).
    for n in range(1, degree + 1):
        coeff[n] = sum(k * p[k] * coeff[n - k] for k in range(1, n + 1)) / mp.mpf(n)
    return coeff


def gram_entry(lam: float, tau: float, shape: Dict[int, float], p: int, q: int) -> float:
    M = math.floor(tau / lam)
    m, n = M + p, M + q
    coeff = exp_polynomial_coeffs(shape, m + n)
    total = mp.mpf("0")
    for K, e_K in enumerate(coeff):
        if abs(e_K) < mp.mpf("1e-100") or K > m + n or (m + n - K) % 2:
            continue
        r0 = (m + n - K) // 2
        left = (K + m - n) // 2
        if left < 0 or left > K or 2 * left != K + m - n:
            continue
        log_ratio = (mp.loggamma(m + 1) + mp.loggamma(n + 1)) / 2 - mp.loggamma(r0 + 1)
        term = e_K * mp.power(mp.mpf(str(lam)), mp.mpf(K) / 2) * mp.exp(log_ratio) * mp.binomial(K, left)
        total += term
    return float(total)


def limiting_entry(tau: float, shape: Dict[int, float], delta: int) -> float:
    # A generous finite truncation is enough because exp of a polynomial is
    # entire and the tested shapes are small.
    coeff = exp_polynomial_coeffs(shape, 320)
    total = mp.mpf("0")
    for K, e_K in enumerate(coeff):
        if (K + delta) % 2 or abs(delta) > K:
            continue
        total += e_K * mp.power(mp.mpf(str(tau)), mp.mpf(K) / 2) * mp.binomial(K, (K + delta) // 2)
    return float(total)


def check_entrywise_convergence() -> None:
    mp.mp.dps = 80
    tau = 1.25
    # Keep the effective symbol exponent moderate so the finite-rank
    # convergence is visible before high-precision terms become enormous.
    shape = {5: 0.01, 7: -0.005, 9: 0.002}
    offsets = range(-2, 3)
    for lam in (1 / 40, 1 / 80, 1 / 160, 1 / 320):
        errors = []
        for p in offsets:
            for q in offsets:
                errors.append(abs(gram_entry(lam, tau, shape, p, q) - limiting_entry(tau, shape, p - q)))
        if lam == 1 / 40:
            coarse = max(errors)
        else:
            assert max(errors) < coarse
    assert max(errors) < 0.10
    print("R152_BULK_ENTRYWISE_CONVERGENCE_PASSED")


def check_toeplitz_positivity() -> None:
    tau = 1.25
    for shape in ({5: 0.01}, {5: -0.01, 7: 0.005}, {5: 0.008, 9: -0.004, 11: 0.001}):
        offsets = list(range(-5, 6))
        matrix = np.array(
            [[limiting_entry(tau, shape, p - q) for q in offsets] for p in offsets],
            dtype=float,
        )
        matrix = (matrix + matrix.T) / 2
        assert np.linalg.eigvalsh(matrix)[0] > 0
    print("R152_LIMIT_TOEPLITZ_POSITIVITY_PASSED")


def main() -> None:
    check_entrywise_convergence()
    check_toeplitz_positivity()
    print("R152_SCOPE_EXPLICIT: finite-support local bulk only; edge and growing-support regimes remain open")
    print("R152_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
