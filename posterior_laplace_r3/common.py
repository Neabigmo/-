from __future__ import annotations

import os
from pathlib import Path


def result_dir() -> Path:
    path = Path(os.environ.get("LAPLACE_RESULTS_DIR", Path(__file__).resolve().parent / "results"))
    path.mkdir(parents=True, exist_ok=True)
    return path
