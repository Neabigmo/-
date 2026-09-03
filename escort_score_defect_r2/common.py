from __future__ import annotations

import os
from pathlib import Path


def result_dir() -> Path:
    """Return the artifact directory, optionally redirected by a test run."""
    path = Path(os.environ.get("ESCORT_RESULTS_DIR", Path(__file__).resolve().parent / "results"))
    path.mkdir(parents=True, exist_ok=True)
    return path
