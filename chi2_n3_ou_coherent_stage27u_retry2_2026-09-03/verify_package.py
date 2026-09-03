#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "PACKAGE_INTEGRITY.json"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    if not MANIFEST.exists():
        print("PACKAGE_VERIFY_FAILED missing PACKAGE_INTEGRITY.json")
        return 2
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    for rel, expected in data["files"].items():
        p = ROOT / rel
        if not p.is_file():
            failures.append(f"MISSING {rel}")
            continue
        got = sha256(p)
        if got != expected:
            failures.append(f"SHA256 {rel} expected={expected} got={got}")
    expected_paths = set(data["files"])
    actual_paths = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name != "PACKAGE_INTEGRITY.json" and "__pycache__" not in p.parts
    }
    extra = sorted(actual_paths - expected_paths)
    missing_from_tree = sorted(expected_paths - actual_paths)
    for rel in extra:
        failures.append(f"UNEXPECTED {rel}")
    for rel in missing_from_tree:
        if not any(x == f"MISSING {rel}" for x in failures):
            failures.append(f"MISSING {rel}")
    if failures:
        print("PACKAGE_VERIFY_FAILED")
        for x in failures:
            print(x)
        return 1
    print(f"STAGE27U_RETRY2_PACKAGE_VERIFY_OK files={len(expected_paths)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
