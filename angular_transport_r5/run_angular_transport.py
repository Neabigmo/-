"""Run the bounded angular-transport R5 audit."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main() -> None:
    for script in ("derive_bivariate_mixture.py", "derive_rotation_transport.py", "derive_missing_information.py", "derive_stage8_bridge.py", "audit_fisher_closure_final.py", "audit_results.py"):
        subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, check=True)
    print("ANGULAR_TRANSPORT_R5_COMPLETED")

if __name__ == "__main__":
    main()
