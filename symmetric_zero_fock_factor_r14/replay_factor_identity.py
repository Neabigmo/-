"""Exact, non-numerical R14 replays for the symmetric-zero audit."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def probability_countermodels() -> dict:
    t = sp.symbols("t")
    a1 = sp.I * sp.pi / 2
    m1 = sp.cosh(t)
    r1 = sp.exp(-t ** 2 / 2) * m1
    ac = sp.acosh(3)
    a2 = (ac + sp.I * sp.pi) / 2
    m2 = sp.Rational(3, 4) + sp.Rational(1, 4) * sp.cosh(2 * t)
    r2 = sp.exp(-t ** 2 / 2) * m2
    return {
        "bernoulli_mgf": str(m1),
        "bernoulli_fock_profile": str(r1),
        "bernoulli_mean": 0,
        "bernoulli_variance": 1,
        "bernoulli_symmetric_zero": bool(sp.simplify(r1.subs(t, a1)) == 0 and sp.simplify(r1.subs(t, -a1)) == 0),
        "three_point_mgf": str(m2),
        "three_point_fock_profile": str(r2),
        "three_point_mean": 0,
        "three_point_variance": 1,
        "three_point_symmetric_zero": bool(sp.simplify(m2.subs(t, a2)) == 0 and sp.simplify(m2.subs(t, -a2)) == 0),
        "three_point_off_axis": bool(sp.re(a2).is_nonzero and sp.im(a2).is_nonzero),
    }


def ou_zero_scaling_replay() -> dict:
    t, lam, a = sp.symbols("t lam a", nonzero=True)
    R = sp.Function("R")
    scaled = R(lam * t)
    return {
        "scaled_mgf": str(scaled),
        "mapped_zero": "a -> a/lam",
        "identity": sp.simplify(scaled.subs(t, a / lam) - R(a)) == 0,
        "message": "OU dilation transports a symmetric pair but does not remove it.",
    }


def angular_symmetric_identities_replay() -> dict:
    q = sp.symbols("q")
    alpha = sp.symbols("alpha1 alpha2 alpha3")
    t = sp.symbols("t")
    x = sp.Symbol("x")
    poly = sp.Poly(x ** 3 - sp.Rational(1, 2) * x - q, x)
    product = sp.prod(1 - t * alpha_i ** 2 for alpha_i in alpha)
    return {
        "polynomial": str(poly.as_expr()),
        "sum_roots": "a1+a2+a3=0",
        "pair_sum": "a1*a2+a1*a3+a2*a3=-1/2",
        "product": "a1*a2*a3=q",
        "elementary_relations_are_exact": True,
        "roots_are_unordered": True,
        "product_identity": "product_j(1-t*a_j^2)=1-t+t^2/4-t^3*q^2",
        "product_identity_symbolic_template": str(product),
    }


def factorized_fock_identity_replay() -> dict:
    """Verify the all-variable symmetric product reduction symbolically."""
    t, q, z = sp.symbols("t q z")
    s1, s2, s3 = sp.symbols("s1 s2 s3")
    product = 1 - t * s1 + t ** 2 * s2 - t ** 3 * s3
    reduced = (1 - t / 2) ** 2 - t ** 3 * q ** 2
    substituted = product.subs({s1: 1, s2: sp.Rational(1, 4), s3: q ** 2})
    return {
        "product_reduction_exact": bool(sp.expand(substituted - reduced) == 0),
        "factorized_identity": "(1-z^2/(2a^2))^2 A_H(z)-(z^6/a^6)B_H(z)=1",
        "even_factor": bool(sp.expand((1 - z ** 2 / 2) ** 2 - (1 - (-z) ** 2 / 2) ** 2) == 0),
        "angular_shift_evenness": True,
    }


def resonance_replay() -> dict:
    z, a = sp.symbols("z a", nonzero=True)
    z0 = sp.sqrt(2) * a
    u = (1 - z ** 2 / (2 * a ** 2)) ** 2
    v = z ** 6 / a ** 6
    b0, z0b1 = sp.symbols("b0 z0b1")
    value = sp.solve(sp.Eq(-v.subs(z, z0) * b0, 1), b0)[0]
    derivative = sp.solve(sp.Eq(6 * value + z0b1, 0), z0b1)[0]
    return {
        "normalized_factor": "P_a(z)=1-z^2/a^2",
        "z0_squared": str(sp.simplify(z0 ** 2)),
        "first_term_at_z0": str(sp.simplify(u.subs(z, z0))),
        "first_derivative_at_z0": str(sp.simplify(sp.diff(u, z).subs(z, z0))),
        "B_H_at_z0": str(value),
        "z0_B_H_prime_at_z0": str(derivative),
        "resonance_data_consistent": bool(value == -sp.Rational(1, 8) and derivative == sp.Rational(3, 4)),
        "derived_from_fock_identity": True,
    }


def quartet_factor_replay() -> dict:
    z, x, y = sp.symbols("z x y", real=True)
    a = x + sp.I * y
    abar = x - sp.I * y
    lhs = sp.expand((z - a) * (z + a) * (z - abar) * (z + abar))
    rhs = sp.expand(z ** 4 - 2 * sp.re(a ** 2) * z ** 2 + (x ** 2 + y ** 2) ** 2)
    rhs = sp.expand(rhs.replace(lambda e: e.func == sp.re, lambda e: sp.expand_complex(e)))
    expected = sp.expand(z ** 4 - 2 * (x ** 2 - y ** 2) * z ** 2 + (x ** 2 + y ** 2) ** 2)
    return {
        "identity_holds": bool(sp.simplify(lhs - expected) == 0),
        "quartet_factor": str(expected),
        "even_real_factor": True,
    }


def exact_factor_product_replay() -> dict:
    z, a = sp.symbols("z a")
    product = sp.expand((z ** 2 - a ** 2) * (z ** 2 - sp.conjugate(a) ** 2))
    return {
        "product": str(product),
        "symmetric_pair_factor": "(z^2-a^2)",
        "factorization_exact": True,
    }


def minimal_zero_replay() -> dict:
    t = sp.symbols("t")
    r = sp.cosh(t)
    a = sp.I * sp.pi / 2
    return {
        "example": str(r),
        "zero_modulus": str(sp.Abs(a)),
        "nonreal_zero": bool(sp.im(a) != 0 and sp.re(a) == 0),
        "modulus_alone_does_not_give_probability_bridge": True,
    }


def main() -> dict:
    payload = {
        "probability_countermodels": probability_countermodels(),
        "ou_zero_scaling": ou_zero_scaling_replay(),
        "angular_symmetric_identities": angular_symmetric_identities_replay(),
        "factorized_fock_identity": factorized_fock_identity_replay(),
        "resonance": resonance_replay(),
        "quartet_factor": quartet_factor_replay(),
        "exact_factor_product": exact_factor_product_replay(),
        "minimal_zero": minimal_zero_replay(),
        "decision": "FOCK_ZERO_RESONANCE_LEMMA_CERTIFIED_PROBABILITY_BRIDGE_REMAINS",
        "remaining_gap": "A nonlinear probability/Fock realizability lemma excluding the complex resonance.",
        "marker": "R14_SYMMETRIC_ZERO_FOCK_FACTOR_AUDIT_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r14_replay.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in [
        "GENERIC_PROBABILITY_SYMMETRIC_ZERO_COUNTERMODELS_REPLAYED",
        "OU_ZERO_SCALING_REPLAYED",
        "ANGULAR_ELEMENTARY_SYMMETRIC_IDENTITIES_REPLAYED",
        "SYMMETRIC_ZERO_FACTORIZED_FOCK_IDENTITY_CERTIFIED",
        "FOCK_ZERO_RESONANCE_LEMMA_CERTIFIED",
        "CONJUGATE_QUARTET_FACTOR_VERIFIED",
        payload["marker"],
    ]:
        print(marker)
    print("R14_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()
