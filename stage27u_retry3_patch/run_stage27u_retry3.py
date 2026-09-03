#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

PATCH = Path(__file__).resolve().parent
REPO = PATCH.parent
PKG_ROOT = REPO / "chi2_n3_ou_coherent_stage27u_retry2_2026-09-03"
PKG_PY = PKG_ROOT / "python"

sys.path.insert(0, str(PKG_PY))
sys.path.insert(0, str(PATCH))

import outer_minimax as om
import run_stage27u_preflight as pre
from gradient_audit_retry3 import (
    gradient_audit_rows_retry3,
    gradient_spot_check_retry3,
)

# Patch only audit behavior. Core Fock, Gram, NNQP, objective, ridge, and
# campaign equations remain the byte-identical retry2-fix1 implementation.
om.gradient_spot_check = gradient_spot_check_retry3
pre.gradient_audit_rows = gradient_audit_rows_retry3

# Import campaign only after monkeypatching outer_minimax. Its imported
# local_search/multistart functions resolve gradient_spot_check through the
# patched outer_minimax module globals at runtime.
import run_stage27u_campaign as campaign
import run_stage27u as base

base.run_preflight = pre.run_preflight
base.run_campaign = campaign.run_campaign

if __name__ == "__main__":
    base.main()
