"""Bounded runner for the R4 angular Fisher audit."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    scripts = [
        "derive_angular_geometry.py",
        "derive_first_odd_mode.py",
        "derive_fisher_budget.py",
        "optional_symmetrization.py",
        "audit_fisher_closure.py",
        "audit_results.py",
    ]
    for script in scripts:
        subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, check=True)
    print("ANGULAR_FISHER_R4_COMPLETED")


if __name__ == "__main__":
    main()

