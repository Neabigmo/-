from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from audit_r14 import main  # noqa: E402
from replay_factor_identity import (  # noqa: E402
    probability_countermodels,
    quartet_factor_replay,
    resonance_replay,
)


def test_exact_probability_countermodels():
    data = probability_countermodels()
    assert data["bernoulli_symmetric_zero"]
    assert data["three_point_symmetric_zero"]


def test_formal_resonance_data_is_consistent():
    assert resonance_replay()["resonance_data_consistent"]


def test_quartet_factor_is_exact():
    assert quartet_factor_replay()["identity_holds"]


def test_audit_is_conservative():
    data = main()
    assert data["all_exact_replays_pass"]
    assert data["decision"] == "FOCK_ZERO_RESONANCE_LEMMA_CERTIFIED_PROBABILITY_BRIDGE_REMAINS"
