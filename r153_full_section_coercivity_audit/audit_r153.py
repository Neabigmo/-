"""Independent finite audit of the R153 full-section coercivity mechanism.

The checks are intentionally modest: exact finite coefficient identities,
quadrature exactness/normalisation, explicit Hermite bounds, and a concrete
positive entire model.  They do not certify the uniform hypotheses for the
original infinite-dimensional sparse/full-SF problem.
"""

from __future__ import annotations

import math
from typing import Iterable, Mapping

import mpmath as mp
import numpy as np


MP = mp.mpf


def polynomial_exp_coeffs(shape: Mapping[int, str | float], degree: int) -> list[mp.mpf]:
    """Taylor coefficients of exp(sum shape[k] z**k), through ``degree``."""
    p = [MP("0") for _ in range(degree + 1)]
    for k, value in shape.items():
        if 0 <= k <= degree:
            p[k] = MP(str(value))
    coeff = [MP("0") for _ in range(degree + 1)]
    coeff[0] = MP("1")
    # If E'=P'E, then n E_n=sum_{k=1}^n k P_k E_(n-k).
    for n in range(1, degree + 1):
        coeff[n] = sum(k * p[k] * coeff[n - k] for k in range(1, n + 1)) / MP(n)
    return coeff


def hermite_prob(k: int, x: mp.mpf) -> mp.mpf:
    """Probabilists' Hermite polynomial He_k(x), by its three-term recurrence."""
    if k == 0:
        return MP("1")
    if k == 1:
        return x
    h0, h1 = MP("1"), x
    for n in range(1, k):
        h0, h1 = h1, x * h1 - n * h0
    return h1


def generalized_hermite(k: int, lam: mp.mpf, y: mp.mpf) -> mp.mpf:
    """H_k^(lambda)(y)=lambda^(k/2) He_k(y/sqrt(lambda)), stably expanded."""
    total = MP("0")
    for r in range(k // 2 + 1):
        total += (
            (-1) ** r
            * MP(math.factorial(k))
            / (MP(2) ** r * MP(math.factorial(r)) * MP(math.factorial(k - 2 * r)))
            * lam**r
            * y ** (k - 2 * r)
        )
    return total


def kernel_gamma_entry(
    lam: mp.mpf, coeff: list[mp.mpf], m: int, n: int
) -> mp.mpf:
    """Coefficient of u^m/sqrt(m!) v^n/sqrt(n!) in exp(uv)E(sqrt(lam)(u+v))."""
    total = MP("0")
    for k, e_k in enumerate(coeff[: m + n + 1]):
        remainder = m + n - k
        if remainder < 0 or remainder % 2:
            continue
        r = remainder // 2
        left = k + m - n
        if left < 0 or left % 2:
            continue
        left //= 2
        if left > k:
            continue
        total += (
            e_k
            * lam ** (MP(k) / 2)
            * mp.sqrt(mp.factorial(m) * mp.factorial(n))
            / mp.factorial(r)
            * mp.binomial(k, left)
        )
    return total


def gh_nodes_weights(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Nodes/weights for standard Gaussian expectation."""
    nodes, weights = np.polynomial.hermite_e.hermegauss(n)
    return nodes, weights / math.sqrt(2 * math.pi)


def density_value(lam: mp.mpf, coeff: list[mp.mpf], M: int, x: mp.mpf) -> mp.mpf:
    return sum(coeff[k] * lam ** (MP(k) / 2) * hermite_prob(k, x) for k in range(2 * M + 1))


def check_exact_density_identity() -> None:
    mp.mp.dps = 70
    lam = MP("0.037")
    M = 5
    coeff = polynomial_exp_coeffs({2: "0.03", 5: "-0.011", 7: "0.004"}, 2 * M)
    nodes, weights = gh_nodes_weights(2 * M + 1)
    for m in range(M + 1):
        for n in range(M + 1):
            quadrature = MP("0")
            for x_float, w_float in zip(nodes, weights):
                x = MP(str(x_float))
                quadrature += (
                    MP(str(w_float))
                    * density_value(lam, coeff, M, x)
                    * hermite_prob(m, x)
                    * hermite_prob(n, x)
                    / mp.sqrt(mp.factorial(m) * mp.factorial(n))
                )
            exact = kernel_gamma_entry(lam, coeff, m, n)
            assert abs(quadrature - exact) < MP("2e-11"), (m, n, quadrature, exact)
    print("R153_EXACT_DENSITY_NORMALISATION_PASSED")


def check_full_section_degree_count() -> None:
    for M in range(0, 20):
        N = 2 * M + 1
        assert 2 * N - 1 >= 4 * M
        assert 2 * M + 2 * M <= 4 * M
    print("R153_GAUSS_HERMITE_DEGREE_COUNT_PASSED")


def check_gauss_node_envelope() -> None:
    for N in range(1, 80):
        nodes, _ = gh_nodes_weights(N)
        assert float(np.max(np.abs(nodes))) < 2 * math.sqrt(N)
    print("R153_GAUSS_NODE_ENVELOPE_PASSED")


def check_generalized_hermite_formula_and_error() -> None:
    mp.mp.dps = 80
    for lam in (MP("0.001"), MP("0.017"), MP("0.11")):
        for y in (MP("-2.1"), MP("-0.3"), MP("0"), MP("1.7"), MP("2.4")):
            for k in range(0, 25):
                h = generalized_hermite(k, lam, y)
                direct = lam ** (MP(k) / 2) * hermite_prob(k, y / mp.sqrt(lam))
                assert abs(h - direct) < MP("1e-45") * max(MP("1"), abs(h), abs(direct))

    # Audit the webpage's compact error envelope on |y|<=R_tau.
    tau = MP("0.35")
    R = 2 * mp.sqrt(2 * tau + 1)
    A = max(MP("1"), R)
    for lam in (MP("0.0005"), MP("0.003"), MP("0.02")):
        for k in range(1, 32):
            for j in range(9):
                y = -R + 2 * R * MP(j) / MP(8)
                lhs = abs(generalized_hermite(k, lam, y) - y**k)
                rhs = A**k * (mp.exp(lam * k**2 / (2 * A**2)) - 1)
                assert lhs <= rhs * (1 + MP("1e-35")), (k, lam, y, lhs, rhs)
    print("R153_GENERALIZED_HERMITE_BOUND_PASSED")


def check_compact_truncation_bound() -> None:
    mp.mp.dps = 70
    tau = MP("0.35")
    R = 2 * mp.sqrt(2 * tau + 1)
    A = max(MP("1"), R)
    S = MP("4.0")
    alpha = MP("0.0007")
    # E(z)=exp(alpha z^5), so B is a valid circle bound on |z|=S.
    B = mp.exp(abs(alpha) * S**5)
    D = A * mp.exp(tau / A**2)
    assert S > D
    ratio = D / S
    tail_ratio = A / S

    def bound(lam: mp.mpf, M: int) -> mp.mpf:
        first = lam * B / (2 * A**2) * ratio * (1 + ratio) / (1 - ratio) ** 3
        second = B * tail_ratio ** (2 * M + 1) / (1 - tail_ratio)
        return first + second

    coeff = polynomial_exp_coeffs({5: str(alpha)}, 400)
    active = [k for k, value in enumerate(coeff) if value]
    for lam in (MP("0.01"), MP("0.005"), MP("0.002")):
        M = max(1, int(mp.floor(tau / lam)))
        max_error = MP("0")
        for j in range(101):
            y = -R + 2 * R * MP(j) / MP(100)
            truncated = sum(
                coeff[k] * generalized_hermite(k, lam, y)
                for k in active
                if k <= 2 * M
            )
            target = mp.exp(alpha * y**5)
            max_error = max(max_error, abs(truncated - target))
        assert max_error <= bound(lam, M) * (1 + MP("1e-20")), (lam, M, max_error, bound(lam, M))
    print("R153_COMPACT_TRUNCATION_BOUND_PASSED")


def check_positive_full_section_model() -> None:
    """Numerically exhibit the conditional margin for one fixed positive entire E."""
    mp.mp.dps = 70
    tau = MP("0.35")
    R = 2 * mp.sqrt(2 * tau + 1)
    alpha = MP("0.0007")
    m_tau = mp.exp(-abs(alpha) * R**5)
    coeff = polynomial_exp_coeffs({5: str(alpha)}, 2 * 80)
    for lam_float in (0.05, 0.02, 0.01, 0.005):
        lam = MP(str(lam_float))
        M = max(1, math.floor(float(tau / lam)))
        nodes, _ = gh_nodes_weights(2 * M + 1)
        node_values = [density_value(lam, coeff, M, MP(str(x))) for x in nodes]
        assert min(node_values) >= m_tau / 2, (lam, M, min(node_values), m_tau / 2)
    print("R153_CONDITIONAL_NODE_POSITIVITY_MODEL_PASSED")


def check_r132_exponent_algebra() -> None:
    for tau in (MP("0"), MP("0.1"), MP("1"), MP("7.25")):
        R = 2 * mp.sqrt(2 * tau + 1)
        assert abs(R**2 / 2 - (4 * tau + 2)) < MP("1e-60")
    print("R153_R132_COMPACT_GAP_EXPONENT_PASSED")


def main() -> None:
    check_exact_density_identity()
    check_full_section_degree_count()
    check_gauss_node_envelope()
    check_generalized_hermite_formula_and_error()
    check_compact_truncation_bound()
    check_positive_full_section_model()
    check_r132_exponent_algebra()
    print("R153_SCOPE_EXPLICIT: finite/algebraic audit only; uniform branch hypotheses and original rigidity remain open")
    print("R153_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
