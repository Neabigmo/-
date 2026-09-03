from __future__ import annotations

import json

from common import result_dir


def main():
    out_dir = result_dir()
    data = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in out_dir.glob("*.json") if p.name != "audit_results.json"}
    text = json.dumps(data, ensure_ascii=False)
    assert "NaN" not in text and "Infinity" not in text
    required = ["posterior_triple.json", "conditional_q_moments.json", "moment_countermodel.json", "semigroup_bridge.json", "critical_kernel_audit.json"]
    assert all(name in data for name in required), sorted(data)
    assert all(v == "0" for v in data["conditional_q_moments.json"]["conditional_moment_residuals"].values())
    assert data["moment_countermodel.json"]["status"] == "EXACT_MOMENT_RELAXATION_COUNTERMODEL"
    assert data["critical_kernel_audit.json"]["status"] == "EXACT_CRITICAL_KERNEL_COUNTEREXAMPLE"
    out = {"status": "AUDIT_OK", "required_files": required, "result_files": sorted(data), "nan_inf_free": True, "derived_from_results": True}
    (out_dir / "audit_results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("POSTERIOR_LAPLACE_RESULTS_AUDIT_OK", out_dir / "audit_results.json")


if __name__ == "__main__":
    main()
