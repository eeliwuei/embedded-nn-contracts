import csv
from pathlib import Path


def validate_pi_vulkan_routes(root: Path) -> list[str]:
    issues = []
    path = root / "data/frozen_tables/raspberry_pi_supplement_results.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if row["backend"] == "ncnn_vulkan":
            if row["decision"] != "no_retained_ncnn_vulkan_path":
                issues.append(f"unexpected Vulkan decision for {row['model']}: {row['decision']}")
            coverage = row.get("coverage", "")
            if "91 -> 168" in coverage and "crash" in row.get("note", "").lower():
                # Explicit crash wording is allowed; timing claim is not.
                continue
    return issues
