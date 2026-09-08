from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, (path, needle)


def main() -> None:
    require("r154_escape_energy_audit/README.md", [
        "Theta_M(I)",
        "supercritical",
        "R154_AUDIT_COMPLETED",
    ])
    require("THEORY_ROUTE_FRAMEWORK.md", [
        "R154 真正剩余的超临界问题",
        "R154_CONCENTRATION_MATRIX_PASSED",
        "证据等级",
    ])
    require("PROJECT_WORKLOG_APPEND.md", [
        "R154 — Supercritical Escape-Energy / Christoffel Localisation",
        "R154_AUDIT_COMPLETED",
        "发表性判断仍为“无”",
    ])
    readme = (ROOT / "r155_global_publication_audit/README.md").read_text(encoding="utf-8")
    assert "全历史" in readme
    assert "可投稿结果" in readme
    assert "不能把本次网页中止记为" in readme
    print("R155_GLOBAL_SCOPE_RECORDED")
    print("R155_R154_ABORT_NOT_MATH_RESULT_PASSED")
    print("R155_PUBLICATION_AUDIT_REQUEST_RECORDED")
    print("R155_EVIDENCE_BOUNDARY_EXPLICIT")
    print("R155_AUDIT_COMPLETED")


if __name__ == "__main__":
    main()
