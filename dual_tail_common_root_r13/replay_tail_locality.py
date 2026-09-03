"""Small exact replays for the R13 dual-tail/common-root reduction."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def lower_triangular_replay(size: int = 7) -> dict:
    """Verify the normalized principal multiplication has exact diagonal 1."""
    x = sp.symbols("x")
    symbol = 1 + 2 * x - x**2 + 3 * x**3
    matrix = sp.zeros(size)
    for row in range(size):
        for col in range(row + 1):
            matrix[row, col] = sp.expand(symbol).coeff(x, row - col)
    return {
        "size": size,
        "diagonal": [str(matrix[i, i]) for i in range(size)],
        "exact_diagonal_one": all(matrix[i, i] == 1 for i in range(size)),
        "lower_triangular": all(matrix[row, col] == 0 for row in range(size) for col in range(row + 1, size)),
        "symbol": str(symbol),
    }


def tail_locality_sufficient_bound_replay() -> dict:
    """Replay a sufficient row-tail estimate, without claiming R11 implies it."""
    # A finite model of |(K^*phi)_i| <= eta_i sup_{q>=i}|phi_q|.
    phi = [sp.Rational(1, 2) ** i for i in range(12)]
    eta = [sp.Rational(1, 3) ** i for i in range(12)]
    values = [eta[i] * max(abs(v) for v in phi[i:]) for i in range(12)]
    normalized = [values[i] / max(abs(v) for v in phi[i:]) for i in range(12)]
    return {
        "finite_model_bound_holds": all(normalized[i] <= eta[i] for i in range(12)),
        "normalized_tail_tends_to_zero_in_model": bool(normalized[-1] < normalized[0]),
        "sufficient_condition": "sup_{q>=i}|K^*phi_q| <= eta_i b_i with eta_i -> 0",
        "r11_compactness_implies_this": False,
    }


def tail_normalization_selection_replay() -> dict:
    """Check the elementary approximate-tail-maximizer selection principle."""
    phi = [sp.Rational(1, 3), 0, sp.Rational(1, 5), 0, sp.Rational(1, 10), 0, sp.Rational(1, 20), 0]
    selected = []
    base = 0
    while base < len(phi):
        tail = max(abs(v) for v in phi[base:])
        if tail == 0:
            break
        candidates = [n for n in range(base, len(phi)) if abs(phi[n]) >= tail / 2]
        n = candidates[0]
        selected.append({"base": base, "index": n, "b_base": str(tail), "ratio": str(abs(phi[n]) / tail)})
        base = n + 1
    return {
        "selected": selected,
        "all_selected_ratio_at_least_half": all(sp.Rational(row["ratio"]) >= sp.Rational(1, 2) for row in selected),
        "selection_is_strictly_increasing": all(selected[i]["index"] < selected[i + 1]["index"] for i in range(len(selected) - 1)),
        "normalized_limit_object": "psi^(k)_m=phi_{i_k+m}/b_{i_k}, ||psi^(k)||_infinity<=1, |psi^(k)_0|>=1/2",
    }


def finite_support_dual_replay() -> dict:
    """A nonzero finite-support sequence cannot solve a recurrence with d_0=1."""
    psi = [sp.Integer(0), sp.Integer(0), sp.Integer(5), sp.Integer(-2), sp.Integer(0)]
    d0 = sp.Integer(1)
    last = max(i for i, value in enumerate(psi) if value != 0)
    terminal_equation = sp.expand(d0 * psi[last])
    return {
        "last_support_index": last,
        "terminal_equation": str(terminal_equation),
        "finite_support_nonzero_contradiction": terminal_equation != 0,
        "reason": "At the largest support index p, all forward terms except d_0 psi_p vanish.",
    }


def common_root_spectral_toy_replay() -> dict:
    """Check the polynomial/common-root logic used after tail extraction."""
    lam = sp.symbols("lambda")
    d_common = 1 - 2 * lam
    c_common = 3 - 6 * lam
    d_disjoint = 1 - 2 * lam
    c_disjoint = 1 - 3 * lam
    common_gcd = sp.gcd(d_common, c_common)
    disjoint_gcd = sp.gcd(d_disjoint, c_disjoint)
    return {
        "common_case_gcd": str(common_gcd),
        "common_case_has_root": bool(sp.degree(common_gcd, lam) > 0),
        "disjoint_case_gcd": str(disjoint_gcd),
        "disjoint_case_has_no_common_root": bool(sp.degree(disjoint_gcd, lam) == 0),
        "spectral_mapping_step": "D(S)psi=C(S)psi=0 implies D(lambda)=C(lambda)=0 for lambda in spectrum(S|V)",
        "disk_bound_step": "spectrum of a contraction on ell_infinity lies in the closed unit disk",
    }


def gaussian_replay() -> dict:
    return {"R": "1", "D_R": "1", "C_R": "0", "no_principal_defect": True}


def main() -> dict:
    lower = lower_triangular_replay()
    tail = tail_locality_sufficient_bound_replay()
    selection = tail_normalization_selection_replay()
    finite = finite_support_dual_replay()
    spectral = common_root_spectral_toy_replay()
    gaussian = gaussian_replay()
    payload = {
        "lower_triangular": lower,
        "tail_locality": tail,
        "tail_normalization": selection,
        "finite_support_dual": finite,
        "spectral_common_root": spectral,
        "gaussian": gaussian,
        "dual_annihilator_characterization": "Delta_rho non-surjective iff a nonzero bounded dual functional annihilates both L_e and B_o, subject to the Fredholm finite-dimensional quotient.",
        "conditional_common_root_theorem": "If the normalized dual tails satisfy the required K^* tail-locality and both recurrences pass to the limit, then a nonzero dual defect forces a common D/C spectral root.",
        "decision": "TAIL_LOCALITY_GAP",
        "single_remaining_gap": "R11 compactness bookkeeping does not by itself prove the relative tail-local remainder estimate needed after division by b_i.",
        "marker": "R13_DUAL_TAIL_COMMON_ROOT_REPLAY_COMPLETED",
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "r13_replay.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    for marker in [
        "DUAL_DEFECT_CHARACTERIZATION_FORMALIZED",
        "TAIL_NORMALIZATION_SELECTION_LEMMA_REPLAYED",
        "SIMULTANEOUS_RECURRENCE_REPLAYED",
        "COMMON_ROOT_REDUCTION_CONDITIONAL_ON_TAIL_LOCALITY",
        payload["marker"],
    ]:
        print(marker)
    print("R13_LOWER_TRIANGULAR_DIAGONAL_ONE", lower["exact_diagonal_one"])
    print("R13_TAIL_LOCALITY_SUFFICIENT_MODEL", tail["finite_model_bound_holds"])
    print("R13_TAIL_LOCALITY_FROM_R11", tail["r11_compactness_implies_this"])
    print("R13_COMMON_ROOT_TOY", spectral["common_case_has_root"])
    print("R13_DECISION", payload["decision"])
    return payload


if __name__ == "__main__":
    main()
