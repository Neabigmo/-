"""Finite audit of the R154 Christoffel localisation criterion."""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad
from scipy.special import eval_hermitenorm


SQRT_2PI = math.sqrt(2.0 * math.pi)


def psi(n: int, x: float) -> float:
    return float(eval_hermitenorm(n, x) / math.sqrt(math.factorial(n)))


def gaussian_density(x: float) -> float:
    return math.exp(-0.5 * x * x) / SQRT_2PI


def interval_gram(M: int, left: float, right: float) -> np.ndarray:
    A = np.zeros((M + 1, M + 1), dtype=float)
    for m in range(M + 1):
        for n in range(m, M + 1):
            value = quad(
                lambda x: psi(m, x) * psi(n, x) * gaussian_density(x),
                left,
                right,
                epsabs=2e-12,
                epsrel=2e-12,
                limit=200,
            )[0]
            A[m, n] = value
            A[n, m] = value
    return A


def check_concentration_matrix() -> None:
    M = 10
    A = interval_gram(M, -1.25, 1.25)
    full = interval_gram(M, -12.0, 12.0)
    assert np.linalg.eigvalsh(A)[0] >= -3e-11
    assert np.max(np.abs(full - np.eye(M + 1))) < 3e-10
    theta = float(np.linalg.eigvalsh(A)[-1])
    assert 0.0 < theta < 1.0
    print("R154_CONCENTRATION_MATRIX_PASSED")


def check_exact_loewner_criterion() -> None:
    M = 12
    A = interval_gram(M, -1.5, 1.5)
    theta = float(np.linalg.eigvalsh(A)[-1])
    a, b = 4.0, 1.0
    # The signed density is -a on I and +b outside I.
    gram = b * np.eye(M + 1) - (a + b) * A
    bound = b - (a + b) * theta
    eigmin = float(np.linalg.eigvalsh(gram)[0])
    assert abs(eigmin - bound) < 2e-10
    assert theta > b / (a + b)
    assert eigmin < 0.0
    print("R154_CHRISTOFFEL_NEGATIVE_DIRECTION_PASSED")


def check_pointwise_negative_is_not_sufficient() -> None:
    M = 10
    A = interval_gram(M, -0.08, 0.08)
    theta = float(np.linalg.eigvalsh(A)[-1])
    # g=-1 on a tiny interval and +1 elsewhere.  It has a negative pointwise
    # region, but the degree-M Gram remains positive when theta<1/2.
    gram = np.eye(M + 1) - 2.0 * A
    eigmin = float(np.linalg.eigvalsh(gram)[0])
    assert theta < 0.5
    assert eigmin > 0.0
    print("R154_POINTWISE_NEGATIVITY_NOT_SUFFICIENT_PASSED")


def check_scaled_interval_bookkeeping() -> None:
    # The scaled interval y in [y0-h,y0+h] becomes this x interval under
    # y=sqrt(lambda)x.  This is the exact conversion needed in supercritical
    # experiments; no hidden change of Gaussian measure is made.
    lam, y0, half_width = 0.04, 2.5, 0.25
    left = (y0 - half_width) / math.sqrt(lam)
    right = (y0 + half_width) / math.sqrt(lam)
    assert abs(math.sqrt(lam) * left - (y0 - half_width)) < 1e-14
    assert abs(math.sqrt(lam) * right - (y0 + half_width)) < 1e-14
    assert right > left
    print("R154_SCALED_INTERVAL_BOOKKEEPING_PASSED")


def main() -> None:
    check_concentration_matrix()
    check_exact_loewner_criterion()
    check_pointwise_negative_is_not_sufficient()
    check_scaled_interval_bookkeeping()
    print("R154_SCOPE_EXPLICIT: exact finite criterion only; supercritical tail and genuine branch remain open")
    print("R154_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()

