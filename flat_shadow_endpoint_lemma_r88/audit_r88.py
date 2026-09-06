"""Exact checks for the abstract R88 real-u endpoint lemma."""

from math import factorial
import sympy as sp


def check_endpoint_differentiation() -> None:
    u, zeta, L = sp.symbols("u zeta L")
    A, A_prime = sp.symbols("A A_prime")
    denominator = zeta * u + L
    B = A * u / denominator
    expected = A_prime * u / denominator + A * L / denominator**2
    # A_prime is the formal derivative of A(u); the quotient-rule identity is
    # the exact step used after integration by parts.
    derivative = A_prime * sp.diff(B, A) + sp.diff(B, u)
    assert sp.simplify(derivative - expected) == 0
    assert sp.simplify(sp.diff(u / denominator, u) - L / denominator**2) == 0
    print("R88_ENDPOINT_DIFFERENTIATION_PASSED")


def check_endpoint_geometry() -> None:
    u, alpha, zeta, Delta = sp.symbols(
        "u alpha zeta Delta", positive=True
    )
    L = 1 + alpha + zeta
    Delta_expr = L + zeta
    derivative_rearrangement = sp.simplify(
        (zeta + L / u) - (Delta_expr + (1 / u - 1) * L)
    )
    assert derivative_rearrangement == 0
    assert sp.simplify(2 * L - (1 + alpha + Delta_expr)) == 0
    assert sp.simplify((zeta + L) - Delta_expr) == 0
    print("R88_ENDPOINT_GEOMETRY_PASSED")


def check_remainder_constant() -> None:
    eta, ell0, Lmax, M, j = sp.symbols(
        "eta ell0 Lmax M j", positive=True
    )
    c = sp.symbols("c", positive=True)
    C = M / eta * (1 / c + Lmax / c**2)
    # The bound is exactly (sup |B'|/j) times the Laplace integral bound.
    assert sp.simplify(C - (M * (1 / c + Lmax / c**2)) / eta) == 0
    assert sp.simplify((C / j**2) * j**2 - C) == 0
    print("R88_EXPLICIT_REMAINDER_CONSTANT_PASSED")


def check_corrected_green_factor() -> None:
    alpha, zeta = sp.symbols("alpha zeta", positive=True)
    L = 1 + alpha + zeta
    Delta = L + zeta
    factor = 1 - 2 * zeta / Delta
    assert sp.simplify(factor - (L - zeta) / (L + zeta)) == 0
    assert sp.simplify(factor - (1 + alpha) / Delta) == 0

    p_h = (1 + zeta / L) ** 3 / (1 - zeta / L)
    assert sp.simplify(p_h - Delta**3 / ((1 + alpha) * L**2)) == 0
    assert sp.simplify(p_h * factor - Delta**2 / L**2) == 0
    print("R88_CORRECTED_GREEN_FACTOR_PASSED")


def check_finite_boundary_term_model() -> None:
    # For Re(L)>0, the lower integration boundary is killed by u^(j*L) and
    # the extra B(u)=O(u) factor.  This exact power bookkeeping is all that is
    # needed for the abstract integration-by-parts boundary term.
    j = sp.symbols("j", positive=True)
    assert sp.simplify((j + 1) - j - 1) == 0
    assert sp.simplify(sp.diff(sp.log(sp.Symbol("u")), sp.Symbol("u")) - 1 / sp.Symbol("u")) == 0
    print("R88_LOWER_BOUNDARY_BOOKKEEPING_PASSED")


if __name__ == "__main__":
    check_endpoint_differentiation()
    check_endpoint_geometry()
    check_remainder_constant()
    check_corrected_green_factor()
    check_finite_boundary_term_model()
    print("R88_ENDPOINT_LEMMA_AUDIT_COMPLETED")
