"""Small exact-arithmetic helpers for the angular Fisher audit."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, sp.Basic):
        return str(sp.factor(value))
    if isinstance(value, Path):
        return str(value)
    return value


def write_json(name: str, payload: dict[str, Any]) -> Path:
    path = RESULTS / name
    path.write_text(
        json.dumps(jsonable(payload), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def no_nonfinite(value: Any) -> bool:
    if isinstance(value, dict):
        return all(no_nonfinite(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return all(no_nonfinite(v) for v in value)
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, str):
        return value not in {"nan", "inf", "-inf", "NaN", "Infinity", "-Infinity"}
    return True

