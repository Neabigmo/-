from __future__ import annotations
import itertools
import json
from pathlib import Path
import sympy as sp
from common import result_dir

def D(expr, r):
    return sp.expand(sum(sp.diff(expr, r[k])*r[k+1] for k in range(len(r)-1)))

def hlog(r):
    return (r[1] + r[0]**2) / 2

def heat_r(r, k):
    e = hlog(r)
    for _ in range(k+1):
        e = D(e, r)
    return sp.expand(e)

def certificate(target, r, max_degree=3, max_index=5):
    mons = []
    for degree in range(max_degree + 1):
        for exps in itertools.product(range(degree + 1), repeat=max_index):
            if sum(exps) == degree:
                mons.append(sp.prod(r[i]**exps[i] for i in range(max_index)))
    coeff = sp.symbols("a:" + str(len(mons)))
    g = sum(a*m for a, m in zip(coeff, mons))
    poly = sp.Poly(sp.expand(D(g, r) + 3*r[0]*g - target), *r)
    equations = [v for _, v in poly.terms()]
    solutions = sp.linsolve(equations, coeff)
    return mons, solutions


def certificate_mod_relation(target, relation, r, max_degree_g=4, max_degree_h=1, max_index=6):
    """Find Dg+3*rho*g = target modulo the declared F''' relation."""
    def monomials(max_degree):
        mons = []
        for degree in range(max_degree + 1):
            for exps in itertools.product(range(degree + 1), repeat=max_index):
                if sum(exps) == degree:
                    mons.append(sp.prod(r[i]**exps[i] for i in range(max_index)))
        return mons

    gm = monomials(max_degree_g)
    hm = monomials(max_degree_h)
    a = sp.symbols("g0:" + str(len(gm)))
    b = sp.symbols("h0:" + str(len(hm)))
    g = sum(x*m for x, m in zip(a, gm))
    h = sum(x*m for x, m in zip(b, hm))
    expr = sp.expand(D(g, r) + 3*r[0]*g - target - h*relation)
    poly = sp.Poly(expr, *r)
    equations = [v for _, v in poly.terms()]
    solutions = sp.linsolve(equations, (*a, *b))
    return gm, hm, solutions

def main():
    tau = sp.symbols("tau", positive=True)
    r = sp.symbols("r0:9")
    rho, c, rho2 = r[0], r[1], r[2]
    G = tau*c + 1
    lhs = sp.expand(tau * (2*G*(c + tau*heat_r(r, 1))
                           + G**2*(sp.Rational(3, 2)*(c + rho**2) + 1/tau)))
    rhs1 = sp.expand(-tau**3*rho2**2 + 4*G**3 + 3*tau*rho**2*G**2 - 3*G**2)
    diff1 = sp.expand(lhs-rhs1)
    mons1, sol1 = certificate(diff1, r)
    assert sol1 != sp.EmptySet
    sol1_tuple = next(iter(sol1))
    coeff1 = list(sol1_tuple)
    witness1 = sp.expand(sum(a*m for a, m in zip(coeff1, mons1)))
    assert sp.expand(D(witness1, r) + 3*r[0]*witness1 - diff1) == 0

    # F''' target relation, expressed by p^(k)/p Bell polynomials.
    q = [sp.Integer(1)]
    for _ in range(6):
        q.append(sp.expand(D(q[-1], r) + rho*q[-1]))
    f3 = sp.expand(sp.Rational(3, 8)*q[6] + sp.Rational(9, 4)*q[2]*q[4] + sp.Rational(3, 4)*q[2]**3)
    target_f3 = sp.expand(f3 + 6/tau**3)
    rhs2 = sp.expand(sp.Rational(9, 5)*tau**3*rho**6 - 1 - 9*G**2 - 6*tau*rho**2*G**2)
    diff2 = sp.expand(lhs-rhs2)
    # Include the declared F''' relation in the certificate equations.  The
    # previous version tested total derivatives only, which was not the
    # advertised Candidate-2 audit.  Clear tau denominators first so the
    # relation is an honest polynomial identity in the jet variables.
    scaled_diff2 = sp.expand(tau**3 * diff2)
    scaled_f3_relation = sp.expand(tau**3 * target_f3)
    mons_g, mons_h, sol2 = certificate_mod_relation(
        scaled_diff2, scaled_f3_relation, r, max_degree_g=4, max_degree_h=1, max_index=6
    )
    candidate2_found = sol2 != sp.EmptySet
    out = {
        "status": "LOCAL_IDENTITIES_INSUFFICIENT_FOR_CANDIDATE_2",
        "candidate_1": "VERIFIED_BY_TOTAL_DERIVATIVE",
        "candidate_1_certificate_exists": True,
        "candidate_1_total_derivative_witness": str(witness1),
        "corrected_formula": "tau*delta_prime=-E[U^2]+4E[G^3]+3E[R^2G^2]-3delta",
        "candidate_2": "NOT_VERIFIED",
        "candidate_2_certificate_search": "total derivative modulo the declared F''' relation; g degree<=4, multiplier degree<=1",
        "candidate_2_relation_included": True,
        "candidate_2_certificate_found": candidate2_found,
        "candidate_2_density_claim": False,
        "candidate_2_exact_residual_terms": len(sp.Poly(diff2, *r).terms()),
        "target_F3_relation_terms": len(sp.Poly(target_f3, *r).terms()),
        "candidate_2_scaled_relation_terms": len(sp.Poly(scaled_f3_relation, *r).terms()),
        "interpretation": "No density counterexample; candidate 2 requires a separate proof or correction.",
    }
    path = result_dir() / "third_order_defect.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("THIRD_ORDER_CANDIDATE_1_CERTIFIED_CANDIDATE_2_UNVERIFIED", path)

if __name__ == "__main__":
    main()
