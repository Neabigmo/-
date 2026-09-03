import json
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).parents[1]))

from audit_symbol_theorem import main as audit_main
from derive_angular_moment import beta_moment, direct_moment
from derive_student_kernel import direct_kernel, fixed_band_rows, student_kernel
from replay_normalization import main as normalization_main


def test_gaussian_normalization():
    normalization_main()
    payload = json.loads((Path(__file__).parents[1] / "results" / "normalization.json").read_text(encoding="utf-8"))
    assert payload["fock_R"] == "1"
    assert payload["D_R"] == "1"


def test_student_moments_and_kernel_integrals():
    for n in (4, 6):
        for degree in range(5):
            assert sp.simplify(beta_moment(n, degree) - direct_moment(n, degree)) == 0
    for degree in (4, 6):
        for j in range(3):
            for k in range(3 - j):
                assert sp.simplify(student_kernel(j, k, degree) - direct_kernel(j, k, degree)) == 0


def test_fixed_band_limits():
    assert all(row["limit_residual"] == "0" for row in fixed_band_rows())


def test_published_audit():
    audit_main()
    payload = json.loads((Path(__file__).parents[1] / "results" / "r10_audit.json").read_text(encoding="utf-8"))
    assert payload["exact_replays_pass"] is True
    assert payload["marker"] == "R10_STAGE7_STUDENT_KERNEL_AUDIT_COMPLETED"
    assert payload["decision"] == "STUDENT_KERNEL_CERTIFIED_OPERATOR_GAP_REMAINS"
