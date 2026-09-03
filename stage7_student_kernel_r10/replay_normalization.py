"""Independent exact Fock Gaussian normalization replay."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    z, x = sp.symbols("z x")
    gaussian_mgf = sp.exp(z**2 / 2)
    fock_R = sp.simplify(gaussian_mgf * sp.exp(-z**2 / 2))
    D = sp.simplify((fock_R**2 + fock_R.subs(z, -z)**2) / 2)
    payload = {"gaussian_mgf": str(gaussian_mgf), "fock_R": str(fock_R), "D_R": str(D), "R_residual": str(fock_R - 1), "D_residual": str(D - 1), "marker": "R10_GAUSSIAN_FOCK_NORMALIZATION_CORRECTED"}
    (RESULTS / "normalization.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload["marker"])
    print("R10_GAUSSIAN_R_RESIDUAL", payload["R_residual"])
    print("R10_GAUSSIAN_D_RESIDUAL", payload["D_residual"])


if __name__ == "__main__":
    main()
