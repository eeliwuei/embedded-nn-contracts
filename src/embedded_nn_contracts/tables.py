import shutil
from pathlib import Path


def regenerate_tables(root: Path) -> None:
    out = root / "outputs/tables"
    out.mkdir(parents=True, exist_ok=True)
    copies = {
        "data/frozen_tables/all_board_model_results.csv": "final_results_table.csv",
        "data/frozen_tables/experiment_method_ledger.csv": "method_family_table.csv",
        "data/frozen_tables/experiment_failure_ledger.csv": "failure_taxonomy.csv",
    }
    for src, dst in copies.items():
        source = root / src
        if source.exists():
            shutil.copyfile(source, out / dst)
