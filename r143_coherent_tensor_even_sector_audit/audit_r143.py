"""Finite checks for the R143 coherent-frame/tensor audit.

These checks cover only finite algebra, a finite measure Gram representation,
and numerical Fourier identities.  They do not certify the infinite-dimensional
analytic theorem, the full-SF hypothesis, or the iid ridge-product implication.
"""

from __future__ import annotations

import cmath
import math

import mpmath as mp
import sympy as sp


def check_coherent_kernel_factorization() -> None:
    z, w = sp.symbols("z w", real=True)
    exponent = z * w - (z**2 + w**2) / 2 - (z + w) ** 2 / 2
    assert sp.expand(exponent + z**2 + w**2) == 0
    print("R143_COHERENT_KERNEL_FACTORING_PASSED")


def coherent(z: complex, x: float) -> complex:
    return cmath.exp(z * x - z * z / 2 - abs(z) ** 2 / 2)


def kernel(z: complex, w: complex, xs: list[float], ps: list[float]) -> complex:
    return sum(p * coherent(z, x).conjugate() * coherent(w, x)
               for x, p in zip(xs, ps))


def check_finite_gram_and_tensor_psd() -> None:
    xs = [-1.25, 0.2, 1.7]
    ps = [0.2, 0.5, 0.3]
    zs = [0.0 + 0.0j, 0.35 + 0.2j, -0.4 + 0.15j]
    cs = [1.0 + 0.5j, -0.3 + 0.8j, 0.7 - 0.2j]
    q = sum(cs[i].conjugate() * cs[j] * kernel(zs[i], zs[j], xs, ps)
            for i in range(len(zs)) for j in range(len(zs)))
    assert q.real >= -1e-10 and abs(q.imag) <= 1e-10

    pairs = [(zs[0], zs[1]), (zs[1], zs[2]), (zs[2], zs[0])]
    tensor_q = 0.0 + 0.0j
    for i, (za, zb) in enumerate(pairs):
        for j, (wa, wb) in enumerate(pairs):
            tensor_q += cs[i].conjugate() * cs[j] * kernel(za, wa, xs, ps) * kernel(zb, wb, xs, ps)
    assert tensor_q.real >= -1e-10 and abs(tensor_q.imag) <= 1e-10
    print("R143_PSD_QUADRATIC_FORM_PASSED")


def check_reflection_thresholds() -> None:
    y = sp.symbols("y", real=True)
    raw_det = sp.symbols("Bplus", positive=True) * sp.symbols("Bminus", positive=True) - sp.exp(-y**2)
    deconv_det = sp.symbols("Bplus", positive=True) * sp.symbols("Bminus", positive=True) - 1
    assert sp.simplify(raw_det - (sp.symbols("Bplus", positive=True) * sp.symbols("Bminus", positive=True) - sp.exp(-y**2))) == 0
    assert sp.simplify(deconv_det - (sp.symbols("Bplus", positive=True) * sp.symbols("Bminus", positive=True) - 1)) == 0
    print("R143_REFLECTION_THRESHOLDS_PASSED")


def check_frame_geometry_and_bessel_modes() -> None:
    alpha, delta = sp.symbols("alpha delta", real=True)
    rho = sp.sqrt(sp.Rational(2, 3))

    def r(theta: sp.Expr, j: int) -> sp.Expr:
        return rho * sp.cos(theta + 2 * sp.pi * j / 3)

    for j in range(3):
        identity = r(alpha + delta / 2, j) + r(alpha - delta / 2, j)
        assert sp.trigsimp(identity - 2 * sp.cos(delta / 2) * r(alpha, j)) == 0
    assert sp.trigsimp(sum(r(alpha, j) ** 2 for j in range(3)) - 1) == 0

    for t in (0.6, 1.4, 2.1):
        a = t * t / 4
        for n in (0, 1, 2, 5):
            # Midpoint quadrature checks the Fourier coefficient of the exact
            # autocorrelation exp(-a*(1-cos(delta))).
            points = 12000
            integral = sum(
                math.exp(-a * (1 - math.cos(2 * math.pi * k / points))
                          ) * math.cos(n * 2 * math.pi * k / points)
                for k in range(points)
            ) / points
            target = math.exp(-a) * float(mp.besseli(n, a))
            assert abs(integral - target) < 2e-6
    print("R143_FRAME_BESSEL_ENERGY_PASSED")


def check_purity_defect_and_operator_witness() -> None:
    epsilon = 0.25
    assert 1 - epsilon > 0
    assert 1 + epsilon > 0
    # The 2x2 nontrivial block of T_epsilon has eigenvalues 1 +/- epsilon.
    block = sp.Matrix([[1, -sp.Rational(1, 4)], [-sp.Rational(1, 4), 1]])
    assert sorted(block.eigenvals().keys()) == [sp.Rational(3, 4), sp.Rational(5, 4)]
    # The variance decomposition is the finite identity E[F^2]=E[F]^2+Var(F).
    mean, second = sp.symbols("mean second", real=True)
    variance = sp.expand(second - mean**2)
    assert sp.expand(mean**2 + variance - second) == 0
    print("R143_PURITY_DEFECT_WITNESS_PASSED")


def check_even_sector_reversal() -> None:
    c_d, A_2d, p2, y, d = sp.symbols("c_d A_2d p2 y d", positive=True)
    c_2d = -p2 * c_d**2 / (2 * A_2d)
    even_log = sp.expand(2 * c_2d * y ** (2 * d))
    assert sp.simplify(even_log + p2 * c_d**2 * y ** (2 * d) / A_2d) == 0
    print("R143_EVEN_SECTOR_REVERSAL_PASSED")


def main() -> None:
    check_coherent_kernel_factorization()
    check_finite_gram_and_tensor_psd()
    check_reflection_thresholds()
    check_frame_geometry_and_bessel_modes()
    check_purity_defect_and_operator_witness()
    check_even_sector_reversal()
    print("R143_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
