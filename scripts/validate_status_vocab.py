import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import csv
from embedded_nn_contracts.status import VALID_STATUSES

rows = list(csv.DictReader((ROOT / "data/frozen_tables/all_board_model_results.csv").open()))
issues = [f"{r['board']}/{r['model']} invalid status {r['status']}" for r in rows if r["status"] not in VALID_STATUSES]
if issues:
    raise SystemExit("\n".join(issues))
print("status vocabulary: PASS")
