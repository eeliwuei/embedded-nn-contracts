#!/usr/bin/env bash
set -euo pipefail
echo "[INFO] Final frozen results are in data/frozen_tables/all_board_model_results.csv"
python3 scripts/validate_numbers.py
