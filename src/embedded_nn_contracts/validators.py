import csv
from pathlib import Path

from .metrics import throughput_to_latency_ms


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def validate_final_results(root: Path) -> list[str]:
    issues = []
    rows = read_csv(root / "data/frozen_tables/all_board_model_results.csv")
    by_key = {(r["board"], r["model"]): r for r in rows}
    expected = {
        ("f746", "kws"): ("26.652", "retained"),
        ("f746", "vww"): ("8.386", "retained"),
        ("f746", "ic"): ("6.859", "retained"),
        ("f746", "ad"): ("396.286", "retained"),
        ("g0", "kws"): ("0.169", "dropped_noncompetitive"),
    }
    for key, (throughput, status) in expected.items():
        row = by_key.get(key)
        if not row:
            issues.append(f"missing final result row: {key}")
            continue
        if row["throughput_inf_sec"] != throughput:
            issues.append(f"{key} throughput expected {throughput}, got {row['throughput_inf_sec']}")
        if row["status"] != status:
            issues.append(f"{key} status expected {status}, got {row['status']}")
    return issues


def validate_canonical_values(root: Path) -> list[str]:
    issues = []
    rows = read_csv(root / "data/frozen_tables/all_board_model_results.csv")
    for row in rows:
        if row["board"] == "f746" and row["model"] == "ad":
            if row["throughput_inf_sec"] != "396.286":
                issues.append("F746 AD canonical value must be 396.286 inf/s")
        if row["board"] == "f746" and row["model"] == "vww":
            if row["throughput_inf_sec"] != "8.386":
                issues.append("F746 VWW final value must be 8.386 inf/s")
            if "8.290" in row.get("note", "") and "replaces" not in row.get("note", ""):
                issues.append("VWW 8.290 must be marked historical, not final")
    return issues


def validate_no_infsec_as_ms(root: Path, tolerance: float = 0.02) -> list[str]:
    issues = []
    rows = read_csv(root / "data/frozen_tables/all_board_model_results.csv")
    for row in rows:
        th = row.get("throughput_inf_sec", "")
        lat = row.get("latency_ms", "")
        if not th or not lat:
            continue
        expected = throughput_to_latency_ms(float(th))
        if abs(float(lat) - expected) > tolerance:
            issues.append(f"latency mismatch for {row['board']}/{row['model']}: {lat} vs {expected:.3f}")
    return issues


def validate_u575_not_source_retained(root: Path) -> list[str]:
    issues = []
    rows = read_csv(root / "data/frozen_tables/all_board_model_results.csv")
    for row in rows:
        if row["board"] == "u575" and row["status"] == "retained":
            issues.append(f"U575 {row['model']} must not be source-retained")
    return issues


def validate_g0_status(root: Path) -> list[str]:
    issues = []
    rows = read_csv(root / "data/frozen_tables/all_board_model_results.csv")
    by_key = {(r["board"], r["model"]): r for r in rows}
    if by_key.get(("g0", "ad"), {}).get("status") != "retained":
        issues.append("G0 AD must be retained in frozen table")
    if by_key.get(("g0", "kws"), {}).get("status") != "dropped_noncompetitive":
        issues.append("G0 KWS must be dropped_noncompetitive")
    for model in ("vww", "ic"):
        if by_key.get(("g0", model), {}).get("status") != "infeasible_on_board":
            issues.append(f"G0 {model} must be infeasible_on_board")
    return issues


def validate_all(root: Path) -> list[str]:
    issues = []
    for fn in [
        validate_final_results,
        validate_canonical_values,
        validate_no_infsec_as_ms,
        validate_u575_not_source_retained,
        validate_g0_status,
    ]:
        issues.extend(fn(root))
    return issues
